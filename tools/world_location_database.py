from __future__ import annotations

import argparse
import collections
import copy
import functools
import hashlib
import json
import math
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence

from world_location_dependencies import (
    DependencyStagingError,
    normalize_depot_path as normalize_dependency_path,
)
from world_location_world import blender_node_is_visual


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = ROOT / "tools/world-location-poc-v1.json"
DEFAULT_OUTPUT = ROOT / "converted/world-location-database"
DEFAULT_BLOCK = Path(
    r"H:\Ghostline-audits\sq021-world-trace-20260724\block-serialized\all.streamingblock.json"
)
DEFAULT_SECTORS = Path(r"H:\Ghostline-audits\drop-point-index-20260722\all-sectors")
DEFAULT_QUEST_JSON = Path(r"H:\Ghostline-audits\vanilla-quest-sectors-20260726")
DEFAULT_GAME = Path(r"H:\Cyberpunk 2077")
DEFAULT_KRAKEN = Path(r"H:\WolvenKit.Console-8.17.4\kraken.dll")
DEFAULT_BLENDER = Path(r"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe")
DEFAULT_GHOSTLINE_RED = ROOT / "tools/ghostline-red/target/release/ghostline-red.exe"
DEFAULT_RED_SCHEMA = ROOT / "red-schema.json"
RENDER_SCRIPT = ROOT / "tools/world_location_render_blender.py"
SCHEMA_VERSION = 1
PIPELINE_VERSION = "world-location-poc-v2"
SAFE_ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
WINDOWS_RESERVED_NAMES = {
    "aux",
    "con",
    "nul",
    "prn",
    *(f"com{index}" for index in range(1, 10)),
    *(f"lpt{index}" for index in range(1, 10)),
}


class LocationDatabaseError(RuntimeError):
    pass


def validate_path_identifier(value: str, field: str) -> str:
    if not SAFE_ID_PATTERN.fullmatch(value) or value in WINDOWS_RESERVED_NAMES:
        raise LocationDatabaseError(
            f"{field} must be a lowercase hyphenated identifier: {value!r}"
        )
    return value


@dataclass(frozen=True)
class TileState:
    tile_id: str
    state_id: str
    label: str
    archetype: str
    district: str
    area: str
    anchor: tuple[float, float, float]
    bounds: tuple[float, float, float, float, float, float]
    clip_margin: float
    sector_categories: tuple[str, ...]
    lod_levels: tuple[int, ...]
    variant_policy: dict[str, Any]
    navigation_agent_types: tuple[str, ...]
    sample_spacing: float
    level_separation: float
    max_viewpoints: int
    eye_height: float
    directions: tuple[float, ...]
    fov: float
    resolution: int
    render_format: str
    render_quality: int
    expected_signals: tuple[str, ...]

    @property
    def key(self) -> str:
        return f"{self.tile_id}--{self.state_id}"

    @property
    def size(self) -> float:
        return self.bounds[3] - self.bounds[0]


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise LocationDatabaseError(f"Unable to read JSON {path}: {exc}") from exc


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
        prefix=f".{path.name}.",
    ) as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
        prefix=f".{path.name}.",
    ) as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            count += 1
        temporary = Path(handle.name)
    os.replace(temporary, path)
    return count


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path, block_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(block_size):
            digest.update(chunk)
    return digest.hexdigest()


@functools.lru_cache(maxsize=None)
def file_identity(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path.resolve()),
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "sha256": sha256_file(path),
    }


def directory_inventory_identity(
    root: Path, *, suffixes: Sequence[str] = ()
) -> dict[str, Any]:
    """Return a compact identity for a potentially large immutable input tree."""

    resolved = root.resolve()
    if not resolved.is_dir():
        return {"path": str(resolved), "exists": False}
    normalized_suffixes = tuple(suffix.casefold() for suffix in suffixes)
    files = sorted(
        (
            path
            for path in resolved.rglob("*")
            if path.is_file()
            and (
                not normalized_suffixes
                or path.name.casefold().endswith(normalized_suffixes)
            )
        ),
        key=lambda path: path.relative_to(resolved).as_posix().casefold(),
    )
    digest = hashlib.sha256()
    total_size = 0
    max_mtime_ns = 0
    for path in files:
        stat = path.stat()
        total_size += stat.st_size
        max_mtime_ns = max(max_mtime_ns, stat.st_mtime_ns)
        relative = path.relative_to(resolved).as_posix().casefold()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(stat.st_size).encode("ascii"))
        digest.update(b"\0")
        digest.update(str(stat.st_mtime_ns).encode("ascii"))
        digest.update(b"\n")
    return {
        "path": str(resolved),
        "exists": True,
        "file_count": len(files),
        "total_size": total_size,
        "max_mtime_ns": max_mtime_ns,
        "inventory_sha256": digest.hexdigest(),
    }


def pipeline_identity() -> dict[str, Any]:
    source_names = (
        "world_location_database.py",
        "world_location_dependencies.py",
        "world_location_nav.py",
        "world_location_render_blender.py",
        "world_location_spatial.py",
        "world_location_world.py",
    )
    return {
        "version": PIPELINE_VERSION,
        "sources": [file_identity(ROOT / "tools" / name) for name in source_names],
    }


def merged(defaults: dict[str, Any], *overrides: dict[str, Any]) -> dict[str, Any]:
    result = dict(defaults)
    for override in overrides:
        for key, value in override.items():
            if key == "variant_policy" and isinstance(value, dict):
                result[key] = {**result.get(key, {}), **value}
            else:
                result[key] = value
    return result


def tile_bounds(
    tile: dict[str, Any],
) -> tuple[float, float, float, float, float, float]:
    anchor = tile["anchor"]
    size = float(tile["tile_size_metres"])
    if not 128.0 <= size <= 256.0:
        raise LocationDatabaseError(
            f"Tile {tile.get('id', '<unknown>')} has size {size}; expected 128-256 metres"
        )
    half = size / 2.0
    z_min, z_max = (float(value) for value in tile["z_range"])
    if z_min >= z_max:
        raise LocationDatabaseError(f"Invalid Z range for tile {tile.get('id')}")
    return (
        float(anchor["x"]) - half,
        float(anchor["y"]) - half,
        z_min,
        float(anchor["x"]) + half,
        float(anchor["y"]) + half,
        z_max,
    )


def load_tile_states(spec_path: Path) -> tuple[dict[str, Any], list[TileState]]:
    spec = read_json(spec_path)
    if int(spec.get("schema_version", 0)) != SCHEMA_VERSION:
        raise LocationDatabaseError(
            f"Unsupported location spec version {spec.get('schema_version')!r}"
        )
    defaults = spec.get("defaults")
    tiles = spec.get("tiles")
    if not isinstance(defaults, dict) or not isinstance(tiles, list):
        raise LocationDatabaseError(
            "Location spec requires object defaults and a tiles array"
        )
    seen_tiles: set[str] = set()
    result: list[TileState] = []
    for raw_tile in tiles:
        if not isinstance(raw_tile, dict):
            raise LocationDatabaseError("Every tile must be an object")
        tile_id = validate_path_identifier(str(raw_tile.get("id", "")), "tile id")
        if not tile_id or tile_id in seen_tiles:
            raise LocationDatabaseError(f"Missing or duplicate tile id: {tile_id!r}")
        seen_tiles.add(tile_id)
        base = merged(defaults, raw_tile)
        states = raw_tile.get("states") or [{"id": "open-world"}]
        seen_states: set[str] = set()
        for raw_state in states:
            state_id = validate_path_identifier(
                str(raw_state.get("id", "")), f"state id for {tile_id}"
            )
            if not state_id or state_id in seen_states:
                raise LocationDatabaseError(
                    f"Missing or duplicate state id for {tile_id}: {state_id!r}"
                )
            seen_states.add(state_id)
            value = merged(base, raw_state)
            anchor = value["anchor"]
            result.append(
                TileState(
                    tile_id=tile_id,
                    state_id=state_id,
                    label=str(value["label"]),
                    archetype=str(value["archetype"]),
                    district=str(value["district"]),
                    area=str(value["area"]),
                    anchor=(
                        float(anchor["x"]),
                        float(anchor["y"]),
                        float(anchor["z_hint"]),
                    ),
                    bounds=tile_bounds(value),
                    clip_margin=float(value["clip_margin_metres"]),
                    sector_categories=tuple(str(x) for x in value["sector_categories"]),
                    lod_levels=tuple(int(x) for x in value["lod_levels"]),
                    variant_policy=dict(value["variant_policy"]),
                    navigation_agent_types=tuple(
                        str(x) for x in value["navigation_agent_types"]
                    ),
                    sample_spacing=float(value["sample_spacing_metres"]),
                    level_separation=float(value["level_separation_metres"]),
                    max_viewpoints=int(value["max_viewpoints"]),
                    eye_height=float(value["eye_height_metres"]),
                    directions=tuple(float(x) for x in value["directions_degrees"]),
                    fov=float(value["horizontal_fov_degrees"]),
                    resolution=int(value["render_resolution"]),
                    render_format=str(value["render_format"]),
                    render_quality=int(value["render_quality"]),
                    expected_signals=tuple(str(x) for x in value["expected_signals"]),
                )
            )
    if len(seen_tiles) != 6:
        raise LocationDatabaseError(
            f"The proof-of-concept contract requires exactly six spatial tiles; got {len(seen_tiles)}"
        )
    return spec, result


def connect(database: Path) -> sqlite3.Connection:
    database.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    return connection


