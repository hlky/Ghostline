"""Blender-side renderer for decoded neutral-proxy scene RID previews."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


def _arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--video", type=Path, required=True)
    parser.add_argument("--frames-dir", type=Path, required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    return parser.parse_args(argv)


def _reset() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for collection in (
        bpy.data.meshes,
        bpy.data.curves,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights,
    ):
        for block in list(collection):
            if block.users == 0:
                collection.remove(block)


def _material(name: str, color: list[float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    material.roughness = 0.85
    return material


def _skeleton_object(actor: dict, actor_index: int) -> bpy.types.Object:
    first = actor["frames"][0]
    parents = actor["parents"]
    edges = []
    for joint, parent in enumerate(parents):
        if parent < 0:
            continue
        distance = math.sqrt(
            sum((first[joint][axis] - first[parent][axis]) ** 2 for axis in range(3))
        )
        if distance > 1e-5:
            edges.append((parent, joint))
    mesh = bpy.data.meshes.new(f"{actor['signature']}_skeleton")
    mesh.from_pydata(first, edges, [])
    mesh.update()
    obj = bpy.data.objects.new(actor["signature"], mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(
        _material(f"{actor['signature']}_material", actor["color"])
    )

    obj.shape_key_add(name="Basis")
    for preview_frame in range(1, len(actor["frames"])):
        key = obj.shape_key_add(name=f"frame_{preview_frame:04d}")
        for vertex, position in zip(
            key.data, actor["frames"][preview_frame], strict=True
        ):
            vertex.co = position
        blender_frame = preview_frame + 1
        key.value = 0.0
        key.keyframe_insert("value", frame=blender_frame - 1)
        key.value = 1.0
        key.keyframe_insert("value", frame=blender_frame)
        if preview_frame + 1 < len(actor["frames"]):
            key.value = 0.0
            key.keyframe_insert("value", frame=blender_frame + 1)
    obj.modifiers.new("Neutral proxy thickness", "SKIN")
    radii = mesh.skin_vertices[0].data
    radii[0].use_root = True
    for radius in radii:
        radius.radius = (0.022, 0.022)
    for index, name in enumerate(actor["bone_names"]):
        if name in {"Hips", "Spine", "Head"}:
            radii[index].radius = (0.045, 0.045)
    subdivision = obj.modifiers.new("Smooth neutral proxy", "SUBSURF")
    subdivision.levels = 1
    subdivision.render_levels = 1
    obj["rid_signature"] = actor["signature"]
    obj["source_joint_count"] = actor["source_joint_count"]
    obj["approximate_contract"] = actor["approximate_contract"]
    obj.select_set(False)
    return obj


def _floor(bounds: dict) -> None:
    minimum = bounds["min"]
    maximum = bounds["max"]
    center_x = (minimum[0] + maximum[0]) * 0.5
    center_y = (minimum[1] + maximum[1]) * 0.5
    size = max(maximum[0] - minimum[0], maximum[1] - minimum[1], 2.0) * 1.8
    bpy.ops.mesh.primitive_plane_add(
        size=size,
        location=(center_x, center_y, minimum[2] - 0.025),
    )
    floor = bpy.context.object
    floor.name = "Reference floor"
    floor.data.materials.append(
        _material("Reference floor", [0.055, 0.065, 0.085, 1.0])
    )


def _camera(bounds: dict) -> bpy.types.Object:
    minimum = Vector(bounds["min"])
    maximum = Vector(bounds["max"])
    center = (minimum + maximum) * 0.5
    extent = maximum - minimum
    span = max(extent.x, extent.y, extent.z, 1.0)
    data = bpy.data.cameras.new("Review overview camera")
    data.type = "ORTHO"
    data.ortho_scale = span * 1.55
    camera = bpy.data.objects.new("Review overview camera", data)
    bpy.context.collection.objects.link(camera)
    camera.location = center + Vector((span * 1.25, -span * 1.65, span * 1.35))
    camera.rotation_euler = (
        (center - camera.location).to_track_quat("-Z", "Y").to_euler()
    )
    bpy.context.scene.camera = camera
    return camera


def _configure_scene(data: dict, frames_dir: Path) -> None:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.display.shading.light = "STUDIO"
    scene.display.shading.studio_light = "paint.sl"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "BOTH"
    scene.display.shading.background_type = "WORLD"
    scene.display.shading.show_specular_highlight = False
    scene.world.color = (0.012, 0.016, 0.024)
    scene.render.resolution_x = 960
    scene.render.resolution_y = 540
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.fps = int(data["fps"])
    scene.frame_start = 1
    scene.frame_end = int(data["frame_count"])
    scene.render.filepath = str(frames_dir / "frame_")
    scene.render.film_transparent = False
    scene.render.use_file_extension = True


def main() -> None:
    args = _arguments()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    args.video.parent.mkdir(parents=True, exist_ok=True)
    args.frames_dir.mkdir(parents=True, exist_ok=True)
    _reset()
    for index, actor in enumerate(data["actors"]):
        _skeleton_object(actor, index)
    _floor(data["bounds"])
    _camera(data["bounds"])
    _configure_scene(data, args.frames_dir)
    blend_path = args.video.with_suffix(".blend")
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    bpy.ops.render.render(animation=True)


if __name__ == "__main__":
    main()
