"""Braindance CR2W conversion, depot publication, and runtime evidence."""
from __future__ import annotations
import copy
import hashlib
import json
import shutil
import subprocess
import tempfile
from datetime import UTC, datetime
from pathlib import Path

from artifact_io import atomic_write_json
from toolchain import default_tool_path, resolve_tool
from typing import Any
from braindance_support.scene_types import (
    BraindancePipelineError,
)


ROOT = Path(__file__).resolve().parents[2]


WOLVENKIT_CLI = default_tool_path("wolvenkit")


RUNTIME_CASES = (
    "seek_forward",
    "rewind_backward",
    "switch_visual_layer",
    "switch_audio_layer",
    "switch_thermal_layer",
    "normal_exit_cleanup",
    "interrupted_cleanup",
    "replay_after_cleanup",
)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BraindancePipelineError(f"Cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise BraindancePipelineError(f"JSON root must be an object: {path}")
    return value


def write_json(path: Path, value: Any) -> None:
    atomic_write_json(path, value)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def find_wolvenkit(explicit: Path | None = None) -> Path:
    try:
        return resolve_tool("wolvenkit", explicit)
    except (OSError, ValueError) as exc:
        raise BraindancePipelineError(str(exc)) from exc


def deserialize_cr2w_json(
    json_path: Path,
    binary_output: Path,
    *,
    wolvenkit: Path,
) -> dict[str, Any]:
    serialized_name = json_path.name.casefold()
    if (
        not serialized_name.endswith(".json")
        or "." not in serialized_name[:-5]
    ):
        raise BraindancePipelineError(
            "CR2W JSON input must retain its resource extension before .json"
        )
    with tempfile.TemporaryDirectory(prefix="ghostline-bd-cr2w-") as directory:
        staging = Path(directory)
        command = [
            str(wolvenkit),
            "cr2w",
            "--deserialize",
            "--path",
            str(json_path.resolve()),
            "--outpath",
            str(staging),
        ]
        completed = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        failed_output = (
            "[ 0: Error" in completed.stdout
            or "Could not convert" in completed.stdout
            or "Invalid output directory" in completed.stdout
        )
        if completed.returncode != 0 or failed_output:
            raise BraindancePipelineError(
                f"WolvenKit failed ({completed.returncode}): "
                f"{completed.stdout.strip()}"
            )
        expected_name = json_path.name[:-5]
        matches = list(staging.rglob(expected_name))
        if len(matches) != 1:
            raise BraindancePipelineError(
                f"WolvenKit did not produce exactly one {expected_name}"
            )
        binary_output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(matches[0], binary_output)
    if binary_output.read_bytes()[:4] != b"CR2W":
        raise BraindancePipelineError(
            f"Deserialized output is not CR2W: {binary_output}"
        )
    return {
        "binary_output": str(binary_output.resolve()),
        "bytes": binary_output.stat().st_size,
        "sha256": file_sha256(binary_output),
    }


def _safe_depot_path(value: str) -> Path:
    normalized = value.replace("\\", "/")
    path = Path(normalized)
    if (
        path.is_absolute()
        or ".." in path.parts
        or not path.parts
        or path.parts[0] not in {"mod", "base"}
    ):
        raise BraindancePipelineError(f"Unsafe depot path: {value}")
    return path


def package_assets(
    mappings: list[tuple[Path, str]],
    *,
    depot_root: Path,
) -> dict[str, Any]:
    root = depot_root.resolve()
    entries: list[dict[str, Any]] = []
    seen: set[str] = set()
    for source, depot_path in mappings:
        if not source.is_file():
            raise BraindancePipelineError(f"Package source does not exist: {source}")
        relative = _safe_depot_path(depot_path)
        key = relative.as_posix().casefold()
        if key in seen:
            raise BraindancePipelineError(f"Duplicate package depot path: {depot_path}")
        seen.add(key)
        target = (root / relative).resolve()
        try:
            target.relative_to(root)
        except ValueError as exc:
            raise BraindancePipelineError(
                f"Package target escapes depot root: {depot_path}"
            ) from exc
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.resolve() != target:
            shutil.copy2(source, target)
        source_hash = file_sha256(source)
        target_hash = file_sha256(target)
        if source_hash != target_hash:
            raise BraindancePipelineError(
                f"Packaged file hash mismatch: {depot_path}"
            )
        entries.append(
            {
                "source": str(source.resolve()),
                "depot_path": relative.as_posix(),
                "target": str(target),
                "bytes": target.stat().st_size,
                "sha256": target_hash,
            }
        )
    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_package_manifest",
        "depot_root": str(root),
        "entries": entries,
    }


def init_runtime_evidence(
    *,
    name: str,
    package_manifest: dict[str, Any],
) -> dict[str, Any]:
    hashes = {
        entry["depot_path"]: entry["sha256"]
        for entry in package_manifest.get("entries", [])
    }
    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_runtime_evidence",
        "name": name,
        "package_hashes": hashes,
        "cases": {
            case: {"status": "pending", "notes": None, "recorded_at": None}
            for case in RUNTIME_CASES
        },
    }


def record_runtime_case(
    evidence: dict[str, Any],
    *,
    case: str,
    passed: bool,
    notes: str,
) -> dict[str, Any]:
    if case not in RUNTIME_CASES:
        raise BraindancePipelineError(f"Unknown runtime case: {case}")
    result = copy.deepcopy(evidence)
    cases = result.get("cases")
    if not isinstance(cases, dict) or case not in cases:
        raise BraindancePipelineError("Runtime evidence has an invalid case table")
    cases[case] = {
        "status": "passed" if passed else "failed",
        "notes": notes,
        "recorded_at": datetime.now(UTC).isoformat(),
    }
    return result


def verify_runtime_evidence(
    evidence: dict[str, Any],
    *,
    depot_root: Path,
) -> dict[str, Any]:
    errors: list[str] = []
    hashes = evidence.get("package_hashes")
    if not isinstance(hashes, dict) or not hashes:
        errors.append("Runtime evidence has no package hashes")
        hashes = {}
    for depot_path, expected_hash in hashes.items():
        target = depot_root / _safe_depot_path(depot_path)
        if not target.is_file():
            errors.append(f"Runtime package file is missing: {depot_path}")
        elif file_sha256(target) != expected_hash:
            errors.append(f"Runtime package hash changed: {depot_path}")
    cases = evidence.get("cases")
    if not isinstance(cases, dict):
        errors.append("Runtime evidence has no cases")
        cases = {}
    for case in RUNTIME_CASES:
        status = cases.get(case, {}).get("status")
        if status != "passed":
            errors.append(f"Runtime case is not passed: {case} ({status})")
    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_runtime_verification",
        "ok": not errors,
        "errors": errors,
        "package_hash_count": len(hashes),
        "passed_cases": sum(
            1
            for case in RUNTIME_CASES
            if cases.get(case, {}).get("status") == "passed"
        ),
        "required_cases": len(RUNTIME_CASES),
    }
