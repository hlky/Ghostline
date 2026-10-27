"""Reviewed lethal-volume exclusions, shared by planning and queue execution."""

from __future__ import annotations

import json
import math
import sqlite3
from typing import Any, Mapping

from .database import json_text, transaction, utc_now
from .model import Quaternion, Vec3


def validate_hazard_rules(config: Mapping[str, Any]) -> None:
    ids = [rule["id"] for rule in config.get("hazard_rules", ())]
    if len(set(ids)) != len(ids):
        raise ValueError("hazard IDs must be unique")
    for rule in config.get("hazard_rules", ()):
        if rule.get("type") not in {"polygon", "prism"}:
            raise ValueError(f"unsupported hazard type: {rule.get('type')}")
        points = rule.get("outline", [])
        if len(points) < 3 or any(len(p) != 2 for p in points):
            raise ValueError("hazard outline requires at least three XY points")
        numbers = [v for p in points for v in p]
        numbers.extend(rule.get("origin", {}).values())
        numbers.extend(rule.get("rotation", {}).values())
        numbers.append(rule.get("margin_m", 0))
        if rule["type"] == "prism":
            numbers.extend([rule["min_z"], rule["max_z"]])
            if rule["min_z"] > rule["max_z"]:
                raise ValueError("hazard height is reversed")
        if any(isinstance(n, bool) or not math.isfinite(float(n)) for n in numbers):
            raise ValueError("hazard coordinates must be finite")
        if rule.get("margin_m", 0) < 0:
            raise ValueError("hazard margin must be nonnegative")


def _inside(x: float, y: float, points: list, margin: float) -> bool:
    inside = False
    for a, b in zip(points, [*points[1:], points[0]]):
        dx, dy = b[0] - a[0], b[1] - a[1]
        length2 = dx * dx + dy * dy
        t = max(0, min(1, ((x-a[0])*dx + (y-a[1])*dy) / length2)) if length2 else 0
        if math.hypot(x-a[0]-t*dx, y-a[1]-t*dy) <= margin:
            return True
        if (a[1] > y) != (b[1] > y) and x < (b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:
            inside = not inside
    return inside


def hazard_at_point(point: Vec3, config: Mapping[str, Any]) -> dict[str, Any] | None:
    for rule in config.get("hazard_rules", ()):
        local = point
        if rule["type"] == "prism":
            origin = Vec3.from_mapping(rule["origin"])
            rotation = Quaternion.from_mapping(rule["rotation"])
            local = Quaternion(-rotation.i, -rotation.j, -rotation.k, rotation.r).rotate(point-origin)
        margin = float(rule.get("margin_m", 0))
        if rule["type"] == "prism" and not rule["min_z"]-margin <= local.z <= rule["max_z"]+margin:
            continue
        if _inside(local.x, local.y, rule["outline"], margin):
            return {
                "scope_status": "out_of_scope", "scope_rule_id": rule["id"],
                "scope_rule_version": str(config["hazard_rule_version"]),
                "scope_detail_json": json_text({
                    "reason": rule["reason"], "evidence": rule["evidence"],
                    "margin_m": margin, "hazard": True,
                }),
            }
    return None


def record_hazard(record: Mapping[str, Any], config: Mapping[str, Any]) -> dict[str, Any] | None:
    points = [Vec3(*(float(record[f"requested_{axis}"]) for axis in "xyz"))]
    provenance = json.loads(record.get("provenance_json") or "{}")
    anchor = provenance.get("target_anchor") or provenance.get("door_anchor")
    if anchor:
        points.append(Vec3.from_mapping(anchor))
    for point in points:
        result = hazard_at_point(point, config)
        if result:
            return result
    # Retain explicit reviewed Border Crossing labels even if spatial metadata
    # uses a slightly different outline than the serialized location volume.
    name = str(record.get("named_area") or "").lower().replace("_", " ")
    if "border crossing" in name:
        rule = next((r for r in config.get("hazard_rules", ()) if r["id"] == "border_crossing"), None)
        if rule:
            return {"scope_status": "out_of_scope", "scope_rule_id": rule["id"],
                    "scope_rule_version": str(config["hazard_rule_version"]),
                    "scope_detail_json": json_text({"reason": rule["reason"], "named_area": name, "hazard": True})}
    return None


def apply_hazard_exclusions(connection: sqlite3.Connection, config: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Only change matched rows; preserve poses, pair IDs and captured evidence."""
    rows = [dict(row) for row in connection.execute("SELECT * FROM places")]
    matches = {row["location_id"]: result for row in rows if (result := record_hazard(row, config))}
    pairs: dict[str, dict] = {}
    for row in rows:
        pair = json.loads(row["provenance_json"]).get("capture_pair_id")
        if pair and row["location_id"] in matches:
            pairs[pair] = matches[row["location_id"]]
    for row in rows:
        pair = json.loads(row["provenance_json"]).get("capture_pair_id")
        if pair in pairs:
            matches.setdefault(row["location_id"], pairs[pair])
    changes = []
    with transaction(connection):
        for row in rows:
            result = matches.get(row["location_id"])
            if result is None or (row["scope_status"] == "out_of_scope" and row["scope_rule_id"] == result["scope_rule_id"]):
                continue
            changes.append({"location_id": row["location_id"], "before": row, "exclusion": result})
            connection.execute(
                """UPDATE places SET scope_status=:scope_status,scope_rule_id=:scope_rule_id,
                scope_rule_version=:scope_rule_version,scope_detail_json=:scope_detail_json,
                queue_status=CASE WHEN queue_status='captured' THEN queue_status ELSE 'disabled' END,
                publishable=0,updated_at=:now WHERE location_id=:location_id""",
                {**result, "now": utc_now(), "location_id": row["location_id"]},
            )
    return changes
