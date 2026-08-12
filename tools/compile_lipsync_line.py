#!/usr/bin/env python3
"""Align dialogue audio, synthesize facial curves, and add them to a WKit GLB."""

from __future__ import annotations

import argparse
import copy
import json
import struct
from collections.abc import Sequence
from dataclasses import asdict
from pathlib import Path
from typing import Any

import numpy as np
from build_lipsync_corpus import text_to_phones
from build_lipsync_dataset import DEFAULT_PHONE_MODEL, CTCPhoneAligner, normalize_phones
from make_lipsync_ab_glb import read_glb, track_names, write_glb
from synthesize_lipsync_line import synthesize

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT / "generated/lipsync-corpus/templates/lipsync-templates.json"
BIN_CHUNK = 0x004E4942


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8-sig") as stream:
        return json.load(stream)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def frame_times(duration: float, frames_per_second: float) -> np.ndarray:
    regular = np.arange(0.0, duration, 1.0 / frames_per_second, dtype=np.float64)
    if not len(regular) or duration - regular[-1] > 1e-6:
        regular = np.append(regular, duration)
    else:
        regular[-1] = duration
    return regular


def apply_speech_window(
    times: np.ndarray,
    values: np.ndarray,
    speech_start: float,
    speech_end: float,
    anticipation_ms: float,
    release_ms: float,
) -> np.ndarray:
    """Fade generated controls around speech and guarantee neutral boundaries."""
    if values.shape[0] != len(times):
        raise ValueError("Curve matrix does not match the supplied times")
    if not len(times):
        return values.copy()
    anticipation = max(0.0, anticipation_ms / 1000.0)
    release = max(0.0, release_ms / 1000.0)
    duration = float(times[-1])
    attack_start = max(0.0, speech_start - anticipation)
    release_end = min(duration, speech_end + release)
    weights = np.ones(len(times), dtype=np.float64)
    if speech_start > attack_start:
        weights = np.minimum(
            weights,
            np.clip((times - attack_start) / (speech_start - attack_start), 0.0, 1.0),
        )
    else:
        weights[times < speech_start] = 0.0
    if release_end > speech_end:
        weights = np.minimum(
            weights,
            np.clip((release_end - times) / (release_end - speech_end), 0.0, 1.0),
        )
    else:
        weights[times > speech_end] = 0.0
    weights[0] = 0.0
    weights[-1] = 0.0
    return values * weights[:, None]


def zero_track_prefixes(
    curve_names: Sequence[str],
    values: np.ndarray,
    prefixes: Sequence[str],
) -> tuple[np.ndarray, list[str]]:
    """Zero rig-incompatible generated controls selected by name prefix."""
    normalized = tuple(prefix.casefold() for prefix in prefixes if prefix)
    if not normalized:
        return values, []
    selected = [
        index
        for index, name in enumerate(curve_names)
        if name.casefold().startswith(normalized)
    ]
    masked = values.copy()
    if selected:
        masked[:, selected] = 0.0
    return masked, [curve_names[index] for index in selected]


def keep_duration_marker_channel(animation: dict[str, Any]) -> int:
    """Strip donor skeletal animation while keeping one no-op duration channel."""
    channels = animation.get("channels", [])
    samplers = animation.get("samplers", [])
    removed = len(channels)
    if channels and samplers:
        marker_channel = copy.deepcopy(channels[0])
        marker_sampler = copy.deepcopy(samplers[int(marker_channel["sampler"])])
        marker_channel["sampler"] = 0
        animation["channels"] = [marker_channel]
        animation["samplers"] = [marker_sampler]
        return removed - 1
    if samplers:
        animation["samplers"] = [copy.deepcopy(samplers[0])]
    animation["channels"] = []
    return removed


