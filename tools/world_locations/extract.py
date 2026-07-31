"""Incremental, per-sector extraction of capture-relevant world features."""

from __future__ import annotations

from collections.abc import Iterator, Mapping
import base64
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import struct
from typing import Any, Callable

from .database import (
    record_sector_error,
    replace_sector,
    sector_is_current,
    transaction,
)
from .model import (
    Bounds,
    Quaternion,
    Vec3,
    canonical_json,
    outward_vector,
    stable_id,
    unwrap,
)


ROAD_RESOURCE = re.compile(
    r"(?:^|[\\/])road_meshes[\\/](?P<road>[^\\/]+)[\\/](?:prx)?(?P<order>\d+)\.mesh$",
    re.IGNORECASE,
)
MAX_FALLBACK_BYTES = 64 * 1024 * 1024


class StreamingParserRequired(RuntimeError):
    pass


def _ijson() -> Any | None:
    try:
        import ijson  # type: ignore[import-not-found]
    except ImportError:
        return None
    return ijson


def _items(path: Path, prefix: str) -> Iterator[Any]:
    parser = _ijson()
    if parser is not None:
        with path.open("rb") as stream:
            yield from parser.items(stream, prefix)
        return
    if path.stat().st_size > MAX_FALLBACK_BYTES:
        raise StreamingParserRequired(
            f"{path.name} is too large for the standard-library fallback; "
            "install tools/requirements-world-locations.txt"
        )
    document = json.loads(path.read_text(encoding="utf-8"))
    value: Any = document
    for component in prefix.split("."):
        if component == "item":
            if not isinstance(value, list):
                return
            yield from value
            return
        if not isinstance(value, Mapping):
            return
        value = value.get(component)


def _all_strings(value: Any, *, limit: int = 2048) -> Iterator[str]:
    remaining = [limit]

    def visit(current: Any, key: str = "") -> Iterator[str]:
        if remaining[0] <= 0 or key.lower() in {"bytes", "buffer", "cookeddata"}:
            return
        current = unwrap(current)
        if isinstance(current, str):
            remaining[0] -= 1
            yield current
        elif isinstance(current, Mapping):
            for child_key, child in current.items():
                yield from visit(child, str(child_key))
        elif isinstance(current, list):
            for child in current:
                yield from visit(child, key)

    yield from visit(value)


def _first_string_for_keys(value: Any, names: set[str]) -> str | None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key.lower() in names:
                scalar = unwrap(child)
                if isinstance(scalar, str) and scalar:
                    return scalar
            found = _first_string_for_keys(child, names)
            if found:
                return found
    elif isinstance(value, list):
        for child in value:
            found = _first_string_for_keys(child, names)
            if found:
                return found
    return None


def _resource_path(data: Mapping[str, Any]) -> str | None:
    preferred = (
        "entityTemplate",
        "mesh",
        "resource",
        "template",
        "appearanceResource",
    )
    for name in preferred:
        child = data.get(name)
        if child is not None:
            found = _first_string_for_keys(child, {"depotpath"})
            if found:
                return found.replace("/", "\\").lower()
    found = _first_string_for_keys(data, {"depotpath"})
    return found.replace("/", "\\").lower() if found else None


def _text(value: Any) -> str | None:
    scalar = unwrap(value)
    if isinstance(scalar, str):
        return scalar
    return None


def _matches_rule(rule: Mapping[str, Any], node_type: str, haystack: str) -> bool:
    node_types = {str(item).lower() for item in rule.get("node_types", [])}
    if node_types and node_type.lower() not in node_types:
        return False
    lowered = haystack.lower()
    patterns = [str(item).lower() for item in rule.get("patterns", [])]
    excluded = [str(item).lower() for item in rule.get("exclude_patterns", [])]
    return bool(patterns and any(item in lowered for item in patterns)) and not any(
        item in lowered for item in excluded
    )


