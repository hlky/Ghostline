"""Paired scouting views for entrances, routes and elevated installations."""

from __future__ import annotations

import math
import sqlite3
from typing import Any, Mapping, Sequence

from .model import Quaternion, Vec3, game_yaw_degrees, morton_key_2d, outward_vector, stable_id

SURVEY_CATEGORIES = (
    "intercom", "elevator", "security_checkpoint", "security_device", "road_barrier", "antenna", "fast_travel", "drop_point", "access_point", "terminal",
)
GROUND_CATEGORIES = (
    "ai_workspot", "parking_space", "fake_door", "door_gate", "fast_travel", "terminal", "utility_device",
)


def _ground_reference(connection: sqlite3.Connection, anchor: Vec3, rules: Mapping[str, Any]):
    radius = float(rules.get("maximum_ground_reference_distance_m", 25))
    drop = float(rules.get("maximum_ground_reference_drop_m", 30))
    ground_categories = tuple(rules.get("ground_reference_categories", GROUND_CATEGORIES))
    rows = connection.execute(
        # CROSS JOIN keeps the spatial fence first; otherwise SQLite may scan
        # every workspot for every device through the category index.
        "SELECT f.* FROM feature_rtree r CROSS JOIN features f ON f.feature_pk=r.feature_pk "
        "WHERE r.max_x>=? AND r.min_x<=? AND r.max_y>=? AND r.min_y<=? "
        "AND f.z BETWEEN ? AND ? AND f.capture_enabled=1 AND f.calibrated=1 "
        f"AND f.category IN ({','.join('?' for _ in ground_categories)})",
        (anchor.x-radius, anchor.x+radius, anchor.y-radius, anchor.y+radius,
         anchor.z-drop, anchor.z+0.25, *ground_categories),
    ).fetchall()
    minimum = float(rules.get("minimum_ground_reference_distance_m", 4))
    height_ratio = float(rules.get("ground_reference_height_ratio", 2))
    candidates = [
        row for row in rows
        if max(minimum, height_ratio * abs(anchor.z-row["z"]))
        <= math.hypot(row["x"]-anchor.x, row["y"]-anchor.y) <= radius
    ]
    return min(candidates, default=None, key=lambda row: (
        (row["x"]-anchor.x)**2 + (row["y"]-anchor.y)**2 + 0.25*(row["z"]-anchor.z)**2,
        row["feature_id"],
    ))


