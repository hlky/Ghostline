"""Survey vanilla shell pieces and validate precise ArchiveXL entrance patches.

The source sector remains immutable. Selections pin its SHA-256, node count,
types and collision actor counts before emitting a streaming.sectors patch.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]


def collision_actor_scale(node, raw, actor):
    """Read the actor's indexed world-axis scale (WolvenKit CollisionReader)."""
    index = struct.unpack_from('<h', raw, actor * 48 + 36)[0]
    if index == -1 or not node.get('numScales', 0):
        return [1, 1, 1]
    if not 0 <= index < node['numScales']:
        raise ValueError('Collision actor has an invalid scale index')
    offset = (node['numActors'] * 48 + node['numShapeInfos'] * 32
              + node.get('numShapePositions', 0) * 12 + node.get('numShapeRotations', 0) * 16)
    return list(struct.unpack_from('<3f', raw, offset + index * 12))


def _integer(value, name, low, high):
    if isinstance(value, bool) or not isinstance(value, int) or not low <= value <= high:
        raise ValueError(f"{name} must be an integer in {low}..{high}")
    return value


def _source(entry):
    relative = entry.get("source", "")
    if not isinstance(relative, str) or not relative:
        raise ValueError("A shell patch needs its surveyed sector source")
    source = (ROOT / relative).resolve()
    if not source.is_relative_to(ROOT):
        raise ValueError("Shell survey sources must be inside this repository")
    data = source.read_bytes()
    if hashlib.sha256(data).hexdigest() != entry.get("sha256"):
        raise ValueError("Shell source changed; survey and review the entrance selection again")
    document = json.loads(data)
    return document["Data"]["RootChunk"]