def _find_fast_travel_data(value: Any) -> dict[str, Any] | None:
    if isinstance(value, Mapping):
        type_name = _text(value.get("$type"))
        if type_name == "gameFastTravelPointData":
            marker = _text(value.get("markerRef"))
            record = unwrap(value.get("pointRecord"))
            return {"marker_ref": marker, "point_record": record}
        for child in value.values():
            found = _find_fast_travel_data(child)
            if found:
                return found
    elif isinstance(value, list):
        for child in value:
            found = _find_fast_travel_data(child)
            if found:
                return found
    return None


def _area_outline(data: Mapping[str, Any]) -> list[dict[str, float]]:
    outline = data.get("outline")
    if not isinstance(outline, Mapping):
        return []
    outline_data = outline.get("Data")
    if not isinstance(outline_data, Mapping):
        return []
    encoded = unwrap(outline_data.get("buffer"))
    if not isinstance(encoded, str) or not encoded:
        return []
    try:
        buffer = base64.b64decode(encoded, validate=True)
    except ValueError:
        return []
    if len(buffer) < 4:
        return []
    count = struct.unpack_from("<I", buffer)[0]
    if count < 3 or len(buffer) < 4 + count * 16:
        return []
    return [
        {"x": float(x), "y": float(y), "z": float(z)}
        for x, y, z, _ in (
            struct.unpack_from("<ffff", buffer, 4 + index * 16)
            for index in range(count)
        )
    ]


def _location_district_id(data: Mapping[str, Any]) -> str | None:
    for notifier in data.get("notifiers", []):
        if not isinstance(notifier, Mapping):
            continue
        notifier_data = notifier.get("Data")
        if not isinstance(notifier_data, Mapping):
            continue
        district_id = unwrap(notifier_data.get("districtID"))
        if district_id not in (None, ""):
            return str(district_id)
    return None


def _descriptor(
    index: int, node: Mapping[str, Any], rules: list[Mapping[str, Any]]
) -> dict[str, Any] | None:
    data = node.get("Data", node)
    if not isinstance(data, Mapping):
        return None
    node_type = str(unwrap(data.get("$type")) or "")
    resource = _resource_path(data)
    debug_name = _text(data.get("debugName"))
    appearance = _text(data.get("appearanceName")) or _text(data.get("meshAppearance"))
    haystack = "\n".join(
        item
        for item in [node_type, resource, debug_name, appearance, *_all_strings(data)]
        if item
    )
    rule = next(
        (
            candidate
            for candidate in rules
            if _matches_rule(candidate, node_type, haystack)
        ),
        None,
    )
    if rule is None:
        return None
    metadata: dict[str, Any] = {
        "orientation": {
            "forward_axis": rule.get("forward_axis", "+y"),
            "yaw_correction_degrees": float(rule.get("yaw_correction_degrees", 0.0)),
        },
        "front_extent_m": float(rule.get("front_extent_m", 0.0)),
        "clearance_m": float(rule.get("clearance_m", 0.0)),
        "lateral_search_m": float(rule.get("lateral_search_m", 0.0)),
    }
    fast_travel = _find_fast_travel_data(data)
    if fast_travel:
        metadata["fast_travel"] = fast_travel
    area_outline = _area_outline(data)
    if area_outline:
        metadata["area_outline"] = area_outline
        metadata["district_id"] = _location_district_id(data)
    road_id: str | None = None
    road_order: int | None = None
    if resource:
        match = ROAD_RESOURCE.search(resource)
        if match:
            road_id = match.group("road").lower()
            road_order = int(match.group("order"))
    return {
        "node_index": index,
        "category": str(rule["category"]),
        "node_type": node_type,
        "resource_path": resource,
        "debug_name": debug_name,
        "appearance": appearance,
        "calibrated": bool(rule.get("calibrated", False)),
        "capture_enabled": bool(rule.get("capture_enabled", False)),
        "rule_id": str(rule["id"]),
        "tags": " ".join(str(tag) for tag in rule.get("tags", [])),
        "road_id": road_id,
        "road_order": road_order,
        "metadata": metadata,
    }


