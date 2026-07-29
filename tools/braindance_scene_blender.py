"""Blender-side implementation for tools/braindance_scene.py."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

import bpy  # type: ignore[import-not-found]
from mathutils import Matrix, Quaternion, Vector  # type: ignore[import-not-found]


COLLECTION_NAMES = (
    "BD_ORIGIN",
    "ENVIRONMENT_REFERENCE",
    "ACTORS",
    "PROPS",
    "CAMERAS",
    "CLUES",
)


def parse_args() -> argparse.Namespace:
    arguments = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--no-glb", action="store_true")
    parser.add_argument("--bake-existing", action="store_true")
    return parser.parse_args(arguments)


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for owner in list(obj.users_collection):
        owner.objects.unlink(obj)
    collection.objects.link(obj)


def create_collection(name: str) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    return collection


def vector3(value: list[float]) -> tuple[float, float, float]:
    return float(value[0]), float(value[1]), float(value[2])


def euler3(value: list[float]) -> tuple[float, float, float]:
    return tuple(math.radians(float(item)) for item in value)


def make_material(name: str, color: list[float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = tuple(float(item) for item in color)
    return material


def apply_transform(obj: bpy.types.Object, transform: dict[str, Any], *, camera: bool = False) -> None:
    if "location" in transform:
        obj.location = vector3(transform["location"])
    if "scale" in transform:
        obj.scale = vector3(transform["scale"])
    if "rotation_degrees" in transform:
        obj.rotation_mode = "XYZ"
        obj.rotation_euler = euler3(transform["rotation_degrees"])
    elif camera and "look_at" in transform:
        direction = Vector(vector3(transform["look_at"])) - obj.location
        if direction.length_squared == 0:
            raise RuntimeError(f"Camera key at {obj.location[:]} looks at itself")
        obj.rotation_mode = "XYZ"
        obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler("XYZ")
    if camera and "focal_length" in transform:
        obj.data.lens = float(transform["focal_length"])


def insert_transform_key(obj: bpy.types.Object, frame: int, *, camera: bool = False) -> None:
    obj.keyframe_insert("location", frame=frame, group="Transform")
    obj.keyframe_insert("rotation_euler", frame=frame, group="Transform")
    obj.keyframe_insert("scale", frame=frame, group="Transform")
    if camera:
        obj.data.keyframe_insert("lens", frame=frame, group="Camera")


def set_interpolation(owner: Any, interpolation: str) -> None:
    animation = owner.animation_data
    if animation is None or animation.action is None:
        return
    action = animation.action
    if hasattr(action, "fcurves"):
        curves = list(action.fcurves)
    else:
        curves = [
            curve
            for layer in action.layers
            for strip in layer.strips
            for channelbag in strip.channelbags
            for curve in channelbag.fcurves
        ]
    for curve in curves:
        for point in curve.keyframe_points:
            point.interpolation = interpolation


def create_environment_box(
    box: dict[str, Any],
    collection: bpy.types.Collection,
    origin: bpy.types.Object,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1)
    obj = bpy.context.object
    obj.name = f"ENV_{box['id']}"
    move_to_collection(obj, collection)
    obj.parent = origin
    obj.location = vector3(box["location"])
    obj.rotation_euler = euler3(box.get("rotation_degrees", [0, 0, 0]))
    obj.scale = vector3(box["size"])
    color = box.get("color", [0.18, 0.2, 0.24, 1.0])
    obj.data.materials.append(make_material(f"MAT_{box['id']}", color))
    obj["ghostline_type"] = "environment_reference"
    obj["ghostline_id"] = box["id"]
    return obj


def import_glb(path: Path) -> list[bpy.types.Object]:
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(path))
    return [obj for obj in bpy.data.objects if obj not in before]


def _load_actor_rig_contract(
    actor: dict[str, Any],
    repo_root: Path,
) -> tuple[dict[str, Any], str] | None:
    rig = actor.get("rig")
    if not isinstance(rig, dict):
        return None
    path = (repo_root / str(rig["contract"])).resolve()
    raw = path.read_bytes()
    contract = json.loads(raw)
    return contract, hashlib.sha256(raw).hexdigest()


def parent_imported_roots(
    objects: list[bpy.types.Object],
    parent: bpy.types.Object,
    collection: bpy.types.Collection | None = None,
) -> None:
    imported = set(objects)
    for obj in objects:
        if collection is not None:
            move_to_collection(obj, collection)
        if obj.parent not in imported:
            obj.parent = parent


def create_proxy_actor(
    actor: dict[str, Any],
    root: bpy.types.Object,
    collection: bpy.types.Collection,
) -> None:
    height = float(actor["proxy"]["height"])
    material = make_material(f"MAT_ACTOR_{actor['id']}", actor["proxy"]["color"])

    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=height * 0.17, depth=height * 0.58)
    body = bpy.context.object
    body.name = f"PROXY_{actor['id']}_body"
    move_to_collection(body, collection)
    body.parent = root
    body.location = (0, 0, height * 0.42)
    body.data.materials.append(material)

    bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=height * 0.105)
    head = bpy.context.object
    head.name = f"PROXY_{actor['id']}_head"
    move_to_collection(head, collection)
    head.parent = root
    head.location = (0, 0, height * 0.83)
    head.data.materials.append(material)

    bpy.ops.mesh.primitive_cube_add(size=1)
    facing = bpy.context.object
    facing.name = f"PROXY_{actor['id']}_facing"
    move_to_collection(facing, collection)
    facing.parent = root
    facing.location = (0, -height * 0.13, height * 0.83)
    facing.scale = (height * 0.03, height * 0.06, height * 0.03)
    facing.data.materials.append(material)


def create_actor(
    actor: dict[str, Any],
    collection: bpy.types.Collection,
    origin: bpy.types.Object,
    repo_root: Path,
) -> bpy.types.Object:
    root = bpy.data.objects.new(f"ACTOR_{actor['id']}", None)
    collection.objects.link(root)
    root.empty_display_type = "ARROWS"
    root.empty_display_size = 0.35
    root.parent = origin
    root["ghostline_type"] = "actor"
    root["ghostline_id"] = actor["id"]
    root["ghostline_actor_id"] = int(actor["actor_id"])
    root["ghostline_performer_id"] = int(actor["performer_id"])
    root["ghostline_display_name"] = actor["display_name"]

    if "asset" in actor:
        imported = import_glb((repo_root / actor["asset"]["path"]).resolve())
        parent_imported_roots(imported, root, collection)
        for obj in imported:
            obj["ghostline_actor_id"] = actor["id"]
            if actor.get("body_animation") is not None:
                obj.animation_data_clear()
    else:
        create_proxy_actor(actor, root, collection)
    for channel_name in ("facial", "cyberware"):
        channel = actor.get(channel_name)
        asset = channel.get("asset") if isinstance(channel, dict) else None
        if isinstance(asset, dict):
            imported = import_glb((repo_root / asset["path"]).resolve())
            parent_imported_roots(imported, root, collection)
            for obj in imported:
                obj["ghostline_actor_id"] = actor["id"]
                obj["ghostline_rid_channel"] = channel_name

    apply_transform(root, actor["start"])
    inherited = dict(actor["start"])
    keys = actor["keys"] or [{"frame": 0}]
    for key in keys:
        inherited.update({name: value for name, value in key.items() if name != "frame"})
        apply_transform(root, inherited)
        insert_transform_key(root, int(key["frame"]))
    set_interpolation(root, actor["interpolation"])
    if actor.get("body_animation") is not None:
        _apply_body_animation(actor, root)
    return root


def create_camera(
    spec: dict[str, Any],
    collection: bpy.types.Collection,
    origin: bpy.types.Object,
) -> bpy.types.Object:
    camera_data = bpy.data.cameras.new(f"CAMERA_DATA_{spec['id']}")
    camera = bpy.data.objects.new(f"CAMERA_{spec['id']}", camera_data)
    collection.objects.link(camera)
    camera.parent = origin
    camera["ghostline_type"] = "recording_camera"
    camera["ghostline_id"] = spec["id"]
    camera["ghostline_recorded_actor"] = spec["recorded_actor"]
    for key in spec["keys"]:
        apply_transform(camera, key, camera=True)
        insert_transform_key(camera, int(key["frame"]), camera=True)
    set_interpolation(camera, spec["interpolation"])
    set_interpolation(camera_data, spec["interpolation"])
    bpy.context.scene.camera = camera
    return camera


def create_clue(
    clue: dict[str, Any],
    collection: bpy.types.Collection,
    origin: bpy.types.Object,
    frame_start: int,
    frame_end: int,
) -> bpy.types.Object:
    obj = bpy.data.objects.new(f"CLUE_{clue['id']}", None)
    collection.objects.link(obj)
    obj.parent = origin
    obj.location = vector3(clue["position"])
    obj.empty_display_type = "SPHERE" if clue["layer"] == "Audio" else "CUBE"
    obj.empty_display_size = 0.22
    obj.color = {
        "Visual": (0.15, 0.55, 1.0, 1.0),
        "Audio": (0.95, 0.55, 0.1, 1.0),
        "Thermal": (1.0, 0.15, 0.1, 1.0),
    }[clue["layer"]]
    obj["ghostline_type"] = "braindance_clue"
    obj["ghostline_id"] = clue["id"]
    obj["ghostline_layer"] = clue["layer"]
    obj["ghostline_fact"] = clue["fact"]
    obj["ghostline_start_frame"] = int(clue["frames"][0])
    obj["ghostline_end_frame"] = int(clue["frames"][1])

    visible_start, visible_end = (int(item) for item in clue["frames"])
    for frame, hidden in (
        (frame_start, frame_start < visible_start),
        (max(frame_start, visible_start - 1), True),
        (visible_start, False),
        (visible_end, False),
        (min(frame_end, visible_end + 1), True),
    ):
        obj.hide_viewport = hidden
        obj.hide_render = hidden
        obj.keyframe_insert("hide_viewport", frame=frame)
        obj.keyframe_insert("hide_render", frame=frame)
    return obj


def create_readme_text(spec: dict[str, Any], spec_path: Path) -> None:
    text = bpy.data.texts.new("GHOSTLINE_BRAINDANCE_README")
    text.write(
        "Generated by tools/braindance_scene.py\n"
        f"Source: {spec_path}\n"
        f"Braindance: {spec['name']}\n"
        "Edit the JSON spec for deterministic changes. Blender edits are suitable "
        "for animation exploration but are not the checked source of truth.\n"
    )


def select_export_objects(
    actor_roots: list[bpy.types.Object],
    camera: bpy.types.Object,
) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    roots = set(actor_roots)
    for obj in bpy.data.objects:
        ancestor = obj
        while ancestor is not None and ancestor not in roots:
            ancestor = ancestor.parent
        if ancestor in roots:
            obj.select_set(True)
    camera.select_set(True)


def _transform_row(
    frame: int,
    matrix: Matrix,
) -> dict[str, Any]:
    location, rotation, scale = matrix.decompose()
    rotation.normalize()
    return {
        "frame": frame,
        "translation": [float(value) for value in location],
        "rotation": [
            float(rotation.x),
            float(rotation.y),
            float(rotation.z),
            float(rotation.w),
        ],
        "scale": [float(value) for value in scale],
    }


_BLENDER_MODEL_TO_RED = Matrix(
    (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, -1.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )
)


def _red_transform_matrix(value: dict[str, Any]) -> Matrix:
    translation = Vector(
        tuple(float(item) for item in value["translation"])
    )
    rotation_values = [float(item) for item in value["rotation"]]
    rotation = Quaternion(
        (
            rotation_values[3],
            rotation_values[0],
            rotation_values[1],
            rotation_values[2],
        )
    )
    scale = Vector(tuple(float(item) for item in value["scale"]))
    return Matrix.LocRotScale(translation, rotation, scale)


def _rig_absolute_local_matrix(
    armature: bpy.types.Object,
    bone_name: str,
    bone_contract: dict[str, Any],
    matrix_basis: Matrix,
) -> Matrix:
    """Map Blender's pose-bone delta onto the RED rig's local rest transform."""
    blender_model_rotation = (
        armature.data.bones[bone_name].matrix_local.to_quaternion()
    )
    red_model_rotation_values = [
        float(item)
        for item in bone_contract["model_rest"]["rotation"]
    ]
    red_model_rotation = Quaternion(
        (
            red_model_rotation_values[3],
            red_model_rotation_values[0],
            red_model_rotation_values[1],
            red_model_rotation_values[2],
        )
    )
    blender_to_red_rotation = _BLENDER_MODEL_TO_RED.to_quaternion()
    blender_bone_to_red_bone = (
        red_model_rotation.conjugated()
        @ blender_to_red_rotation
        @ blender_model_rotation
    )
    blender_bone_to_red_bone.normalize()
    basis_change = blender_bone_to_red_bone.to_matrix().to_4x4()
    red_delta = basis_change @ matrix_basis @ basis_change.inverted()
    return _red_transform_matrix(bone_contract["local_rest"]) @ red_delta


def _descendants(root: bpy.types.Object) -> list[bpy.types.Object]:
    result: list[bpy.types.Object] = []
    pending = list(root.children)
    while pending:
        current = pending.pop()
        result.append(current)
        pending.extend(current.children)
    return result


def _actor_armature(
    root: bpy.types.Object,
    actor: dict[str, Any],
) -> bpy.types.Object | None:
    armatures = [obj for obj in _descendants(root) if obj.type == "ARMATURE"]
    configured = actor.get("asset", {}).get("armature")
    if configured:
        matches = [obj for obj in armatures if obj.name == configured]
        if len(matches) != 1:
            raise RuntimeError(
                f"Actor {actor['id']} armature {configured!r} was not found uniquely"
            )
        return matches[0]
    if len(armatures) > 1:
        raise RuntimeError(
            f"Actor {actor['id']} imports multiple armatures; set asset.armature"
        )
    return armatures[0] if armatures else None


def _wrapped_angle_delta(current: float, previous: float) -> float:
    return (current - previous + math.pi) % (2.0 * math.pi) - math.pi


def _apply_body_animation(
    actor: dict[str, Any],
    root: bpy.types.Object,
) -> None:
    animation = actor["body_animation"]
    if animation["type"] != "walk_from_root_motion":
        raise RuntimeError(
            f"Unsupported body animation type {animation['type']!r}"
        )
    armature = _actor_armature(root, actor)
    if armature is None:
        raise RuntimeError(
            f"Actor {actor['id']} body animation requires an armature"
        )
    required = {
        "Hips",
        "Spine1",
        "LeftUpLeg",
        "RightUpLeg",
        "LeftLeg",
        "RightLeg",
        "LeftFoot",
        "RightFoot",
        "LeftArm",
        "RightArm",
        "LeftForeArm",
        "RightForeArm",
    }
    missing = sorted(required - set(armature.pose.bones.keys()))
    if missing:
        raise RuntimeError(
            f"Actor {actor['id']} rig is missing gait bones: {', '.join(missing)}"
        )
    scene = bpy.context.scene
    original_frame = scene.frame_current
    stride_length = float(animation.get("stride_length", 0.9))
    leg_swing = math.radians(float(animation.get("leg_swing_degrees", 24.0)))
    knee_bend = math.radians(float(animation.get("knee_bend_degrees", 34.0)))
    arm_swing = math.radians(float(animation.get("arm_swing_degrees", 18.0)))
    phase = math.radians(float(animation.get("phase_degrees", 0.0)))
    speed_threshold = float(animation.get("speed_threshold", 0.02))
    previous_location: Vector | None = None
    previous_yaw: float | None = None
    target_bones = sorted(required)

    def axis_rotation(
        axis: tuple[float, float, float],
        radians: float,
    ) -> Quaternion:
        return Quaternion(Vector(axis).normalized(), radians)

    def set_axis_rotation(
        name: str,
        axis: tuple[float, float, float],
        radians: float,
    ) -> None:
        bone = armature.pose.bones[name]
        bone.rotation_mode = "QUATERNION"
        bone.rotation_quaternion = axis_rotation(axis, radians)

    for frame in range(scene.frame_start, scene.frame_end + 1):
        scene.frame_set(frame)
        location = root.matrix_basis.translation.copy()
        yaw = float(root.rotation_euler.z)
        distance = (
            0.0
            if previous_location is None
            else float((location - previous_location).length)
        )
        turn_distance = (
            0.0
            if previous_yaw is None
            else abs(_wrapped_angle_delta(yaw, previous_yaw)) * 0.18
        )
        travel = distance + turn_distance
        speed = travel * float(scene.render.fps)
        moving = speed > speed_threshold
        if moving:
            phase += travel / stride_length * math.tau
        activity = 0.0 if not moving else min(1.0, max(0.45, speed / 0.65))
        stride = math.sin(phase)
        for name in target_bones:
            bone = armature.pose.bones[name]
            bone.rotation_mode = "QUATERNION"
            bone.rotation_quaternion = Quaternion()

        left_leg = leg_swing * stride * activity
        right_leg = -left_leg
        set_axis_rotation("LeftUpLeg", (-0.05, 0.88, 0.47), left_leg)
        set_axis_rotation("RightUpLeg", (-0.11, 0.97, 0.20), right_leg)
        set_axis_rotation(
            "LeftLeg",
            (0.0, -1.0, 0.0),
            knee_bend * max(0.0, -stride) * activity,
        )
        set_axis_rotation(
            "RightLeg",
            (0.0, -1.0, 0.0),
            knee_bend * max(0.0, stride) * activity,
        )
        set_axis_rotation("LeftFoot", (0.0, -1.0, 0.0), -left_leg * 0.45)
        set_axis_rotation("RightFoot", (0.0, -1.0, 0.0), -right_leg * 0.45)

        # The RED man_base rest pose is an authoring A-pose. Apply a stable
        # lowered-arm base pose, then layer the authored gait swing over it.
        left_arm_base = axis_rotation((0.54, 0.08, -0.84), math.radians(31.0))
        right_arm_base = axis_rotation((0.75, -0.05, -0.66), math.radians(39.0))
        left_arm_swing = axis_rotation(
            (0.0, 1.0, 0.0),
            -arm_swing * stride * activity,
        )
        right_arm_swing = axis_rotation(
            (0.0, 1.0, 0.0),
            arm_swing * stride * activity,
        )
        armature.pose.bones["LeftArm"].rotation_quaternion = (
            left_arm_base @ left_arm_swing
        )
        armature.pose.bones["RightArm"].rotation_quaternion = (
            right_arm_base @ right_arm_swing
        )
        set_axis_rotation(
            "LeftForeArm",
            (0.0, 1.0, 0.0),
            math.radians(16.0)
            + math.radians(10.0) * max(0.0, stride) * activity,
        )
        set_axis_rotation(
            "RightForeArm",
            (0.0, 1.0, 0.0),
            math.radians(16.0)
            + math.radians(10.0) * max(0.0, -stride) * activity,
        )
        set_axis_rotation(
            "Hips",
            (-0.77, 0.34, 0.54),
            math.radians(5.0) * stride * activity,
        )
        set_axis_rotation(
            "Spine1",
            (-0.39, -0.78, -0.49),
            math.radians(2.5) * stride * activity,
        )
        for name in target_bones:
            armature.pose.bones[name].keyframe_insert(
                "rotation_quaternion",
                frame=frame,
                group="Ghostline Body",
            )
        previous_location = location
        previous_yaw = yaw
    set_interpolation(armature, "LINEAR")
    scene.frame_set(original_frame)


def _channel_armature(
    root: bpy.types.Object,
    actor: dict[str, Any],
    channel_name: str,
) -> bpy.types.Object | None:
    channel = actor.get(channel_name)
    if not isinstance(channel, dict):
        return None
    configured = channel.get("armature")
    asset = channel.get("asset")
    if not configured and isinstance(asset, dict):
        configured = asset.get("armature")
    if configured:
        matches = [
            obj
            for obj in _descendants(root)
            if obj.type == "ARMATURE" and obj.name == configured
        ]
        if len(matches) != 1:
            raise RuntimeError(
                f"Actor {actor['id']} {channel_name} armature "
                f"{configured!r} was not found uniquely"
            )
        return matches[0]
    return None


def _resolve_float_track(
    actor: dict[str, Any],
    channel_name: str,
    track: dict[str, Any],
) -> float:
    target = bpy.data.objects.get(track["object"])
    if target is None:
        raise RuntimeError(
            f"Actor {actor['id']} {channel_name} track {track['index']} "
            f"references missing object {track['object']!r}"
        )
    try:
        value = target.path_resolve(track["data_path"])
    except (ValueError, TypeError) as exc:
        raise RuntimeError(
            f"Actor {actor['id']} {channel_name} track {track['index']} "
            f"cannot resolve {track['object']}.{track['data_path']}"
        ) from exc
    if not isinstance(value, (int, float)):
        raise RuntimeError(
            f"Actor {actor['id']} {channel_name} track {track['index']} "
            "does not resolve to a number"
        )
    return float(value)


def _bake_rig_channel(
    scene: bpy.types.Scene,
    actor: dict[str, Any],
    root: bpy.types.Object,
    channel_name: str,
    frames: range,
) -> dict[str, Any] | None:
    channel = actor.get(channel_name)
    if not isinstance(channel, dict):
        return None
    armature = _channel_armature(root, actor, channel_name)
    bone_names = (
        [bone.name for bone in armature.data.bones] if armature is not None else []
    )
    joint_samples: dict[int, list[dict[str, Any]]] = {}
    track_samples: dict[int, list[dict[str, Any]]] = {
        int(track["index"]): [] for track in channel.get("tracks", [])
    }
    for frame in frames:
        scene.frame_set(frame)
        if armature is not None:
            for joint_index, bone_name in enumerate(bone_names):
                joint_samples.setdefault(joint_index, []).append(
                    _transform_row(
                        frame,
                        armature.pose.bones[bone_name].matrix_basis.copy(),
                    )
                )
        for track in channel.get("tracks", []):
            track_samples[int(track["index"])].append(
                {
                    "frame": frame,
                    "value": _resolve_float_track(actor, channel_name, track),
                }
            )
    return {
        "armature": armature.name if armature is not None else None,
        "bone_order": bone_names,
        "bone_count": len(bone_names) if bone_names else None,
        "joints": [
            {
                "index": joint_index,
                "name": bone_names[joint_index],
                "samples": samples,
            }
            for joint_index, samples in sorted(joint_samples.items())
            if not _is_default_joint(samples)
        ],
        "tracks": [
            {"index": index, "samples": samples}
            for index, samples in sorted(track_samples.items())
        ],
    }


def _is_default_joint(samples: list[dict[str, Any]], tolerance: float = 1e-6) -> bool:
    for sample in samples:
        if any(abs(value) > tolerance for value in sample["translation"]):
            return False
        x, y, z, w = sample["rotation"]
        if abs(x) > tolerance or abs(y) > tolerance or abs(z) > tolerance:
            return False
        if abs(abs(w) - 1.0) > tolerance:
            return False
        if any(abs(value - 1.0) > tolerance for value in sample["scale"]):
            return False
    return True


def bake_animation_samples(
    scene: bpy.types.Scene,
    plan: dict[str, Any],
    actor_roots: list[bpy.types.Object],
    camera: bpy.types.Object,
    repo_root: Path,
) -> dict[str, Any]:
    frame_start = int(plan["frames"]["start"])
    frame_end = int(plan["frames"]["end"])
    frames = range(frame_start, frame_end + 1)
    original_frame = scene.frame_current
    actors: list[dict[str, Any]] = []
    for actor, root in zip(plan["actors"], actor_roots, strict=True):
        scene.frame_set(frame_start)
        start_location, start_rotation, start_scale = root.matrix_basis.decompose()
        start_rotation.normalize()
        inverse_start_rotation = start_rotation.conjugated()
        armature = _actor_armature(root, actor)
        rig_contract_row = _load_actor_rig_contract(actor, repo_root)
        rig_contract = (
            rig_contract_row[0] if rig_contract_row is not None else None
        )
        rig_contract_sha256 = (
            rig_contract_row[1] if rig_contract_row is not None else None
        )
        if rig_contract is not None:
            if armature is None:
                raise RuntimeError(
                    f"Actor {actor['id']} rig contract has no armature"
                )
            bone_names = [bone["name"] for bone in rig_contract["bones"]]
            missing = sorted(set(bone_names) - set(armature.pose.bones.keys()))
            extra = sorted(set(armature.pose.bones.keys()) - set(bone_names))
            if missing or extra:
                raise RuntimeError(
                    f"Actor {actor['id']} armature/contract mismatch; "
                    f"missing={missing}, extra={extra}"
                )
            trajectory_index = int(rig_contract["trajectory_joint_index"])
        else:
            bone_names = (
                [bone.name for bone in armature.data.bones]
                if armature is not None
                else []
            )
            trajectory_index = 1 if len(bone_names) > 1 or not bone_names else 0
        joint_samples: dict[int, list[dict[str, Any]]] = {}
        for frame in frames:
            scene.frame_set(frame)
            location, rotation, scale = root.matrix_basis.decompose()
            rotation.normalize()
            root_delta_location = inverse_start_rotation @ (location - start_location)
            root_delta_rotation = inverse_start_rotation @ rotation
            root_delta_scale = Vector(
                (
                    scale.x / start_scale.x,
                    scale.y / start_scale.y,
                    scale.z / start_scale.z,
                )
            )
            root_delta = Matrix.LocRotScale(
                root_delta_location,
                root_delta_rotation,
                root_delta_scale,
            )
            if armature is None:
                joint_samples.setdefault(trajectory_index, []).append(
                    _transform_row(frame, root_delta)
                )
                continue
            for joint_index, bone_name in enumerate(bone_names):
                basis = armature.pose.bones[bone_name].matrix_basis.copy()
                if joint_index == trajectory_index:
                    basis = root_delta @ basis
                elif bone_name == "reference_joint":
                    # Vanilla scene RIDs keep the trajectory joint local and
                    # extract its delta into motionExtraction, but also bake
                    # the performer's scene-space transform into the separate
                    # reference joint. Leaving reference_joint at identity
                    # makes the RID evaluator lose the moving performer's
                    # stable scene reference.
                    basis = root.matrix_basis.copy()
                elif rig_contract is not None:
                    basis = _rig_absolute_local_matrix(
                        armature,
                        bone_name,
                        rig_contract["bones"][joint_index],
                        basis,
                    )
                joint_samples.setdefault(joint_index, []).append(
                    _transform_row(frame, basis)
                )
        joints = [
            {
                "index": joint_index,
                "name": (
                    bone_names[joint_index]
                    if bone_names
                    else "__ghostline_trajectory__"
                ),
                "samples": samples,
            }
            for joint_index, samples in sorted(joint_samples.items())
            if (
                rig_contract is not None
                or joint_index == trajectory_index
                or not _is_default_joint(samples)
            )
        ]
        actors.append(
            {
                "id": actor["id"],
                "armature": armature.name if armature is not None else None,
                "bone_order": bone_names,
                "bone_count": len(bone_names) if bone_names else None,
                "rig_contract_sha256": rig_contract_sha256,
                "trajectory_joint_index": trajectory_index,
                "joints": joints,
                "facial": _bake_rig_channel(
                    scene,
                    actor,
                    root,
                    "facial",
                    frames,
                ),
                "cyberware": _bake_rig_channel(
                    scene,
                    actor,
                    root,
                    "cyberware",
                    frames,
                ),
            }
        )
    camera_samples: list[dict[str, Any]] = []
    for frame in frames:
        scene.frame_set(frame)
        row = _transform_row(frame, camera.matrix_basis)
        row["focal_length"] = float(camera.data.lens)
        camera_samples.append(row)
    scene.frame_set(original_frame)
    return {
        "schema_version": 1,
        "coordinate_space": "blender_local_z_up_right_handed",
        "frame_start": frame_start,
        "frame_end": frame_end,
        "sample_rate": int(plan["fps"]),
        "actors": actors,
        "camera": {
            "id": plan["recording_camera"]["id"],
            "samples": camera_samples,
        },
    }


def main() -> None:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    sys.path.insert(0, str(repo_root / "tools"))
    import braindance_scene  # pylint: disable=import-error,import-outside-toplevel

    spec = braindance_scene.load_json(args.spec)
    report = braindance_scene.validate_spec(spec, repo_root=repo_root)
    if not report.ok:
        raise RuntimeError("\n".join(report.errors))
    plan = braindance_scene.normalized_plan(spec)
    blend_path = braindance_scene.resolve_repo_path(
        plan["outputs"]["blend"], repo_root=repo_root
    )
    glb_path = braindance_scene.resolve_repo_path(
        plan["outputs"]["glb"], repo_root=repo_root
    )
    manifest_path = braindance_scene.resolve_repo_path(
        plan["outputs"]["manifest"], repo_root=repo_root
    )
    for path in (blend_path, glb_path, manifest_path):
        path.parent.mkdir(parents=True, exist_ok=True)

    if args.bake_existing:
        if not blend_path.is_file():
            raise RuntimeError(f"Blender scene does not exist: {blend_path}")
        bpy.ops.wm.open_mainfile(filepath=str(blend_path))
        scene = bpy.context.scene
        actor_roots = []
        for actor in plan["actors"]:
            root = bpy.data.objects.get(f"ACTOR_{actor['id']}")
            if root is None:
                raise RuntimeError(
                    f"Existing scene is missing ACTOR_{actor['id']}"
                )
            actor_roots.append(root)
        camera = bpy.data.objects.get(
            f"CAMERA_{plan['recording_camera']['id']}"
        )
        if camera is None or camera.type != "CAMERA":
            raise RuntimeError("Existing scene is missing its recording camera")
    else:
        bpy.ops.wm.read_factory_settings(use_empty=True)
        scene = bpy.context.scene
        scene.name = plan["name"]
        scene.render.engine = "BLENDER_EEVEE"
        scene.render.fps = int(plan["fps"])
        scene.frame_start = int(plan["frames"]["start"])
        scene.frame_end = int(plan["frames"]["end"])
        scene.unit_settings.system = "METRIC"
        scene.unit_settings.length_unit = "METERS"
        scene.world = bpy.data.worlds.new("Ghostline Braindance World")
        scene.world.color = (0.025, 0.03, 0.05)

        collections = {name: create_collection(name) for name in COLLECTION_NAMES}
        origin = bpy.data.objects.new(plan["origin"]["name"], None)
        collections["BD_ORIGIN"].objects.link(origin)
        origin.empty_display_type = "PLAIN_AXES"
        origin.empty_display_size = 1.0
        origin.location = vector3(plan["origin"]["location"])
        origin.rotation_euler = euler3(plan["origin"]["rotation_degrees"])
        origin["ghostline_type"] = "braindance_origin"
        origin["ghostline_spec"] = plan["name"]

        for box in plan["environment"]["boxes"]:
            create_environment_box(box, collections["ENVIRONMENT_REFERENCE"], origin)
        for imported in plan["environment"]["imports"]:
            objects = import_glb((repo_root / imported["path"]).resolve())
            parent_imported_roots(
                objects,
                origin,
                collections["ENVIRONMENT_REFERENCE"],
            )
            for obj in objects:
                obj["ghostline_type"] = "environment_reference"
                obj["ghostline_id"] = imported["id"]

        actor_roots = [
            create_actor(actor, collections["ACTORS"], origin, repo_root)
            for actor in plan["actors"]
        ]
        camera = create_camera(
            plan["recording_camera"],
            collections["CAMERAS"],
            origin,
        )
        for clue in plan["clues"]:
            create_clue(
                clue,
                collections["CLUES"],
                origin,
                scene.frame_start,
                scene.frame_end,
            )
        for marker in plan["markers"]:
            scene.timeline_markers.new(marker["name"], frame=int(marker["frame"]))

        create_readme_text(plan, args.spec)
        scene.frame_set(scene.frame_start)

    manifest = braindance_scene.build_handoff_manifest(
        spec,
        args.spec,
        repo_root=repo_root,
    )
    manifest["animation_samples"] = bake_animation_samples(
        scene,
        plan,
        actor_roots,
        camera,
        repo_root,
    )
    manifest["rid_status"] = "custom_animation_compile_ready"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    if not args.bake_existing:
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

    if not args.no_glb:
        select_export_objects(actor_roots, camera)
        bpy.ops.export_scene.gltf(
            filepath=str(glb_path),
            export_format="GLB",
            use_selection=True,
            export_animations=True,
            export_cameras=True,
        )

    print(
        "GHOSTLINE_BRAINDANCE_COMPLETE "
        + json.dumps(
            {
                "blend": str(blend_path),
                "glb": None if args.no_glb else str(glb_path),
                "manifest": str(manifest_path),
                "actors": len(actor_roots),
                "clues": len(plan["clues"]),
                "baked_existing": args.bake_existing,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
