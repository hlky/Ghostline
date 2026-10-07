"""Stage, verify, and publish RID binaries at the WolvenKit boundary."""
from __future__ import annotations
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from artifact_io import atomic_write_json
from toolchain import default_tool_path, resolve_tool
from typing import Any
from braindance_support.rid_types import (
    CR2W_MAGIC,
    RidCompileError,
    RidValidationReport,
)
from braindance_support.rid_compile import (
    compile_rid_document,
)
from braindance_support.rid_validation import (
    validate_compiled_document,
)


ROOT = Path(__file__).resolve().parents[2]


DEFAULT_HANDOFF = (
    ROOT
    / "projects/test-quests/gqt005"
    / ".tmp"
    / "braindance"
    / "gqt005"
    / "gqt005_braindance_analysis.handoff.json"
)


DEFAULT_OUTPUT = (
    ROOT
    / "projects/test-quests/gqt005"
    / ".tmp"
    / "braindance"
    / "gqt005"
    / "gqt005_braindance_analysis.scenerid"
)


WOLVENKIT_CLI = default_tool_path("wolvenkit")


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RidCompileError(f"JSON does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RidCompileError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RidCompileError(f"JSON root must be an object: {path}")
    return value


def write_json(path: Path, value: Any) -> None:
    atomic_write_json(path, value)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def find_wolvenkit(explicit: Path | None = None) -> Path:
    try:
        return resolve_tool("wolvenkit", explicit)
    except (OSError, ValueError) as exc:
        raise RidCompileError(str(exc)) from exc


def _run(command: list[str]) -> str:
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
        raise RidCompileError(
            f"Command failed ({completed.returncode}): {' '.join(command)}\n"
            f"{completed.stdout.strip()}"
        )
    return completed.stdout


def serialize_template(
    template_path: Path,
    output_directory: Path,
    wolvenkit: Path,
) -> Path:
    if template_path.name.casefold().endswith(".scenerid.json"):
        return template_path
    if template_path.suffix.casefold() != ".scenerid":
        raise RidCompileError("Template must be .scenerid or .scenerid.json")
    output_directory.mkdir(parents=True, exist_ok=True)
    _run(
        [
            str(wolvenkit),
            "cr2w",
            "--serialize",
            "--outpath",
            str(output_directory),
            str(template_path.resolve()),
            "--verbosity",
            "Minimal",
        ]
    )
    output = output_directory / f"{template_path.name}.json"
    if not output.is_file():
        raise RidCompileError(f"WolvenKit did not produce template JSON: {output}")
    return output


def deserialize_rid(
    json_path: Path,
    output_path: Path,
    wolvenkit: Path,
    staging_directory: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    staging_directory.mkdir(parents=True, exist_ok=True)
    expected_name = json_path.name.removesuffix(".json")
    if expected_name != output_path.name:
        raise RidCompileError(
            f"Compiler JSON must be named {output_path.name}.json, got {json_path.name}"
        )
    _run(
        [
            str(wolvenkit),
            "cr2w",
            "--deserialize",
            "--outpath",
            str(staging_directory),
            str(json_path.resolve()),
            "--verbosity",
            "Minimal",
        ]
    )
    staged_output = staging_directory / output_path.name
    if not staged_output.is_file():
        raise RidCompileError(f"WolvenKit did not produce RID: {staged_output}")
    with staged_output.open("rb") as stream:
        if stream.read(4) != CR2W_MAGIC:
            raise RidCompileError(
                f"Generated RID has invalid CR2W magic: {staged_output}"
            )
    shutil.copyfile(staged_output, output_path)


def verify_binary(
    output_path: Path,
    wolvenkit: Path,
    *,
    expected_name: str,
    expected_duration: float,
    expected_actor_signatures: list[str],
    directory: Path,
) -> RidValidationReport:
    directory.mkdir(parents=True, exist_ok=True)
    _run(
        [
            str(wolvenkit),
            "cr2w",
            "--serialize",
            "--outpath",
            str(directory),
            str(output_path.resolve()),
            "--verbosity",
            "Minimal",
        ]
    )
    json_path = directory / f"{output_path.name}.json"
    if not json_path.is_file():
        raise RidCompileError(f"WolvenKit did not verify RID as JSON: {json_path}")
    report = validate_compiled_document(
        load_json(json_path),
        expected_name=expected_name,
        expected_duration=expected_duration,
        expected_actor_signatures=expected_actor_signatures,
    )
    if not report.ok:
        raise RidCompileError("Generated RID verification failed: " + "; ".join(report.errors))
    return report


def _validation_buffer_hashes(report: RidValidationReport) -> dict[str, Any]:
    return {
        "actors": [
            {
                "actor": details["actor"],
                "sha256": details["sha256"],
            }
            for details in report.details.get("actor_animation_buffers", [])
        ],
        "auxiliary": [
            {
                "actor": details["actor"],
                "channel": details["channel"],
                "sha256": details["sha256"],
            }
            for details in report.details.get(
                "auxiliary_animation_buffers", []
            )
        ],
        "camera": (
            report.details["camera_animation_buffer"]["sha256"]
            if report.details.get("camera_animation_buffer")
            else None
        ),
    }


def compile_binary(
    handoff_path: Path,
    template_path: Path,
    output_path: Path,
    *,
    wolvenkit_path: Path | None = None,
    actor_template_signatures: list[str] | None = None,
    json_output_path: Path | None = None,
    report_path: Path | None = None,
    verify: bool = True,
) -> dict[str, Any]:
    handoff = load_json(handoff_path)
    wolvenkit = find_wolvenkit(wolvenkit_path)
    output_path = output_path.resolve()
    json_output_path = (
        json_output_path.resolve()
        if json_output_path is not None
        else Path(f"{output_path}.json")
    )
    report_path = (
        report_path.resolve()
        if report_path is not None
        else output_path.with_name(f"{output_path.stem}.rid-report.json")
    )
    if json_output_path.name != f"{output_path.name}.json":
        raise RidCompileError(
            f"--json-output must end with {output_path.name}.json so WolvenKit "
            "emits the requested binary name"
        )
    with tempfile.TemporaryDirectory(prefix="ghostline-rid-") as temp:
        temp_root = Path(temp)
        template_json_path = serialize_template(
            template_path.resolve(),
            temp_root / "template",
            wolvenkit,
        )
        template = load_json(template_json_path)
        compiled, build_report = compile_rid_document(
            handoff,
            template,
            actor_template_signatures=actor_template_signatures,
        )
        expected_duration = (
            handoff["frames"]["end"] - handoff["frames"]["start"]
        ) / handoff["fps"]
        actor_signatures = [
            str(actor.get("rid_signature", actor["id"])) for actor in handoff["actors"]
        ]
        validation = validate_compiled_document(
            compiled,
            expected_name=handoff["name"],
            expected_duration=expected_duration,
            expected_actor_signatures=actor_signatures,
        )
        if not validation.ok:
            raise RidCompileError("Compiled JSON is invalid: " + "; ".join(validation.errors))
        write_json(json_output_path, compiled)
        deserialize_rid(
            json_output_path,
            output_path,
            wolvenkit,
            temp_root / "binary",
        )
        verified = None
        if verify:
            verified = verify_binary(
                output_path,
                wolvenkit,
                expected_name=handoff["name"],
                expected_duration=expected_duration,
                expected_actor_signatures=actor_signatures,
                directory=temp_root / "verified",
            )
            compiled_hashes = _validation_buffer_hashes(validation)
            verified_hashes = _validation_buffer_hashes(verified)
            if verified_hashes != compiled_hashes:
                raise RidCompileError(
                    "Generated RID round trip changed authored animation buffers"
                )
    build_report.update(
        {
            "handoff": str(handoff_path.resolve()),
            "handoff_sha256": file_sha256(handoff_path),
            "template": str(template_path.resolve()),
            "template_sha256": file_sha256(template_path),
            "wolvenkit": str(wolvenkit),
            "json_output": str(json_output_path),
            "binary_output": str(output_path),
            "binary_size": output_path.stat().st_size,
            "binary_sha256": file_sha256(output_path),
            "cr2w_magic": True,
            "validation": {
                "compiled_json": validation.details,
                "round_trip": verified.details if verified is not None else None,
                "animation_buffer_hashes": _validation_buffer_hashes(validation),
            },
        }
    )
    write_json(report_path, build_report)
    return build_report
