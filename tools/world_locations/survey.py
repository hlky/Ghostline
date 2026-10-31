"""Prepare independent survey views and a shared geographic capture route."""
from __future__ import annotations

import json
import math
from pathlib import Path
import sqlite3
from typing import Any, Mapping

from .database import connect, utc_now
from .hazards import record_hazard
from .model import morton_key_2d, stable_id
from .planning import evaluate_scope
from .model import Vec3


DETAIL_ROLES = {"terminal", "drop_point", "entrance"}


def recovery_candidates(place: Mapping[str, Any], config: Mapping[str, Any]) -> list[dict[str, float]]:
    """Only authorize small lateral translations that pass the existing scope rules."""
    yaw = math.radians(float(place["requested_yaw"]))
    candidates = []
    for distance in config.get("obstruction_recovery", {}).get("lateral_offsets_m", [1.5, -1.5, 2.0, -2.0]):
        pose = {axis: float(place[f"requested_{axis}"]) for axis in ("x", "y", "z", "yaw", "pitch", "roll")}
        pose["x"] += math.cos(yaw) * distance
        pose["y"] += math.sin(yaw) * distance
        record = {**dict(place), **{f"requested_{key}": value for key, value in pose.items()}}
        scope = evaluate_scope(Vec3(pose["x"], pose["y"], pose["z"]), config)
        if scope["scope_status"] == "in_scope" and not record_hazard(record, config):
            candidates.append(pose)
    return candidates


