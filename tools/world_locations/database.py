"""SQLite schema, migrations, and focused persistence helpers."""

from __future__ import annotations

from contextlib import contextmanager
from datetime import UTC, datetime
import json
from pathlib import Path
import sqlite3
from typing import Any, Iterator, Mapping

from . import SCHEMA_VERSION


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds")


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, timeout=60.0)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    connection.execute("PRAGMA synchronous = NORMAL")
    migrate(connection)
    return connection


@contextmanager
def transaction(connection: sqlite3.Connection) -> Iterator[sqlite3.Connection]:
    connection.execute("BEGIN IMMEDIATE")
    try:
        yield connection
    except BaseException:
        connection.rollback()
        raise
    else:
        connection.commit()


def migrate(connection: sqlite3.Connection) -> None:
    current = int(connection.execute("PRAGMA user_version").fetchone()[0])
    if current > SCHEMA_VERSION:
        raise RuntimeError(
            f"database schema {current} is newer than supported schema {SCHEMA_VERSION}"
        )
    if current == 0:
        connection.executescript(_SCHEMA_V1)
        connection.execute("PRAGMA user_version = 1")
        current = 1
    if current == 1:
        connection.executescript(_SCHEMA_V2)
        connection.execute("PRAGMA user_version = 2")
        current = 2
    if current == 2:
        connection.executescript(_SCHEMA_V3)
        connection.execute("PRAGMA user_version = 3")
        connection.commit()


