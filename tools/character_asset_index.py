#!/usr/bin/env python3
"""Index current Cyberpunk character assets and prepare isolated mesh previews."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GAME = Path(r"H:\Cyberpunk 2077")
DEFAULT_WOLVENKIT = Path(r"H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe")
DEFAULT_OUTPUT = ROOT / "converted/character-index/assets.json"
DEFAULT_ARCHIVE_RELATIVE_PATHS = (
    Path("archive/pc/content/basegame_4_appearance.archive"),
    Path("archive/pc/ep1/ep1_2_gamedata.archive"),
)
DEFAULT_ASSET_REGEX = (
    r"^(?:base|ep1)\\characters\\(?:"
    r"garment\\player_equipment\\.*\.(?:mesh|ent)|"
    r"appearances\\player\\items\\.*\.app|"
    r"common\\hair\\.*\.(?:mesh|ent|app)|"
    r"head\\player_base_heads\\.*\.(?:mesh|morphtarget)|"
    r"common\\player_base_bodies\\.*\.(?:mesh|morphtarget)"
    r")$"
)
DEPOT_PATH_PATTERN = re.compile(r"^(?:base|ep1)\\.+\.[a-z0-9_-]+$", re.IGNORECASE)
FRAME_PATTERN = re.compile(
    r"(?:^|_)(pma|pwa|mba|wba|mab|wab|ma|wa|mb|wb)(?=__|_|\.|$)", re.IGNORECASE
)
FRAME_LABELS = {
    "pma": "player_male_average",
    "pwa": "player_female_average",
    "ma": "male_average",
    "wa": "female_average",
    "mba": "male_big_average",
    "wba": "female_big_average",
    "mab": "male_average_big",
    "wab": "female_average_big",
    "mb": "male_big",
    "wb": "female_big",
}
SUPPORTED_CLOTHING_SLOTS = {
    "torso": "inner_torso",
    "legs": "legs",
    "feet": "feet",
}


class CharacterAssetIndexError(RuntimeError):
    pass


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            stream.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
            temporary = Path(stream.name)
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def replace_file(source: Path, target: Path) -> None:
    """Replace one derived cache file only after its staged source is complete."""
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=target.parent,
            prefix=f".{target.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
        shutil.copyfile(source, temporary)
        temporary.replace(target)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CharacterAssetIndexError(f"Unable to read asset index {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CharacterAssetIndexError(f"Expected a JSON object in asset index {path}")
    return value


def preview_cache_id(depot_path: str) -> str:
    return hashlib.sha1(depot_path.replace("/", "\\").casefold().encode("utf-8")).hexdigest()[:16]


def stat_identity(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {"path": str(path.resolve()), "size": stat.st_size, "mtime_ns": stat.st_mtime_ns}


def mesh_preview_cache_key(depot_path: str, archive: Path, wolvenkit: Path, game_path: Path) -> str:
    game_executable = game_path / "bin/x64/Cyberpunk2077.exe"
    value = {
        "schema": 1,
        "depot_path": depot_path.casefold(),
        "archive": stat_identity(archive),
        "wolvenkit": stat_identity(wolvenkit),
        "game": stat_identity(game_executable) if game_executable.is_file() else str(game_path.resolve()),
        "exporter": {"mesh_export_type": "MeshOnly", "lod_filter": True},
    }
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def archive_id(path: Path, game_path: Path) -> str:
    try:
        return path.resolve().relative_to(game_path.resolve()).as_posix()
    except ValueError:
        return path.name


def parse_archive_listing(output: str) -> list[str]:
    paths: list[str] = []
    for raw in output.splitlines():
        value = raw.strip()
        if DEPOT_PATH_PATTERN.fullmatch(value) and value not in paths:
            paths.append(value)
    return paths


def list_archive_assets(wolvenkit: Path, archive: Path, pattern: str) -> list[str]:
    command = [
        str(wolvenkit),
        "archive",
        str(archive),
        "-l",
        "-r",
        pattern,
        "-v",
        "Minimal",
    ]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    paths = parse_archive_listing(completed.stdout)
    if completed.returncode != 0:
        raise CharacterAssetIndexError(
            f"Archive listing failed ({completed.returncode}): {' '.join(command)}\n"
            f"{completed.stdout}\n{completed.stderr}"
        )
    return paths


def asset_role(stem: str, extension: str) -> str:
    lower = stem.casefold()
    for marker, role in (
        ("shadow", "shadow"),
        ("cuff", "cuff"),
        ("decal", "decal"),
        ("cyberware", "cyberware_variant"),
        ("seamfix", "seamfix"),
        ("morph", "morph_source"),
        ("dangle", "dangle"),
        ("cap", "cap"),
    ):
        if marker in lower:
            return role
    return {"mesh": "primary_mesh", "ent": "component_entity", "app": "appearance"}.get(
        extension, extension
    )


def classify_asset(depot_path: str, source_archive: str) -> dict[str, Any]:
    normalized = depot_path.replace("/", "\\")
    parts = normalized.split("\\")
    lower_parts = [part.casefold() for part in parts]
    extension = Path(parts[-1]).suffix.lstrip(".").casefold()
    stem = Path(parts[-1]).stem
    category = "character_asset"
    slot: str | None = None
    family: str | None = parts[-2] if len(parts) > 1 else None

    if "player_equipment" in lower_parts:
        root_index = lower_parts.index("player_equipment")
        category = "clothing"
        slot = parts[root_index + 1] if len(parts) > root_index + 1 else None
        family = parts[root_index + 2] if len(parts) > root_index + 2 else family
    elif "appearances" in lower_parts and "items" in lower_parts:
        category = "clothing_appearance"
    elif "hair" in lower_parts:
        category = "hair"
    elif "player_base_heads" in lower_parts:
        category = "head"
    elif "player_base_bodies" in lower_parts:
        category = "body"

    path_frame_tokens: list[str] = []
    for match in FRAME_PATTERN.finditer(normalized):
        token = match.group(1).casefold()
        if token not in path_frame_tokens:
            path_frame_tokens.append(token)
    frame_tokens: list[str] = []
    for match in FRAME_PATTERN.finditer(stem):
        token = match.group(1).casefold()
        if token not in frame_tokens:
            frame_tokens.append(token)
    frames = [FRAME_LABELS[token] for token in frame_tokens]
    expansion = "phantom_liberty" if lower_parts[0] == "ep1" else "base_game"
    record: dict[str, Any] = {
        "depot_path": normalized,
        "source_archives": [source_archive],
        "expansion": expansion,
        "category": category,
        "resource_type": extension,
        "slot": slot,
        "family": family,
        "role": asset_role(stem, extension),
        "frame_tokens": frame_tokens,
        "frames": frames,
        "path_frame_tokens": path_frame_tokens,
        "previewable": extension == "mesh",
    }
    warnings: list[str] = []
    if category == "clothing" and extension == "mesh":
        warnings.append(
            "Player garment support is not automatically runtime-equivalent on NPC components; validate fit in game"
        )
    if extension == "mesh":
        warnings.append("Material-accurate preview requires on-demand material extraction")
    record["warnings"] = warnings
    return record


def summarize_assets(assets: Iterable[dict[str, Any]]) -> dict[str, Any]:
    rows = list(assets)
    return {
        "total": len(rows),
        "by_category": dict(sorted(Counter(row["category"] for row in rows).items())),
        "by_resource_type": dict(sorted(Counter(row["resource_type"] for row in rows).items())),
        "by_expansion": dict(sorted(Counter(row["expansion"] for row in rows).items())),
        "by_slot": dict(
            sorted(Counter(row["slot"] for row in rows if row.get("slot") is not None).items())
        ),
    }


def build_asset_index(
    game_path: Path,
    wolvenkit: Path,
    archives: list[Path] | None = None,
    pattern: str = DEFAULT_ASSET_REGEX,
) -> dict[str, Any]:
    if not game_path.is_dir():
        raise CharacterAssetIndexError(f"Cyberpunk game directory was not found: {game_path}")
    if not wolvenkit.is_file():
        raise CharacterAssetIndexError(f"WolvenKit was not found: {wolvenkit}")
    selected = archives or [game_path / relative for relative in DEFAULT_ARCHIVE_RELATIVE_PATHS]
    missing = [str(path) for path in selected if not path.is_file()]
    if missing:
        raise CharacterAssetIndexError(f"Character asset archives were not found: {', '.join(missing)}")

    records: dict[str, dict[str, Any]] = {}
    sources: list[dict[str, Any]] = []
    for archive in selected:
        source_id = archive_id(archive, game_path)
        paths = list_archive_assets(wolvenkit, archive, pattern)
        sources.append({"id": source_id, "path": str(archive.resolve()), "matched": len(paths)})
        for depot_path in paths:
            key = depot_path.casefold()
            if key in records:
                if source_id not in records[key]["source_archives"]:
                    records[key]["source_archives"].append(source_id)
                continue
            records[key] = classify_asset(depot_path, source_id)

    assets = sorted(records.values(), key=lambda row: row["depot_path"].casefold())
    return {
        "schema_version": 1,
        "game_path": str(game_path.resolve()),
        "wolvenkit": str(wolvenkit.resolve()),
        "filter": pattern,
        "sources": sources,
        "summary": summarize_assets(assets),
        "assets": assets,
    }


def search_assets(
    index: dict[str, Any],
    query: str = "",
    category: str = "",
    slot: str = "",
    frame: str = "",
    limit: int = 100,
) -> list[dict[str, Any]]:
    words = [word.casefold() for word in query.split() if word]
    matches: list[dict[str, Any]] = []
    for asset in index.get("assets", []):
        if category and asset.get("category") != category:
            continue
        if slot and asset.get("slot") != slot:
            continue
        if frame and frame not in asset.get("frame_tokens", []) and frame not in asset.get("frames", []):
            continue
        haystack = " ".join(
            str(asset.get(key, "")) for key in ("depot_path", "family", "slot", "role", "category")
        ).casefold()
        if any(word not in haystack for word in words):
            continue
        matches.append(asset)
        if len(matches) >= max(1, min(limit, 500)):
            break
    return matches


def find_asset(index: dict[str, Any], depot_path: str) -> dict[str, Any]:
    wanted = depot_path.replace("/", "\\").casefold()
    for asset in index.get("assets", []):
        if str(asset.get("depot_path", "")).casefold() == wanted:
            return asset
    raise CharacterAssetIndexError(f"Asset is not present in the current index: {depot_path}")


def selection_support(asset: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    slot = str(asset.get("slot") or "")
    manifest_category = SUPPORTED_CLOTHING_SLOTS.get(slot)
    if asset.get("category") != "clothing":
        reasons.append("only indexed player-equipment clothing is assignable")
    if asset.get("resource_type") != "mesh":
        reasons.append("only .mesh records are assignable")
    if asset.get("role") != "primary_mesh":
        reasons.append("cuff, shadow, and other companion meshes are not primary selections")
    if manifest_category is None:
        reasons.append("the first selector supports torso, legs, and feet")
    depot_stem = Path(str(asset.get("depot_path", "")).replace("\\", "/")).stem
    filename_frames = {
        match.group(1).casefold() for match in FRAME_PATTERN.finditer(depot_stem)
    }
    if "pma" not in filename_frames:
        reasons.append("Patch currently requires the pma player-male-average frame")
    return {
        "supported": not reasons,
        "manifest_category": manifest_category,
        "asset_slot": slot or None,
        "required_frame": "pma",
        "reasons": reasons,
    }


def mesh_appearance_metadata(document: dict[str, Any]) -> list[dict[str, Any]]:
    header = document.get("Header")
    data_root = document.get("Data")
    root = data_root.get("RootChunk") if isinstance(data_root, dict) else None
    if not isinstance(header, dict) or header.get("DataType") != "CR2W":
        raise CharacterAssetIndexError("Serialized mesh metadata has no CR2W header")
    if not isinstance(root, dict):
        raise CharacterAssetIndexError("Serialized mesh metadata has no RootChunk")
    appearances = root.get("appearances")
    if not isinstance(appearances, list):
        raise CharacterAssetIndexError("Serialized mesh metadata appearances must be a list")
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, wrapper in enumerate(appearances):
        if not isinstance(wrapper, dict):
            raise CharacterAssetIndexError(f"Mesh appearance {index} is not an object")
        data = wrapper.get("Data", wrapper) if isinstance(wrapper, dict) else None
        if not isinstance(data, dict) or data.get("$type") != "meshMeshAppearance":
            raise CharacterAssetIndexError(
                f"Mesh appearance {index} is not a meshMeshAppearance"
            )
        raw_name = data.get("name")
        name = raw_name.get("$value") if isinstance(raw_name, dict) else raw_name
        if not isinstance(name, str) or not name or name in seen:
            continue
        chunk_materials = data.get("chunkMaterials")
        if not isinstance(chunk_materials, list):
            raise CharacterAssetIndexError(
                f"Mesh appearance {name!r} chunkMaterials must be a list"
            )
        materials: list[str] = []
        for raw_material in chunk_materials:
            material = (
                raw_material.get("$value") if isinstance(raw_material, dict) else raw_material
            )
            if isinstance(material, str) and material:
                materials.append(material)
        rows.append({"name": name, "materials": materials})
        seen.add(name)
    return rows


def canonical_indexed_override(
    asset: dict[str, Any], mesh_appearance: str, appearances: Iterable[str]
) -> dict[str, Any]:
    support = selection_support(asset)
    if not support["supported"]:
        raise CharacterAssetIndexError("Asset cannot be assigned: " + "; ".join(support["reasons"]))
    available = list(appearances)
    if mesh_appearance not in available:
        raise CharacterAssetIndexError(
            f"Mesh appearance {mesh_appearance!r} is not advertised by {asset.get('depot_path')}"
        )
    return {
        "manifest_category": support["manifest_category"],
        "override": {
            "depot_path": str(asset["depot_path"]),
            "mesh_appearance": mesh_appearance,
        },
    }


def source_archive_path(index: dict[str, Any], asset: dict[str, Any]) -> Path:
    source_ids = asset.get("source_archives", [])
    for source in reversed(index.get("sources", [])):
        if source.get("id") in source_ids:
            path = Path(str(source.get("path", "")))
            if path.is_file():
                return path
    raise CharacterAssetIndexError(f"No installed source archive resolves {asset.get('depot_path')}")


def serialize_mesh_metadata(
    cooked_mesh: Path, metadata_root: Path, wolvenkit: Path
) -> tuple[list[str], Path, list[dict[str, Any]]]:
    metadata_root.mkdir(parents=True, exist_ok=True)
    expected_metadata = metadata_root / f"{cooked_mesh.name}.json"
    command = [
        str(wolvenkit),
        "convert",
        "serialize",
        str(cooked_mesh),
        "-o",
        str(metadata_root),
        "-v",
        "Minimal",
    ]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if completed.returncode != 0 or not expected_metadata.is_file():
        raise CharacterAssetIndexError(
            f"WolvenKit could not read mesh appearances ({completed.returncode}): "
            f"{' '.join(command)}\n{completed.stdout}\n{completed.stderr}"
        )
    rows = mesh_appearance_metadata(read_json(expected_metadata))
    return command, expected_metadata, rows


def prepare_mesh_preview(
    index: dict[str, Any],
    depot_path: str,
    output_dir: Path,
    wolvenkit: Path = DEFAULT_WOLVENKIT,
    game_path: Path = DEFAULT_GAME,
) -> dict[str, Any]:
    asset = find_asset(index, depot_path)
    if asset.get("resource_type") != "mesh":
        raise CharacterAssetIndexError("Only .mesh assets can be previewed")
    if not wolvenkit.is_file():
        raise CharacterAssetIndexError(f"WolvenKit was not found: {wolvenkit}")
    if not game_path.is_dir():
        raise CharacterAssetIndexError(f"Cyberpunk game directory was not found: {game_path}")
    archive = source_archive_path(index, asset)
    normalized = str(asset["depot_path"])
    relative_mesh = Path(*normalized.split("\\"))
    raw_root = output_dir / "raw"
    cooked_root = output_dir / "dependencies"
    expected_glb = (raw_root / relative_mesh).with_suffix(".glb")
    expected_cooked = cooked_root / relative_mesh
    metadata_root = output_dir / "metadata"
    expected_metadata = metadata_root / f"{relative_mesh.name}.json"
    manifest_path = output_dir / "preview-manifest.json"
    cache_key = mesh_preview_cache_key(normalized, archive, wolvenkit, game_path)
    try:
        old_manifest = read_json(manifest_path) if manifest_path.is_file() else {}
    except CharacterAssetIndexError:
        old_manifest = {}
    reused = (
        expected_glb.is_file()
        and expected_cooked.is_file()
        and old_manifest.get("cache_key") == cache_key
    )
    command: list[str] = []
    metadata_command: list[str] = []
    metadata_reused = (
        reused and expected_metadata.is_file() and old_manifest.get("cache_key") == cache_key
    )
    appearance_rows: list[dict[str, Any]]
    if not reused:
        output_dir.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            dir=output_dir.parent, prefix=f".{output_dir.name}.refresh."
        ) as staging_directory:
            staging_root = Path(staging_directory)
            staging_raw = staging_root / "raw"
            staging_cooked = staging_root / "dependencies"
            staging_glb = (staging_raw / relative_mesh).with_suffix(".glb")
            staging_cooked_mesh = staging_cooked / relative_mesh
            command = [
                str(wolvenkit),
                "extract-and-export",
                str(archive),
                "-o",
                str(staging_cooked),
                "-or",
                str(staging_raw),
                "-r",
                f"^{re.escape(normalized)}$",
                "--gamepath",
                str(game_path),
                "--mesh-export-type",
                "MeshOnly",
                "--mesh-export-lod-filter",
                "-v",
                "Minimal",
            ]
            completed = subprocess.run(
                command, cwd=ROOT, text=True, capture_output=True, check=False
            )
            if (
                completed.returncode != 0
                or not staging_glb.is_file()
                or not staging_cooked_mesh.is_file()
            ):
                raise CharacterAssetIndexError(
                    f"WolvenKit did not produce a fresh preview ({completed.returncode}): "
                    f"{' '.join(command)}\n{completed.stdout}\n{completed.stderr}"
                )
            metadata_command, staging_metadata, appearance_rows = serialize_mesh_metadata(
                staging_cooked_mesh, staging_root / "metadata", wolvenkit
            )
            replace_file(staging_glb, expected_glb)
            replace_file(staging_cooked_mesh, expected_cooked)
            replace_file(staging_metadata, expected_metadata)
    elif not metadata_reused:
        output_dir.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            dir=output_dir.parent, prefix=f".{output_dir.name}.metadata."
        ) as staging_directory:
            metadata_command, staging_metadata, appearance_rows = serialize_mesh_metadata(
                expected_cooked, Path(staging_directory), wolvenkit
            )
            replace_file(staging_metadata, expected_metadata)
    else:
        if not expected_cooked.is_file():
            raise CharacterAssetIndexError(
                f"Cached preview has no cooked mesh for metadata: {expected_cooked}"
            )
        appearance_rows = mesh_appearance_metadata(read_json(expected_metadata))
    mesh_appearances = [row["name"] for row in appearance_rows]
    support = selection_support(asset)
    warnings = list(asset.get("warnings", []))
    if not mesh_appearances:
        warnings.append("The mesh did not advertise any selectable appearances")
    if support["supported"]:
        warnings.append(
            "Assignment replaces only the slot's primary mesh; its curated cuff/shadow companion remains"
        )

    manifest = {
        "schema_version": 2,
        "preview_kind": "asset",
        "source": normalized,
        "cache_key": cache_key,
        "models": [
            {
                "id": preview_cache_id(normalized),
                "file": expected_glb.relative_to(output_dir).as_posix(),
                "source_type": "mesh",
                "color": "#77cfc4",
            }
        ],
        "morph_mapping": {},
        "mesh_appearances": mesh_appearances,
        "appearance_materials": appearance_rows,
        "assignment": support,
        "warnings": warnings,
    }
    write_json(manifest_path, manifest)
    return {
        "ok": True,
        "source": normalized,
        "manifest": str(manifest_path.resolve()),
        "model": str(expected_glb.resolve()),
        "reused": reused,
        "metadata_reused": metadata_reused,
        "command": command,
        "metadata_command": metadata_command,
        "asset": asset,
        "mesh_appearances": mesh_appearances,
        "appearance_materials": appearance_rows,
        "assignment": support,
        "warnings": manifest["warnings"],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gamepath", type=Path, default=DEFAULT_GAME)
    parser.add_argument("--wolvenkit", type=Path, default=DEFAULT_WOLVENKIT)
    parser.add_argument("--archive", type=Path, action="append", default=[])
    parser.add_argument("--regex", default=DEFAULT_ASSET_REGEX)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        index = build_asset_index(args.gamepath, args.wolvenkit, args.archive or None, args.regex)
        write_json(args.out, index)
        print(json.dumps({"ok": True, "output": str(args.out.resolve()), **index["summary"]}, indent=2))
        return 0
    except CharacterAssetIndexError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
