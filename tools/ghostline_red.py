"""Shared ghostline-red CLI paths and CR2W conversion helpers."""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RED_CLI = ROOT / "tools/ghostline-red/target/release/ghostline-red.exe"
DEFAULT_RED_SCHEMA = ROOT / "red-schema.json"
WOLVENKIT_SOURCE = ROOT / "WolvenKit"


def ensure_schema(
    red_cli: Path = DEFAULT_RED_CLI,
    schema: Path = DEFAULT_RED_SCHEMA,
) -> Path:
    if not red_cli.is_file():
        raise FileNotFoundError(
            f"ghostline-red release not found: {red_cli}. "
            "Run cargo build --release --manifest-path tools/ghostline-red/Cargo.toml."
        )
    if not schema.is_file():
        subprocess.run(
            [str(red_cli), "schema-generate", str(WOLVENKIT_SOURCE), str(schema)],
            check=True,
        )
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
