"""Independent validation of handoffs and encoded RID documents."""
from __future__ import annotations
import math
from typing import Any
from braindance_support.rid_types import (
    ANIMATION_SAMPLE_SPACE,
    RID_KIND,
    RidCompileError,
    RidValidationReport,
    _cname,
    _root,
    _serial,
    _tag_signature,
)
from braindance_support.rid_types import (
    _actor_sample,
)
from braindance_support.rid_codec import (
    inspect_compressed_buffer,
    inspect_motion_extraction,
)


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