def create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS runs (
            run_id TEXT PRIMARY KEY,
            poc_id TEXT NOT NULL,
            spec_path TEXT NOT NULL,
            spec_fingerprint TEXT NOT NULL,
            created_utc TEXT NOT NULL,
            status TEXT NOT NULL,
            config_json TEXT NOT NULL,
            summary_json TEXT NOT NULL DEFAULT '{}'
        );
        CREATE TABLE IF NOT EXISTS tiles (
            tile_id TEXT PRIMARY KEY,
            label TEXT NOT NULL,
            archetype TEXT NOT NULL,
            district TEXT NOT NULL,
            area TEXT NOT NULL,
            anchor_x REAL NOT NULL,
            anchor_y REAL NOT NULL,
            anchor_z REAL NOT NULL,
            bounds_json TEXT NOT NULL,
            expected_signals_json TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS tile_states (
            state_key TEXT PRIMARY KEY,
            tile_id TEXT NOT NULL REFERENCES tiles(tile_id),
            state_id TEXT NOT NULL,
            run_id TEXT NOT NULL REFERENCES runs(run_id),
            variant_policy_json TEXT NOT NULL,
            content_fingerprint TEXT NOT NULL,
            project_path TEXT NOT NULL DEFAULT '',
            manifest_path TEXT NOT NULL DEFAULT '',
            status TEXT NOT NULL,
            error TEXT NOT NULL DEFAULT '',
            sector_count INTEGER NOT NULL DEFAULT 0,
            node_count INTEGER NOT NULL DEFAULT 0,
            instance_count INTEGER NOT NULL DEFAULT 0,
            UNIQUE(tile_id, state_id, run_id)
        );
        CREATE TABLE IF NOT EXISTS sectors (
            state_key TEXT NOT NULL REFERENCES tile_states(state_key),
            depot_path TEXT NOT NULL,
            category TEXT NOT NULL,
            level INTEGER NOT NULL,
            source_path TEXT NOT NULL DEFAULT '',
            staged_path TEXT NOT NULL DEFAULT '',
            selected_variants_json TEXT NOT NULL DEFAULT '[]',
            source_instances INTEGER NOT NULL DEFAULT 0,
            final_instances INTEGER NOT NULL DEFAULT 0,
            final_nodes INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY(state_key, depot_path)
        );
        CREATE TABLE IF NOT EXISTS navigation_islands (
            island_id TEXT PRIMARY KEY,
            state_key TEXT NOT NULL REFERENCES tile_states(state_key),
            agent_type TEXT NOT NULL,
            source_sector TEXT NOT NULL DEFAULT '',
            polygon_count INTEGER NOT NULL DEFAULT 0,
            walkable_area REAL NOT NULL DEFAULT 0,
            bounds_json TEXT NOT NULL DEFAULT '{}',
            level_key TEXT NOT NULL DEFAULT ''
        );
        CREATE TABLE IF NOT EXISTS places (
            place_id TEXT PRIMARY KEY,
            state_key TEXT NOT NULL REFERENCES tile_states(state_key),
            island_id TEXT REFERENCES navigation_islands(island_id),
            x REAL NOT NULL,
            y REAL NOT NULL,
            z REAL NOT NULL,
            yaw_degrees REAL NOT NULL DEFAULT 0,
            interior INTEGER NOT NULL DEFAULT 0,
            source TEXT NOT NULL,
            status TEXT NOT NULL,
            structural_json TEXT NOT NULL DEFAULT '{}',
            nearby_resources_json TEXT NOT NULL DEFAULT '[]',
            renderer_fingerprint TEXT NOT NULL DEFAULT '',
            vlm_tags_json TEXT NOT NULL DEFAULT '{}'
        );
        CREATE INDEX IF NOT EXISTS places_state_idx ON places(state_key);
        CREATE INDEX IF NOT EXISTS places_xyz_idx ON places(x, y, z);
        CREATE TABLE IF NOT EXISTS images (
            image_id TEXT PRIMARY KEY,
            place_id TEXT NOT NULL REFERENCES places(place_id),
            direction_degrees REAL NOT NULL,
            path TEXT NOT NULL,
            width INTEGER NOT NULL DEFAULT 0,
            height INTEGER NOT NULL DEFAULT 0,
            renderer_fingerprint TEXT NOT NULL DEFAULT '',
            content_fingerprint TEXT NOT NULL DEFAULT '',
            perceptual_hash TEXT NOT NULL DEFAULT '',
            status TEXT NOT NULL,
            diagnostics_json TEXT NOT NULL DEFAULT '{}',
            UNIQUE(place_id, direction_degrees)
        );
        CREATE TABLE IF NOT EXISTS metrics (
            state_key TEXT NOT NULL REFERENCES tile_states(state_key),
            name TEXT NOT NULL,
            value REAL NOT NULL,
            unit TEXT NOT NULL DEFAULT '',
            details_json TEXT NOT NULL DEFAULT '{}',
            PRIMARY KEY(state_key, name)
        );
        CREATE TABLE IF NOT EXISTS resources (
            state_key TEXT NOT NULL REFERENCES tile_states(state_key),
            depot_path TEXT NOT NULL,
            resource_type TEXT NOT NULL,
            node_types_json TEXT NOT NULL DEFAULT '[]',
            instance_count INTEGER NOT NULL DEFAULT 0,
            export_status TEXT NOT NULL DEFAULT 'not_requested',
            cache_fingerprint TEXT NOT NULL DEFAULT '',
            error TEXT NOT NULL DEFAULT '',
            PRIMARY KEY(state_key, depot_path)
        );
        """
    )
    connection.execute(
        "INSERT OR REPLACE INTO metadata(key, value) VALUES ('schema_version', ?)",
        (str(SCHEMA_VERSION),),
    )
    connection.commit()


def delete_state_catalog(
    connection: sqlite3.Connection, state_keys: Iterable[str]
) -> None:
    """Delete state-owned rows in foreign-key-safe order."""

    for state_key in sorted(set(state_keys)):
        connection.execute(
            "DELETE FROM images WHERE place_id IN "
            "(SELECT place_id FROM places WHERE state_key=?)",
            (state_key,),
        )
        connection.execute("DELETE FROM places WHERE state_key=?", (state_key,))
        connection.execute(
            "DELETE FROM navigation_islands WHERE state_key=?", (state_key,)
        )
        connection.execute("DELETE FROM sectors WHERE state_key=?", (state_key,))
        connection.execute("DELETE FROM resources WHERE state_key=?", (state_key,))
        connection.execute("DELETE FROM metrics WHERE state_key=?", (state_key,))
        connection.execute("DELETE FROM tile_states WHERE state_key=?", (state_key,))


def begin_run(
    connection: sqlite3.Connection,
    spec_path: Path,
    spec: dict[str, Any],
    states: Sequence[TileState],
    config: dict[str, Any],
    *,
    active_state_keys: set[str] | None = None,
) -> str:
    if active_state_keys is None:
        active_state_keys = {state.key for state in states}
    spec_fingerprint = sha256_text(canonical_json(spec))
    run_id = sha256_text(
        canonical_json(
            {
                "spec": spec_fingerprint,
                "config": config,
            }
        )
    )[:20]
    active_row = connection.execute(
        "SELECT value FROM metadata WHERE key='active_run_id'"
    ).fetchone()
    active_run_id = str(active_row[0]) if active_row else ""
    if not active_run_id:
        existing = {
            str(row[0])
            for row in connection.execute("SELECT DISTINCT run_id FROM tile_states")
        }
        if len(existing) == 1:
            active_run_id = next(iter(existing))
        elif existing:
            active_run_id = "<mixed-generations>"

    if active_run_id and active_run_id != run_id:
        delete_state_catalog(
            connection,
            (
                str(row[0])
                for row in connection.execute("SELECT state_key FROM tile_states")
            ),
        )
        connection.execute("DELETE FROM tiles")
    elif active_run_id == run_id:
        expected_state_keys = {state.key for state in states}
        obsolete = {
            str(row[0])
            for row in connection.execute("SELECT state_key FROM tile_states")
            if str(row[0]) not in expected_state_keys
        }
        delete_state_catalog(connection, obsolete)
        expected_tile_ids = {state.tile_id for state in states}
        for row in connection.execute("SELECT tile_id FROM tiles").fetchall():
            if str(row[0]) not in expected_tile_ids:
                connection.execute("DELETE FROM tiles WHERE tile_id=?", (str(row[0]),))

    connection.execute(
        """
        INSERT INTO runs(run_id, poc_id, spec_path, spec_fingerprint, created_utc,
                         status, config_json, summary_json)
        VALUES (?, ?, ?, ?, datetime('now'), 'preparing', ?, '{}')
        ON CONFLICT(run_id) DO UPDATE SET
            created_utc=datetime('now'), status='preparing', config_json=excluded.config_json
        """,
        (
            run_id,
            str(spec.get("poc_id", "")),
            str(spec_path.resolve()),
            spec_fingerprint,
            canonical_json(config),
        ),
    )
    connection.execute(
        "INSERT OR REPLACE INTO metadata(key, value) VALUES ('active_run_id', ?)",
        (run_id,),
    )
    for state in states:
        connection.execute(
            """
            INSERT INTO tiles VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(tile_id) DO UPDATE SET
                label=excluded.label, archetype=excluded.archetype,
                district=excluded.district, area=excluded.area,
                anchor_x=excluded.anchor_x, anchor_y=excluded.anchor_y,
                anchor_z=excluded.anchor_z, bounds_json=excluded.bounds_json,
                expected_signals_json=excluded.expected_signals_json
            """,
            (
                state.tile_id,
                state.label,
                state.archetype,
                state.district,
                state.area,
                *state.anchor,
                canonical_json(state.bounds),
                canonical_json(state.expected_signals),
            ),
        )
        content_fingerprint = sha256_text(
            canonical_json(
                {
                    "state": state.__dict__,
                    "spec": spec_fingerprint,
                    "run_id": run_id,
                }
            )
        )
        parameters = (
            state.key,
            state.tile_id,
            state.state_id,
            run_id,
            canonical_json(state.variant_policy),
            content_fingerprint,
        )
        if state.key in active_state_keys:
            connection.execute(
                """
                INSERT INTO tile_states(
                    state_key, tile_id, state_id, run_id, variant_policy_json,
                    content_fingerprint, status
                ) VALUES (?, ?, ?, ?, ?, ?, 'pending')
                ON CONFLICT(state_key) DO UPDATE SET
                    run_id=excluded.run_id,
                    variant_policy_json=excluded.variant_policy_json,
                    content_fingerprint=excluded.content_fingerprint,
                    status='pending', error=''
                """,
                parameters,
            )
        else:
            connection.execute(
                """
                INSERT INTO tile_states(
                    state_key, tile_id, state_id, run_id, variant_policy_json,
                    content_fingerprint, status
                ) VALUES (?, ?, ?, ?, ?, ?, 'pending')
                ON CONFLICT(state_key) DO NOTHING
                """,
                parameters,
            )
    connection.commit()
    return run_id


def json_value(value: Any) -> str:
    if isinstance(value, dict):
        candidate = value.get("$value")
        if isinstance(candidate, (str, int, float)):
            return str(candidate)
    return str(value) if isinstance(value, (str, int, float)) else ""


def walk_resources(value: Any) -> Iterator[str]:
    if isinstance(value, dict):
        depot = value.get("DepotPath")
        if depot is not None:
            path = json_value(depot)
            if path:
                yield path
        for child in value.values():
            yield from walk_resources(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_resources(child)


def scan_sector_resources(paths: Iterable[Path]) -> dict[str, Any]:
    resources: dict[str, dict[str, Any]] = {}
    node_types: collections.Counter[str] = collections.Counter()
    visual_node_definitions = 0
    visual_node_instances = 0
    for path in paths:
        root = read_json(path).get("Data", {}).get("RootChunk", {})
        nodes = root.get("nodes", [])
        node_data = root.get("nodeData", [])
        if isinstance(node_data, dict):
            node_data = node_data.get("Data", [])
        use_counts: collections.Counter[int] = collections.Counter()
        if isinstance(node_data, list):
            for record in node_data:
                if not isinstance(record, dict):
                    continue
                try:
                    use_counts[int(json_value(record.get("NodeIndex")))] += 1
                except ValueError:
                    continue
        for node_index, node in enumerate(nodes):
            data = node.get("Data", {}) if isinstance(node, dict) else {}
            node_type = str(data.get("$type", "unknown"))
            node_types[node_type] += 1
            weight = max(1, use_counts[node_index])
            if blender_node_is_visual(node) and use_counts[node_index] > 0:
                visual_node_definitions += 1
                visual_node_instances += use_counts[node_index]
            appearance = (
                json_value(data.get("meshAppearance"))
                or json_value(data.get("appearanceName"))
                or "default"
            )
            for depot_path in dict.fromkeys(walk_resources(data)):
                normalized = depot_path.replace("/", "\\").casefold()
                suffix = Path(normalized).suffix.casefold()
                row = resources.setdefault(
                    normalized,
                    {
                        "depot_path": normalized,
                        "resource_type": suffix.lstrip(".") or "unknown",
                        "node_types": set(),
                        "appearances": collections.Counter(),
                        "instance_count": 0,
                    },
                )
                row["node_types"].add(node_type)
                row["appearances"][appearance] += weight
                row["instance_count"] += weight
    serializable = []
    for row in resources.values():
        serializable.append(
            {
                **row,
                "node_types": sorted(row["node_types"]),
                "appearances": [name for name, _ in row["appearances"].most_common()],
            }
        )
    serializable.sort(key=lambda row: row["depot_path"].casefold())
    return {
        "resources": serializable,
        "node_types": dict(sorted(node_types.items())),
        "summary": {
            "resources": len(serializable),
            "meshes": sum(row["resource_type"] == "mesh" for row in serializable),
            "entities": sum(row["resource_type"] == "ent" for row in serializable),
            "appearances": sum(row["resource_type"] == "app" for row in serializable),
            "node_definitions": sum(node_types.values()),
            "visual_node_definitions": visual_node_definitions,
            "visual_node_instances": visual_node_instances,
        },
    }


def install_file(source: Path, target: Path) -> str:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        try:
            if os.path.samefile(source, target):
                return "reused"
        except OSError:
            pass
        with tempfile.NamedTemporaryFile(
            dir=target.parent,
            delete=False,
            prefix=f".{target.name}.",
        ) as handle:
            temporary = Path(handle.name)
        temporary.unlink()
        try:
            try:
                os.link(source, temporary)
            except OSError:
                shutil.copy2(source, temporary)
            os.replace(temporary, target)
        finally:
            if temporary.exists():
                temporary.unlink()
        return "replaced"
    try:
        os.link(source, target)
        return "hardlinked"
    except OSError:
        shutil.copy2(source, target)
        return "copied"


def cache_fingerprint(
    depot_path: str,
    ghostline_red: Path,
    red_schema: Path,
    game: Path,
) -> str:
    executable = game / "bin/x64/Cyberpunk2077.exe"
    return sha256_text(
        canonical_json(
            {
                "depot_path": depot_path.casefold(),
                "ghostline_red": file_identity(ghostline_red),
                "schema": file_identity(red_schema),
                "game": file_identity(executable),
                "mode": "native-all-appearance-geometry-required-material-best-effort-v3",
            }
        )
    )


def native_pbr_cache_fingerprint(
    depot_path: str,
    appearance: str,
    ghostline_red: Path,
    red_schema: Path,
    game: Path,
) -> str:
    executable = game / "bin/x64/Cyberpunk2077.exe"
    return sha256_text(
        canonical_json(
            {
                "depot_path": depot_path.casefold(),
                "appearance": appearance,
                "ghostline_red": file_identity(ghostline_red),
                "schema": file_identity(red_schema),
                "game": file_identity(executable),
                "mode": "native-pbr-selected-appearance-v3",
            }
        )
    )


def mesh_appearance_requests(
    resource_scan: Mapping[str, Any],
) -> list[tuple[str, str]]:
    requests: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    resources = resource_scan.get("resources", [])
    if not isinstance(resources, Sequence) or isinstance(resources, (str, bytes)):
        return requests
    for resource in resources:
        if not isinstance(resource, Mapping) or resource.get("resource_type") != "mesh":
            continue
        depot_path = str(resource.get("depot_path", ""))
        if not depot_path:
            continue
        raw_appearances = resource.get("appearances", [])
        appearances: list[str] = []
        if isinstance(raw_appearances, Sequence) and not isinstance(
            raw_appearances, (str, bytes)
        ):
            for value in raw_appearances:
                if value is None:
                    continue
                appearance = str(value)
                if appearance:
                    appearances.append(appearance)
        for appearance in appearances or ["default"]:
            key = (depot_path, appearance)
            if key not in seen:
                seen.add(key)
                requests.append(key)
    return requests


def prepare_native_pbr_assets(
    resource_scan: Mapping[str, Any],
    cache_root: Path,
    game: Path,
    ghostline_red: Path,
    red_schema: Path,
    archives_root: Path,
    material_repo: Path,
    threads: int,
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    pbr_cache = cache_root / "pbr-meshes"
    pbr_cache.mkdir(parents=True, exist_ok=True)
    descriptors: dict[tuple[str, str], dict[str, Any]] = {}
    jobs: list[dict[str, str]] = []
    for depot_path, appearance in mesh_appearance_requests(resource_scan):
        fingerprint = native_pbr_cache_fingerprint(
            depot_path,
            appearance,
            ghostline_red,
            red_schema,
            game,
        )
        cache_dir = pbr_cache / fingerprint
        glb = cache_dir / "asset.glb"
        material_json = cache_dir / "asset.Material.json"
        manifest = cache_dir / "manifest.json"
        asset = {
            "depot_path": depot_path,
            "appearance": appearance,
            "glb": str(glb.resolve()),
            "material_json": str(material_json.resolve()),
            "fingerprint": fingerprint,
        }
        cached = glb.is_file() and material_json.is_file() and manifest.is_file()
        descriptors[(depot_path, appearance)] = {
            "asset": asset,
            "glb": glb,
            "material_json": material_json,
            "manifest": manifest,
            "cached": cached,
        }
        if cached:
            continue
        cache_dir.mkdir(parents=True, exist_ok=True)
        manifest.unlink(missing_ok=True)
        jobs.append(
            {
                "mesh": depot_path,
                "appearance": appearance,
                "output": str(glb.resolve()),
            }
        )

    outcome_map: dict[tuple[str, str], dict[str, Any]] = {}
    batch_error = ""
    return_code: int | None = None
    if jobs:
        batch_dir = cache_root / "jobs"
        batch_dir.mkdir(parents=True, exist_ok=True)
        batch_fingerprint = sha256_text(canonical_json(jobs))[:20]
        manifest_path = batch_dir / f"pbr-meshes-{batch_fingerprint}.json"
        report_path = batch_dir / f"pbr-meshes-{batch_fingerprint}-report.json"
        for job in jobs:
            output = Path(job["output"])
            output.unlink(missing_ok=True)
            output.with_suffix(".Material.json").unlink(missing_ok=True)
        report_path.unlink(missing_ok=True)
        write_json(manifest_path, {"jobs": jobs})
        command = [
            str(ghostline_red),
            "--kraken",
            str(DEFAULT_KRAKEN),
            "mesh-export-batch",
            str(manifest_path),
            "--schema",
            str(red_schema),
            "--archives-root",
            str(archives_root),
            "--material-repo",
            str(material_repo),
            "--report",
            str(report_path),
            "--pbr",
            "--pbr-size",
            "512",
            "--threads",
            str(max(1, threads)),
        ]
        try:
            completed = subprocess.run(command, cwd=ROOT, text=True)
            return_code = completed.returncode
        except OSError as exc:
            batch_error = f"native PBR batch could not start: {exc}"
        if not batch_error:
            if not report_path.is_file():
                batch_error = (
                    "ghostline-red did not write the native PBR batch report "
                    f"{report_path} (exit {return_code})"
                )
            else:
                try:
                    raw_outcomes = read_json(report_path)
                except LocationDatabaseError as exc:
                    batch_error = str(exc)
                else:
                    if not isinstance(raw_outcomes, list):
                        batch_error = (
                            "ghostline-red native PBR batch report must be an array: "
                            f"{report_path}"
                        )
                    else:
                        for outcome in raw_outcomes:
                            if not isinstance(outcome, Mapping):
                                continue
                            key = (
                                str(outcome.get("mesh", "")),
                                str(outcome.get("appearance", "")),
                            )
                            if key in descriptors:
                                outcome_map[key] = dict(outcome)

    assets: list[dict[str, Any]] = []
    failures: list[dict[str, str]] = []
    scheduled = {
        (str(job["mesh"]), str(job["appearance"])) for job in jobs
    }
    for key, descriptor in descriptors.items():
        asset = descriptor["asset"]
        if descriptor["cached"]:
            assets.append(asset)
            continue
        outcome = outcome_map.get(key)
        error = batch_error
        if not error and key in scheduled and outcome is None:
            error = (
                "native PBR batch report omitted this mesh appearance "
                f"(exit {return_code})"
            )
        if not error and outcome is not None:
            error = str(outcome.get("error") or "")
        if not error and not descriptor["glb"].is_file():
            error = "native PBR exporter did not create a GLB"
        if not error and not descriptor["material_json"].is_file():
            error = "native PBR exporter did not create a material sidecar"
        if error:
            failures.append(
                {
                    "depot_path": key[0],
                    "appearance": key[1],
                    "error": error,
                }
            )
            continue
        try:
            write_json(
                descriptor["manifest"],
                {
                    "schema_version": 1,
                    **asset,
                    "material_repo": str(material_repo.resolve()),
                    "exporter": "ghostline-red mesh-export-batch",
                    "pbr_baked": True,
                    "pbr_size": 512,
                },
            )
        except OSError as exc:
            failures.append(
                {
                    "depot_path": key[0],
                    "appearance": key[1],
                    "error": f"could not write native PBR cache manifest: {exc}",
                }
            )
            continue
        assets.append(asset)
    return assets, failures


def prepare_mesh_assets(
    resource_scan: dict[str, Any],
    project_raw: Path,
    cache_root: Path,
    game: Path,
    ghostline_red: Path,
    red_schema: Path,
    threads: int,
) -> dict[str, Any]:
    for required in (ghostline_red, red_schema, game / "bin/x64/Cyberpunk2077.exe"):
        if not required.is_file():
            raise LocationDatabaseError(
                f"Required mesh export input is missing: {required}"
            )
    archives_root = game / "archive/pc"
    if not archives_root.is_dir():
        raise LocationDatabaseError(f"Game archive root is missing: {archives_root}")
    mesh_cache = cache_root / "meshes"
    material_repo = cache_root / "material-repo"
    mesh_cache.mkdir(parents=True, exist_ok=True)
    material_repo.mkdir(parents=True, exist_ok=True)
    descriptors: dict[str, dict[str, Any]] = {}
    jobs: list[dict[str, str]] = []
    for resource in resource_scan["resources"]:
        if resource["resource_type"] != "mesh":
            continue
        depot_path = resource["depot_path"]
        fingerprint = cache_fingerprint(depot_path, ghostline_red, red_schema, game)
        cache_dir = mesh_cache / fingerprint
        glb = cache_dir / "asset.glb"
        material_json = cache_dir / "asset.Material.json"
        manifest = cache_dir / "manifest.json"
        descriptors[depot_path] = {
            "fingerprint": fingerprint,
            "glb": glb,
            "material_json": material_json,
            "manifest": manifest,
            "resource": resource,
            "cached_record": {},
        }
        if glb.is_file() and manifest.is_file():
            try:
                cached_record = read_json(manifest)
            except LocationDatabaseError:
                cached_record = {}
            material_status = cached_record.get("material_status")
            if material_status == "unavailable" or material_json.is_file():
                descriptors[depot_path]["cached_record"] = cached_record
                continue
        cache_dir.mkdir(parents=True, exist_ok=True)
        jobs.append(
            {
                "mesh": depot_path,
                "output": str(glb.resolve()),
            }
        )

    outcomes: dict[str, dict[str, Any]] = {}
    command: list[str] = []
    if jobs:
        batch_dir = cache_root / "jobs"
        batch_dir.mkdir(parents=True, exist_ok=True)
        batch_fingerprint = sha256_text(canonical_json(jobs))[:20]
        manifest_path = batch_dir / f"meshes-{batch_fingerprint}.json"
        report_path = batch_dir / f"meshes-{batch_fingerprint}-report.json"
        for job in jobs:
            output = Path(job["output"])
            output.unlink(missing_ok=True)
            output.with_suffix(".Material.json").unlink(missing_ok=True)
        report_path.unlink(missing_ok=True)
        write_json(manifest_path, {"jobs": jobs})
        command = [
            str(ghostline_red),
            "--kraken",
            str(DEFAULT_KRAKEN),
            "mesh-export-batch",
            str(manifest_path),
            "--schema",
            str(red_schema),
            "--archives-root",
            str(archives_root),
            "--material-repo",
            str(material_repo),
            "--report",
            str(report_path),
            "--threads",
            str(max(1, threads)),
        ]
        completed = subprocess.run(command, cwd=ROOT, text=True)
        if report_path.is_file():
            raw_outcomes = read_json(report_path)
            if not isinstance(raw_outcomes, list):
                raise LocationDatabaseError(
                    f"ghostline-red mesh batch report must be an array: {report_path}"
                )
            expected_outputs = {
                str(job["mesh"]): Path(job["output"]).resolve() for job in jobs
            }
            for outcome in raw_outcomes:
                if not isinstance(outcome, dict):
                    raise LocationDatabaseError(
                        f"ghostline-red mesh batch report contains a non-object: {report_path}"
                    )
                mesh = str(outcome.get("mesh", ""))
                if mesh not in expected_outputs:
                    raise LocationDatabaseError(
                        f"ghostline-red mesh batch reported unexpected resource: {mesh!r}"
                    )
                if mesh in outcomes:
                    raise LocationDatabaseError(
                        f"ghostline-red mesh batch duplicated resource: {mesh!r}"
                    )
                reported_output = Path(str(outcome.get("output", ""))).resolve()
                if reported_output != expected_outputs[mesh]:
                    raise LocationDatabaseError(
                        "ghostline-red mesh batch output mismatch for "
                        f"{mesh}: {reported_output} != {expected_outputs[mesh]}"
                    )
                outcomes[mesh] = outcome
            for mesh in sorted(expected_outputs.keys() - outcomes.keys()):
                outcomes[mesh] = {
                    "mesh": mesh,
                    "error": "native batch report omitted this mesh",
                }
        if not report_path.is_file():
            raise LocationDatabaseError(
                "ghostline-red did not write the required mesh batch report "
                f"{report_path} (exit {completed.returncode})"
            )

    installed = 0
    reused = 0
    failed: list[dict[str, str]] = []
    material_warnings: list[dict[str, str]] = []
    assets: list[dict[str, Any]] = []
    for depot_path, descriptor in descriptors.items():
        outcome = outcomes.get(depot_path, {})
        cached_record = descriptor["cached_record"]
        error = str(outcome.get("error") or "")
        glb = descriptor["glb"]
        material_json = descriptor["material_json"]
        if error or not glb.is_file():
            failed.append(
                {
                    "depot_path": depot_path,
                    "error": error or "native exporter did not create a GLB",
                }
            )
            continue
        material_error = str(
            outcome.get("material_error") or cached_record.get("material_error") or ""
        )
        if material_error and material_json.exists():
            material_json.unlink()
        if not material_json.is_file() and not material_error:
            material_error = "native exporter did not create a material sidecar"
        material_status = "complete" if material_json.is_file() else "unavailable"
        if material_error:
            material_warnings.append(
                {"depot_path": depot_path, "error": material_error}
            )
        manifest = descriptor["manifest"]
        cache_record = {
            "schema_version": 1,
            "depot_path": depot_path,
            "fingerprint": descriptor["fingerprint"],
            "glb": str(glb.resolve()),
            "material_json": (
                str(material_json.resolve()) if material_json.is_file() else ""
            ),
            "material_status": material_status,
            "material_error": material_error,
            "material_repo": str(material_repo.resolve()),
            "exporter": "ghostline-red mesh-export-batch",
            "appearances": "all",
            "pbr_baked": False,
        }
        write_json(manifest, cache_record)
        target_glb = depot_output_path(project_raw, depot_path).with_suffix(".glb")
        target_material = target_glb.with_name(f"{target_glb.stem}.Material.json")
        glb_action = install_file(glb, target_glb)
        material_action = (
            install_file(material_json, target_material)
            if material_json.is_file()
            else "not_available"
        )
        if material_action == "not_available":
            target_material.unlink(missing_ok=True)
        actions = (glb_action, material_action)
        if glb_action == "reused" and material_action in {"reused", "not_available"}:
            reused += 1
        else:
            installed += 1
        assets.append(
            {
                **cache_record,
                "staged_glb": str(target_glb.resolve()),
                "staged_material_json": (
                    str(target_material.resolve()) if material_json.is_file() else ""
                ),
                "install_actions": actions,
            }
        )
    pbr_requests = mesh_appearance_requests(resource_scan)
    try:
        pbr_assets, pbr_failures = prepare_native_pbr_assets(
            resource_scan,
            cache_root,
            game,
            ghostline_red,
            red_schema,
            archives_root,
            material_repo,
            threads,
        )
    except (KeyError, LocationDatabaseError, OSError, TypeError, ValueError) as exc:
        pbr_assets = []
        pbr_failures = [
            {
                "depot_path": depot_path,
                "appearance": appearance,
                "error": f"native PBR preparation failed: {exc}",
            }
            for depot_path, appearance in pbr_requests
        ]
    return {
        "schema_version": 1,
        "requested": len(descriptors),
        "export_jobs": len(jobs),
        "installed": installed,
        "reused": reused,
        "failed": failed,
        "material_warnings": material_warnings,
        "assets": assets,
        "pbr_assets": pbr_assets,
        "pbr_failures": pbr_failures,
        "material_repo": str(material_repo.resolve()),
        "command": command,
    }


def database_summary(connection: sqlite3.Connection) -> dict[str, Any]:
    def scalar(sql: str, parameters: Sequence[Any] = ()) -> int:
        row = connection.execute(sql, parameters).fetchone()
        return int(row[0]) if row else 0

    status_rows = connection.execute(
        "SELECT status, COUNT(*) AS count FROM tile_states GROUP BY status ORDER BY status"
    ).fetchall()
    image_status_rows = connection.execute(
        "SELECT status, COUNT(*) AS count FROM images GROUP BY status ORDER BY status"
    ).fetchall()
    return {
        "spatial_tiles": scalar("SELECT COUNT(*) FROM tiles"),
        "tile_states": scalar("SELECT COUNT(*) FROM tile_states"),
        "state_statuses": {row["status"]: row["count"] for row in status_rows},
        "sectors": scalar("SELECT COUNT(*) FROM sectors"),
        "navigation_islands": scalar("SELECT COUNT(*) FROM navigation_islands"),
        "places": scalar("SELECT COUNT(*) FROM places"),
        "fallback_places": scalar(
            "SELECT COUNT(*) FROM places WHERE source != 'navigation'"
        ),
        "images": scalar("SELECT COUNT(*) FROM images"),
        "image_statuses": {row["status"]: row["count"] for row in image_status_rows},
        "resources": scalar("SELECT COUNT(*) FROM resources"),
        "mesh_resources": scalar(
            "SELECT COUNT(*) FROM resources WHERE resource_type = 'mesh'"
        ),
        "entity_resources": scalar(
            "SELECT COUNT(*) FROM resources WHERE resource_type = 'ent'"
        ),
        "appearance_resources": scalar(
            "SELECT COUNT(*) FROM resources WHERE resource_type = 'app'"
        ),
        "failed_resources": scalar(
            "SELECT COUNT(*) FROM resources WHERE export_status = 'failed'"
        ),
        "material_warning_resources": scalar(
            """SELECT COUNT(*) FROM resources
               WHERE resource_type = 'mesh' AND export_status = 'complete'
                 AND error != ''"""
        ),
        "unexported_mesh_resources": scalar(
            """SELECT COUNT(*) FROM resources
               WHERE resource_type = 'mesh' AND export_status != 'complete'"""
        ),
        "unstaged_entity_dependencies": scalar(
            """SELECT COUNT(*) FROM resources
               WHERE resource_type IN ('ent', 'app')
                 AND export_status != 'not_applicable'
                 AND export_status != 'complete'"""
        ),
    }


def location_rows(
    connection: sqlite3.Connection,
    query: str = "",
    *,
    archetype: str = "",
    district: str = "",
    limit: int | None = 50,
) -> list[dict[str, Any]]:
    clauses: list[str] = []
    parameters: list[Any] = []
    if query:
        clauses.append(
            """lower(
                t.label || ' ' || t.district || ' ' || t.area || ' ' ||
                t.archetype || ' ' || t.expected_signals_json || ' ' ||
                p.structural_json || ' ' || p.nearby_resources_json || ' ' ||
                p.vlm_tags_json
            ) LIKE ?"""
        )
        parameters.append(f"%{query.casefold()}%")
    if archetype:
        clauses.append("t.archetype = ?")
        parameters.append(archetype)
    if district:
        clauses.append("lower(t.district) = ?")
        parameters.append(district.casefold())
    where = "WHERE " + " AND ".join(clauses) if clauses else ""
    limit_clause = ""
    if limit is not None:
        parameters.append(max(1, min(int(limit), 1000)))
        limit_clause = "LIMIT ?"
    rows = connection.execute(
        f"""
        SELECT p.*, ts.state_id, t.tile_id, t.label, t.archetype,
               t.district, t.area, t.expected_signals_json,
               ni.walkable_area, ni.polygon_count, ni.bounds_json AS island_bounds_json
        FROM places p
        JOIN tile_states ts ON ts.state_key = p.state_key
        JOIN tiles t ON t.tile_id = ts.tile_id
        LEFT JOIN navigation_islands ni ON ni.island_id = p.island_id
        {where}
        ORDER BY t.tile_id, ts.state_id, p.place_id
        {limit_clause}
        """,
        parameters,
    ).fetchall()
    result: list[dict[str, Any]] = []
    for row in rows:
        value = dict(row)
        for field in (
            "expected_signals_json",
            "structural_json",
            "nearby_resources_json",
            "vlm_tags_json",
            "island_bounds_json",
        ):
            encoded = value.pop(field, "")
            value[field.removesuffix("_json")] = json.loads(encoded or "{}")
        image_rows = connection.execute(
            """
            SELECT direction_degrees, path, width, height, status,
                   content_fingerprint, perceptual_hash
            FROM images WHERE place_id = ? ORDER BY direction_degrees
            """,
            (row["place_id"],),
        ).fetchall()
        value["images"] = [dict(image) for image in image_rows]
        result.append(value)
    return result


def vlm_jobs(
    database: Path, output: Path, *, include_unrendered: bool = False
) -> dict[str, Any]:
    connection = connect(database)
    create_schema(connection)
    rows = location_rows(connection, limit=None)
    connection.close()

    def jobs() -> Iterator[dict[str, Any]]:
        for row in rows:
            images = [
                image["path"]
                for image in row["images"]
                if include_unrendered or image["status"] == "complete"
            ]
            if not include_unrendered and not images:
                continue
            yield {
                "place_id": row["place_id"],
                "tile_id": row["tile_id"],
                "state_id": row["state_id"],
                "label": row["label"],
                "coordinate": {"x": row["x"], "y": row["y"], "z": row["z"]},
                "orientation_degrees": row["yaw_degrees"],
                "district": row["district"],
                "area": row["area"],
                "archetype": row["archetype"],
                "interior": bool(row["interior"]),
                "navigation_island": row["island_id"],
                "expected_signals": row["expected_signals"],
                "structural_facts": row["structural"],
                "nearby_resources": row["nearby_resources"],
                "images": images,
                "caption_schema": {
                    "atmosphere": [],
                    "architecture": [],
                    "faction_signals": [],
                    "condition": [],
                    "lighting": [],
                    "combat_suitability": [],
                    "stealth_suitability": [],
                    "quest_themes": [],
                    "recognizable_landmarks": [],
                    "confidence": 0.0,
                },
            }

    count = write_jsonl(output, jobs())
    return {"jobs": count, "output": str(output.resolve())}


VLM_TAG_FIELDS = (
    "atmosphere",
    "architecture",
    "faction_signals",
    "condition",
    "lighting",
    "combat_suitability",
    "stealth_suitability",
    "quest_themes",
    "recognizable_landmarks",
    "confidence",
)


def import_vlm_tags(database: Path, source: Path) -> dict[str, Any]:
    """Atomically ingest place-tag JSONL produced from the exported VLM jobs."""

    connection = connect(database)
    create_schema(connection)
    imported = 0
    try:
        with source.open("r", encoding="utf-8-sig") as handle:
            for line_number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                try:
                    document = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise LocationDatabaseError(
                        f"Invalid VLM JSONL at {source}:{line_number}: {exc}"
                    ) from exc
                if not isinstance(document, dict):
                    raise LocationDatabaseError(
                        f"VLM result at {source}:{line_number} must be an object"
                    )
                place_id = str(document.get("place_id", ""))
                if not place_id:
                    raise LocationDatabaseError(
                        f"VLM result at {source}:{line_number} has no place_id"
                    )
                tags_value = document.get("tags", document.get("response"))
                if isinstance(tags_value, dict):
                    tags = {
                        key: tags_value[key]
                        for key in VLM_TAG_FIELDS
                        if key in tags_value
                    }
                else:
                    tags = {
                        key: document[key] for key in VLM_TAG_FIELDS if key in document
                    }
                if not tags:
                    raise LocationDatabaseError(
                        f"VLM result at {source}:{line_number} has no recognized tag fields"
                    )
                for key, value in tags.items():
                    if key == "confidence":
                        if not isinstance(value, (int, float)) or isinstance(
                            value, bool
                        ):
                            raise LocationDatabaseError(
                                f"VLM confidence at {source}:{line_number} must be numeric"
                            )
                    elif not isinstance(value, list) or not all(
                        isinstance(item, str) for item in value
                    ):
                        raise LocationDatabaseError(
                            f"VLM tag {key!r} at {source}:{line_number} must be a string array"
                        )
                cursor = connection.execute(
                    "UPDATE places SET vlm_tags_json=? WHERE place_id=?",
                    (canonical_json(tags), place_id),
                )
                if cursor.rowcount != 1:
                    raise LocationDatabaseError(
                        f"VLM result at {source}:{line_number} references unknown place {place_id!r}"
                    )
                imported += 1
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
    return {"imported": imported, "source": str(source.resolve())}


def write_poc_report(database: Path, output: Path) -> dict[str, Any]:
    connection = connect(database)
    create_schema(connection)
    summary = database_summary(connection)
    states = [
        dict(row)
        for row in connection.execute(
            """
            SELECT ts.state_key, ts.state_id, ts.status, ts.error,
                   ts.sector_count, ts.node_count, ts.instance_count,
                   t.tile_id, t.label, t.archetype, t.district, t.area,
                   (SELECT COUNT(*) FROM places p WHERE p.state_key=ts.state_key) AS places,
                   (SELECT COUNT(*) FROM images i JOIN places p ON p.place_id=i.place_id
                    WHERE p.state_key=ts.state_key AND i.status='complete') AS images,
                   (SELECT COALESCE(SUM(value), 0) FROM metrics m
                    WHERE m.state_key=ts.state_key AND m.name='render_seconds') AS render_seconds
                   ,(SELECT COALESCE(MAX(value), 0) FROM metrics m
                     WHERE m.state_key=ts.state_key
                       AND m.name='render_directions_per_place') AS expected_directions
                   ,(SELECT COUNT(*) FROM resources r
                     WHERE r.state_key=ts.state_key
                       AND r.resource_type='mesh') AS mesh_resources
                   ,(SELECT COUNT(*) FROM resources r
                     WHERE r.state_key=ts.state_key
                       AND r.resource_type='mesh'
                       AND r.export_status='complete') AS complete_mesh_resources
                   ,(SELECT COUNT(*) FROM resources r
                     WHERE r.state_key=ts.state_key
                       AND r.resource_type='mesh'
                       AND r.export_status='complete'
                       AND r.error != '') AS material_warning_resources
                   ,(SELECT COUNT(*) FROM resources r
                     WHERE r.state_key=ts.state_key
                       AND r.resource_type IN ('ent', 'app')
                       AND r.export_status != 'not_applicable') AS dependency_resources
                   ,(SELECT COUNT(*) FROM resources r
                     WHERE r.state_key=ts.state_key
                       AND r.resource_type IN ('ent', 'app')
                       AND r.export_status='complete') AS complete_dependency_resources
                   ,(SELECT COUNT(*) FROM metrics m
                     WHERE m.state_key=ts.state_key
                       AND m.name='render_content_errors') AS render_content_checks
                   ,(SELECT COALESCE(MAX(value), 0) FROM metrics m
                     WHERE m.state_key=ts.state_key
                       AND m.name='render_content_errors') AS render_content_errors
            FROM tile_states ts JOIN tiles t ON t.tile_id=ts.tile_id
            ORDER BY t.tile_id, ts.state_id
            """
        ).fetchall()
    ]
    metrics = [
        dict(row)
        for row in connection.execute(
            "SELECT state_key, name, value, unit, details_json FROM metrics ORDER BY state_key, name"
        ).fetchall()
    ]
    connection.close()
    checks = {
        "six_spatial_tiles": summary["spatial_tiles"] == 6,
        "variant_state_exercised": summary["tile_states"] > summary["spatial_tiles"],
        "all_states_assembled": bool(states)
        and all(row["status"] not in {"pending", "failed"} for row in states),
        "all_states_have_sectors": bool(states)
        and all(row["sector_count"] > 0 for row in states),
        "all_states_have_places": bool(states)
        and all(row["places"] > 0 for row in states),
        "no_fallback_cameras": summary["fallback_places"] == 0,
        "all_expected_images_rendered": bool(states)
        and all(
            row["expected_directions"] > 0
            and row["images"] >= row["places"] * row["expected_directions"]
            for row in states
        ),
        "all_render_content_complete": bool(states)
        and all(
            row["render_content_checks"] > 0 and row["render_content_errors"] == 0
            for row in states
        ),
        "all_mesh_exports_succeeded": bool(states)
        and all(
            row["mesh_resources"] == row["complete_mesh_resources"] for row in states
        ),
        "all_entity_dependencies_staged": bool(states)
        and all(
            row["dependency_resources"] == row["complete_dependency_resources"]
            for row in states
        ),
    }
    report = {
        "schema_version": 1,
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "database": str(database.resolve()),
        "summary": summary,
        "checks": checks,
        "states": states,
        "metrics": metrics,
        "limitations": [
            "Animated advertisements, crowds, traffic, particles, fog, and REDengine lighting are not reproduced.",
            "Entity and appearance resources are staged recursively, but animated rigs, animations, dynamic device state, and runtime appearance overrides are not reproduced.",
            "Camera ray validation detects obvious invalid placements but does not reproduce runtime door state or dynamic collision.",
        ],
    }
    write_json(output, report)
    markdown = output.with_suffix(".md")
    lines = [
        "# World-location six-tile proof of concept",
        "",
        f"Generated `{report['generated_utc']}` from `{database}`.",
        "",
        "| Tile state | Status | Sectors | Nodes | Instances | Places | Images |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in states:
        lines.append(
            f"| {row['tile_id']} / {row['state_id']} | {row['status']} | "
            f"{row['sector_count']} | {row['node_count']} | {row['instance_count']} | "
            f"{row['places']} | {row['images']} |"
        )
    lines.extend(["", "## Acceptance checks", ""])
    for name, passed in checks.items():
        lines.append(f"- [{'x' if passed else ' '}] {name.replace('_', ' ')}")
    lines.extend(["", "## Known limitations", ""])
    lines.extend(f"- {item}" for item in report["limitations"])
    markdown.parent.mkdir(parents=True, exist_ok=True)
    markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    report["markdown"] = str(markdown.resolve())
    return report


def depot_relative_path(depot_path: str) -> Path:
    try:
        normalized = normalize_dependency_path(depot_path)
    except DependencyStagingError as exc:
        raise LocationDatabaseError(str(exc)) from exc
    return Path(*normalized.split("\\"))


def depot_output_path(
    root: Path, depot_path: str, *, json_sidecar: bool = False
) -> Path:
    """Resolve a depot path beneath ``root`` and prove containment."""

    resolved_root = root.resolve()
    target = resolved_root / depot_relative_path(depot_path)
    if json_sidecar:
        target = Path(str(target) + ".json")
    resolved_target = target.resolve()
    if not resolved_target.is_relative_to(resolved_root):
        raise LocationDatabaseError(
            f"Depot path escapes target root {resolved_root}: {depot_path!r}"
        )
    return resolved_target


def find_depot_file(root: Path, depot_path: str, *, json_sidecar: bool = False) -> Path:
    candidate = depot_output_path(root, depot_path, json_sidecar=json_sidecar)
    if not candidate.is_file():
        raise LocationDatabaseError(
            f"Depot resource is missing beneath {root}: {depot_path}"
        )
    return candidate


def serialize_sector_cached(
    depot_path: str,
    sectors_root: Path,
    cache_root: Path,
    ghostline_red: Path,
    red_schema: Path,
    *,
    serialized_roots: Sequence[Path] = (),
) -> tuple[Path, dict[str, Any]]:
    for root in serialized_roots:
        candidate = depot_output_path(root, depot_path, json_sidecar=True)
        if candidate.is_file():
            return candidate, {
                "source": "pre_serialized",
                "depot_path": depot_path,
                "path": str(candidate.resolve()),
                "identity": file_identity(candidate),
            }

    binary = find_depot_file(sectors_root, depot_path)
    fingerprint = sha256_text(
        canonical_json(
            {
                "binary": file_identity(binary),
                "ghostline_red": file_identity(ghostline_red),
                "schema": file_identity(red_schema),
                "mode": "cr2w-serialize-sector-v1",
            }
        )
    )
    directory = cache_root / "serialized-sectors" / fingerprint
    output = directory / (binary.name + ".json")
    manifest = directory / "manifest.json"
    if not output.is_file():
        from ghostline_red import serialize

        directory.mkdir(parents=True, exist_ok=True)
        serialize(binary, output, red_cli=ghostline_red, schema=red_schema)
    record = {
        "source": "native_cache",
        "depot_path": depot_path,
        "binary": str(binary.resolve()),
        "path": str(output.resolve()),
        "fingerprint": fingerprint,
        "identity": file_identity(output),
    }
    if not manifest.is_file():
        write_json(manifest, {"schema_version": 1, **record})
    return output, record


def navigation_documents(path: Path) -> Iterator[tuple[str, dict[str, Any]]]:
    document = read_json(path)
    embedded = document.get("Data", {}).get("EmbeddedFiles", [])
    if not isinstance(embedded, list):
        return
    for item in embedded:
        if not isinstance(item, dict) or not isinstance(item.get("Content"), dict):
            continue
        filename = json_value(item.get("FileName"))
        content = item["Content"]
        if str(content.get("$type", "")) != "worldNavigationTileResource":
            continue
        yield (
            filename,
            {
                "Header": {"ArchiveFileName": filename},
                "Data": {"RootChunk": content},
            },
        )


def embedded_render_documents(
    document: Mapping[str, Any],
) -> Iterator[tuple[str, dict[str, Any]]]:
    """Yield loose JSON documents required by the Blender sector importer.

    WolvenKit keeps compiled foliage resources embedded in a streaming sector,
    while Cyberpunk IO Suite resolves each ``foliageResource`` as a loose
    ``.cfoliage.json`` beside the staged project.  Preserve the embedded copy
    in the sector and materialize the same content at its depot path.
    """

    data = document.get("Data")
    embedded = data.get("EmbeddedFiles", []) if isinstance(data, Mapping) else []
    if not isinstance(embedded, list):
        return
    for item in embedded:
        if not isinstance(item, Mapping):
            continue
        filename = json_value(item.get("FileName"))
        content = item.get("Content")
        if not filename.casefold().endswith(".cfoliage") or not isinstance(
            content, Mapping
        ):
            continue
        yield (
            filename,
            {
                "Header": {
                    "ArchiveFileName": filename,
                    "DataType": "CR2W",
                    "ExportedDateTime": "1970-01-01T00:00:00Z",
                    "GameVersion": 2310,
                    "WKitJsonVersion": "0.0.9",
                    "WolvenKitVersion": "8.17-compatible (Ghostline embedded resource)",
                },
                "Data": {
                    "Version": 195,
                    "BuildVersion": 0,
                    "RootChunk": copy.deepcopy(content),
                },
            },
        )


def clipped_navigation_buffers(
    sector_paths: Iterable[Path],
    bounds: tuple[float, float, float, float, float, float],
    active_variant_ids: set[int],
) -> tuple[Any, ...]:
    from world_location_nav import load_navigation_sector, vand_position_to_world

    min_x, min_y, min_z, max_x, max_y, max_z = bounds
    buffers: list[Any] = []
    for sector_path in sector_paths:
        for resource_path, document in navigation_documents(sector_path):
            sector = load_navigation_sector(
                document,
                source_id=resource_path,
                human_only=True,
            )
            for buffer in sector.buffers:
                required = set(buffer.source.active_variant_ids)
                if required and not required.issubset(active_variant_ids):
                    continue
                # VAND stores positions as X/Z/Y while streaming-sector bounds
                # and every database record use RED world X/Y/Z.
                buffer = replace(
                    buffer,
                    vertices=tuple(
                        vand_position_to_world(vertex) for vertex in buffer.vertices
                    ),
                )
                faces = []
                for face in buffer.faces:
                    vertices = buffer.face_vertices(face)
                    if (
                        max(vertex.x for vertex in vertices) < min_x
                        or min(vertex.x for vertex in vertices) > max_x
                        or max(vertex.y for vertex in vertices) < min_y
                        or min(vertex.y for vertex in vertices) > max_y
                        or max(vertex.z for vertex in vertices) < min_z
                        or min(vertex.z for vertex in vertices) > max_z
                    ):
                        continue
                    faces.append(face)
                if faces:
                    buffers.append(replace(buffer, faces=tuple(faces)))
    return tuple(buffers)


def select_navigation_samples(
    samples: Sequence[Any],
    islands: Sequence[Any],
    state: TileState,
    placements: Sequence[dict[str, Any]],
) -> list[Any]:
    min_x, min_y, min_z, max_x, max_y, max_z = state.bounds
    minimum_local_width = 0.75 if state.archetype == "multilevel_interior" else 1.25
    preserve_vertical_levels = state.archetype in {"elevated_road", "multilevel_interior"}

    candidates = [
        sample
        for sample in samples
        if min_x <= sample.surface_position.x <= max_x
        and min_y <= sample.surface_position.y <= max_y
        and min_z <= sample.surface_position.z <= max_z
        and sample.local_width_m >= minimum_local_width
        and (preserve_vertical_levels or abs(sample.surface_position.z - state.anchor[2]) <= 4.0)
    ]
    if not candidates:
        return []
    island_by_id = {island.island_id: island for island in islands}

    def anchor_distance(sample: Any) -> float:
        dx = sample.surface_position.x - state.anchor[0]
        dy = sample.surface_position.y - state.anchor[1]
        dz = sample.surface_position.z - state.anchor[2]
        return math.sqrt(dx * dx + dy * dy + 16.0 * dz * dz)

    candidates.sort(
        key=lambda sample: (
            anchor_distance(sample),
            sample.island_id,
            sample.sample_index,
        )
    )
    chosen = [candidates.pop(0)]
    nearby_candidates = [
        sample
        for sample in candidates
        if math.hypot(
            sample.surface_position.x - state.anchor[0],
            sample.surface_position.y - state.anchor[1],
        )
        <= 35.0
    ]
    if nearby_candidates:
        candidates = nearby_candidates
    placement_density: dict[int, float] = {}
    for sample in candidates:
        sx = sample.surface_position.x
        sy = sample.surface_position.y
        sz = sample.surface_position.z
        density = 0.0
        for placement in placements:
            px, py, pz = placement["position"]
            if abs(pz - sz) > 10.0:
                continue
            distance_squared = (px - sx) ** 2 + (py - sy) ** 2
            if distance_squared <= 45.0**2:
                density += 1.0 / (1.0 + distance_squared / 144.0)
        placement_density[id(sample)] = density
    prioritize_levels = state.archetype in {"elevated_road", "multilevel_interior"}
    while candidates and len(chosen) < state.max_viewpoints:
        selected_levels = {
            round(sample.surface_position.z / state.level_separation)
            for sample in chosen
        }
        selected_islands = {sample.island_id for sample in chosen}

        def diversity(sample: Any) -> tuple[float, float, str, int]:
            nearest = min(
                math.sqrt(
                    (sample.surface_position.x - other.surface_position.x) ** 2
                    + (sample.surface_position.y - other.surface_position.y) ** 2
                    + 9.0 * (sample.surface_position.z - other.surface_position.z) ** 2
                )
                for other in chosen
            )
            level = round(sample.surface_position.z / state.level_separation)
            level_bonus = (
                1000.0 if prioritize_levels and level not in selected_levels else 0.0
            )
            island_bonus = 200.0 if sample.island_id not in selected_islands else 0.0
            island_area = island_by_id[sample.island_id].metrics.surface_area_m2
            score = (
                level_bonus
                + island_bonus
                + min(nearest, 24.0)
                + min(25.0, math.log1p(placement_density.get(id(sample), 0.0)) * 8.0)
                + min(100.0, island_area / 25.0)
            )
            score -= anchor_distance(sample) * 0.02
            return (
                score,
                -anchor_distance(sample),
                sample.island_id,
                -sample.sample_index,
            )

        best = max(candidates, key=diversity)
        chosen.append(best)
        candidates.remove(best)
    return chosen


def sample_yaw(sample: Any, island: Any, state: TileState) -> float:
    if state.archetype == "building_exterior":
        return (
            math.degrees(
                math.atan2(
                    state.anchor[1] - sample.surface_position.y,
                    state.anchor[0] - sample.surface_position.x,
                )
            )
            % 360.0
        )
    x_extent = island.bounds.maximum.x - island.bounds.minimum.x
    y_extent = island.bounds.maximum.y - island.bounds.minimum.y
    return 0.0 if x_extent >= y_extent else 90.0


def staged_placements(paths: Iterable[Path]) -> list[dict[str, Any]]:
    placements: list[dict[str, Any]] = []
    for path in paths:
        root = read_json(path).get("Data", {}).get("RootChunk", {})
        nodes = root.get("nodes", [])
        records = root.get("nodeData", [])
        if isinstance(records, dict):
            records = records.get("Data", [])
        if not isinstance(nodes, list) or not isinstance(records, list):
            continue
        for record in records:
            if not isinstance(record, dict):
                continue
            position = record.get("Position")
            if not isinstance(position, dict):
                continue
            try:
                node_index = int(json_value(record.get("NodeIndex")))
                node = nodes[node_index]
                data = node.get("Data", {})
                point = (
                    float(json_value(position.get("X"))),
                    float(json_value(position.get("Y"))),
                    float(json_value(position.get("Z"))),
                )
            except (ValueError, IndexError, TypeError):
                continue
            placements.append(
                {
                    "position": point,
                    "node_type": str(data.get("$type", "unknown")),
                    "debug_name": json_value(data.get("debugName")),
                    "resources": sorted(set(walk_resources(data))),
                    "sector": str(path),
                }
            )
    return placements


def nearby_placements(
    placements: Sequence[dict[str, Any]],
    point: tuple[float, float, float],
    *,
    radius: float = 40.0,
    limit: int = 30,
) -> list[dict[str, Any]]:
    found: list[tuple[float, dict[str, Any]]] = []
    for placement in placements:
        x, y, z = placement["position"]
        distance = math.sqrt(
            (x - point[0]) ** 2 + (y - point[1]) ** 2 + (z - point[2]) ** 2
        )
        if distance <= radius:
            found.append((distance, placement))
    found.sort(
        key=lambda item: (
            item[0],
            item[1]["node_type"],
            item[1]["debug_name"],
        )
    )
    return [
        {
            "distance_metres": round(distance, 3),
            "node_type": placement["node_type"],
            "debug_name": placement["debug_name"],
            "resources": placement["resources"],
        }
        for distance, placement in found[:limit]
    ]


def merge_resource_scans(scans: Iterable[dict[str, Any]]) -> dict[str, Any]:
    resources: dict[str, dict[str, Any]] = {}
    node_types: collections.Counter[str] = collections.Counter()
    for scan in scans:
        node_types.update(scan.get("node_types", {}))
        for row in scan.get("resources", []):
            depot_path = str(row["depot_path"]).replace("/", "\\").casefold()
            current = resources.setdefault(
                depot_path,
                {
                    "depot_path": depot_path,
                    "resource_type": row["resource_type"],
                    "node_types": set(),
                    "appearances": [],
                    "instance_count": 0,
                },
            )
            current["node_types"].update(row.get("node_types", []))
            current["instance_count"] += int(row.get("instance_count", 0))
            for appearance in row.get("appearances", []):
                if appearance not in current["appearances"]:
                    current["appearances"].append(appearance)
    rows = []
    for row in resources.values():
        rows.append({**row, "node_types": sorted(row["node_types"])})
    rows.sort(key=lambda row: row["depot_path"].casefold())
    return {
        "resources": rows,
        "node_types": dict(sorted(node_types.items())),
        "summary": {
            "resources": len(rows),
            "meshes": sum(row["resource_type"] == "mesh" for row in rows),
            "entities": sum(row["resource_type"] == "ent" for row in rows),
            "appearances": sum(row["resource_type"] == "app" for row in rows),
            "node_definitions": sum(node_types.values()),
        },
    }


def augment_resource_scan(
    scan: dict[str, Any], dependency_resources: Iterable[dict[str, Any]]
) -> dict[str, Any]:
    """Add an archive dependency closure without inflating placement counts."""

    dependency_rows = []
    for resource in dependency_resources:
        depot_path = str(resource.get("resource", ""))
        resource_type = str(resource.get("resource_type", "unknown"))
        if not depot_path:
            continue
        dependency_rows.append(
            {
                "depot_path": depot_path,
                "resource_type": resource_type,
                "node_types": ["archive_dependency"],
                "appearances": [],
                "instance_count": 0,
            }
        )
    return merge_resource_scans(
        (
            scan,
            {
                "resources": dependency_rows,
                "node_types": {},
            },
        )
    )


def requires_render_dependency(resource: dict[str, Any]) -> bool:
    """Return whether an archive resource can contribute catalog geometry."""

    if resource.get("resource_type") != "ent":
        return True
    path = str(resource.get("depot_path", "")).replace("/", "\\").casefold()
    name = path.rsplit("\\", 1)[-1]
    return not ("\\communities\\" in path and "spawner" in name)


def directory_size(path: Path) -> int:
    total = 0
    if not path.is_dir():
        return total
    for root, _directories, filenames in os.walk(path):
        root_path = Path(root)
        for filename in filenames:
            try:
                total += (root_path / filename).stat().st_size
            except OSError:
                continue
    return total


def selector_for_state(index: Any, state: TileState) -> Any:
    from world_location_world import WorldLocationWorldError, WorldStateSelector

    mode = str(state.variant_policy.get("mode", "defaults")).casefold()
    if mode in {"default", "defaults", "open-world", "open_world"}:
        return WorldStateSelector.defaults(index)
    if mode != "explicit":
        raise LocationDatabaseError(
            f"Unknown variant policy mode for {state.key}: {mode!r}"
        )
    names = {
        str(name).casefold() for name in state.variant_policy.get("names", []) if name
    }
    selected = [
        group.key
        for group in index.variant_groups
        if group.key.name.casefold() in names
    ]
    found_names = {key.name.casefold() for key in selected}
    missing = sorted(names - found_names)
    if missing:
        raise LocationDatabaseError(
            f"State {state.key} requests unknown variants: {', '.join(missing)}"
        )
    try:
        return WorldStateSelector(
            index,
            selected,
            include_enabled_defaults=bool(
                state.variant_policy.get("include_enabled_defaults", True)
            ),
        )
    except WorldLocationWorldError as exc:
        raise LocationDatabaseError(
            f"Invalid variant state {state.key}: {exc}"
        ) from exc


def state_job(
    state: TileState,
    context: dict[str, Any],
    output_root: Path,
    *,
    run_id: str = "",
) -> dict[str, Any]:
    viewpoints = []
    for place in context["places"]:
        viewpoints.append(
            {
                "id": place["place_id"],
                "surface_position": [place["x"], place["y"], place["z"]],
                "eye_height": state.eye_height,
                "yaw_degrees": place["yaw_degrees"],
                "directions": list(state.directions),
                "horizontal_fov_degrees": state.fov,
                "metadata": {
                    "navigation_island": place.get("island_id"),
                    "source": place["source"],
                    "structural": place["structural"],
                },
            }
        )
    dependency_resources = context.get("dependency_report", {}).get("resources")
    if isinstance(dependency_resources, list):
        expected_entities = sum(
            row.get("resource_type") == "ent" for row in dependency_resources
        )
        expected_appearances = sum(
            row.get("resource_type") == "app" for row in dependency_resources
        )
    else:
        expected_entities = context["resource_scan"]["summary"].get("entities", 0)
        expected_appearances = context["resource_scan"]["summary"].get("appearances", 0)
    return {
        "tile_id": state.key,
        "run_id": run_id,
        "state_id": state.state_id,
        "project": str(context["project_root"].resolve()),
        "output": str((output_root / "renders" / state.key).resolve()),
        "content_fingerprint": context["content_fingerprint"],
        "native_pbr_assets": [
            dict(row)
            for row in context.get("asset_report", {}).get("pbr_assets", [])
        ],
        "tile_bounds": list(state.bounds),
        "contributing_sectors": [
            row["depot_path"]
            for row in context["sector_rows"]
            if row.get("retained_instance_count", 0) > 0
        ],
        "viewpoints": viewpoints,
        "resolution": state.resolution,
        "image_format": state.render_format,
        "image_quality": state.render_quality,
        "horizontal_fov_degrees": state.fov,
        "with_static_lights": False,
        "expected_content": {
            "sector_jsons": sum(
                row.get("retained_instance_count", 0) > 0
                for row in context["sector_rows"]
            ),
            "mesh_glbs": context["resource_scan"]["summary"]["meshes"],
            "imported_mesh_glbs": context.get(
                "direct_resource_summary", context["resource_scan"]["summary"]
            )["meshes"],
            "entity_jsons": expected_entities,
            "appearance_jsons": expected_appearances,
            "node_definitions": context["resource_scan"]["summary"].get(
                "visual_node_definitions", 0
            ),
            "node_instances": context["resource_scan"]["summary"].get(
                "visual_node_instances", 0
            ),
        },
        "catalog_content": {
            "node_definitions": context["resource_scan"]["summary"]["node_definitions"],
            "visual_node_definitions": context["resource_scan"]["summary"].get(
                "visual_node_definitions", 0
            ),
            "visual_node_instances": context["resource_scan"]["summary"].get(
                "visual_node_instances", 0
            ),
        },
    }


def set_metric(
    connection: sqlite3.Connection,
    state_key: str,
    name: str,
    value: float,
    unit: str = "",
    details: dict[str, Any] | None = None,
) -> None:
    connection.execute(
        """
        INSERT INTO metrics VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(state_key, name) DO UPDATE SET
            value=excluded.value, unit=excluded.unit, details_json=excluded.details_json
        """,
        (state_key, name, float(value), unit, canonical_json(details or {})),
    )


def store_state_context(
    connection: sqlite3.Connection,
    state: TileState,
    context: dict[str, Any],
) -> None:
    connection.execute("DELETE FROM sectors WHERE state_key = ?", (state.key,))
    for row in context["sector_rows"]:
        connection.execute(
            """
            INSERT INTO sectors VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                state.key,
                row["depot_path"],
                row["category"],
                int(row["level"]),
                row.get("source_sector_path", ""),
                row.get("staged_path", ""),
                canonical_json(row.get("active_variants", [])),
                int(row.get("source_instance_count", 0)),
                int(row.get("retained_instance_count", 0)),
                int(row.get("retained_node_count", 0)),
            ),
        )

    connection.execute("DELETE FROM resources WHERE state_key = ?", (state.key,))
    asset_by_path = {
        row["depot_path"]: row
        for row in context.get("asset_report", {}).get("assets", [])
    }
    failure_by_path = {
        row["depot_path"]: row
        for row in context.get("asset_report", {}).get("failed", [])
    }
    dependency_by_path = {
        str(row["resource"]).casefold(): row
        for row in context.get("dependency_report", {}).get("resources", [])
    }
    installed_dependencies = {
        str(row["resource"]).casefold(): row
        for row in context.get("dependency_report", {}).get("installed", [])
    }
    ignored_dependencies = {
        str(path).casefold() for path in context.get("ignored_dependency_resources", [])
    }
    for resource in context["resource_scan"]["resources"]:
        exported = asset_by_path.get(resource["depot_path"])
        failure = failure_by_path.get(resource["depot_path"])
        status = "not_applicable"
        fingerprint = ""
        error = ""
        if resource["resource_type"] == "mesh":
            if exported:
                status = "complete"
                fingerprint = exported["fingerprint"]
                error = str(exported.get("material_error", ""))
            elif failure:
                status = "failed"
                error = failure["error"]
            else:
                status = context.get("asset_status", "not_requested")
        elif resource["resource_type"] in {"ent", "app"}:
            depot_key = resource["depot_path"].casefold()
            dependency = dependency_by_path.get(depot_key)
            installed = installed_dependencies.get(depot_key)
            if installed and dependency and dependency.get("status") == "ready":
                status = "complete"
                fingerprint = str(dependency.get("cache_fingerprint", ""))
            elif dependency:
                status = "failed"
                error = str(
                    dependency.get("error")
                    or "archive dependency JSON was not installed"
                )
            elif depot_key in ignored_dependencies:
                status = "not_applicable"
            else:
                status = "not_requested"
        connection.execute(
            "INSERT INTO resources VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                state.key,
                resource["depot_path"],
                resource["resource_type"],
                canonical_json(resource.get("node_types", [])),
                int(resource.get("instance_count", 0)),
                status,
                fingerprint,
                error,
            ),
        )

    connection.execute(
        "DELETE FROM images WHERE place_id IN (SELECT place_id FROM places WHERE state_key = ?)",
        (state.key,),
    )
    connection.execute("DELETE FROM places WHERE state_key = ?", (state.key,))
    connection.execute(
        "DELETE FROM navigation_islands WHERE state_key = ?", (state.key,)
    )
    for island in context["islands"]:
        connection.execute(
            "INSERT INTO navigation_islands VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                island["island_id"],
                state.key,
                island["agent_type"],
                island["source_sector"],
                island["polygon_count"],
                island["walkable_area"],
                canonical_json(island["bounds"]),
                island["level_key"],
            ),
        )
    for place in context["places"]:
        connection.execute(
            """
            INSERT INTO places(
                place_id, state_key, island_id, x, y, z, yaw_degrees, interior,
                source, status, structural_json, nearby_resources_json,
                renderer_fingerprint, vlm_tags_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '', '{}')
            """,
            (
                place["place_id"],
                state.key,
                place.get("island_id"),
                place["x"],
                place["y"],
                place["z"],
                place["yaw_degrees"],
                int(place["interior"]),
                place["source"],
                place["status"],
                canonical_json(place["structural"]),
                canonical_json(place["nearby_resources"]),
            ),
        )

    retained = [
        row
        for row in context["sector_rows"]
        if row.get("retained_instance_count", 0) > 0
    ]
    connection.execute(
        """
        UPDATE tile_states SET project_path=?, manifest_path=?, status=?, error=?,
            content_fingerprint=?,
            sector_count=?, node_count=?, instance_count=?
        WHERE state_key=?
        """,
        (
            str(context["project_root"].resolve()),
            str(context["manifest_path"].resolve()),
            context["status"],
            context.get("error", ""),
            context["content_fingerprint"],
            len(retained),
            sum(int(row.get("retained_node_count", 0)) for row in retained),
            sum(int(row.get("retained_instance_count", 0)) for row in retained),
            state.key,
        ),
    )
    connection.execute("DELETE FROM metrics WHERE state_key = ?", (state.key,))
    for name, metric in context.get("metrics", {}).items():
        set_metric(
            connection,
            state.key,
            name,
            metric["value"],
            metric.get("unit", ""),
            metric.get("details"),
        )
    connection.commit()