_SCHEMA_V1 = r"""
CREATE TABLE source_sectors (
    sector_id INTEGER PRIMARY KEY,
    relative_path TEXT NOT NULL UNIQUE,
    size_bytes INTEGER NOT NULL,
    mtime_ns INTEGER NOT NULL,
    content_sha256 TEXT,
    extraction_rule_version TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('indexed', 'error')),
    feature_count INTEGER NOT NULL DEFAULT 0,
    error TEXT,
    indexed_at TEXT NOT NULL
);

CREATE TABLE features (
    feature_pk INTEGER PRIMARY KEY,
    feature_id TEXT NOT NULL UNIQUE,
    sector_id INTEGER NOT NULL REFERENCES source_sectors(sector_id) ON DELETE CASCADE,
    source_sector TEXT NOT NULL,
    node_index INTEGER NOT NULL,
    instance_index INTEGER NOT NULL,
    instance_id TEXT,
    category TEXT NOT NULL,
    node_type TEXT NOT NULL,
    resource_path TEXT,
    debug_name TEXT,
    appearance TEXT,
    x REAL NOT NULL,
    y REAL NOT NULL,
    z REAL NOT NULL,
    q_i REAL NOT NULL,
    q_j REAL NOT NULL,
    q_k REAL NOT NULL,
    q_r REAL NOT NULL,
    min_x REAL,
    min_y REAL,
    min_z REAL,
    max_x REAL,
    max_y REAL,
    max_z REAL,
    forward_x REAL,
    forward_y REAL,
    forward_z REAL,
    calibrated INTEGER NOT NULL DEFAULT 0,
    capture_enabled INTEGER NOT NULL DEFAULT 0,
    rule_id TEXT NOT NULL,
    extraction_rule_version TEXT NOT NULL,
    road_id TEXT,
    road_order INTEGER,
    tags TEXT NOT NULL DEFAULT '',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    UNIQUE(source_sector, node_index, instance_index, rule_id)
);

CREATE INDEX features_category_idx ON features(category);
CREATE INDEX features_road_idx ON features(road_id, road_order);
CREATE INDEX features_sector_idx ON features(sector_id);

CREATE VIRTUAL TABLE feature_rtree USING rtree(
    feature_pk, min_x, max_x, min_y, max_y
);

CREATE TRIGGER feature_rtree_insert AFTER INSERT ON features BEGIN
  INSERT INTO feature_rtree VALUES (new.feature_pk, new.x, new.x, new.y, new.y);
END;
CREATE TRIGGER feature_rtree_update AFTER UPDATE OF x, y ON features BEGIN
  UPDATE feature_rtree SET min_x=new.x, max_x=new.x, min_y=new.y, max_y=new.y
  WHERE feature_pk=new.feature_pk;
END;
CREATE TRIGGER feature_rtree_delete AFTER DELETE ON features BEGIN
  DELETE FROM feature_rtree WHERE feature_pk=old.feature_pk;
END;

CREATE VIRTUAL TABLE feature_fts USING fts5(
    feature_id UNINDEXED, name, category, resource_path, tags,
    tokenize='unicode61 separators ''\\/_-'''
);
CREATE TRIGGER feature_fts_insert AFTER INSERT ON features BEGIN
  INSERT INTO feature_fts(rowid, feature_id, name, category, resource_path, tags)
  VALUES (new.feature_pk, new.feature_id, coalesce(new.debug_name, ''), new.category,
          coalesce(new.resource_path, ''), new.tags);
END;
CREATE TRIGGER feature_fts_update AFTER UPDATE ON features BEGIN
  DELETE FROM feature_fts WHERE rowid=old.feature_pk;
  INSERT INTO feature_fts(rowid, feature_id, name, category, resource_path, tags)
  VALUES (new.feature_pk, new.feature_id, coalesce(new.debug_name, ''), new.category,
          coalesce(new.resource_path, ''), new.tags);
END;
CREATE TRIGGER feature_fts_delete AFTER DELETE ON features BEGIN
  DELETE FROM feature_fts WHERE rowid=old.feature_pk;
END;

CREATE TABLE roads (
    road_pk INTEGER PRIMARY KEY,
    road_id TEXT NOT NULL UNIQUE,
    name TEXT,
    points_json TEXT NOT NULL,
    length_m REAL NOT NULL,
    min_x REAL NOT NULL,
    max_x REAL NOT NULL,
    min_y REAL NOT NULL,
    max_y REAL NOT NULL,
    source_json TEXT NOT NULL,
    provenance_json TEXT NOT NULL DEFAULT '{}',
    planning_rule_version TEXT NOT NULL
);
CREATE VIRTUAL TABLE road_rtree USING rtree(road_pk, min_x, max_x, min_y, max_y);
CREATE TRIGGER road_rtree_insert AFTER INSERT ON roads BEGIN
  INSERT INTO road_rtree VALUES (new.road_pk, new.min_x, new.max_x, new.min_y, new.max_y);
END;
CREATE TRIGGER road_rtree_update AFTER UPDATE OF min_x, max_x, min_y, max_y ON roads BEGIN
  UPDATE road_rtree SET min_x=new.min_x, max_x=new.max_x, min_y=new.min_y, max_y=new.max_y
  WHERE road_pk=new.road_pk;
END;
CREATE TRIGGER road_rtree_delete AFTER DELETE ON roads BEGIN
  DELETE FROM road_rtree WHERE road_pk=old.road_pk;
END;

CREATE TABLE areas (
    area_pk INTEGER PRIMARY KEY,
    area_id TEXT NOT NULL UNIQUE,
    name TEXT,
    district TEXT,
    subdistrict TEXT,
    area_kind TEXT,
    min_x REAL NOT NULL,
    max_x REAL NOT NULL,
    min_y REAL NOT NULL,
    max_y REAL NOT NULL,
    min_z REAL,
    max_z REAL,
    source_resource TEXT,
    provenance_json TEXT NOT NULL DEFAULT '{}'
);
CREATE VIRTUAL TABLE area_rtree USING rtree(area_pk, min_x, max_x, min_y, max_y);
CREATE TRIGGER area_rtree_insert AFTER INSERT ON areas BEGIN
  INSERT INTO area_rtree VALUES (new.area_pk, new.min_x, new.max_x, new.min_y, new.max_y);
END;
CREATE TRIGGER area_rtree_update AFTER UPDATE OF min_x, max_x, min_y, max_y ON areas BEGIN
  UPDATE area_rtree SET min_x=new.min_x, max_x=new.max_x, min_y=new.min_y, max_y=new.max_y
  WHERE area_pk=new.area_pk;
END;
CREATE TRIGGER area_rtree_delete AFTER DELETE ON areas BEGIN
  DELETE FROM area_rtree WHERE area_pk=old.area_pk;
END;

CREATE TABLE fast_travel_points (
    fast_travel_id TEXT PRIMARY KEY,
    feature_id TEXT NOT NULL UNIQUE REFERENCES features(feature_id) ON DELETE CASCADE,
    record_id TEXT,
    name TEXT,
    x REAL NOT NULL,
    y REAL NOT NULL,
    z REAL NOT NULL,
    source_sector TEXT NOT NULL,
    provenance_json TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX fast_travel_xy_idx ON fast_travel_points(x, y);
CREATE VIRTUAL TABLE fast_travel_rtree USING rtree(
    fast_travel_pk, min_x, max_x, min_y, max_y
);
CREATE TRIGGER fast_travel_rtree_insert AFTER INSERT ON fast_travel_points BEGIN
  INSERT INTO fast_travel_rtree VALUES (new.rowid, new.x, new.x, new.y, new.y);
END;
CREATE TRIGGER fast_travel_rtree_update AFTER UPDATE OF x, y ON fast_travel_points BEGIN
  UPDATE fast_travel_rtree SET min_x=new.x, max_x=new.x, min_y=new.y, max_y=new.y
  WHERE fast_travel_pk=new.rowid;
END;
CREATE TRIGGER fast_travel_rtree_delete AFTER DELETE ON fast_travel_points BEGIN
  DELETE FROM fast_travel_rtree WHERE fast_travel_pk=old.rowid;
END;

CREATE TABLE places (
    place_pk INTEGER PRIMARY KEY,
    location_id TEXT NOT NULL UNIQUE,
    anchor_feature_id TEXT REFERENCES features(feature_id) ON DELETE CASCADE,
    category TEXT NOT NULL,
    direction TEXT NOT NULL DEFAULT 'outward',
    requested_x REAL NOT NULL,
    requested_y REAL NOT NULL,
    requested_z REAL NOT NULL,
    requested_yaw REAL NOT NULL,
    requested_pitch REAL NOT NULL DEFAULT 0,
    requested_roll REAL NOT NULL DEFAULT 0,
    forward_x REAL NOT NULL,
    forward_y REAL NOT NULL,
    forward_z REAL NOT NULL,
    actual_x REAL,
    actual_y REAL,
    actual_z REAL,
    actual_yaw REAL,
    actual_pitch REAL,
    actual_roll REAL,
    actual_fov REAL,
    resource_path TEXT,
    source_sector TEXT,
    road_id TEXT,
    nearest_fast_travel_id TEXT REFERENCES fast_travel_points(fast_travel_id),
    nearest_fast_travel_name TEXT,
    nearest_fast_travel_x REAL,
    nearest_fast_travel_y REAL,
    nearest_fast_travel_z REAL,
    nearest_fast_travel_distance_m REAL,
    nearest_street_road_id TEXT,
    nearest_street_name TEXT,
    nearest_street_x REAL,
    nearest_street_y REAL,
    nearest_street_z REAL,
    nearest_street_distance_m REAL,
    district TEXT,
    subdistrict TEXT,
    named_area TEXT,
    interior_state TEXT,
    extraction_rule_version TEXT NOT NULL,
    placement_rule_version TEXT NOT NULL,
    provenance_json TEXT NOT NULL DEFAULT '{}',
    queue_order INTEGER NOT NULL,
    queue_status TEXT NOT NULL DEFAULT 'pending'
      CHECK(queue_status IN ('pending','in_progress','captured','failed','disabled')),
    review_status TEXT NOT NULL DEFAULT 'needs_metadata'
      CHECK(review_status IN ('resolved','needs_metadata','needs_calibration','rejected')),
    publishable INTEGER NOT NULL DEFAULT 0,
    failure_code TEXT,
    failure_detail TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE INDEX places_queue_idx ON places(queue_status, queue_order);
CREATE INDEX places_category_idx ON places(category);

CREATE VIRTUAL TABLE place_fts USING fts5(
    location_id UNINDEXED, category, resource_path, fast_travel, street, district,
    subdistrict, named_area, tokenize='unicode61 separators ''\\/_-'''
);
CREATE TRIGGER place_fts_insert AFTER INSERT ON places BEGIN
  INSERT INTO place_fts(rowid, location_id, category, resource_path, fast_travel,
                        street, district, subdistrict, named_area)
  VALUES (new.place_pk, new.location_id, new.category, coalesce(new.resource_path,''),
          coalesce(new.nearest_fast_travel_name,''), coalesce(new.nearest_street_name,''),
          coalesce(new.district,''), coalesce(new.subdistrict,''), coalesce(new.named_area,''));
END;
CREATE TRIGGER place_fts_update AFTER UPDATE ON places BEGIN
  DELETE FROM place_fts WHERE rowid=old.place_pk;
  INSERT INTO place_fts(rowid, location_id, category, resource_path, fast_travel,
                        street, district, subdistrict, named_area)
  VALUES (new.place_pk, new.location_id, new.category, coalesce(new.resource_path,''),
          coalesce(new.nearest_fast_travel_name,''), coalesce(new.nearest_street_name,''),
          coalesce(new.district,''), coalesce(new.subdistrict,''), coalesce(new.named_area,''));
END;
CREATE TRIGGER place_fts_delete AFTER DELETE ON places BEGIN
  DELETE FROM place_fts WHERE rowid=old.place_pk;
END;

CREATE TABLE capture_sessions (
    session_id TEXT PRIMARY KEY,
    game_profile TEXT NOT NULL,
    capture_profile_json TEXT NOT NULL,
    runtime_path TEXT NOT NULL,
    started_at TEXT NOT NULL,
    ended_at TEXT,
    status TEXT NOT NULL,
    restoration_verified INTEGER NOT NULL DEFAULT 0,
    error TEXT
);

CREATE TABLE capture_attempts (
    attempt_id TEXT PRIMARY KEY,
    session_id TEXT NOT NULL REFERENCES capture_sessions(session_id),
    location_id TEXT NOT NULL REFERENCES places(location_id),
    command_id TEXT NOT NULL UNIQUE,
    attempt_number INTEGER NOT NULL,
    status TEXT NOT NULL,
    accepted_at TEXT,
    teleported_at TEXT,
    ready_at TEXT,
    captured_at TEXT,
    finished_at TEXT,
    teleport_to_ready_ms REAL,
    ready_to_capture_ms REAL,
    total_capture_ms REAL,
    ready_event_json TEXT,
    actual_pose_json TEXT,
    error_code TEXT,
    error_detail TEXT
);
CREATE INDEX attempts_location_idx ON capture_attempts(location_id, attempt_number);

CREATE TABLE captures (
    capture_id TEXT PRIMARY KEY,
    attempt_id TEXT NOT NULL UNIQUE REFERENCES capture_attempts(attempt_id),
    location_id TEXT NOT NULL REFERENCES places(location_id),
    png_path TEXT NOT NULL,
    sidecar_path TEXT NOT NULL,
    thumbnail_path TEXT NOT NULL,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    image_sha256 TEXT NOT NULL,
    metadata_sha256 TEXT NOT NULL,
    perceptual_hash TEXT,
    captured_at TEXT NOT NULL,
    validation_status TEXT NOT NULL,
    validation_json TEXT NOT NULL,
    UNIQUE(location_id, image_sha256)
);

CREATE TABLE metadata_overrides (
    override_id INTEGER PRIMARY KEY,
    target_type TEXT NOT NULL CHECK(target_type IN ('feature','road','area','place','fast_travel')),
    target_id TEXT NOT NULL,
    field_name TEXT NOT NULL,
    value_json TEXT NOT NULL,
    reviewed_by TEXT NOT NULL,
    reviewed_at TEXT NOT NULL,
    reason TEXT,
    UNIQUE(target_type, target_id, field_name)
);
"""