def validate_retrofit(layout):
    entries = layout.get("retrofit", {}).get("sectors", []) if isinstance(layout.get("retrofit", {}), dict) else None
    if not isinstance(entries, list) or len(entries) > 32:
        raise ValueError("Retrofit sectors must be a list of at most 32 surveyed patches")
    result, seen = [], set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("Each shell patch must be an object")
        path = entry.get("path", "")
        if not isinstance(path, str) or not path.startswith(("base\\worlds\\", "ep1\\worlds\\")) or not path.endswith(".streamingsector") or ".." in path:
            raise ValueError("A shell patch must name a vanilla world streaming sector")
        if path in seen:
            raise ValueError("Combine deletions for the same shell sector")
        seen.add(path)
        root = _source(entry)
        nodes = root.get("nodes", [])
        placements = root.get("nodeData", {}).get("Data", [])
        if entry.get("expectedNodes") != len(placements):
            raise ValueError("Shell expectedNodes does not match its surveyed source")
        deletions = entry.get("nodeDeletions", [])
        if not isinstance(deletions, list) or len(deletions) > 128:
            raise ValueError("A shell patch supports at most 128 node selections")
        clean, used = [], set()
        for deletion in deletions:
            if not isinstance(deletion, dict):
                raise ValueError("Each shell deletion must be an object")
            index = _integer(deletion.get("index"), "Shell placement index", 0, len(placements) - 1)
            if index in used:
                raise ValueError("Duplicate shell node selection")
            used.add(index)
            node = nodes[placements[index]["NodeIndex"]]["Data"]
            kind = node["$type"]
            if kind != deletion.get("type"):
                raise ValueError("Shell node type changed from the surveyed selection")
            if kind not in ("worldMeshNode", "worldStaticMeshNode", "worldInstancedMeshNode", "worldInstancedDestructibleMeshNode", "worldCollisionNode", "worldStaticOccluderMeshNode", "worldInstancedOccluderNode", "worldEntityNode", "worldEntityProxyMeshNode", "worldGenericProxyMeshNode", "worldNavigationNode"):
                raise ValueError("Shell patches support meshes, collision and explicit occluders; gameplay nodes are not entrance geometry")
            item = {"index": index, "type": kind}
            if kind == "worldInstancedOccluderNode":
                # ArchiveXL replaces the whole definition with a dummy node;
                # it does not support deleting individual occluder matrices.
                # Require an explicit, surveyed whole-group acknowledgement.
                raw = base64.b64decode(node.get("$rawTail", ""), validate=True)
                if not raw or raw[0] >= 128 or len(raw) != 1 + 64 * raw[0]:
                    raise ValueError("Unsupported instanced occluder matrix appendix")
                if deletion.get("expectedInstances") != raw[0] or deletion.get("removeWholeGroup") is not True:
                    raise ValueError("Pin every occluder instance and acknowledge removal of the whole group")
                if "instanceDeletions" in deletion or "actorDeletions" in deletion:
                    raise ValueError("ArchiveXL cannot delete individual instanced occluders")
            if kind == "worldNavigationNode":
                mask = layout.get("navigation", {}).get("terrain_mask", {})
                resource = node.get("navigationTileResource", {}).get("DepotPath", {}).get("$value")
                if mask.get("sector") != path or mask.get("placement_index") != index or deletion.get("expectedNavigationResource") != resource:
                    raise ValueError("Navigation deletion requires a pinned terrain replacement")
            if kind == "worldEntityNode":
                template = node.get("entityTemplate", {}).get("DepotPath", {}).get("$value")
                if template not in (r"base\gameplay\devices\doors\final\single_door_decorative.ent", r"base\gameplay\devices\doors\final\double_door_decorative.ent") or deletion.get("expectedTemplate") != template:
                    raise ValueError("Only an explicitly pinned decorative door entity can be replaced")
            if kind == "worldGenericProxyMeshNode":
                mesh = node.get("mesh", {}).get("DepotPath", {}).get("$value")
                name = node.get("debugName", {}).get("$value", "")
                if not mesh or deletion.get("expectedMesh") != mesh or not name.startswith(("single_door_", "double_door_")) or not name.endswith("_ProxyMesh"):
                    raise ValueError("Pin the exact mesh of a decorative door's named generic proxy")
                item["expectedMesh"] = mesh
            if kind == "worldEntityProxyMeshNode":
                owner = node.get("ownerGlobalId", {}).get("hash")
                if not owner or deletion.get("expectedOwnerGlobalId") != owner:
                    raise ValueError("Pin the decorative door proxy's exact owner identity")
            if kind == "worldCollisionNode":
                count = node.get("numActors", 0)
                if deletion.get("expectedActors") != count:
                    raise ValueError("Collision expectedActors does not match the surveyed source")
                actors = deletion.get("actorDeletions")
                if not isinstance(actors, list) or not actors:
                    raise ValueError("Select collision actors or actor/shape pairs; whole collision-node deletion is not an entrance patch")
                clean_actors = []
                for actor in actors:
                    actor_index = actor[0] if isinstance(actor, list) and len(actor) == 2 else actor
                    _integer(actor_index, "Collision actor index", 0, count - 1)
                    if isinstance(actor, list):
                        raw = base64.b64decode(node["compiledData"]["Bytes"], validate=True)
                        _, shapes = struct.unpack_from("<HH", raw, actor_index * 48 + 32)
                        _integer(actor[1], "Actor-relative shape index", 0, shapes - 1)
                    if actor in clean_actors:
                        raise ValueError("Duplicate collision actor/shape selection")
                    clean_actors.append(actor)
                item.update(expectedActors=count, actorDeletions=clean_actors)
            elif kind in ("worldInstancedMeshNode", "worldInstancedDestructibleMeshNode"):
                field = "cookedInstanceTransforms" if kind == "worldInstancedDestructibleMeshNode" else "worldTransformsBuffer"
                count = node.get(field, {}).get("numElements", 0)
                if kind == "worldInstancedDestructibleMeshNode":
                    mesh = node.get("mesh", {}).get("DepotPath", {}).get("$value")
                    if not mesh or deletion.get("expectedMesh") != mesh:
                        raise ValueError("Pin the exact mesh of surveyed destructible clutter")
                    item["expectedMesh"] = mesh
                if deletion.get("expectedInstances") != count:
                    raise ValueError("Render expectedInstances does not match the surveyed source")
                instances = deletion.get("instanceDeletions")
                if not isinstance(instances, list) or not instances:
                    raise ValueError("Select render instances rather than deleting an entire facade group")
                for instance in instances:
                    _integer(instance, "Render instance index", 0, count - 1)
                if len(instances) != len(set(instances)):
                    raise ValueError("Duplicate render instance selection")
                item.update(expectedInstances=count, instanceDeletions=instances)
            elif "actorDeletions" in deletion:
                raise ValueError("Actor deletions only apply to collision nodes")
            clean.append(item)
        if clean:
            result.append({"path": path, "expectedNodes": len(placements), "nodeDeletions": clean})
    return result