def build_state_context(
    state: TileState,
    index: Any,
    output_root: Path,
    sectors_root: Path,
    ghostline_red: Path,
    red_schema: Path,
    *,
    quest_sources: dict[str, Path] | None = None,
) -> dict[str, Any]:
    from world_location_nav import (
        reconstruct_navigation_islands,
        sample_navigation_islands,
    )
    from world_location_world import (
        AABB,
        GEOMETRY_POLICY_DETAILED,
        TileSectorOverlap,
        stage_streaming_sector,
    )

    started = time.perf_counter()
    quest_sources = quest_sources or {}
    selector = selector_for_state(index, state)
    min_x, min_y, min_z, max_x, max_y, max_z = state.bounds
    tile, overlaps = index.query_tile(
        state.anchor,
        core_size=state.size,
        near_size=state.size + state.clip_margin * 2.0,
        far_size=None,
        z_min=min_z,
        z_max=max_z,
    )
    allowed_categories = {value.casefold() for value in state.sector_categories}
    allowed_levels = set(state.lod_levels)
    visible: dict[str, TileSectorOverlap] = {}
    for overlap in overlaps:
        descriptor = overlap.descriptor
        if descriptor.category == "quest":
            continue
        if descriptor.category not in allowed_categories:
            continue
        if descriptor.level not in allowed_levels:
            continue
        visible[descriptor.depot_path] = overlap
    descriptors_by_path = {
        item.depot_path.casefold(): item for item in index.descriptors
    }
    for depot_path in quest_sources:
        descriptor = descriptors_by_path.get(depot_path.casefold())
        if descriptor is None or "quest" not in allowed_categories:
            continue
        visible[descriptor.depot_path] = TileSectorOverlap(
            descriptor,
            "core",
            GEOMETRY_POLICY_DETAILED,
        )

    project_root = output_root / "tiles" / state.key / "project"
    project_raw = project_root / "source" / "raw"
    project_raw.mkdir(parents=True, exist_ok=True)
    cache_root = output_root / "cache"
    clip_bounds = AABB(min_x, min_y, min_z, max_x, max_y, max_z)
    sector_rows: list[dict[str, Any]] = []
    staged_paths: list[Path] = []
    embedded_render_resources: dict[str, dict[str, Any]] = {}
    sector_failures: list[dict[str, str]] = []
    serialized_bytes = 0
    stage_started = time.perf_counter()
    visible_sectors = sorted(visible.items())
    for sector_number, (depot_path, overlap) in enumerate(visible_sectors, 1):
        descriptor = overlap.descriptor
        if (
            sector_number == 1
            or sector_number % 10 == 0
            or sector_number == len(visible_sectors)
        ):
            print(
                f"[world-location] sector [{sector_number}/{len(visible_sectors)}] "
                f"{descriptor.depot_path}",
                flush=True,
            )
        try:
            quest_source = quest_sources.get(depot_path.casefold())
            if quest_source is not None:
                source_path = quest_source
            else:
                source_path, _source_record = serialize_sector_cached(
                    depot_path,
                    sectors_root,
                    cache_root,
                    ghostline_red,
                    red_schema,
                )
            serialized_bytes += source_path.stat().st_size
            staged = stage_streaming_sector(
                source_path,
                descriptor,
                selector,
                tile_id=state.key,
                overlap=overlap,
                clip_bounds=clip_bounds,
                clip_margin=state.clip_margin,
            )
            target = depot_output_path(project_raw, depot_path, json_sidecar=True)
            if staged.manifest_row["retained_instance_count"]:
                row = staged.write(target)
                staged_paths.append(target)
                for embedded_path, embedded_document in embedded_render_documents(
                    staged.document
                ):
                    normalized = embedded_path.replace("/", "\\").casefold()
                    prior = embedded_render_resources.get(normalized)
                    if prior is not None and prior != embedded_document:
                        raise LocationDatabaseError(
                            f"Conflicting embedded render resources for {embedded_path}"
                        )
                    embedded_render_resources[normalized] = embedded_document
            else:
                if target.is_file():
                    target.unlink()
                row = dict(staged.manifest_row)
                row["staged_path"] = ""
            sector_rows.append(row)
        except Exception as exc:
            sector_failures.append({"depot_path": depot_path, "error": str(exc)})

    retained_set = {path.resolve() for path in staged_paths}
    for stale in project_raw.rglob("*.streamingsector.json"):
        if stale.resolve() not in retained_set:
            stale.unlink()
    embedded_render_paths: list[Path] = []
    for depot_path, embedded_document in sorted(embedded_render_resources.items()):
        target = depot_output_path(project_raw, depot_path, json_sidecar=True)
        write_json(target, embedded_document)
        embedded_render_paths.append(target)
    retained_embedded_set = {path.resolve() for path in embedded_render_paths}
    for stale in project_raw.rglob("*.cfoliage.json"):
        if stale.resolve() not in retained_embedded_set:
            stale.unlink()
    stage_seconds = time.perf_counter() - stage_started

    resource_scan = scan_sector_resources(staged_paths)
    placements = staged_placements(staged_paths)

    navigation_overlaps = {
        overlap.descriptor.depot_path: overlap
        for overlap in overlaps
        if overlap.descriptor.category == "navigation"
    }
    navigation_paths: list[Path] = []
    navigation_failures: list[dict[str, str]] = []
    nav_started = time.perf_counter()
    for depot_path in sorted(navigation_overlaps):
        try:
            path, _record = serialize_sector_cached(
                depot_path,
                sectors_root,
                cache_root,
                ghostline_red,
                red_schema,
            )
            navigation_paths.append(path)
        except Exception as exc:
            navigation_failures.append({"depot_path": depot_path, "error": str(exc)})
    active_variant_ids = {key.variant_id for key in selector.active_keys}
    buffers = clipped_navigation_buffers(
        navigation_paths,
        state.bounds,
        active_variant_ids,
    )
    raw_islands = reconstruct_navigation_islands(buffers)
    raw_samples = sample_navigation_islands(
        raw_islands,
        spacing_m=state.sample_spacing,
        camera_height_m=state.eye_height,
        seed=int(sha256_text(state.key)[:8], 16),
    )
    chosen_samples = select_navigation_samples(
        raw_samples,
        raw_islands,
        state,
        placements,
    )
    nav_seconds = time.perf_counter() - nav_started

    raw_island_by_id = {island.island_id: island for island in raw_islands}
    db_island_ids = {
        island.island_id: sha256_text(f"{state.key}:{island.island_id}")[:24]
        for island in raw_islands
    }
    island_rows: list[dict[str, Any]] = []
    for island in raw_islands:
        if not any(sample.island_id == island.island_id for sample in raw_samples):
            continue
        sources = sorted({face.source.resource_path for face in island.faces})
        island_rows.append(
            {
                "island_id": db_island_ids[island.island_id],
                "agent_type": "Human",
                "source_sector": ";".join(sources),
                "polygon_count": len(island.faces),
                "walkable_area": island.metrics.surface_area_m2,
                "bounds": {
                    "min": island.bounds.minimum.__dict__,
                    "max": island.bounds.maximum.__dict__,
                },
                "level_key": str(
                    round(
                        (island.metrics.z_min + island.metrics.z_max)
                        / 2.0
                        / state.level_separation
                    )
                ),
            }
        )

    places: list[dict[str, Any]] = []
    for sample in chosen_samples:
        island = raw_island_by_id[sample.island_id]
        point = (
            sample.surface_position.x,
            sample.surface_position.y,
            sample.surface_position.z,
        )
        place_id = sha256_text(
            canonical_json(
                {
                    "state": state.key,
                    "island": sample.island_id,
                    "position": point,
                }
            )
        )[:24]
        structural = {
            "walkable_area_m2": round(island.metrics.surface_area_m2, 3),
            "navigation_polygon_count": len(island.faces),
            "navigation_local_width_m": round(sample.local_width_m, 3),
            "navigation_island_width_m": round(island.metrics.approximate_width_m, 3),
            "navigation_vertical_range_m": round(island.metrics.z_range_m, 3),
            "boundary_length_m": round(island.metrics.boundary_length_m, 3),
            "road_access": "unclassified",
            "enclosure": "pending_renderer_rays",
            "entrances": "unclassified",
            "approximate_scale": (
                "large"
                if island.metrics.surface_area_m2 >= 2500
                else "medium"
                if island.metrics.surface_area_m2 >= 400
                else "small"
            ),
            "sample_spacing_m": state.sample_spacing,
        }
        places.append(
            {
                "place_id": place_id,
                "island_id": db_island_ids[sample.island_id],
                "x": point[0],
                "y": point[1],
                "z": point[2],
                "yaw_degrees": sample_yaw(sample, island, state),
                "interior": state.archetype == "multilevel_interior",
                "source": "navigation",
                "status": "candidate",
                "structural": structural,
                "nearby_resources": nearby_placements(placements, point),
                "provenance": sample.provenance.__dict__,
            }
        )
    if not places:
        point = state.anchor
        places.append(
            {
                "place_id": sha256_text(f"{state.key}:anchor-fallback")[:24],
                "island_id": None,
                "x": point[0],
                "y": point[1],
                "z": point[2],
                "yaw_degrees": 0.0,
                "interior": state.archetype == "multilevel_interior",
                "source": "anchor_fallback",
                "status": "requires_renderer_validation",
                "structural": {
                    "navigation": "unavailable",
                    "enclosure": "pending_renderer_rays",
                },
                "nearby_resources": nearby_placements(placements, point),
                "provenance": {"method": "spec_anchor"},
            }
        )

    content_fingerprint = sha256_text(
        canonical_json(
            {
                "state": state.__dict__,
                "sectors": [row["staged_sector_fingerprint"] for row in sector_rows],
                "navigation": [file_identity(path) for path in navigation_paths],
                "places": [
                    (place["x"], place["y"], place["z"], place["yaw_degrees"])
                    for place in places
                ],
            }
        )
    )
    status = "prepared"
    errors = sector_failures + navigation_failures
    if not staged_paths:
        status = "failed"
    elif errors or places[0]["source"] != "navigation":
        status = "prepared_with_gaps"
    manifest_path = output_root / "tiles" / state.key / "assembly-manifest.json"
    metrics = {
        "stage_seconds": {"value": stage_seconds, "unit": "seconds"},
        "navigation_seconds": {"value": nav_seconds, "unit": "seconds"},
        "serialized_input_bytes": {"value": serialized_bytes, "unit": "bytes"},
        "candidate_sector_count": {"value": len(visible), "unit": "sectors"},
        "navigation_sector_count": {
            "value": len(navigation_paths),
            "unit": "sectors",
        },
        "navigation_buffer_count": {"value": len(buffers), "unit": "buffers"},
        "navigation_island_count": {
            "value": len(raw_islands),
            "unit": "islands",
        },
        "candidate_place_count": {"value": len(places), "unit": "places"},
        "embedded_render_resource_count": {
            "value": len(embedded_render_paths),
            "unit": "resources",
        },
    }
    context = {
        "schema_version": 1,
        "state_key": state.key,
        "tile_id": state.tile_id,
        "state_id": state.state_id,
        "project_root": project_root,
        "project_raw": project_raw,
        "manifest_path": manifest_path,
        "content_fingerprint": content_fingerprint,
        "status": status,
        "error": "; ".join(row["error"] for row in errors[:5]),
        "sector_rows": sector_rows,
        "sector_failures": sector_failures,
        "navigation_failures": navigation_failures,
        "navigation_sources": [str(path.resolve()) for path in navigation_paths],
        "embedded_render_resources": [
            str(path.resolve()) for path in embedded_render_paths
        ],
        "islands": island_rows,
        "places": places,
        "resource_scan": resource_scan,
        "direct_resource_summary": dict(resource_scan["summary"]),
        "asset_status": "not_requested",
        "metrics": metrics,
        "assembly_seconds": time.perf_counter() - started,
    }
    manifest_document = {
        key: value
        for key, value in context.items()
        if key not in {"project_root", "project_raw", "manifest_path"}
    }
    manifest_document["project_root"] = str(project_root.resolve())
    manifest_document["project_raw"] = str(project_raw.resolve())
    write_json(manifest_path, manifest_document)
    return context


