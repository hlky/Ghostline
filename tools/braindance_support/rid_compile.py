"""Compile authored actor and camera samples into a RID document."""
from __future__ import annotations
import copy
import math
from typing import Any, Iterable
from braindance_support.rid_types import (
    _actor_sample,
    RID_REPORT_KIND,
    RidCompileError,
    _patch_durations,
    _root,
    _set_animation_name,
    _set_next_serial,
    _set_tag,
    _tag_signature,
)
from braindance_support.rid_codec import (
    _animation_buffer_from_actor,
    _animation_buffer_from_camera,
    _encode_spline_motion_extraction,
    _is_near_vector,
    _merge_template_pose_channels,
    _multiply_quaternions,
    _proxy_pose_motion_sync,
    _red_transform,
    _replace_compressed_buffer,
    _rotate_vector,
    _sample_time,
    _world_actor_transform,
    encode_compressed_animation,
    euler_degrees_to_quaternion,
    inspect_compressed_buffer,
)
from braindance_support.rid_validation import (
    _collect_handle_ids,
    validate_handoff,
)




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
