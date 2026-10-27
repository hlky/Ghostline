"""Road centerlines from native deformation frames, without proxy interpolation.

Each Matrix.W is a centerline station in node-local space; Matrix.Y is its
longitudinal direction. Apply instance scale, rotation, then translation.
deformedBox is a local envelope used for validation, never a curve substitute.
Segments stay separate: shared template meshes do not imply connected roads.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Callable, Mapping

from .database import json_text, transaction
from .extract import _resource_path
from .model import Quaternion, Vec3, interpolate_polyline, polyline_length, stable_id, unwrap


GEOMETRY_METHOD = "bended_deformation_frames_v1"
EXCLUDED_ROAD_RESOURCES = ("metro", "rail", "tram", "monorail")


def _vector(value: Mapping[str, Any]) -> Vec3:
    components = [float(unwrap(value[axis])) for axis in ("X", "Y", "Z")]
    if not all(math.isfinite(component) for component in components):
        raise ValueError("nonfinite road deformation vector")
    return Vec3(*components)


def deformation_centerline(
    node: Mapping[str, Any], instance: Mapping[str, Any],
) -> tuple[list[Vec3], list[Vec3]]:
    """Decode a single road instance; malformed data must never become (0,0,0)."""
    frames = node.get("deformationData", [])
    if len(frames) < 2:
        raise ValueError("road needs at least two deformation frames")
    position = _vector(instance["Position"])
    scale = _vector(instance.get("Scale", {"X": 1, "Y": 1, "Z": 1}))
    if min(abs(scale.x), abs(scale.y), abs(scale.z)) < 1e-9:
        raise ValueError("singular road instance scale")
    orientation = instance["Orientation"]
    q_values = [float(unwrap(orientation[axis])) for axis in ("i", "j", "k", "r")]
    if not all(math.isfinite(v) for v in q_values) or sum(v*v for v in q_values) < 1e-12:
        raise ValueError("invalid road instance rotation")
    rotation = Quaternion(*q_values).normalized()
    box = node["deformedBox"]
    low, high = _vector(box["Min"]), _vector(box["Max"])

    def transform(vector: Vec3) -> Vec3:
        return rotation.rotate(Vec3(vector.x * scale.x, vector.y * scale.y, vector.z * scale.z))

    points, tangents = [], []
    for frame in frames:
        point, tangent = _vector(frame["W"]), _vector(frame["Y"])
        if abs(float(unwrap(frame["W"]["W"])) - 1) > 1e-4:
            raise ValueError("invalid deformation station homogeneous coordinate")
        if not all(a - 0.25 <= v <= b + 0.25 for a, v, b in zip(
            (low.x, low.y, low.z), (point.x, point.y, point.z), (high.x, high.y, high.z),
        )):
            raise ValueError("deformation station outside local deformedBox")
        world_tangent = transform(tangent)
        if world_tangent.horizontal_length() < 1e-6:
            raise ValueError("road has no horizontal tangent")
        world_point = position + transform(point)
        if points and (world_point - points[-1]).length() < 1e-5:
            raise ValueError("duplicate road deformation stations")
        points.append(world_point)
        tangents.append(world_tangent.normalized())
    # This also detects transposing the frames or decoding an unrelated matrix.
    for index, (left, right) in enumerate(zip(points, points[1:])):
        chord = (right - left).normalized()
        if min(chord.dot(tangents[index]), chord.dot(tangents[index + 1])) < 0.2:
            raise ValueError("deformation tangent disagrees with station order")
    return points, tangents


def deformation_tangent(points: list[Vec3], tangents: list[Vec3], distance: float) -> Vec3:
    """Interpolate native longitudinal directions at the sampled arc distance."""
    remaining = max(0.0, distance)
    for index, (left, right) in enumerate(zip(points, points[1:])):
        length = (right - left).length()
        if remaining <= length:
            blend = remaining / length
            return (tangents[index] * (1 - blend) + tangents[index + 1] * blend).normalized(horizontal=True)
        remaining -= length
    return tangents[-1].normalized(horizontal=True)


def rebuild_deformed_roads(
    connection, source_root: Path, placement_version: str,
    *, progress: Callable[[int, int], None] | None = None,
) -> dict[str, Any]:
    """Replace derived roads only; leave indexed features and capture history intact."""
    if not source_root.is_dir():
        raise FileNotFoundError(source_root)
    records, rejected = [], []
    files = sorted(source_root.rglob("*.streamingsector.json"))
    for ordinal, path in enumerate(files, 1):
        # Cheap prefilter; stream large JSON files only when this node exists.
        raw = path.read_bytes()
        if b'"worldBendedMeshNode"' not in raw:
            continue
        # A single C-decoder pass is much faster than two streaming passes over
        # millions of numeric matrix fields. Only matching sectors are decoded.
        document = json.loads(raw)["Data"]["RootChunk"]
        del raw
        relative = path.relative_to(source_root).as_posix()
        nodes = {}
        for index, handle in enumerate(document["nodes"]):
            node = handle.get("Data", handle)
            resource = _resource_path(node) or ""
            if (node.get("$type") == "worldBendedMeshNode"
                    and unwrap(node.get("isBendedRoad")) in (True, 1)
                    and "road_meshes\\bended\\" in resource.lower()
                    and not any(word in resource.lower() for word in EXCLUDED_ROAD_RESOURCES)):
                nodes[index] = (node, resource)
        counters = {}
        if nodes:
            for instance in document["nodeData"]["Data"]:
                index = int(unwrap(instance["NodeIndex"]))
                if index not in nodes:
                    continue
                instance_index = counters.get(index, 0)
                counters[index] = instance_index + 1
                node, resource = nodes[index]
                source = {"sector": relative, "node_index": index, "instance_index": instance_index, "mesh": resource}
                try:
                    points, tangents = deformation_centerline(node, instance)
                except (KeyError, TypeError, ValueError) as error:
                    rejected.append({**source, "reason": str(error)})
                    continue
                road_id = stable_id("road", relative, index, instance_index, GEOMETRY_METHOD)
                maximum_bend = max(math.degrees(math.acos(max(-1, min(1, tangents[0].dot(b))))) for b in tangents)
                records.append({
                    "road_id": road_id, "name": None,
                    "points_json": json_text([p.as_dict() for p in points]),
                    "length_m": polyline_length(points),
                    "min_x": min(p.x for p in points), "max_x": max(p.x for p in points),
                    "min_y": min(p.y for p in points), "max_y": max(p.y for p in points),
                    "source_json": json_text(source),
                    "provenance_json": json_text({
                        "geometry": GEOMETRY_METHOD,
                        "native_tangents": [p.as_dict() for p in tangents],
                        "maximum_bend_degrees": maximum_bend,
                        "transform": "instance_position + instance_rotation(instance_scale * Matrix.W.xyz)",
                        "envelope_validation": "node-local deformedBox, 0.25m tolerance",
                        "source": source,
                    }),
                    "planning_rule_version": placement_version,
                })
        if progress and ordinal % 100 == 0:
            progress(ordinal, len(files))
    if not records:
        raise ValueError("No valid deformed road centerlines; existing roads retained")
    with transaction(connection):
        connection.execute("DELETE FROM roads")
        connection.executemany(
            """INSERT INTO roads(road_id,name,points_json,length_m,min_x,max_x,min_y,max_y,
               source_json,provenance_json,planning_rule_version) VALUES(:road_id,:name,:points_json,
               :length_m,:min_x,:max_x,:min_y,:max_y,:source_json,:provenance_json,:planning_rule_version)""",
            records,
        )
    return {"roads": len(records), "rejected": rejected, "geometry": GEOMETRY_METHOD}


def select_calibration_roads(connection, config: Mapping[str, Any] | None = None) -> list[str]:
    """Choose separated, visibly curved street segments in the main city."""
    candidates = []
    for row in connection.execute("SELECT * FROM roads ORDER BY road_id"):
        provenance = json.loads(row["provenance_json"])
        if provenance.get("geometry") != GEOMETRY_METHOD:
            continue
        if any(word in provenance["source"]["mesh"].lower() for word in ("destroyed", "heavy_damage", "broken")):
            continue
        points = [Vec3(**value) for value in json.loads(row["points_json"])]
        midpoint, _ = interpolate_polyline(points, row["length_m"] / 2)
        bend = provenance["maximum_bend_degrees"]
        # Avoid tiny pieces, railways, outlying highways and extreme elevations.
        if (12 <= row["length_m"] <= 90 and 12 <= bend <= 100
                and -2400 <= midpoint.x <= 1600 and -2200 <= midpoint.y <= 2200
                and 0 <= midpoint.z <= 110):
            rise = max(p.z for p in points) - min(p.z for p in points)
            candidates.append((dict(row), midpoint, bend, rise))
    selected = []
    # Mix a gentle bend, a sharper turn and a rising bend, then another curve.
    for target_bend, prefer_rise in ((20, False), (65, False), (30, True), (40, False)):
        available = [c for c in candidates if all(c[1].distance_2d(previous[1]) >= 150 for previous in selected)]
        available.sort(key=lambda c: (-min(c[3], 8) if prefer_rise else abs(c[2] - target_bend), c[0]["road_id"]))
        if config is not None:
            from .planning import evaluate_scope

            available = (candidate for candidate in available if evaluate_scope(candidate[1], config)["scope_status"] == "in_scope")
        chosen = next(iter(available), None)
        if chosen is None:
            raise ValueError("Not enough separated curved roads for the calibration sample")
        selected.append(chosen)
    return [item[0]["road_id"] for item in selected]