def install_exported_assets(
    resource_scan: dict[str, Any],
    union_report: dict[str, Any],
    project_raw: Path,
) -> dict[str, Any]:
    exported = {row["depot_path"]: row for row in union_report.get("assets", [])}
    failures = {row["depot_path"]: row for row in union_report.get("failed", [])}
    assets: list[dict[str, Any]] = []
    failed: list[dict[str, str]] = []
    installed = 0
    reused = 0
    requested = 0
    expected_targets: set[Path] = set()
    for resource in resource_scan["resources"]:
        if resource["resource_type"] != "mesh":
            continue
        requested += 1
        depot_path = resource["depot_path"]
        cached = exported.get(depot_path)
        if cached is None:
            failed.append(
                failures.get(
                    depot_path,
                    {
                        "depot_path": depot_path,
                        "error": "mesh absent from union export",
                    },
                )
            )
            continue
        source_glb = Path(cached["glb"])
        material_value = str(cached.get("material_json", ""))
        source_material = Path(material_value) if material_value else None
        target_glb = depot_output_path(project_raw, depot_path).with_suffix(".glb")
        target_material = target_glb.with_name(f"{target_glb.stem}.Material.json")
        expected_targets.add(target_glb.resolve())
        glb_action = install_file(source_glb, target_glb)
        if source_material is not None and source_material.is_file():
            expected_targets.add(target_material.resolve())
            material_action = install_file(source_material, target_material)
            staged_material = str(target_material.resolve())
        else:
            target_material.unlink(missing_ok=True)
            material_action = "not_available"
            staged_material = ""
        actions = (glb_action, material_action)
        if glb_action == "reused" and material_action in {"reused", "not_available"}:
            reused += 1
        else:
            installed += 1
        assets.append(
            {
                **cached,
                "staged_glb": str(target_glb.resolve()),
                "staged_material_json": staged_material,
                "install_actions": actions,
            }
        )
    pruned = 0
    for pattern in ("*.glb", "*.Material.json"):
        for stale in project_raw.rglob(pattern):
            if stale.resolve() not in expected_targets:
                stale.unlink()
                pruned += 1
    pbr_keys = set(mesh_appearance_requests(resource_scan))
    pbr_assets = [
        dict(row)
        for row in union_report.get("pbr_assets", [])
        if isinstance(row, Mapping)
        and (str(row.get("depot_path", "")), str(row.get("appearance", "")))
        in pbr_keys
    ]
    pbr_failures = [
        dict(row)
        for row in union_report.get("pbr_failures", [])
        if isinstance(row, Mapping)
        and (str(row.get("depot_path", "")), str(row.get("appearance", "")))
        in pbr_keys
    ]
    return {
        "schema_version": 1,
        "requested": requested,
        "installed": installed,
        "reused": reused,
        "pruned": pruned,
        "failed": failed,
        "material_warnings": [
            {
                "depot_path": row["depot_path"],
                "error": row["material_error"],
            }
            for row in assets
            if row.get("material_error")
        ],
        "assets": assets,
        "pbr_assets": pbr_assets,
        "pbr_failures": pbr_failures,
    }


