"""Render source joint positions as a neutral mannequin; no game assets authored."""
import argparse
import json
from pathlib import Path
import sys

import bpy
from mathutils import Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sex_rid_preview_blender import _reset, _floor, _configure_scene, _material


def skinned_body(data):
    import numpy as np
    from workspot_skin import load_parts, model_matrices, deformation_deltas, rest_matrix, skin_vertices
    manifest = data["skin_manifest"]
    contract = json.loads(Path(manifest["deform_contract"]).read_text(encoding="utf-8"))
    actor = data["actors"][0]
    core_rest = {b["name"]: rest_matrix(b) for b in data["skeleton_contract"]["bones"]}
    parts = []
    for source in manifest["meshes"]:
        parts += load_parts(source["path"], rigid_head=source.get("rigid_head", False))
    material = _material("Neutral source mesh", [.36, .58, .66, 1])
    objects = []
    for part in parts:
        mesh = bpy.data.meshes.new(part["name"])
        mesh.from_pydata(part["vertices"].tolist(), [], part["faces"].tolist())
        obj = bpy.data.objects.new(part["name"], mesh)
        bpy.context.collection.objects.link(obj)
        mesh.materials.append(material)
        for polygon in mesh.polygons:
            polygon.use_smooth = True
        objects.append(obj)
    poses = []
    low, high = np.full(3, np.inf), np.full(3, -np.inf)
    for frame in range(data["frame_count"]):
        models = model_matrices(actor, frame)
        deltas = deformation_deltas(models, contract)
        head_delta = models["Head"] @ np.linalg.inv(core_rest["Head"])
        frames = [skin_vertices(part, deltas, head_delta) for part in parts]
        poses.append(frames)
        for vertices in frames:
            low = np.minimum(low, vertices.min(axis=0))
            high = np.maximum(high, vertices.max(axis=0))
    data["bounds"] = {"min": low.tolist(), "max": high.tolist()}

    def update(scene):
        index = min(max(scene.frame_current - 1, 0), len(poses) - 1)
        for obj, vertices in zip(objects, poses[index], strict=True):
            obj.data.vertices.foreach_set("co", vertices.astype(np.float32).ravel())
            obj.data.update()
    bpy.app.handlers.frame_change_pre.append(update)
    update(bpy.context.scene)


def mannequin(actor):
    names = {name: i for i, name in enumerate(actor["bone_names"])}
    material = _material("Neutral body", [0.16, 0.67, 0.76, 1])
    segments = [
        ("Hips", "Spine1", .13, .09), ("Spine1", "Spine3", .16, .095),
        ("Spine3", "Neck1", .06, .055),
    ]
    for side in ("Left", "Right"):
        segments += [(side + "UpLeg", side + "Leg", .072, .065),
                     (side + "Leg", side + "Foot", .05, .045),
                     (side + "Foot", side + "ToeBase", .05, .035),
                     (side + "Shoulder", side + "Arm", .055, .05),
                     (side + "Arm", side + "ForeArm", .045, .04),
                     (side + "ForeArm", side + "Hand", .034, .03),
                     (side + "Hand", side + "InHandMiddle", .035, .024)]
    objects = []
    for first, last, width, depth in segments:
        if first not in names or last not in names:
            continue
        bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8)
        obj = bpy.context.object
        obj.name = first + "_" + last
        obj.data.materials.append(material)
        for polygon in obj.data.polygons:
            polygon.use_smooth = True
        objects.append((obj, names[first], names[last], width, depth))
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20, ring_count=12)
    head = bpy.context.object
    head.name = "Neutral head (orientation not evaluated)"
    head.data.materials.append(material)
    head.scale = (.095, .09, .13)
    for polygon in head.data.polygons:
        polygon.use_smooth = True
    for index, pose in enumerate(actor["frames"], 1):
        for obj, first, last, width, depth in objects:
            a, b = Vector(pose[first]), Vector(pose[last])
            direction = b - a
            obj.location = (a + b) / 2
            obj.rotation_quaternion = direction.to_track_quat("Z", "Y")
            obj.rotation_mode = "QUATERNION"
            obj.scale = (width, depth, max(direction.length * .55, .01))
            for field in ("location", "rotation_quaternion", "scale"):
                obj.keyframe_insert(field, frame=index)
        origin = Vector(pose[names["Head"]])
        axis = origin - Vector(pose[names.get("Neck1", names["Head"])])
        head.location = origin + (axis.normalized() if axis.length else Vector((0, 0, 1))) * .09
        head.keyframe_insert("location", frame=index)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--video", type=Path, required=True)
    parser.add_argument("--frames-dir", type=Path, required=True)
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:])
    data = json.loads(args.input.read_text(encoding="utf-8"))
    _reset()
    if data.get("skin_manifest"):
        skinned_body(data)
    else:
        for actor in data["actors"]:
            mannequin(actor)
    _floor(data["bounds"])
    minimum, maximum = Vector(data["bounds"]["min"]), Vector(data["bounds"]["max"])
    center = (minimum + maximum) / 2 + Vector((0, 0, .05))
    span = max((maximum - minimum).length, 1.5)
    camera_data = bpy.data.cameras.new("Three-quarter body view")
    camera_data.type = "ORTHO"
    # Blender's orthographic scale is the horizontal span at 16:9.
    camera_data.ortho_scale = max(maximum.z - minimum.z + .5, 1.8) * (960 / 540) * 1.05
    camera = bpy.data.objects.new("Three-quarter body view", camera_data)
    bpy.context.collection.objects.link(camera)
    camera.location = center + Vector((span * .85, span * 1.6, span * .3))
    camera.rotation_euler = (center - camera.location).to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = camera
    _configure_scene(data, args.frames_dir)
    # Workbench studio shading keeps the geometry legible without skin textures.
    bpy.context.scene.display.shading.show_shadows = False
    bpy.ops.render.render(animation=True)


if __name__ == "__main__":
    main()