def append_float_accessor(
    document: dict[str, Any],
    chunks: list[tuple[int, bytes]],
    samples: Sequence[float] | Sequence[Sequence[float]],
    accessor_type: str,
    *,
    name: str,
) -> int:
    """Append tightly packed float samples and return their accessor index."""
    widths = {"SCALAR": 1, "VEC3": 3, "VEC4": 4}
    width = widths[accessor_type]
    if accessor_type == "SCALAR":
        vectors = [[float(value)] for value in samples]  # type: ignore[arg-type]
    else:
        vectors = [[float(value) for value in sample] for sample in samples]  # type: ignore[union-attr]
    if not vectors or any(len(vector) != width for vector in vectors):
        raise ValueError(f"Invalid {accessor_type} samples")

    chunk_index = next((index for index, item in enumerate(chunks) if item[0] == BIN_CHUNK), None)
    if chunk_index is None:
        raise ValueError("GLB has no binary chunk")
    payload = chunks[chunk_index][1]
    padding = b"\0" * ((-len(payload)) % 4)
    byte_offset = len(payload) + len(padding)
    flattened = [value for vector in vectors for value in vector]
    payload = payload + padding + struct.pack(f"<{len(flattened)}f", *flattened)
    chunks[chunk_index] = (BIN_CHUNK, payload)

    document.setdefault("bufferViews", []).append(
        {
            "buffer": 0,
            "byteLength": 4 * len(flattened),
            "byteOffset": byte_offset,
        }
    )
    accessor = {
        "name": name,
        "bufferView": len(document["bufferViews"]) - 1,
        "componentType": 5126,
        "count": len(vectors),
        "max": [max(vector[column] for vector in vectors) for column in range(width)],
        "min": [min(vector[column] for vector in vectors) for column in range(width)],
        "type": accessor_type,
    }
    document.setdefault("accessors", []).append(accessor)
    document["buffers"][0]["byteLength"] = len(payload)
    return len(document["accessors"]) - 1


def build_neutral_skeletal_channels(
    document: dict[str, Any],
    chunks: list[tuple[int, bytes]],
    animation_name: str,
    duration: float,
) -> dict[str, Any]:
    """Encode a complete zero-additive skeleton using native constant keys.

    WKit maps STEP glTF channels to CR2W constAnimKeys. The engine requires a
    complete constant reference set; deleting the channels or representing a
    one-key pose as LINEAR produces buffers that import successfully but
    collapse the face at runtime. One harmless, two-key translation channel is
    retained solely to carry the requested animation duration.
    """
    animation = next(
        (item for item in document.get("animations", []) if item.get("name") == animation_name),
        None,
    )
    if animation is None:
        raise ValueError(f"Animation not found: {animation_name}")
    nodes = document.get("nodes", [])
    channels = animation.get("channels", [])
    if not channels:
        raise ValueError(f"Animation has no skeletal channels: {animation_name}")

    defaults = {
        "translation": ([0.0, 0.0, 0.0], "VEC3"),
        "rotation": ([0.0, 0.0, 0.0, 1.0], "VEC4"),
        "scale": ([1.0, 1.0, 1.0], "VEC3"),
    }
    marker_channel = next(
        (
            channel
            for channel in channels
            if channel.get("target", {}).get("path") == "translation"
            and nodes[int(channel["target"]["node"])].get("name") == "face_root_JNT"
        ),
        next(
            channel
            for channel in channels
            if channel.get("target", {}).get("path") == "translation"
        ),
    )
    zero_time = append_float_accessor(
        document, chunks, [0.0], "SCALAR", name="Ghostline.Neutral.Time"
    )
    duration_times = append_float_accessor(
        document,
        chunks,
        [0.0, float(duration)],
        "SCALAR",
        name="Ghostline.Neutral.Duration",
    )

    neutralized = 0
    for channel in channels:
        target = channel.get("target", {})
        path = target.get("path")
        node_index = target.get("node")
        if path not in defaults or not isinstance(node_index, int) or not 0 <= node_index < len(nodes):
            raise ValueError(f"Unsupported skeletal channel in {animation_name}: {target}")
        default, accessor_type = defaults[path]
        rest_value = [float(value) for value in nodes[node_index].get(path, default)]
        is_marker = channel is marker_channel
        output = append_float_accessor(
            document,
            chunks,
            [rest_value, rest_value] if is_marker else [rest_value],
            accessor_type,
            name=f"Ghostline.Neutral.{nodes[node_index].get('name', node_index)}.{path}",
        )
        sampler = animation["samplers"][int(channel["sampler"])]
        sampler["input"] = duration_times if is_marker else zero_time
        sampler["output"] = output
        sampler["interpolation"] = "LINEAR" if is_marker else "STEP"
        neutralized += 1
    return {
        "neutralized_skeletal_channels": neutralized,
        "constant_skeletal_channels": neutralized - 1,
        "duration_marker_node": nodes[int(marker_channel["target"]["node"])].get("name"),
        "duration_marker_path": marker_channel["target"]["path"],
    }