def stage_state_dependencies(
    state_dependencies: Any,
    state_key: str,
    project_raw: Path,
) -> dict[str, Any]:
    from world_location_dependencies import install_dependency_jsons

    selected = set(state_dependencies.state_resources[state_key])
    records = [
        resource
        for resource in state_dependencies.closure.resources
        if resource.resource in selected
    ]
    installed = install_dependency_jsons(
        state_dependencies.closure,
        project_raw,
        resources=selected,
        fail_on_errors=False,
    )
    expected_targets = {record.target.resolve() for record in installed}
    pruned = 0
    for pattern in ("*.ent.json", "*.app.json"):
        for stale in project_raw.rglob(pattern):
            if stale.resolve() not in expected_targets:
                stale.unlink()
                pruned += 1
    resource_reports = [record.to_report() for record in records]
    failures = [
        report
        for report in resource_reports
        if report["serializable"] and report["status"] != "ready"
    ]
    selections = state_dependencies.appearance_selections.get(state_key, {})
    unmatched = state_dependencies.unmatched_appearance_selections.get(state_key, {})
    selection_failures = [
        {
            "resource": resource,
            "error": (
                "requested appearance selection was not found: " + ", ".join(names)
            ),
            "selections": list(names),
        }
        for resource, names in sorted(unmatched.items())
    ]
    failures.extend(selection_failures)
    return {
        "schema_version": 1,
        "identity_fingerprint": state_dependencies.closure.identity_fingerprint,
        "summary": {
            "resources": len(records),
            "serializable": sum(record.serializable for record in records),
            "ready_json": sum(
                record.serializable and record.status == "ready" for record in records
            ),
            "cache_hits": sum(record.cache_hit for record in records),
            "installed": len(installed),
            "pruned": pruned,
            "failures": len(failures),
        },
        "appearance_selections": {
            resource: list(names) for resource, names in sorted(selections.items())
        },
        "unmatched_appearance_selections": {
            resource: list(names) for resource, names in sorted(unmatched.items())
        },
        "resources": resource_reports,
        "installed": [record.to_report() for record in installed],
        "failed": failures,
    }


