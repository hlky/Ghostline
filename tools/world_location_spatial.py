#!/usr/bin/env python3
"""Actual-content spatial index for serialized world streaming sectors.

Streaming-block descriptor bounds are not always useful spatial bounds.  In
particular, quest descriptors can cover most or all of the world even when the
serialized sector only contains a handful of local placements.  This module
indexes the positions in ``worldStreamingSector.nodeData`` instead.

The implementation intentionally uses only the Python standard library.  It
does not depend on :mod:`world_location_world`; ``Bounds3D.coerce`` accepts a
six-value tuple, a pair of three-value tuples, or any dataclass-like object
with ``min_x`` through ``max_z`` attributes.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import tempfile
from bisect import bisect_right
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any


CACHE_FORMAT_VERSION = 3
SECTOR_JSON_SUFFIX = ".streamingsector.json"


class SpatialIndexError(ValueError):
    """Raised when a serialized sector cannot be indexed safely."""


def _scalar(value: Any) -> Any:
    """Unwrap the scalar wrappers emitted by WolvenKit and ghostline-red."""

    seen: set[int] = set()
    while isinstance(value, Mapping):
        identity = id(value)
        if identity in seen:
            break
        seen.add(identity)
        if "$value" in value:
            value = value["$value"]
            continue
        if "value" in value and set(value).issubset({"$type", "value"}):
            value = value["value"]
            continue
        break
    return value


def _number(value: Any) -> float | None:
    value = _scalar(value)
    if value is None or isinstance(value, bool):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError):
        return None
    return result if math.isfinite(result) else None


def _integer(value: Any) -> int | None:
    value = _scalar(value)
    if value is None or isinstance(value, bool):
        return None
    try:
        numeric = float(value)
    except (TypeError, ValueError, OverflowError):
        return None
    if not math.isfinite(numeric) or not numeric.is_integer():
        return None
    return int(numeric)


def normalize_depot_path(value: Any) -> str:
    """Return a stable, case-insensitive REDengine depot path."""

    value = _scalar(value)
    if value is None:
        return ""
    text = str(value).strip().replace("/", "\\")
    while "\\\\" in text:
        text = text.replace("\\\\", "\\")
    while text.startswith(".\\"):
        text = text[2:]
    text = text.lstrip("\\")
    if text.casefold().endswith(".streamingsector.json"):
        text = text[:-5]
    return text.casefold()


@dataclass(frozen=True)
class Bounds3D:
    """Inclusive axis-aligned bounds used by the sector index."""

    min_x: float
    min_y: float
    min_z: float
    max_x: float
    max_y: float
    max_z: float

    def __post_init__(self) -> None:
        values = (
            self.min_x,
            self.min_y,
            self.min_z,
            self.max_x,
            self.max_y,
            self.max_z,
        )
        if any(math.isnan(float(value)) for value in values):
            raise SpatialIndexError("Bounds cannot contain NaN coordinates.")
        if (
            self.min_x > self.max_x
            or self.min_y > self.max_y
            or self.min_z > self.max_z
        ):
            raise SpatialIndexError(f"Bounds minimum exceeds maximum: {self!r}")

    @classmethod
    def coerce(cls, value: Any) -> Bounds3D:
        """Coerce tuples, mappings, or dataclass-like bounds to ``Bounds3D``."""

        if isinstance(value, cls):
            return value

        names = ("min_x", "min_y", "min_z", "max_x", "max_y", "max_z")
        if isinstance(value, Mapping) and all(name in value for name in names):
            return cls(*(float(value[name]) for name in names))
        if all(hasattr(value, name) for name in names):
            return cls(*(float(getattr(value, name)) for name in names))

        if isinstance(value, Sequence) and not isinstance(
            value, (str, bytes, bytearray)
        ):
            if len(value) == 6:
                return cls(*(float(item) for item in value))
            if len(value) == 2:
                minimum, maximum = value
                if (
                    isinstance(minimum, Sequence)
                    and not isinstance(minimum, (str, bytes, bytearray))
                    and isinstance(maximum, Sequence)
                    and not isinstance(maximum, (str, bytes, bytearray))
                    and len(minimum) == 3
                    and len(maximum) == 3
                ):
                    return cls(
                        float(minimum[0]),
                        float(minimum[1]),
                        float(minimum[2]),
                        float(maximum[0]),
                        float(maximum[1]),
                        float(maximum[2]),
                    )
        raise SpatialIndexError(
            "Bounds must be six values, (minimum, maximum), or expose "
            "min_x through max_z attributes."
        )

    def intersects(self, other: Any) -> bool:
        """Return whether these inclusive bounds intersect ``other``."""

        candidate = self.coerce(other)
        return not (
            self.max_x < candidate.min_x
            or self.min_x > candidate.max_x
            or self.max_y < candidate.min_y
            or self.min_y > candidate.max_y
            or self.max_z < candidate.min_z
            or self.min_z > candidate.max_z
        )

    def to_list(self) -> list[float]:
        """Return a compact JSON representation."""

        return [self.min_x, self.min_y, self.min_z, self.max_x, self.max_y, self.max_z]

    @classmethod
    def from_list(cls, value: Any) -> Bounds3D:
        return cls.coerce(value)


@dataclass(frozen=True)
class SourceJsonIdentity:
    """Filesystem and content identity for one serialized sector source."""

    root: str
    relative_path: str
    absolute_path: str
    size: int
    mtime_ns: int
    sha256: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "root": self.root,
            "relative_path": self.relative_path,
            "absolute_path": self.absolute_path,
            "size": self.size,
            "mtime_ns": self.mtime_ns,
            "sha256": self.sha256,
        }

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> SourceJsonIdentity:
        return cls(
            root=str(value["root"]),
            relative_path=str(value["relative_path"]),
            absolute_path=str(value["absolute_path"]),
            size=int(value["size"]),
            mtime_ns=int(value["mtime_ns"]),
            sha256=str(value["sha256"]),
        )


@dataclass(frozen=True)
class SectorSpatialRecord:
    """Actual placement bounds and provenance for one serialized sector."""

    depot_path: str
    bounds: Bounds3D | None
    node_count: int
    located_node_count: int
    unlocated_node_count: int
    category: str
    level: int | None
    source: SourceJsonIdentity
    placement_positions: tuple[tuple[float, float, float], ...]

    @property
    def source_json(self) -> Path:
        return Path(self.source.absolute_path)

    def to_dict(self) -> dict[str, Any]:
        return {
            "depot_path": self.depot_path,
            "bounds": None if self.bounds is None else self.bounds.to_list(),
            "node_count": self.node_count,
            "located_node_count": self.located_node_count,
            "unlocated_node_count": self.unlocated_node_count,
            "category": self.category,
            "level": self.level,
            "source": self.source.to_dict(),
            "placement_positions": [list(point) for point in self.placement_positions],
        }

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> SectorSpatialRecord:
        raw_bounds = value.get("bounds")
        return cls(
            depot_path=normalize_depot_path(value["depot_path"]),
            bounds=None if raw_bounds is None else Bounds3D.from_list(raw_bounds),
            node_count=int(value["node_count"]),
            located_node_count=int(value["located_node_count"]),
            unlocated_node_count=int(value["unlocated_node_count"]),
            category=str(value.get("category", "")),
            level=None if value.get("level") is None else int(value["level"]),
            source=SourceJsonIdentity.from_dict(value["source"]),
            placement_positions=tuple(
                (float(point[0]), float(point[1]), float(point[2]))
                for point in value["placement_positions"]
            ),
        )


@dataclass(frozen=True)
class RootSnapshot:
    """Cheap deterministic cache key for a set of serialized JSON roots."""

    roots: tuple[str, ...]
    file_count: int
    total_size: int
    max_mtime_ns: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "roots": list(self.roots),
            "file_count": self.file_count,
            "total_size": self.total_size,
            "max_mtime_ns": self.max_mtime_ns,
        }

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> RootSnapshot:
        return cls(
            roots=tuple(str(item) for item in value["roots"]),
            file_count=int(value["file_count"]),
            total_size=int(value["total_size"]),
            max_mtime_ns=int(value["max_mtime_ns"]),
        )


def _record_sort_key(record: SectorSpatialRecord) -> tuple[str, str, str]:
    return (
        record.depot_path,
        record.source.relative_path.casefold(),
        record.source.absolute_path.casefold(),
    )


@dataclass(frozen=True)
class SectorSpatialIndex:
    """Immutable collection with a standard-library X-axis sweep index."""

    records: tuple[SectorSpatialRecord, ...]
    snapshot: RootSnapshot
    cache_hit: bool = field(default=False, compare=False)
    _x_records: tuple[SectorSpatialRecord, ...] = field(
        init=False, repr=False, compare=False
    )
    _x_minimums: tuple[float, ...] = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        records = tuple(sorted(self.records, key=_record_sort_key))
        located = sorted(
            (record for record in records if record.bounds is not None),
            key=lambda record: (
                record.bounds.min_x if record.bounds is not None else math.inf,
                *_record_sort_key(record),
            ),
        )
        object.__setattr__(self, "records", records)
        object.__setattr__(self, "_x_records", tuple(located))
        object.__setattr__(
            self,
            "_x_minimums",
            tuple(
                record.bounds.min_x for record in located if record.bounds is not None
            ),
        )

    @property
    def located_records(self) -> tuple[SectorSpatialRecord, ...]:
        return tuple(record for record in self.records if record.bounds is not None)

    @property
    def unlocated_records(self) -> tuple[SectorSpatialRecord, ...]:
        return tuple(record for record in self.records if record.bounds is None)

    def query(self, bounds: Any) -> tuple[SectorSpatialRecord, ...]:
        """Return deterministically ordered records intersecting ``bounds``.

        Records with no valid placement positions are never returned.  Their
        counts and source identity remain available through ``records`` and
        ``unlocated_records`` so callers can report or handle them explicitly.
        """

        query_bounds = Bounds3D.coerce(bounds)
        candidate_end = bisect_right(self._x_minimums, query_bounds.max_x)
        matches = (
            record
            for record in self._x_records[:candidate_end]
            if record.bounds is not None and record.bounds.intersects(query_bounds)
        )
        return tuple(sorted(matches, key=_record_sort_key))

    def query_placements(self, bounds: Any) -> tuple[SectorSpatialRecord, ...]:
        """Return records with at least one actual placement inside ``bounds``.

        ``query`` is deliberately an aggregate-AABB broad phase.  Sparse quest
        sectors can span kilometres between a few placements, so callers that
        select tile-local quest content must use this exact second phase to
        avoid importing unrelated placements from the middle of that span.
        """

        query_bounds = Bounds3D.coerce(bounds)
        return tuple(
            record
            for record in self.query(query_bounds)
            if any(
                query_bounds.min_x <= x <= query_bounds.max_x
                and query_bounds.min_y <= y <= query_bounds.max_y
                and query_bounds.min_z <= z <= query_bounds.max_z
                for x, y, z in record.placement_positions
            )
        )

    def for_depot_path(self, depot_path: Any) -> tuple[SectorSpatialRecord, ...]:
        """Return all source records for a normalized depot path."""

        normalized = normalize_depot_path(depot_path)
        return tuple(
            record for record in self.records if record.depot_path == normalized
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "format_version": CACHE_FORMAT_VERSION,
            "snapshot": self.snapshot.to_dict(),
            "records": [record.to_dict() for record in self.records],
        }


@dataclass(frozen=True)
class _DiscoveredSector:
    path: Path
    root: Path
    size: int
    mtime_ns: int


def _path_key(path: Path) -> str:
    return os.path.normcase(str(path.resolve())).casefold()


def _normalize_roots(
    roots: str | os.PathLike[str] | Iterable[str | os.PathLike[str]],
) -> tuple[Path, ...]:
    if isinstance(roots, (str, os.PathLike)):
        values = [roots]
    else:
        values = list(roots)
    if not values:
        raise SpatialIndexError("At least one serialized sector JSON root is required.")

    normalized: dict[str, Path] = {}
    for raw_root in values:
        root = Path(raw_root).expanduser().resolve()
        if not root.exists():
            raise SpatialIndexError(
                f"Serialized sector JSON root does not exist: {root}"
            )
        if root.is_file() and not root.name.casefold().endswith(SECTOR_JSON_SUFFIX):
            raise SpatialIndexError(f"Expected a *{SECTOR_JSON_SUFFIX} file: {root}")
        if not root.is_file() and not root.is_dir():
            raise SpatialIndexError(
                f"Serialized sector JSON root is not a file or directory: {root}"
            )
        normalized[_path_key(root)] = root
    return tuple(normalized[key] for key in sorted(normalized))


def _relative_to(path: Path, root: Path) -> Path:
    if root.is_file():
        return Path(path.name)
    return path.relative_to(root)


def _discover_sectors(roots: tuple[Path, ...]) -> tuple[_DiscoveredSector, ...]:
    candidates: dict[str, tuple[Path, list[Path]]] = {}
    for root in roots:
        paths = [root] if root.is_file() else list(root.rglob(f"*{SECTOR_JSON_SUFFIX}"))
        for path in paths:
            if not path.is_file():
                continue
            resolved = path.resolve()
            key = _path_key(resolved)
            if key not in candidates:
                candidates[key] = (resolved, [root])
            else:
                candidates[key][1].append(root)

    discovered: list[_DiscoveredSector] = []
    for key in sorted(candidates):
        path, matching_roots = candidates[key]
        # The most specific root gives a useful relative fallback even when
        # callers supplied overlapping parent and child roots.
        source_root = sorted(
            matching_roots, key=lambda item: (-len(item.parts), _path_key(item))
        )[0]
        stat = path.stat()
        discovered.append(
            _DiscoveredSector(
                path=path,
                root=source_root,
                size=stat.st_size,
                mtime_ns=stat.st_mtime_ns,
            )
        )
    return tuple(discovered)


def _snapshot(
    roots: tuple[Path, ...], sectors: tuple[_DiscoveredSector, ...]
) -> RootSnapshot:
    return RootSnapshot(
        roots=tuple(str(root) for root in roots),
        file_count=len(sectors),
        total_size=sum(sector.size for sector in sectors),
        max_mtime_ns=max((sector.mtime_ns for sector in sectors), default=0),
    )


def snapshot_sector_json_roots(
    roots: str | os.PathLike[str] | Iterable[str | os.PathLike[str]],
) -> RootSnapshot:
    """Return the cache-invalidation snapshot for one or more JSON roots."""

    normalized_roots = _normalize_roots(roots)
    return _snapshot(normalized_roots, _discover_sectors(normalized_roots))


def _root_chunk(document: Any) -> Mapping[str, Any]:
    if not isinstance(document, Mapping):
        return {}
    data = document.get("Data")
    if isinstance(data, Mapping) and isinstance(data.get("RootChunk"), Mapping):
        return data["RootChunk"]
    root = document.get("RootChunk")
    return root if isinstance(root, Mapping) else {}


def _node_entries(root: Mapping[str, Any]) -> list[Any]:
    value: Any = root.get("nodeData")
    for _ in range(3):
        if isinstance(value, list):
            return value
        if isinstance(value, Mapping) and "Data" in value:
            value = value["Data"]
            continue
        break
    return []


def _position(entry: Any) -> tuple[float, float, float] | None:
    if not isinstance(entry, Mapping):
        return None
    value = entry.get("Position")
    if not isinstance(value, Mapping):
        return None
    coordinates = tuple(_number(value.get(axis)) for axis in ("X", "Y", "Z"))
    if any(coordinate is None for coordinate in coordinates):
        return None
    x, y, z = coordinates
    assert x is not None and y is not None and z is not None
    return x, y, z


def _bounds(positions: Sequence[tuple[float, float, float]]) -> Bounds3D | None:
    if not positions:
        return None
    return Bounds3D(
        min(point[0] for point in positions),
        min(point[1] for point in positions),
        min(point[2] for point in positions),
        max(point[0] for point in positions),
        max(point[1] for point in positions),
        max(point[2] for point in positions),
    )


def _fallback_depot_path(sector: _DiscoveredSector) -> str:
    relative = _relative_to(sector.path, sector.root)
    return normalize_depot_path(relative.as_posix())


def _is_absolute_filesystem_path(value: Any) -> bool:
    """Recognize host-independent absolute paths stored in CR2W headers."""

    value = _scalar(value)
    if value is None:
        return False
    text = str(value).strip()
    if not text:
        return False

    windows_path = PureWindowsPath(text)
    return (
        windows_path.is_absolute()
        or bool(windows_path.drive)
        or PurePosixPath(text.replace("\\", "/")).is_absolute()
    )


def _canonical_depot_path(archive_name: Any, sector: _DiscoveredSector) -> str:
    """Choose a depot path without leaking serializer output locations.

    A valid ``ArchiveFileName`` is already a depot-relative REDengine path and
    remains authoritative.  Native serialization tools can instead stamp the
    absolute output filename into that field.  In that case the discovered
    source path relative to the caller-supplied JSON root is the canonical
    depot identity.
    """

    normalized_header = normalize_depot_path(archive_name)
    if normalized_header and not _is_absolute_filesystem_path(archive_name):
        return normalized_header
    return _fallback_depot_path(sector)


def _parse_sector(sector: _DiscoveredSector) -> SectorSpatialRecord:
    try:
        raw = sector.path.read_bytes()
        document = json.loads(raw.decode("utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SpatialIndexError(
            f"Could not read serialized sector {sector.path}: {exc}"
        ) from exc

    root = _root_chunk(document)
    entries = _node_entries(root)
    positions = [
        position for entry in entries if (position := _position(entry)) is not None
    ]
    unique_positions = tuple(sorted(set(positions)))

    header = document.get("Header") if isinstance(document, Mapping) else None
    archive_name = (
        header.get("ArchiveFileName") if isinstance(header, Mapping) else None
    )
    depot_path = _canonical_depot_path(archive_name, sector)

    raw_category = _scalar(root.get("category"))
    category = "" if raw_category is None else str(raw_category).strip().casefold()
    level = _integer(root.get("level"))
    relative = _relative_to(sector.path, sector.root)
    stat = sector.path.stat()
    source = SourceJsonIdentity(
        root=str(sector.root),
        relative_path=relative.as_posix(),
        absolute_path=str(sector.path),
        size=len(raw),
        mtime_ns=stat.st_mtime_ns,
        sha256=hashlib.sha256(raw).hexdigest(),
    )
    return SectorSpatialRecord(
        depot_path=depot_path,
        bounds=_bounds(positions),
        node_count=len(entries),
        located_node_count=len(positions),
        unlocated_node_count=len(entries) - len(positions),
        category=category,
        level=level,
        source=source,
        placement_positions=unique_positions,
    )


def _load_cache(path: Path, expected: RootSnapshot) -> SectorSpatialIndex | None:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(document, Mapping):
            return None
        if int(document.get("format_version", -1)) != CACHE_FORMAT_VERSION:
            return None
        cached_snapshot = RootSnapshot.from_dict(document["snapshot"])
        if cached_snapshot != expected:
            return None
        raw_records = document["records"]
        if not isinstance(raw_records, list):
            return None
        records = tuple(SectorSpatialRecord.from_dict(item) for item in raw_records)
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        KeyError,
        TypeError,
        ValueError,
    ):
        return None
    return SectorSpatialIndex(records=records, snapshot=expected, cache_hit=True)


def _atomic_write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            prefix=f".{path.name}.",
            suffix=".tmp",
            dir=path.parent,
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def build_sector_spatial_index(
    roots: str | os.PathLike[str] | Iterable[str | os.PathLike[str]],
    *,
    cache_path: str | os.PathLike[str] | None = None,
    force_rebuild: bool = False,
) -> SectorSpatialIndex:
    """Build or load an actual-content spatial index.

    Cache validity is intentionally cheap to evaluate: normalized root paths,
    matching file count, total byte size, and maximum nanosecond mtime.  A
    rebuild is retried once if that snapshot changes while files are parsed.
    """

    normalized_roots = _normalize_roots(roots)
    cache = None if cache_path is None else Path(cache_path).expanduser().resolve()

    for attempt in range(2):
        discovered = _discover_sectors(normalized_roots)
        before = _snapshot(normalized_roots, discovered)
        if attempt == 0 and cache is not None and cache.is_file() and not force_rebuild:
            cached = _load_cache(cache, before)
            if cached is not None:
                return cached

        records = tuple(_parse_sector(sector) for sector in discovered)
        after_discovered = _discover_sectors(normalized_roots)
        after = _snapshot(normalized_roots, after_discovered)
        before_paths = tuple(_path_key(sector.path) for sector in discovered)
        after_paths = tuple(_path_key(sector.path) for sector in after_discovered)
        if before == after and before_paths == after_paths:
            index = SectorSpatialIndex(records=records, snapshot=after, cache_hit=False)
            if cache is not None:
                _atomic_write_json(cache, index.to_dict())
            return index

    raise SpatialIndexError(
        "Serialized sector JSON roots changed repeatedly while indexing."
    )


__all__ = [
    "Bounds3D",
    "CACHE_FORMAT_VERSION",
    "RootSnapshot",
    "SECTOR_JSON_SUFFIX",
    "SectorSpatialIndex",
    "SectorSpatialRecord",
    "SourceJsonIdentity",
    "SpatialIndexError",
    "build_sector_spatial_index",
    "normalize_depot_path",
    "snapshot_sector_json_roots",
]
