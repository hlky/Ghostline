"""Build and review a human-readable catalog of Cyberpunk scene RIDs.

The catalog deliberately separates facts read from CR2W-JSON from human
annotation.  Rebuilding the technical inventory therefore never overwrites
pose labels, compatibility decisions, or reviewer notes.
"""

from __future__ import annotations

import argparse
import base64
import copy
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

from ghostline_red import serialize as serialize_cr2w


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = 1
ANNOTATION_FIELDS = (
    "label",
    "phase",
    "activity",
    "pose",
    "player_role",
    "partner_role",
    "location_context",
    "compatibility",
    "confidence",
    "tags",
    "notes",
)
BESPOKE_SEEDS: dict[str, dict[str, Any]] = {
    "sq027_06_panzer__jack_in_1first_player.scenerid": {
        "label": "Panam — first Basilisk jack-in (player performance)",
        "phase": "setup",
        "activity": "neural link jack-in",
        "player_role": "male or female V performance tracks",
        "partner_role": "Panam",
        "location_context": "Basilisk cockpit",
        "compatibility": "bespoke-only",
        "confidence": "high",
        "tags": ["panam", "basilisk", "personal-link", "setup"],
        "notes": "Includes Panam, both V FPP tracks, personal links, and the Basilisk rig; not a drop-in two-humanoid clip.",
    },
    "sq027_06_panzer__jack_in_1first_v.scenerid": {
        "label": "Panam — first Basilisk jack-in (V body)",
        "phase": "setup",
        "activity": "neural link jack-in",
        "player_role": "male and female average V bodies",
        "partner_role": "Panam",
        "location_context": "Basilisk cockpit",
        "compatibility": "bespoke-only",
        "confidence": "high",
        "tags": ["panam", "basilisk", "setup"],
        "notes": "Short V/Panam body segment paired with the first jack-in performance RID.",
    },
    "sq027_06_panzer__jack_in_2second_panam.scenerid": {
        "label": "Panam — second Basilisk jack-in",
        "phase": "setup",
        "activity": "neural link jack-in",
        "player_role": "male or female V performance tracks",
        "partner_role": "Panam",
        "location_context": "Basilisk cockpit",
        "compatibility": "bespoke-only",
        "confidence": "high",
        "tags": ["panam", "basilisk", "personal-link", "setup"],
        "notes": "Includes two Panam controls, both V FPP tracks, personal links, and the Basilisk rig.",
    },
    "sq027_06_panzer__sex_scene.scenerid": {
        "label": "Panam — Basilisk sex sequence",
        "phase": "main",
        "activity": "sex",
        "player_role": "male V",
        "partner_role": "Panam",
        "location_context": "Basilisk cockpit",
        "compatibility": "bespoke-only",
        "confidence": "high",
        "tags": ["panam", "basilisk", "sex", "vehicle-rig"],
        "notes": "Depends on Panam control rigs, V body/FPP tracks, two personal links, and the Basilisk rig.",
    },
    "sq027_06_panzer__sex_scene__jap.scenerid": {
        "label": "Panam — Basilisk sex sequence (__jap variant)",
        "phase": "main",
        "activity": "sex",
        "player_role": "male V",
        "partner_role": "Panam",
        "location_context": "Basilisk cockpit",
        "compatibility": "bespoke-only",
        "confidence": "high",
        "tags": ["panam", "basilisk", "sex", "variant"],
        "notes": "Named alternate of the Basilisk sex RID; visual review must establish the exact camera/performance difference.",
    },
    "sq028_04_destructive_tendencies_jp.scenerid": {
        "label": "Kerry — romance sequence (jp variant)",
        "phase": "main",
        "activity": "romance/sex",
        "player_role": "male V",
        "partner_role": "Kerry",
        "location_context": "Kerry romance scene",
        "compatibility": "bespoke-only",
        "confidence": "high",
        "tags": ["kerry", "lighter", "variant"],
        "notes": "Includes Kerry, player, and lighter tracks; visual review must distinguish this variant from new_camera_edit.",
    },
    "sq028_04_destructive_tendencies_new_camera_edit.scenerid": {
        "label": "Kerry — romance sequence (new camera edit)",
        "phase": "main",
        "activity": "romance/sex",
        "player_role": "male V",
        "partner_role": "Kerry",
        "location_context": "Kerry romance scene",
        "compatibility": "bespoke-only",
        "confidence": "high",
        "tags": ["kerry", "lighter", "camera-edit"],
        "notes": "Includes Kerry, player, and lighter tracks; the name identifies a camera edit, not a generic reusable pose.",
    },
    "synced__sq029_04a_dinner__rivers_bedroom_sex.scenerid": {
        "label": "River — bedroom sex sequence",
        "phase": "main",
        "activity": "sex",
        "player_role": "female V",
        "partner_role": "River",
        "location_context": "River bedroom",
        "compatibility": "bespoke-only",
        "confidence": "high",
        "tags": ["river", "bedroom", "sex", "doors", "beer-bottle"],
        "notes": "Includes River/V plus two door rigs and a beer-bottle prop; reuse needs the same environmental contract or retargeting.",
    },
    "synced__sq029_04a_dinner__rooftop_kiss.scenerid": {
        "label": "River — rooftop kiss",
        "phase": "prelude",
        "activity": "kiss",
        "player_role": "female V",
        "partner_role": "River",
        "location_context": "rooftop",
        "compatibility": "conditional",
        "confidence": "high",
        "tags": ["river", "rooftop", "kiss"],
        "notes": "Two-character bespoke River/V performance; simpler than the bedroom RID but still authored to River's rig and offsets.",
    },
    "synced__sq029_04a_dinner__street_prelude.scenerid": {
        "label": "River — street prelude",
        "phase": "prelude",
        "activity": "romance prelude",
        "player_role": "female V",
        "partner_role": "River",
        "location_context": "street",
        "compatibility": "conditional",
        "confidence": "high",
        "tags": ["river", "street", "prelude"],
        "notes": "Short two-character River/V performance; visual review is still required before treating it as a generic interaction.",
    },
    "sex_judy_layout.scenerid": {
        "label": "Judy — apartment sex sequence",
        "phase": "main",
        "activity": "sex",
        "player_role": "female V",
        "partner_role": "Judy",
        "location_context": "Judy apartment",
        "compatibility": "bespoke-only",
        "confidence": "high",
        "tags": ["judy", "sex", "cigarette", "lighter"],
        "notes": "Includes Judy/V, cigarette, and lighter performances; it is a complete bespoke layout rather than a single loop.",
    },
}