def finalize_staged_content_fingerprint(context: dict[str, Any]) -> None:
    assembly_fingerprint = context.setdefault(
        "assembly_content_fingerprint", context["content_fingerprint"]
    )
    dependency_report = context.get("dependency_report", {})
    asset_report = context.get("asset_report", {})
    context["content_fingerprint"] = sha256_text(
        canonical_json(
            {
                "assembly": assembly_fingerprint,
                "resources": [
                    (row["depot_path"], row["resource_type"])
                    for row in context["resource_scan"]["resources"]
                ],
                "dependency_identity": dependency_report.get(
                    "identity_fingerprint", ""
                ),
                "dependencies": [
                    (
                        row.get("resource", ""),
                        row.get("status", ""),
                        row.get("cache_fingerprint", ""),
                    )
                    for row in dependency_report.get("resources", [])
                    if row.get("serializable")
                ],
                "meshes": [
                    (row.get("depot_path", ""), row.get("fingerprint", ""))
                    for row in asset_report.get("assets", [])
                ],
                "native_pbr_assets": [
                    (
                        row.get("depot_path", ""),
                        row.get("appearance", ""),
                        row.get("fingerprint", ""),
                    )
                    for row in asset_report.get("pbr_assets", [])
                ],
                "failed_dependencies": [
                    row.get("resource", "")
                    for row in dependency_report.get("failed", [])
                ],
                "failed_meshes": [
                    row.get("depot_path", "") for row in asset_report.get("failed", [])
                ],
                "failed_native_pbr_assets": [
                    (row.get("depot_path", ""), row.get("appearance", ""))
                    for row in asset_report.get("pbr_failures", [])
                ],
            }
        )
    )


