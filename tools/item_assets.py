"""Native mesh and material export for item previews."""

from __future__ import annotations

from toolchain import resolve_tool
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Iterable

from item_common import (
    ItemDatabaseError,
    ROOT,
    file_identity,
    read_json,
    sha1_text,
    write_json,
)
from item_catalog import (
    asset_sources,
)


def source_archive_for_mesh(index: dict[str, Any], depot_path: str) -> Path:
    sources = asset_sources(index)
    normalized = depot_path.replace("/", "\\").casefold()
    for asset in index.get("assets", []):
        if str(asset.get("depot_path", "")).casefold() != normalized:
            continue
        for source_id in asset.get("source_archives", []):
            archive = sources.get(str(source_id))
            if archive and archive.is_file():
                return archive
    raise ItemDatabaseError(f"Mesh is absent from the installed asset index: {depot_path}")

def material_export_fingerprint(
    mesh: str,
    appearance: str,
    archive: Path,
    ghostline_red: Path,
    red_schema: Path,
    game: Path,
) -> str:
    executable = game / "bin/x64/Cyberpunk2077.exe"
    payload = {
        "mesh": mesh.casefold(),
        "appearance": appearance,
        "archive": file_identity(archive),
        "ghostline_red": file_identity(ghostline_red),
        "red_schema": file_identity(red_schema),
        "game": file_identity(executable),
        "mode": "native-pbr-selected-appearance-v3",
    }
    return sha1_text(json.dumps(payload, sort_keys=True))

