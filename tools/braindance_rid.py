#!/usr/bin/env python3
"""Compile evaluated Blender animation into a RED ``.scenerid``.

A vanilla RID supplies only compatible reflected layouts, handle shapes, and
actor rig cardinality. Actor root motion, rigged pose-bone channels, camera
transform, and focal length are sampled in Blender and encoded into new RED
compressed-animation buffers. WolvenKit is used only for the CR2W/JSON
boundary because the project's generic writer does not yet decode these custom
buffer payloads.
"""

from __future__ import annotations

import argparse
import base64
import bisect
import copy
import hashlib
import json
import math
import shutil
import struct
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HANDOFF = (
    ROOT
    / ".tmp"
    / "braindance"
    / "gqt005"
    / "gqt005_braindance_analysis.handoff.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / ".tmp"
    / "braindance"
    / "gqt005"
    / "gqt005_braindance_analysis.scenerid"
)
WOLVENKIT_CLI = (
    ROOT
    / "WolvenKit"
    / "WolvenKit.CLI"
    / "bin"
    / "Release"
    / "net8.0"
    / "WolvenKit.CLI.exe"
)
RID_KIND = "ghostline_braindance_animation_handoff"
RID_REPORT_KIND = "ghostline_braindance_rid_report"
CR2W_MAGIC = b"CR2W"
ANIMATION_SAMPLE_SPACE = "blender_local_z_up_right_handed"
# Preserve the padding pattern seen in the selected vanilla man_base layout.
# RED ignores this aligned word, but matching the layout keeps binary audits
# deterministic.
CONST_TRANSLATION_AUX = 0x9C3F
# Matching padding for vanilla KeyFrameConstTrack records.
CONST_TRACK_AUX = 0x3454


class RidCompileError(RuntimeError):
    """Raised for an invalid handoff, template, or compiler result."""


