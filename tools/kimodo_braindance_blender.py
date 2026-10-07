#!/usr/bin/env python3
"""Blender-side SOMA BVH to Ghostline man_base retargeting."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import bpy
from mathutils import Matrix, Quaternion, Vector


# Target RED/man_base bone -> Kimodo SOMA BVH bone.
BONE_MAP = {
    "Hips": "Hips",
    "Spine": "Spine1",
    "Spine1": "Spine2",
    "Spine2": "Chest",
    "Neck": "Neck1",
    "Neck1": "Neck2",
    "Head": "Head",
    "LeftEye": "LeftEye",
    "RightEye": "RightEye",
    "LeftShoulder": "LeftShoulder",
    "LeftArm": "LeftArm",
    "LeftForeArm": "LeftForeArm",
    "LeftHand": "LeftHand",
    "RightShoulder": "RightShoulder",
    "RightArm": "RightArm",
    "RightForeArm": "RightForeArm",
    "RightHand": "RightHand",
    "LeftUpLeg": "LeftLeg",
    "LeftLeg": "LeftShin",
    "LeftFoot": "LeftFoot",
    "LeftToeBase": "LeftToeBase",
    "RightUpLeg": "RightLeg",
    "RightLeg": "RightShin",
    "RightFoot": "RightFoot",
    "RightToeBase": "RightToeBase",
}

for side in ("Left", "Right"):
    for finger in ("Index", "Middle", "Ring", "Pinky"):
        for segment in (1, 2, 3):
            BONE_MAP[f"{side}Hand{finger}{segment}"] = f"{side}Hand{finger}{segment}"
    for segment in (1, 2):
        BONE_MAP[f"{side}HandThumb{segment}"] = f"{side}HandThumb{segment}"


def parse_args() -> argparse.Namespace:
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bvh", type=Path, required=True)
    parser.add_argument("--actor", required=True)
    parser.add_argument("--start-frame", type=int, required=True)
    parser.add_argument("--end-frame", type=int, required=True)
    parser.add_argument("--blend-in", type=int, required=True)
    parser.add_argument("--blend-out", type=int, required=True)
    parser.add_argument("--output-blend", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    return parser.parse_args(argv)


def actor_armature(actor_id: str) -> tuple[bpy.types.Object, bpy.types.Object]:
    root = bpy.data.objects.get(f"ACTOR_{actor_id}")
    if root is None:
        raise RuntimeError(f"Actor root ACTOR_{actor_id} is missing")
    armatures = [obj for obj in root.children_recursive if obj.type == "ARMATURE"]
    if len(armatures) != 1:
        raise RuntimeError(
            f"Actor {actor_id!r} must have exactly one descendant armature; found {len(armatures)}"
        )
    return root, armatures[0]


def import_bvh(path: Path) -> bpy.types.Object:
    before = set(bpy.data.objects)
    bpy.ops.import_anim.bvh(
        filepath=str(path),
        axis_forward="-Z",
        axis_up="Y",
        global_scale=1.0,
        frame_start=1,
        use_fps_scale=False,
        update_scene_fps=False,
        update_scene_duration=False,
        use_cyclic=False,
        rotate_mode="NATIVE",
    )
    imported = [obj for obj in bpy.data.objects if obj not in before and obj.type == "ARMATURE"]
    if len(imported) != 1:
        raise RuntimeError(f"Expected one imported BVH armature; found {len(imported)}")
    return imported[0]


def hierarchy(armature: bpy.types.Object) -> list[bpy.types.PoseBone]:
    result: list[bpy.types.PoseBone] = []

    def visit(bone: bpy.types.PoseBone) -> None:
        result.append(bone)
        for child in bone.children:
            visit(child)

    for bone in armature.pose.bones:
        if bone.parent is None:
            visit(bone)
    return result


def local_matrix(global_matrices: dict[str, Matrix], bone: bpy.types.PoseBone) -> Matrix:
    matrix = global_matrices[bone.name]
    if bone.parent is None:
        return matrix.copy()
    return global_matrices[bone.parent.name].inverted_safe() @ matrix


def weight_for(frame: int, start: int, end: int, blend_in: int, blend_out: int) -> float:
    weight = 1.0
    if blend_in:
        weight = min(weight, max(0.0, (frame - start) / blend_in))
    if blend_out:
        weight = min(weight, max(0.0, (end - frame) / blend_out))
    # Smoothstep avoids a visible velocity corner at both handoff boundaries.
    return weight * weight * (3.0 - 2.0 * weight)


def matrix_from_rotation_translation(rotation: Quaternion, translation: Vector) -> Matrix:
    matrix = rotation.to_matrix().to_4x4()
    matrix.translation = translation
    return matrix


def key_pose_bone(bone: bpy.types.PoseBone, frame: int) -> None:
    bone.keyframe_insert(data_path="location", frame=frame, group=bone.name)
    if bone.rotation_mode == "QUATERNION":
        bone.keyframe_insert(data_path="rotation_quaternion", frame=frame, group=bone.name)
    elif bone.rotation_mode == "AXIS_ANGLE":
        bone.keyframe_insert(data_path="rotation_axis_angle", frame=frame, group=bone.name)
    else:
        bone.keyframe_insert(data_path="rotation_euler", frame=frame, group=bone.name)
    bone.keyframe_insert(data_path="scale", frame=frame, group=bone.name)


def capture_target(
    scene: bpy.types.Scene,
    target: bpy.types.Object,
    frames: range,
) -> dict[int, dict[str, Matrix]]:
    captured: dict[int, dict[str, Matrix]] = {}
    for frame in frames:
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        captured[frame] = {bone.name: bone.matrix.copy() for bone in target.pose.bones}
    return captured


def capture_source_deltas(
    scene: bpy.types.Scene,
    source: bpy.types.Object,
    count: int,
) -> list[dict[str, Quaternion]]:
    rest = {
        bone.name: source.data.bones[bone.name].matrix_local.to_quaternion()
        for bone in source.pose.bones
    }
    captured: list[dict[str, Quaternion]] = []
    for index in range(count):
        scene.frame_set(index + 1)
        bpy.context.view_layer.update()
        captured.append(
            {
                bone.name: bone.matrix.to_quaternion() @ rest[bone.name].inverted()
                for bone in source.pose.bones
            }
        )
    return captured


def remove_source(source: bpy.types.Object) -> None:
    action = source.animation_data.action if source.animation_data else None
    armature_data = source.data
    bpy.data.objects.remove(source, do_unlink=True)
    if action and action.users == 0:
        bpy.data.actions.remove(action)
    if armature_data.users == 0:
        bpy.data.armatures.remove(armature_data)


def main() -> None:
    args = parse_args()
    scene = bpy.context.scene
    original_start = scene.frame_start
    original_end = scene.frame_end
    original_fps = scene.render.fps
    _, target = actor_armature(args.actor)
    target_order = hierarchy(target)
    target_names = {bone.name for bone in target_order}
    missing_target = sorted(set(BONE_MAP) - target_names)
    if missing_target:
        raise RuntimeError("Target armature is missing mapped bones: " + ", ".join(missing_target))

    frames = range(args.start_frame, args.end_frame + 1)
    originals = capture_target(scene, target, frames)
    source = import_bvh(args.bvh.resolve())
    source_names = {bone.name for bone in source.pose.bones}
    active_map = {
        target_name: source_name
        for target_name, source_name in BONE_MAP.items()
        if source_name in source_names
    }
    missing_essential = sorted(
        name for name in ("Hips", "LeftArm", "RightArm", "LeftLeg", "RightLeg")
        if name not in active_map.values()
    )
    if missing_essential:
        raise RuntimeError("Source armature is missing essential bones: " + ", ".join(missing_essential))

    count = len(frames)
    source_deltas = capture_source_deltas(scene, source, count)
    remove_source(source)
    target_rest_rotations = {
        bone.name: target.data.bones[bone.name].matrix_local.to_quaternion()
        for bone in target_order
    }

    changed_bones = [bone for bone in target_order if bone.name in active_map]
    for index, frame in enumerate(frames):
        scene.frame_set(frame)
        original_globals = originals[frame]
        desired_globals: dict[str, Matrix] = {}
        weight = weight_for(
            frame,
            args.start_frame,
            args.end_frame,
            args.blend_in,
            args.blend_out,
        )
        for bone in target_order:
            original_local = local_matrix(original_globals, bone)
            parent_global = (
                desired_globals[bone.parent.name] if bone.parent is not None else Matrix.Identity(4)
            )
            if bone.name in active_map:
                source_delta = source_deltas[index][active_map[bone.name]]
                generated_global_rotation = source_delta @ target_rest_rotations[bone.name]
                original_global_rotation = original_globals[bone.name].to_quaternion()
                final_global_rotation = original_global_rotation.slerp(
                    generated_global_rotation,
                    weight,
                )
                parent_rotation = parent_global.to_quaternion()
                final_local_rotation = parent_rotation.inverted() @ final_global_rotation
                desired_local = matrix_from_rotation_translation(
                    final_local_rotation,
                    original_local.translation,
                )
            else:
                desired_local = original_local
            desired_globals[bone.name] = parent_global @ desired_local
        for bone in target_order:
            bone.matrix = desired_globals[bone.name]
        bpy.context.view_layer.update()
        for bone in changed_bones:
            key_pose_bone(bone, frame)

    scene.frame_start = original_start
    scene.frame_end = original_end
    scene.render.fps = original_fps
    scene.frame_set(args.start_frame)
    output = args.output_blend.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(output), check_existing=False)
    report = {
        "schema_version": 1,
        "actor": args.actor,
        "source_bvh": str(args.bvh.resolve()),
        "output_blend": str(output),
        "destination_frames": [args.start_frame, args.end_frame],
        "blend_in_frames": args.blend_in,
        "blend_out_frames": args.blend_out,
        "mapped_bones": active_map,
        "source_bones_ignored": sorted(source_names - set(active_map.values())),
        "root_translation": "discarded; existing ACTOR root motion retained",
    }
    report_path = args.report.resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("GHOSTLINE_KIMODO_RETARGET_COMPLETE " + json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
