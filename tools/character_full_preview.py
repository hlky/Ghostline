#!/usr/bin/env python3
"""Build an offline whole-character GLB preview from a generated appearance."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

import character_asset_index
import character_builder


ROOT = Path(__file__).resolve().parents[1]
MAX_FULL_PREVIEW_MODELS = 24
HEAD_CORE_COMPONENTS = {"h0_head", "he_eyes", "ht_teeth", "heb_eyebrows"}
SKIP_NAME_PARTS = ("shadow", "nail")
MESH_COMPONENT_TYPES = {
    "entSkinnedMeshComponent",
    "entGarmentSkinnedMeshComponent",
}
ROLE_COLORS = {
    "body": "#d6a08a",
    "hair": "#11151c",
    "clothing": "#27323b",
    "accessory": "#7d8791",
}


class CharacterFullPreviewError(RuntimeError):
    """Raised when a whole-character preview cannot be prepared."""


def mesh_path(component: dict[str, Any]) -> str:
    mesh = component.get("mesh")
    depot = mesh.get("DepotPath") if isinstance(mesh, dict) else None
    value = character_builder.typed_value(depot)
    return str(value) if isinstance(value, str) else ""


def mesh_role(name: str, depot_path: str) -> str:
    folded = f"{name} {depot_path}".casefold()
    if "hair" in folded or name.casefold().startswith("hh_"):
        return "hair"
    if any(token in folded for token in ("shirt", "pants", "boot", "shoe", "jacket")):
        return "clothing"
    if "\\body\\" in depot_path.casefold():
        return "body"
    return "accessory"


def visible_mesh_layers(
    app_document: dict[str, Any], namespace: str
) -> tuple[list[dict[str, str]], list[str]]:
    """Return a bounded silhouette-oriented mesh set from the selected appearance."""
    appearances = character_builder.appearance_data(app_document)
    if len(appearances) != 1:
        raise CharacterFullPreviewError(
            f"Whole-character preview requires one generated appearance, found {len(appearances)}"
        )
    component_sets = character_builder.component_sets(appearances[0])
    if not component_sets:
        raise CharacterFullPreviewError("Generated appearance has no component list")

    namespace_prefix = namespace.casefold().rstrip("\\") + "\\"
    layers: list[dict[str, str]] = []
    warnings: list[str] = []
    seen_paths: set[str] = set()
    included_feet = False
    omitted_head_layers = 0

    for component in component_sets[0]:
        if component.get("$type") not in MESH_COMPONENT_TYPES:
            continue
        if component.get("isEnabled", 1) == 0:
            continue
        name = character_builder.component_name(component)
        path = mesh_path(component)
        folded_name = name.casefold()
        folded_path = path.casefold()
        if not path or path == "0" or not folded_path.endswith(".mesh"):
            continue
        if name in HEAD_CORE_COMPONENTS:
            continue
        if any(part in folded_name or part in folded_path for part in SKIP_NAME_PARTS):
            continue
        if folded_path.startswith(namespace_prefix + "head\\"):
            omitted_head_layers += 1
            continue
        if folded_path.startswith(namespace_prefix + "body\\"):
            if "feet" in folded_name:
                if included_feet:
                    continue
                included_feet = True
            if not any(token in folded_name for token in ("body", "arm", "feet")):
                continue
        elif not folded_path.startswith(("base\\", "ep1\\")):
            warnings.append(f"Skipped unresolved preview mesh {path}")
            continue
        if folded_path in seen_paths:
            continue
        seen_paths.add(folded_path)
        role = mesh_role(name, path)
        layers.append(
            {
                "component": name,
                "depot_path": path,
                "role": role,
                "color": ROLE_COLORS[role],
            }
        )

    if omitted_head_layers:
        warnings.append(
            f"Neutral preview omits {omitted_head_layers} makeup/piercing head layer(s)"
        )
    return layers, warnings


def stat_identity(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path.resolve()),
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
    }


def preview_cache_key(
    layers: list[dict[str, str]],
    generated_archive_root: Path,
    wolvenkit: Path,
    game_path: Path,
) -> str:
    local_files = []
    for layer in layers:
        path = layer["depot_path"]
        if path.casefold().startswith(("base\\", "ep1\\")):
            continue
        source = generated_archive_root.joinpath(*path.split("\\"))
        if not source.is_file():
            raise CharacterFullPreviewError(f"Generated preview mesh is missing: {source}")
        local_files.append(stat_identity(source))
    payload = {
        "schema": 1,
        "layers": layers,
        "local_files": local_files,
        "wolvenkit": stat_identity(wolvenkit),
        "game_archive_root": stat_identity(game_path / "archive" / "pc"),
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def expected_glb(output_dir: Path, depot_path: str) -> Path:
    return output_dir.joinpath("raw", *depot_path.split("\\")).with_suffix(".glb")


def run_checked(command: list[str], label: str, timeout: int = 240) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=timeout,
    )
    if completed.returncode != 0:
        raise CharacterFullPreviewError(
            f"{label} failed ({completed.returncode}): {' '.join(command)}\n"
            f"{completed.stdout}\n{completed.stderr}"
        )
    return completed


def export_layers(
    layers: list[dict[str, str]],
    generated_archive_root: Path,
    output_dir: Path,
    wolvenkit: Path,
    game_path: Path,
) -> dict[str, Any]:
    if not layers:
        raise CharacterFullPreviewError("Generated appearance has no previewable body or outfit meshes")
    if not wolvenkit.is_file():
        raise CharacterFullPreviewError(f"WolvenKit was not found: {wolvenkit}")
    game_archive_root = game_path / "archive" / "pc"
    if not game_archive_root.is_dir():
        raise CharacterFullPreviewError(f"Cyberpunk archive directory was not found: {game_archive_root}")

    manifest_path = output_dir / "layers-manifest.json"
    cache_key = preview_cache_key(layers, generated_archive_root, wolvenkit, game_path)
    expected = [expected_glb(output_dir, layer["depot_path"]) for layer in layers]
    try:
        previous = character_asset_index.read_json(manifest_path) if manifest_path.is_file() else {}
    except character_asset_index.CharacterAssetIndexError:
        previous = {}
    reused = previous.get("cache_key") == cache_key and all(path.is_file() for path in expected)

    pack_command: list[str] = []
    export_command: list[str] = []
    if not reused:
        output_dir.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            dir=output_dir.parent, prefix=f".{output_dir.name}.refresh."
        ) as directory:
            staging = Path(directory)
            packed = staging / "packed"
            raw = staging / "raw"
            cooked = staging / "cooked"
            packed.mkdir(parents=True)
            pack_command = [
                str(wolvenkit),
                "pack",
                str(generated_archive_root),
                "--outpath",
                str(packed),
                "--verbosity",
                "Minimal",
            ]
            run_checked(pack_command, "Temporary character archive pack")
            archive = packed / "archive.archive"
            if not archive.is_file():
                raise CharacterFullPreviewError("WolvenKit did not create the temporary character archive")

            depot_paths = [layer["depot_path"] for layer in layers]
            pattern = "^(?:" + "|".join(re.escape(path) for path in depot_paths) + ")$"
            archive_sources = [game_archive_root / "content"]
            ep1_archives = game_archive_root / "ep1"
            if ep1_archives.is_dir():
                archive_sources.append(ep1_archives)
            export_command = [
                str(wolvenkit),
                "extract-and-export",
                *(str(path) for path in archive_sources),
                str(archive),
                "-o",
                str(cooked),
                "-or",
                str(raw),
                "-r",
                pattern,
                "--gamepath",
                str(game_path),
                "--mesh-export-type",
                "MeshOnly",
                "--mesh-export-lod-filter",
                "--verbosity",
                "Minimal",
            ]
            completed = run_checked(export_command, "Whole-character mesh export")
            missing = [
                layer["depot_path"]
                for layer in layers
                if not expected_glb(staging, layer["depot_path"]).is_file()
            ]
            if missing:
                raise CharacterFullPreviewError(
                    "WolvenKit did not export preview GLBs for: "
                    + ", ".join(missing)
                    + f"\n{completed.stdout}\n{completed.stderr}"
                )
            for layer in layers:
                source = expected_glb(staging, layer["depot_path"])
                target = expected_glb(output_dir, layer["depot_path"])
                character_asset_index.replace_file(source, target)

    models = [
        {
            "id": character_asset_index.preview_cache_id(layer["depot_path"]),
            "file": expected_glb(output_dir, layer["depot_path"])
            .relative_to(output_dir)
            .as_posix(),
            "source_type": "mesh",
            **layer,
        }
        for layer in layers
    ]
    manifest = {
        "schema_version": 1,
        "cache_key": cache_key,
        "models": models,
    }
    character_asset_index.write_json(manifest_path, manifest)
    return {
        "models": models,
        "reused": reused,
        "pack_command": pack_command,
        "export_command": export_command,
    }


def relative_model_file(model_file: str, source_manifest: Path, output_dir: Path) -> str:
    source = (source_manifest.parent / Path(model_file.replace("/", os.sep))).resolve()
    return Path(os.path.relpath(source, output_dir.resolve())).as_posix()


def assemble_preview_manifest(
    head_manifest: dict[str, Any],
    head_manifest_path: Path,
    layer_result: dict[str, Any],
    output_dir: Path,
    warnings: list[str],
) -> dict[str, Any]:
    head_models = []
    for model in head_manifest.get("models", []):
        if not isinstance(model, dict) or not isinstance(model.get("file"), str):
            continue
        head_models.append(
            {
                **model,
                "file": relative_model_file(model["file"], head_manifest_path, output_dir),
                "role": "head",
            }
        )
    models = [*head_models, *layer_result["models"]]
    if len(models) > MAX_FULL_PREVIEW_MODELS:
        raise CharacterFullPreviewError(
            f"Whole-character preview has {len(models)} models; maximum is {MAX_FULL_PREVIEW_MODELS}"
        )
    return {
        "schema_version": 2,
        "preview_kind": "character",
        "models": models,
        "morph_mapping": head_manifest.get("morph_mapping", {}),
        "warnings": warnings,
    }


def prepare_full_preview(
    manifest: dict[str, Any],
    app_document: dict[str, Any],
    character_root: Path,
    head_manifest_path: Path,
    output_dir: Path,
    wolvenkit: Path,
    game_path: Path,
) -> dict[str, Any]:
    layers, warnings = visible_mesh_layers(app_document, str(manifest["namespace"]))
    layer_result = export_layers(
        layers,
        character_root / "source" / "archive",
        output_dir,
        wolvenkit,
        game_path,
    )
    head_manifest = character_asset_index.read_json(head_manifest_path)
    preview = assemble_preview_manifest(
        head_manifest,
        head_manifest_path,
        layer_result,
        output_dir,
        warnings,
    )
    preview_path = output_dir / "preview-manifest.json"
    character_asset_index.write_json(preview_path, preview)
    return {
        "ok": True,
        "manifest": str(preview_path.resolve()),
        "models": len(preview["models"]),
        "layers": layers,
        "warnings": warnings,
        "reused": layer_result["reused"],
        "pack_command": layer_result["pack_command"],
        "export_command": layer_result["export_command"],
    }