def _orientation_correction(
    descriptor: Mapping[str, Any], corrections: list[Mapping[str, Any]]
) -> tuple[str, float, str | None]:
    resource = str(descriptor.get("resource_path") or "").lower()
    for correction in corrections:
        pattern = str(correction.get("resource_pattern", "")).lower()
        if pattern and pattern in resource:
            return (
                str(correction.get("forward_axis", "+y")),
                float(correction.get("yaw_correction_degrees", 0.0)),
                str(correction.get("id", pattern)),
            )
    orientation = descriptor["metadata"]["orientation"]
    return (
        str(orientation.get("forward_axis", "+y")),
        float(orientation.get("yaw_correction_degrees", 0.0)),
        None,
    )


def extract_sector(
    path: Path, relative_path: str, config: Mapping[str, Any]
) -> list[dict[str, Any]]:
    rules = list(config.get("classification_rules", []))
    descriptors: dict[int, dict[str, Any]] = {}
    for index, node in enumerate(_items(path, "Data.RootChunk.nodes.item")):
        if isinstance(node, Mapping):
            descriptor = _descriptor(index, node, rules)
            if descriptor:
                descriptors[index] = descriptor
    if not descriptors:
        return []

    features: list[dict[str, Any]] = []
    instance_counters: dict[int, int] = {}
    corrections = list(config.get("orientation_corrections", []))
    version = str(config["extraction_rule_version"])
    for instance in _items(path, "Data.RootChunk.nodeData.Data.item"):
        if not isinstance(instance, Mapping):
            continue
        try:
            node_index = int(unwrap(instance.get("NodeIndex")))
        except (TypeError, ValueError):
            continue
        descriptor = descriptors.get(node_index)
        if descriptor is None:
            continue
        instance_index = instance_counters.get(node_index, 0)
        instance_counters[node_index] = instance_index + 1
        position_value = instance.get("Position")
        if not isinstance(position_value, Mapping):
            continue
        position = Vec3.from_mapping(position_value)
        rotation_value = instance.get("Orientation")
        rotation = Quaternion.from_mapping(
            rotation_value if isinstance(rotation_value, Mapping) else None
        )
        bounds_value = instance.get("Bounds")
        bounds = Bounds.from_mapping(
            bounds_value if isinstance(bounds_value, Mapping) else None
        )
        axis, yaw_correction, correction_id = _orientation_correction(
            descriptor, corrections
        )
        forward = outward_vector(rotation, axis, yaw_correction)
        instance_id = unwrap(instance.get("Id"))
        identity_transform = {
            "position": [position.x, position.y, position.z],
            "rotation": [rotation.i, rotation.j, rotation.k, rotation.r],
        }
        feature_id = stable_id(
            "feature",
            relative_path.lower(),
            node_index,
            instance_index,
            str(instance_id) if instance_id is not None else None,
            identity_transform,
            descriptor["rule_id"],
            version,
        )
        metadata = dict(descriptor["metadata"])
        area_outline = metadata.get("area_outline", [])
        if area_outline:
            scale_value = instance.get("Scale")
            scale = scale_value if isinstance(scale_value, Mapping) else {}
            scale_x = float(unwrap(scale.get("X", scale.get("x", 1.0))) or 1.0)
            scale_y = float(unwrap(scale.get("Y", scale.get("y", 1.0))) or 1.0)
            scale_z = float(unwrap(scale.get("Z", scale.get("z", 1.0))) or 1.0)
            metadata["area_outline"] = [
                {
                    "x": float(point["x"]) * scale_x,
                    "y": float(point["y"]) * scale_y,
                    "z": float(point["z"]) * scale_z,
                }
                for point in area_outline
            ]
            metadata["area_scale"] = {
                "x": scale_x,
                "y": scale_y,
                "z": scale_z,
            }
        if correction_id:
            metadata["orientation_correction_id"] = correction_id
        metadata["identity_transform"] = identity_transform
        minimum, maximum = (bounds.minimum, bounds.maximum) if bounds else (None, None)
        area_outline = metadata.get("area_outline", [])
        if area_outline:
            min_x = min(float(point["x"]) for point in area_outline)
            min_y = min(float(point["y"]) for point in area_outline)
            max_x = max(float(point["x"]) for point in area_outline)
            max_y = max(float(point["y"]) for point in area_outline)
            min_z = max_z = None
        else:
            min_x = minimum.x if minimum else None
            min_y = minimum.y if minimum else None
            min_z = minimum.z if minimum else None
            max_x = maximum.x if maximum else None
            max_y = maximum.y if maximum else None
            max_z = maximum.z if maximum else None
        features.append(
            {
                "feature_id": feature_id,
                "source_sector": relative_path,
                "node_index": node_index,
                "instance_index": instance_index,
                "instance_id": str(instance_id) if instance_id is not None else None,
                "category": descriptor["category"],
                "node_type": descriptor["node_type"],
                "resource_path": descriptor["resource_path"],
                "debug_name": descriptor["debug_name"],
                "appearance": descriptor["appearance"],
                "x": position.x,
                "y": position.y,
                "z": position.z,
                "q_i": rotation.i,
                "q_j": rotation.j,
                "q_k": rotation.k,
                "q_r": rotation.r,
                "min_x": min_x,
                "min_y": min_y,
                "min_z": min_z,
                "max_x": max_x,
                "max_y": max_y,
                "max_z": max_z,
                "forward_x": forward.x,
                "forward_y": forward.y,
                "forward_z": forward.z,
                "calibrated": int(descriptor["calibrated"]),
                "capture_enabled": int(descriptor["capture_enabled"]),
                "rule_id": descriptor["rule_id"],
                "extraction_rule_version": version,
                "road_id": descriptor["road_id"],
                "road_order": descriptor["road_order"],
                "tags": descriptor["tags"],
                "metadata_json": canonical_json(metadata),
            }
        )
    return features


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def index_sectors(
    connection: sqlite3.Connection,
    source_root: Path,
    config: Mapping[str, Any],
    *,
    content_hash: bool = False,
    continue_on_error: bool = True,
    limit: int | None = None,
    progress: Callable[[int, int, str, str], None] | None = None,
) -> dict[str, int]:
    if not source_root.is_dir():
        raise FileNotFoundError(f"serialized sector root does not exist: {source_root}")
    rule_version = str(config["extraction_rule_version"])
    paths = sorted(source_root.rglob("*.streamingsector.json"))
    if limit is not None:
        paths = paths[:limit]
    counts = {
        "discovered": len(paths),
        "indexed": 0,
        "unchanged": 0,
        "errors": 0,
        "features": 0,
    }
    seen: set[str] = set()
    for ordinal, path in enumerate(paths, 1):
        relative = path.relative_to(source_root).as_posix()
        seen.add(relative)
        stat = path.stat()
        if sector_is_current(
            connection, relative, stat.st_size, stat.st_mtime_ns, rule_version
        ):
            counts["unchanged"] += 1
            if progress:
                progress(ordinal, len(paths), relative, "unchanged")
            continue
        try:
            features = extract_sector(path, relative, config)
            digest = sha256_file(path) if content_hash else None
            replace_sector(
                connection,
                relative_path=relative,
                size_bytes=stat.st_size,
                mtime_ns=stat.st_mtime_ns,
                content_sha256=digest,
                rule_version=rule_version,
                features=features,
            )
        except Exception as error:
            record_sector_error(
                connection,
                relative_path=relative,
                size_bytes=stat.st_size,
                mtime_ns=stat.st_mtime_ns,
                rule_version=rule_version,
                error=f"{type(error).__name__}: {error}",
            )
            counts["errors"] += 1
            if progress:
                progress(ordinal, len(paths), relative, "error")
            if not continue_on_error:
                raise
            continue
        counts["indexed"] += 1
        counts["features"] += len(features)
        if progress:
            progress(ordinal, len(paths), relative, f"indexed:{len(features)}")

    if limit is None:
        with transaction(connection):
            rows = connection.execute(
                "SELECT sector_id,relative_path FROM source_sectors"
            ).fetchall()
            stale = [
                row["sector_id"] for row in rows if row["relative_path"] not in seen
            ]
            connection.executemany(
                "DELETE FROM source_sectors WHERE sector_id=?",
                ((value,) for value in stale),
            )
        counts["pruned"] = len(stale)
    return counts