@dataclass(frozen=True)
class RidValidationReport:
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
        raise RidCompileError(f"JSON does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RidCompileError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RidCompileError(f"JSON root must be an object: {path}")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _root(document: dict[str, Any]) -> dict[str, Any]:
    try:
        root = document["Data"]["RootChunk"]
    except (KeyError, TypeError) as exc:
        raise RidCompileError("Template is missing Data.RootChunk") from exc
    if not isinstance(root, dict) or root.get("$type") != "scnRidResource":
        raise RidCompileError("Template RootChunk must be a scnRidResource")
    return root


def _cname(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        inner = value.get("$value")
        return inner if isinstance(inner, str) else None
    return None


def _serial(value: Any) -> int | None:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, dict):
        inner = value.get("serialNumber")
        return inner if isinstance(inner, int) and not isinstance(inner, bool) else None
    return None


def _set_cname(container: dict[str, Any], key: str, text: str) -> None:
    current = container.get(key)
    if isinstance(current, dict):
        current["$value"] = text
        current.setdefault("$type", "CName")
        current.setdefault("$storage", "string")
    else:
        container[key] = {
            "$type": "CName",
            "$storage": "string",
            "$value": text,
        }


def _set_serial(tag: dict[str, Any], value: int) -> None:
    current = tag.get("serialNumber")
    if isinstance(current, dict):
        current["serialNumber"] = value
        current.setdefault("$type", "scnRidSerialNumber")
    else:
        tag["serialNumber"] = {
            "$type": "scnRidSerialNumber",
            "serialNumber": value,
        }


def _tag_signature(record: dict[str, Any]) -> str | None:
    tag = record.get("tag")
    return _cname(tag.get("signature")) if isinstance(tag, dict) else None


def _set_tag(record: dict[str, Any], signature: str, serial: int) -> None:
    tag = record.get("tag")
    if not isinstance(tag, dict):
        tag = {"$type": "scnRidTag"}
        record["tag"] = tag
    _set_cname(tag, "signature", signature)
    _set_serial(tag, serial)


def _set_next_serial(root: dict[str, Any], value: int) -> None:
    current = root.get("nextSerialNumber")
    if isinstance(current, dict):
        current["serialNumber"] = value
        current.setdefault("$type", "scnRidSerialNumber")
    else:
        root["nextSerialNumber"] = {
            "$type": "scnRidSerialNumber",
            "serialNumber": value,
        }


def _set_animation_name(animation_rid: dict[str, Any], value: str) -> None:
    animation = animation_rid.get("animation")
    if not isinstance(animation, dict):
        raise RidCompileError("Actor animation template has no animation handle")
    data = animation.get("Data")
    if not isinstance(data, dict) or data.get("$type") != "animAnimation":
        raise RidCompileError("Actor animation handle must contain animAnimation")
    _set_cname(data, "name", value)


def _patch_durations(value: Any, duration: float) -> None:
    """Retimes duration-bearing template objects without touching key bytes."""
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "duration" and isinstance(child, (int, float)) and not isinstance(child, bool):
                value[key] = duration
            else:
                _patch_durations(child, duration)
    elif isinstance(value, list):
        for child in value:
            _patch_durations(child, duration)


def _multiply_quaternions(
    left: tuple[float, float, float, float],
    right: tuple[float, float, float, float],
) -> tuple[float, float, float, float]:
    lx, ly, lz, lw = left
    rx, ry, rz, rw = right
    return (
        lw * rx + lx * rw + ly * rz - lz * ry,
        lw * ry - lx * rz + ly * rw + lz * rx,
        lw * rz + lx * ry - ly * rx + lz * rw,
        lw * rw - lx * rx - ly * ry - lz * rz,
    )


def _rotate_vector(
    quaternion: tuple[float, float, float, float],
    vector: Iterable[float],
) -> tuple[float, float, float]:
    x, y, z, w = quaternion
    vx, vy, vz = (float(item) for item in vector)
    vector_quaternion = (vx, vy, vz, 0.0)
    conjugate = (-x, -y, -z, w)
    rotated = _multiply_quaternions(
        _multiply_quaternions(quaternion, vector_quaternion),
        conjugate,
    )
    return rotated[0], rotated[1], rotated[2]


def euler_degrees_to_quaternion(values: Iterable[float]) -> tuple[float, float, float, float]:
    """Return an XYZ Euler rotation as RED's i/j/k/r quaternion."""
    x, y, z = (math.radians(float(item)) / 2.0 for item in values)
    qx = (math.sin(x), 0.0, 0.0, math.cos(x))
    qy = (0.0, math.sin(y), 0.0, math.cos(y))
    qz = (0.0, 0.0, math.sin(z), math.cos(z))
    return _multiply_quaternions(_multiply_quaternions(qz, qy), qx)


def look_at_quaternion(
    location: Iterable[float],
    target: Iterable[float],
) -> tuple[float, float, float, float]:
    """Aim RED camera local +Y at a target with local +Z as up."""
    px, py, pz = (float(item) for item in location)
    tx, ty, tz = (float(item) for item in target)
    dx, dy, dz = tx - px, ty - py, tz - pz
    horizontal = math.hypot(dx, dy)
    if horizontal == 0.0 and dz == 0.0:
        raise RidCompileError("Camera look_at target cannot equal its location")
    yaw = math.atan2(-dx, dy)
    pitch = math.atan2(dz, horizontal)
    qx = (math.sin(pitch / 2.0), 0.0, 0.0, math.cos(pitch / 2.0))
    qz = (0.0, 0.0, math.sin(yaw / 2.0), math.cos(yaw / 2.0))
    return _multiply_quaternions(qz, qx)


def _red_transform(
    location: Iterable[float],
    quaternion: tuple[float, float, float, float],
    *,
    final_w: float = 0.0,
) -> dict[str, Any]:
    x, y, z = (float(item) for item in location)
    i, j, k, r = quaternion
    return {
        "$type": "Transform",
        "orientation": {
            "$type": "Quaternion",
            "i": i,
            "j": j,
            "k": k,
            "r": r,
        },
        "position": {
            "$type": "Vector4",
            "W": float(final_w),
            "X": x,
            "Y": y,
            "Z": z,
        },
    }


def _world_actor_transform(
    actor_key: dict[str, Any],
    origin: dict[str, Any],
) -> dict[str, Any]:
    location = [float(item) for item in actor_key["location"]]
    rotation = [
        float(item) for item in actor_key.get("rotation_degrees", [0.0, 0.0, 0.0])
    ]
    origin_location = [float(item) for item in origin.get("location", [0.0, 0.0, 0.0])]
    origin_rotation = [
        float(item) for item in origin.get("rotation_degrees", [0.0, 0.0, 0.0])
    ]
    origin_quaternion = euler_degrees_to_quaternion(origin_rotation)
    rotated_location = _rotate_vector(origin_quaternion, location)
    world_location = (
        origin_location[0] + rotated_location[0],
        origin_location[1] + rotated_location[1],
        origin_location[2] + rotated_location[2],
    )
    world_quaternion = _multiply_quaternions(
        origin_quaternion,
        euler_degrees_to_quaternion(rotation),
    )
    return _red_transform(world_location, world_quaternion)


def _camera_trajectory(handoff: dict[str, Any]) -> list[dict[str, Any]]:
    camera = handoff["recording_camera"]
    origin = handoff.get("origin", {})
    origin_location = [
        float(item) for item in origin.get("location", [0.0, 0.0, 0.0])
    ]
    origin_quaternion = euler_degrees_to_quaternion(
        origin.get("rotation_degrees", [0.0, 0.0, 0.0])
    )
    fps = float(handoff["fps"])
    first_frame = int(handoff["frames"]["start"])
    keys = camera["keys"]
    trajectory: list[dict[str, Any]] = []
    for index, key in enumerate(keys):
        rotated_location = _rotate_vector(origin_quaternion, key["location"])
        world_location = tuple(
            origin_location[axis] + rotated_location[axis] for axis in range(3)
        )
        if "look_at" in key:
            rotated_target = _rotate_vector(origin_quaternion, key["look_at"])
            world_target = tuple(
                origin_location[axis] + rotated_target[axis] for axis in range(3)
            )
            quaternion = look_at_quaternion(world_location, world_target)
        else:
            quaternion = _multiply_quaternions(
                origin_quaternion,
                euler_degrees_to_quaternion(key["rotation_degrees"]),
            )
        trajectory.append(
            {
                "$type": "scnAnimationMotionSample",
                "time": (int(key["frame"]) - first_frame) / fps,
                "transform": _red_transform(
                    world_location,
                    quaternion,
                    final_w=1.0 if index == len(keys) - 1 else 0.0,
                ),
            }
        )
    return trajectory


def _sample_time(frame: int, samples: dict[str, Any]) -> float:
    return (frame - int(samples["frame_start"])) / float(samples["sample_rate"])


def _is_near_vector(
    values: Iterable[float],
    expected: Iterable[float],
    *,
    tolerance: float = 1e-6,
) -> bool:
    return all(
        math.isclose(float(value), float(target), abs_tol=tolerance)
        for value, target in zip(values, expected, strict=True)
    )


def _continuous_quaternions(
    samples: list[dict[str, Any]],
) -> list[tuple[int, tuple[float, float, float, float]]]:
    result: list[tuple[int, tuple[float, float, float, float]]] = []
    previous: tuple[float, float, float, float] | None = None
    for sample in samples:
        quaternion = tuple(float(value) for value in sample["rotation"])
        length = math.sqrt(sum(value * value for value in quaternion))
        if length == 0.0:
            raise RidCompileError("Animation sample contains a zero quaternion")
        quaternion = tuple(value / length for value in quaternion)
        if previous is not None and sum(
            left * right for left, right in zip(previous, quaternion, strict=True)
        ) < 0.0:
            quaternion = tuple(-value for value in quaternion)
        result.append((int(sample["frame"]), quaternion))
        previous = quaternion
    return result


def _pack_time(time: float, duration: float) -> int:
    if duration <= 0.0:
        raise RidCompileError("Animation duration must be greater than zero")
    return max(0, min(65535, int(time / duration * 65535.0)))


def _pack_raw_transform_key(
    time: float,
    duration: float,
    joint_index: int,
    component: int,
    values: Iterable[float],
) -> bytes:
    if not 0 <= joint_index <= 0x1FFF:
        raise RidCompileError(f"Joint index is outside RED key range: {joint_index}")
    normalized_time = _pack_time(time, duration)
    value_list = [float(value) for value in values]
    w_sign = False
    if component == 1:
        if len(value_list) != 4:
            raise RidCompileError("Rotation keys need four quaternion values")
        x, y, z, w = value_list
        length = math.sqrt(x * x + y * y + z * z + w * w)
        if length == 0.0:
            raise RidCompileError("Rotation key contains a zero quaternion")
        x, y, z, w = x / length, y / length, z / length, w / length
        w_sign = w < 0.0
        denominator = math.sqrt(1.0 + abs(w))
        value_list = [x / denominator, y / denominator, z / denominator]
    elif len(value_list) != 3:
        raise RidCompileError("Translation and scale keys need three values")
    bitwise = joint_index | (component << 13)
    if w_sign:
        bitwise |= 1 << 15
    return struct.pack(
        "<HHfff",
        normalized_time,
        bitwise,
        value_list[0],
        value_list[1],
        value_list[2],
    )


def _pack_const_transform_key(
    joint_index: int,
    component: int,
    values: Iterable[float],
) -> bytes:
    """Pack one constant transform channel in RED's 16-byte key layout."""
    if not 0 <= joint_index <= 0x1FFF:
        raise RidCompileError(f"Joint index is outside RED key range: {joint_index}")
    value_list = [float(value) for value in values]
    w_sign = False
    if component == 1:
        if len(value_list) != 4:
            raise RidCompileError("Rotation keys need four quaternion values")
        x, y, z, w = value_list
        length = math.sqrt(x * x + y * y + z * z + w * w)
        if length == 0.0:
            raise RidCompileError("Rotation key contains a zero quaternion")
        x, y, z, w = x / length, y / length, z / length, w / length
        w_sign = w < 0.0
        denominator = math.sqrt(1.0 + abs(w))
        value_list = [x / denominator, y / denominator, z / denominator]
    elif len(value_list) != 3:
        raise RidCompileError("Translation and scale keys need three values")
    bitwise = joint_index | (component << 13)
    if w_sign:
        bitwise |= 1 << 15
    auxiliary = CONST_TRANSLATION_AUX if component == 0 else 0
    return struct.pack(
        "<HHfff",
        bitwise,
        auxiliary,
        value_list[0],
        value_list[1],
        value_list[2],
    )


def _pack_track_key(
    time: float,
    duration: float,
    track_index: int,
    value: float,
    *,
    constant: bool,
) -> bytes:
    if constant:
        return struct.pack("<HHf", track_index, CONST_TRACK_AUX, float(value))
    normalized_time = _pack_time(time, duration)
    return struct.pack("<HHf", normalized_time, track_index, float(value))


def _raw_transform_key_sort_key(payload: bytes) -> tuple[int, int, int]:
    normalized_time, bitwise = struct.unpack_from("<HH", payload)
    return (
        bitwise & 0x1FFF,
        normalized_time,
        (bitwise & 0x6000) >> 13,
    )


def _const_transform_key_sort_key(payload: bytes) -> tuple[int, int]:
    (bitwise,) = struct.unpack_from("<H", payload)
    component = (bitwise & 0x6000) >> 13
    # Vanilla buffers store a joint's rotation before its translation.
    component_order = {1: 0, 0: 1, 2: 2}
    return bitwise & 0x1FFF, component_order.get(component, component + 3)


def _unpack_raw_transform_key(
    payload: bytes,
    *,
    duration: float,
) -> tuple[float, int, int, tuple[float, ...]]:
    normalized_time, bitwise, x, y, z = struct.unpack("<HHfff", payload)
    component = (bitwise & 0x6000) >> 13
    joint_index = bitwise & 0x1FFF
    if component == 1:
        dot = x * x + y * y + z * z
        multiplier = math.sqrt(max(0.0, 2.0 - dot))
        w = 1.0 - dot
        if bitwise & 0x8000:
            w = -w
        values: tuple[float, ...] = (
            x * multiplier,
            y * multiplier,
            z * multiplier,
            w,
        )
    else:
        values = (x, y, z)
    return (
        normalized_time / 65535.0 * duration,
        joint_index,
        component,
        values,
    )


def _interpolate_pose_values(
    rows: list[tuple[float, tuple[float, ...]]],
    source_time: float,
    *,
    rotation: bool,
) -> tuple[float, ...]:
    times = [row[0] for row in rows]
    upper = bisect.bisect_left(times, source_time)
    if upper <= 0:
        return rows[0][1]
    if upper >= len(rows):
        return rows[-1][1]
    before_time, before = rows[upper - 1]
    after_time, after = rows[upper]
    if math.isclose(after_time, before_time, abs_tol=1e-9):
        return after
    amount = (source_time - before_time) / (after_time - before_time)
    if rotation and sum(
        left * right for left, right in zip(before, after, strict=True)
    ) < 0.0:
        after = tuple(-value for value in after)
    values = tuple(
        left + (right - left) * amount
        for left, right in zip(before, after, strict=True)
    )
    if not rotation:
        return values
    length = math.sqrt(sum(value * value for value in values))
    if length <= 1e-12:
        return before
    return tuple(value / length for value in values)


def _motion_extraction_positions(
    motion_extraction: Any,
) -> list[tuple[float, tuple[float, float, float]]]:
    data = (
        motion_extraction.get("Data")
        if isinstance(motion_extraction, dict)
        else None
    )
    if (
        not isinstance(data, dict)
        or data.get("$type") != "animSplineCompressedMotionExtraction"
    ):
        return []
    duration = data.get("duration")
    values = data.get("posKeysData")
    if (
        not isinstance(duration, (int, float))
        or float(duration) <= 0.0
        or not isinstance(values, list)
        or len(values) < 32
        or len(values) % 16
        or any(
            not isinstance(value, int) or not 0 <= value <= 255
            for value in values
        )
    ):
        return []
    rows: list[tuple[float, tuple[float, float, float]]] = []
    previous_time = -1.0
    payload = bytes(values)
    for offset in range(0, len(payload), 16):
        time, joint_index, component, decoded = _unpack_raw_transform_key(
            payload[offset : offset + 16],
            duration=float(duration),
        )
        if joint_index != 0 or component != 0 or time < previous_time:
            return []
        previous_time = time
        rows.append((time, (decoded[0], decoded[1], decoded[2])))
    return rows


def _longest_locomotion_segment(
    rows: list[tuple[float, tuple[float, float, float]]],
    *,
    minimum_speed: float = 0.2,
    maximum_gap: float = 0.25,
    minimum_distance: float = 0.25,
) -> tuple[int, int] | None:
    moving: list[tuple[int, float]] = []
    for index, ((before_time, before), (after_time, after)) in enumerate(
        zip(rows, rows[1:], strict=False)
    ):
        elapsed = after_time - before_time
        if elapsed <= 0.0:
            continue
        distance = math.dist(before, after)
        if distance / elapsed >= minimum_speed:
            moving.append((index, distance))
    if not moving:
        return None
    groups: list[list[tuple[int, float]]] = []
    for interval in moving:
        if (
            groups
            and rows[interval[0]][0]
            - rows[groups[-1][-1][0] + 1][0]
            <= maximum_gap
        ):
            groups[-1].append(interval)
        else:
            groups.append([interval])
    best = max(
        groups,
        key=lambda group: sum(distance for _, distance in group),
    )
    start_index = best[0][0]
    end_index = best[-1][0] + 1
    distance = sum(
        math.dist(rows[index][1], rows[index + 1][1])
        for index in range(start_index, end_index)
    )
    if distance < minimum_distance:
        return None
    return start_index, end_index


def _proxy_pose_motion_sync(
    *,
    source_motion_extraction: Any,
    trajectory_joint: dict[str, Any],
    sample_contract: dict[str, Any],
) -> dict[str, Any] | None:
    """Build a donor-pose clock driven by authored root travel.

    A proxy has no skeletal bake, so its body pose comes from the selected
    vanilla actor. The donor's motion-extraction curve identifies the exact
    portion of that performance containing locomotion. Advancing that pose by
    authored travel distance keeps footsteps active while the proxy moves and
    freezes them while its root is stationary.
    """

    source_rows = _motion_extraction_positions(source_motion_extraction)
    source_segment = _longest_locomotion_segment(source_rows)
    samples = trajectory_joint.get("samples")
    if source_segment is None or not isinstance(samples, list) or len(samples) < 2:
        return None
    start_index, end_index = source_segment
    source_path = source_rows[start_index : end_index + 1]
    source_distances = [0.0]
    for (_, before), (_, after) in zip(source_path, source_path[1:], strict=False):
        source_distances.append(
            source_distances[-1] + math.dist(before, after)
        )
    source_distance = source_distances[-1]
    if source_distance <= 0.0:
        return None

    authored_distances = [0.0]
    previous = tuple(float(value) for value in samples[0]["translation"])
    for sample in samples[1:]:
        current = tuple(float(value) for value in sample["translation"])
        authored_distances.append(
            authored_distances[-1] + math.dist(previous, current)
        )
        previous = current
    authored_distance = authored_distances[-1]
    if authored_distance <= 1e-4:
        return None
    distance_scale = min(1.0, source_distance / authored_distance)
    source_times: list[tuple[int, float]] = []
    for sample, authored_travel in zip(samples, authored_distances, strict=True):
        source_travel = authored_travel * distance_scale
        upper = bisect.bisect_left(source_distances, source_travel)
        if upper <= 0:
            source_time = source_path[0][0]
        elif upper >= len(source_path):
            source_time = source_path[-1][0]
        else:
            before_distance = source_distances[upper - 1]
            after_distance = source_distances[upper]
            amount = (
                0.0
                if math.isclose(after_distance, before_distance, abs_tol=1e-9)
                else (source_travel - before_distance)
                / (after_distance - before_distance)
            )
            source_time = (
                source_path[upper - 1][0]
                + (source_path[upper][0] - source_path[upper - 1][0])
                * amount
            )
        source_times.append((int(sample["frame"]), source_time))
    frozen_samples = sum(
        math.isclose(before, after, abs_tol=1e-9)
        for before, after in zip(
            authored_distances,
            authored_distances[1:],
            strict=False,
        )
    )
    return {
        "source_times": source_times,
        "details": {
            "mode": "authored_travel_distance",
            "source_start_seconds": source_path[0][0],
            "source_end_seconds": source_path[-1][0],
            "source_path_distance": source_distance,
            "authored_path_distance": authored_distance,
            "distance_scale": distance_scale,
            "sample_count": len(source_times),
            "frozen_samples": frozen_samples,
        },
    }


def encode_compressed_animation(
    joints: list[dict[str, Any]],
    *,
    sample_contract: dict[str, Any],
    duration: float,
    num_joints: int,
    num_extra_joints: int = 0,
    num_tracks: int = 0,
    num_extra_tracks: int = 0,
    track_samples: dict[int, list[tuple[float, float]]] | None = None,
    const_tracks: dict[int, tuple[float, float]] | None = None,
    force_channels: set[tuple[int, str]] | None = None,
    exclude_channels: set[tuple[int, str]] | None = None,
) -> dict[str, Any]:
    raw_keys: list[bytes] = []
    const_keys: list[bytes] = []
    emitted_channels: list[dict[str, Any]] = []
    scale_constant = True
    for joint in sorted(joints, key=lambda item: int(item["index"])):
        joint_index = int(joint["index"])
        if joint_index >= num_joints:
            raise RidCompileError(
                f"Authored joint {joint_index} exceeds template joint count {num_joints}"
            )
        samples = joint.get("samples")
        if not isinstance(samples, list) or not samples:
            raise RidCompileError(f"Joint {joint_index} has no animation samples")
        translations = [
            (int(sample["frame"]), tuple(float(value) for value in sample["translation"]))
            for sample in samples
        ]
        scales = [
            (int(sample["frame"]), tuple(float(value) for value in sample["scale"]))
            for sample in samples
        ]
        rotations = _continuous_quaternions(samples)
        channels = (
            ("translation", 0, translations, (0.0, 0.0, 0.0)),
            ("scale", 2, scales, (1.0, 1.0, 1.0)),
            ("rotation", 1, rotations, (0.0, 0.0, 0.0, 1.0)),
        )
        for channel_name, component, values, default in channels:
            if (joint_index, channel_name) in (exclude_channels or set()):
                continue
            # Blender/glTF round trips introduce sub-micrometre scale noise.
            # man_base has no authored scale animation, and turning that noise
            # into a raw scale channel switches RED to an unstable decode path.
            if channel_name == "scale" and all(
                _is_near_vector(value, default, tolerance=1e-4)
                for _, value in values
            ):
                continue
            constant_value = values[0][1]
            is_constant = all(
                _is_near_vector(value, constant_value, tolerance=1e-5)
                for _, value in values[1:]
            )
            if (
                (joint_index, channel_name) not in (force_channels or set())
                and all(_is_near_vector(value, default) for _, value in values)
            ):
                continue
            if channel_name == "scale":
                scale_constant = False
            storage = "constant" if is_constant else "raw"
            if is_constant:
                const_keys.append(
                    _pack_const_transform_key(
                        joint_index,
                        component,
                        constant_value,
                    )
                )
            else:
                for frame, value in values:
                    raw_keys.append(
                        _pack_raw_transform_key(
                            _sample_time(frame, sample_contract),
                            duration,
                            joint_index,
                            component,
                            value,
                        )
                    )
            emitted_channels.append(
                {
                    "joint_index": joint_index,
                    "joint_name": joint.get("name"),
                    "channel": channel_name,
                    "sample_count": 1 if is_constant else len(values),
                    "storage": storage,
                }
            )
    raw_keys.sort(key=_raw_transform_key_sort_key)
    const_keys.sort(key=_const_transform_key_sort_key)
    track_keys: list[bytes] = []
    for track_index, values in sorted((track_samples or {}).items()):
        if not 0 <= track_index < num_tracks:
            raise RidCompileError(
                f"Track index {track_index} exceeds track count {num_tracks}"
            )
        for time, value in values:
            track_keys.append(
                _pack_track_key(time, duration, track_index, value, constant=False)
            )
    constant_track_keys: list[bytes] = []
    for track_index, (time, value) in sorted((const_tracks or {}).items()):
        if not 0 <= track_index < num_tracks:
            raise RidCompileError(
                f"Track index {track_index} exceeds track count {num_tracks}"
            )
        constant_track_keys.append(
            _pack_track_key(time, duration, track_index, value, constant=True)
        )
    payload = b"".join(
        raw_keys + const_keys + track_keys + constant_track_keys
    )
    frame_count = (
        int(sample_contract["frame_end"]) - int(sample_contract["frame_start"]) + 1
    )
    return {
        "bytes": payload,
        "bytes_base64": base64.b64encode(payload).decode("ascii"),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "num_frames": frame_count,
        "num_joints": num_joints,
        "num_extra_joints": num_extra_joints,
        "num_tracks": num_tracks,
        "num_extra_tracks": num_extra_tracks,
        "num_anim_keys": 0,
        "num_anim_keys_raw": len(raw_keys),
        "num_const_anim_keys": len(const_keys),
        "num_track_keys": len(track_keys),
        "num_const_track_keys": len(constant_track_keys),
        "is_scale_constant": scale_constant,
        "has_raw_rotations": True,
        "emitted_channels": emitted_channels,
    }


def _encode_spline_motion_extraction(
    trajectory_joint: dict[str, Any],
    *,
    sample_contract: dict[str, Any],
    duration: float,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Encode authored trajectory samples using vanilla BD root-motion layout.

    RED's motion-extraction payload always identifies the logical root as
    joint zero.  ``scnAnimationRid.trajectoryBoneIndex`` remains the rig
    trajectory joint (normally one); the two indices are separate contracts.
    """

    samples = trajectory_joint.get("samples")
    if not isinstance(samples, list) or len(samples) < 2:
        raise RidCompileError("Trajectory joint needs at least two samples")
    translations = [
        (
            int(sample["frame"]),
            tuple(float(value) for value in sample["translation"]),
        )
        for sample in samples
    ]
    rotations = _continuous_quaternions(samples)
    position_keys = b"".join(
        _pack_raw_transform_key(
            _sample_time(frame, sample_contract),
            duration,
            0,
            0,
            value,
        )
        for frame, value in translations
    )
    rotation_keys = b"".join(
        _pack_raw_transform_key(
            _sample_time(frame, sample_contract),
            duration,
            0,
            1,
            value,
        )
        for frame, value in rotations
    )
    data = {
        "$type": "animSplineCompressedMotionExtraction",
        "duration": duration,
        "posKeysData": list(position_keys),
        "rotKeysData": list(rotation_keys),
    }
    return data, {
        "type": data["$type"],
        "position_keys": len(position_keys) // 16,
        "rotation_keys": len(rotation_keys) // 16,
        "position_sha256": hashlib.sha256(position_keys).hexdigest(),
        "rotation_sha256": hashlib.sha256(rotation_keys).hexdigest(),
    }


def _animation_buffer_from_actor(body: dict[str, Any]) -> dict[str, Any]:
    animation = body.get("animation")
    data = animation.get("Data") if isinstance(animation, dict) else None
    anim_buffer = data.get("animBuffer") if isinstance(data, dict) else None
    buffer_data = anim_buffer.get("Data") if isinstance(anim_buffer, dict) else None
    if not isinstance(buffer_data, dict) or buffer_data.get("$type") != "animAnimationBufferCompressed":
        raise RidCompileError("Actor template requires animAnimationBufferCompressed")
    return buffer_data


def _animation_buffer_from_camera(camera_animation: dict[str, Any]) -> dict[str, Any]:
    animation = camera_animation.get("animation")
    data = animation.get("Data") if isinstance(animation, dict) else None
    if not isinstance(data, dict) or data.get("$type") != "animAnimationBufferCompressed":
        raise RidCompileError("Camera template requires animAnimationBufferCompressed")
    return data


def _merge_template_pose_channels(
    encoded: dict[str, Any],
    template_buffer: dict[str, Any],
    *,
    authored_channels: set[tuple[int, int]],
    source_duration: float | None = None,
    destination_duration: float | None = None,
    sample_contract: dict[str, Any] | None = None,
    motion_sync: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Retain template skeletal channels missing from a proxy-only bake.

    A proxy Blender actor supplies only its trajectory joint. Real RED actor
    rigs still require the remaining pose channels from a compatible layout;
    omitting them collapses the skinned mesh. When the donor supplies a usable
    locomotion curve, its pose is resampled against authored travel instead of
    merely compressing the donor's complete scene timeline.
    """

    counts = {
        "anim": int(template_buffer.get("numAnimKeys", 0)),
        "raw": int(template_buffer.get("numAnimKeysRaw", 0)),
        "const": int(template_buffer.get("numConstAnimKeys", 0)),
        "track": int(template_buffer.get("numTrackKeys", 0)),
        "const_track": int(template_buffer.get("numConstTrackKeys", 0)),
    }
    if counts["raw"] + counts["const"] == 0:
        encoded["template_pose_fallback"] = {
            "raw_transform_keys": 0,
            "const_transform_keys": 0,
        }
        return encoded
    if counts["anim"]:
        raise RidCompileError(
            "Proxy pose fallback requires a raw-key actor template"
        )
    deferred = template_buffer.get("defferedBuffer")
    source_base64 = deferred.get("Bytes") if isinstance(deferred, dict) else None
    if not isinstance(source_base64, str):
        raise RidCompileError(
            "Proxy pose fallback template has no deferred animation bytes"
        )
    try:
        source_payload = base64.b64decode(source_base64, validate=True)
    except ValueError as exc:
        raise RidCompileError(
            "Proxy pose fallback template has invalid deferred animation bytes"
        ) from exc
    expected_size = (
        counts["raw"] * 16
        + counts["const"] * 16
        + counts["track"] * 8
        + counts["const_track"] * 8
    )
    if len(source_payload) != expected_size:
        raise RidCompileError(
            "Proxy pose fallback template key counts do not match its "
            f"{len(source_payload)} deferred bytes"
        )

    source_raw_end = counts["raw"] * 16
    source_const_end = source_raw_end + counts["const"] * 16
    source_raw = [
        source_payload[offset : offset + 16]
        for offset in range(0, source_raw_end, 16)
    ]
    source_const = [
        source_payload[offset : offset + 16]
        for offset in range(source_raw_end, source_const_end, 16)
    ]

    def raw_channel(payload: bytes) -> tuple[int, int]:
        _, bitwise = struct.unpack_from("<HH", payload)
        return bitwise & 0x1FFF, (bitwise & 0x6000) >> 13

    def const_channel(payload: bytes) -> tuple[int, int]:
        (bitwise,) = struct.unpack_from("<H", payload)
        return bitwise & 0x1FFF, (bitwise & 0x6000) >> 13

    fallback_raw: list[bytes]
    motion_sync_details = None
    if (
        motion_sync is not None
        and isinstance(source_duration, (int, float))
        and float(source_duration) > 0.0
        and isinstance(destination_duration, (int, float))
        and float(destination_duration) > 0.0
        and isinstance(sample_contract, dict)
    ):
        source_channels: dict[
            tuple[int, int],
            list[tuple[float, tuple[float, ...]]],
        ] = {}
        for payload in source_raw:
            time, joint_index, component, values = _unpack_raw_transform_key(
                payload,
                duration=float(source_duration),
            )
            if (joint_index, component) in authored_channels:
                continue
            source_channels.setdefault((joint_index, component), []).append(
                (time, values)
            )
        source_times = motion_sync.get("source_times")
        if not isinstance(source_times, list) or not source_times:
            raise RidCompileError("Proxy pose motion sync has no source times")
        fallback_raw = []
        for (joint_index, component), rows in sorted(source_channels.items()):
            rows.sort(key=lambda row: row[0])
            for frame, source_time in source_times:
                fallback_raw.append(
                    _pack_raw_transform_key(
                        _sample_time(int(frame), sample_contract),
                        float(destination_duration),
                        joint_index,
                        component,
                        _interpolate_pose_values(
                            rows,
                            float(source_time),
                            rotation=component == 1,
                        ),
                    )
                )
        motion_sync_details = motion_sync.get("details")
    else:
        fallback_raw = [
            payload
            for payload in source_raw
            if raw_channel(payload) not in authored_channels
        ]
    fallback_const = [
        payload
        for payload in source_const
        if const_channel(payload) not in authored_channels
    ]
    authored_raw_size = int(encoded["num_anim_keys_raw"]) * 16
    authored_const_size = int(encoded["num_const_anim_keys"]) * 16
    authored_const_end = authored_raw_size + authored_const_size
    authored_raw = [
        encoded["bytes"][offset : offset + 16]
        for offset in range(0, authored_raw_size, 16)
    ]
    authored_const = [
        encoded["bytes"][offset : offset + 16]
        for offset in range(authored_raw_size, authored_const_end, 16)
    ]
    combined_raw = [*fallback_raw, *authored_raw]
    combined_raw.sort(key=_raw_transform_key_sort_key)
    combined_const = [*fallback_const, *authored_const]
    combined_const.sort(key=_const_transform_key_sort_key)
    authored_tail = encoded["bytes"][authored_const_end:]
    payload = b"".join([*combined_raw, *combined_const]) + authored_tail

    result = dict(encoded)
    result.update(
        {
            "bytes": payload,
            "bytes_base64": base64.b64encode(payload).decode("ascii"),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "num_anim_keys_raw": len(combined_raw),
            "num_const_anim_keys": len(combined_const),
            "is_scale_constant": bool(
                encoded["is_scale_constant"]
                and int(template_buffer.get("isScaleConstant", 1))
            ),
            "template_pose_fallback": {
                "raw_transform_keys": len(fallback_raw),
                "const_transform_keys": len(fallback_const),
                "motion_sync": motion_sync_details,
            },
        }
    )
    return result


def _replace_compressed_buffer(
    buffer_data: dict[str, Any],
    encoded: dict[str, Any],
    duration: float,
) -> None:
    buffer_data.update(
        {
            "animKeys": None,
            "animKeysRaw": None,
            "constAnimKeys": None,
            "constTrackKeys": None,
            "duration": duration,
            "extraDataNames": [],
            "fallbackFrameIndices": [],
            "hasRawRotations": 1 if encoded["has_raw_rotations"] else 0,
            "inplaceCompressedBuffer": None,
            "isScaleConstant": 1 if encoded["is_scale_constant"] else 0,
            "numAnimKeys": encoded["num_anim_keys"],
            "numAnimKeysRaw": encoded["num_anim_keys_raw"],
            "numConstAnimKeys": encoded["num_const_anim_keys"],
            "numConstTrackKeys": encoded["num_const_track_keys"],
            "numExtraJoints": encoded["num_extra_joints"],
            "numExtraTracks": encoded["num_extra_tracks"],
            "numFrames": encoded["num_frames"],
            "numJoints": encoded["num_joints"],
            "numTrackKeys": encoded["num_track_keys"],
            "numTracks": encoded["num_tracks"],
            "tempBuffer": None,
            "trackKeys": None,
        }
    )
    deferred = buffer_data.get("defferedBuffer")
    if not isinstance(deferred, dict):
        deferred = {"BufferId": "0", "Flags": 0}
        buffer_data["defferedBuffer"] = deferred
    deferred["Flags"] = 0
    deferred["Bytes"] = encoded["bytes_base64"]


def _actor_sample(
    samples: dict[str, Any],
    actor_id: str,
) -> dict[str, Any]:
    actors = samples.get("actors")
    if not isinstance(actors, list):
        raise RidCompileError("animation_samples.actors must be an array")
    matches = [
        actor for actor in actors
        if isinstance(actor, dict) and actor.get("id") == actor_id
    ]
    if len(matches) != 1:
        raise RidCompileError(
            f"animation_samples must contain exactly one actor {actor_id!r}"
        )
    return matches[0]


def _channel_track_samples(
    channel: dict[str, Any],
    sample_contract: dict[str, Any],
) -> dict[int, list[tuple[float, float]]]:
    result: dict[int, list[tuple[float, float]]] = {}
    tracks = channel.get("tracks", [])
    if not isinstance(tracks, list):
        raise RidCompileError("RID channel tracks must be an array")
    for track in tracks:
        if not isinstance(track, dict) or not isinstance(track.get("index"), int):
            raise RidCompileError("RID channel track entries need an integer index")
        rows = track.get("samples")
        if not isinstance(rows, list) or not rows:
            raise RidCompileError(
                f"RID channel track {track['index']} has no samples"
            )
        result[int(track["index"])] = [
            (
                _sample_time(int(row["frame"]), sample_contract),
                float(row["value"]),
            )
            for row in rows
        ]
    return result


def _compile_actor_aux_channel(
    *,
    source: dict[str, Any],
    channel_name: str,
    signature: str,
    animation_name: str,
    serial: int,
    duration: float,
    sample_contract: dict[str, Any],
    sampled_channel: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    compiled = copy.deepcopy(source)
    suffix = "head" if channel_name == "facial" else "cyb"
    _set_tag(compiled, f"{signature}_anim_{suffix}_0", serial)
    _set_animation_name(compiled, animation_name)
    _patch_durations(compiled, duration)
    buffer_data = _animation_buffer_from_actor({"animation": compiled["animation"]})
    template_joint_count = int(buffer_data["numJoints"])
    template_track_count = int(buffer_data.get("numTracks", 0))
    sampled_bone_count = sampled_channel.get("bone_count")
    if (
        sampled_bone_count is not None
        and int(sampled_bone_count) != template_joint_count
    ):
        raise RidCompileError(
            f"Actor {signature!r} {channel_name} armature has "
            f"{sampled_bone_count} bones, but the template requires "
            f"{template_joint_count}"
        )
    encoded = encode_compressed_animation(
        sampled_channel.get("joints", []),
        sample_contract=sample_contract,
        duration=duration,
        num_joints=template_joint_count,
        num_extra_joints=int(buffer_data.get("numExtraJoints", 0)),
        num_tracks=template_track_count,
        num_extra_tracks=int(buffer_data.get("numExtraTracks", 0)),
        track_samples=_channel_track_samples(sampled_channel, sample_contract),
    )
    _replace_compressed_buffer(buffer_data, encoded, duration)
    animation_data = compiled["animation"]["Data"]
    animation_data["motionExtraction"] = None
    compiled["motionExtracted"] = 0
    compiled["bonesCount"] = template_joint_count
    compiled["trajectoryBoneIndex"] = -1
    return compiled, {
        "channel": channel_name,
        "serial": serial,
        "armature": sampled_channel.get("armature"),
        "bone_count": sampled_bone_count,
        "template_joint_count": template_joint_count,
        "template_track_count": template_track_count,
        "buffer_sha256": encoded["sha256"],
        "buffer_bytes": len(encoded["bytes"]),
        "raw_transform_keys": encoded["num_anim_keys_raw"],
        "float_track_keys": encoded["num_track_keys"],
        "channels": encoded["emitted_channels"],
    }


def _camera_red_quaternion(
    blender_quaternion: Iterable[float],
) -> tuple[float, float, float, float]:
    # Blender cameras look down local -Z with +Y up. RED cameras look down
    # local +Y with +Z up, so append a -90-degree local X basis rotation.
    basis = (-math.sqrt(0.5), 0.0, 0.0, math.sqrt(0.5))
    quaternion = tuple(float(value) for value in blender_quaternion)
    return _multiply_quaternions(quaternion, basis)


def _camera_joints(samples: dict[str, Any]) -> list[dict[str, Any]]:
    camera = samples.get("camera")
    rows = camera.get("samples") if isinstance(camera, dict) else None
    if not isinstance(rows, list) or not rows:
        raise RidCompileError("animation_samples.camera.samples must not be empty")
    return [
        {
            "index": 0,
            "name": "Camera",
            "samples": [
                {
                    **row,
                    "rotation": list(_camera_red_quaternion(row["rotation"])),
                    "scale": [1.0, 1.0, 1.0],
                }
                for row in rows
            ],
        }
    ]


def _camera_tracks(
    samples: dict[str, Any],
) -> tuple[dict[int, list[tuple[float, float]]], dict[int, tuple[float, float]]]:
    rows = samples["camera"]["samples"]
    focal_values = [
        (_sample_time(int(row["frame"]), samples), float(row["focal_length"]))
        for row in rows
    ]
    const_tracks = {
        0: (0.0, 1.0),
        2: (0.0, 0.0),
        3: (0.0, 0.0),
        4: (0.0, 0.0),
        5: (0.0, 0.0),
        6: (0.0, 0.0),
    }
    if all(
        math.isclose(value, focal_values[0][1], abs_tol=1e-6)
        for _, value in focal_values
    ):
        const_tracks[1] = focal_values[0]
        return {}, const_tracks
    return {1: focal_values}, const_tracks


def _sampled_camera_trajectory(
    handoff: dict[str, Any],
    samples: dict[str, Any],
) -> list[dict[str, Any]]:
    origin = handoff.get("origin", {})
    origin_location = [
        float(item) for item in origin.get("location", [0.0, 0.0, 0.0])
    ]
    origin_quaternion = euler_degrees_to_quaternion(
        origin.get("rotation_degrees", [0.0, 0.0, 0.0])
    )
    camera_rows = samples["camera"]["samples"]
    sample_indices = sorted({0, len(camera_rows) // 2, len(camera_rows) - 1})
    trajectory: list[dict[str, Any]] = []
    for output_index, sample_index in enumerate(sample_indices):
        row = camera_rows[sample_index]
        rotated_location = _rotate_vector(origin_quaternion, row["translation"])
        world_location = tuple(
            origin_location[axis] + rotated_location[axis] for axis in range(3)
        )
        world_quaternion = _multiply_quaternions(
            origin_quaternion,
            _camera_red_quaternion(row["rotation"]),
        )
        trajectory.append(
            {
                "$type": "scnAnimationMotionSample",
                "time": _sample_time(int(row["frame"]), samples),
                "transform": _red_transform(
                    world_location,
                    world_quaternion,
                    final_w=1.0 if output_index == len(sample_indices) - 1 else 0.0,
                ),
            }
        )
    return trajectory


def _sampled_camera_lod_tracks(samples: dict[str, Any]) -> list[dict[str, Any]]:
    camera_rows = samples["camera"]["samples"]
    sample_indices = sorted({0, len(camera_rows) // 2, len(camera_rows) - 1})
    return [
        {
            "Elements": [
                1.0,
                float(camera_rows[index]["focal_length"]),
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
            ]
        }
        for index in sample_indices
    ]


def validate_handoff(handoff: dict[str, Any]) -> RidValidationReport:
    errors: list[str] = []
    warnings: list[str] = []
    if handoff.get("kind") != RID_KIND:
        errors.append(f"kind must be {RID_KIND}")
    if handoff.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    name = handoff.get("name")
    if not isinstance(name, str) or not name:
        errors.append("name must be a non-empty string")
    fps = handoff.get("fps")
    if not isinstance(fps, int) or isinstance(fps, bool) or fps <= 0:
        errors.append("fps must be a positive integer")
    frames = handoff.get("frames")
    if (
        not isinstance(frames, dict)
        or not isinstance(frames.get("start"), int)
        or not isinstance(frames.get("end"), int)
        or frames.get("end", 0) <= frames.get("start", 0)
    ):
        errors.append("frames must contain integer start < end")
    actors = handoff.get("actors")
    if not isinstance(actors, list) or not actors:
        errors.append("actors must be a non-empty array")
        actors = []
    signatures: set[str] = set()
    for index, actor in enumerate(actors):
        if not isinstance(actor, dict):
            errors.append(f"actors[{index}] must be an object")
            continue
        signature = actor.get("rid_signature", actor.get("id"))
        if not isinstance(signature, str) or not signature:
            errors.append(f"actors[{index}] needs id or rid_signature")
        elif signature in signatures:
            errors.append(f"Duplicate actor RID signature: {signature}")
        else:
            signatures.add(signature)
        keys = actor.get("transform_keys")
        if not isinstance(keys, list) or not keys:
            errors.append(f"actors[{index}].transform_keys must not be empty")
        elif not isinstance(keys[0], dict) or "location" not in keys[0]:
            errors.append(f"actors[{index}].transform_keys[0].location is required")
    camera = handoff.get("recording_camera")
    if not isinstance(camera, dict) or not isinstance(camera.get("keys"), list):
        errors.append("recording_camera.keys must be an array")
    elif len(camera["keys"]) < 2:
        errors.append("recording_camera.keys must contain at least two keys")
    samples = handoff.get("animation_samples")
    if not isinstance(samples, dict):
        errors.append(
            "animation_samples is required; rebuild or bake the Blender scene"
        )
    else:
        if samples.get("schema_version") != 1:
            errors.append("animation_samples.schema_version must be 1")
        if samples.get("coordinate_space") != ANIMATION_SAMPLE_SPACE:
            errors.append(
                f"animation_samples.coordinate_space must be {ANIMATION_SAMPLE_SPACE}"
            )
        if isinstance(frames, dict) and (
            samples.get("frame_start") != frames.get("start")
            or samples.get("frame_end") != frames.get("end")
        ):
            errors.append("animation_samples frame range must match handoff frames")
        if samples.get("sample_rate") != fps:
            errors.append("animation_samples.sample_rate must match handoff fps")
        sample_actors = samples.get("actors")
        if not isinstance(sample_actors, list) or len(sample_actors) != len(actors):
            errors.append("animation_samples.actors must match handoff actors")
        else:
            expected_samples = (
                frames["end"] - frames["start"] + 1
                if isinstance(frames, dict)
                and isinstance(frames.get("start"), int)
                and isinstance(frames.get("end"), int)
                else None
            )
            for actor in actors:
                if not isinstance(actor, dict):
                    continue
                try:
                    sampled_actor = _actor_sample(samples, str(actor["id"]))
                except RidCompileError as exc:
                    errors.append(str(exc))
                    continue
                joints = sampled_actor.get("joints")
                if not isinstance(joints, list) or not joints:
                    errors.append(
                        f"animation_samples actor {actor['id']!r} needs joints"
                    )
                    continue
                indices: set[int] = set()
                for joint in joints:
                    index = joint.get("index") if isinstance(joint, dict) else None
                    if not isinstance(index, int) or index < 0:
                        errors.append(
                            f"animation_samples actor {actor['id']!r} has invalid joint index"
                        )
                        continue
                    if index in indices:
                        errors.append(
                            f"animation_samples actor {actor['id']!r} duplicates joint {index}"
                        )
                    indices.add(index)
                    rows = joint.get("samples")
                    if (
                        not isinstance(rows, list)
                        or expected_samples is not None
                        and len(rows) != expected_samples
                    ):
                        errors.append(
                            f"animation_samples actor {actor['id']!r} joint "
                            f"{index} must cover every frame"
                        )
                rig = actor.get("rig")
                sampled_bone_count = sampled_actor.get("bone_count")
                sampled_bone_order = sampled_actor.get("bone_order")
                sampled_armature = sampled_actor.get("armature")
                trajectory_index = sampled_actor.get(
                    "trajectory_joint_index"
                )
                if isinstance(rig, dict):
                    expected_order = rig.get("bone_order")
                    expected_count = rig.get("bone_count")
                    if (
                        not isinstance(sampled_armature, str)
                        or not sampled_armature
                    ):
                        errors.append(
                            f"animation_samples actor {actor['id']!r} "
                            "needs a named armature"
                        )
                    if (
                        not isinstance(expected_order, list)
                        or not isinstance(expected_count, int)
                        or expected_count != len(expected_order)
                    ):
                        errors.append(
                            f"actor {actor['id']!r} has an invalid rig contract"
                        )
                    else:
                        if sampled_bone_count != expected_count:
                            errors.append(
                                f"animation_samples actor {actor['id']!r} "
                                f"bone_count must be {expected_count}"
                            )
                        if sampled_bone_order != expected_order:
                            errors.append(
                                f"animation_samples actor {actor['id']!r} "
                                "bone_order must match its rig contract"
                            )
                        expected_indices = set(range(expected_count))
                        if indices != expected_indices:
                            missing = sorted(expected_indices - indices)
                            extra = sorted(indices - expected_indices)
                            errors.append(
                                f"animation_samples actor {actor['id']!r} "
                                "must cover every rig joint; "
                                f"missing={missing}, extra={extra}"
                            )
                        for joint in joints:
                            if not isinstance(joint, dict):
                                continue
                            joint_index = joint.get("index")
                            if (
                                isinstance(joint_index, int)
                                and 0 <= joint_index < expected_count
                                and joint.get("name")
                                != expected_order[joint_index]
                            ):
                                errors.append(
                                    f"animation_samples actor "
                                    f"{actor['id']!r} joint {joint_index} "
                                    "name does not match its rig contract"
                                )
                    if sampled_actor.get("rig_contract_sha256") != rig.get(
                        "contract_sha256"
                    ):
                        errors.append(
                            f"animation_samples actor {actor['id']!r} "
                            "rig contract hash does not match the handoff"
                        )
                    if trajectory_index != rig.get(
                        "trajectory_joint_index"
                    ):
                        errors.append(
                            f"animation_samples actor {actor['id']!r} "
                            "trajectory joint does not match its rig contract"
                        )
                elif sampled_bone_count is not None:
                    errors.append(
                        f"animation_samples actor {actor['id']!r} has a "
                        "rigged bake without an actor rig contract"
                    )
                for channel_name in ("facial", "cyberware"):
                    requested = actor.get(channel_name)
                    sampled_channel = sampled_actor.get(channel_name)
                    if requested is None:
                        if sampled_channel is not None:
                            errors.append(
                                f"animation_samples actor {actor['id']!r} "
                                f"unexpectedly contains {channel_name}"
                            )
                        continue
                    if not isinstance(sampled_channel, dict):
                        errors.append(
                            f"animation_samples actor {actor['id']!r} needs "
                            f"{channel_name} samples"
                        )
                        continue
                    channel_joints = sampled_channel.get("joints", [])
                    channel_tracks = sampled_channel.get("tracks", [])
                    if not isinstance(channel_joints, list):
                        errors.append(
                            f"animation_samples actor {actor['id']!r} "
                            f"{channel_name}.joints must be an array"
                        )
                    else:
                        channel_joint_indices: set[int] = set()
                        for joint in channel_joints:
                            index = (
                                joint.get("index")
                                if isinstance(joint, dict)
                                else None
                            )
                            rows = (
                                joint.get("samples")
                                if isinstance(joint, dict)
                                else None
                            )
                            if not isinstance(index, int) or index < 0:
                                errors.append(
                                    f"animation_samples actor {actor['id']!r} "
                                    f"{channel_name} has an invalid joint index"
                                )
                            elif index in channel_joint_indices:
                                errors.append(
                                    f"animation_samples actor {actor['id']!r} "
                                    f"{channel_name} duplicates joint {index}"
                                )
                            else:
                                channel_joint_indices.add(index)
                            if (
                                not isinstance(rows, list)
                                or expected_samples is not None
                                and len(rows) != expected_samples
                            ):
                                errors.append(
                                    f"animation_samples actor {actor['id']!r} "
                                    f"{channel_name} joint {index} must cover "
                                    "every frame"
                                )
                    if not isinstance(channel_tracks, list):
                        errors.append(
                            f"animation_samples actor {actor['id']!r} "
                            f"{channel_name}.tracks must be an array"
                        )
                        continue
                    track_indices: set[int] = set()
                    for track in channel_tracks:
                        index = (
                            track.get("index")
                            if isinstance(track, dict)
                            else None
                        )
                        rows = (
                            track.get("samples")
                            if isinstance(track, dict)
                            else None
                        )
                        if not isinstance(index, int) or index < 0:
                            errors.append(
                                f"animation_samples actor {actor['id']!r} "
                                f"{channel_name} has an invalid track index"
                            )
                        elif index in track_indices:
                            errors.append(
                                f"animation_samples actor {actor['id']!r} "
                                f"{channel_name} duplicates track {index}"
                            )
                        else:
                            track_indices.add(index)
                        if (
                            not isinstance(rows, list)
                            or expected_samples is not None
                            and len(rows) != expected_samples
                        ):
                            errors.append(
                                f"animation_samples actor {actor['id']!r} "
                                f"{channel_name} track {index} must cover every frame"
                            )
        camera_samples = samples.get("camera")
        rows = camera_samples.get("samples") if isinstance(camera_samples, dict) else None
        expected_samples = (
            frames["end"] - frames["start"] + 1
            if isinstance(frames, dict)
            and isinstance(frames.get("start"), int)
            and isinstance(frames.get("end"), int)
            else None
        )
        if (
            not isinstance(rows, list)
            or expected_samples is not None
            and len(rows) != expected_samples
        ):
            errors.append("animation_samples.camera.samples must cover every frame")
    duration = None
    if not errors and isinstance(frames, dict) and isinstance(fps, int):
        duration = (frames["end"] - frames["start"]) / fps
    if any(actor.get("rig") is None for actor in actors if isinstance(actor, dict)):
        warnings.append(
            "Proxy actors encode authored root motion only; use an actor rig "
            "contract for skeletal acting"
        )
    return RidValidationReport(
        tuple(errors),
        tuple(warnings),
        {
            "name": name,
            "actor_count": len(actors),
            "duration_seconds": duration,
        },
    )


def _template_actor_slots(root: dict[str, Any]) -> list[dict[str, Any]]:
    actors = root.get("actors")
    if not isinstance(actors, list):
        raise RidCompileError("Template actors must be an array")
    return [
        actor
        for actor in actors
        if isinstance(actor, dict)
        and isinstance(actor.get("animations"), list)
        and actor["animations"]
    ]


def _select_actor_slots(
    root: dict[str, Any],
    count: int,
    signatures: list[str] | None,
) -> list[dict[str, Any]]:
    candidates = _template_actor_slots(root)
    if signatures:
        by_signature = {
            signature: actor
            for actor in candidates
            if (signature := _tag_signature(actor)) is not None
        }
        missing = [signature for signature in signatures if signature not in by_signature]
        if missing:
            raise RidCompileError(
                "Template actor signatures were not found: " + ", ".join(missing)
            )
        selected = [by_signature[signature] for signature in signatures]
    else:
        selected = candidates[:count]
    if len(selected) != count:
        raise RidCompileError(
            f"Template supplies {len(selected)} usable actor clips; {count} required"
        )
    return selected


def _freshen_handle_ids(
    value: Any,
    *,
    next_handle_id: int,
) -> int:
    """Give a copied template subtree globally unique CR2W handles."""

    definitions: list[str] = []
    _collect_handle_ids(value, definitions)
    unique_definitions = list(dict.fromkeys(definitions))
    mapping = {
        handle_id: str(next_handle_id + index)
        for index, handle_id in enumerate(unique_definitions)
    }

    def rewrite(item: Any) -> None:
        if isinstance(item, dict):
            handle_id = item.get("HandleId")
            if isinstance(handle_id, str) and handle_id in mapping:
                item["HandleId"] = mapping[handle_id]
            handle_ref_id = item.get("HandleRefId")
            if (
                isinstance(handle_ref_id, str)
                and handle_ref_id in mapping
            ):
                item["HandleRefId"] = mapping[handle_ref_id]
            for child in item.values():
                rewrite(child)
        elif isinstance(item, list):
            for child in item:
                rewrite(child)

    rewrite(value)
    return next_handle_id + len(unique_definitions)


def _collect_buffer_ids(value: Any, buffer_ids: list[str]) -> None:
    if isinstance(value, dict):
        buffer_id = value.get("BufferId")
        if isinstance(buffer_id, str):
            buffer_ids.append(buffer_id)
        for child in value.values():
            _collect_buffer_ids(child, buffer_ids)
    elif isinstance(value, list):
        for child in value:
            _collect_buffer_ids(child, buffer_ids)


def _freshen_buffer_ids(
    value: Any,
    *,
    next_buffer_id: int,
) -> int:
    """Give copied deferred buffers unique Red JSON reference IDs."""

    buffer_ids: list[str] = []
    _collect_buffer_ids(value, buffer_ids)
    mapping = {
        buffer_id: str(next_buffer_id + index)
        for index, buffer_id in enumerate(dict.fromkeys(buffer_ids))
    }

    def rewrite(item: Any) -> None:
        if isinstance(item, dict):
            buffer_id = item.get("BufferId")
            if isinstance(buffer_id, str) and buffer_id in mapping:
                item["BufferId"] = mapping[buffer_id]
            for child in item.values():
                rewrite(child)
        elif isinstance(item, list):
            for child in item:
                rewrite(child)

    rewrite(value)
    return next_buffer_id + len(mapping)


def compile_rid_document(
    handoff: dict[str, Any],
    template: dict[str, Any],
    *,
    actor_template_signatures: list[str] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    handoff_report = validate_handoff(handoff)
    if not handoff_report.ok:
        raise RidCompileError("; ".join(handoff_report.errors))
    result = copy.deepcopy(template)
    root = _root(result)
    actors = handoff["actors"]
    slots = _select_actor_slots(root, len(actors), actor_template_signatures)
    duration = (
        int(handoff["frames"]["end"]) - int(handoff["frames"]["start"])
    ) / float(handoff["fps"])
    origin = handoff.get("origin", {})
    animation_samples = handoff["animation_samples"]
    serial = 1
    compiled_actors: list[dict[str, Any]] = []
    encoded_actors: list[dict[str, Any]] = []
    template_handle_ids: list[str] = []
    _collect_handle_ids(root, template_handle_ids)
    next_handle_id = (
        max((int(handle_id) for handle_id in template_handle_ids), default=-1)
        + 1
    )
    template_buffer_ids: list[str] = []
    _collect_buffer_ids(root, template_buffer_ids)
    next_buffer_id = (
        max((int(buffer_id) for buffer_id in template_buffer_ids), default=-1)
        + 1
    )
    for actor, slot in zip(actors, slots, strict=True):
        compiled = copy.deepcopy(slot)
        next_handle_id = _freshen_handle_ids(
            compiled,
            next_handle_id=next_handle_id,
        )
        next_buffer_id = _freshen_buffer_ids(
            compiled,
            next_buffer_id=next_buffer_id,
        )
        source_signature = _tag_signature(slot)
        signature = str(actor.get("rid_signature", actor["id"]))
        _set_tag(compiled, signature, serial)
        serial += 1
        animations = compiled["animations"]
        if len(animations) != 1:
            raise RidCompileError(
                f"Template actor {source_signature!r} must have exactly one body animation"
            )
        body = animations[0]
        source_actor_buffer = _animation_buffer_from_actor(body)
        source_pose_duration = source_actor_buffer.get("duration")
        source_animation_handle = body.get("animation")
        source_animation_data = (
            source_animation_handle.get("Data")
            if isinstance(source_animation_handle, dict)
            else None
        )
        source_motion_extraction = copy.deepcopy(
            source_animation_data.get("motionExtraction")
            if isinstance(source_animation_data, dict)
            else None
        )
        _set_tag(body, f"{signature}_anim_body_0", serial)
        _set_animation_name(body, f"{handoff['name']}_anim_sn{serial}")
        body["offset"] = _world_actor_transform(actor["transform_keys"][0], origin)
        _patch_durations(body, duration)
        sampled_actor = _actor_sample(animation_samples, str(actor["id"]))
        actor_buffer = _animation_buffer_from_actor(body)
        layout_template_buffer_sha256 = inspect_compressed_buffer(
            actor_buffer
        )["sha256"]
        template_joint_count = int(actor_buffer["numJoints"])
        sampled_bone_count = sampled_actor.get("bone_count")
        if sampled_bone_count is not None and int(sampled_bone_count) != template_joint_count:
            raise RidCompileError(
                f"Actor {actor['id']!r} armature has {sampled_bone_count} bones, "
                f"but template actor {source_signature!r} requires "
                f"{template_joint_count}"
            )
        proxy_only = sampled_bone_count is None
        trajectory_joint_index = int(sampled_actor["trajectory_joint_index"])
        trajectory_joint = next(
            (
                joint
                for joint in sampled_actor["joints"]
                if int(joint["index"]) == trajectory_joint_index
            ),
            None,
        )
        if trajectory_joint is None:
            raise RidCompileError(
                f"Actor {actor['id']!r} has no trajectory joint "
                f"{trajectory_joint_index}"
            )
        reference_joint = next(
            (
                joint
                for joint in sampled_actor["joints"]
                if str(joint.get("name")) == "reference_joint"
            ),
            None,
        )
        if not proxy_only and reference_joint is None:
            raise RidCompileError(
                f"Actor {actor['id']!r} full-rig bake has no reference_joint"
            )
        if not proxy_only and reference_joint is not None:
            trajectory_samples = trajectory_joint["samples"]
            reference_samples = reference_joint["samples"]

            def samples_vary(samples: list[dict[str, Any]]) -> bool:
                first = samples[0]
                return any(
                    not _is_near_vector(
                        sample["translation"],
                        first["translation"],
                        tolerance=1e-5,
                    )
                    or not _is_near_vector(
                        sample["rotation"],
                        first["rotation"],
                        tolerance=1e-5,
                    )
                    for sample in samples[1:]
                )

            if (
                samples_vary(trajectory_samples)
                and not samples_vary(reference_samples)
            ):
                raise RidCompileError(
                    f"Actor {actor['id']!r} moving full-rig bake has a "
                    "constant reference_joint; rebake the actor root transform"
                )
        motion_extraction, motion_extraction_report = (
            _encode_spline_motion_extraction(
                trajectory_joint,
                sample_contract=animation_samples,
                duration=duration,
            )
        )
        actor_joints = copy.deepcopy(sampled_actor["joints"])
        # motionExtraction owns trajectory movement, but RED still expects the
        # body buffer to define identity translation/rotation channels for the
        # trajectory joint. Omitting it leaves the pose evaluator and attached
        # clue slots with an incomplete 71-joint transform set.
        body_trajectory_joint = next(
            joint
            for joint in actor_joints
            if int(joint["index"]) == trajectory_joint_index
        )
        for sample in body_trajectory_joint["samples"]:
            sample["translation"] = [0.0, 0.0, 0.0]
            sample["rotation"] = [0.0, 0.0, 0.0, 1.0]
            sample["scale"] = [1.0, 1.0, 1.0]
        actor_track_count = int(actor_buffer.get("numTracks", 0))
        encoded = encode_compressed_animation(
            actor_joints,
            sample_contract=animation_samples,
            duration=duration,
            num_joints=template_joint_count,
            num_extra_joints=int(actor_buffer.get("numExtraJoints", 0)),
            num_tracks=actor_track_count,
            num_extra_tracks=int(actor_buffer.get("numExtraTracks", 0)),
            const_tracks=(
                {
                    track_index: (0.0, 1.0)
                    for track_index in range(min(4, actor_track_count))
                }
                if not proxy_only
                else None
            ),
            force_channels=(
                {
                    (joint_index, channel)
                    for joint_index in range(template_joint_count)
                    for channel in ("translation", "rotation")
                }
                if not proxy_only
                else {
                    (trajectory_joint_index, "translation"),
                    (trajectory_joint_index, "rotation"),
                }
            ),
        )
        if proxy_only:
            component_by_name = {
                "translation": 0,
                "rotation": 1,
                "scale": 2,
            }
            motion_sync = _proxy_pose_motion_sync(
                source_motion_extraction=source_motion_extraction,
                trajectory_joint=trajectory_joint,
                sample_contract=animation_samples,
            )
            encoded = _merge_template_pose_channels(
                encoded,
                actor_buffer,
                authored_channels={
                    (
                        int(channel["joint_index"]),
                        component_by_name[str(channel["channel"])],
                    )
                    for channel in encoded["emitted_channels"]
                },
                source_duration=(
                    float(source_pose_duration)
                    if isinstance(source_pose_duration, (int, float))
                    else None
                ),
                destination_duration=duration,
                sample_contract=animation_samples,
                motion_sync=motion_sync,
            )
        elif encoded["sha256"] == layout_template_buffer_sha256:
            raise RidCompileError(
                f"Actor {actor['id']!r} rigged body buffer still matches "
                f"layout template actor {source_signature!r}"
            )
        _replace_compressed_buffer(actor_buffer, encoded, duration)
        animation_handle = body["animation"]
        animation_data = animation_handle["Data"]
        motion_extraction_handle = animation_data.get("motionExtraction")
        if (
            not isinstance(motion_extraction_handle, dict)
            or not isinstance(motion_extraction_handle.get("HandleId"), str)
            or not isinstance(motion_extraction_handle.get("Data"), dict)
        ):
            raise RidCompileError(
                f"Template actor {source_signature!r} requires a defined "
                "motionExtraction handle"
            )
        motion_extraction_handle["Data"] = motion_extraction
        additional_tracks = animation_data.get("additionalTracks")
        if isinstance(additional_tracks, dict):
            additional_tracks["entries"] = []
        additional_transforms = animation_data.get("additionalTransforms")
        if isinstance(additional_transforms, dict):
            additional_transforms["entries"] = []
        body["backendData"] = None
        body["events"] = None
        body["motionExtracted"] = 1
        body["bonesCount"] = template_joint_count
        body["trajectoryBoneIndex"] = trajectory_joint_index
        encoded_actors.append(
            {
                "actor": signature,
                "layout_template_actor": source_signature,
                "body_serial": serial,
                "armature": sampled_actor.get("armature"),
                "bone_count": sampled_bone_count,
                "trajectory_joint_index": sampled_actor["trajectory_joint_index"],
                "motion_extraction": motion_extraction_report,
                "buffer_sha256": encoded["sha256"],
                "layout_template_buffer_sha256": (
                    layout_template_buffer_sha256
                ),
                "buffer_bytes": len(encoded["bytes"]),
                "raw_transform_keys": encoded["num_anim_keys_raw"],
                "const_transform_keys": encoded["num_const_anim_keys"],
                "const_float_track_keys": encoded[
                    "num_const_track_keys"
                ],
                "template_pose_fallback": encoded.get(
                    "template_pose_fallback"
                ),
                "template_pose_fallback_used": proxy_only,
                "expected_pose_joint_count": (
                    None if proxy_only else template_joint_count
                ),
                "authored_pose_joint_count": (
                    None
                    if proxy_only
                    else len(
                        {
                            int(channel["joint_index"])
                            for channel in encoded["emitted_channels"]
                        }
                    )
                ),
                "channels": encoded["emitted_channels"],
                "facial": None,
                "cyberware": None,
            }
        )
        serial += 1
        for channel_name, field_name in (
            ("facial", "facialAnimations"),
            ("cyberware", "cyberwareAnimations"),
        ):
            requested_channel = actor.get(channel_name)
            sampled_channel = sampled_actor.get(channel_name)
            if requested_channel is None:
                compiled[field_name] = []
                continue
            source_channels = compiled.get(field_name)
            if not isinstance(source_channels, list) or not source_channels:
                raise RidCompileError(
                    f"Template actor {source_signature!r} has no "
                    f"{channel_name} animation layout"
                )
            if len(source_channels) != 1:
                raise RidCompileError(
                    f"Template actor {source_signature!r} must have exactly "
                    f"one {channel_name} animation"
                )
            if not isinstance(sampled_channel, dict):
                raise RidCompileError(
                    f"Actor {actor['id']!r} has no baked {channel_name} samples"
                )
            compiled_channel, channel_report = _compile_actor_aux_channel(
                source=source_channels[0],
                channel_name=channel_name,
                signature=signature,
                animation_name=f"{handoff['name']}_anim_sn{serial}",
                serial=serial,
                duration=duration,
                sample_contract=animation_samples,
                sampled_channel=sampled_channel,
            )
            compiled[field_name] = [compiled_channel]
            encoded_actors[-1][channel_name] = channel_report
            serial += 1
        compiled_actors.append(compiled)
    cameras = root.get("cameras")
    if not isinstance(cameras, list) or not cameras:
        raise RidCompileError("Template must contain a camera")
    camera = copy.deepcopy(cameras[0])
    camera_signature = str(handoff["recording_camera"].get("rid_signature", "Camera"))
    _set_tag(camera, camera_signature, serial)
    serial += 1
    camera_animations = camera.get("animations")
    if not isinstance(camera_animations, list) or len(camera_animations) != 1:
        raise RidCompileError("Template camera must have exactly one animation")
    camera_animation = camera_animations[0]
    _set_tag(camera_animation, f"{camera_signature}_anim_0", serial)
    _patch_durations(camera_animation, duration)
    camera_buffer = _animation_buffer_from_camera(camera_animation)
    camera_track_samples, camera_const_tracks = _camera_tracks(animation_samples)
    encoded_camera = encode_compressed_animation(
        _camera_joints(animation_samples),
        sample_contract=animation_samples,
        duration=duration,
        num_joints=1,
        num_extra_joints=0,
        num_tracks=7,
        num_extra_tracks=0,
        track_samples=camera_track_samples,
        const_tracks=camera_const_tracks,
    )
    _replace_compressed_buffer(camera_buffer, encoded_camera, duration)
    lod = camera_animation.get("cameraAnimationLOD")
    if not isinstance(lod, dict):
        raise RidCompileError("Template camera animation has no cameraAnimationLOD")
    trajectory = lod.get("trajectory")
    if not isinstance(trajectory, dict):
        trajectory = {}
        lod["trajectory"] = trajectory
    trajectory["Elements"] = _sampled_camera_trajectory(
        handoff,
        animation_samples,
    )
    tracks = lod.get("tracks")
    if not isinstance(tracks, dict):
        tracks = {}
        lod["tracks"] = tracks
    tracks["Elements"] = _sampled_camera_lod_tracks(animation_samples)
    serial += 1
    root["actors"] = compiled_actors
    root["cameras"] = [camera]
    _set_next_serial(root, serial)
    root["version"] = 5
    report = {
        "schema_version": 1,
        "kind": RID_REPORT_KIND,
        "name": handoff["name"],
        "duration_seconds": duration,
        "actor_count": len(compiled_actors),
        "camera_count": 1,
        "next_serial_number": serial,
        "animation_source": {
            "mode": "authored_blender_samples_encoded",
            "coordinate_space": animation_samples["coordinate_space"],
            "sample_rate": animation_samples["sample_rate"],
            "sample_count": (
                int(animation_samples["frame_end"])
                - int(animation_samples["frame_start"])
                + 1
            ),
            "actors": encoded_actors,
            "camera": {
                "layout_template": _tag_signature(cameras[0]),
                "buffer_sha256": encoded_camera["sha256"],
                "buffer_bytes": len(encoded_camera["bytes"]),
                "raw_transform_keys": encoded_camera["num_anim_keys_raw"],
                "float_track_keys": encoded_camera["num_track_keys"],
                "const_float_track_keys": encoded_camera[
                    "num_const_track_keys"
                ],
                "channels": encoded_camera["emitted_channels"],
            },
            "custom_skeletal_animation": any(
                actor.get("bone_count") is not None
                for actor in encoded_actors
            ),
            "custom_facial_animation": any(
                actor.get("facial") is not None for actor in encoded_actors
            ),
            "custom_cyberware_animation": any(
                actor.get("cyberware") is not None for actor in encoded_actors
            ),
            "custom_camera_buffer": True,
        },
        "authored": {
            "actor_tags": True,
            "actor_offsets": True,
            "camera_tag": True,
            "camera_lod_trajectory": True,
            "duration": True,
            "actor_animation_buffers": True,
            "facial_animation_buffers": any(
                actor.get("facial") is not None for actor in encoded_actors
            ),
            "cyberware_animation_buffers": any(
                actor.get("cyberware") is not None for actor in encoded_actors
            ),
            "camera_animation_buffer": True,
        },
        "warnings": list(handoff_report.warnings),
    }
    return result, report


def _collect_handle_ids(value: Any, definitions: list[str]) -> None:
    if isinstance(value, dict):
        handle_id = value.get("HandleId")
        if isinstance(handle_id, str) and isinstance(value.get("Data"), dict):
            definitions.append(handle_id)
        for child in value.values():
            _collect_handle_ids(child, definitions)
    elif isinstance(value, list):
        for child in value:
            _collect_handle_ids(child, definitions)


def inspect_compressed_buffer(buffer_data: dict[str, Any]) -> dict[str, Any]:
    deferred = buffer_data.get("defferedBuffer")
    encoded = deferred.get("Bytes") if isinstance(deferred, dict) else None
    if not isinstance(encoded, str):
        raise RidCompileError("Compressed animation buffer has no deferred bytes")
    try:
        payload = base64.b64decode(encoded, validate=True)
    except ValueError as exc:
        raise RidCompileError("Compressed animation buffer has invalid base64") from exc
    counts = {
        "anim": int(buffer_data.get("numAnimKeys", 0)),
        "raw": int(buffer_data.get("numAnimKeysRaw", 0)),
        "const": int(buffer_data.get("numConstAnimKeys", 0)),
        "track": int(buffer_data.get("numTrackKeys", 0)),
        "const_track": int(buffer_data.get("numConstTrackKeys", 0)),
    }
    expected_size = (
        counts["anim"] * 10
        + counts["raw"] * 16
        + counts["const"] * 16
        + counts["track"] * 8
        + counts["const_track"] * 8
    )
    if len(payload) != expected_size:
        raise RidCompileError(
            f"Compressed animation buffer has {len(payload)} bytes; "
            f"key counts require {expected_size}"
        )
    offset = counts["anim"] * 10
    duration = float(buffer_data["duration"])
    channel_counts: dict[str, int] = {
        "translation": 0,
        "rotation": 0,
        "scale": 0,
    }
    joint_indices: set[int] = set()
    first_keys: dict[str, dict[str, Any]] = {}
    last_keys: dict[str, dict[str, Any]] = {}
    rows_by_channel: dict[tuple[int, str], list[dict[str, Any]]] = {}
    last_time_by_joint: dict[int, int] = {}
    raw_key_order_errors: list[dict[str, int]] = []
    component_names = {0: "translation", 1: "rotation", 2: "scale"}
    for _ in range(counts["raw"]):
        normalized_time, bitwise, x, y, z = struct.unpack_from(
            "<HHfff", payload, offset
        )
        offset += 16
        component = (bitwise & 0x6000) >> 13
        joint_index = bitwise & 0x1FFF
        name = component_names.get(component)
        if name is None:
            raise RidCompileError(
                f"Compressed animation key uses unknown component {component}"
            )
        previous_time = last_time_by_joint.get(joint_index)
        if previous_time is not None and normalized_time < previous_time:
            raw_key_order_errors.append(
                {
                    "joint_index": joint_index,
                    "previous_time": previous_time,
                    "time": normalized_time,
                }
            )
        last_time_by_joint[joint_index] = normalized_time
        values: list[float]
        if component == 1:
            dot = x * x + y * y + z * z
            multiplier = math.sqrt(max(0.0, 2.0 - dot))
            w = 1.0 - dot
            if bitwise & 0x8000:
                w = -w
            values = [x * multiplier, y * multiplier, z * multiplier, w]
        else:
            values = [x, y, z]
        row = {
            "joint_index": joint_index,
            "time": normalized_time / 65535.0 * duration,
            "value": values,
        }
        channel_counts[name] += 1
        joint_indices.add(joint_index)
        first_keys.setdefault(name, row)
        last_keys[name] = row
        rows_by_channel.setdefault((joint_index, name), []).append(row)
    const_joint_indices: set[int] = set()
    const_channel_counts: dict[str, int] = {
        "translation": 0,
        "rotation": 0,
        "scale": 0,
    }
    for _ in range(counts["const"]):
        (bitwise,) = struct.unpack_from("<H", payload, offset)
        offset += 16
        component = (bitwise & 0x6000) >> 13
        joint_index = bitwise & 0x1FFF
        name = component_names.get(component)
        if name is None:
            raise RidCompileError(
                f"Compressed constant key uses unknown component {component}"
            )
        const_joint_indices.add(joint_index)
        const_channel_counts[name] += 1
    track_indices: set[int] = set()
    track_rows: dict[int, list[dict[str, float]]] = {}
    for _ in range(counts["track"]):
        normalized_time, track_index, value = struct.unpack_from(
            "<HHf", payload, offset
        )
        offset += 8
        track_indices.add(track_index)
        track_rows.setdefault(track_index, []).append(
            {
                "time": normalized_time / 65535.0 * duration,
                "value": value,
            }
        )
    for _ in range(counts["const_track"]):
        track_index, _padding, value = struct.unpack_from(
            "<HHf", payload, offset
        )
        offset += 8
        track_indices.add(track_index)
        track_rows.setdefault(track_index, []).append(
            {
                "time": 0.0,
                "value": value,
            }
        )
    return {
        "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "counts": counts,
        "is_scale_constant": bool(
            int(buffer_data.get("isScaleConstant", 1))
        ),
        "channel_counts": channel_counts,
        "joint_indices": sorted(joint_indices),
        "const_channel_counts": const_channel_counts,
        "const_joint_indices": sorted(const_joint_indices),
        "pose_joint_indices": sorted(joint_indices | const_joint_indices),
        "raw_key_order_ok": not raw_key_order_errors,
        "raw_key_order_errors": raw_key_order_errors,
        "track_indices": sorted(track_indices),
        "first_keys": first_keys,
        "last_keys": last_keys,
        "channel_checkpoints": [
            {
                "joint_index": joint_index,
                "channel": channel,
                "first": rows[0],
                "middle": rows[len(rows) // 2],
                "last": rows[-1],
            }
            for (joint_index, channel), rows in sorted(rows_by_channel.items())
        ],
        "track_checkpoints": [
            {
                "track_index": track_index,
                "first": rows[0],
                "middle": rows[len(rows) // 2],
                "last": rows[-1],
            }
            for track_index, rows in sorted(track_rows.items())
        ],
    }


def inspect_motion_extraction(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RidCompileError("Actor animation has no motionExtraction handle")
    handle_id = value.get("HandleId")
    data = value.get("Data")
    if not isinstance(handle_id, str) or not isinstance(data, dict):
        raise RidCompileError("Actor motionExtraction handle is not defined")
    if data.get("$type") != "animSplineCompressedMotionExtraction":
        raise RidCompileError(
            "Actor motionExtraction must use "
            "animSplineCompressedMotionExtraction"
        )
    duration = data.get("duration")
    if not isinstance(duration, (int, float)) or float(duration) <= 0.0:
        raise RidCompileError("Actor motionExtraction has an invalid duration")
    component_names = {0: "translation", 1: "rotation", 2: "scale"}
    result: dict[str, Any] = {
        "handle_id": handle_id,
        "type": data["$type"],
        "duration": float(duration),
    }
    for field, expected_component in (
        ("posKeysData", 0),
        ("rotKeysData", 1),
    ):
        values = data.get(field)
        if (
            not isinstance(values, list)
            or not values
            or any(
                not isinstance(value, int) or not 0 <= value <= 255
                for value in values
            )
        ):
            raise RidCompileError(
                f"Actor motionExtraction {field} is not a byte array"
            )
        payload = bytes(values)
        if len(payload) % 16:
            raise RidCompileError(
                f"Actor motionExtraction {field} is not 16-byte aligned"
            )
        rows: list[dict[str, Any]] = []
        previous_time = -1
        for offset in range(0, len(payload), 16):
            normalized_time, bitwise, x, y, z = struct.unpack_from(
                "<HHfff",
                payload,
                offset,
            )
            component = (bitwise & 0x6000) >> 13
            joint_index = bitwise & 0x1FFF
            if component != expected_component:
                raise RidCompileError(
                    f"Actor motionExtraction {field} contains "
                    f"{component_names.get(component, component)!r} keys"
                )
            if joint_index != 0:
                raise RidCompileError(
                    f"Actor motionExtraction {field} uses joint "
                    f"{joint_index}; expected logical root joint 0"
                )
            if normalized_time < previous_time:
                raise RidCompileError(
                    f"Actor motionExtraction {field} key times decrease"
                )
            previous_time = normalized_time
            rows.append(
                {
                    "time_ratio": normalized_time,
                    "time": normalized_time / 65535.0 * float(duration),
                    "value": [x, y, z],
                }
            )
        if rows[0]["time_ratio"] != 0 or rows[-1]["time_ratio"] != 65535:
            raise RidCompileError(
                f"Actor motionExtraction {field} must span the full duration"
            )
        result[field] = {
            "bytes": len(payload),
            "key_count": len(rows),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "first": rows[0],
            "middle": rows[len(rows) // 2],
            "last": rows[-1],
        }
    return result


def validate_compiled_document(
    document: dict[str, Any],
    *,
    expected_name: str | None = None,
    expected_duration: float | None = None,
    expected_actor_signatures: list[str] | None = None,
) -> RidValidationReport:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        root = _root(document)
    except RidCompileError as exc:
        return RidValidationReport((str(exc),), (), {})
    actors = root.get("actors")
    cameras = root.get("cameras")
    if not isinstance(actors, list) or not actors:
        errors.append("Compiled RID must contain actors")
        actors = []
    if not isinstance(cameras, list) or len(cameras) != 1:
        errors.append("Compiled RID must contain exactly one camera")
        cameras = []
    actor_signatures = [
        signature
        for actor in actors
        if isinstance(actor, dict)
        if (signature := _tag_signature(actor)) is not None
    ]
    if expected_actor_signatures is not None and actor_signatures != expected_actor_signatures:
        errors.append(
            f"Actor signatures {actor_signatures!r} do not match "
            f"{expected_actor_signatures!r}"
        )
    serials: list[int] = []
    durations: list[float] = []
    actor_buffer_details: list[dict[str, Any]] = []
    actor_motion_details: list[dict[str, Any]] = []
    auxiliary_buffer_details: list[dict[str, Any]] = []
    for actor in actors:
        if not isinstance(actor, dict):
            continue
        tag = actor.get("tag")
        if isinstance(tag, dict) and (value := _serial(tag.get("serialNumber"))) is not None:
            serials.append(value)
        animations = actor.get("animations", [])
        if not isinstance(animations, list) or len(animations) != 1:
            errors.append(f"Actor {_tag_signature(actor)!r} needs one body animation")
            continue
        body = animations[0]
        tag = body.get("tag")
        if isinstance(tag, dict) and (value := _serial(tag.get("serialNumber"))) is not None:
            serials.append(value)
        animation = body.get("animation", {})
        data = animation.get("Data", {}) if isinstance(animation, dict) else {}
        if isinstance(data, dict):
            name = _cname(data.get("name"))
            if expected_name is not None and not str(name).startswith(f"{expected_name}_anim_sn"):
                errors.append(f"Unexpected actor animation name: {name!r}")
            duration = data.get("duration")
            if isinstance(duration, (int, float)):
                durations.append(float(duration))
            anim_buffer = data.get("animBuffer")
            buffer_data = (
                anim_buffer.get("Data", {}) if isinstance(anim_buffer, dict) else {}
            )
            if isinstance(buffer_data, dict):
                try:
                    details = inspect_compressed_buffer(buffer_data)
                    details["actor"] = _tag_signature(actor)
                    actor_buffer_details.append(details)
                    if details["counts"]["raw"] == 0:
                        errors.append(
                            f"Actor {_tag_signature(actor)!r} has no authored transform keys"
                        )
                    if not details["raw_key_order_ok"]:
                        errors.append(
                            f"Actor {_tag_signature(actor)!r} raw transform "
                            "key time decreases within a joint"
                        )
                    if (
                        int(buffer_data.get("numJoints", 0)) > 1
                        and not details["pose_joint_indices"]
                    ):
                        errors.append(
                            f"Actor {_tag_signature(actor)!r} has no "
                            "rig-compatible pose fallback"
                        )
                    trajectory_joint_index = body.get(
                        "trajectoryBoneIndex"
                    )
                    if (
                        not isinstance(trajectory_joint_index, int)
                        or trajectory_joint_index < 0
                    ):
                        errors.append(
                            f"Actor {_tag_signature(actor)!r} has an invalid "
                            "trajectory bone index"
                        )
                    elif trajectory_joint_index in details["joint_indices"]:
                        errors.append(
                            f"Actor {_tag_signature(actor)!r} duplicates "
                            "dynamic trajectory motion in its pose buffer"
                        )
                except RidCompileError as exc:
                    errors.append(str(exc))
            if body.get("motionExtracted") != 1:
                errors.append(
                    f"Actor {_tag_signature(actor)!r} must expose extracted root motion"
                )
            try:
                motion_details = inspect_motion_extraction(
                    data.get("motionExtraction")
                )
                motion_details["actor"] = _tag_signature(actor)
                actor_motion_details.append(motion_details)
                if isinstance(duration, (int, float)) and not math.isclose(
                    motion_details["duration"],
                    float(duration),
                    abs_tol=1e-5,
                ):
                    errors.append(
                        f"Actor {_tag_signature(actor)!r} motion extraction "
                        "duration does not match its animation"
                    )
            except RidCompileError as exc:
                errors.append(str(exc))
            if body.get("events") is not None:
                events = body.get("events", {}).get("Data", {}).get(
                    "events",
                    [],
                )
                num_frames = int(buffer_data.get("numFrames", 0))
                invalid_frames = [
                    event.get("Data", {}).get("startFrame")
                    for event in events
                    if isinstance(event, dict)
                    and isinstance(
                        event.get("Data", {}).get("startFrame"),
                        int,
                    )
                    and event["Data"]["startFrame"] >= num_frames
                ]
                if invalid_frames:
                    errors.append(
                        f"Actor {_tag_signature(actor)!r} retains animation "
                        f"events outside {num_frames} frames"
                    )
            if body.get("backendData") is not None:
                errors.append(
                    f"Actor {_tag_signature(actor)!r} retains donor backend timeline data"
                )
        for channel_name, field_name in (
            ("facial", "facialAnimations"),
            ("cyberware", "cyberwareAnimations"),
        ):
            channel_animations = actor.get(field_name, [])
            if not isinstance(channel_animations, list):
                errors.append(
                    f"Actor {_tag_signature(actor)!r} {field_name} must be an array"
                )
                continue
            for channel_animation in channel_animations:
                if not isinstance(channel_animation, dict):
                    continue
                tag = channel_animation.get("tag")
                if isinstance(tag, dict) and (
                    value := _serial(tag.get("serialNumber"))
                ) is not None:
                    serials.append(value)
                animation = channel_animation.get("animation")
                animation_data = (
                    animation.get("Data", {})
                    if isinstance(animation, dict)
                    else {}
                )
                anim_buffer = (
                    animation_data.get("animBuffer")
                    if isinstance(animation_data, dict)
                    else None
                )
                buffer_data = (
                    anim_buffer.get("Data", {})
                    if isinstance(anim_buffer, dict)
                    else {}
                )
                if isinstance(animation_data, dict) and isinstance(
                    animation_data.get("duration"), (int, float)
                ):
                    durations.append(float(animation_data["duration"]))
                if isinstance(buffer_data, dict):
                    try:
                        details = inspect_compressed_buffer(buffer_data)
                        details["actor"] = _tag_signature(actor)
                        details["channel"] = channel_name
                        auxiliary_buffer_details.append(details)
                    except RidCompileError as exc:
                        errors.append(str(exc))
    camera_trajectory_count = 0
    camera_buffer_details: dict[str, Any] | None = None
    for camera in cameras:
        if not isinstance(camera, dict):
            continue
        tag = camera.get("tag")
        if isinstance(tag, dict) and (value := _serial(tag.get("serialNumber"))) is not None:
            serials.append(value)
        animations = camera.get("animations", [])
        if not isinstance(animations, list) or len(animations) != 1:
            errors.append("Camera needs one animation")
            continue
        animation = animations[0]
        tag = animation.get("tag")
        if isinstance(tag, dict) and (value := _serial(tag.get("serialNumber"))) is not None:
            serials.append(value)
        buffer_handle = animation.get("animation")
        buffer_data = (
            buffer_handle.get("Data", {}) if isinstance(buffer_handle, dict) else {}
        )
        if isinstance(buffer_data, dict):
            duration = buffer_data.get("duration")
            if isinstance(duration, (int, float)):
                durations.append(float(duration))
            try:
                camera_buffer_details = inspect_compressed_buffer(buffer_data)
                if camera_buffer_details["counts"]["raw"] == 0:
                    errors.append("Camera buffer has no authored transform keys")
                if not camera_buffer_details["raw_key_order_ok"]:
                    errors.append(
                        "Camera raw transform key time decreases within its joint"
                    )
                if camera_buffer_details["track_indices"] != list(range(7)):
                    errors.append("Camera buffer does not define all seven tracks")
            except RidCompileError as exc:
                errors.append(str(exc))
        lod = animation.get("cameraAnimationLOD", {})
        trajectory = lod.get("trajectory", {}) if isinstance(lod, dict) else {}
        elements = trajectory.get("Elements", []) if isinstance(trajectory, dict) else []
        camera_trajectory_count = len(elements) if isinstance(elements, list) else 0
        if camera_trajectory_count < 2:
            errors.append("Camera LOD trajectory needs at least two samples")
        lod_tracks = lod.get("tracks", {}) if isinstance(lod, dict) else {}
        lod_track_rows = (
            lod_tracks.get("Elements", [])
            if isinstance(lod_tracks, dict)
            else []
        )
        if (
            camera_buffer_details is not None
            and camera_trajectory_count >= 2
        ):
            focal_checkpoint = next(
                (
                    checkpoint
                    for checkpoint in camera_buffer_details[
                        "track_checkpoints"
                    ]
                    if checkpoint["track_index"] == 1
                ),
                None,
            )
            expected_focal = (
                [
                    focal_checkpoint["first"]["value"],
                    focal_checkpoint["middle"]["value"],
                    focal_checkpoint["last"]["value"],
                ]
                if focal_checkpoint is not None
                else []
            )
            actual_focal = [
                row.get("Elements", [None, None])[1]
                for row in lod_track_rows
                if isinstance(row, dict)
                and len(row.get("Elements", [])) == 7
            ]
            if (
                len(lod_track_rows) != camera_trajectory_count
                or len(actual_focal) != len(expected_focal)
                or any(
                    not math.isclose(
                        float(actual),
                        float(expected),
                        abs_tol=1e-4,
                    )
                    for actual, expected in zip(
                        actual_focal,
                        expected_focal,
                        strict=True,
                    )
                )
            ):
                errors.append(
                    "Camera LOD tracks do not match authored focal checkpoints"
                )
    if len(serials) != len(set(serials)):
        errors.append("RID tags contain duplicate serial numbers")
    next_serial = _serial(root.get("nextSerialNumber"))
    if serials and (next_serial is None or next_serial <= max(serials)):
        errors.append("nextSerialNumber must be greater than every RID tag serial")
    if expected_duration is not None:
        for duration in durations:
            if not math.isclose(duration, expected_duration, abs_tol=1e-5):
                errors.append(
                    f"Animation duration {duration} does not match {expected_duration}"
                )
    handle_ids: list[str] = []
    _collect_handle_ids(root, handle_ids)
    duplicate_handles = sorted(
        handle_id for handle_id in set(handle_ids) if handle_ids.count(handle_id) > 1
    )
    if duplicate_handles:
        errors.append("Duplicate handle definitions: " + ", ".join(duplicate_handles))
    return RidValidationReport(
        tuple(errors),
        tuple(warnings),
        {
            "actor_count": len(actors),
            "camera_count": len(cameras),
            "actor_signatures": actor_signatures,
            "serial_numbers": serials,
            "next_serial_number": next_serial,
            "animation_durations": durations,
            "camera_trajectory_samples": camera_trajectory_count,
            "handle_definition_count": len(handle_ids),
            "actor_animation_buffers": actor_buffer_details,
            "actor_motion_extractions": actor_motion_details,
            "auxiliary_animation_buffers": auxiliary_buffer_details,
            "camera_animation_buffer": camera_buffer_details,
        },
    )


def find_wolvenkit(explicit: Path | None = None) -> Path:
    candidates = [explicit] if explicit is not None else []
    candidates.extend([WOLVENKIT_CLI, Path("WolvenKit.CLI.exe")])
    discovered = shutil.which("WolvenKit.CLI")
    if discovered:
        candidates.append(Path(discovered))
    for candidate in candidates:
        if candidate is not None and candidate.is_file():
            return candidate.resolve()
    raise RidCompileError(
        "Built WolvenKit.CLI.exe was not found; pass --wolvenkit or build "
        "WolvenKit.CLI in Release/net8.0"
    )


def _run(command: list[str]) -> str:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    failed_output = (
        "[ 0: Error" in completed.stdout
        or "Could not convert" in completed.stdout
        or "Invalid output directory" in completed.stdout
    )
    if completed.returncode != 0 or failed_output:
        raise RidCompileError(
            f"Command failed ({completed.returncode}): {' '.join(command)}\n"
            f"{completed.stdout.strip()}"
        )
    return completed.stdout


def serialize_template(
    template_path: Path,
    output_directory: Path,
    wolvenkit: Path,
) -> Path:
    if template_path.name.casefold().endswith(".scenerid.json"):
        return template_path
    if template_path.suffix.casefold() != ".scenerid":
        raise RidCompileError("Template must be .scenerid or .scenerid.json")
    output_directory.mkdir(parents=True, exist_ok=True)
    _run(
        [
            str(wolvenkit),
            "cr2w",
            "--serialize",
            "--outpath",
            str(output_directory),
            str(template_path.resolve()),
            "--verbosity",
            "Minimal",
        ]
    )
    output = output_directory / f"{template_path.name}.json"
    if not output.is_file():
        raise RidCompileError(f"WolvenKit did not produce template JSON: {output}")
    return output


def deserialize_rid(
    json_path: Path,
    output_path: Path,
    wolvenkit: Path,
    staging_directory: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    staging_directory.mkdir(parents=True, exist_ok=True)
    expected_name = json_path.name.removesuffix(".json")
    if expected_name != output_path.name:
        raise RidCompileError(
            f"Compiler JSON must be named {output_path.name}.json, got {json_path.name}"
        )
    _run(
        [
            str(wolvenkit),
            "cr2w",
            "--deserialize",
            "--outpath",
            str(staging_directory),
            str(json_path.resolve()),
            "--verbosity",
            "Minimal",
        ]
    )
    staged_output = staging_directory / output_path.name
    if not staged_output.is_file():
        raise RidCompileError(f"WolvenKit did not produce RID: {staged_output}")
    with staged_output.open("rb") as stream:
        if stream.read(4) != CR2W_MAGIC:
            raise RidCompileError(
                f"Generated RID has invalid CR2W magic: {staged_output}"
            )
    shutil.copyfile(staged_output, output_path)


def verify_binary(
    output_path: Path,
    wolvenkit: Path,
    *,
    expected_name: str,
    expected_duration: float,
    expected_actor_signatures: list[str],
    directory: Path,
) -> RidValidationReport:
    directory.mkdir(parents=True, exist_ok=True)
    _run(
        [
            str(wolvenkit),
            "cr2w",
            "--serialize",
            "--outpath",
            str(directory),
            str(output_path.resolve()),
            "--verbosity",
            "Minimal",
        ]
    )
    json_path = directory / f"{output_path.name}.json"
    if not json_path.is_file():
        raise RidCompileError(f"WolvenKit did not verify RID as JSON: {json_path}")
    report = validate_compiled_document(
        load_json(json_path),
        expected_name=expected_name,
        expected_duration=expected_duration,
        expected_actor_signatures=expected_actor_signatures,
    )
    if not report.ok:
        raise RidCompileError("Generated RID verification failed: " + "; ".join(report.errors))
    return report


def _validation_buffer_hashes(report: RidValidationReport) -> dict[str, Any]:
    return {
        "actors": [
            {
                "actor": details["actor"],
                "sha256": details["sha256"],
            }
            for details in report.details.get("actor_animation_buffers", [])
        ],
        "auxiliary": [
            {
                "actor": details["actor"],
                "channel": details["channel"],
                "sha256": details["sha256"],
            }
            for details in report.details.get(
                "auxiliary_animation_buffers", []
            )
        ],
        "camera": (
            report.details["camera_animation_buffer"]["sha256"]
            if report.details.get("camera_animation_buffer")
            else None
        ),
    }


def compile_binary(
    handoff_path: Path,
    template_path: Path,
    output_path: Path,
    *,
    wolvenkit_path: Path | None = None,
    actor_template_signatures: list[str] | None = None,
    json_output_path: Path | None = None,
    report_path: Path | None = None,
    verify: bool = True,
) -> dict[str, Any]:
    handoff = load_json(handoff_path)
    wolvenkit = find_wolvenkit(wolvenkit_path)
    output_path = output_path.resolve()
    json_output_path = (
        json_output_path.resolve()
        if json_output_path is not None
        else Path(f"{output_path}.json")
    )
    report_path = (
        report_path.resolve()
        if report_path is not None
        else output_path.with_name(f"{output_path.stem}.rid-report.json")
    )
    if json_output_path.name != f"{output_path.name}.json":
        raise RidCompileError(
            f"--json-output must end with {output_path.name}.json so WolvenKit "
            "emits the requested binary name"
        )
    with tempfile.TemporaryDirectory(prefix="ghostline-rid-") as temp:
        temp_root = Path(temp)
        template_json_path = serialize_template(
            template_path.resolve(),
            temp_root / "template",
            wolvenkit,
        )
        template = load_json(template_json_path)
        compiled, build_report = compile_rid_document(
            handoff,
            template,
            actor_template_signatures=actor_template_signatures,
        )
        expected_duration = (
            handoff["frames"]["end"] - handoff["frames"]["start"]
        ) / handoff["fps"]
        actor_signatures = [
            str(actor.get("rid_signature", actor["id"])) for actor in handoff["actors"]
        ]
        validation = validate_compiled_document(
            compiled,
            expected_name=handoff["name"],
            expected_duration=expected_duration,
            expected_actor_signatures=actor_signatures,
        )
        if not validation.ok:
            raise RidCompileError("Compiled JSON is invalid: " + "; ".join(validation.errors))
        write_json(json_output_path, compiled)
        deserialize_rid(
            json_output_path,
            output_path,
            wolvenkit,
            temp_root / "binary",
        )
        verified = None
        if verify:
            verified = verify_binary(
                output_path,
                wolvenkit,
                expected_name=handoff["name"],
                expected_duration=expected_duration,
                expected_actor_signatures=actor_signatures,
                directory=temp_root / "verified",
            )
            compiled_hashes = _validation_buffer_hashes(validation)
            verified_hashes = _validation_buffer_hashes(verified)
            if verified_hashes != compiled_hashes:
                raise RidCompileError(
                    "Generated RID round trip changed authored animation buffers"
                )
    build_report.update(
        {
            "handoff": str(handoff_path.resolve()),
            "handoff_sha256": file_sha256(handoff_path),
            "template": str(template_path.resolve()),
            "template_sha256": file_sha256(template_path),
            "wolvenkit": str(wolvenkit),
            "json_output": str(json_output_path),
            "binary_output": str(output_path),
            "binary_size": output_path.stat().st_size,
            "binary_sha256": file_sha256(output_path),
            "cr2w_magic": True,
            "validation": {
                "compiled_json": validation.details,
                "round_trip": verified.details if verified is not None else None,
                "animation_buffer_hashes": _validation_buffer_hashes(validation),
            },
        }
    )
    write_json(report_path, build_report)
    return build_report


def _print_validation(report: RidValidationReport) -> None:
    print(
        json.dumps(
            {
                "ok": report.ok,
                "errors": list(report.errors),
                "warnings": list(report.warnings),
                "details": report.details,
            },
            indent=2,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate", help="Validate a handoff or compiled RID JSON")
    validate.add_argument("path", type=Path)
    compile_command = commands.add_parser(
        "compile",
        help="Compile a handoff with a vanilla .scenerid template",
    )
    compile_command.add_argument("--handoff", type=Path, default=DEFAULT_HANDOFF)
    compile_command.add_argument("--template", type=Path, required=True)
    compile_command.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    compile_command.add_argument("--json-output", type=Path)
    compile_command.add_argument("--report", type=Path)
    compile_command.add_argument("--wolvenkit", type=Path)
    compile_command.add_argument(
        "--actor-template",
        action="append",
        dest="actor_templates",
        help="Template actor signature, in handoff actor order; repeat for each actor",
    )
    compile_command.add_argument(
        "--no-verify",
        action="store_true",
        help="Skip the generated binary's WolvenKit JSON verification pass",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate":
            document = load_json(args.path)
            if document.get("kind") == RID_KIND:
                report = validate_handoff(document)
            else:
                report = validate_compiled_document(document)
            _print_validation(report)
            return 0 if report.ok else 1
        build_report = compile_binary(
            args.handoff,
            args.template,
            args.output,
            wolvenkit_path=args.wolvenkit,
            actor_template_signatures=args.actor_templates,
            json_output_path=args.json_output,
            report_path=args.report,
            verify=not args.no_verify,
        )
        print(json.dumps(build_report, indent=2))
        return 0
    except RidCompileError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
