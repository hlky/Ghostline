#!/usr/bin/env python3
"""Validate and build deterministic Ghostline braindance Blender scenes.

The checked JSON specification is the source of truth. Blender is invoked only
as a renderer/baker for the generated authoring scene; generated .blend, .glb,
and handoff manifest files default to the ignored .tmp workspace.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BLENDER_RUNNER = Path(__file__).with_name("braindance_scene_blender.py")
DEFAULT_SPEC = ROOT / "source" / "braindance" / "tests" / "gqt005_braindance_analysis.json"
SUPPORTED_SCHEMA_VERSION = 1
NAME_RE = re.compile(r"^[a-z][a-z0-9_]*$")
INTERPOLATIONS = {"LINEAR", "BEZIER", "CONSTANT"}
CLUE_LAYERS = {"Visual", "Audio", "Thermal"}
RID_ACTOR_CHANNELS = ("facial", "cyberware")
BODY_ANIMATION_TYPES = {"walk_from_root_motion"}

TOP_LEVEL_FIELDS = {
    "schema_version",
    "name",
    "fps",
    "frames",
    "outputs",
    "origin",
    "environment",
    "actors",
    "recording_camera",
    "clues",
    "markers",
}


class BraindanceBuildError(RuntimeError):
    pass


@dataclass(frozen=True)
class ValidationReport:
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    details: dict[str, Any]

    @property
    def ok(self) -> bool:
        return not self.errors


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BraindanceBuildError(f"Spec does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BraindanceBuildError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise BraindanceBuildError(f"Spec root must be an object: {path}")
    return value


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _check_vector(
    value: Any,
    length: int,
    label: str,
    errors: list[str],
    *,
    positive: bool = False,
) -> None:
    if not isinstance(value, list) or len(value) != length or not all(_is_number(item) for item in value):
        errors.append(f"{label} must be an array of {length} numbers")
        return
    if positive and any(float(item) <= 0 for item in value):
        errors.append(f"{label} values must be greater than zero")


def _check_transform(
    value: Any,
    label: str,
    errors: list[str],
    *,
    camera: bool = False,
) -> None:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return
    unknown = set(value) - {
        "frame",
        "location",
        "rotation_degrees",
        "look_at",
        "scale",
        "focal_length",
    }
    if unknown:
        errors.append(f"{label} has unsupported fields: {', '.join(sorted(unknown))}")
    if "location" in value:
        _check_vector(value["location"], 3, f"{label}.location", errors)
    if "rotation_degrees" in value:
        _check_vector(value["rotation_degrees"], 3, f"{label}.rotation_degrees", errors)
    if "look_at" in value:
        _check_vector(value["look_at"], 3, f"{label}.look_at", errors)
    if "scale" in value:
        _check_vector(value["scale"], 3, f"{label}.scale", errors, positive=True)
    if camera:
        has_rotation = "rotation_degrees" in value
        has_look_at = "look_at" in value
        if has_rotation == has_look_at:
            errors.append(f"{label} must define exactly one of rotation_degrees or look_at")
        if "focal_length" in value and (
            not _is_number(value["focal_length"]) or float(value["focal_length"]) <= 0
        ):
            errors.append(f"{label}.focal_length must be greater than zero")
    elif "look_at" in value or "focal_length" in value:
        errors.append(f"{label} cannot use camera-only look_at or focal_length fields")


def _check_frame(value: Any, label: str, start: int, end: int, errors: list[str]) -> int | None:
    if not isinstance(value, int) or isinstance(value, bool):
        errors.append(f"{label} must be an integer")
        return None
    if value < start or value > end:
        errors.append(f"{label} must be within {start}..{end}")
    return value


def _check_output_path(value: Any, label: str, suffix: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty path")
    elif Path(value).suffix.casefold() != suffix:
        errors.append(f"{label} must end with {suffix}")


def _check_rid_actor_channel(
    value: Any,
    label: str,
    errors: list[str],
    *,
    repo_root: Path,
) -> None:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return
    unsupported = set(value) - {"asset", "armature", "tracks"}
    if unsupported:
        errors.append(
            f"{label} has unsupported fields: {', '.join(sorted(unsupported))}"
        )
    asset = value.get("asset")
    if asset is not None:
        if (
            not isinstance(asset, dict)
            or set(asset) - {"path", "armature"}
            or "path" not in asset
        ):
            errors.append(f"{label}.asset must contain path and optional armature")
        else:
            path = repo_root / str(asset["path"])
            if Path(str(asset["path"])).suffix.casefold() not in {".glb", ".gltf"}:
                errors.append(f"{label}.asset.path must be a .glb or .gltf")
            elif not path.exists():
                errors.append(f"{label}.asset.path does not exist: {asset['path']}")
    armature = value.get("armature")
    if armature is not None and (
        not isinstance(armature, str) or not armature.strip()
    ):
        errors.append(f"{label}.armature must be a non-empty Blender object name")
    if isinstance(asset, dict) and asset.get("armature") and armature:
        errors.append(f"{label} must set armature either directly or in asset, not both")
    tracks = value.get("tracks", [])
    if not isinstance(tracks, list):
        errors.append(f"{label}.tracks must be an array")
        return
    indices: set[int] = set()
    for index, track in enumerate(tracks):
        track_label = f"{label}.tracks[{index}]"
        if not isinstance(track, dict) or set(track) != {
            "index",
            "object",
            "data_path",
        }:
            errors.append(
                f"{track_label} must contain exactly index, object, and data_path"
            )
            continue
        track_index = track["index"]
        if (
            not isinstance(track_index, int)
            or isinstance(track_index, bool)
            or track_index < 0
        ):
            errors.append(f"{track_label}.index must be a non-negative integer")
        elif track_index in indices:
            errors.append(f"{label}.tracks duplicates index {track_index}")
        else:
            indices.add(track_index)
        for field in ("object", "data_path"):
            if not isinstance(track[field], str) or not track[field].strip():
                errors.append(f"{track_label}.{field} must be a non-empty string")


def _load_skeleton_contract(
    value: Any,
    label: str,
    errors: list[str],
    *,
    repo_root: Path,
) -> dict[str, Any] | None:
    if not isinstance(value, dict) or set(value) != {"contract"}:
        errors.append(f"{label} must contain exactly contract")
        return None
    raw_path = value.get("contract")
    if not isinstance(raw_path, str) or not raw_path.strip():
        errors.append(f"{label}.contract must be a non-empty path")
        return None
    path = repo_root / raw_path
    if not path.is_file():
        errors.append(f"{label}.contract does not exist: {raw_path}")
        return None
    try:
        contract = load_json(path)
    except BraindanceBuildError as exc:
        errors.append(f"{label}.contract is invalid: {exc}")
        return None
    bones = contract.get("bones")
    if (
        contract.get("schema_version") != 1
        or contract.get("kind") != "ghostline_braindance_skeleton"
        or not isinstance(contract.get("name"), str)
        or not isinstance(bones, list)
        or not bones
        or contract.get("bone_count") != len(bones)
    ):
        errors.append(f"{label}.contract is not a valid skeleton contract")
        return None
    names: set[str] = set()
    for index, bone in enumerate(bones):
        bone_label = f"{label}.contract.bones[{index}]"
        if not isinstance(bone, dict):
            errors.append(f"{bone_label} must be an object")
            continue
        if bone.get("index") != index:
            errors.append(f"{bone_label}.index must be {index}")
        name = bone.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"{bone_label}.name must be non-empty")
        elif name in names:
            errors.append(f"{label}.contract duplicates bone {name!r}")
        else:
            names.add(name)
        parent = bone.get("parent")
        if (
            not isinstance(parent, int)
            or isinstance(parent, bool)
            or parent < -1
            or parent >= index
        ):
            errors.append(f"{bone_label}.parent must be within -1..{index - 1}")
        for rest_name in ("local_rest", "model_rest"):
            rest = bone.get(rest_name)
            if not isinstance(rest, dict):
                errors.append(f"{bone_label}.{rest_name} must be an object")
                continue
            _check_vector(
                rest.get("translation"),
                3,
                f"{bone_label}.{rest_name}.translation",
                errors,
            )
            _check_vector(
                rest.get("rotation"),
                4,
                f"{bone_label}.{rest_name}.rotation",
                errors,
            )
            _check_vector(
                rest.get("scale"),
                3,
                f"{bone_label}.{rest_name}.scale",
                errors,
                positive=True,
            )
    trajectory = contract.get("trajectory_joint_index")
    if (
        not isinstance(trajectory, int)
        or isinstance(trajectory, bool)
        or not 0 <= trajectory < len(bones)
        or bones[trajectory].get("name") != "Trajectory"
    ):
        errors.append(
            f"{label}.contract trajectory_joint_index must identify Trajectory"
        )
    return contract


def _check_body_animation(
    value: Any,
    label: str,
    errors: list[str],
) -> None:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return
    allowed = {
        "type",
        "stride_length",
        "leg_swing_degrees",
        "knee_bend_degrees",
        "arm_swing_degrees",
        "phase_degrees",
        "speed_threshold",
    }
    unsupported = set(value) - allowed
    if unsupported:
        errors.append(
            f"{label} has unsupported fields: {', '.join(sorted(unsupported))}"
        )
    if value.get("type") not in BODY_ANIMATION_TYPES:
        errors.append(
            f"{label}.type must be one of "
            f"{', '.join(sorted(BODY_ANIMATION_TYPES))}"
        )
    for field in (
        "stride_length",
        "leg_swing_degrees",
        "knee_bend_degrees",
        "arm_swing_degrees",
    ):
        if field in value and (
            not _is_number(value[field]) or float(value[field]) <= 0
        ):
            errors.append(f"{label}.{field} must be greater than zero")
    if "phase_degrees" in value and not _is_number(value["phase_degrees"]):
        errors.append(f"{label}.phase_degrees must be a number")
    if "speed_threshold" in value and (
        not _is_number(value["speed_threshold"])
        or float(value["speed_threshold"]) < 0
    ):
        errors.append(f"{label}.speed_threshold must be zero or greater")


def _rig_summary(
    actor: dict[str, Any],
    *,
    repo_root: Path,
) -> dict[str, Any] | None:
    rig = actor.get("rig")
    if not isinstance(rig, dict):
        return None
    path = (repo_root / str(rig["contract"])).resolve()
    raw = path.read_bytes()
    contract = json.loads(raw)
    bones = contract["bones"]
    return {
        "contract": str(rig["contract"]),
        "name": contract["name"],
        "contract_sha256": hashlib.sha256(raw).hexdigest(),
        "bone_count": len(bones),
        "bone_order": [bone["name"] for bone in bones],
        "trajectory_joint_index": contract["trajectory_joint_index"],
    }


def validate_spec(spec: dict[str, Any], *, repo_root: Path = ROOT) -> ValidationReport:
    errors: list[str] = []
    warnings: list[str] = []
    unknown = set(spec) - TOP_LEVEL_FIELDS
    if unknown:
        errors.append(f"Unsupported top-level fields: {', '.join(sorted(unknown))}")

    if spec.get("schema_version") != SUPPORTED_SCHEMA_VERSION:
        errors.append(f"schema_version must be {SUPPORTED_SCHEMA_VERSION}")

    name = spec.get("name")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        errors.append("name must match ^[a-z][a-z0-9_]*$")

    fps = spec.get("fps")
    if not isinstance(fps, int) or isinstance(fps, bool) or not 1 <= fps <= 240:
        errors.append("fps must be an integer from 1 through 240")

    frames = spec.get("frames")
    if not isinstance(frames, dict) or set(frames) != {"start", "end"}:
        errors.append("frames must contain exactly start and end")
        frame_start, frame_end = 0, 0
    else:
        frame_start = frames.get("start")
        frame_end = frames.get("end")
        if not isinstance(frame_start, int) or isinstance(frame_start, bool):
            errors.append("frames.start must be an integer")
            frame_start = 0
        if not isinstance(frame_end, int) or isinstance(frame_end, bool):
            errors.append("frames.end must be an integer")
            frame_end = 0
        if frame_end <= frame_start:
            errors.append("frames.end must be greater than frames.start")

    outputs = spec.get("outputs")
    if not isinstance(outputs, dict) or set(outputs) != {"blend", "glb", "manifest"}:
        errors.append("outputs must contain exactly blend, glb, and manifest")
    else:
        _check_output_path(outputs["blend"], "outputs.blend", ".blend", errors)
        _check_output_path(outputs["glb"], "outputs.glb", ".glb", errors)
        _check_output_path(outputs["manifest"], "outputs.manifest", ".json", errors)
        for key, raw_path in outputs.items():
            if not isinstance(raw_path, str):
                continue
            path = Path(raw_path)
            if path.is_absolute():
                errors.append(f"outputs.{key} must be relative to the repository root")
                continue
            try:
                (repo_root / path).resolve().relative_to(repo_root.resolve())
            except ValueError:
                errors.append(f"outputs.{key} must stay inside the repository root")

    origin = spec.get("origin")
    if not isinstance(origin, dict) or set(origin) != {"name", "location", "rotation_degrees"}:
        errors.append("origin must contain exactly name, location, and rotation_degrees")
    else:
        if not isinstance(origin["name"], str) or not NAME_RE.fullmatch(origin["name"]):
            errors.append("origin.name must be a lowercase identifier")
        _check_vector(origin["location"], 3, "origin.location", errors)
        _check_vector(origin["rotation_degrees"], 3, "origin.rotation_degrees", errors)

    environment = spec.get("environment", {})
    if not isinstance(environment, dict):
        errors.append("environment must be an object")
    else:
        env_unknown = set(environment) - {"boxes", "imports"}
        if env_unknown:
            errors.append(f"environment has unsupported fields: {', '.join(sorted(env_unknown))}")
        box_ids: set[str] = set()
        for index, box in enumerate(environment.get("boxes", [])):
            label = f"environment.boxes[{index}]"
            if not isinstance(box, dict):
                errors.append(f"{label} must be an object")
                continue
            required = {"id", "location", "size"}
            missing = required - set(box)
            unsupported = set(box) - required - {"rotation_degrees", "color"}
            if missing:
                errors.append(f"{label} missing fields: {', '.join(sorted(missing))}")
            if unsupported:
                errors.append(f"{label} has unsupported fields: {', '.join(sorted(unsupported))}")
            box_id = box.get("id")
            if not isinstance(box_id, str) or not NAME_RE.fullmatch(box_id):
                errors.append(f"{label}.id must be a lowercase identifier")
            elif box_id in box_ids:
                errors.append(f"Duplicate environment box id: {box_id}")
            else:
                box_ids.add(box_id)
            if "location" in box:
                _check_vector(box["location"], 3, f"{label}.location", errors)
            if "size" in box:
                _check_vector(box["size"], 3, f"{label}.size", errors, positive=True)
            if "rotation_degrees" in box:
                _check_vector(box["rotation_degrees"], 3, f"{label}.rotation_degrees", errors)
            if "color" in box:
                _check_vector(box["color"], 4, f"{label}.color", errors)

        for index, imported in enumerate(environment.get("imports", [])):
            label = f"environment.imports[{index}]"
            if not isinstance(imported, dict) or set(imported) != {"id", "path"}:
                errors.append(f"{label} must contain exactly id and path")
                continue
            if not isinstance(imported["id"], str) or not NAME_RE.fullmatch(imported["id"]):
                errors.append(f"{label}.id must be a lowercase identifier")
            path = repo_root / str(imported["path"])
            if Path(str(imported["path"])).suffix.casefold() not in {".glb", ".gltf"}:
                errors.append(f"{label}.path must be a .glb or .gltf")
            elif not path.exists():
                errors.append(f"{label}.path does not exist: {imported['path']}")

    actors = spec.get("actors")
    actor_ids: set[str] = set()
    numeric_actor_ids: set[int] = set()
    if not isinstance(actors, list) or not actors:
        errors.append("actors must be a non-empty array")
        actors = []
    for index, actor in enumerate(actors):
        label = f"actors[{index}]"
        if not isinstance(actor, dict):
            errors.append(f"{label} must be an object")
            continue
        required = {"id", "actor_id", "display_name", "start", "keys"}
        missing = required - set(actor)
        unsupported = set(actor) - required - {
            "asset",
            "rig",
            "body_animation",
            "proxy",
            "interpolation",
            "rid_signature",
            *RID_ACTOR_CHANNELS,
        }
        if missing:
            errors.append(f"{label} missing fields: {', '.join(sorted(missing))}")
        if unsupported:
            errors.append(f"{label} has unsupported fields: {', '.join(sorted(unsupported))}")
        actor_key = actor.get("id")
        if not isinstance(actor_key, str) or not NAME_RE.fullmatch(actor_key):
            errors.append(f"{label}.id must be a lowercase identifier")
        elif actor_key in actor_ids:
            errors.append(f"Duplicate actor id: {actor_key}")
        else:
            actor_ids.add(actor_key)
        if "rid_signature" in actor and (
            not isinstance(actor["rid_signature"], str) or not actor["rid_signature"]
        ):
            errors.append(f"{label}.rid_signature must be a non-empty string")
        actor_id = actor.get("actor_id")
        if not isinstance(actor_id, int) or isinstance(actor_id, bool) or actor_id < 0:
            errors.append(f"{label}.actor_id must be a non-negative integer")
        elif actor_id in numeric_actor_ids:
            errors.append(f"Duplicate actor actor_id: {actor_id}")
        else:
            numeric_actor_ids.add(actor_id)
        if not isinstance(actor.get("display_name"), str) or not actor.get("display_name"):
            errors.append(f"{label}.display_name must be a non-empty string")
        if "start" in actor:
            _check_transform(actor["start"], f"{label}.start", errors)
            if isinstance(actor["start"], dict) and "location" not in actor["start"]:
                errors.append(f"{label}.start.location is required")
        interpolation = actor.get("interpolation", "LINEAR")
        if interpolation not in INTERPOLATIONS:
            errors.append(f"{label}.interpolation must be one of {', '.join(sorted(INTERPOLATIONS))}")
        if "asset" in actor:
            asset = actor["asset"]
            if not isinstance(asset, dict) or set(asset) - {"path", "armature"} or "path" not in asset:
                errors.append(f"{label}.asset must contain path and optional armature")
            else:
                path = repo_root / str(asset["path"])
                if Path(str(asset["path"])).suffix.casefold() not in {".glb", ".gltf"}:
                    errors.append(f"{label}.asset.path must be a .glb or .gltf")
                elif not path.exists():
                    errors.append(f"{label}.asset.path does not exist: {asset['path']}")
        rig_contract = None
        if "rig" in actor:
            rig_contract = _load_skeleton_contract(
                actor["rig"],
                f"{label}.rig",
                errors,
                repo_root=repo_root,
            )
            if "asset" not in actor:
                errors.append(f"{label}.rig requires an actor asset")
        if "body_animation" in actor:
            _check_body_animation(
                actor["body_animation"],
                f"{label}.body_animation",
                errors,
            )
            if rig_contract is None:
                errors.append(f"{label}.body_animation requires a valid rig")
        for channel in RID_ACTOR_CHANNELS:
            if channel in actor:
                _check_rid_actor_channel(
                    actor[channel],
                    f"{label}.{channel}",
                    errors,
                    repo_root=repo_root,
                )
        proxy = actor.get("proxy", {})
        if not isinstance(proxy, dict) or set(proxy) - {"height", "color"}:
            errors.append(f"{label}.proxy supports only height and color")
        else:
            height = proxy.get("height", 1.75)
            if not _is_number(height) or float(height) <= 0:
                errors.append(f"{label}.proxy.height must be greater than zero")
            if "color" in proxy:
                _check_vector(proxy["color"], 4, f"{label}.proxy.color", errors)
        keys = actor.get("keys", [])
        if not isinstance(keys, list):
            errors.append(f"{label}.keys must be an array")
            keys = []
        seen_frames: set[int] = set()
        last_frame: int | None = None
        for key_index, key in enumerate(keys):
            key_label = f"{label}.keys[{key_index}]"
            _check_transform(key, key_label, errors)
            frame = key.get("frame") if isinstance(key, dict) else None
            checked = _check_frame(frame, f"{key_label}.frame", frame_start, frame_end, errors)
            if checked is not None:
                if checked in seen_frames:
                    errors.append(f"{label}.keys has duplicate frame {checked}")
                if last_frame is not None and checked <= last_frame:
                    errors.append(f"{label}.keys must be strictly ordered by frame")
                seen_frames.add(checked)
                last_frame = checked

    camera = spec.get("recording_camera")
    if not isinstance(camera, dict):
        errors.append("recording_camera must be an object")
    else:
        required = {"id", "keys"}
        missing = required - set(camera)
        unsupported = set(camera) - required - {
            "recorded_actor",
            "interpolation",
            "rid_signature",
        }
        if missing:
            errors.append(f"recording_camera missing fields: {', '.join(sorted(missing))}")
        if unsupported:
            errors.append(f"recording_camera has unsupported fields: {', '.join(sorted(unsupported))}")
        if not isinstance(camera.get("id"), str) or not NAME_RE.fullmatch(str(camera.get("id", ""))):
            errors.append("recording_camera.id must be a lowercase identifier")
        if "rid_signature" in camera and (
            not isinstance(camera["rid_signature"], str) or not camera["rid_signature"]
        ):
            errors.append("recording_camera.rid_signature must be a non-empty string")
        if camera.get("recorded_actor") not in actor_ids:
            errors.append("recording_camera.recorded_actor must reference an actor id")
        if camera.get("interpolation", "LINEAR") not in INTERPOLATIONS:
            errors.append("recording_camera.interpolation is invalid")
        camera_keys = camera.get("keys", [])
        if not isinstance(camera_keys, list) or len(camera_keys) < 2:
            errors.append("recording_camera.keys must contain at least two keys")
            camera_keys = []
        last_frame = None
        seen_frames = set()
        for index, key in enumerate(camera_keys):
            label = f"recording_camera.keys[{index}]"
            _check_transform(key, label, errors, camera=True)
            if isinstance(key, dict) and "location" not in key:
                errors.append(f"{label}.location is required")
            frame = key.get("frame") if isinstance(key, dict) else None
            checked = _check_frame(frame, f"{label}.frame", frame_start, frame_end, errors)
            if checked is not None:
                if checked in seen_frames:
                    errors.append(f"recording_camera.keys has duplicate frame {checked}")
                if last_frame is not None and checked <= last_frame:
                    errors.append("recording_camera.keys must be strictly ordered by frame")
                seen_frames.add(checked)
                last_frame = checked

    clues = spec.get("clues", [])
    clue_ids: set[str] = set()
    if not isinstance(clues, list):
        errors.append("clues must be an array")
        clues = []
    for index, clue in enumerate(clues):
        label = f"clues[{index}]"
        required = {"id", "layer", "position", "frames", "fact"}
        if not isinstance(clue, dict) or set(clue) != required:
            errors.append(f"{label} must contain exactly {', '.join(sorted(required))}")
            continue
        clue_id = clue["id"]
        if not isinstance(clue_id, str) or not NAME_RE.fullmatch(clue_id):
            errors.append(f"{label}.id must be a lowercase identifier")
        elif clue_id in clue_ids:
            errors.append(f"Duplicate clue id: {clue_id}")
        else:
            clue_ids.add(clue_id)
        if clue["layer"] not in CLUE_LAYERS:
            errors.append(f"{label}.layer must be one of {', '.join(sorted(CLUE_LAYERS))}")
        _check_vector(clue["position"], 3, f"{label}.position", errors)
        clue_frames = clue["frames"]
        if not isinstance(clue_frames, list) or len(clue_frames) != 2:
            errors.append(f"{label}.frames must contain start and end")
        else:
            start = _check_frame(clue_frames[0], f"{label}.frames[0]", frame_start, frame_end, errors)
            end = _check_frame(clue_frames[1], f"{label}.frames[1]", frame_start, frame_end, errors)
            if start is not None and end is not None and end <= start:
                errors.append(f"{label}.frames end must be greater than start")
        if not isinstance(clue["fact"], str) or not clue["fact"]:
            errors.append(f"{label}.fact must be a non-empty string")

    markers = spec.get("markers", [])
    marker_names: set[str] = set()
    if not isinstance(markers, list):
        errors.append("markers must be an array")
        markers = []
    for index, marker in enumerate(markers):
        label = f"markers[{index}]"
        if not isinstance(marker, dict) or set(marker) != {"name", "frame"}:
            errors.append(f"{label} must contain exactly name and frame")
            continue
        marker_name = marker["name"]
        if not isinstance(marker_name, str) or not NAME_RE.fullmatch(marker_name):
            errors.append(f"{label}.name must be a lowercase identifier")
        elif marker_name in marker_names:
            errors.append(f"Duplicate marker name: {marker_name}")
        else:
            marker_names.add(marker_name)
        _check_frame(marker["frame"], f"{label}.frame", frame_start, frame_end, errors)

    if not clues:
        warnings.append("No braindance clues are declared")
    duration = (frame_end - frame_start) / fps if isinstance(fps, int) and fps > 0 else 0
    return ValidationReport(
        tuple(errors),
        tuple(warnings),
        {
            "name": name,
            "actor_count": len(actors),
            "clue_count": len(clues),
            "duration_seconds": duration,
            "frame_range": [frame_start, frame_end],
        },
    )


def normalized_plan(spec: dict[str, Any]) -> dict[str, Any]:
    """Return the stable contract consumed by Blender and the RID compiler."""
    actors = []
    for actor in spec["actors"]:
        row = copy.deepcopy(actor)
        row["performer_id"] = int(actor["actor_id"]) * 256 + 1
        row.setdefault("interpolation", "LINEAR")
        row.setdefault("proxy", {})
        row["proxy"].setdefault("height", 1.75)
        row["proxy"].setdefault("color", [0.35, 0.45, 0.8, 1.0])
        actors.append(row)
    camera = dict(spec["recording_camera"])
    camera.setdefault("interpolation", "LINEAR")
    return {
        "schema_version": SUPPORTED_SCHEMA_VERSION,
        "name": spec["name"],
        "fps": spec["fps"],
        "frames": spec["frames"],
        "outputs": spec["outputs"],
        "origin": spec["origin"],
        "environment": {
            "boxes": spec.get("environment", {}).get("boxes", []),
            "imports": spec.get("environment", {}).get("imports", []),
        },
        "actors": actors,
        "recording_camera": camera,
        "clues": spec.get("clues", []),
        "markers": spec.get("markers", []),
    }


def source_fingerprint(spec_path: Path) -> str:
    return hashlib.sha256(spec_path.read_bytes()).hexdigest()


def build_handoff_manifest(
    spec: dict[str, Any],
    spec_path: Path,
    *,
    repo_root: Path = ROOT,
) -> dict[str, Any]:
    plan = normalized_plan(spec)
    resolved_spec = spec_path.resolve()
    try:
        source_spec = resolved_spec.relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        source_spec = resolved_spec.as_posix()

    def actor_handoff(actor: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": actor["id"],
            "actor_id": actor["actor_id"],
            "performer_id": actor["performer_id"],
            "display_name": actor["display_name"],
            "rid_signature": actor.get("rid_signature", actor["id"]),
            "root_object": f"ACTOR_{actor['id']}",
            "asset": actor.get("asset"),
            "rig": _rig_summary(actor, repo_root=repo_root),
            "body_animation": actor.get("body_animation"),
            "facial": actor.get("facial"),
            "cyberware": actor.get("cyberware"),
            "transform_keys": actor["keys"],
            "interpolation": actor["interpolation"],
        }

    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_animation_handoff",
        "name": plan["name"],
        "source_spec": source_spec,
        "source_sha256": source_fingerprint(spec_path),
        "fps": plan["fps"],
        "frames": plan["frames"],
        "origin": plan["origin"],
        "actors": [actor_handoff(actor) for actor in plan["actors"]],
        "recording_camera": {
            **plan["recording_camera"],
            "rid_signature": plan["recording_camera"].get("rid_signature", "Camera"),
            "object": f"CAMERA_{plan['recording_camera']['id']}",
        },
        "clues": [
            {**clue, "object": f"CLUE_{clue['id']}"}
            for clue in plan["clues"]
        ],
        "markers": plan["markers"],
        "rid_status": "requires_blender_bake",
    }


def resolve_repo_path(path: str, *, repo_root: Path = ROOT) -> Path:
    candidate = (repo_root / path).resolve()
    try:
        candidate.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise BraindanceBuildError(f"Path escapes repository root: {path}") from exc
    return candidate


def find_blender(explicit: Path | None = None) -> Path:
    candidates: list[Path] = []
    if explicit is not None:
        candidates.append(explicit)
    configured = os.environ.get("GHOSTLINE_BLENDER")
    if configured:
        candidates.append(Path(configured))
    discovered = shutil.which("blender")
    if discovered:
        candidates.append(Path(discovered))
    foundation = Path(r"C:\Program Files\Blender Foundation")
    if foundation.exists():
        candidates.extend(
            sorted(foundation.glob("Blender */blender.exe"), reverse=True)
        )
    steam = Path(r"C:\Program Files\Steam\steamapps\common\Blender\blender.exe")
    candidates.append(steam)
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise BraindanceBuildError(
        "Blender was not found; pass --blender or set GHOSTLINE_BLENDER"
    )


def print_report(report: ValidationReport) -> None:
    payload = {
        "ok": report.ok,
        "errors": list(report.errors),
        "warnings": list(report.warnings),
        "details": report.details,
    }
    print(json.dumps(payload, indent=2))


def build_command(
    blender: Path,
    spec_path: Path,
    *,
    repo_root: Path = ROOT,
    no_glb: bool = False,
    bake_existing: bool = False,
) -> list[str]:
    command = [
        str(blender),
        "--background",
        "--factory-startup",
        "--python",
        str(BLENDER_RUNNER),
        "--",
        "--spec",
        str(spec_path.resolve()),
        "--repo-root",
        str(repo_root.resolve()),
    ]
    if no_glb:
        command.append("--no-glb")
    if bake_existing:
        command.append("--bake-existing")
    return command


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate")
    validate.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    plan = subparsers.add_parser("plan")
    plan.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    build = subparsers.add_parser("build")
    build.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    build.add_argument("--blender", type=Path)
    build.add_argument("--dry-run", action="store_true")
    build.add_argument("--no-glb", action="store_true")
    bake = subparsers.add_parser(
        "bake",
        help="Bake evaluated animation samples from the existing .blend",
    )
    bake.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    bake.add_argument("--blender", type=Path)
    bake.add_argument("--dry-run", action="store_true")
    bake.add_argument("--no-glb", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    spec_path = args.spec.resolve()
    try:
        spec = load_json(spec_path)
        report = validate_spec(spec)
        if args.command == "validate":
            print_report(report)
            return 0 if report.ok else 1
        if not report.ok:
            print_report(report)
            return 1
        if args.command == "plan":
            print(json.dumps(normalized_plan(spec), indent=2))
            return 0

        blender = find_blender(args.blender)
        command = build_command(
            blender,
            spec_path,
            no_glb=args.no_glb,
            bake_existing=args.command == "bake",
        )
        if args.dry_run:
            print(json.dumps({"command": command, "plan": normalized_plan(spec)}, indent=2))
            return 0
        completed = subprocess.run(
            command,
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.stdout:
            print(completed.stdout, end="")
        if completed.stderr:
            print(completed.stderr, end="", file=sys.stderr)
        marker = "GHOSTLINE_BRAINDANCE_COMPLETE "
        if completed.returncode != 0 or marker not in completed.stdout:
            raise BraindanceBuildError(
                "Blender scene build did not report successful completion "
                f"(exit code {completed.returncode})"
            )
        outputs = {
            key: str(resolve_repo_path(value))
            for key, value in spec["outputs"].items()
            if not (args.no_glb and key == "glb")
        }
        missing = [path for path in outputs.values() if not Path(path).is_file()]
        if missing:
            raise BraindanceBuildError(
                "Blender reported completion but outputs are missing: "
                + ", ".join(missing)
            )
        print(json.dumps({"ok": True, "outputs": outputs}, indent=2))
        return 0
    except BraindanceBuildError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
