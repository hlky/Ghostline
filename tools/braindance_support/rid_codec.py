"""Pure RED compressed-animation encoding, inspection, and transform math."""
from __future__ import annotations
import base64
import bisect
import hashlib
import math
import struct
from typing import Any, Iterable
from braindance_support.rid_types import (
    CONST_TRACK_AUX,
    CONST_TRANSLATION_AUX,
    RidCompileError,
)


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