def build_site_surveys(
    connection: sqlite3.Connection, config: Mapping[str, Any],
    runtime_areas: Sequence[Mapping[str, Any]] = (), *, category: str | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, dict[str, int]]]:
    from .planning import (
        REQUIRED_NAME_FIELDS, _deduplicate_candidate_coordinates, _metadata_for_point,
        _place_record, evaluate_scope,
    )

    version = str(config["placement_rule_version"])
    fallback = float(config.get("metadata_rules", {}).get("runtime_area_fallback_m", 500))
    profiles = config.get("site_survey_rules", {})
    records, unresolved, counts = [], [], {}
    ground_viewpoints = set()
    for family, rules in profiles.items():
        if category is not None and family != category:
            continue
        patterns = rules.get("resource_patterns", ())
        conditions = ["category=?", *("instr(lower(coalesce(resource_path,'')),?)>0" for _ in patterns)]
        rows = connection.execute(
            "SELECT * FROM features WHERE " + " OR ".join(conditions) + " ORDER BY feature_id",
            (family, *(pattern.lower() for pattern in patterns)),
        ).fetchall()
        anchors = []
        for row in rows:
            resource = str(row["resource_path"] or "").lower()
            if row["category"] != family and not any(pattern.lower() in resource for pattern in patterns):
                continue
            anchor = Vec3(row["x"], row["y"], row["z"])
            anchors.append({
                "location_id": row["feature_id"], "category": family,
                "requested_x": anchor.x, "requested_y": anchor.y, "requested_z": anchor.z,
                **evaluate_scope(anchor, config), "feature": row,
            })
        preferred = {row[0] for row in connection.execute(
            "SELECT anchor_feature_id FROM places WHERE category=? AND queue_status='captured'", (family,),
        )}
        retained, removed = _deduplicate_candidate_coordinates(
            anchors, {family: float(rules.get("minimum_anchor_separation_m", 0))}, preferred_ids=preferred,
        )
        summary = counts[family] = {"anchors": len(anchors), "deduplicated_anchors": removed, "deduplicated_viewpoint_pairs": 0, "pairs": 0, "unresolved_ground_references": 0}
        for entry in retained:
            row = entry["feature"]
            anchor = Vec3(row["x"], row["y"], row["z"])
            outward = Vec3(row["forward_x"], row["forward_y"], row["forward_z"]).normalized(horizontal=True)
            ground = None
            mode = rules["mode"]
            near = float(rules.get("near_distance_m", 3))
            far = float(rules.get("far_distance_m", 12))
            labels = rules["view_labels"]
            if mode == "usable_side_pair":
                outward = outward_vector(Quaternion(row["q_i"], row["q_j"], row["q_k"], row["q_r"]), rules["front_axis"])
                views = ((labels[0], anchor+outward*near, outward), (labels[1], anchor+outward*far, outward*-1))
            elif mode == "ground_context":
                ground = _ground_reference(connection, anchor, rules)
                if ground is None:
                    unresolved.append({"category": family, "feature_id": row["feature_id"], "resource": row["resource_path"], "anchor": anchor.as_dict(), "reason": "no_nearby_ground_reference"})
                    summary["unresolved_ground_references"] += 1
                    continue
                origin = Vec3(ground["x"], ground["y"], ground["z"])
                delta = anchor-origin
                toward = delta.normalized(horizontal=True) if delta.horizontal_length() > 0.01 else outward * -1
                viewpoint = (*tuple(round(value, 6) for value in (origin.x, origin.y, origin.z)), round(game_yaw_degrees(toward), 5) % 180)
                if viewpoint in ground_viewpoints:
                    summary["deduplicated_viewpoint_pairs"] += 1
                    continue
                ground_viewpoints.add(viewpoint)
                views = ((labels[0], origin, toward), (labels[1], origin, toward * -1))
            elif mode == "two_sides":
                views = ((labels[0], anchor+outward*near, outward*-1), (labels[1], anchor-outward*near, outward))
            elif mode == "entrance_lobby":
                origin = anchor+outward*near
                views = ((labels[0], origin, outward*-1), (labels[1], origin, outward))
            else:  # detail_approach
                views = ((labels[0], anchor+outward*near, outward*-1), (labels[1], anchor+outward*far, outward*-1))
            ids = {label: stable_id("place", row["feature_id"], family, label, version) for label, _, _ in views}
            pair_id = stable_id("pair", row["feature_id"], family, version)
            for label, requested, forward in views:
                resolved, provenance = _metadata_for_point(connection, requested, ids[label], fallback, runtime_areas)
                provenance.update({
                    "anchor": f"feature:{row['feature_id']}", "pose": f"placement_rule:{version}:site_survey_v1",
                    "capture_pair_id": pair_id, "view": label,
                    "paired_location_id": next(value for key, value in ids.items() if key != label),
                    "target_anchor": anchor.as_dict(), "viewpoint_strategy": mode,
                    "source_node_index": row["node_index"], "source_instance_index": row["instance_index"],
                    "source_instance_id": row["instance_id"],
                    "orientation": rules.get("orientation_evidence", "extracted local axis; view usefulness requires runtime review"),
                    "front_axis": rules.get("front_axis"),
                    "ground_z": "nearby reference height; FreeFly preserves planned XYZ" if ground else "serialized anchor height; FreeFly preserves planned XYZ",
                    "ground_reference": {"feature_id": ground["feature_id"], "category": ground["category"], "position": origin.as_dict()} if ground else None,
                })
                if family == "fast_travel":
                    import json

                    provenance["native_fast_travel"] = json.loads(row["metadata_json"]).get("fast_travel", {})
                record = _place_record(
                    location_id=ids[label], anchor_feature_id=row["feature_id"], category=family,
                    direction=label, requested=requested, forward=forward, resource_path=row["resource_path"],
                    source_sector=row["source_sector"], road_id=None,
                    extraction_version=row["extraction_rule_version"], placement_version=version,
                    metadata=resolved, provenance=provenance,
                    review_status="needs_metadata" if any(not resolved.get(field) for field in REQUIRED_NAME_FIELDS) else "resolved",
                )
                record["queue_order"] = morton_key_2d(requested.x, requested.y)
                records.append(record)
            summary["pairs"] += 1
    return records, unresolved, counts