def replace_lipsync_tracks(
    document: dict[str, Any],
    source_name: str,
    output_name: str,
    curve_names: Sequence[str],
    times: np.ndarray,
    values: np.ndarray,
    *,
    strip_donor_skeleton: bool = False,
    clear_donor_controls: bool = False,
) -> dict[str, int]:
    """Duplicate a clip and replace its generated lipsync/output-weight tracks."""
    if values.shape != (len(times), len(curve_names)):
        raise ValueError("Curve matrix does not match the supplied times and track names")
    names = track_names(document)
    name_to_index = {name: index for index, name in enumerate(names)}
    missing = [name for name in curve_names if name not in name_to_index]
    if missing:
        raise ValueError(f"Donor rig is missing model track: {missing[0]}")

    animations = document.get("animations", [])
    source = next((item for item in animations if item.get("name") == source_name), None)
    if source is None:
        raise ValueError(f"Source animation not found: {source_name}")
    if any(item.get("name") == output_name for item in animations):
        raise ValueError(f"Animation already exists: {output_name}")

    generated_indices = {name_to_index[name] for name in curve_names}
    # Vanilla lipsync clips pair each *LipsyncPoseOutput curve with a negative
    # AnimOverrideWeight curve. Recreate that pair so an underlying facial
    # animation cannot fight the generated mouth pose.
    override_pairs: list[tuple[int, int]] = []
    for column, name in enumerate(curve_names):
        suffix = "LipsyncPoseOutput"
        if name.endswith(suffix):
            override = name[: -len(suffix)] + "AnimOverrideWeight"
            if override in name_to_index:
                override_pairs.append((column, name_to_index[override]))
    generated_output_indices = generated_indices | {
        track_index for _, track_index in override_pairs
    }

    cleared_indices = {
        index
        for index, name in enumerate(names)
        if name.endswith(("LipsyncPoseOutput", "AnimOverrideWeight"))
    }
    cleared_indices.update(generated_indices)

    duplicate = copy.deepcopy(source)
    duplicate["name"] = output_name
    extras = duplicate.setdefault("extras", {})
    donor_track_keys = len(extras.get("trackKeys", [])) + len(
        extras.get("constTrackKeys", [])
    )
    retained_dynamic = (
        []
        if clear_donor_controls
        else [
            key
            for key in extras.get("trackKeys", [])
            if int(key.get("trackIndex", -1)) not in cleared_indices
        ]
    )
    retained_constant = (
        [
            {"trackIndex": index, "time": 0.0, "value": 0.0}
            for index in range(len(names))
            if index not in generated_output_indices
        ]
        if clear_donor_controls
        else [
            key
            for key in extras.get("constTrackKeys", [])
            if int(key.get("trackIndex", -1)) not in cleared_indices
        ]
    )
    generated: list[dict[str, float | int]] = []
    for column, name in enumerate(curve_names):
        track_index = name_to_index[name]
        for time, value in zip(times, values[:, column]):
            generated.append(
                {"trackIndex": track_index, "time": float(time), "value": float(value)}
            )
    for column, track_index in override_pairs:
        for time, value in zip(times, values[:, column]):
            generated.append(
                {"trackIndex": track_index, "time": float(time), "value": -float(value)}
            )
    generated.sort(key=lambda key: (int(key["trackIndex"]), float(key["time"])))
    if strip_donor_skeleton:
        extras["trackKeys"] = generated
        extras["constTrackKeys"] = []
        removed_skeletal_channels = keep_duration_marker_channel(duplicate)
        removed_donor_track_keys = donor_track_keys
    else:
        extras["trackKeys"] = retained_dynamic + generated
        extras["constTrackKeys"] = retained_constant
        removed_skeletal_channels = 0
        removed_donor_track_keys = (
            donor_track_keys
            if clear_donor_controls
            else donor_track_keys - len(retained_dynamic) - len(retained_constant)
        )
    animations.append(duplicate)
    return {
        "frames": len(times),
        "generated_tracks": len(curve_names),
        "override_tracks": len(override_pairs),
        "cleared_donor_tracks": len(cleared_indices),
        "removed_donor_track_keys": removed_donor_track_keys,
        "cleared_all_donor_controls": clear_donor_controls,
        "neutral_constant_tracks": len(retained_constant) if clear_donor_controls else 0,
        "removed_skeletal_channels": removed_skeletal_channels,
        "generated_keys": len(generated),
    }


