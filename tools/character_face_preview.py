"""Material-aware live face previews using the selected RED mesh appearances."""

from __future__ import annotations

import copy
import os
import re
from pathlib import Path
from typing import Any

import character_builder as builder
import character_cache as cache
import character_full_preview as full


def face_layers(manifest: dict, app: dict) -> list[dict]:
    """Resolve enabled head components, including their exact appearance and masks."""
    prefix = manifest["namespace"].casefold() + "\\head\\"
    result = []
    for component in builder.component_sets(builder.appearance_data(app)[0])[0]:
        path = full.mesh_path(component)
        name = builder.component_name(component)
        hair = name == "hh_hair" and path.casefold().startswith(("base\\", "ep1\\"))
        if component.get("isEnabled", 1) == 0 or not (path.casefold().startswith(prefix) or hair):
            continue
        result.append({
            "component": name, "depot_path": path, "role": "hair" if hair else "head",
            "mesh_appearance": builder.typed_value(component.get("meshAppearance")),
            "chunk_mask": str(component.get("chunkMask", "18446744073709551615")),
        })
    return result


def selected_materials(document: dict, appearance: str) -> list[dict]:
    appearances = document.get("Appearances", {})
    names = appearances.get(appearance)
    if names is None:
        # WolvenKit appends an appearance ordinal to the original CName.
        matches = [v for k, v in appearances.items()
                   if k.startswith(appearance) and k[len(appearance):].isdigit()]
        if len(matches) != 1:
            raise builder.CharacterBuildError(f"Cannot resolve preview appearance {appearance!r}")
        names = matches[0]
    materials = {entry["Name"]: entry for entry in document["Materials"]}
    try:
        return [materials[name] for name in names]
    except KeyError as exc:
        raise builder.CharacterBuildError(f"Missing exported material {exc}") from exc


def prepare_face_preview(manifest_path: Path, output: Path,
                         wolvenkit: Path, game: Path) -> dict[str, Any]:
    manifest = builder.load_manifest(manifest_path)
    manifest_root = output.parent
    builder.generate(manifest_path, manifest_root)
    app = builder.read_json(builder.output_path(manifest_root, manifest["outputs"]["appearance_raw"]))
    layers = face_layers(manifest, app)
    source_prefix = manifest["outputs"]["entity_raw"].replace("\\", "/").split("source/raw/", 1)[0]
    archive_root = manifest_root / source_prefix / "source/archive"
    assets = output / "materials"
    key = cache.fingerprint({
        "version": 1, "layers": layers,
        "sources": [builder.stat_identity(archive_root.joinpath(*v["depot_path"].split("\\")))
                    for v in layers if v["role"] != "hair"],
        "wolvenkit": builder.stat_identity(wolvenkit),
        "game": cache.archive_identities(game),
    })
    cache_path = assets / "cache.json"
    previous = builder.read_json(cache_path) if cache_path.is_file() else {}
    files = [Path(v) for v in previous.get("files", [])]
    reused = bool(files) and cache.cache_matches(cache_path, key, [assets / v for v in files])
    if not reused:
        files = []

        def export(staging: Path) -> None:
            packed = staging / "packed"
            packed.mkdir()
            full.run_checked([str(wolvenkit), "pack", str(archive_root), "-o", str(packed), "-v", "Minimal"], "Face archive pack")
            pattern = "^(?:" + "|".join(re.escape(v["depot_path"]) for v in layers) + ")$"
            full.run_checked([
                str(wolvenkit), "extract-and-export", str(game / "archive/pc/content"),
                *([str(game / "archive/pc/ep1")] if (game / "archive/pc/ep1").is_dir() else []),
                str(packed / "archive.archive"),
                "-o", str(staging / "cooked"), "-or", str(staging / "raw"),
                "--gamepath", str(game), "-r", pattern, "--mesh-export-type", "WithMaterials",
                "--mesh-export-material-repo", str(staging / "textures"),
                "--mesh-export-lod-filter", "--uext", "png", "-v", "Minimal",
            ], "Face material export", timeout=600)
            for layer in layers:
                glb = full.expected_glb(staging, layer["depot_path"])
                builder.glb_target_names(glb)
                selected_materials(builder.read_json(glb.with_suffix(".Material.json")), layer["mesh_appearance"])
            files.extend(p.relative_to(staging) for folder in ("raw", "textures")
                         for p in sorted((staging / folder).rglob("*")) if p.is_file())
            builder.write_json(staging / "cache.json", {"cache_key": key, "files": [v.as_posix() for v in files]})
            files.append(Path("cache.json"))

        cache.refresh_export(assets, files, export)

    # Morph geometry remains live; material assignments come from its matching mesh.
    morph_manifest = copy.deepcopy(manifest)
    morph_root = builder.repo_path(manifest["head"]["morphtarget_source"])
    morph_by_mesh = {builder.mesh_name_for_morphtarget(p.name): p.name for p in morph_root.glob("*.morphtarget")}
    morph_manifest["head"]["morphtargets"] = list(dict.fromkeys(
        morph_by_mesh[Path(v["depot_path"].replace("\\", "/")).name]
        for v in layers if Path(v["depot_path"].replace("\\", "/")).name in morph_by_mesh
    ))
    temporary = output / "face-morph-input.json"
    builder.write_json(temporary, {k: v for k, v in morph_manifest.items() if not k.startswith("_")})
    builder.prepare_head_preview(temporary, output / "morphs", wolvenkit, game, True)
    preview = builder.read_json(output / "morphs/preview-manifest.json")
    morph_models = {builder.mesh_name_for_morphtarget(v["id"] + ".morphtarget"): v for v in preview["models"]}
    models = []
    for layer in layers:
        glb = full.expected_glb(assets, layer["depot_path"])
        name = Path(layer["depot_path"].replace("\\", "/")).name
        model = copy.deepcopy(morph_models.get(name, {}))
        geometry = output / "morphs" / model["file"] if model else glb
        model.update(layer)
        model["file"] = Path(os.path.relpath(geometry, output)).as_posix()
        model["materials"] = selected_materials(builder.read_json(glb.with_suffix(".Material.json")), layer["mesh_appearance"])
        for material in model["materials"]:
            for param, value in list(material["Data"].items()):
                if isinstance(value, str) and value.endswith(".xbm"):
                    texture = assets / "textures" / Path(value.replace("\\", "/")).with_suffix(".png")
                    if texture.is_file():
                        material["Data"][param] = Path(os.path.relpath(texture, output)).as_posix()
                    else:
                        material["Data"].pop(param)
        models.append(model)
    preview.update(models=models, preview_kind="face", material_quality="RED textures / PBR approximation")
    builder.write_json(output / "preview-manifest.json", preview)
    return {"ok": True, "models": len(models), "reused": reused,
            "manifest": str(output / "preview-manifest.json")}