_SCHEMA_V2 = r"""
ALTER TABLE captures ADD COLUMN thumbnail_sha256 TEXT;
"""

_SCHEMA_V3 = r"""
ALTER TABLE places ADD COLUMN scope_status TEXT NOT NULL DEFAULT 'in_scope'
  CHECK(scope_status IN ('in_scope','out_of_scope'));
ALTER TABLE places ADD COLUMN scope_rule_id TEXT NOT NULL DEFAULT 'none';
ALTER TABLE places ADD COLUMN scope_rule_version TEXT NOT NULL DEFAULT 'none';
ALTER TABLE places ADD COLUMN scope_detail_json TEXT NOT NULL DEFAULT '{}';
CREATE INDEX places_scope_idx ON places(scope_status, queue_status, queue_order);
"""


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sector_is_current(
    connection: sqlite3.Connection,
    relative_path: str,
    size_bytes: int,
    mtime_ns: int,
    rule_version: str,
) -> bool:
    row = connection.execute(
        """SELECT size_bytes, mtime_ns, extraction_rule_version, status
           FROM source_sectors WHERE relative_path=?""",
        (relative_path,),
    ).fetchone()
    return bool(
        row
        and row["size_bytes"] == size_bytes
        and row["mtime_ns"] == mtime_ns
        and row["extraction_rule_version"] == rule_version
        and row["status"] == "indexed"
    )


