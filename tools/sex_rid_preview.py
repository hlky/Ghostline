"""Decode scene RID body tracks and build neutral-proxy review previews."""

from __future__ import annotations

import argparse
import base64
import json
import math
import re
import shutil
import struct
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from sex_rid_catalog import preview_slug


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKELETON = ROOT / "braindance/rigs/man_base.skeleton.json"
DEFAULT_BLENDER = Path(r"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe")
BLENDER_SCRIPT = ROOT / "tools/sex_rid_preview_blender.py"
PREVIEW_SCHEMA_VERSION = 1
ACTOR_COLORS = (
    [0.13, 0.75, 0.88, 1.0],
    [1.0, 0.32, 0.48, 1.0],
    [0.96, 0.72, 0.18, 1.0],
    [0.58, 0.38, 0.95, 1.0],
    [0.3, 0.85, 0.42, 1.0],
)
OTHER_COLOR = ACTOR_COLORS[0]
PLAYER_COLOR = ACTOR_COLORS[1]


class RidPreviewError(RuntimeError):
    """Raised when a RID cannot satisfy the preview contract."""


@dataclass(frozen=True)
class SimdAnimation:
    duration: float
    frame_count: int
    translations: list[list[list[float]]]
    rotations: list[list[list[float]]]
    scales: list[list[list[float]]]
    tracks: list[list[float]]
    bytes_consumed: int
    payload_bytes: int


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RidPreviewError(f"Cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RidPreviewError(f"Expected a JSON object in {path}")
    return value


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def _root(document: dict[str, Any]) -> dict[str, Any]:
    data = document.get("Data")
    root = data.get("RootChunk") if isinstance(data, dict) else None
    if not isinstance(root, dict) or root.get("$type") != "scnRidResource":
        raise RidPreviewError("Expected a scnRidResource RootChunk")
    return root


def _cname(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict) and isinstance(value.get("$value"), str):
        return value["$value"]
    return None


def _signature(value: dict[str, Any]) -> str | None:
    tag = value.get("tag")
    return _cname(tag.get("signature")) if isinstance(tag, dict) else None


def select_human_actor_signatures(document: dict[str, Any], rid_id: str) -> list[str]:
    """Choose the uncluttered human pair for a neutral RID preview."""
    available = [
        signature
        for actor in _root(document).get("actors", [])
        if isinstance(actor, dict)
        and (signature := _signature(actor))
        and isinstance(actor.get("animations"), list)
        and actor["animations"]
    ]
    available_set = set(available)
    path = rid_id.casefold()

    preferred: list[list[str]] = []
    if "sex_judy_layout" in path:
        preferred = [["female_average"], ["femalePlayerFpp"]]
    elif "rivers_bedroom" in path:
        preferred = [["app_naked__river_ward_controlRig"], ["female_player_1"]]
    elif "river" in path:
        preferred = [["app_default__river_ward_controlRig"], ["female_player_1"]]
    elif "destructive_tendencies" in path:
        preferred = [["male_average_3"], ["player"]]
    elif "panzer__sex_scene" in path:
        preferred = [["panam_controlRig"], ["man_player_1"]]
    elif "panzer__jack_in" in path:
        preferred = [
            ["npc_panam_1", "npc_panam", "female_average"],
            ["man_player_dual_fpp_1", "man_player_1", "male_average"],
        ]
    elif "female_npc" in path or re.search(r"_[0-9]+s_f\.scenerid$", path):
        preferred = [
            ["female_average", "woman_average_1", "male_average"],
            ["player", "male_player", "femalePlayerFpp"],
        ]
    elif "male_npc" in path or re.search(r"_[0-9]+s_m\.scenerid$", path):
        preferred = [
            ["male_average"],
            ["player", "femalePlayerFpp", "female_player_1"],
        ]
    selected = [
        match
        for candidates in preferred
        if (match := next((item for item in candidates if item in available_set), None))
    ]
    if selected:
        return selected

    human = [
        signature
        for signature in available
        if any(
            token in signature.casefold()
            for token in ("player", "female", "male", "woman", "man", "panam", "river")
        )
        and not any(
            token in signature.casefold()
            for token in ("personal_link", "basilisk", "item_", "doors", "food_")
        )
    ]
    partner = next(
        (signature for signature in human if "player" not in signature.casefold()),
        None,
    )
    player = next(
        (signature for signature in human if "player" in signature.casefold()), None
    )
    return [signature for signature in (partner, player) if signature] or human[:2]


def actor_preview_color(signature: str, fallback_index: int) -> list[float]:
    """Keep Player pink and the primary counterpart cyan in every preview."""
    if "player" in signature.casefold():
        return list(PLAYER_COLOR)
    if fallback_index < 2:
        return list(OTHER_COLOR)
    return list(ACTOR_COLORS[fallback_index % len(ACTOR_COLORS)])


def _buffer_bytes(buffer: dict[str, Any]) -> bytes:
    deferred = buffer.get("defferedBuffer") or buffer.get("inplaceCompressedBuffer")
    encoded = deferred.get("Bytes") if isinstance(deferred, dict) else None
    if not isinstance(encoded, str):
        raise RidPreviewError("Animation buffer has no deferred Bytes payload")
    try:
        return base64.b64decode(encoded, validate=True)
    except ValueError as exc:
        raise RidPreviewError("Animation buffer payload is invalid base64") from exc


def _normalize_quaternion(value: list[float]) -> list[float]:
    length = math.sqrt(sum(component * component for component in value))
    if length < 1e-10:
        return [0.0, 0.0, 0.0, 1.0]
    return [component / length for component in value]


def _take_floats(payload: bytes, offset: int, count: int) -> tuple[list[float], int]:
    size = count * 4
    if offset + size > len(payload):
        raise RidPreviewError("SIMD payload ended while reading floats")
    return list(struct.unpack_from(f"<{count}f", payload, offset)), offset + size


def decode_simd_buffer(buffer: dict[str, Any]) -> SimdAnimation:
    """Port WolvenKit's pinned SIMD decoder into a review-friendly shape."""
    if buffer.get("$type") != "animAnimationBufferSimd":
        raise RidPreviewError(
            f"Expected animAnimationBufferSimd, got {buffer.get('$type')}"
        )
    payload = _buffer_bytes(buffer)
    frames = int(buffer["numFrames"])
    joints = int(buffer["numJoints"])
    extra_joints = int(buffer.get("numExtraJoints", 0))
    tracks_count = int(buffer.get("numTracks", 0))
    eval_count = int(buffer.get("numTranslationsToEvalAlignedToSimd", 0))
    copy_count = int(buffer.get("numTranslationsToCopy", 0))
    quantization_bits = int(buffer.get("quantizationBits", 0))
    duration = float(buffer["duration"])
    if frames < 2 or joints < 1 or extra_joints > joints:
        raise RidPreviewError("SIMD buffer has invalid frame/joint cardinality")
    aligned_joints = (joints - extra_joints + 3) & ~3
    rotations = [
        [[0.0, 0.0, 0.0, 1.0] for _joint in range(joints)] for _frame in range(frames)
    ]
    offset = 0
    if quantization_bits:
        if quantization_bits > 16:
            raise RidPreviewError(
                f"Unsupported SIMD quantization width {quantization_bits}"
            )
        total_values = ((frames * aligned_joints * 3) + 3) & ~3
        compressed_size = total_values * quantization_bits // 8
        compressed_size = (compressed_size + 15) & ~15
        if compressed_size > len(payload):
            raise RidPreviewError("SIMD rotation payload is truncated")
        mask = (1 << quantization_bits) - 1
        decompressed: list[float] = []
        for index in range(total_values):
            bit_offset = index * quantization_bits
            byte_offset = bit_offset // 8
            shift = bit_offset % 8
            packed = int.from_bytes(
                payload[byte_offset : byte_offset + 4].ljust(4, b"\0"), "little"
            )
            decompressed.append((((packed >> shift) & mask) / mask * 2.0) - 1.0)
        for frame in range(frames):
            for joint_block in range(0, aligned_joints, 4):
                base = frame * aligned_joints * 3 + joint_block * 3
                for lane in range(4):
                    joint = joint_block + lane
                    if joint >= joints:
                        continue
                    x = decompressed[base + lane]
                    y = decompressed[base + 4 + lane]
                    z = decompressed[base + 8 + lane]
                    dot = x * x + y * y + z * z
                    multiplier = math.sqrt(max(0.0, 2.0 - dot))
                    rotations[frame][joint] = _normalize_quaternion(
                        [x * multiplier, y * multiplier, z * multiplier, 1.0 - dot]
                    )
        offset = compressed_size
    else:
        for frame in range(frames):
            for joint_block in range(0, aligned_joints, 4):
                values, offset = _take_floats(payload, offset, 16)
                for lane in range(min(4, joints - joint_block)):
                    rotations[frame][joint_block + lane] = _normalize_quaternion(
                        [
                            values[lane],
                            values[4 + lane],
                            values[8 + lane],
                            values[12 + lane],
                        ]
                    )

    eval_values, offset = _take_floats(payload, offset, frames * eval_count * 3)
    scales = [[[1.0, 1.0, 1.0] for _joint in range(joints)] for _frame in range(frames)]
    if bool(int(buffer.get("isScaleConstant", 0))):
        values, offset = _take_floats(payload, offset, 4)
        scale = [values[0], values[1], values[2]]
        for frame in range(frames):
            scales[frame] = [list(scale) for _joint in range(joints)]
    else:
        values, offset = _take_floats(payload, offset, frames * aligned_joints * 3)
        for frame in range(frames):
            for joint_block in range(0, aligned_joints, 4):
                base = frame * aligned_joints * 3 + joint_block * 3
                for lane in range(min(4, joints - joint_block)):
                    scales[frame][joint_block + lane] = [
                        values[base + lane],
                        values[base + 4 + lane],
                        values[base + 8 + lane],
                    ]

    tracks = [[0.0 for _track in range(tracks_count)] for _frame in range(frames)]
    if tracks_count:
        if bool(int(buffer.get("isTrackConstant", 0))):
            values, offset = _take_floats(payload, offset, 1)
            tracks = [
                [values[0] for _track in range(tracks_count)]
                for _frame in range(frames)
            ]
        else:
            aligned_tracks = (tracks_count + 3) & ~3
            for frame in range(frames):
                values, offset = _take_floats(payload, offset, aligned_tracks)
                tracks[frame] = values[:tracks_count]

    copy_positions: list[list[float]] = []
    for _index in range(copy_count):
        values, offset = _take_floats(payload, offset, 3)
        copy_positions.append(values)
    index_bytes = (copy_count + eval_count) * 2
    if offset + index_bytes > len(payload):
        raise RidPreviewError("SIMD payload ended while reading translation indices")
    copy_indices = (
        list(struct.unpack_from(f"<{copy_count}h", payload, offset))
        if copy_count
        else []
    )
    offset += copy_count * 2
    eval_indices = (
        list(struct.unpack_from(f"<{eval_count}h", payload, offset))
        if eval_count
        else []
    )
    offset += eval_count * 2

    translations = [
        [[0.0, 0.0, 0.0] for _joint in range(joints)] for _frame in range(frames)
    ]
    for frame in range(frames):
        for eval_block in range(0, eval_count, 4):
            base = frame * eval_count * 3 + eval_block * 3
            for lane in range(min(4, eval_count - eval_block)):
                joint = eval_indices[eval_block + lane]
                if 0 <= joint < joints:
                    translations[frame][joint] = [
                        eval_values[base + lane],
                        eval_values[base + 4 + lane],
                        eval_values[base + 8 + lane],
                    ]
        for index, joint in enumerate(copy_indices):
            if 0 <= joint < joints:
                translations[frame][joint] = list(copy_positions[index])
    return SimdAnimation(
        duration=duration,
        frame_count=frames,
        translations=translations,
        rotations=rotations,
        scales=scales,
        tracks=tracks,
        bytes_consumed=offset,
        payload_bytes=len(payload),
    )


def _compressed_rotation(x: float, y: float, z: float, w_negative: bool) -> list[float]:
    dot = x * x + y * y + z * z
    multiplier = math.sqrt(max(0.0, 2.0 - dot))
    w = 1.0 - dot
    if w_negative:
        w = -w
    return _normalize_quaternion([x * multiplier, y * multiplier, z * multiplier, w])


def _sample_keys(
    keys: list[tuple[float, list[float]]],
    time: float,
    default: list[float],
    *,
    quaternion: bool = False,
) -> list[float]:
    if not keys:
        return list(default)
    if len(keys) == 1 or time <= keys[0][0]:
        return list(keys[0][1])
    if time >= keys[-1][0]:
        return list(keys[-1][1])
    for index in range(1, len(keys)):
        right_time, right = keys[index]
        if time > right_time:
            continue
        left_time, left = keys[index - 1]
        span = right_time - left_time
        factor = 0.0 if span <= 1e-10 else (time - left_time) / span
        if quaternion and sum(a * b for a, b in zip(left, right)) < 0.0:
            right = [-component for component in right]
        value = [
            left[axis] + (right[axis] - left[axis]) * factor
            for axis in range(len(left))
        ]
        return _normalize_quaternion(value) if quaternion else value
    return list(keys[-1][1])


def decode_compressed_buffer(buffer: dict[str, Any]) -> SimdAnimation:
    """Port WolvenKit's animAnimationBufferCompressed key reader."""
    if buffer.get("$type") != "animAnimationBufferCompressed":
        raise RidPreviewError(
            f"Expected animAnimationBufferCompressed, got {buffer.get('$type')}"
        )
    payload = _buffer_bytes(buffer)
    duration = float(buffer["duration"])
    frames = int(buffer["numFrames"])
    joints = int(buffer["numJoints"])
    tracks_count = int(buffer.get("numTracks", 0))
    if frames < 1 or joints < 1 or duration < 0.0:
        raise RidPreviewError("Compressed buffer has invalid frame/joint cardinality")

    animated: list[dict[int, list[tuple[float, list[float]]]]] = [
        {} for _component in range(3)
    ]
    constant: list[dict[int, list[tuple[float, list[float]]]]] = [
        {} for _component in range(3)
    ]
    offset = 0

    def add_key(
        target: list[dict[int, list[tuple[float, list[float]]]]],
        time_raw: int,
        packed: int,
        values: list[float],
    ) -> None:
        component = (packed & 0x6000) >> 13
        joint = packed & 0x1FFF
        if component > 2 or joint >= joints:
            raise RidPreviewError(
                f"Compressed key targets invalid component/joint {component}/{joint}"
            )
        if component == 1:
            values = _compressed_rotation(
                values[0], values[1], values[2], bool(packed & 0x8000)
            )
        time = time_raw / 65535.0 * duration
        target[component].setdefault(joint, []).append((time, values))

    for _index in range(int(buffer.get("numAnimKeys", 0))):
        if offset + 10 > len(payload):
            raise RidPreviewError("Compressed payload ended in quantized keys")
        time_raw, packed, x, y, z = struct.unpack_from("<5H", payload, offset)
        offset += 10
        add_key(
            animated,
            time_raw,
            packed,
            [component / 65535.0 * 2.0 - 1.0 for component in (x, y, z)],
        )
    for _index in range(int(buffer.get("numAnimKeysRaw", 0))):
        if offset + 16 > len(payload):
            raise RidPreviewError("Compressed payload ended in raw keys")
        time_raw, packed, x, y, z = struct.unpack_from("<HHfff", payload, offset)
        offset += 16
        add_key(animated, time_raw, packed, [x, y, z])
    for _index in range(int(buffer.get("numConstAnimKeys", 0))):
        if offset + 16 > len(payload):
            raise RidPreviewError("Compressed payload ended in constant keys")
        packed, time_raw, x, y, z = struct.unpack_from("<HHfff", payload, offset)
        offset += 16
        add_key(constant, time_raw, packed, [x, y, z])

    track_key_count = int(buffer.get("numTrackKeys", 0))
    const_track_key_count = int(buffer.get("numConstTrackKeys", 0))
    track_bytes = (track_key_count + const_track_key_count) * 8
    if offset + track_bytes > len(payload):
        raise RidPreviewError("Compressed payload ended in track keys")
    offset += track_bytes

    for collection in (animated, constant):
        for channels in collection:
            for keys in channels.values():
                keys.sort(key=lambda key: key[0])
    translations = []
    rotations = []
    scales = []
    for frame in range(frames):
        time = 0.0 if frames == 1 else duration * frame / (frames - 1)
        frame_translations = []
        frame_rotations = []
        frame_scales = []
        for joint in range(joints):
            frame_translations.append(
                _sample_keys(
                    animated[0].get(joint) or constant[0].get(joint, []),
                    time,
                    [0.0, 0.0, 0.0],
                )
            )
            frame_rotations.append(
                _sample_keys(
                    animated[1].get(joint) or constant[1].get(joint, []),
                    time,
                    [0.0, 0.0, 0.0, 1.0],
                    quaternion=True,
                )
            )
            frame_scales.append(
                _sample_keys(
                    animated[2].get(joint) or constant[2].get(joint, []),
                    time,
                    [1.0, 1.0, 1.0],
                )
            )
        translations.append(frame_translations)
        rotations.append(frame_rotations)
        scales.append(frame_scales)
    return SimdAnimation(
        duration=duration,
        frame_count=frames,
        translations=translations,
        rotations=rotations,
        scales=scales,
        tracks=[[0.0 for _track in range(tracks_count)] for _frame in range(frames)],
        bytes_consumed=offset,
        payload_bytes=len(payload),
    )


def _quat_multiply(left: list[float], right: list[float]) -> list[float]:
    lx, ly, lz, lw = left
    rx, ry, rz, rw = right
    return _normalize_quaternion(
        [
            lw * rx + lx * rw + ly * rz - lz * ry,
            lw * ry - lx * rz + ly * rw + lz * rx,
            lw * rz + lx * ry - ly * rx + lz * rw,
            lw * rw - lx * rx - ly * ry - lz * rz,
        ]
    )


def _quat_rotate(rotation: list[float], value: list[float]) -> list[float]:
    x, y, z, w = rotation
    vx, vy, vz = value
    tx = 2.0 * (y * vz - z * vy)
    ty = 2.0 * (z * vx - x * vz)
    tz = 2.0 * (x * vy - y * vx)
    return [
        vx + w * tx + (y * tz - z * ty),
        vy + w * ty + (z * tx - x * tz),
        vz + w * tz + (x * ty - y * tx),
    ]


def _model_positions(
    animation: SimdAnimation,
    parents: list[int],
    offset_translation: list[float],
    offset_rotation: list[float],
) -> list[list[list[float]]]:
    joint_count = len(parents)
    result: list[list[list[float]]] = []
    for frame in range(animation.frame_count):
        positions = [[0.0, 0.0, 0.0] for _joint in range(joint_count)]
        rotations = [[0.0, 0.0, 0.0, 1.0] for _joint in range(joint_count)]
        scales = [[1.0, 1.0, 1.0] for _joint in range(joint_count)]
        for joint, parent in enumerate(parents):
            local_position = animation.translations[frame][joint]
            local_rotation = animation.rotations[frame][joint]
            local_scale = animation.scales[frame][joint]
            if parent < 0:
                position = local_position
                rotation = local_rotation
                scale = local_scale
            else:
                scaled = [
                    local_position[index] * scales[parent][index] for index in range(3)
                ]
                rotated = _quat_rotate(rotations[parent], scaled)
                position = [
                    positions[parent][index] + rotated[index] for index in range(3)
                ]
                rotation = _quat_multiply(rotations[parent], local_rotation)
                scale = [
                    scales[parent][index] * local_scale[index] for index in range(3)
                ]
            positions[joint] = position
            rotations[joint] = rotation
            scales[joint] = scale
        placed = []
        for position in positions:
            rotated = _quat_rotate(offset_rotation, position)
            placed.append(
                [offset_translation[index] + rotated[index] for index in range(3)]
            )
        result.append(placed)
    return result


def _offset(clip: dict[str, Any]) -> tuple[list[float], list[float]]:
    value = clip.get("offset")
    position = value.get("position") if isinstance(value, dict) else None
    orientation = value.get("orientation") if isinstance(value, dict) else None
    if not isinstance(position, dict) or not isinstance(orientation, dict):
        return [0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]
    return (
        [float(position.get(axis, 0.0)) for axis in ("X", "Y", "Z")],
        _normalize_quaternion(
            [float(orientation.get(axis, 0.0)) for axis in ("i", "j", "k", "r")]
        ),
    )


def build_preview_data(
    document: dict[str, Any],
    skeleton: dict[str, Any],
    rid_id: str,
    *,
    actor_signatures: set[str] | None = None,
) -> dict[str, Any]:
    root = _root(document)
    bones = skeleton.get("bones")
    if not isinstance(bones, list) or not bones:
        raise RidPreviewError("Skeleton contract has no bones")
    parents = [int(bone["parent"]) for bone in bones]
    names = [str(bone["name"]) for bone in bones]
    actors = []
    diagnostics = []
    for actor in root.get("actors", []):
        if not isinstance(actor, dict):
            continue
        signature = _signature(actor)
        if not signature or (
            actor_signatures is not None and signature not in actor_signatures
        ):
            continue
        clips = actor.get("animations", [])
        if not isinstance(clips, list) or not clips:
            continue
        clip = clips[0]
        animation_handle = clip.get("animation") if isinstance(clip, dict) else None
        animation_data = (
            animation_handle.get("Data") if isinstance(animation_handle, dict) else None
        )
        buffer_handle = (
            animation_data.get("animBuffer")
            if isinstance(animation_data, dict)
            else None
        )
        buffer = buffer_handle.get("Data") if isinstance(buffer_handle, dict) else None
        if not isinstance(buffer, dict):
            continue
        buffer_type = buffer.get("$type")
        if buffer_type == "animAnimationBufferSimd":
            decoded = decode_simd_buffer(buffer)
        elif buffer_type == "animAnimationBufferCompressed":
            decoded = decode_compressed_buffer(buffer)
        else:
            continue
        joint_count = min(len(bones), int(buffer["numJoints"]))
        translation, rotation = _offset(clip)
        positions = _model_positions(
            decoded, parents[:joint_count], translation, rotation
        )
        sample_points = [
            point
            for frame in positions[:: max(1, len(positions) // 5)]
            for point in frame
        ]
        actors.append(
            {
                "signature": signature,
                "animation_name": _cname(animation_data.get("name")),
                "color": actor_preview_color(signature, len(actors)),
                "bone_names": names[:joint_count],
                "parents": parents[:joint_count],
                "frames": positions,
                "duration_seconds": decoded.duration,
                "source_joint_count": int(buffer["numJoints"]),
                "preview_joint_count": joint_count,
                "approximate_contract": int(buffer["numJoints"]) != len(bones),
                "bounds": {
                    "min": [
                        min(point[axis] for point in sample_points) for axis in range(3)
                    ],
                    "max": [
                        max(point[axis] for point in sample_points) for axis in range(3)
                    ],
                },
            }
        )
        diagnostics.append(
            {
                "actor": signature,
                "buffer_type": buffer_type,
                "payload_bytes": decoded.payload_bytes,
                "bytes_consumed": decoded.bytes_consumed,
                "trailing_bytes": decoded.payload_bytes - decoded.bytes_consumed,
            }
        )
    if not actors:
        raise RidPreviewError("RID has no selected supported body animations")
    frame_count = min(len(actor["frames"]) for actor in actors)
    duration = min(float(actor["duration_seconds"]) for actor in actors)
    all_points = [
        point
        for actor in actors
        for frame in actor["frames"][:: max(1, frame_count // 10)]
        for point in frame
    ]
    return {
        "schema_version": PREVIEW_SCHEMA_VERSION,
        "kind": "ghostline_sex_rid_preview_data",
        "rid_id": rid_id,
        "fps": 30,
        "frame_count": frame_count,
        "duration_seconds": duration,
        "coordinate_system": "RED_Z_UP",
        "skeleton_contract": skeleton.get("name"),
        "bounds": {
            "min": [min(point[axis] for point in all_points) for axis in range(3)],
            "max": [max(point[axis] for point in all_points) for axis in range(3)],
        },
        "actors": actors,
        "diagnostics": diagnostics,
    }


def _find_blender(explicit: Path | None) -> Path:
    if explicit is not None and explicit.is_file():
        return explicit
    discovered = shutil.which("blender")
    if discovered:
        return Path(discovered)
    if DEFAULT_BLENDER.is_file():
        return DEFAULT_BLENDER
    raise RidPreviewError("Blender was not found; pass --blender")


def render_preview(
    preview_data_path: Path,
    video_path: Path,
    contact_sheet_path: Path,
    *,
    blender: Path | None = None,
) -> None:
    executable = _find_blender(blender)
    video_path.parent.mkdir(parents=True, exist_ok=True)
    frames_dir = video_path.parent / f".{video_path.stem}-frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            str(executable),
            "--background",
            "--python",
            str(BLENDER_SCRIPT),
            "--",
            "--input",
            str(preview_data_path),
            "--video",
            str(video_path),
            "--frames-dir",
            str(frames_dir),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg is None:
        raise RidPreviewError("ffmpeg was not found for preview encoding")
    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-framerate",
            "30",
            "-start_number",
            "1",
            "-i",
            str(frames_dir / "frame_%04d.png"),
            "-c:v",
            "libx264",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            str(video_path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if not video_path.is_file():
        raise RidPreviewError("ffmpeg completed without producing the preview video")
    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(video_path),
            "-vf",
            "fps=1,scale=320:-1,tile=3x2:padding=4:margin=4",
            "-frames:v",
            "1",
            str(contact_sheet_path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if not contact_sheet_path.is_file():
        raise RidPreviewError("ffmpeg completed without producing the contact sheet")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rid-json", type=Path, required=True)
    parser.add_argument("--rid-id", required=True)
    parser.add_argument("--skeleton", type=Path, default=DEFAULT_SKELETON)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--actor", action="append", default=[])
    parser.add_argument("--blender", type=Path)
    parser.add_argument("--decode-only", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        data = build_preview_data(
            _read_json(args.rid_json.resolve()),
            _read_json(args.skeleton.resolve()),
            args.rid_id,
            actor_signatures=set(args.actor) if args.actor else None,
        )
        slug = preview_slug(args.rid_id)
        output_dir = args.output_dir.resolve()
        data_path = output_dir / f"{slug}.preview.json"
        video_path = output_dir / f"{slug}.mp4"
        contact_sheet_path = output_dir / f"{slug}.jpg"
        _write_json(data_path, data)
        print(f"Decoded {len(data['actors'])} actor(s) into {data_path}")
        if not args.decode_only:
            render_preview(
                data_path,
                video_path,
                contact_sheet_path,
                blender=args.blender.resolve() if args.blender else None,
            )
            print(f"Rendered {video_path}")
            print(f"Rendered {contact_sheet_path}")
    except (RidPreviewError, subprocess.CalledProcessError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