def survey(source, depot, position, radius):
    import math
    if not math.isfinite(radius) or not .1 <= radius <= 1000 or len(position) != 3 or any(not math.isfinite(v) for v in position):
        raise ValueError("Survey needs finite X/Y/Z coordinates and a radius in 0.1..1000 m")
    source = Path(source).resolve()
    if not source.is_relative_to(ROOT):
        raise ValueError("Keep reference sectors inside the repository")
    data = source.read_bytes()
    root = json.loads(data)["Data"]["RootChunk"]
    nodes, candidates = root["nodes"], []
    handles = {}
    def collect(value):
        if isinstance(value, dict):
            if "HandleId" in value and "Data" in value:
                handles[value["HandleId"]] = value["Data"]
            for child in value.values():
                collect(child)
        elif isinstance(value, list):
            for child in value:
                collect(child)
    collect(root)
    for index, placement in enumerate(root["nodeData"]["Data"]):
        definition_index = placement["NodeIndex"]
        node = nodes[definition_index]["Data"]
        p = placement["Position"]
        xyz = [p[a] for a in ("X", "Y", "Z")]
        kind = node["$type"]
        distance = sum((a - b) ** 2 for a, b in zip(xyz, position)) ** .5
        if kind == "worldInstancedMeshNode":
            transforms = node.get("worldTransformsBuffer", {})
            shared = transforms.get("sharedDataBuffer", {})
            shared = shared.get("Data", handles.get(shared.get("HandleRefId"), {}))
            buffer = shared.get("buffer", {})
            raw = base64.b64decode(buffer.get("Bytes", ""), validate=True)
            start, count = transforms.get("startIndex", 0), transforms.get("numElements", 0)
            if len(raw) < (start + count) * 48:
                raise ValueError("Truncated facade world-transform buffer")
            for instance in range(count):
                point = [v / 131072 for v in struct.unpack_from("<3i", raw, (start + instance) * 48)]
                if sum((a - b) ** 2 for a, b in zip(point, position)) <= radius * radius:
                    candidates.append({"index": index, "definition_index": definition_index, "type": kind,
                                       "render_instance": instance, "expectedInstances": count, "world_position": point, "mesh": node.get("mesh", {})})
        elif kind == "worldCollisionNode":
            raw = base64.b64decode(node["compiledData"]["Bytes"], validate=True)
            for actor in range(node.get("numActors", 0)):
                point = [v / 131072 for v in struct.unpack_from("<3i", raw, actor * 48)]
                if sum((a - b) ** 2 for a, b in zip(point, position)) > radius * radius:
                    continue
                start_shape, count = struct.unpack_from("<HH", raw, actor * 48 + 32)
                shapes = []
                for relative in range(count):
                    offset = node["numActors"] * 48 + (start_shape + relative) * 32
                    kind_code = struct.unpack_from("<h", raw, offset + 12)[0]
                    shape = {"relative_index": relative, "type_code": kind_code}
                    if kind_code == 0:
                        shape["box_half_extents_collision_axes"] = list(struct.unpack_from("<3f", raw, offset))
                    elif kind_code in (4, 5):
                        shape["geometry_hash"] = str(struct.unpack_from("<Q", raw, offset)[0])
                    shapes.append(shape)
                candidates.append({"index": index, "type": kind, "expectedActors": node["numActors"],
                                   "actor": actor, "shape_count": count, "world_position": point,
                                   "actor_orientation": list(struct.unpack_from("<4f", raw, actor * 48 + 16)),
                                   "actor_scale": collision_actor_scale(node, raw, actor), "shapes": shapes})
        elif distance <= radius and kind in ("worldMeshNode", "worldStaticMeshNode", "worldStaticOccluderMeshNode"):
            candidates.append({"index": index, "type": kind, "world_position": xyz,
                               "mesh": node.get("mesh", {}), "debug_name": node.get("debugName", {})})
    return {"schema_version": 1, "selection": {"source": source.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(data).hexdigest(),
            "path": depot, "expectedNodes": len(root["nodeData"]["Data"]), "nodeDeletions": []}, "candidates": candidates,
            "indexing": "ArchiveXL indices and expectedNodes address nodeData placements, not node definitions.",
            "notes": ["Copy the selection into layout.retrofit.sectors and populate nodeDeletions with reviewed candidate indices.",
                      "Actor pivots are candidate hints, not mesh extents. A large triangle-mesh actor can extend beyond the search radius.",
                      "Remove visual geometry and its separate collision. Replace the removed bay with your doorway module.",
                      "Occlusion may be separate; removing the visible mesh alone does not establish a working entrance."]}