def prepare_sector_feature_deletion(
    connection: sqlite3.Connection, sector_id: int
) -> None:
    """Detach durable place history from replaceable features in one sector.

    Feature extraction is rebuilt per sector. Unattempted planned places may
    cascade away with their old anchor, but a place referenced by a capture
    attempt must survive so its capture history remains valid. Cached nearest
    fast-travel links must also be cleared before their feature-backed rows can
    cascade away; planning restores them from the refreshed feature set.
    """
    connection.execute(
        """UPDATE places SET nearest_fast_travel_id=NULL
           WHERE nearest_fast_travel_id IN (
             SELECT fast_travel_id FROM fast_travel_points
             WHERE feature_id IN (
               SELECT feature_id FROM features WHERE sector_id=?
             )
           )""",
        (sector_id,),
    )
    connection.execute(
        """UPDATE places SET anchor_feature_id=NULL
           WHERE anchor_feature_id IN (
             SELECT feature_id FROM features WHERE sector_id=?
           )
           AND EXISTS (
             SELECT 1 FROM capture_attempts
             WHERE capture_attempts.location_id=places.location_id
           )""",
        (sector_id,),
    )


def replace_sector(
    connection: sqlite3.Connection,
    *,
    relative_path: str,
    size_bytes: int,
    mtime_ns: int,
    content_sha256: str | None,
    rule_version: str,
    features: list[Mapping[str, Any]],
) -> None:
    now = utc_now()
    with transaction(connection):
        connection.execute(
            """INSERT INTO source_sectors(
                   relative_path,size_bytes,mtime_ns,content_sha256,extraction_rule_version,
                   status,feature_count,error,indexed_at)
               VALUES(?,?,?,?,?,'indexed',?,NULL,?)
               ON CONFLICT(relative_path) DO UPDATE SET
                   size_bytes=excluded.size_bytes, mtime_ns=excluded.mtime_ns,
                   content_sha256=excluded.content_sha256,
                   extraction_rule_version=excluded.extraction_rule_version,
                   status='indexed', feature_count=excluded.feature_count,
                   error=NULL, indexed_at=excluded.indexed_at""",
            (
                relative_path,
                size_bytes,
                mtime_ns,
                content_sha256,
                rule_version,
                len(features),
                now,
            ),
        )
        sector_id = connection.execute(
            "SELECT sector_id FROM source_sectors WHERE relative_path=?",
            (relative_path,),
        ).fetchone()[0]
        prepare_sector_feature_deletion(connection, sector_id)
        connection.execute("DELETE FROM features WHERE sector_id=?", (sector_id,))
        statement = """INSERT INTO features(
            feature_id,sector_id,source_sector,node_index,instance_index,instance_id,
            category,node_type,resource_path,debug_name,appearance,x,y,z,q_i,q_j,q_k,q_r,
            min_x,min_y,min_z,max_x,max_y,max_z,forward_x,forward_y,forward_z,
            calibrated,capture_enabled,rule_id,extraction_rule_version,road_id,road_order,
            tags,metadata_json)
            VALUES(:feature_id,:sector_id,:source_sector,:node_index,:instance_index,:instance_id,
            :category,:node_type,:resource_path,:debug_name,:appearance,:x,:y,:z,:q_i,:q_j,:q_k,:q_r,
            :min_x,:min_y,:min_z,:max_x,:max_y,:max_z,:forward_x,:forward_y,:forward_z,
            :calibrated,:capture_enabled,:rule_id,:extraction_rule_version,:road_id,:road_order,
            :tags,:metadata_json)"""
        for feature in features:
            row = dict(feature)
            row["sector_id"] = sector_id
            connection.execute(statement, row)