def prepare_material_export(
    index: dict[str, Any],
    depot_path: str,
    appearance: str,
    cache_root: Path,
    ghostline_red: Path,
    red_schema: Path,
    game: Path,
    *, kraken: Path | None = None,
) -> dict[str, Any]:
    archive = source_archive_for_mesh(index, depot_path)
    fingerprint = material_export_fingerprint(
        depot_path,
        appearance,
        archive,
        ghostline_red,
        red_schema,
        game,
    )
    final = cache_root / fingerprint
    relative = Path(*depot_path.replace("/", "\\").split("\\"))
    glb = (final / "raw" / relative).with_suffix(".glb")
    material_json = glb.with_name(f"{glb.stem}.Material.json")
    manifest = final / "manifest.json"
    if glb.is_file() and material_json.is_file() and manifest.is_file():
        return read_json(manifest)
    cache_root.mkdir(parents=True, exist_ok=True)
    shared_materials = cache_root.parent / "material-repo"
    shared_materials.mkdir(parents=True, exist_ok=True)
    kraken = resolve_tool("kraken", kraken)
    with tempfile.TemporaryDirectory(dir=cache_root, prefix=".material-export.") as directory:
        staging = Path(directory)
        cooked = staging / "cooked"
        raw = staging / "raw"
        cooked_mesh = cooked / relative
        staged_glb = (raw / relative).with_suffix(".glb")
        extract_command = [
            str(ghostline_red),
            "--kraken",
            str(kraken),
            "extract",
            str(archive),
            "--output",
            str(cooked),
            "--path",
            depot_path,
        ]
        extracted = subprocess.run(extract_command, cwd=ROOT, text=True, capture_output=True)
        if extracted.returncode != 0 or not cooked_mesh.is_file():
            raise ItemDatabaseError(
                f"ghostline-red mesh extraction failed for {depot_path}:\n"
                f"{extracted.stdout}\n{extracted.stderr}"
            )
        staged_glb.parent.mkdir(parents=True, exist_ok=True)
        export_command = [
            str(ghostline_red),
            "--kraken",
            str(kraken),
            "mesh-export",
            str(cooked_mesh),
            "--schema",
            str(red_schema),
            "--output",
            str(staged_glb),
            "--archives-root",
            str(game / "archive/pc"),
            "--material-repo",
            str(shared_materials),
            "--appearance",
            appearance,
            "--pbr",
            "--pbr-size",
            "512",
        ]
        completed = subprocess.run(export_command, cwd=ROOT, text=True, capture_output=True)
        staged_material = staged_glb.with_name(f"{staged_glb.stem}.Material.json")
        if completed.returncode != 0 or not staged_glb.is_file() or not staged_material.is_file():
            raise ItemDatabaseError(
                f"ghostline-red material export failed for {depot_path} ({appearance}):\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
        final.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(staging, final)
    result = {
        "schema_version": 1,
        "fingerprint": fingerprint,
        "source": depot_path,
        "appearance": appearance,
        "archive": str(archive.resolve()),
        "glb": str(glb.resolve()),
        "material_json": str(material_json.resolve()),
        "material_repo": str(shared_materials.resolve()),
        "exporter": "ghostline-red",
        "native_pbr": True,
    }
    write_json(manifest, result)
    return result

def prepare_material_exports_bulk(
    index: dict[str, Any],
    requests: Iterable[tuple[str, str]],
    cache_root: Path,
    ghostline_red: Path,
    red_schema: Path,
    game: Path,
    export_workers: int,
    *, kraken: Path | None = None,
) -> tuple[dict[tuple[str, str], dict[str, Any]], dict[tuple[str, str], str]]:
    cache_root.mkdir(parents=True, exist_ok=True)
    shared_materials = cache_root.parent / "material-repo"
    shared_materials.mkdir(parents=True, exist_ok=True)
    descriptors: dict[tuple[str, str], dict[str, Any]] = {}
    errors: dict[tuple[str, str], str] = {}
    jobs: list[dict[str, str]] = []
    for depot_path, appearance in dict.fromkeys(requests):
        archive = source_archive_for_mesh(index, depot_path)
        fingerprint = material_export_fingerprint(
            depot_path,
            appearance,
            archive,
            ghostline_red,
            red_schema,
            game,
        )
        final = cache_root / fingerprint
        relative = Path(*depot_path.replace("/", "\\").split("\\"))
        glb = (final / "raw" / relative).with_suffix(".glb")
        material_json = glb.with_name(f"{glb.stem}.Material.json")
        manifest = final / "manifest.json"
        failure_manifest = final / "failure.json"
        result = {
            "schema_version": 1,
            "fingerprint": fingerprint,
            "source": depot_path,
            "appearance": appearance,
            "archive": str(archive.resolve()),
            "glb": str(glb.resolve()),
            "material_json": str(material_json.resolve()),
            "material_repo": str(shared_materials.resolve()),
            "exporter": "ghostline-red-batch",
            "native_pbr": True,
        }
        key = (depot_path, appearance)
        descriptors[key] = {
            "result": result,
            "manifest": manifest,
            "failure_manifest": failure_manifest,
            "glb": glb,
            "material_json": material_json,
        }
        if glb.is_file() and material_json.is_file() and manifest.is_file():
            continue
        if failure_manifest.is_file():
            failure = read_json(failure_manifest)
            errors[key] = str(failure.get("error") or "cached material export failure")
            continue
        glb.parent.mkdir(parents=True, exist_ok=True)
        jobs.append(
            {
                "mesh": depot_path,
                "appearance": appearance,
                "output": str(glb.resolve()),
            }
        )

    if jobs:
        with tempfile.TemporaryDirectory(dir=cache_root, prefix=".bulk-material-export.") as directory:
            temporary = Path(directory)
            job_manifest = temporary / "jobs.json"
            report_path = temporary / "report.json"
            write_json(job_manifest, {"jobs": jobs})
            command = [
                str(ghostline_red),
                "--kraken",
                str(resolve_tool("kraken", kraken)),
                "mesh-export-batch",
                str(job_manifest),
                "--schema",
                str(red_schema),
                "--archives-root",
                str(game / "archive/pc"),
                "--material-repo",
                str(shared_materials),
                "--report",
                str(report_path),
                "--pbr",
                "--pbr-size",
                "512",
                "--threads",
                str(max(1, export_workers)),
            ]
            completed = subprocess.run(command, cwd=ROOT, text=True)
            outcomes = read_json(report_path) if report_path.is_file() else []
            outcome_map = {
                (str(outcome["mesh"]), str(outcome["appearance"])): outcome
                for outcome in outcomes
            }
            for job in jobs:
                key = (job["mesh"], job["appearance"])
                outcome = outcome_map.get(key)
                error = str(outcome.get("error") or "") if outcome else ""
                descriptor = descriptors[key]
                if (
                    not error
                    and descriptor["glb"].is_file()
                    and descriptor["material_json"].is_file()
                ):
                    write_json(descriptor["manifest"], descriptor["result"])
                else:
                    failure = error or (
                        f"bulk exporter exited {completed.returncode} without producing "
                        f"{descriptor['glb']}"
                    )
                    errors[key] = failure
                    if error:
                        write_json(
                            descriptor["failure_manifest"],
                            {
                                "schema_version": 1,
                                "source": job["mesh"],
                                "appearance": job["appearance"],
                                "error": failure,
                            },
                        )

    exports = {
        key: descriptor["result"]
        for key, descriptor in descriptors.items()
        if key not in errors
        and descriptor["glb"].is_file()
        and descriptor["material_json"].is_file()
        and descriptor["manifest"].is_file()
    }
    return exports, errors