def portable_context(context: dict[str, Any]) -> dict[str, Any]:
    result = {
        key: value
        for key, value in context.items()
        if key not in {"project_root", "project_raw", "manifest_path"}
    }
    result.update(
        {
            "project_root": str(context["project_root"].resolve()),
            "project_raw": str(context["project_raw"].resolve()),
            "manifest_path": str(context["manifest_path"].resolve()),
        }
    )
    return result


def build_poc(
    *,
    spec_path: Path = DEFAULT_SPEC,
    output_root: Path = DEFAULT_OUTPUT,
    block_path: Path = DEFAULT_BLOCK,
    sectors_root: Path = DEFAULT_SECTORS,
    quest_json_root: Path | None = DEFAULT_QUEST_JSON,
    game: Path = DEFAULT_GAME,
    ghostline_red: Path = DEFAULT_GHOSTLINE_RED,
    red_schema: Path = DEFAULT_RED_SCHEMA,
    metadata_only: bool = False,
    export_threads: int = 8,
    selected_tiles: set[str] | None = None,
) -> dict[str, Any]:
    from world_location_spatial import build_sector_spatial_index
    from world_location_world import AABB, WorldSectorIndex, parse_streaming_block

    for required in (spec_path, block_path, ghostline_red, red_schema):
        if not required.is_file():
            raise LocationDatabaseError(f"Required POC input is missing: {required}")
    if not sectors_root.is_dir():
        raise LocationDatabaseError(f"Extracted sector root is missing: {sectors_root}")
    spec, all_states = load_tile_states(spec_path)
    known_tiles = {state.tile_id for state in all_states}
    if selected_tiles:
        unknown = sorted(selected_tiles - known_tiles)
        if unknown:
            raise LocationDatabaseError(f"Unknown tile id(s): {', '.join(unknown)}")
        states = [state for state in all_states if state.tile_id in selected_tiles]
    else:
        states = all_states

    output_root.mkdir(parents=True, exist_ok=True)
    database = output_root / "locations.sqlite3"
    connection = connect(database)
    create_schema(connection)
    game_archives = game / "archive/pc"
    game_executable = game / "bin/x64/Cyberpunk2077.exe"
    config = {
        "block_identity": file_identity(block_path),
        "sectors_root": str(sectors_root.resolve()),
        "sectors_identity": directory_inventory_identity(
            sectors_root, suffixes=(".streamingsector", ".streamingsector.json")
        ),
        "quest_json_root": (
            str(quest_json_root.resolve())
            if quest_json_root is not None and quest_json_root.exists()
            else None
        ),
        "quest_json_identity": (
            directory_inventory_identity(
                quest_json_root, suffixes=(".streamingsector.json",)
            )
            if quest_json_root is not None
            else None
        ),
        "game": str(game.resolve()),
        "game_archive_identity": directory_inventory_identity(
            game_archives, suffixes=(".archive",)
        ),
        "game_executable_identity": (
            file_identity(game_executable) if game_executable.is_file() else None
        ),
        "ghostline_red": file_identity(ghostline_red),
        "red_schema": file_identity(red_schema),
        "pipeline": pipeline_identity(),
        "metadata_only": metadata_only,
    }
    run_id = begin_run(
        connection,
        spec_path,
        spec,
        all_states,
        config,
        active_state_keys={state.key for state in states},
    )
    index_started = time.perf_counter()
    index = WorldSectorIndex(parse_streaming_block(block_path))
    world_index_seconds = time.perf_counter() - index_started

    quest_index = None
    if quest_json_root is not None and quest_json_root.is_dir():
        quest_index = build_sector_spatial_index(
            [quest_json_root],
            cache_path=output_root / "cache/quest-sector-spatial-index.json",
        )

    contexts: list[tuple[TileState, dict[str, Any]]] = []
    for state in states:
        print(f"[world-location] assembling {state.key}", flush=True)
        quest_sources: dict[str, Path] = {}
        if quest_index is not None:
            margin = state.clip_margin
            expanded = AABB(
                state.bounds[0] - margin,
                state.bounds[1] - margin,
                state.bounds[2] - margin,
                state.bounds[3] + margin,
                state.bounds[4] + margin,
                state.bounds[5] + margin,
            )
            for record in quest_index.query_placements(expanded):
                if record.category.casefold() == "quest":
                    quest_sources[record.depot_path.casefold()] = record.source_json
        try:
            context = build_state_context(
                state,
                index,
                output_root,
                sectors_root,
                ghostline_red,
                red_schema,
                quest_sources=quest_sources,
            )
        except Exception as exc:
            connection.execute(
                "UPDATE tile_states SET status='failed', error=? WHERE state_key=?",
                (str(exc), state.key),
            )
            connection.commit()
            raise
        context["metrics"]["world_index_seconds"] = {
            "value": world_index_seconds,
            "unit": "seconds",
            "details": {"shared_across_states": True},
        }
        context["metrics"]["quest_spatial_candidates"] = {
            "value": len(quest_sources),
            "unit": "sectors",
        }
        context["metrics"]["render_directions_per_place"] = {
            "value": len(state.directions),
            "unit": "directions",
        }
        contexts.append((state, context))

    union_report: dict[str, Any] = {
        "assets": [],
        "failed": [],
        "pbr_assets": [],
        "pbr_failures": [],
    }
    dependency_seconds = 0.0
    mesh_export_seconds = 0.0
    dependency_cache_bytes = 0
    mesh_cache_bytes = 0
    if not metadata_only and contexts:
        from world_location_dependencies import ArchiveDependencyResolver

        print("[world-location] resolving entity/appearance dependencies", flush=True)
        dependency_started = time.perf_counter()
        resolver = ArchiveDependencyResolver(
            cache_root=output_root / "cache/dependencies",
            ghostline_red=ghostline_red,
            schemas=red_schema,
            archives_root=game / "archive/pc",
            kraken=DEFAULT_KRAKEN,
            threads=export_threads,
            cwd=ROOT,
        )
        for _state, context in contexts:
            context["ignored_dependency_resources"] = [
                resource["depot_path"]
                for resource in context["resource_scan"]["resources"]
                if resource["resource_type"] in {"ent", "app"}
                and not requires_render_dependency(resource)
            ]
            context["requested_appearance_selections"] = {
                resource["depot_path"]: list(resource.get("appearances") or ["default"])
                for resource in context["resource_scan"]["resources"]
                if resource["resource_type"] in {"ent", "app"}
                and requires_render_dependency(resource)
            }
        state_dependencies = resolver.resolve_states(
            {
                state.key: [
                    resource["depot_path"]
                    for resource in context["resource_scan"]["resources"]
                    if resource["resource_type"] in {"ent", "app"}
                    and requires_render_dependency(resource)
                ]
                for state, context in contexts
            },
            state_appearance_selections={
                state.key: context["requested_appearance_selections"]
                for state, context in contexts
            },
        )
        dependency_seconds = time.perf_counter() - dependency_started
        write_json(
            output_root / "cache/dependencies/dependency-report.json",
            state_dependencies.to_report(),
        )
        for state, context in contexts:
            selected = set(state_dependencies.state_resources[state.key])
            dependency_rows = [
                resource.to_report()
                for resource in state_dependencies.closure.resources
                if resource.resource in selected
            ]
            context["resource_scan"] = augment_resource_scan(
                context["resource_scan"], dependency_rows
            )
            install_started = time.perf_counter()
            context["dependency_report"] = stage_state_dependencies(
                state_dependencies, state.key, context["project_raw"]
            )
            context["metrics"]["dependency_install_seconds"] = {
                "value": time.perf_counter() - install_started,
                "unit": "seconds",
            }
            dependency_summary = context["dependency_report"]["summary"]
            context["metrics"]["dependency_resource_count"] = {
                "value": dependency_summary["resources"],
                "unit": "resources",
            }
            context["metrics"]["dependency_failure_count"] = {
                "value": dependency_summary["failures"],
                "unit": "resources",
            }
            context["metrics"]["runtime_only_entity_count"] = {
                "value": len(context["ignored_dependency_resources"]),
                "unit": "resources",
            }

        print("[world-location] exporting shared mesh/material cache", flush=True)
        union_scan = merge_resource_scans(
            context["resource_scan"] for _state, context in contexts
        )
        mesh_started = time.perf_counter()
        union_report = prepare_mesh_assets(
            union_scan,
            output_root / "cache/export-project/source/raw",
            output_root / "cache",
            game,
            ghostline_red,
            red_schema,
            export_threads,
        )
        mesh_export_seconds = time.perf_counter() - mesh_started
        dependency_cache_bytes = directory_size(output_root / "cache/dependencies")
        mesh_cache_bytes = directory_size(output_root / "cache/meshes")

    jobs: list[dict[str, Any]] = []
    for state, context in contexts:
        if not metadata_only:
            asset_report = install_exported_assets(
                context["resource_scan"], union_report, context["project_raw"]
            )
            context["asset_report"] = asset_report
            dependency_failures = context["dependency_report"]["failed"]
            asset_failures = [*dependency_failures, *asset_report["failed"]]
            context["asset_status"] = "complete" if not asset_failures else "failed"
            if context["status"] != "failed":
                if asset_failures:
                    context["status"] = "prepared_with_asset_gaps"
                elif context["status"] == "prepared":
                    context["status"] = "ready_to_render"
            if asset_failures:
                errors = [context.get("error", "")]
                errors.extend(
                    str(row.get("error") or "asset preparation failed")
                    for row in asset_failures[:5]
                )
                context["error"] = "; ".join(error for error in errors if error)
            context["metrics"]["dependency_resolve_seconds"] = {
                "value": dependency_seconds,
                "unit": "seconds",
                "details": {"shared_across_states": True},
            }
            context["metrics"]["mesh_export_seconds"] = {
                "value": mesh_export_seconds,
                "unit": "seconds",
                "details": {"shared_across_states": True},
            }
            context["metrics"]["material_warning_count"] = {
                "value": len(asset_report.get("material_warnings", [])),
                "unit": "meshes",
            }
            context["metrics"]["dependency_cache_bytes"] = {
                "value": dependency_cache_bytes,
                "unit": "bytes",
                "details": {"shared_across_states": True},
            }
            context["metrics"]["mesh_cache_bytes"] = {
                "value": mesh_cache_bytes,
                "unit": "bytes",
                "details": {"shared_across_states": True},
            }
            context["metrics"]["tile_project_bytes"] = {
                "value": directory_size(context["project_raw"]),
                "unit": "bytes",
            }
            finalize_staged_content_fingerprint(context)
        context["content_fingerprint"] = sha256_text(
            canonical_json(
                {
                    "run_id": run_id,
                    "staged_content": context["content_fingerprint"],
                }
            )
        )
        write_json(context["manifest_path"], portable_context(context))
        store_state_context(connection, state, context)
        jobs.append(state_job(state, context, output_root, run_id=run_id))

    jobs_path = output_root / "six-tile-render-jobs.json"
    if selected_tiles and jobs_path.is_file():
        prior_document = read_json(jobs_path)
        prior_jobs = (
            prior_document.get("jobs", [])
            if str(prior_document.get("run_id", "")) == run_id
            else []
        )
        if isinstance(prior_jobs, list):
            current_fingerprints = {
                str(row["state_key"]): str(row["content_fingerprint"])
                for row in connection.execute(
                    "SELECT state_key, content_fingerprint FROM tile_states "
                    "WHERE run_id=?",
                    (run_id,),
                )
            }
            merged_jobs = {
                str(job.get("tile_id", "")): job
                for job in prior_jobs
                if isinstance(job, dict)
                and str(job.get("tile_id", "")) in current_fingerprints
                and str(job.get("content_fingerprint", ""))
                == current_fingerprints[str(job.get("tile_id", ""))]
            }
            merged_jobs.update({str(job["tile_id"]): job for job in jobs})
            jobs = [merged_jobs[key] for key in sorted(merged_jobs)]
    write_json(
        jobs_path,
        {
            "schema_version": 1,
            "run_id": run_id,
            "defaults": {
                "resolution": int(spec["defaults"]["render_resolution"]),
                "image_format": spec["defaults"]["render_format"],
                "image_quality": int(spec["defaults"]["render_quality"]),
                "horizontal_fov_degrees": float(
                    spec["defaults"]["horizontal_fov_degrees"]
                ),
                "with_static_lights": False,
            },
            "jobs": jobs,
        },
    )
    summary = database_summary(connection)
    if metadata_only:
        run_status = "metadata_prepared"
    elif set(summary["state_statuses"]) <= {"ready_to_render"}:
        run_status = "ready_to_render"
    else:
        run_status = "prepared_with_gaps"
    connection.execute(
        "UPDATE runs SET status=?, summary_json=? WHERE run_id=?",
        (
            run_status,
            canonical_json(summary),
            run_id,
        ),
    )
    connection.commit()
    connection.close()
    report = write_poc_report(database, output_root / "poc-report.json")
    return {
        "run_id": run_id,
        "database": str(database.resolve()),
        "jobs": str(jobs_path.resolve()),
        "report": str((output_root / "poc-report.json").resolve()),
        "summary": report["summary"],
        "quest_spatial_cache_hit": (
            quest_index.cache_hit if quest_index is not None else None
        ),
    }


