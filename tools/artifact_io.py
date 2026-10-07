"""Publish complete JSON artifact sets, preserving earlier outputs on failure."""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


def _stage_bytes(path: Path, content: bytes) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise
    return temporary


def _json_bytes(value: Any, *, ensure_ascii: bool, indent: int | None) -> bytes:
    return (json.dumps(value, ensure_ascii=ensure_ascii, indent=indent) + "\n").encode(
        "utf-8"
    )


def atomic_write_json(
    path: Path, value: Any, *, ensure_ascii: bool = False, indent: int | None = 2
) -> None:
    """Replace one JSON document only after serialization and writing succeed."""
    path = Path(path)
    content = _json_bytes(value, ensure_ascii=ensure_ascii, indent=indent)
    if path.is_file() and path.read_bytes() == content:
        return
    temporary = _stage_bytes(path, content)
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


@dataclass(frozen=True)
class PublicationReport:
    paths: tuple[Path, ...]
    obsolete_paths: tuple[Path, ...]


def publish_json_artifacts(
    artifacts: Mapping[Path, Any],
    *,
    ownership_path: Path | None = None,
    binary_artifacts: Mapping[Path, bytes] | None = None,
) -> PublicationReport:
    """Stage all documents, then replace them with rollback on a failed write.

    Ownership records report retired outputs; they never authorize deletion.
    This is an exception-safe local transaction, not a crash-atomic filesystem
    transaction. Binary import and game installation are separate operations.
    """
    documents: dict[Path, Any] = {}
    for destination, value in artifacts.items():
        path = Path(destination).resolve()
        if path in documents:
            raise ValueError(f"Duplicate artifact destination: {path}")
        documents[path] = value
    binaries: dict[Path, bytes] = {}
    for destination, content in (binary_artifacts or {}).items():
        path = Path(destination).resolve()
        if path in documents or path in binaries:
            raise ValueError(f"Duplicate artifact destination: {path}")
        if not isinstance(content, bytes):
            raise TypeError(f"Binary artifact must contain bytes: {path}")
        binaries[path] = content
    paths = (*documents, *binaries)
    obsolete: set[Path] = set()
    if ownership_path is not None:
        ownership_path = Path(ownership_path).resolve()
        if ownership_path in documents or ownership_path in binaries:
            raise ValueError("Ownership record must have its own destination")
        if ownership_path.exists():
            previous = json.loads(ownership_path.read_text(encoding="utf-8"))
            if previous.get("schema_version") != 1:
                raise ValueError(
                    f"Unsupported artifact ownership record: {ownership_path}"
                )
            obsolete.update(Path(path) for path in previous.get("outputs", []))
            obsolete.update(Path(path) for path in previous.get("obsolete", []))
        obsolete.difference_update(paths)
        documents[ownership_path] = {
            "schema_version": 1,
            "outputs": [str(path) for path in paths],
            "obsolete": [str(path) for path in sorted(obsolete)],
        }

    # Serialize the entire collection before creating or replacing any file.
    encoded = {
        path: _json_bytes(value, ensure_ascii=False, indent=2)
        for path, value in documents.items()
    }
    encoded.update(binaries)
    staged: dict[Path, Path] = {}
    backups: dict[Path, Path | None] = {}
    replaced: list[Path] = []
    recovery_files: set[Path] = set()
    try:
        for path, content in encoded.items():
            old = path.read_bytes() if path.exists() else None
            if old == content:
                continue
            staged[path] = _stage_bytes(path, content)
            backups[path] = _stage_bytes(path, old) if old is not None else None
        try:
            for path, temporary in staged.items():
                os.replace(temporary, path)
                replaced.append(path)
        except BaseException as publication_error:
            recovery_errors: list[str] = []
            for path in reversed(replaced):
                backup = backups[path]
                try:
                    if backup is None:
                        path.unlink(missing_ok=True)
                    else:
                        os.replace(backup, path)
                except OSError as recovery_error:
                    if backup is not None:
                        recovery_files.add(backup)
                    recovery_errors.append(
                        f"{path}: {recovery_error}; backup: {backup}"
                    )
            if recovery_errors:
                raise RuntimeError(
                    "Artifact rollback needs recovery: " + "; ".join(recovery_errors)
                ) from publication_error
            raise
    finally:
        for temporary in [*staged.values(), *backups.values()]:
            if temporary is not None and temporary not in recovery_files:
                temporary.unlink(missing_ok=True)
    return PublicationReport(paths, tuple(sorted(obsolete)))
