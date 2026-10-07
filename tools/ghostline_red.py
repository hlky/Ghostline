"""Shared ghostline-red CLI paths and CR2W conversion helpers."""

from __future__ import annotations

import hashlib
import subprocess
import json
import tempfile
from pathlib import Path

from artifact_io import atomic_write_json, publish_json_artifacts
from toolchain import default_tool_path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RED_CLI = default_tool_path("ghostline_red")
DEFAULT_RED_SCHEMA = ROOT / "red-schema.json"
WOLVENKIT_SOURCE = ROOT / "WolvenKit"


def schema_input_identity(red_cli: Path) -> dict[str, str]:
    """Identify the writer, pin, and actual C# worktree consumed by schema-generate."""
    def git(*arguments: str) -> bytes:
        return subprocess.run(
            ["git", "-C", str(WOLVENKIT_SOURCE), *arguments],
            capture_output=True, check=True,
        ).stdout

    revision = git("rev-parse", "HEAD").decode().strip()
    worktree = hashlib.sha256(git("diff", "--no-ext-diff", "--binary", "HEAD", "--", "*.cs"))
    # The native scanner also reads ignored build-generated C# files. Include
    # those as well as new authoring types instead of assuming HEAD is complete.
    untracked = set(git("ls-files", "--others", "--exclude-standard", "-z", "--", "*.cs").split(b"\0"))
    untracked.update(git("ls-files", "--others", "--ignored", "--exclude-standard", "-z", "--", "*.cs").split(b"\0"))
    for relative in sorted(untracked - {b""}):
        path = WOLVENKIT_SOURCE / relative.decode("utf-8")
        worktree.update(relative + b"\0")
        worktree.update(hashlib.sha256(path.read_bytes()).digest())
    return {
        "writer_sha256": hashlib.sha256(red_cli.read_bytes()).hexdigest(),
        "wolvenkit_revision": revision,
        "wolvenkit_worktree_sha256": worktree.hexdigest(),
    }


def ensure_schema(
    red_cli: Path = DEFAULT_RED_CLI,
    schema: Path = DEFAULT_RED_SCHEMA,
) -> Path:
    if not red_cli.is_file():
        raise FileNotFoundError(
            f"ghostline-red release not found: {red_cli}. "
            "Run cargo build --release --manifest-path tools/ghostline-red/Cargo.toml."
        )
    identity = schema_input_identity(red_cli)
    receipt = schema.with_name(schema.name + ".identity.json")
    try:
        previous = json.loads(receipt.read_text(encoding="utf-8"))
        valid = all(previous.get(key) == value for key, value in identity.items())
        valid = valid and previous.get("schema_sha256") == hashlib.sha256(schema.read_bytes()).hexdigest()
    except (OSError, ValueError, AttributeError):
        valid = False
    if not valid:
        schema.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=schema.parent, prefix=".red-schema.") as directory:
            candidate = Path(directory) / schema.name
            subprocess.run(
                [str(red_cli), "schema-generate", str(WOLVENKIT_SOURCE), str(candidate)],
                check=True,
            )
            document = json.loads(candidate.read_text(encoding="utf-8"))
            if not isinstance(document, dict):
                raise ValueError("Generated RED schema must be a JSON object")
            atomic_write_json(candidate, document)
            identity["schema_sha256"] = hashlib.sha256(candidate.read_bytes()).hexdigest()
            publish_json_artifacts({schema: document, receipt: identity})
    return schema


def deserialize(
    raw_path: Path,
    archive_path: Path,
    *,
    template: Path | None = None,
    red_cli: Path = DEFAULT_RED_CLI,
    schema: Path = DEFAULT_RED_SCHEMA,
) -> None:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    template = template or archive_path
    if not template.is_file():
        raise FileNotFoundError(
            f"CR2W template not found: {template}. Native writes require an "
            "existing resource with a compatible class layout."
        )
    subprocess.run(
        [
            str(red_cli),
            "cr2w-deserialize",
            str(raw_path),
            str(archive_path),
            "--template",
            str(template),
            "--schema",
            str(ensure_schema(red_cli, schema)),
        ],
        check=True,
    )


def deserialize_localization(
    raw_path: Path,
    archive_path: Path,
    *,
    template: Path | None = None,
    red_cli: Path = DEFAULT_RED_CLI,
) -> None:
    """Write an onscreen-localization CR2W with implicit default fields."""
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    template = template or archive_path
    if not template.is_file():
        raise FileNotFoundError(
            f"CR2W template not found: {template}. Native writes require an "
            "existing resource with a compatible class layout."
        )
    subprocess.run(
        [
            str(red_cli),
            "cr2w-deserialize-localization",
            str(raw_path),
            str(archive_path),
            "--template",
            str(template),
        ],
        check=True,
    )


def serialize(
    archive_path: Path,
    raw_path: Path,
    *,
    red_cli: Path = DEFAULT_RED_CLI,
    schema: Path = DEFAULT_RED_SCHEMA,
) -> None:
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            str(red_cli),
            "cr2w-serialize",
            str(archive_path),
            str(raw_path),
            "--schema",
            str(ensure_schema(red_cli, schema)),
        ],
        check=True,
    )