def ingest_render_report(database: Path, batch_report: Path) -> dict[str, Any]:
    batch = read_json(batch_report)
    connection = connect(database)
    create_schema(connection)
    ingested_images = 0
    invalid_images = 0
    stale_reports = 0
    for entry in batch.get("tiles", []):
        state_key = str(entry.get("tile_id", ""))
        tile_report_path = Path(str(entry.get("report", "")))
        if not state_key or not tile_report_path.is_file():
            continue
        report = read_json(tile_report_path)
        state_row = connection.execute(
            "SELECT content_fingerprint, run_id FROM tile_states WHERE state_key=?",
            (state_key,),
        ).fetchone()
        if state_row is None:
            continue
        expected_fingerprint = str(state_row["content_fingerprint"])
        reported_fingerprint = str(report.get("content_fingerprint", ""))
        reported_run_id = str(report.get("run_id", ""))
        if (
            not reported_fingerprint
            or reported_fingerprint != expected_fingerprint
            or (reported_run_id and reported_run_id != str(state_row["run_id"]))
        ):
            stale_reports += 1
            connection.execute(
                "UPDATE tile_states SET status='render_stale', error=? WHERE state_key=?",
                (
                    "renderer content fingerprint does not match the current assembly",
                    state_key,
                ),
            )
            continue
        connection.execute(
            "DELETE FROM images WHERE place_id IN "
            "(SELECT place_id FROM places WHERE state_key=?)",
            (state_key,),
        )
        connection.execute(
            "UPDATE places SET status='render_missing' WHERE state_key=?",
            (state_key,),
        )
        renderer = report.get("renderer", {})
        renderer_fingerprint = str(renderer.get("renderer_fingerprint", ""))
        resolution = int(renderer.get("resolution", 0) or 0)
        seen_places: set[str] = set()
        for view in report.get("views", []):
            place_id = str(view.get("viewpoint_id", ""))
            if not place_id:
                continue
            exists = connection.execute(
                "SELECT 1 FROM places WHERE place_id=? AND state_key=?",
                (place_id, state_key),
            ).fetchone()
            if not exists:
                continue
            yaw = float(view.get("yaw_degrees", 0.0)) % 360.0
            image = view.get("image") if isinstance(view.get("image"), dict) else {}
            path = str(image.get("path") or view.get("output") or "")
            artifact_error = ""
            artifact_sha256 = ""
            artifact_bytes = 0
            if not path:
                artifact_error = "render report has no image path"
            else:
                artifact = Path(path)
                if not artifact.is_file():
                    artifact_error = f"rendered image is missing: {artifact}"
                else:
                    artifact_bytes = artifact.stat().st_size
                    if artifact_bytes <= 0:
                        artifact_error = f"rendered image is empty: {artifact}"
                    else:
                        artifact_sha256 = sha256_file(artifact)
                        reported_sha256 = str(image.get("sha256", ""))
                        if reported_sha256 and reported_sha256 != artifact_sha256:
                            artifact_error = (
                                f"rendered image hash mismatch: {reported_sha256} != "
                                f"{artifact_sha256}"
                            )
            status = (
                "complete"
                if view.get("valid") and image and not artifact_error
                else "invalid"
            )
            image_id = sha256_text(f"{place_id}:{yaw:.6f}")[:24]
            diagnostics = {
                key: value
                for key, value in view.items()
                if key not in {"image", "metadata"}
            }
            diagnostics["artifact"] = {
                "sha256": artifact_sha256,
                "bytes": artifact_bytes,
                "error": artifact_error,
            }
            connection.execute(
                """
                INSERT INTO images VALUES (?, ?, ?, ?, ?, ?, ?, ?, '', ?, ?)
                ON CONFLICT(place_id, direction_degrees) DO UPDATE SET
                    image_id=excluded.image_id, path=excluded.path,
                    width=excluded.width, height=excluded.height,
                    renderer_fingerprint=excluded.renderer_fingerprint,
                    content_fingerprint=excluded.content_fingerprint,
                    status=excluded.status, diagnostics_json=excluded.diagnostics_json
                """,
                (
                    image_id,
                    place_id,
                    yaw,
                    path,
                    resolution,
                    resolution,
                    renderer_fingerprint,
                    expected_fingerprint,
                    status,
                    canonical_json(diagnostics),
                ),
            )
            if status == "complete":
                ingested_images += 1
            else:
                invalid_images += 1
            if place_id not in seen_places:
                row = connection.execute(
                    "SELECT structural_json FROM places WHERE place_id=?",
                    (place_id,),
                ).fetchone()
                structural = json.loads(row[0] or "{}") if row else {}
                validation = view.get("position_validation", {})
                openness = validation.get("horizontal_openness", {})
                if openness:
                    mean = float(openness.get("mean", 0.0))
                    structural["horizontal_openness_mean_m"] = round(mean, 3)
                    structural["horizontal_openness_min_m"] = round(
                        float(openness.get("minimum", 0.0)), 3
                    )
                    structural["horizontal_openness_max_m"] = round(
                        float(openness.get("maximum", 0.0)), 3
                    )
                    structural["enclosure"] = (
                        "enclosed"
                        if mean < 4.0
                        else "semi_enclosed"
                        if mean < 10.0
                        else "open"
                    )
                structural["estimated_ceiling_height_m"] = validation.get(
                    "estimated_ceiling_height"
                )
                structural["camera_validation"] = (
                    "valid" if validation.get("valid") else "invalid"
                )
                connection.execute(
                    """
                    UPDATE places SET structural_json=?, renderer_fingerprint=?
                    WHERE place_id=?
                    """,
                    (canonical_json(structural), renderer_fingerprint, place_id),
                )
                seen_places.add(place_id)
        for place_id in seen_places:
            complete = connection.execute(
                "SELECT COUNT(*) FROM images WHERE place_id=? AND status='complete'",
                (place_id,),
            ).fetchone()[0]
            expected_directions = int(
                connection.execute(
                    """SELECT COALESCE(MAX(value), 0) FROM metrics
                       WHERE state_key=? AND name='render_directions_per_place'""",
                    (state_key,),
                ).fetchone()[0]
            )
            connection.execute(
                "UPDATE places SET status=? WHERE place_id=?",
                (
                    (
                        "rendered"
                        if expected_directions > 0 and complete >= expected_directions
                        else "partial_render"
                        if complete
                        else "invalid_camera"
                    ),
                    place_id,
                ),
            )
        tile_status = str(report.get("status", "failed"))
        connection.execute(
            "UPDATE tile_states SET status=?, error=? WHERE state_key=?",
            (
                f"render_{tile_status}",
                str(report.get("error", "")),
                state_key,
            ),
        )
        timings = report.get("timings", {})
        content = report.get("content", {})
        signals = content.get("signals", []) if isinstance(content, dict) else []
        if isinstance(signals, list):
            error_count = sum(
                isinstance(signal, dict) and signal.get("severity") == "error"
                for signal in signals
            )
            set_metric(
                connection,
                state_key,
                "render_content_errors",
                error_count,
                "signals",
                content if isinstance(content, dict) else {},
            )
        if "import_seconds" in timings:
            set_metric(
                connection,
                state_key,
                "import_seconds",
                float(timings["import_seconds"]),
                "seconds",
            )
        if "total_seconds" in timings:
            set_metric(
                connection,
                state_key,
                "render_seconds",
                float(timings["total_seconds"]),
                "seconds",
                report.get("view_summary", {}),
            )
    summary = database_summary(connection)
    active = connection.execute(
        "SELECT value FROM metadata WHERE key='active_run_id'"
    ).fetchone()
    if active:
        connection.execute(
            "UPDATE runs SET status='rendered', summary_json=? WHERE run_id=?",
            (canonical_json(summary), active[0]),
        )
    connection.commit()
    connection.close()
    return {
        "images": ingested_images,
        "invalid": invalid_images,
        "stale_reports": stale_reports,
        "summary": summary,
    }


def render_poc(
    *,
    output_root: Path = DEFAULT_OUTPUT,
    blender: Path = DEFAULT_BLENDER,
    jobs_path: Path | None = None,
    fail_on_invalid: bool = False,
    selected_tiles: set[str] | None = None,
    with_materials: bool | None = None,
) -> dict[str, Any]:
    jobs_path = jobs_path or output_root / "six-tile-render-jobs.json"
    database = output_root / "locations.sqlite3"
    for required in (blender, RENDER_SCRIPT, jobs_path, database):
        if not required.is_file():
            raise LocationDatabaseError(f"Required render input is missing: {required}")
    if selected_tiles:
        document = read_json(jobs_path)
        source_jobs = document.get("jobs", [])
        if not isinstance(source_jobs, list):
            raise LocationDatabaseError(f"Render jobs must be an array: {jobs_path}")
        matched_tiles: set[str] = set()
        selected_jobs = []
        for job in source_jobs:
            if not isinstance(job, dict):
                continue
            state_key = str(job.get("tile_id", ""))
            spatial_tile = state_key.split("--", 1)[0]
            matches = {
                selector
                for selector in selected_tiles
                if selector in {state_key, spatial_tile}
            }
            if matches:
                selected_jobs.append(job)
                matched_tiles.update(matches)
        missing = sorted(selected_tiles - matched_tiles)
        if missing:
            raise LocationDatabaseError(
                f"No render job matched tile selector(s): {', '.join(missing)}"
            )
        selection_fingerprint = sha256_text(
            canonical_json(
                {
                    "source": file_identity(jobs_path),
                    "tiles": sorted(selected_tiles),
                }
            )
        )[:20]
        selected_jobs_path = (
            output_root / "cache/jobs" / f"render-{selection_fingerprint}.json"
        )
        write_json(selected_jobs_path, {**document, "jobs": selected_jobs})
        jobs_path = selected_jobs_path
    batch_report = output_root / "six-tile-render-report.json"
    command = [
        str(blender),
        "--background",
        "--factory-startup",
        "--python",
        str(RENDER_SCRIPT),
        "--",
        "--jobs",
        str(jobs_path),
        "--batch-report",
        str(batch_report),
    ]
    if fail_on_invalid:
        command.append("--fail-on-invalid")
    if with_materials is not None:
        command.append("--with-materials" if with_materials else "--without-materials")
    batch_report.unlink(missing_ok=True)
    process = subprocess.Popen(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    tail: collections.deque[str] = collections.deque(maxlen=200)
    if process.stdout is None:
        raise LocationDatabaseError("Blender did not expose a progress stream")
    for line in process.stdout:
        tail.append(line)
        message = line.strip()
        if message.startswith("GHOSTLINE_WORLD_"):
            print(message, flush=True)
    return_code = process.wait()
    if not batch_report.is_file():
        raise LocationDatabaseError(
            f"Blender exited {return_code} without a batch report:\n{''.join(tail)[-8000:]}"
        )
    ingested = ingest_render_report(database, batch_report)
    report = write_poc_report(database, output_root / "poc-report.json")
    if return_code != 0:
        raise LocationDatabaseError(
            f"Blender rendering failed with exit code {return_code}; "
            f"results were ingested from {batch_report}"
        )
    return {
        "return_code": return_code,
        "batch_report": str(batch_report.resolve()),
        "ingested": ingested,
        "checks": report["checks"],
    }


def plan_document(spec_path: Path) -> dict[str, Any]:
    spec, states = load_tile_states(spec_path)
    return {
        "schema_version": 1,
        "poc_id": spec["poc_id"],
        "spatial_tiles": len({state.tile_id for state in states}),
        "tile_states": len(states),
        "expected_images": sum(
            state.max_viewpoints * len(state.directions) for state in states
        ),
        "states": [
            {
                "state_key": state.key,
                "label": state.label,
                "archetype": state.archetype,
                "bounds": state.bounds,
                "variant_policy": state.variant_policy,
                "max_viewpoints": state.max_viewpoints,
                "directions": state.directions,
            }
            for state in states
        ],
    }


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build and query the Ghostline place-level world-location database."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan = subparsers.add_parser(
        "plan", help="Validate and summarize the six-tile spec"
    )
    plan.add_argument("--spec", type=Path, default=DEFAULT_SPEC)

    build = subparsers.add_parser(
        "build", help="Assemble sectors, sample navigation, and prepare Blender jobs"
    )
    build.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    build.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    build.add_argument("--block", type=Path, default=DEFAULT_BLOCK)
    build.add_argument("--sectors-root", type=Path, default=DEFAULT_SECTORS)
    build.add_argument("--quest-json-root", type=Path, default=DEFAULT_QUEST_JSON)
    build.add_argument("--game", type=Path, default=DEFAULT_GAME)
    build.add_argument("--ghostline-red", type=Path, default=DEFAULT_GHOSTLINE_RED)
    build.add_argument("--red-schema", type=Path, default=DEFAULT_RED_SCHEMA)
    build.add_argument("--metadata-only", action="store_true")
    build.add_argument("--export-threads", type=int, default=8)
    build.add_argument(
        "--tile",
        action="append",
        dest="tiles",
        help="Build only this spatial tile id (repeatable; useful for smoke tests)",
    )

    render = subparsers.add_parser("render", help="Run prepared jobs in Blender")
    render.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    render.add_argument("--blender", type=Path, default=DEFAULT_BLENDER)
    render.add_argument("--jobs", type=Path)
    render.add_argument("--fail-on-invalid", action="store_true")
    render_materials = render.add_mutually_exclusive_group()
    render_materials.add_argument(
        "--with-materials",
        dest="with_materials",
        action="store_true",
        help="Override prepared jobs and import Cyberpunk material sidecars.",
    )
    render_materials.add_argument(
        "--without-materials",
        dest="with_materials",
        action="store_false",
        help="Override prepared jobs and import geometry without materials.",
    )
    render.set_defaults(with_materials=None)
    render.add_argument(
        "--tile",
        action="append",
        dest="tiles",
        help="Render only this spatial tile or exact tile-state id (repeatable)",
    )

    poc = subparsers.add_parser(
        "poc", help="Build all six tiles with assets, then render and ingest them"
    )
    poc.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    poc.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    poc.add_argument("--block", type=Path, default=DEFAULT_BLOCK)
    poc.add_argument("--sectors-root", type=Path, default=DEFAULT_SECTORS)
    poc.add_argument("--quest-json-root", type=Path, default=DEFAULT_QUEST_JSON)
    poc.add_argument("--game", type=Path, default=DEFAULT_GAME)
    poc.add_argument("--ghostline-red", type=Path, default=DEFAULT_GHOSTLINE_RED)
    poc.add_argument("--red-schema", type=Path, default=DEFAULT_RED_SCHEMA)
    poc.add_argument("--blender", type=Path, default=DEFAULT_BLENDER)
    poc.add_argument("--export-threads", type=int, default=8)
    poc.add_argument("--fail-on-invalid", action="store_true")
    poc_materials = poc.add_mutually_exclusive_group()
    poc_materials.add_argument(
        "--with-materials",
        dest="with_materials",
        action="store_true",
        help="Import Cyberpunk material sidecars after building the POC.",
    )
    poc_materials.add_argument(
        "--without-materials",
        dest="with_materials",
        action="store_false",
        help="Import geometry without materials after building the POC.",
    )
    poc.set_defaults(with_materials=None)

    search = subparsers.add_parser("search", help="Search place records")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--database", type=Path)
    search.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    search.add_argument("--archetype", default="")
    search.add_argument("--district", default="")
    search.add_argument("--limit", type=int, default=50)

    vlm = subparsers.add_parser(
        "vlm-export", help="Export one JSONL tagging job per sampled place"
    )
    vlm.add_argument("--database", type=Path)
    vlm.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    vlm.add_argument("--file", type=Path)
    vlm.add_argument("--include-unrendered", action="store_true")

    vlm_import = subparsers.add_parser(
        "vlm-import", help="Import structured VLM tags into sampled places"
    )
    vlm_import.add_argument("file", type=Path)
    vlm_import.add_argument("--database", type=Path)
    vlm_import.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)

    report = subparsers.add_parser(
        "report", help="Regenerate the measurable POC report"
    )
    report.add_argument("--database", type=Path)
    report.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    report.add_argument("--file", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "plan":
            result = plan_document(args.spec.resolve())
        elif args.command == "build":
            result = build_poc(
                spec_path=args.spec.resolve(),
                output_root=args.output.resolve(),
                block_path=args.block.resolve(),
                sectors_root=args.sectors_root.resolve(),
                quest_json_root=(
                    args.quest_json_root.resolve() if args.quest_json_root else None
                ),
                game=args.game.resolve(),
                ghostline_red=args.ghostline_red.resolve(),
                red_schema=args.red_schema.resolve(),
                metadata_only=args.metadata_only,
                export_threads=max(1, args.export_threads),
                selected_tiles=set(args.tiles) if args.tiles else None,
            )
        elif args.command == "render":
            result = render_poc(
                output_root=args.output.resolve(),
                blender=args.blender.resolve(),
                jobs_path=args.jobs.resolve() if args.jobs else None,
                fail_on_invalid=args.fail_on_invalid,
                selected_tiles=set(args.tiles) if args.tiles else None,
                with_materials=args.with_materials,
            )
        elif args.command == "poc":
            built = build_poc(
                spec_path=args.spec.resolve(),
                output_root=args.output.resolve(),
                block_path=args.block.resolve(),
                sectors_root=args.sectors_root.resolve(),
                quest_json_root=(
                    args.quest_json_root.resolve() if args.quest_json_root else None
                ),
                game=args.game.resolve(),
                ghostline_red=args.ghostline_red.resolve(),
                red_schema=args.red_schema.resolve(),
                metadata_only=False,
                export_threads=max(1, args.export_threads),
            )
            rendered = render_poc(
                output_root=args.output.resolve(),
                blender=args.blender.resolve(),
                fail_on_invalid=args.fail_on_invalid,
                with_materials=args.with_materials,
            )
            result = {"build": built, "render": rendered}
        elif args.command == "search":
            database = (args.database or args.output / "locations.sqlite3").resolve()
            connection = connect(database)
            create_schema(connection)
            result = {
                "places": location_rows(
                    connection,
                    args.query,
                    archetype=args.archetype,
                    district=args.district,
                    limit=args.limit,
                )
            }
            connection.close()
        elif args.command == "vlm-export":
            database = (args.database or args.output / "locations.sqlite3").resolve()
            target = (args.file or args.output / "vlm-jobs.jsonl").resolve()
            result = vlm_jobs(
                database, target, include_unrendered=args.include_unrendered
            )
        elif args.command == "vlm-import":
            database = (args.database or args.output / "locations.sqlite3").resolve()
            result = import_vlm_tags(database, args.file.resolve())
        elif args.command == "report":
            database = (args.database or args.output / "locations.sqlite3").resolve()
            target = (args.file or args.output / "poc-report.json").resolve()
            result = write_poc_report(database, target)
        else:  # pragma: no cover - argparse enforces the command set.
            parser.error(f"Unknown command {args.command}")
            return 2
    except (LocationDatabaseError, OSError, sqlite3.Error, ValueError) as exc:
        print(f"world-location error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