def record_sector_error(
    connection: sqlite3.Connection,
    *,
    relative_path: str,
    size_bytes: int,
    mtime_ns: int,
    rule_version: str,
    error: str,
) -> None:
    with transaction(connection):
        connection.execute(
            """INSERT INTO source_sectors(
                   relative_path,size_bytes,mtime_ns,extraction_rule_version,status,
                   feature_count,error,indexed_at)
               VALUES(?,?,?,?,'error',0,?,?)
               ON CONFLICT(relative_path) DO UPDATE SET
                   size_bytes=excluded.size_bytes,mtime_ns=excluded.mtime_ns,
                   extraction_rule_version=excluded.extraction_rule_version,status='error',
                   feature_count=0,error=excluded.error,indexed_at=excluded.indexed_at""",
            (relative_path, size_bytes, mtime_ns, rule_version, error, utc_now()),
        )
        sector_id = connection.execute(
            "SELECT sector_id FROM source_sectors WHERE relative_path=?",
            (relative_path,),
        ).fetchone()[0]
        # A changed sector that no longer parses must not leave stale features
        # looking current in spatial or text indexes.
        prepare_sector_feature_deletion(connection, sector_id)
        connection.execute("DELETE FROM features WHERE sector_id=?", (sector_id,))


def apply_reviewed_overrides(
    connection: sqlite3.Connection, target_type: str, target_id: str
) -> dict[str, Any]:
    values: dict[str, Any] = {}
    for row in connection.execute(
        "SELECT field_name,value_json FROM metadata_overrides WHERE target_type=? AND target_id=?",
        (target_type, target_id),
    ):
        values[row["field_name"]] = json.loads(row["value_json"])
    return values


