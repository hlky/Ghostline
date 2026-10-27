#!/usr/bin/env python3
"""Read-only vanilla building research; writes compact evidence, never game assets.

The optional corpus scan counts serialized references, NOT placed instances.
Case studies resolve nodeData indices separately from definition indices.
"""
from __future__ import annotations

import argparse
import base64
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import struct
import subprocess


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "converted/world-location-database/full-world/serialized-sectors/base/worlds/03_night_city/_compiled/default"
CASES = (
    "interior_-48_-31_2_0", "interior_-24_-16_1_1",
    "exterior_-16_22_0_0", "exterior_5_-26_0_0",
    "exterior_7_-32_0_0", "exterior_6_-32_0_0",
    "exterior_2_-26_0_0", "exterior_4_-29_-1_0",
    "interior_21_-27_0_1", "interior_3_-29_-1_1",
    "exterior_-3_11_0_1", "interior_-4_5_0_4",
    "navigation_1_-7_0_3",
)
ENVIRONMENT = {
    "worldInteriorAreaNode", "worldTriggerAreaNode", "worldAmbientAreaNode",
    "worldReflectionProbeNode", "worldInteriorMapNode", "worldGIShapeNode",
    "worldGISpaceNode", "worldNavigationNode", "worldAcousticPortalNode",
    "worldBuildingProxyMeshNode", "worldStaticOccluderMeshNode",
}


def scalar(value):
    return value.get("$value", value) if isinstance(value, dict) else value


def paths(value):
    if isinstance(value, dict):
        if "DepotPath" in value:
            path = scalar(value["DepotPath"])
            if isinstance(path, str) and "\\" in path:
                yield path
        for item in value.values():
            yield from paths(item)
    elif isinstance(value, list):
        for item in value:
            yield from paths(item)


