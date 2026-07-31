"""Deterministic conversion of indexed features into capture destinations."""

from __future__ import annotations

from collections import defaultdict
import json
import math
import re
import sqlite3
from typing import Any, Iterable, Mapping, Sequence

from .database import apply_reviewed_overrides, json_text, transaction, utc_now
from .model import (
    Bounds,
    Quaternion,
    Vec3,
    closest_point_on_segment_2d,
    game_yaw_degrees,
    interpolate_polyline,
    morton_key_2d,
    polyline_length,
    stable_id,
)


REQUIRED_NAME_FIELDS = ("nearest_fast_travel_name", "nearest_street_name", "named_area")


def resolve_metadata(
    runtime: Mapping[str, Any] | None,
    spatial: Mapping[str, Any] | None,
    reviewed_overrides: Mapping[str, Any] | None,
) -> tuple[dict[str, Any], dict[str, str]]:
    """Resolve metadata using the project's explicit source precedence."""
    sources = (
        ("runtime", runtime or {}),
        ("spatial", spatial or {}),
        ("reviewed_override", reviewed_overrides or {}),
    )
    fields = set().union(*(set(values) for _, values in sources))
    resolved: dict[str, Any] = {}
    provenance: dict[str, str] = {}
    for field in sorted(fields):
        for source, values in sources:
            value = values.get(field)
            if value is not None and value != "":
                resolved[field] = value
                provenance[field] = source
                break
    return resolved, provenance


def _row_vec(row: Mapping[str, Any]) -> Vec3:
    return Vec3(float(row["x"]), float(row["y"]), float(row["z"]))


def _feature_bounds(row: Mapping[str, Any]) -> Bounds | None:
    if row["min_x"] is None or row["max_x"] is None:
        return None
    return Bounds(
        Vec3(float(row["min_x"]), float(row["min_y"]), float(row["min_z"])),
        Vec3(float(row["max_x"]), float(row["max_y"]), float(row["max_z"])),
    )