class SexRidCatalogError(RuntimeError):
    """Raised when RID catalog input violates the expected contract."""


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SexRidCatalogError(f"Cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SexRidCatalogError(f"Expected a JSON object in {path}")
    return value


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _contains_raw_data(value: Any) -> bool:
    if isinstance(value, dict):
        value_type = value.get("$type")
        if (
            "$rawData" in value
            and isinstance(value_type, str)
            and value_type.startswith("animAnimationBuffer")
        ):
            return True
        return any(_contains_raw_data(child) for child in value.values())
    if isinstance(value, list):
        return any(_contains_raw_data(child) for child in value)
    return False


def _root(document: dict[str, Any], expected_type: str) -> dict[str, Any]:
    data = document.get("Data")
    root = data.get("RootChunk") if isinstance(data, dict) else None
    if not isinstance(root, dict) or root.get("$type") != expected_type:
        raise SexRidCatalogError(f"Expected RootChunk type {expected_type}")
    return root


def _cname(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        text = value.get("$value")
        if isinstance(text, str):
            return text
    return None


def _serial(tag_owner: dict[str, Any]) -> int | None:
    tag = tag_owner.get("tag")
    serial = tag.get("serialNumber") if isinstance(tag, dict) else None
    value = serial.get("serialNumber") if isinstance(serial, dict) else None
    return int(value) if isinstance(value, (int, float)) else None


def _signature(tag_owner: dict[str, Any]) -> str | None:
    tag = tag_owner.get("tag")
    return _cname(tag.get("signature")) if isinstance(tag, dict) else None


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _normalized_path(path: str) -> str:
    return path.replace("/", "\\").lstrip("\\")


def _buffer_metadata(buffer: Any) -> dict[str, Any] | None:
    if not isinstance(buffer, dict):
        return None
    deferred = buffer.get("defferedBuffer")
    encoded = deferred.get("Bytes") if isinstance(deferred, dict) else None
    payload: bytes | None = None
    if isinstance(encoded, str):
        try:
            payload = base64.b64decode(encoded, validate=True)
        except ValueError as exc:
            raise SexRidCatalogError("Animation buffer has invalid base64") from exc
    duration = buffer.get("duration")
    frames = buffer.get("numFrames")
    fps = None
    if isinstance(duration, (int, float)) and duration > 0 and isinstance(frames, int):
        fps = round((frames - 1) / duration, 4)
    result: dict[str, Any] = {
        "type": buffer.get("$type"),
        "duration_seconds": duration,
        "frames": frames,
        "fps": fps,
        "joints": buffer.get("numJoints"),
        "tracks": buffer.get("numTracks"),
        "extra_joints": buffer.get("numExtraJoints"),
        "extra_tracks": buffer.get("numExtraTracks"),
    }
    if payload is not None:
        result["payload_bytes"] = len(payload)
        result["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    key_fields = (
        "numAnimKeys",
        "numAnimKeysRaw",
        "numConstAnimKeys",
        "numTrackKeys",
        "numConstTrackKeys",
    )
    keys = {field: buffer.get(field) for field in key_fields if field in buffer}
    if keys:
        result["key_counts"] = keys
    return {key: value for key, value in result.items() if value is not None}


def _animation_data(
    clip: dict[str, Any], *, camera: bool
) -> tuple[dict[str, Any], Any]:
    handle = clip.get("animation")
    data = handle.get("Data") if isinstance(handle, dict) else None
    if not isinstance(data, dict):
        return {}, None
    if camera:
        return {}, data
    buffer_handle = data.get("animBuffer")
    buffer = buffer_handle.get("Data") if isinstance(buffer_handle, dict) else None
    return data, buffer


def _event_types(clip: dict[str, Any]) -> dict[str, int]:
    handle = clip.get("events")
    data = handle.get("Data") if isinstance(handle, dict) else None
    events = data.get("events") if isinstance(data, dict) else None
    counts: Counter[str] = Counter()
    if isinstance(events, list):
        for event in events:
            if isinstance(event, dict) and isinstance(event.get("$type"), str):
                counts[event["$type"]] += 1
    return dict(sorted(counts.items()))


def _vector(value: Any, fields: tuple[str, ...]) -> list[float] | None:
    if not isinstance(value, dict):
        return None
    values = [value.get(field) for field in fields]
    if not all(isinstance(item, (int, float)) for item in values):
        return None
    return [round(float(item), 9) for item in values]


def _offset(clip: dict[str, Any]) -> dict[str, list[float]] | None:
    value = clip.get("offset")
    if not isinstance(value, dict):
        return None
    position = _vector(value.get("position"), ("X", "Y", "Z"))
    orientation = _vector(value.get("orientation"), ("i", "j", "k", "r"))
    result = {}
    if position is not None:
        result["position"] = position
    if orientation is not None:
        result["orientation"] = orientation
    return result or None


def _clip_metadata(clip: dict[str, Any], *, channel: str) -> dict[str, Any]:
    camera = channel == "camera"
    animation, buffer = _animation_data(clip, camera=camera)
    metadata: dict[str, Any] = {
        "signature": _signature(clip),
        "serial": _serial(clip),
        "animation_name": _cname(animation.get("name")),
        "animation_type": animation.get("animationType"),
        "duration_seconds": animation.get("duration"),
        "buffer": _buffer_metadata(buffer),
    }
    if camera:
        metadata["buffer"] = _buffer_metadata(buffer)
    else:
        metadata.update(
            {
                "bones": clip.get("bonesCount"),
                "motion_extracted": clip.get("motionExtracted"),
                "trajectory_bone_index": clip.get("trajectoryBoneIndex"),
                "offset": _offset(clip),
                "events": _event_types(clip),
            }
        )
    return {key: value for key, value in metadata.items() if value is not None}


def _infer_path_metadata(depot_path: str) -> dict[str, Any]:
    lowered = depot_path.casefold().replace("/", "\\")
    name = Path(lowered).name.removesuffix(".scenerid")
    family = "bespoke"
    phase = None
    if "\\generic_sex\\" in lowered:
        if "\\exclusive_intros\\" in lowered:
            family, phase = "exclusive", "intro"
        elif "\\exclusive_outros\\" in lowered:
            family, phase = "exclusive", "outro"
        elif "\\jigjig_intros\\" in lowered:
            family, phase = "jigjig", "intro"
        elif "\\jigjig_outros\\" in lowered:
            family, phase = "jigjig", "outro"
        elif "\\intercourse\\" in lowered:
            family, phase = "generic_intercourse", "loop"
        else:
            family = "generic"
    player_frame = None
    if re.search(r"_f$", name):
        player_frame = "female"
    elif re.search(r"_m$", name):
        player_frame = "male"
    nominal = re.search(r"_(\d+)s(?:_[fm])?$", name)
    return {
        "family": family,
        "phase_hint": phase,
        "player_frame_hint": player_frame,
        "maya_variant": "\\maya\\" in lowered,
        "nominal_duration_seconds": int(nominal.group(1)) if nominal else None,
    }


def _resource_duration(entry: dict[str, Any]) -> float | None:
    durations: list[float] = []
    for actor in entry["actors"]:
        for channel in ("body", "facial", "cyberware"):
            for clip in actor[channel]:
                duration = clip.get("duration_seconds")
                if not isinstance(duration, (int, float)):
                    duration = clip.get("buffer", {}).get("duration_seconds")
                if isinstance(duration, (int, float)):
                    durations.append(float(duration))
    for camera in entry["cameras"]:
        for clip in camera["animations"]:
            duration = clip.get("buffer", {}).get("duration_seconds")
            if isinstance(duration, (int, float)):
                durations.append(float(duration))
    return round(max(durations), 6) if durations else None


def inspect_rid(
    document: dict[str, Any],
    depot_path: str,
    *,
    binary_path: Path | None = None,
) -> dict[str, Any]:
    """Return deterministic technical metadata for one scnRidResource."""
    root = _root(document, "scnRidResource")
    actors = []
    for actor in root.get("actors", []):
        if not isinstance(actor, dict):
            continue
        row: dict[str, Any] = {
            "signature": _signature(actor),
            "serial": _serial(actor),
        }
        for channel, field in (
            ("body", "animations"),
            ("facial", "facialAnimations"),
            ("cyberware", "cyberwareAnimations"),
        ):
            clips = actor.get(field, [])
            row[channel] = (
                [
                    _clip_metadata(clip, channel=channel)
                    for clip in clips
                    if isinstance(clip, dict)
                ]
                if isinstance(clips, list)
                else []
            )
        actors.append(row)
    cameras = []
    for camera in root.get("cameras", []):
        if not isinstance(camera, dict):
            continue
        clips = camera.get("animations", [])
        cameras.append(
            {
                "signature": _signature(camera),
                "serial": _serial(camera),
                "animations": [
                    _clip_metadata(clip, channel="camera")
                    for clip in clips
                    if isinstance(clip, dict)
                ]
                if isinstance(clips, list)
                else [],
            }
        )
    normalized = _normalized_path(depot_path)
    entry: dict[str, Any] = {
        "id": normalized,
        "depot_path": normalized,
        "inferred": _infer_path_metadata(normalized),
        "actors": actors,
        "cameras": cameras,
        "actor_signatures": sorted(
            signature
            for signature in (_signature(actor) for actor in root.get("actors", []))
            if signature
        ),
        "next_serial_number": root.get("nextSerialNumber"),
        "rid_version": root.get("version"),
        "used_by": [],
    }
    entry["duration_seconds"] = _resource_duration(entry)
    if binary_path is not None and binary_path.is_file():
        entry["source"] = {
            "bytes": binary_path.stat().st_size,
            "sha256": _sha256_file(binary_path),
        }
    else:
        canonical = json.dumps(root, sort_keys=True, separators=(",", ":"))
        entry["source"] = {
            "root_chunk_sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        }
    return entry


def _iter_scene_rid_references(
    document: dict[str, Any],
) -> Iterable[tuple[int | None, str]]:
    root = _root(document, "scnSceneResource")
    resources = root.get("ridResources", [])
    if not isinstance(resources, list):
        return
    for resource in resources:
        if not isinstance(resource, dict):
            continue
        rid_id = resource.get("id")
        numeric_id = rid_id.get("id") if isinstance(rid_id, dict) else None
        rid_resource = resource.get("ridResource")
        depot = (
            rid_resource.get("DepotPath") if isinstance(rid_resource, dict) else None
        )
        path = _cname(depot)
        if path:
            yield (
                int(numeric_id) if isinstance(numeric_id, (int, float)) else None,
                _normalized_path(path),
            )


def scene_usage(scene_paths: Iterable[Path]) -> dict[str, list[dict[str, Any]]]:
    usage: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in sorted(scene_paths, key=lambda item: str(item).casefold()):
        document = _read_json(path)
        header = document.get("Header")
        archive_name = (
            header.get("ArchiveFileName") if isinstance(header, dict) else None
        )
        scene = (
            Path(archive_name).name
            if isinstance(archive_name, str)
            else path.name.removesuffix(".json")
        )
        counts: Counter[tuple[int | None, str]] = Counter(
            _iter_scene_rid_references(document)
        )
        for (resource_id, depot_path), references in sorted(
            counts.items(), key=lambda row: row[0][1]
        ):
            usage[depot_path.casefold()].append(
                {
                    "scene": scene,
                    "resource_id": resource_id,
                    "references": references,
                }
            )
    return usage


def _json_to_depot_path(path: Path, root: Path) -> str:
    relative = path.relative_to(root).as_posix()
    if not relative.casefold().endswith(".scenerid.json"):
        raise SexRidCatalogError(f"Not a serialized scene RID: {path}")
    return relative[:-5].replace("/", "\\")


def build_catalog(
    rid_json_root: Path,
    *,
    binary_root: Path | None = None,
    scene_json_roots: Iterable[Path] = (),
) -> dict[str, Any]:
    paths = sorted(
        rid_json_root.rglob("*.scenerid.json"), key=lambda item: str(item).casefold()
    )
    if not paths:
        raise SexRidCatalogError(f"No .scenerid.json files under {rid_json_root}")
    scene_paths = [
        path for root in scene_json_roots for path in root.rglob("*.scene.json")
    ]
    usage = scene_usage(scene_paths)
    entries = []
    for path in paths:
        depot_path = _json_to_depot_path(path, rid_json_root)
        binary_path = (
            binary_root / Path(depot_path) if binary_root is not None else None
        )
        entry = inspect_rid(_read_json(path), depot_path, binary_path=binary_path)
        entry["used_by"] = usage.get(depot_path.casefold(), [])
        entries.append(entry)
    families = Counter(entry["inferred"]["family"] for entry in entries)
    referenced = sum(bool(entry["used_by"]) for entry in entries)
    clip_totals = Counter()
    for entry in entries:
        for actor in entry["actors"]:
            for channel in ("body", "facial", "cyberware"):
                clip_totals[channel] += len(actor[channel])
        clip_totals["camera"] += sum(
            len(camera["animations"]) for camera in entry["cameras"]
        )
    catalog_paths = {entry["depot_path"].casefold() for entry in entries}
    missing_references = sorted(path for path in usage if path not in catalog_paths)
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "ghostline_sex_rid_catalog",
        "summary": {
            "resources": len(entries),
            "referenced_resources": referenced,
            "unreferenced_resources": len(entries) - referenced,
            "referenced_not_in_catalog": missing_references,
            "families": dict(sorted(families.items())),
            "clips": dict(sorted(clip_totals.items())),
        },
        "entries": entries,
    }


def starter_annotations(
    catalog: dict[str, Any], existing: dict[str, Any] | None = None
) -> dict[str, Any]:
    old_entries = existing.get("entries", {}) if isinstance(existing, dict) else {}
    if not isinstance(old_entries, dict):
        raise SexRidCatalogError(
            "Annotation entries must be an object keyed by depot path"
        )
    entries: dict[str, Any] = {}
    for row in catalog.get("entries", []):
        rid_id = row["id"]
        old = old_entries.get(rid_id, {})
        if not isinstance(old, dict):
            old = {}
        inferred = row.get("inferred", {})
        defaults: dict[str, Any] = {
            "label": "",
            "phase": inferred.get("phase_hint") or "",
            "activity": "",
            "pose": "",
            "player_role": "",
            "partner_role": "",
            "location_context": "",
            "compatibility": "unreviewed",
            "confidence": "unreviewed",
            "tags": [],
            "notes": "",
        }
        seed = BESPOKE_SEEDS.get(rid_id.replace("\\", "/").rsplit("/", 1)[-1], {})
        entries[rid_id] = {
            field: (
                seed[field]
                if field in seed and old.get(field, defaults[field]) == defaults[field]
                else old.get(field, seed.get(field, defaults[field]))
            )
            for field in ANNOTATION_FIELDS
        }
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "ghostline_sex_rid_annotations",
        "entries": entries,
    }


def preview_slug(rid_id: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", rid_id.casefold()).strip("-")


def preview_manifest(
    catalog: dict[str, Any], preview_dir: str = "previews"
) -> dict[str, Any]:
    jobs = []
    for index, entry in enumerate(catalog.get("entries", []), start=1):
        slug = preview_slug(entry["id"])
        clips = sum(
            len(actor[channel])
            for actor in entry["actors"]
            for channel in ("body", "facial", "cyberware")
        )
        jobs.append(
            {
                "id": entry["id"],
                "order": index,
                "duration_seconds": entry.get("duration_seconds"),
                "actor_signatures": entry.get("actor_signatures", []),
                "animation_clips": clips,
                "camera_clips": sum(
                    len(camera["animations"]) for camera in entry["cameras"]
                ),
                "expected_video": f"{preview_dir}/{slug}.mp4",
                "expected_contact_sheet": f"{preview_dir}/{slug}.jpg",
                "status": "decoder_required",
            }
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "ghostline_sex_rid_preview_manifest",
        "render_contract": {
            "resolution": [960, 540],
            "fps": 30,
            "camera": "rid_camera_or_overview_fallback",
            "actors": "color_coded_neutral_proxies",
            "slate": ["label", "depot_path", "timecode", "actor_signatures"],
        },
        "jobs": jobs,
    }


def resolve_preview_artifacts(
    previews: dict[str, Any], review_directory: Path
) -> dict[str, Any]:
    """Mark preview jobs ready when their generated media is present."""
    resolved = copy.deepcopy(previews)
    for job in resolved.get("jobs", []):
        video = review_directory / Path(job["expected_video"])
        contact_sheet = review_directory / Path(job["expected_contact_sheet"])
        if not video.is_file() or not contact_sheet.is_file():
            continue
        job["status"] = "ready"
        job["video_url"] = Path(job["expected_video"]).as_posix()
        job["contact_sheet_url"] = Path(job["expected_contact_sheet"]).as_posix()
        preview_data = video.with_suffix(".preview.json")
        if preview_data.is_file():
            data = _read_json(preview_data)
            job["rendered_actors"] = [
                actor.get("signature", "") for actor in data.get("actors", [])
            ]
    return resolved


def render_review_html(
    catalog: dict[str, Any], annotations: dict[str, Any], previews: dict[str, Any]
) -> str:
    data = json.dumps(
        {"catalog": catalog, "annotations": annotations, "previews": previews},
        ensure_ascii=False,
    ).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width\">
<title>Ghostline sex RID review</title>
<style>
:root{{--bg:#101319;--panel:#191e27;--ink:#edf1f7;--muted:#9da9b8;--accent:#64d8cb;--line:#323b49}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 system-ui,sans-serif}}
header{{position:sticky;top:0;z-index:2;background:#101319ee;border-bottom:1px solid var(--line);padding:16px 22px}}
h1{{font-size:20px;margin:0 0 12px}}input,select,textarea{{background:#0d1015;color:var(--ink);border:1px solid var(--line);border-radius:5px;padding:7px}}
#search{{width:min(560px,65vw)}}button{{background:var(--accent);border:0;border-radius:5px;padding:8px 12px;font-weight:700;cursor:pointer}}
main{{display:grid;gap:14px;padding:18px}}article{{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:15px}}
.path{{font-family:ui-monospace,monospace;color:var(--accent);overflow-wrap:anywhere}}.meta{{color:var(--muted);margin:6px 0 12px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:9px}}label{{display:grid;gap:4px;color:var(--muted)}}textarea{{min-height:70px}}
.preview{{aspect-ratio:16/9;background:#0b0d11;display:grid;place-items:center;color:var(--muted);margin:10px 0;border-radius:5px;overflow:hidden}}video,img{{max-width:100%;max-height:100%}}
.hidden{{display:none}}code{{color:#d9a7ff}}a{{color:var(--accent)}}</style></head>
<body><header><h1>Ghostline sex RID review</h1><input id=\"search\" placeholder=\"Filter paths, actors, labels, tags…\"> <select id=\"family\"><option value=\"\">All families</option></select> <button id=\"download\">Download annotations</button></header>
<main id=\"cards\"></main><script id=\"rid-data\" type=\"application/json\">{data}</script>
<script>
const D=JSON.parse(document.querySelector('#rid-data').textContent), C=D.catalog.entries, A=D.annotations.entries;
const jobs=Object.fromEntries(D.previews.jobs.map(x=>[x.id,x])); const fields={json.dumps(list(ANNOTATION_FIELDS))};
const families=[...new Set(C.map(x=>x.inferred.family))].sort(); const fs=document.querySelector('#family'); families.forEach(x=>fs.add(new Option(x,x)));
const esc=s=>String(s??'').replace(/[&<>\"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}}[c]));
function input(id,f,v){{if(f==='notes')return `<label>${{f}}<textarea data-id=\"${{esc(id)}}\" data-field=\"${{f}}\">${{esc(v)}}</textarea></label>`;
if(f==='compatibility'||f==='confidence'){{let opts=(f==='compatibility'?['unreviewed','reusable','conditional','bespoke-only','reject']:['unreviewed','low','medium','high']);return `<label>${{f}}<select data-id=\"${{esc(id)}}\" data-field=\"${{f}}\">${{opts.map(x=>`<option ${{x===v?'selected':''}}>${{x}}</option>`).join('')}}</select></label>`}}
return `<label>${{f}}<input data-id=\"${{esc(id)}}\" data-field=\"${{f}}\" value=\"${{esc(Array.isArray(v)?v.join(', '):v)}}\"></label>`}}
function draw(){{const q=document.querySelector('#search').value.toLowerCase(), fam=fs.value;document.querySelector('#cards').innerHTML=C.map(e=>{{const a=A[e.id]||{{}},j=jobs[e.id]||{{}};let hay=JSON.stringify([e.id,e.actor_signatures,a]).toLowerCase();if((q&&!hay.includes(q))||(fam&&e.inferred.family!==fam))return '';
let preview=j.status==='ready'?`<div class=\"preview\"><video controls loop muted playsinline poster=\"${{esc(j.contact_sheet_url)}}\" src=\"${{esc(j.video_url)}}\"></video></div><div class=\"meta\">Rendered roles: <code>${{esc((j.rendered_actors||[]).join(' + '))}}</code> · <a href=\"${{esc(j.contact_sheet_url)}}\">contact sheet</a></div>`:`<div class=\"preview\">Preview pending — ${{esc(j.status||'not planned')}}</div>`;return `<article><div class=\"path\">${{esc(e.depot_path)}}</div><div class=\"meta\">${{esc(e.inferred.family)}} · ${{e.duration_seconds??'?'}}s · actors <code>${{esc(e.actor_signatures.join(', '))}}</code> · ${{e.used_by.length}} scene(s)</div>${{preview}}<div class=\"grid\">${{fields.map(f=>input(e.id,f,a[f]??(f==='tags'?[]:''))).join('')}}</div></article>`}}).join(''); bind()}}
function bind(){{document.querySelectorAll('[data-field]').forEach(el=>el.addEventListener('input',()=>{{let v=el.value;if(el.dataset.field==='tags')v=v.split(',').map(x=>x.trim()).filter(Boolean);A[el.dataset.id][el.dataset.field]=v}}))}}
document.querySelector('#search').addEventListener('input',draw);fs.addEventListener('change',draw);document.querySelector('#download').onclick=()=>{{const out={{schema_version:1,kind:'ghostline_sex_rid_annotations',entries:A}},blob=new Blob([JSON.stringify(out,null,2)+'\\n'],{{type:'application/json'}}),a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='vanilla-sex-rid-annotations.json';a.click();URL.revokeObjectURL(a.href)}};draw();
</script></body></html>"""


def serialize_tree(
    input_root: Path,
    output_root: Path,
    *,
    force: bool = False,
    wolvenkit_cli: Path | None = None,
) -> tuple[int, int]:
    resources = sorted(
        input_root.rglob("*.scenerid"), key=lambda item: str(item).casefold()
    )
    if not resources:
        raise SexRidCatalogError(f"No .scenerid files under {input_root}")
    written = 0
    fallback_sources: dict[Path, list[tuple[Path, Path]]] = defaultdict(list)
    for source in resources:
        relative = source.relative_to(input_root)
        target = output_root / Path(str(relative) + ".json")
        if (
            not force
            and target.is_file()
            and target.stat().st_mtime_ns >= source.stat().st_mtime_ns
            and not _contains_raw_data(_read_json(target))
        ):
            continue
        serialize_cr2w(source, target)
        document = _read_json(target)
        if _contains_raw_data(document):
            if wolvenkit_cli is None or not wolvenkit_cli.is_file():
                raise SexRidCatalogError(
                    f"Native serialization left opaque $rawData in {target}; "
                    "rerun with --wolvenkit-cli"
                )
            fallback_sources[source.parent].append((source, target))
        written += 1
    for rows in fallback_sources.values():
        output_parent = rows[0][1].parent
        subprocess.run(
            [
                str(wolvenkit_cli),
                "convert",
                "serialize",
                *(str(source) for source, _target in rows),
                "--outpath",
                str(output_parent),
                "--verbosity",
                "Minimal",
            ],
            check=True,
        )
        for source, target in rows:
            if not target.is_file() or _contains_raw_data(_read_json(target)):
                raise SexRidCatalogError(
                    f"WolvenKit fallback did not fully serialize {source}"
                )
    return written, sum(len(rows) for rows in fallback_sources.values())


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    serialize = subparsers.add_parser(
        "serialize", help="Serialize a mirrored tree of .scenerid files"
    )
    serialize.add_argument("--input", type=Path, required=True)
    serialize.add_argument("--output", type=Path, required=True)
    serialize.add_argument("--force", action="store_true")
    serialize.add_argument(
        "--wolvenkit-cli",
        type=Path,
        help="Fallback serializer for nested buffers emitted as opaque $rawData",
    )

    build = subparsers.add_parser(
        "build", help="Build technical catalog and merge scene usage"
    )
    build.add_argument("--rid-json-root", type=Path, required=True)
    build.add_argument("--binary-root", type=Path)
    build.add_argument("--scene-json-root", type=Path, action="append", default=[])
    build.add_argument("--output", type=Path, required=True)

    annotate = subparsers.add_parser(
        "annotations", help="Create or refresh the human annotation layer"
    )
    annotate.add_argument("--catalog", type=Path, required=True)
    annotate.add_argument("--output", type=Path, required=True)

    preview = subparsers.add_parser(
        "preview-plan", help="Create the stable preview/render job manifest"
    )
    preview.add_argument("--catalog", type=Path, required=True)
    preview.add_argument("--output", type=Path, required=True)
    preview.add_argument("--preview-dir", default="previews")

    review = subparsers.add_parser(
        "review", help="Generate a portable annotation review page"
    )
    review.add_argument("--catalog", type=Path, required=True)
    review.add_argument("--annotations", type=Path, required=True)
    review.add_argument("--preview-plan", type=Path, required=True)
    review.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "serialize":
            written, fallbacks = serialize_tree(
                args.input.resolve(),
                args.output.resolve(),
                force=args.force,
                wolvenkit_cli=args.wolvenkit_cli.resolve()
                if args.wolvenkit_cli
                else None,
            )
            print(
                f"Serialized {written} scene RID(s) to {args.output} "
                f"({fallbacks} WolvenKit fallback(s))"
            )
        elif args.command == "build":
            catalog = build_catalog(
                args.rid_json_root.resolve(),
                binary_root=args.binary_root.resolve() if args.binary_root else None,
                scene_json_roots=(path.resolve() for path in args.scene_json_root),
            )
            _write_json(args.output, catalog)
            print(
                f"Cataloged {catalog['summary']['resources']} scene RID(s) in {args.output}"
            )
        elif args.command == "annotations":
            existing = _read_json(args.output) if args.output.is_file() else None
            value = starter_annotations(_read_json(args.catalog), existing)
            _write_json(args.output, value)
            print(
                f"Refreshed {len(value['entries'])} annotation row(s) in {args.output}"
            )
        elif args.command == "preview-plan":
            value = preview_manifest(_read_json(args.catalog), args.preview_dir)
            _write_json(args.output, value)
            print(f"Planned {len(value['jobs'])} preview job(s) in {args.output}")
        elif args.command == "review":
            output = args.output.resolve()
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(
                render_review_html(
                    _read_json(args.catalog),
                    _read_json(args.annotations),
                    resolve_preview_artifacts(
                        _read_json(args.preview_plan), output.parent
                    ),
                ),
                encoding="utf-8",
            )
            print(f"Wrote RID review page to {output}")
    except SexRidCatalogError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