def status_counts(connection: sqlite3.Connection) -> dict[str, Any]:
    queue = {
        row["queue_status"]: row["count"]
        for row in connection.execute(
            "SELECT queue_status,COUNT(*) AS count FROM places GROUP BY queue_status"
        )
    }
    scope = {
        row["scope_status"]: row["count"]
        for row in connection.execute(
            "SELECT scope_status,COUNT(*) AS count FROM places GROUP BY scope_status"
        )
    }
    return {
        "sectors": connection.execute("SELECT COUNT(*) FROM source_sectors").fetchone()[
            0
        ],
        "sector_errors": connection.execute(
            "SELECT COUNT(*) FROM source_sectors WHERE status='error'"
        ).fetchone()[0],
        "features": connection.execute("SELECT COUNT(*) FROM features").fetchone()[0],
        "roads": connection.execute("SELECT COUNT(*) FROM roads").fetchone()[0],
        "places": connection.execute("SELECT COUNT(*) FROM places").fetchone()[0],
        "queue": queue,
        "scope": scope,
        "review": connection.execute(
            "SELECT COUNT(*) FROM places WHERE review_status!='resolved'"
        ).fetchone()[0],
        "publishable": connection.execute(
            "SELECT COUNT(*) FROM places WHERE publishable=1"
        ).fetchone()[0],
        "captures": connection.execute("SELECT COUNT(*) FROM captures").fetchone()[0],
    }