def survey_nearby(blocks, sector_root, position, radius, output):
    """Discover finite overlapping sector descriptors, then survey cached sources.

    Descriptor bounds and actor pivots are broad-phase hints, not proof of a
    collision match. Unbounded always-loaded/quest descriptors are reported.
    """
    import math
    from artifact_io import atomic_write_json
    from world_location_world import AABB, WorldSectorIndex
    if len(position) != 3 or any(not math.isfinite(v) for v in position) or not math.isfinite(radius) or not .1 <= radius <= 1000:
        raise ValueError("Survey needs finite X/Y/Z coordinates and a radius in 0.1..1000 m")
    sector_root, output = Path(sector_root).resolve(), Path(output).resolve()
    if not sector_root.is_relative_to(ROOT):
        raise ValueError("Keep reference sectors inside the repository")
    descriptors = WorldSectorIndex.from_streaming_blocks(blocks).query(AABB(
        *(v - radius for v in position), *(v + radius for v in position)))
    rows, missing, unbounded, seen = [], [], [], set()
    for descriptor in descriptors:
        depot = descriptor.depot_path
        if depot in seen:
            continue
        seen.add(depot)
        bounds = descriptor.bounds
        if any(not math.isfinite(v) or abs(v) > 100000 for v in (
            bounds.min_x, bounds.min_y, bounds.min_z, bounds.max_x, bounds.max_y, bounds.max_z)):
            unbounded.append(depot)
            continue
        source = (sector_root / (depot.replace("\\", "/") + ".json")).resolve()
        if not source.is_relative_to(sector_root):
            raise ValueError("Unsafe sector path in the streaming block")
        if not source.is_file():
            missing.append(depot)
            continue
        result = survey(source, depot, position, radius)
        if result["candidates"]:
            name = hashlib.sha256(depot.encode()).hexdigest()[:12] + ".survey.json"
            atomic_write_json(output / name, result)
            rows.append({"path": depot, "survey": name, "candidates": len(result["candidates"]),
                         "collision_candidates": sum(c["type"] == "worldCollisionNode" for c in result["candidates"])})
    report = {"schema_version": 1, "position": position, "radius": radius, "surveys": rows,
              "scanned_cached_sectors": len(seen) - len(missing) - len(unbounded),
              "missing_cached_sectors": missing, "unbounded_descriptors_skipped": unbounded,
              "notes": ["Import individual survey files in Shell entrance patches; selections across sectors are retained.",
                        "Descriptor bounds and actor pivots are broad-phase hints; inspect geometry before matching a facade to collision.",
                        "Missing cached sectors and unbounded descriptors mean this is not an exhaustive collision search."]}
    atomic_write_json(output / "index.json", report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sector", type=Path, nargs="?")
    parser.add_argument("--depot")
    parser.add_argument("--streaming-block", type=Path, action="append", default=[])
    parser.add_argument("--sector-root", type=Path)
    parser.add_argument("--position", nargs=3, type=float, required=True)
    parser.add_argument("--radius", type=float, default=8)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    from artifact_io import atomic_write_json
    if args.streaming_block:
        if not args.sector_root or args.sector or args.depot:
            parser.error("Area surveys need --streaming-block and --sector-root, without a positional sector or --depot")
        survey_nearby(args.streaming_block, args.sector_root, args.position, args.radius, args.out)
    else:
        if not args.sector or not args.depot or args.sector_root:
            parser.error("Single-sector surveys need a sector and --depot")
        atomic_write_json(args.out, survey(args.sector, args.depot, args.position, args.radius))


if __name__ == "__main__":
    main()