def set_animation_duration(
    document: dict[str, Any],
    chunks: list[tuple[int, bytes]],
    animation_name: str,
    duration: float,
) -> None:
    """Give a newly duplicated animation its own glTF duration marker."""
    animation = next(
        (item for item in document.get("animations", []) if item.get("name") == animation_name),
        None,
    )
    if animation is None or not animation.get("samplers"):
        raise ValueError(f"Animation has no sampler available for duration: {animation_name}")
    chunk_index = next((index for index, item in enumerate(chunks) if item[0] == BIN_CHUNK), None)
    if chunk_index is None:
        raise ValueError("GLB has no binary chunk")

    payload = chunks[chunk_index][1]
    padding = b"\0" * ((-len(payload)) % 4)
    byte_offset = len(payload) + len(padding)
    payload = payload + padding + struct.pack("<f", duration)
    chunks[chunk_index] = (BIN_CHUNK, payload)

    buffer_view = {"buffer": 0, "byteLength": 4, "byteOffset": byte_offset}
    document.setdefault("bufferViews", []).append(buffer_view)
    accessor = {
        "name": "Ghostline.Animation.Duration",
        "bufferView": len(document["bufferViews"]) - 1,
        "componentType": 5126,
        "count": 1,
        "max": [duration],
        "min": [duration],
        "type": "SCALAR",
    }
    document.setdefault("accessors", []).append(accessor)
    animation["samplers"][0]["input"] = len(document["accessors"]) - 1
    document["buffers"][0]["byteLength"] = len(payload)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio", type=Path)
    parser.add_argument("donor_glb", type=Path)
    parser.add_argument("output_glb", type=Path)
    parser.add_argument("--text", required=True)
    parser.add_argument(
        "--phones",
        help="Optional space-separated ARPAbet pronunciation overriding automatic G2P",
    )
    parser.add_argument("--locstring", required=True, type=int)
    parser.add_argument("--source", required=True, help="Donor animation name")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--phone-model", default=DEFAULT_PHONE_MODEL)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--fps", type=float, default=30.0)
    parser.add_argument(
        "--context-weight",
        type=float,
        default=0.7,
        help="Strength of learned previous/next-phone amplitude effects.",
    )
    parser.add_argument("--fallback-transition-ms", type=float, default=60.0)
    parser.add_argument("--maximum-transition-ms", type=float, default=120.0)
    parser.add_argument("--anticipation-ms", type=float, default=80.0)
    parser.add_argument("--release-ms", type=float, default=80.0)
    parser.add_argument(
        "--strip-donor-skeleton",
        action="store_true",
        help="Experimental track-only output; matching-rig donors should retain their pose channels.",
    )
    parser.add_argument(
        "--clear-donor-controls",
        action="store_true",
        help="Discard donor facial control keys while preserving skeletal/reference channels.",
    )
    parser.add_argument(
        "--neutral-skeleton",
        action="store_true",
        help="Build a complete STEP-constant zero-additive skeleton for a reusable clean container.",
    )
    parser.add_argument(
        "--zero-track-prefix",
        action="append",
        default=[],
        help="Zero generated controls whose names begin with this prefix; repeat as needed.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.fps <= 0:
        raise ValueError("--fps must be positive")
    if args.strip_donor_skeleton and args.neutral_skeleton:
        raise ValueError("--strip-donor-skeleton and --neutral-skeleton are incompatible")
    phones = normalize_phones(args.phones.split()) if args.phones else text_to_phones(args.text)
    aligner = CTCPhoneAligner(args.phone_model, args.device)
    alignment, duration, device = aligner.align(args.audio, phones)
    report: dict[str, Any] = {
        "animation_name": f"f_{args.locstring:016X}",
        "locstring_id": str(args.locstring),
        "text": args.text,
        "audio_path": str(args.audio.resolve()),
        "audio_duration": duration,
        "animation_duration": duration,
        "phones": phones,
        "alignment": [asdict(item) for item in alignment],
        "alignment_score": float(np.mean([item.score for item in alignment])),
        "device": device,
        "phone_model": args.phone_model,
        "template_model": str(args.model.resolve()),
    }
    model = read_json(args.model)
    times = frame_times(duration, args.fps)
    values, _ = synthesize(
        model,
        report,
        times,
        args.context_weight,
        args.fallback_transition_ms,
        args.maximum_transition_ms,
    )
    values, zeroed_tracks = zero_track_prefixes(
        model["tracks"], values, args.zero_track_prefix
    )
    report["zeroed_tracks"] = zeroed_tracks
    if alignment:
        values = apply_speech_window(
            times,
            values,
            alignment[0].start,
            alignment[-1].end,
            args.anticipation_ms,
            args.release_ms,
        )
    document, chunks = read_glb(args.donor_glb)
    statistics = replace_lipsync_tracks(
        document,
        args.source,
        report["animation_name"],
        model["tracks"],
        times,
        values,
        strip_donor_skeleton=args.strip_donor_skeleton,
        clear_donor_controls=args.clear_donor_controls,
    )
    if args.neutral_skeleton:
        statistics.update(
            build_neutral_skeletal_channels(
                document, chunks, report["animation_name"], duration
            )
        )
    else:
        set_animation_duration(document, chunks, report["animation_name"], duration)
    write_glb(args.output_glb, document, chunks)
    report.update(statistics)
    report["donor_glb"] = str(args.donor_glb.resolve())
    report["source_animation"] = args.source
    report["output_glb"] = str(args.output_glb.resolve())
    report_path = args.report or args.output_glb.with_suffix(".alignment.json")
    write_json(report_path, report)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