def buffer_summary(value):
    """Retain settings but replace opaque buffers with byte counts and hashes."""
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            if key.lower() in {"buffer", "bytes"} and isinstance(item, str):
                try:
                    raw = base64.b64decode(item, validate=True)
                except ValueError:
                    result[key] = item
                else:
                    result[key] = {"decoded_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
            else:
                result[key] = buffer_summary(item)
        return result
    if isinstance(value, list):
        return [buffer_summary(item) for item in value]
    return value


def inspect_collision(node):
    """Inspect parsed collision data or raw layout from WKit CollisionReader.

    Only actor transforms, shape identity and scale are decoded. Material and
    collision-filter tables remain in the source resource.
    """
    compiled = node.get("compiledData", {})
    parsed = compiled.get("Data", {}).get("Actors")
    if parsed is not None:
        return {"actor_count": len(parsed), "shape_types": dict(Counter(
            str(s.get("ShapeType")) for a in parsed for s in a.get("Shapes", []))),
            "sample_actors": parsed[:2], "encoding": "parsed"}
    actor_count = node.get("numActors")
    shape_count = node.get("numShapeInfos")
    result = {"actor_count": actor_count, "shape_count": shape_count,
              "encoding": "opaque"}
    if "Bytes" not in compiled or actor_count is None or shape_count is None:
        return result
    raw = base64.b64decode(compiled["Bytes"], validate=True)
    shape_offset = actor_count * 48
    scale_offset = (shape_offset + shape_count * 32
                    + node.get("numShapePositions", 0) * 12
                    + node.get("numShapeRotations", 0) * 16)
    if len(raw) < scale_offset + node.get("numScales", 0) * 12:
        raise ValueError("Truncated collision buffer")
    kinds = {0: "Box", 1: "Sphere", 2: "Capsule", 3: "ConvexMesh", 4: "TriangleMesh", 6: "Invalid"}
    shape_types = []
    shapes = []
    for index in range(shape_count):
        offset = shape_offset + index * 32
        kind = struct.unpack_from("<h", raw, offset + 12)[0]
        shape_types.append(kinds.get(kind, str(kind)))
        shape = {"shape_index": index, "type": shape_types[-1]}
        if kind in (3, 4):
            shape["hash"] = str(struct.unpack_from("<Q", raw, offset)[0])
        else:
            shape["size"] = struct.unpack_from("<3f", raw, offset)
        shapes.append(shape)
    actors = []
    for index in range(min(actor_count, 2)):
        offset = index * 48
        xyz = struct.unpack_from("<3i", raw, offset)
        start, count, scale_index = struct.unpack_from("<HHh", raw, offset + 32)
        if start + count > shape_count:
            raise ValueError("Collision actor shape range exceeds shape table")
        if scale_index < -1 or scale_index >= node.get("numScales", 0):
            raise ValueError("Collision actor scale index exceeds scale table")
        actors.append({"actor_index": index, "world_position": [v / 131072 for v in xyz],
                       "orientation_ijkr": struct.unpack_from("<4f", raw, offset + 16),
                       "scale": struct.unpack_from("<3f", raw, scale_offset + scale_index * 12) if scale_index >= 0 else (1, 1, 1),
                       "shapes": shapes[start:start + count]})
    return {**result, "encoding": "raw_decoded", "buffer_sha256": hashlib.sha256(raw).hexdigest(),
            "shape_types": dict(Counter(shape_types)), "sample_actors": actors}


def inspect_navigation(document):
    from world_location_nav import load_navigation_sector, vand_position_to_world
    resources = []
    for embedded in document["Data"].get("EmbeddedFiles", []):
        content = embedded.get("Content", {})
        if content.get("$type") != "worldNavigationTileResource":
            continue
        resource_path = scalar(embedded["FileName"])
        sector = load_navigation_sector({"Data": {"RootChunk": content}}, source_id=resource_path, human_only=False)
        vertices = [vand_position_to_world(vertex) for tile in sector.buffers for vertex in tile.vertices]
        resources.append({
            "resource": resource_path, "agent": sector.agent_size,
            "buffers": len(sector.buffers), "vertices": len(vertices),
            "faces": sum(len(tile.faces) for tile in sector.buffers),
            "triangles": sum(face.num_indices == 3 for tile in sector.buffers for face in tile.faces),
            "magic": sorted({tile.header.magic.decode("ascii") for tile in sector.buffers}),
            "header_unknown_1": sorted({tile.header.unknown_1 for tile in sector.buffers}),
            "world_vertex_bounds": {axis: [min(getattr(v, axis) for v in vertices), max(getattr(v, axis) for v in vertices)] for axis in ("x", "y", "z")} if vertices else None,
            "off_mesh_connection_records": sum(len(tile.get("offMeshConnections", {}).get("ids", [])) for tile in content.get("tilesData", [])),
        })
    return resources


def inspect_resource_jobs(manifest_path):
    resources = []
    for job in json.loads(manifest_path.read_bytes())["jobs"]:
        path = Path(job["output"])
        raw = path.read_bytes()
        document = json.loads(raw)
        root = document["Data"]["RootChunk"]
        item = {"resource": job["resource"], "serialized_json_sha256": hashlib.sha256(raw).hexdigest(),
                "root_type": root["$type"]}
        if root["$type"] == "CMesh":
            bounds = root.get("boundingBox")
            parameters = [parameter.get("Data", parameter).get("$type") for parameter in root.get("parameters", [])]
            item.update({"bounds": bounds,
                         "dimensions": {axis: bounds["Max"][axis] - bounds["Min"][axis] for axis in ("X", "Y", "Z")} if bounds else None,
                         "parameters": parameters,
                         "has_mesh_physics_parameter": "meshMeshParamPhysics" in parameters,
                         "appearances": [scalar(appearance.get("Data", appearance).get("name", "default")) for appearance in root.get("appearances", [])]})
        resources.append(item)
    return resources


def compact_snapshot(result):
    snapshot = {key: value for key, value in result.items() if key not in ("case_studies", "corpus")}
    snapshot["case_studies"] = [{key: value for key, value in case.items() if key not in ("architecture", "environment", "collision")} | {
        "architecture_definitions": len(case["architecture"]),
        "collision_actor_count": sum(node.get("actor_count") or 0 for node in case["collision"]),
        "collision_shape_types": dict(sum((Counter(node.get("shape_types", {})) for node in case["collision"]), Counter())),
        "interior_areas": [{key: value for key, value in node.items() if key != "settings"} | {
            "settings": node["settings"]} for node in case["environment"] if node["type"] == "worldInteriorAreaNode"],
    } for case in result["case_studies"]]
    if "corpus" in result:
        snapshot["corpus"] = {key: value for key, value in result["corpus"].items() if key != "architecture_resources"}
    return snapshot


def inspect_case(path):
    raw = path.read_bytes()
    document = json.loads(raw)
    root = document["Data"]["RootChunk"]
    nodes = [item.get("Data", item) for item in root["nodes"]]
    placements = root["nodeData"]["Data"]
    by_definition = defaultdict(list)
    for instance_index, placement in enumerate(placements):
        definition_index = placement["NodeIndex"]
        if not 0 <= definition_index < len(nodes):
            raise ValueError(f"Invalid NodeIndex in {path}: {definition_index}")
        by_definition[definition_index].append(instance_index)
    architecture = []
    environment = []
    collision = []
    for index, node in enumerate(nodes):
        kind = node["$type"]
        resources = sorted(set(paths(node)))
        identity = {
            "definition_index": index,
            "node_data_indices": by_definition[index],
            "type": kind,
            "debug_name": scalar(node.get("debugName")),
            "source_prefab_hash": node.get("sourcePrefabHash"),
        }
        if any("\\architecture\\" in item for item in resources):
            architecture.append({
                **identity, "resources": resources,
                "mesh_appearance": scalar(node.get("meshAppearance")),
                "instance_buffers": {key: buffer_summary(node[key]) for key in ("worldTransformsBuffer", "cookedInstanceTransforms") if key in node},
                "placements": [{"node_data_index": p, **placements[p]} for p in by_definition[index]],
            })
        if kind in ENVIRONMENT:
            environment.append({**identity, "settings": buffer_summary(node),
                                "placements": [{"node_data_index": p, **placements[p]} for p in by_definition[index]]})
        if kind == "worldCollisionNode":
            collision.append({**identity, "sector_hash": node.get("sectorHash"),
                              **inspect_collision(node)})
    return {
        "file": path.name, "sha256": hashlib.sha256(raw).hexdigest(),
        "size": len(raw), "header_game_version": document["Header"].get("GameVersion"),
        "category": root.get("category"), "level": root.get("level"),
        "node_definitions": len(nodes), "node_data_instances": len(placements),
        "node_types": dict(sorted(Counter(node["$type"] for node in nodes).items())),
        "variant_indices": root.get("variantIndices"),
        "architecture": architecture, "environment": environment, "collision": collision,
        "navigation": inspect_navigation(document),
    }


def scan_corpus(source):
    # JSON strings are kept escaped until json.loads, preserving depot backslashes.
    pattern = r'"\$type"\s*:\s*"world[^"\r\n]*Node[^"\r\n]*"|"\$value"\s*:\s*"(?:base|ep1)\\\\environment\\\\architecture\\\\[^"\r\n]*"'
    process = subprocess.Popen(
        ["rg", "--no-filename", "--no-heading", "--color", "never", "-o", pattern,
         "-g", "*.streamingsector.json", str(source)],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8",
    )
    node_types = Counter()
    resources = Counter()
    assert process.stdout is not None
    for line in process.stdout:
        key, value = next(iter(json.loads("{" + line.strip() + "}").items()))
        (node_types if key == "$type" else resources)[value] += 1
    stderr = process.stderr.read() if process.stderr else ""
    code = process.wait()
    if code not in (0, 1):
        raise RuntimeError(f"rg failed ({code}): {stderr}")
    kits = Counter()
    for resource in resources:
        parts = resource.split("\\")
        family = "\\".join(parts[:6]) if "\\common\\int\\" in resource else "\\".join(parts[:5])
        kits[family] += 1
    files = list(source.glob("*.streamingsector.json"))
    return {
        "method": "Lexical counts of serialized $type and architecture $value fields; neither count is a placed-instance count. Resources are referenced paths, not archive-existence certification.",
        "files": len(files), "bytes": sum(path.stat().st_size for path in files),
        "node_type_occurrences": dict(sorted(node_types.items())),
        "architecture_resource_count": len(resources),
        "architecture_families_unique_paths": dict(kits.most_common()),
        "architecture_resources": dict(sorted(resources.items())),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=ROOT / "generated/building-interiors/evidence.json")
    scan = parser.add_mutually_exclusive_group()
    scan.add_argument("--scan-corpus", action="store_true")
    scan.add_argument("--reuse-corpus", type=Path, help="Reuse a prior expensive lexical scan; preserves its original provenance")
    parser.add_argument("--case", action="append", help="Sector stem; overrides the case-study defaults")
    parser.add_argument("--resource-jobs", type=Path, help="Native CR2W serialization job manifest whose completed outputs should be inspected")
    parser.add_argument("--snapshot", type=Path, help="Optional compact reference snapshot without the full per-node or per-resource inventory")
    args = parser.parse_args()
    if not args.source.is_dir():
        parser.error(f"Sector source does not exist: {args.source}")
    result = {"schema_version": 1, "generated_by": "tools/audit_building_interiors.py",
              "source_root": str(args.source.resolve()), "case_studies": [], "missing_cases": []}
    for case in args.case or CASES:
        path = args.source / (case + ".streamingsector.json")
        if not path.is_file():
            result["missing_cases"].append(case)
            continue
        result["case_studies"].append(inspect_case(path))
    print(f"Inspected {len(result['case_studies'])} cases; missing {len(result['missing_cases'])}", flush=True)
    if args.scan_corpus:
        result["corpus"] = scan_corpus(args.source)
        result["corpus"]["source_root"] = str(args.source.resolve())
    elif args.reuse_corpus:
        previous = json.loads(args.reuse_corpus.read_bytes())
        result["corpus"] = previous["corpus"]
        result["corpus"].setdefault("source_root", previous["source_root"])
    if args.resource_jobs:
        result["archive_resource_samples"] = inspect_resource_jobs(args.resource_jobs)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}", flush=True)
    if args.snapshot:
        args.snapshot.parent.mkdir(parents=True, exist_ok=True)
        args.snapshot.write_text(json.dumps(compact_snapshot(result), indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {args.snapshot}", flush=True)


if __name__ == "__main__":
    main()
