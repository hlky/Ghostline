"""Fresh export staging and transactional publication for character preview caches."""

from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from typing import Callable, TypeVar

T = TypeVar("T")


def file_identity(path: Path) -> dict[str, str | int]:
    stat = path.stat()
    return {"path": str(path.resolve()), "size": stat.st_size, "mtime_ns": stat.st_mtime_ns}


def archive_identities(game_path: Path) -> list[dict[str, str | int]]:
    """Fingerprint the files exports consume, rather than their parent directory."""
    root = game_path / "archive" / "pc"
    return [
        file_identity(path)
        for folder in (root / "content", root / "ep1")
        for path in sorted(folder.rglob("*.archive"))
    ]


def fingerprint(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def cache_matches(manifest: Path, key: str, files: list[Path]) -> bool:
    try:
        value = json.loads(manifest.read_text(encoding="utf-8-sig"))
        return (
            isinstance(value, dict)
            and value.get("cache_key") == key
            and bool(files)
            and all(path.is_file() and path.stat().st_size > 0 for path in files)
        )
    except (OSError, ValueError):
        return False


def refresh_export(
    output: Path,
    files: list[Path],
    export: Callable[[Path], T],
    *,
    validate: Callable[[Path], None] | None = None,
    remove: tuple[Path, ...] = (),
) -> T:
    """Build and check every file before replacing anything; roll back failed promotion.

    ``files`` are relative paths, in publication order (cache metadata goes last).
    The callback receives a fresh staging root. Format-specific validation stays
    with the exporter and can fail without changing the previous cache.
    """
    for relative in [*files, *remove]:
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"Export path must remain relative to its cache: {relative}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output.parent, prefix=f".{output.name}.refresh.") as directory:
        staging = Path(directory)
        result = export(staging)
        for relative in files:
            path = staging / relative
            if not path.is_file() or path.stat().st_size == 0:
                raise OSError(f"Export did not produce a complete file: {relative}")
        if validate is not None:
            validate(staging)
        backups = staging / ".previous"
        promoted: list[tuple[Path, Path | None]] = []
        try:
            for relative in files:
                source, target = staging / relative, output / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                backup = backups / relative if target.is_file() else None
                if backup is not None:
                    backup.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(target, backup)
                source.replace(target)
                promoted.append((target, backup))
            for relative in remove:
                target = output / relative
                if target.is_file():
                    backup = backups / relative
                    backup.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(target, backup)
                    target.unlink()
                    promoted.append((target, backup))
        except BaseException:
            for target, backup in reversed(promoted):
                if backup is None:
                    target.unlink(missing_ok=True)
                else:
                    backup.replace(target)
            raise
        return result
