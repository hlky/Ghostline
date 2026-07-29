from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import sys
import traceback
from pathlib import Path

import bpy
from mathutils import Vector


VIEW_DIRECTIONS = {
    "hero": Vector((1.15, -2.6, 1.0)),
    "front": Vector((0.0, -2.8, 0.45)),
    "back": Vector((0.0, 2.8, 0.45)),
    "left": Vector((-2.8, 0.0, 0.45)),
    "right": Vector((2.8, 0.0, 0.45)),
}

MATERIAL_CACHE: dict[str, bpy.types.Material] = {}
MATERIAL_CACHE_STATS = {"hits": 0, "misses": 0}


def enable_material_cache() -> None:
    from i_scene_cp77_gltf.main.setup import MaterialBuilder

    if getattr(MaterialBuilder, "_ghostline_cache_enabled", False):
        return
    original_create = MaterialBuilder.create

    def cached_create(builder, materials, material_index):
        if not materials:
            return original_create(builder, materials, material_index)
        raw_material = materials[material_index]
        signature = hashlib.sha1(
            json.dumps(
                {
                    "material_repo": builder.BasePath,
                    "image_format": builder.image_format,
                    "material": raw_material,
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        cached = MATERIAL_CACHE.get(signature)
        if cached is not None and cached.name in bpy.data.materials:
            MATERIAL_CACHE_STATS["hits"] += 1
            return cached

        material = original_create(builder, materials, material_index)
        MATERIAL_CACHE_STATS["misses"] += 1
        if material is not None:
            material.use_fake_user = True
            material["ghostline_material_cache"] = signature
            MATERIAL_CACHE[signature] = material
        return material

    MaterialBuilder.create = cached_create
    MaterialBuilder._ghostline_cache_enabled = True


def parse_args() -> argparse.Namespace:
    values = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--glb", type=Path)
    parser.add_argument("--appearance")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--jobs", type=Path)
    parser.add_argument("--batch-report", type=Path)
    parser.add_argument("--native-pbr", action="store_true")
    parser.add_argument("--resolution", type=int, default=1024)
    parser.add_argument("--samples", type=int, default=128)
    parser.add_argument("--engine", choices=["BLENDER_EEVEE", "CYCLES"], default="CYCLES")
    parser.add_argument("--views", default="hero,back")
    args = parser.parse_args(values)
    if args.jobs is None and not (args.glb and args.appearance and args.output):
        parser.error("--glb, --appearance, and --output are required without --jobs")
    return args


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (
        bpy.data.materials,
        bpy.data.images,
        bpy.data.curves,
        bpy.data.cameras,
        bpy.data.lights,
    ):
        for datablock in list(datablocks):
            if (
                datablocks == bpy.data.materials
                and datablock.get("ghostline_material_cache")
            ):
                continue
            if datablock.users == 0:
                datablocks.remove(datablock)


def import_cp77(glb: Path, appearance: str) -> None:
    try:
        from i_scene_cp77_gltf.importers.import_with_materials import CP77GLBimport
    except ImportError as exc:
        raise RuntimeError("Cyberpunk IO Suite is not enabled in this Blender installation") from exc
    CP77GLBimport(
        with_materials=True,
        filepath=str(glb.resolve()),
        appearances=[appearance],
        scripting=True,
        hide_armatures=True,
        exclude_unused_mats=True,
        image_format="PNG",
    )


def import_native_pbr(glb: Path) -> None:
    result = bpy.ops.import_scene.gltf(filepath=str(glb.resolve()))
    if "FINISHED" not in result:
        raise RuntimeError(f"Blender's native glTF importer failed for {glb}")


def repair_multilayer_masks(glb: Path, appearance: str, output: Path) -> dict[str, object]:
    sidecar = glb.with_suffix(".Material.json")
    if not sidecar.is_file():
        return {"repaired": [], "reason": f"missing sidecar: {sidecar}"}
    payload = json.loads(sidecar.read_text(encoding="utf-8"))
    material_data = next(
        (entry for entry in payload.get("Materials", []) if entry.get("Name") == appearance),
        None,
    )
    if not material_data:
        return {"repaired": [], "reason": f"appearance not found: {appearance}"}
    mask_depot_path = material_data.get("Data", {}).get("MultilayerMask")
    material_repo = payload.get("MaterialRepo")
    material = bpy.data.materials.get(appearance)
    if not mask_depot_path or not material_repo or material is None or material.node_tree is None:
        return {
            "repaired": [],
            "reason": "material, repository, or multilayer mask metadata unavailable",
            "mask_depot_path": mask_depot_path,
            "material_repo": material_repo,
            "blender_material": material.name if material else None,
        }

    mask_path = Path(material_repo).joinpath(*mask_depot_path.replace("\\", "/").split("/"))
    layer_directory = mask_path.with_suffix("")
    layer_directory = layer_directory.with_name(f"{layer_directory.name}_layers")
    repaired: list[str] = []
    attempted: list[str] = []
    failures: list[str] = []
    staged: list[str] = []
    staging_directory = output / "_material_inputs"
    staging_directory.mkdir(parents=True, exist_ok=True)
    for index in range(1, 100):
        layer = material.node_tree.nodes.get(f"Mat_Mod_Layer_{index}")
        if layer is None:
            break
        mask_input = layer.inputs.get("Mask")
        if mask_input is None or mask_input.is_linked:
            continue
        image_path = layer_directory / f"{mask_path.stem}_{index}.png"
        attempted.append(str(image_path.resolve()))
        try:
            image = bpy.data.images.load(str(image_path.resolve()), check_existing=True)
        except RuntimeError:
            staged_path = staging_directory / f"mask_{index}.png"
            source = str(image_path.resolve())
            if sys.platform == "win32" and not source.startswith("\\\\?\\"):
                source = f"\\\\?\\{source}"
            try:
                shutil.copyfile(source, staged_path)
                image = bpy.data.images.load(str(staged_path.resolve()), check_existing=True)
                staged.append(str(staged_path.resolve()))
            except (OSError, RuntimeError) as exc:
                failures.append(f"{image_path.resolve()}: {exc}")
                continue
        image.colorspace_settings.name = "Non-Color"
        node = material.node_tree.nodes.new("ShaderNodeTexImage")
        node.name = f"Multilayer Mask {index}"
        node.label = f"Layer {index} mask"
        node.image = image
        node.location = (-1300, 450 - 400 * index)
        material.node_tree.links.new(node.outputs["Color"], mask_input)
        repaired.append(str(image_path.resolve()))
    return {
        "repaired": repaired,
        "attempted": attempted,
        "failures": failures,
        "staged": staged,
        "layer_directory": str(layer_directory.resolve()),
    }


def mesh_objects() -> list[bpy.types.Object]:
    return [
        obj
        for obj in bpy.context.scene.objects
        if obj.type == "MESH"
        and not obj.hide_render
        and obj.name.casefold() not in {"icosphere", "studio floor"}
        and not obj.name.casefold().startswith("material")
    ]


def world_bounds(objects: list[bpy.types.Object]) -> tuple[Vector, Vector]:
    points = [obj.matrix_world @ Vector(corner) for obj in objects for corner in obj.bound_box]
    if not points:
        raise RuntimeError("Imported GLB contains no renderable mesh bounds")
    minimum = Vector((min(point.x for point in points), min(point.y for point in points), min(point.z for point in points)))
    maximum = Vector((max(point.x for point in points), max(point.y for point in points), max(point.z for point in points)))
    return minimum, maximum


def look_at(obj: bpy.types.Object, target: Vector) -> None:
    obj.rotation_euler = (target - obj.location).to_track_quat("-Z", "Y").to_euler()


def add_area(name: str, location: tuple[float, float, float], energy: float, size: float, target: Vector) -> None:
    data = bpy.data.lights.new(name, "AREA")
    data.energy = energy
    data.shape = "DISK"
    data.size = size
    light = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(light)
    light.location = location
    look_at(light, target)


def configure_cycles(scene: bpy.types.Scene) -> dict[str, object]:
    result: dict[str, object] = {"requested": "HIP", "active": "CPU", "devices": []}
    try:
        addon = bpy.context.preferences.addons.get("cycles")
        if addon is None:
            return result
        preferences = addon.preferences
        preferences.compute_device_type = "HIP"
        preferences.refresh_devices()
        devices: list[dict[str, object]] = []
        gpu_enabled = False
        for device in preferences.devices:
            enabled = device.type == "HIP"
            device.use = enabled
            gpu_enabled = gpu_enabled or enabled
            devices.append({"name": device.name, "type": device.type, "enabled": enabled})
        if gpu_enabled:
            scene.cycles.device = "GPU"
            result["active"] = "HIP"
        result["devices"] = devices
    except Exception as exc:
        result["error"] = str(exc)
    return result


def setup_scene(
    args: argparse.Namespace,
    minimum: Vector,
    maximum: Vector,
) -> tuple[bpy.types.Object, dict[str, object]]:
    scene = bpy.context.scene
    scene.render.engine = args.engine
    scene.render.resolution_x = args.resolution
    scene.render.resolution_y = args.resolution
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = True
    scene.view_settings.look = "AgX - Medium High Contrast"
    cycles_device: dict[str, object] = {"requested": None, "active": None, "devices": []}
    if args.engine == "CYCLES":
        scene.cycles.samples = args.samples
        scene.cycles.use_denoising = True
        cycles_device = configure_cycles(scene)
    else:
        scene.render.image_settings.color_depth = "8"
        scene.render.film_transparent = True
        scene.render.image_settings.compression = 20

    world = scene.world or bpy.data.worlds.new("Item Studio")
    scene.world = world
    world.use_nodes = True
    background = world.node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.012, 0.016, 0.025, 1.0)
    background.inputs["Strength"].default_value = 0.1

    center = (minimum + maximum) * 0.5
    size = maximum - minimum
    span = max(size.x, size.y, size.z, 0.25)
    add_area("Key", tuple(center + Vector((-1.6, -2.1, 2.4)) * span), 150 * span, 2.2 * span, center)
    add_area("Fill", tuple(center + Vector((2.0, -0.8, 1.0)) * span), 65 * span, 2.6 * span, center)
    add_area("Rim", tuple(center + Vector((0.5, 2.2, 2.1)) * span), 200 * span, 1.7 * span, center)

    camera_data = bpy.data.cameras.new("Item Camera")
    camera_data.lens = 72
    camera = bpy.data.objects.new("Item Camera", camera_data)
    scene.collection.objects.link(camera)
    scene.camera = camera
    return camera, cycles_device


def render_views(
    args: argparse.Namespace,
    camera: bpy.types.Object,
    minimum: Vector,
    maximum: Vector,
) -> list[str]:
    center = (minimum + maximum) * 0.5
    size = maximum - minimum
    span = max(size.x, size.y, size.z, 0.25)
    camera.data.lens = 68 if size.z >= max(size.x, size.y) else 78
    distance = span * 2.45
    target = center + Vector((0, 0, size.z * 0.03))
    args.output.mkdir(parents=True, exist_ok=True)
    images: list[str] = []
    for view in [value for value in args.views.split(",") if value]:
        direction = VIEW_DIRECTIONS.get(view)
        if direction is None:
            raise RuntimeError(f"Unknown view: {view}")
        camera.location = target + direction.normalized() * distance
        look_at(camera, target)
        output = (args.output / f"{view}.png").resolve()
        bpy.context.scene.render.filepath = str(output)
        bpy.ops.render.render(write_still=True)
        if not output.is_file():
            raise RuntimeError(f"Blender did not produce {output}")
        images.append(str(output))
    return images


def material_diagnostics(objects: list[bpy.types.Object]) -> dict[str, object]:
    assignments = {
        obj.name: [
            slot.material.name if slot.material is not None else None
            for slot in obj.material_slots
        ]
        for obj in objects
    }
    nodes: dict[str, list[dict[str, object]]] = {}
    for material in bpy.data.materials:
        if material.name == "Studio Floor" or not material.use_nodes or material.node_tree is None:
            continue
        entries: list[dict[str, object]] = []
        for node in material.node_tree.nodes:
            entry: dict[str, object] = {
                "name": node.name,
                "type": node.bl_idname,
            }
            if node.bl_idname == "ShaderNodeGroup":
                inputs: dict[str, object] = {}
                for socket in node.inputs:
                    value = getattr(socket, "default_value", None)
                    if value is None:
                        continue
                    try:
                        value = list(value)
                    except TypeError:
                        value = float(value) if isinstance(value, (int, float)) else str(value)
                    inputs[socket.name] = value
                entry["inputs"] = inputs
            image = getattr(node, "image", None)
            if image is not None:
                entry["image"] = image.filepath
            entries.append(entry)
        nodes[material.name] = {
            "entries": entries,
            "links": [
                {
                    "from": f"{link.from_node.name}.{link.from_socket.name}",
                    "to": f"{link.to_node.name}.{link.to_socket.name}",
                }
                for link in material.node_tree.links
            ],
        }
    return {
        "assignments": assignments,
        "nodes": nodes,
    }


def image_diagnostics() -> list[dict[str, object]]:
    return [
        {
            "name": image.name,
            "filepath": image.filepath,
            "size": list(image.size),
            "has_data": image.has_data,
            "source": image.source,
        }
        for image in bpy.data.images
    ]


def render_job(args: argparse.Namespace) -> dict[str, object]:
    cache_before = MATERIAL_CACHE_STATS.copy()
    clear_scene()
    if args.native_pbr:
        import_native_pbr(args.glb)
        mask_repair = {"repaired": [], "reason": "native PBR material"}
    else:
        import_cp77(args.glb, args.appearance)
        mask_repair = repair_multilayer_masks(args.glb, args.appearance, args.output)
    objects = mesh_objects()
    minimum, maximum = world_bounds(objects)
    camera, cycles_device = setup_scene(args, minimum, maximum)
    images = render_views(args, camera, minimum, maximum)
    report = {
        "schema_version": 1,
        "glb": str(args.glb.resolve()),
        "appearance": args.appearance,
        "native_pbr": args.native_pbr,
        "engine": args.engine,
        "resolution": args.resolution,
        "samples": args.samples,
        "cycles_device": cycles_device,
        "images": images,
        "materials": sorted(material.name for material in bpy.data.materials),
        "objects": sorted(obj.name for obj in objects),
        "multilayer_mask_repair": mask_repair,
        "material_diagnostics": material_diagnostics(objects),
        "image_diagnostics": image_diagnostics(),
        "material_cache": {
            "hits": MATERIAL_CACHE_STATS["hits"] - cache_before["hits"],
            "misses": MATERIAL_CACHE_STATS["misses"] - cache_before["misses"],
            "cached_materials": len(MATERIAL_CACHE),
            "total_hits": MATERIAL_CACHE_STATS["hits"],
            "total_misses": MATERIAL_CACHE_STATS["misses"],
        },
        "bounds": {
            "minimum": list(minimum),
            "maximum": list(maximum),
        },
    }
    (args.output / "render-report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print("GHOSTLINE_ITEM_RENDER_OK")
    return report


def main() -> None:
    args = parse_args()
    if args.jobs is None:
        if not args.native_pbr:
            enable_material_cache()
        render_job(args)
        return
    payload = json.loads(args.jobs.read_text(encoding="utf-8"))
    jobs = payload.get("jobs", payload) if isinstance(payload, dict) else payload
    if any(not bool(job.get("native_pbr", args.native_pbr)) for job in jobs):
        enable_material_cache()
    failures: list[dict[str, str]] = []
    completed: list[str] = []
    for position, job in enumerate(jobs, start=1):
        print(
            f"GHOSTLINE_BATCH [{position}/{len(jobs)}] "
            f"{job['appearance']} {job['glb']}",
            flush=True,
        )
        batch_args = argparse.Namespace(
            glb=Path(job["glb"]),
            appearance=job["appearance"],
            output=Path(job["output"]),
            resolution=args.resolution,
            samples=args.samples,
            engine=args.engine,
            views=args.views,
            native_pbr=bool(job.get("native_pbr", args.native_pbr)),
        )
        try:
            render_job(batch_args)
            completed.append(str(batch_args.output.resolve()))
            print(
                f"GHOSTLINE_BATCH_DONE [{position}/{len(jobs)}] "
                f"{job['appearance']} {job['glb']}",
                flush=True,
            )
        except Exception as exc:
            traceback.print_exc()
            print(
                f"GHOSTLINE_BATCH_FAILED [{position}/{len(jobs)}] "
                f"{job['appearance']} {exc}",
                flush=True,
            )
            failures.append(
                {
                    "glb": str(batch_args.glb.resolve()),
                    "appearance": batch_args.appearance,
                    "output": str(batch_args.output.resolve()),
                    "error": str(exc),
                }
            )
    report_path = args.batch_report or args.jobs.with_suffix(".report.json")
    report_path.write_text(
        json.dumps({"completed": completed, "failures": failures}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"GHOSTLINE_BATCH_OK completed={len(completed)} failures={len(failures)}",
        flush=True,
    )
    if failures:
        raise RuntimeError(f"{len(failures)} batch render jobs failed")


if __name__ == "__main__":
    main()