def expanded_views(place: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Requeue centers for a fresh pass; append new IDs for changed viewpoints."""
    original = dict(place)
    provenance = json.loads(original["provenance_json"])
    parking = original["category"] == "parking_space"
    offsets = [0, 90, 180, 270] if parking else [0] if original["direction"] in DETAIL_ROLES else [0, -45, 45]
    result = []
    for offset in offsets:
        row = dict(original)
        new_pose = parking or offset != 0
        row["queue_status"] = "pending"
        row["publishable"] = 0
        row["failure_code"] = row["failure_detail"] = None
        row["placement_rule_version"] = "survey-2.0.0"
        for key in row:
            if key.startswith("actual_"):
                row[key] = None
        if new_pose:
            row["location_id"] = stable_id("place", original["location_id"], "survey-v2", offset, 2 if parking else 0)
            row["direction"] = f"{original['direction']}_yaw_{offset:+d}"
        row["requested_yaw"] = (original["requested_yaw"] + offset) % 360
        row["requested_pitch"] = -20.0 if parking else original["requested_pitch"]
        row["requested_z"] = original["requested_z"] + (2.0 if parking else 0.0)
        yaw, pitch = math.radians(row["requested_yaw"]), math.radians(row["requested_pitch"])
        row.update(forward_x=-math.sin(yaw)*math.cos(pitch), forward_y=math.cos(yaw)*math.cos(pitch), forward_z=math.sin(pitch))
        note = dict(provenance)
        if new_pose:
            note["source_capture_pair_id"] = note.pop("capture_pair_id", None)
            note["source_paired_location_id"] = note.pop("paired_location_id", None)
        note["survey"] = {
            "version": 2, "parent_location_id": original["location_id"],
            "parent_view": original["direction"], "yaw_offset_degrees": offset,
            "height_offset_m": 2.0 if parking else 0.0,
            "position_frame": "player_root", "orientation_frame": "active_camera",
            "station_id": stable_id("station", *(round(row[f"requested_{axis}"], 3) for axis in ("x", "y", "z"))),
        }
        row["provenance_json"] = json.dumps(note, separators=(",", ":"), sort_keys=True)
        row["updated_at"] = utc_now()
        result.append(row)
    return result


def queue_survey_views(connection: sqlite3.Connection, originals: list[dict[str, Any]], config: Mapping[str, Any] | None = None) -> None:
    """Requeue a complete survey in its own workspace, retaining capture history."""
    parking_stations = set()
    columns = [r[1] for r in connection.execute("PRAGMA table_info(places)") if r[1] != "place_pk"]
    fields, placeholders = ",".join(columns), ",".join("?" for _ in columns)
    updates = ",".join(f"{k}=excluded.{k}" for k in columns if k != "location_id")
    insert = f"INSERT INTO places({fields}) VALUES({placeholders}) ON CONFLICT(location_id) DO UPDATE SET {updates}"
    pending = []
    with connection:
        connection.execute("UPDATE capture_sessions SET status='error',ended_at=?,error='snapshot of another controller; original session unchanged' WHERE status='running'", (utc_now(),))
        for original in originals:
            if original["category"] == "parking_space":
                connection.execute("UPDATE places SET queue_status='disabled',publishable=0 WHERE location_id=?", (original["location_id"],))
                station = (original["anchor_feature_id"], *(round(original[f"requested_{axis}"], 3) for axis in ("x", "y", "z")))
                if station in parking_stations:
                    continue
                parking_stations.add(station)
            for row in expanded_views(original):
                if config and original["category"] == "parking_space":
                    scope = evaluate_scope(Vec3(*(row[f"requested_{a}"] for a in "xyz")), config)
                    hazard = record_hazard(row, config)
                    if hazard or scope["scope_status"] != "in_scope":
                        row.update(hazard or scope)
                        row["queue_status"] = "disabled"
                connection.execute(insert, [row.get(k) for k in columns])
                if row["queue_status"] == "pending":
                    pending.append(row)
        # One global route: coarse Morton locality then all headings at each stop.
        pending.sort(key=lambda r: (
            morton_key_2d(r["requested_x"], r["requested_y"]),
            tuple(round(r[f"requested_{axis}"], 3) for axis in ("x", "y", "z")),
            abs(json.loads(r["provenance_json"])["survey"]["yaw_offset_degrees"]), r["location_id"],
        ))
        connection.executemany("UPDATE places SET queue_order=? WHERE location_id=?", ((i, r["location_id"]) for i, r in enumerate(pending)))


def prepare_survey(destination: Path, sources: list[Path], config: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Snapshot sources without acquiring their controller locks or changing them."""
    if destination.exists():
        raise ValueError(f"Survey database already exists; refusing to replace {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    seed = sqlite3.connect(sources[0].resolve().as_uri() + "?mode=ro", uri=True)
    target = sqlite3.connect(destination)
    seed.backup(target)
    seed.close()
    target.close()
    connection = connect(destination)
    connection.close()
    connection = sqlite3.connect(destination.resolve().as_uri() + "?mode=rw", uri=True)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys=ON")
    connection.execute("PRAGMA journal_mode=WAL")
    try:
        with connection:
            for table in ("captures", "capture_attempts", "capture_sessions", "places", "metadata_overrides"):
                connection.execute(f"DELETE FROM {table}")
        for source in sources:
            connection.execute("ATTACH DATABASE ? AS survey_source", (source.resolve().as_uri() + "?mode=ro",))
            with connection:
                # Related geographic IDs can differ across historical category snapshots.
                for table, pk in (("roads", "road_pk"), ("fast_travel_points", "fast_travel_pk")):
                    columns = [r[1] for r in connection.execute(f"PRAGMA table_info({table})") if r[1] != pk]
                    fields = ",".join(columns)
                    connection.execute(f"INSERT OR IGNORE INTO {table}({fields}) SELECT {fields} FROM survey_source.{table}")
                fields = ",".join(r[1] for r in connection.execute("PRAGMA table_info(places)") if r[1] != "place_pk")
                connection.execute(f"INSERT OR IGNORE INTO places({fields}) SELECT {fields} FROM survey_source.places")
                for table in ("capture_sessions", "capture_attempts", "captures"):
                    connection.execute(f"INSERT OR IGNORE INTO {table} SELECT * FROM survey_source.{table}")
                fields = ",".join(r[1] for r in connection.execute("PRAGMA table_info(metadata_overrides)") if r[1] != "override_id")
                connection.execute(f"INSERT OR IGNORE INTO metadata_overrides({fields}) SELECT {fields} FROM survey_source.metadata_overrides")
            connection.execute("DETACH DATABASE survey_source")
        originals = [dict(r) for r in connection.execute("SELECT * FROM places WHERE scope_status='in_scope' AND queue_status!='disabled' AND review_status NOT IN ('rejected','needs_calibration') ORDER BY location_id")]
        queue_survey_views(connection, originals, config)
        errors = connection.execute("PRAGMA foreign_key_check").fetchall()
        if errors:
            raise ValueError(f"Survey snapshot has foreign-key errors: {errors[:3]}")
        return {
            "database": str(destination), "sources": [str(p) for p in sources],
            "pending_by_category": dict(connection.execute("SELECT category,count(*) FROM places WHERE queue_status='pending' GROUP BY category")),
            "preserved_captures": connection.execute("SELECT count(*) FROM captures").fetchone()[0],
            "prepared_at": utc_now(), "route": "64m Morton cells; all views at each spatial station",
        }
    finally:
        connection.close()