def _ordered_road_rows(rows: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    ordered_values = [row for row in rows if row["road_order"] is not None]
    if len(ordered_values) == len(rows) and len(
        {row["road_order"] for row in rows}
    ) == len(rows):
        return sorted(rows, key=lambda row: (row["road_order"], row["feature_id"]))
    remaining = sorted(rows, key=lambda row: row["feature_id"])
    if not remaining:
        return []
    ordered = [remaining.pop(0)]
    while remaining:
        tail = _row_vec(ordered[-1])
        next_index = min(
            range(len(remaining)),
            key=lambda index: (
                tail.distance_2d(_row_vec(remaining[index])),
                remaining[index]["feature_id"],
            ),
        )
        ordered.append(remaining.pop(next_index))
    return ordered


def _deduplicate_road_rows(
    rows: Sequence[Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    result: list[Mapping[str, Any]] = []
    for row in _ordered_road_rows(rows):
        point = _row_vec(row)
        if result and point.distance_2d(_row_vec(result[-1])) < 0.25:
            continue
        result.append(row)
    return result


def _split_road_branches(
    road_id: str, rows: Sequence[Mapping[str, Any]], *, maximum_link_m: float = 250.0
) -> list[tuple[str, list[Mapping[str, Any]]]]:
    """A proxy folder is one branch; large discontinuities become explicit branches."""
    ordered = _deduplicate_road_rows(rows)
    if not ordered:
        return []
    branches: list[list[Mapping[str, Any]]] = [[ordered[0]]]
    for row in ordered[1:]:
        if _row_vec(branches[-1][-1]).distance_2d(_row_vec(row)) > maximum_link_m:
            branches.append([row])
        else:
            branches[-1].append(row)
    if len(branches) == 1:
        return [(road_id, branches[0])]
    return [
        (f"{road_id}:branch-{index + 1}", branch)
        for index, branch in enumerate(branches)
    ]


def rebuild_fast_travel(connection: sqlite3.Connection) -> int:
    rows = connection.execute(
        "SELECT * FROM features WHERE category='fast_travel'"
    ).fetchall()
    with transaction(connection):
        connection.execute("UPDATE places SET nearest_fast_travel_id=NULL")
        connection.execute("DELETE FROM fast_travel_points")
        for row in rows:
            metadata = json.loads(row["metadata_json"])
            extracted = metadata.get("fast_travel", {})
            marker = extracted.get("marker_ref")
            record = extracted.get("point_record")
            fast_travel_id = stable_id("ftp", marker or row["feature_id"], record)
            overrides = apply_reviewed_overrides(
                connection, "fast_travel", fast_travel_id
            )
            resolved, provenance = resolve_metadata(None, {"name": marker}, overrides)
            connection.execute(
                """INSERT INTO fast_travel_points(
                       fast_travel_id,feature_id,record_id,name,x,y,z,source_sector,provenance_json)
                   VALUES(?,?,?,?,?,?,?,?,?)""",
                (
                    fast_travel_id,
                    row["feature_id"],
                    str(record) if record is not None else None,
                    resolved.get("name"),
                    row["x"],
                    row["y"],
                    row["z"],
                    row["source_sector"],
                    json_text(provenance),
                ),
            )
    return len(rows)


def rebuild_roads(connection: sqlite3.Connection, placement_version: str) -> int:
    grouped: dict[str, list[sqlite3.Row]] = defaultdict(list)
    for row in connection.execute(
        "SELECT * FROM features WHERE category='road' AND road_id IS NOT NULL"
    ):
        grouped[row["road_id"]].append(row)
    records: list[dict[str, Any]] = []
    for source_road_id in sorted(grouped):
        for road_id, branch_rows in _split_road_branches(
            source_road_id, grouped[source_road_id]
        ):
            points = [_row_vec(row) for row in branch_rows]
            if not points:
                continue
            overrides = apply_reviewed_overrides(connection, "road", road_id)
            resolved, provenance = resolve_metadata(None, {}, overrides)
            records.append(
                {
                    "road_id": road_id,
                    "name": resolved.get("name"),
                    "points_json": json_text([point.as_dict() for point in points]),
                    "length_m": polyline_length(points),
                    "min_x": min(point.x for point in points),
                    "max_x": max(point.x for point in points),
                    "min_y": min(point.y for point in points),
                    "max_y": max(point.y for point in points),
                    "source_json": json_text(
                        [row["feature_id"] for row in branch_rows]
                    ),
                    "provenance_json": json_text(
                        {
                            **provenance,
                            "geometry": "streamingsector:worldRoadProxyMeshNode proxy centers",
                            "branching": "resource spline folder; split at discontinuities",
                        }
                    ),
                    "planning_rule_version": placement_version,
                }
            )
    with transaction(connection):
        connection.execute("DELETE FROM roads")
        connection.executemany(
            """INSERT INTO roads(road_id,name,points_json,length_m,min_x,max_x,min_y,max_y,
                                 source_json,provenance_json,planning_rule_version)
               VALUES(:road_id,:name,:points_json,:length_m,:min_x,:max_x,:min_y,:max_y,
                      :source_json,:provenance_json,:planning_rule_version)""",
            records,
        )
    return len(records)


def _world_aabb(
    row: Mapping[str, Any],
) -> tuple[float, float, float, float, float, float] | None:
    bounds = _feature_bounds(row)
    if bounds is None:
        return None
    position = _row_vec(row)
    rotation = Quaternion(
        float(row["q_i"]), float(row["q_j"]), float(row["q_k"]), float(row["q_r"])
    )
    corners = [
        position + rotation.rotate(Vec3(x, y, z))
        for x in (bounds.minimum.x, bounds.maximum.x)
        for y in (bounds.minimum.y, bounds.maximum.y)
        for z in (bounds.minimum.z, bounds.maximum.z)
    ]
    if not corners:
        return None
    return (
        min(point.x for point in corners),
        max(point.x for point in corners),
        min(point.y for point in corners),
        max(point.y for point in corners),
        min(point.z for point in corners),
        max(point.z for point in corners),
    )


def _area_display_name(value: str | None) -> str | None:
    if not value:
        return None
    name = value.strip().strip("{}").strip()
    name = re.sub(r"_loc_area(?:_new)?$", "", name, flags=re.IGNORECASE)
    return name.replace("_", " ").strip().title() or None


def _point_in_polygon(x: float, y: float, polygon: Sequence[Sequence[float]]) -> bool:
    inside = False
    previous_x, previous_y = polygon[-1]
    for current_x, current_y in polygon:
        if (current_y > y) != (previous_y > y):
            crossing_x = (previous_x - current_x) * (y - current_y) / (
                previous_y - current_y
            ) + current_x
            if x < crossing_x:
                inside = not inside
        previous_x, previous_y = current_x, current_y
    return inside


def rebuild_areas(connection: sqlite3.Connection) -> int:
    records: list[dict[str, Any]] = []
    for row in connection.execute("SELECT * FROM features WHERE category='area'"):
        metadata = json.loads(row["metadata_json"])
        outline = metadata.get("area_outline", [])
        polygon: list[list[float]] = []
        if outline:
            position = _row_vec(row)
            rotation = Quaternion(
                float(row["q_i"]),
                float(row["q_j"]),
                float(row["q_k"]),
                float(row["q_r"]),
            )
            for point in outline:
                world = position + rotation.rotate(
                    Vec3(float(point["x"]), float(point["y"]), float(point["z"]))
                )
                polygon.append([world.x, world.y])
            aabb = (
                min(point[0] for point in polygon),
                max(point[0] for point in polygon),
                min(point[1] for point in polygon),
                max(point[1] for point in polygon),
                None,
                None,
            )
        else:
            aabb = _world_aabb(row)
        if not aabb:
            continue
        area_id = stable_id("area", row["feature_id"])
        spatial = {"name": _area_display_name(row["debug_name"])}
        overrides = apply_reviewed_overrides(connection, "area", area_id)
        resolved, provenance = resolve_metadata(None, spatial, overrides)
        provenance.update(
            {
                "geometry": "streamingsector:worldLocationAreaNode AreaShapeOutline"
                if polygon
                else "streamingsector:node bounds",
                "district_id": metadata.get("district_id"),
                "polygon_xy": polygon,
            }
        )
        records.append(
            {
                "area_id": area_id,
                "name": resolved.get("name"),
                "district": resolved.get("district"),
                "subdistrict": resolved.get("subdistrict"),
                "area_kind": resolved.get("area_kind", row["node_type"]),
                "min_x": aabb[0],
                "max_x": aabb[1],
                "min_y": aabb[2],
                "max_y": aabb[3],
                "min_z": aabb[4],
                "max_z": aabb[5],
                "source_resource": row["resource_path"] or row["source_sector"],
                "provenance_json": json_text(provenance),
            }
        )
    with transaction(connection):
        connection.execute("DELETE FROM areas")
        connection.executemany(
            """INSERT INTO areas(area_id,name,district,subdistrict,area_kind,min_x,max_x,
                                  min_y,max_y,min_z,max_z,source_resource,provenance_json)
               VALUES(:area_id,:name,:district,:subdistrict,:area_kind,:min_x,:max_x,
                      :min_y,:max_y,:min_z,:max_z,:source_resource,:provenance_json)""",
            records,
        )
    return len(records)


def _nearest_fast_travel(connection: sqlite3.Connection, point: Vec3) -> dict[str, Any]:
    row = None
    for radius in (100.0, 500.0, 2_000.0, 10_000.0, 50_000.0):
        row = connection.execute(
            """SELECT f.*, ((f.x-?)*(f.x-?)+(f.y-?)*(f.y-?)) AS distance_squared
               FROM fast_travel_rtree r
               JOIN fast_travel_points f ON f.rowid=r.fast_travel_pk
               WHERE r.max_x>=? AND r.min_x<=? AND r.max_y>=? AND r.min_y<=?
               ORDER BY distance_squared LIMIT 1""",
            (
                point.x,
                point.x,
                point.y,
                point.y,
                point.x - radius,
                point.x + radius,
                point.y - radius,
                point.y + radius,
            ),
        ).fetchone()
        if row:
            break
    if not row:
        return {}
    return {
        "nearest_fast_travel_id": row["fast_travel_id"],
        "nearest_fast_travel_name": row["name"],
        "nearest_fast_travel_x": row["x"],
        "nearest_fast_travel_y": row["y"],
        "nearest_fast_travel_z": row["z"],
        "nearest_fast_travel_distance_m": math.sqrt(row["distance_squared"]),
    }


def _nearest_road(connection: sqlite3.Connection, point: Vec3) -> dict[str, Any]:
    candidates: list[sqlite3.Row] = []
    for radius in (100.0, 500.0, 2_000.0, 10_000.0, 50_000.0):
        candidates = connection.execute(
            """SELECT road.* FROM road_rtree r JOIN roads road ON road.road_pk=r.road_pk
               WHERE r.max_x>=? AND r.min_x<=? AND r.max_y>=? AND r.min_y<=?""",
            (point.x - radius, point.x + radius, point.y - radius, point.y + radius),
        ).fetchall()
        if candidates:
            break
    # R-tree finds nearby splines; exact segment distance chooses among them.
    best: tuple[float, sqlite3.Row, Vec3] | None = None
    for row in candidates:
        points = [
            Vec3(float(value["x"]), float(value["y"]), float(value["z"]))
            for value in json.loads(row["points_json"])
        ]
        candidates = (
            zip(points, points[1:]) if len(points) > 1 else ((points[0], points[0]),)
        )
        for left, right in candidates:
            closest, distance = closest_point_on_segment_2d(point, left, right)
            if best is None or distance < best[0]:
                best = (distance, row, closest)
    if best is None:
        return {}
    distance, row, closest = best
    return {
        "nearest_street_road_id": row["road_id"],
        "nearest_street_name": row["name"],
        "nearest_street_x": closest.x,
        "nearest_street_y": closest.y,
        "nearest_street_z": closest.z,
        "nearest_street_distance_m": distance,
    }


def _containing_area(connection: sqlite3.Connection, point: Vec3) -> dict[str, Any]:
    rows = connection.execute(
        """SELECT a.*,(a.max_x-a.min_x)*(a.max_y-a.min_y) AS footprint
           FROM area_rtree r JOIN areas a ON a.area_pk=r.area_pk
           WHERE r.min_x<=? AND r.max_x>=? AND r.min_y<=? AND r.max_y>=?
             AND (a.min_z IS NULL OR a.min_z<=?) AND (a.max_z IS NULL OR a.max_z>=?)
           ORDER BY footprint ASC""",
        (point.x, point.x, point.y, point.y, point.z, point.z),
    ).fetchall()
    for row in rows:
        polygon = json.loads(row["provenance_json"]).get("polygon_xy", [])
        if polygon and not _point_in_polygon(point.x, point.y, polygon):
            continue
        return {
            "district": row["district"],
            "subdistrict": row["subdistrict"],
            "named_area": row["name"],
        }
    return {}


def _metadata_for_point(
    connection: sqlite3.Connection,
    point: Vec3,
    location_id: str,
    runtime_area_fallback_m: float = 500.0,
    runtime_area_observations: Sequence[Mapping[str, Any]] = (),
) -> tuple[dict[str, Any], dict[str, str]]:
    nearest_runtime_area: dict[str, Any] = {}
    if runtime_area_fallback_m > 0.0 and runtime_area_observations:
        candidates = (
            (
                (point.x - float(row["requested_x"])) ** 2
                + (point.y - float(row["requested_y"])) ** 2,
                row,
            )
            for row in runtime_area_observations
            if abs(point.x - float(row["requested_x"])) <= runtime_area_fallback_m
            and abs(point.y - float(row["requested_y"])) <= runtime_area_fallback_m
        )
        nearest = min(candidates, default=None, key=lambda value: value[0])
        if nearest and nearest[0] <= runtime_area_fallback_m**2:
            row = nearest[1]
            nearest_runtime_area = {
                "district": row["district"],
                "subdistrict": row["subdistrict"],
                "named_area": row["named_area"],
            }
    spatial = {
        **_nearest_fast_travel(connection, point),
        **_nearest_road(connection, point),
        **_containing_area(connection, point),
        **nearest_runtime_area,
    }
    overrides = apply_reviewed_overrides(connection, "place", location_id)
    return resolve_metadata(None, spatial, overrides)


def _runtime_area_observations(
    connection: sqlite3.Connection,
) -> list[Mapping[str, Any]]:
    return list(
        connection.execute(
            """SELECT requested_x,requested_y,district,subdistrict,named_area
               FROM places
               WHERE named_area IS NOT NULL AND trim(named_area)!=''
                 AND json_extract(provenance_json,'$.named_area')='runtime'"""
        )
    )


def evaluate_scope(point: Vec3, config: Mapping[str, Any]) -> dict[str, Any]:
    """Classify a point without discarding its indexed source feature.

    Exclusion half-planes are described by a point on the boundary and its
    tangent. An explicit in-scope reference chooses the normal direction; an
    out-of-scope reference guards against an accidentally reversed rule.
    """
    version = str(config.get("scope_rule_version", "none"))
    evaluations: list[dict[str, Any]] = []
    for rule in config.get("scope_rules", []):
        if not rule.get("enabled", True):
            continue
        rule_id = str(rule.get("id", "unnamed_scope_rule"))
        if rule.get("type") != "exclude_negative_half_plane":
            raise ValueError(f"unsupported scope rule type for {rule_id!r}")

        origin = rule["boundary_origin"]
        tangent = rule["boundary_tangent"]
        origin_x = float(origin["x"])
        origin_y = float(origin["y"])
        tangent_x = float(tangent["x"])
        tangent_y = float(tangent["y"])
        tangent_length = math.hypot(tangent_x, tangent_y)
        if tangent_length <= 1e-9:
            raise ValueError(f"scope rule {rule_id!r} has a zero-length tangent")

        # Either perpendicular is valid until the in-scope q000 reference
        # selects the side that points back into Night City.
        normal_x = -tangent_y / tangent_length
        normal_y = tangent_x / tangent_length
        inside = rule["in_scope_reference"]
        inside_signed = (
            (float(inside["x"]) - origin_x) * normal_x
            + (float(inside["y"]) - origin_y) * normal_y
        )
        if inside_signed < 0.0:
            normal_x = -normal_x
            normal_y = -normal_y
            inside_signed = -inside_signed
        if inside_signed <= 1e-6:
            raise ValueError(
                f"scope rule {rule_id!r} has an in-scope reference on its boundary"
            )

        outside = rule.get("out_of_scope_reference")
        if outside:
            outside_signed = (
                (float(outside["x"]) - origin_x) * normal_x
                + (float(outside["y"]) - origin_y) * normal_y
            )
            if outside_signed >= 0.0:
                raise ValueError(
                    f"scope rule {rule_id!r} does not separate its q000 references"
                )

        signed_distance = (
            (point.x - origin_x) * normal_x + (point.y - origin_y) * normal_y
        )
        margin = float(rule.get("margin_m", 0.0))
        evaluation = {
            "rule_id": rule_id,
            "signed_distance_m": signed_distance,
            "margin_m": margin,
            "boundary_name": rule.get("boundary_name"),
        }
        evaluations.append(evaluation)
        if signed_distance < -margin:
            return {
                "scope_status": "out_of_scope",
                "scope_rule_id": rule_id,
                "scope_rule_version": version,
                "scope_detail_json": json_text(
                    {
                        **evaluation,
                        "reason": rule.get("exclusion_reason", "excluded half-plane"),
                    }
                ),
            }

    nearest = min(
        evaluations,
        key=lambda value: abs(float(value["signed_distance_m"])),
        default=None,
    )
    return {
        "scope_status": "in_scope",
        "scope_rule_id": str(nearest["rule_id"]) if nearest else "none",
        "scope_rule_version": version,
        "scope_detail_json": json_text(nearest or {}),
    }


def _apply_scope(
    records: Iterable[dict[str, Any]], config: Mapping[str, Any]
) -> list[dict[str, Any]]:
    values = list(records)
    for record in values:
        record.update(
            evaluate_scope(
                Vec3(
                    float(record["requested_x"]),
                    float(record["requested_y"]),
                    float(record["requested_z"]),
                ),
                config,
            )
        )
    return values


def _object_places(
    connection: sqlite3.Connection,
    config: Mapping[str, Any],
    runtime_area_observations: Sequence[Mapping[str, Any]] = (),
) -> list[dict[str, Any]]:
    version = str(config["placement_rule_version"])
    area_fallback = float(
        config.get("metadata_rules", {}).get("runtime_area_fallback_m", 500.0)
    )
    records: list[dict[str, Any]] = []
    rows = connection.execute(
        """SELECT * FROM features
           WHERE capture_enabled=1 AND calibrated=1 AND category NOT IN ('road','area')"""
    )
    for row in rows:
        anchor = _row_vec(row)
        forward = Vec3(
            float(row["forward_x"]), float(row["forward_y"]), float(row["forward_z"])
        ).normalized(horizontal=True)
        metadata = json.loads(row["metadata_json"])
        axis_name = metadata.get("orientation", {}).get("forward_axis", "+y")
        local_axis = {
            "+x": Vec3(1, 0, 0),
            "-x": Vec3(-1, 0, 0),
            "+y": Vec3(0, 1, 0),
            "-y": Vec3(0, -1, 0),
        }.get(str(axis_name).lower(), Vec3(0, 1, 0))
        bounds = _feature_bounds(row)
        extent = bounds.half_extent_along(local_axis) if bounds else None
        extent_source = "oriented_instance_bounds"
        if extent is None:
            extent = float(metadata.get("front_extent_m", 0.0))
            extent_source = "reviewed_rule_fallback"
        clearance = float(metadata.get("clearance_m", 0.0))
        requested = anchor + forward * (extent + clearance)
        location_id = stable_id("place", row["feature_id"], "outward", version)
        resolved, provenance = _metadata_for_point(
            connection,
            requested,
            location_id,
            area_fallback,
            runtime_area_observations,
        )
        missing = [field for field in REQUIRED_NAME_FIELDS if not resolved.get(field)]
        provenance.update(
            {
                "anchor": f"feature:{row['feature_id']}",
                "pose": f"placement_rule:{version}",
                "front_extent": extent_source,
                "ground_z": "serialized anchor height; CET resolves ground surface at runtime",
            }
        )
        records.append(
            _place_record(
                location_id=location_id,
                anchor_feature_id=row["feature_id"],
                category=row["category"],
                direction="outward",
                requested=requested,
                forward=forward,
                resource_path=row["resource_path"],
                source_sector=row["source_sector"],
                road_id=None,
                extraction_version=row["extraction_rule_version"],
                placement_version=version,
                metadata=resolved,
                provenance=provenance,
                review_status="needs_metadata" if missing else "resolved",
            )
        )
    return records


def _deduplicate_candidate_coordinates(
    records: Iterable[Mapping[str, Any]],
    minimum_separation_by_category: Mapping[str, float],
) -> tuple[list[Mapping[str, Any]], int]:
    """Greedily retain deterministic 3D candidates at the configured spacing."""
    retained: list[Mapping[str, Any]] = []
    grids: dict[
        str, dict[tuple[int, int, int], list[Mapping[str, Any]]]
    ] = defaultdict(lambda: defaultdict(list))
    removed = 0
    for record in sorted(records, key=lambda value: str(value["location_id"])):
        category = str(record["category"])
        separation = float(minimum_separation_by_category.get(category, 0.0))
        if separation <= 0.0:
            retained.append(record)
            continue
        x = float(record["requested_x"])
        y = float(record["requested_y"])
        z = float(record["requested_z"])
        cell = (
            math.floor(x / separation),
            math.floor(y / separation),
            math.floor(z / separation),
        )
        nearby: list[Mapping[str, Any]] = []
        grid = grids[category]
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    nearby.extend(
                        grid.get((cell[0] + dx, cell[1] + dy, cell[2] + dz), ())
                    )
        if any(
            (x - float(other["requested_x"])) ** 2
            + (y - float(other["requested_y"])) ** 2
            + (z - float(other["requested_z"])) ** 2
            < separation**2
            for other in nearby
        ):
            removed += 1
            continue
        retained.append(record)
        grid[cell].append(record)
    return retained, removed


def _deduplicate_sparse_road_places(
    roads: Iterable[Mapping[str, Any]],
    objects: Iterable[Mapping[str, Any]],
    rules: Mapping[str, Any],
) -> tuple[list[Mapping[str, Any]], int]:
    proximity = float(rules.get("object_proximity_m", 0.0))
    separation = float(rules.get("minimum_separation_m", 0.0))
    road_values = list(roads)
    if proximity <= 0.0 or separation <= 0.0:
        return road_values, 0

    object_grid: dict[tuple[int, int], list[tuple[float, float]]] = defaultdict(list)
    for candidate in objects:
        x = float(candidate["requested_x"])
        y = float(candidate["requested_y"])
        cell = (math.floor(x / proximity), math.floor(y / proximity))
        object_grid[cell].append((x, y))

    def near_object(x: float, y: float) -> bool:
        cell = (math.floor(x / proximity), math.floor(y / proximity))
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if any(
                    (x - other_x) ** 2 + (y - other_y) ** 2 <= proximity**2
                    for other_x, other_y in object_grid.get(
                        (cell[0] + dx, cell[1] + dy), ()
                    )
                ):
                    return True
        return False

    point_groups: dict[tuple[float, float, float], list[Mapping[str, Any]]] = (
        defaultdict(list)
    )
    for road in road_values:
        key = (
            round(float(road["requested_x"]), 6),
            round(float(road["requested_y"]), 6),
            round(float(road["requested_z"]), 6),
        )
        point_groups[key].append(road)

    sparse_grid: dict[
        tuple[int, int, int], list[tuple[float, float, float]]
    ] = defaultdict(list)
    retained: list[Mapping[str, Any]] = []
    removed = 0
    for key, views in sorted(
        point_groups.items(),
        key=lambda item: min(str(view["location_id"]) for view in item[1]),
    ):
        x, y, z = key
        keep = near_object(x, y)
        cell = (
            math.floor(x / separation),
            math.floor(y / separation),
            math.floor(z / separation),
        )
        if not keep:
            nearby: list[tuple[float, float, float]] = []
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for dz in (-1, 0, 1):
                        nearby.extend(
                            sparse_grid.get(
                                (cell[0] + dx, cell[1] + dy, cell[2] + dz), ()
                            )
                        )
            keep = not any(
                (x - other_x) ** 2 + (y - other_y) ** 2 + (z - other_z) ** 2
                < separation**2
                for other_x, other_y, other_z in nearby
            )
            if keep:
                sparse_grid[cell].append((x, y, z))
        if keep:
            retained.extend(sorted(views, key=lambda view: str(view["location_id"])))
        else:
            removed += len(views)
    return retained, removed


def _deduplicate_physical_locations(
    records: Iterable[Mapping[str, Any]],
    minimum_separation_m: float,
    category_priority: Sequence[str] = (),
) -> tuple[list[Mapping[str, Any]], int]:
    """Space physical coordinates globally while retaining views of one winner.

    Exact-coordinate records are treated as alternative anchors for one physical
    location. The highest-priority in-scope anchor wins; multiple directions for
    that same anchor (notably paired road views) remain attached to the retained
    location.
    """
    values = list(records)
    separation = float(minimum_separation_m)
    if separation <= 0.0:
        return values, 0

    priority = {category: index for index, category in enumerate(category_priority)}
    fallback_priority = len(priority)

    def record_priority(record: Mapping[str, Any]) -> tuple[int, int, str, str]:
        category = str(record["category"])
        return (
            0 if record.get("scope_status") == "in_scope" else 1,
            priority.get(category, fallback_priority),
            category,
            str(record["location_id"]),
        )

    def anchor_identity(record: Mapping[str, Any]) -> tuple[str, str]:
        if record.get("anchor_feature_id"):
            return ("feature", str(record["anchor_feature_id"]))
        if record.get("road_id"):
            return ("road", str(record["road_id"]))
        return ("place", str(record["location_id"]))

    coordinate_groups: dict[
        tuple[float, float, float], list[Mapping[str, Any]]
    ] = defaultdict(list)
    for record in values:
        coordinate_groups[
            (
                round(float(record["requested_x"]), 6),
                round(float(record["requested_y"]), 6),
                round(float(record["requested_z"]), 6),
            )
        ].append(record)

    candidates: list[
        tuple[
            tuple[int, int, str, str],
            tuple[float, float, float],
            list[Mapping[str, Any]],
        ]
    ] = []
    removed = 0
    for coordinate, group in coordinate_groups.items():
        winner = min(group, key=record_priority)
        winner_anchor = anchor_identity(winner)
        views = [
            record
            for record in group
            if record["category"] == winner["category"]
            and anchor_identity(record) == winner_anchor
            and record.get("scope_status") == winner.get("scope_status")
        ]
        removed += len(group) - len(views)
        candidates.append((record_priority(winner), coordinate, views))

    grid: dict[
        tuple[int, int, int], list[tuple[float, float, float]]
    ] = defaultdict(list)
    retained: list[Mapping[str, Any]] = []
    for _, coordinate, views in sorted(candidates, key=lambda value: value[0]):
        x, y, z = coordinate
        cell = (
            math.floor(x / separation),
            math.floor(y / separation),
            math.floor(z / separation),
        )
        nearby: list[tuple[float, float, float]] = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    nearby.extend(
                        grid.get((cell[0] + dx, cell[1] + dy, cell[2] + dz), ())
                    )
        if any(
            (x - other_x) ** 2 + (y - other_y) ** 2 + (z - other_z) ** 2
            < separation**2
            for other_x, other_y, other_z in nearby
        ):
            removed += len(views)
            continue
        grid[cell].append(coordinate)
        retained.extend(sorted(views, key=lambda record: str(record["location_id"])))
    retained.sort(key=lambda record: str(record["location_id"]))
    return retained, removed


def _road_sample_distances(length: float, rules: Mapping[str, Any]) -> list[float]:
    short = float(rules.get("short_road_threshold_m", 100.0))
    if length < short:
        return [length * 0.5]
    inset = float(rules.get("endpoint_inset_m", 50.0))
    interval = float(rules.get("interval_m", 100.0))
    values: list[float] = []
    distance = min(inset, length * 0.5)
    while distance <= length - inset + 1e-6:
        values.append(distance)
        distance += interval
    return values or [length * 0.5]


def sample_road_points(
    points: list[Vec3], rules: Mapping[str, Any]
) -> list[tuple[float, Vec3, Vec3]]:
    length = polyline_length(points)
    minimum_arc = float(rules.get("minimum_arc_separation_m", 100.0))
    minimum_straight = float(rules.get("minimum_straight_separation_m", 100.0))
    selected: list[tuple[float, Vec3, Vec3]] = []
    for distance in _road_sample_distances(length, rules):
        point, tangent = interpolate_polyline(points, distance)
        if selected:
            previous_distance = selected[-1][0]
            if distance - previous_distance < minimum_arc - 1e-6:
                continue
            # A looping centerline can bring a later sample back beside any
            # earlier sample, not only its immediate predecessor.  Enforce the
            # straight-line constraint across the whole road branch.
            if any(
                point.distance_2d(previous_point) < minimum_straight - 1e-6
                for _, previous_point, _ in selected
            ):
                continue
        selected.append((distance, point, tangent))
    return selected


def _road_places(
    connection: sqlite3.Connection,
    config: Mapping[str, Any],
    runtime_area_observations: Sequence[Mapping[str, Any]] = (),
) -> list[dict[str, Any]]:
    version = str(config["placement_rule_version"])
    extraction_version = str(config["extraction_rule_version"])
    rules = config.get("road_rules", {})
    area_fallback = float(
        config.get("metadata_rules", {}).get("runtime_area_fallback_m", 500.0)
    )
    records: list[dict[str, Any]] = []
    for road in connection.execute("SELECT * FROM roads ORDER BY road_id"):
        points = [
            Vec3(float(value["x"]), float(value["y"]), float(value["z"]))
            for value in json.loads(road["points_json"])
        ]
        for sample_index, (arc_distance, point, tangent) in enumerate(
            sample_road_points(points, rules)
        ):
            for direction, forward in (("along", tangent), ("against", tangent * -1.0)):
                location_id = stable_id(
                    "place",
                    road["road_id"],
                    round(arc_distance, 6),
                    direction,
                    [round(point.x, 6), round(point.y, 6), round(point.z, 6)],
                    version,
                )
                resolved, provenance = _metadata_for_point(
                    connection,
                    point,
                    location_id,
                    area_fallback,
                    runtime_area_observations,
                )
                if road["name"] and not resolved.get("nearest_street_name"):
                    resolved["nearest_street_name"] = road["name"]
                    provenance["nearest_street_name"] = "spatial:sampled_road"
                missing = [
                    field for field in REQUIRED_NAME_FIELDS if not resolved.get(field)
                ]
                provenance.update(
                    {
                        "road_geometry": f"road:{road['road_id']}",
                        "arc_distance_m": arc_distance,
                        "sample_index": sample_index,
                        "ground_z": "proxy-center height; CET resolves road surface at runtime",
                    }
                )
                records.append(
                    _place_record(
                        location_id=location_id,
                        anchor_feature_id=None,
                        category="road",
                        direction=direction,
                        requested=point,
                        forward=forward,
                        resource_path=None,
                        source_sector=None,
                        road_id=road["road_id"],
                        extraction_version=extraction_version,
                        placement_version=version,
                        metadata=resolved,
                        provenance=provenance,
                        review_status="needs_metadata" if missing else "resolved",
                    )
                )
    return records


def _place_record(
    *,
    location_id: str,
    anchor_feature_id: str | None,
    category: str,
    direction: str,
    requested: Vec3,
    forward: Vec3,
    resource_path: str | None,
    source_sector: str | None,
    road_id: str | None,
    extraction_version: str,
    placement_version: str,
    metadata: Mapping[str, Any],
    provenance: Mapping[str, Any],
    review_status: str,
) -> dict[str, Any]:
    return {
        "location_id": location_id,
        "anchor_feature_id": anchor_feature_id,
        "category": category,
        "direction": direction,
        "requested_x": requested.x,
        "requested_y": requested.y,
        "requested_z": requested.z,
        "requested_yaw": game_yaw_degrees(forward),
        "requested_pitch": 0.0,
        "requested_roll": 0.0,
        "forward_x": forward.x,
        "forward_y": forward.y,
        "forward_z": forward.z,
        "resource_path": resource_path,
        "source_sector": source_sector,
        "road_id": road_id,
        "nearest_fast_travel_id": metadata.get("nearest_fast_travel_id"),
        "nearest_fast_travel_name": metadata.get("nearest_fast_travel_name"),
        "nearest_fast_travel_x": metadata.get("nearest_fast_travel_x"),
        "nearest_fast_travel_y": metadata.get("nearest_fast_travel_y"),
        "nearest_fast_travel_z": metadata.get("nearest_fast_travel_z"),
        "nearest_fast_travel_distance_m": metadata.get(
            "nearest_fast_travel_distance_m"
        ),
        "nearest_street_road_id": metadata.get("nearest_street_road_id"),
        "nearest_street_name": metadata.get("nearest_street_name"),
        "nearest_street_x": metadata.get("nearest_street_x"),
        "nearest_street_y": metadata.get("nearest_street_y"),
        "nearest_street_z": metadata.get("nearest_street_z"),
        "nearest_street_distance_m": metadata.get("nearest_street_distance_m"),
        "district": metadata.get("district"),
        "subdistrict": metadata.get("subdistrict"),
        "named_area": metadata.get("named_area"),
        "interior_state": metadata.get("interior_state"),
        "extraction_rule_version": extraction_version,
        "placement_rule_version": placement_version,
        "provenance_json": json_text(provenance),
        "queue_order": morton_key_2d(requested.x, requested.y),
        "review_status": review_status,
    }


_PLACE_COLUMNS = (
    "location_id",
    "anchor_feature_id",
    "category",
    "direction",
    "requested_x",
    "requested_y",
    "requested_z",
    "requested_yaw",
    "requested_pitch",
    "requested_roll",
    "forward_x",
    "forward_y",
    "forward_z",
    "resource_path",
    "source_sector",
    "road_id",
    "nearest_fast_travel_id",
    "nearest_fast_travel_name",
    "nearest_fast_travel_x",
    "nearest_fast_travel_y",
    "nearest_fast_travel_z",
    "nearest_fast_travel_distance_m",
    "nearest_street_road_id",
    "nearest_street_name",
    "nearest_street_x",
    "nearest_street_y",
    "nearest_street_z",
    "nearest_street_distance_m",
    "district",
    "subdistrict",
    "named_area",
    "interior_state",
    "extraction_rule_version",
    "placement_rule_version",
    "provenance_json",
    "queue_order",
    "review_status",
    "scope_status",
    "scope_rule_id",
    "scope_rule_version",
    "scope_detail_json",
)


def _upsert_places(
    connection: sqlite3.Connection, records: Iterable[Mapping[str, Any]]
) -> int:
    values = list(records)
    now = utc_now()
    placeholders = ",".join(f":{column}" for column in _PLACE_COLUMNS)
    updates = ",".join(
        f"{column}=excluded.{column}"
        for column in _PLACE_COLUMNS
        if column != "location_id"
    )
    statement = f"""INSERT INTO places({",".join(_PLACE_COLUMNS)},created_at,updated_at)
        VALUES({placeholders},:created_at,:updated_at)
        ON CONFLICT(location_id) DO UPDATE SET {updates}, updated_at=excluded.updated_at,
          failure_code=NULL, failure_detail=NULL,
          queue_status=CASE WHEN places.queue_status='captured' THEN 'captured' ELSE 'pending' END"""
    active_ids = {record["location_id"] for record in values}
    with transaction(connection):
        connection.execute(
            "UPDATE places SET queue_status='disabled',updated_at=? WHERE queue_status!='captured'",
            (now,),
        )
        for record in values:
            row = dict(record)
            row["created_at"] = now
            row["updated_at"] = now
            connection.execute(statement, row)
        connection.execute(
            """UPDATE places SET queue_status='disabled',publishable=0,updated_at=?
               WHERE scope_status='out_of_scope' AND queue_status!='captured'""",
            (now,),
        )
        connection.execute(
            "UPDATE places SET publishable=0 WHERE scope_status='out_of_scope'"
        )
        # Captured historical places are deliberately retained for provenance.
        if active_ids:
            connection.execute(
                "UPDATE places SET publishable=0 WHERE review_status!='resolved'"
            )
    return len(values)


def plan_locations(
    connection: sqlite3.Connection, config: Mapping[str, Any]
) -> dict[str, int]:
    fast_travel_count = rebuild_fast_travel(connection)
    road_count = rebuild_roads(connection, str(config["placement_rule_version"]))
    area_count = rebuild_areas(connection)
    runtime_areas = _runtime_area_observations(connection)
    object_candidates = _object_places(connection, config, runtime_areas)
    minimum_separation = {
        str(rule["category"]): float(rule.get("minimum_candidate_separation_m", 0.0))
        for rule in config.get("classification_rules", ())
        if rule.get("category")
    }
    objects, deduplicated_objects = _deduplicate_candidate_coordinates(
        object_candidates, minimum_separation
    )
    road_candidates = _road_places(connection, config, runtime_areas)
    roads, deduplicated_roads = _deduplicate_sparse_road_places(
        road_candidates, objects, config.get("sparse_road_rules", {})
    )
    scoped_candidates = _apply_scope([*objects, *roads], config)
    spacing_rules = config.get("location_spacing_rules", {})
    places, deduplicated_physical_places = _deduplicate_physical_locations(
        scoped_candidates,
        float(spacing_rules.get("minimum_separation_m", 0.0)),
        [str(category) for category in spacing_rules.get("category_priority", ())],
    )
    place_count = _upsert_places(connection, places)
    in_scope = sum(record["scope_status"] == "in_scope" for record in places)
    out_of_scope = sum(record["scope_status"] == "out_of_scope" for record in places)
    object_places = sum(record["category"] != "road" for record in places)
    road_places = sum(record["category"] == "road" for record in places)
    return {
        "fast_travel_points": fast_travel_count,
        "roads": road_count,
        "areas": area_count,
        "object_places": object_places,
        "object_candidates": len(object_candidates),
        "deduplicated_object_places": deduplicated_objects,
        "road_places": road_places,
        "road_candidates": len(road_candidates),
        "deduplicated_road_places": deduplicated_roads,
        "physical_place_candidates": len(scoped_candidates),
        "deduplicated_physical_places": deduplicated_physical_places,
        "places": place_count,
        "in_scope": in_scope,
        "out_of_scope": out_of_scope,
    }
