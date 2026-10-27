"""Measure and prepare the complete discovered vanilla architecture catalogue.

All source mesh buffers stay in generated output. The checked catalogue carries
small measured records, source hashes and per-resource failures, not game data.
Family names and role labels are discovery hints, never compatibility proofs.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import struct
import subprocess

from artifact_io import atomic_write_json
from toolchain import resolve_tool

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "generated/building-editor/library"
CATALOG = ROOT / "reference/world/building-kit-catalog.json"
EVIDENCE = ROOT / "generated/building-interiors/evidence.json"
MESH_EXTENSIONS = (".mesh", ".w2mesh")
_catalog_cache = None
_catalog_stamp = None


def resource_id(path):
    return hashlib.sha256(path.encode()).hexdigest()[:20]


def family_path(path):
    parts = path.split("\\")
    # Preserve the original discovery grouping, but do not call a filename a
    # family when a resource sits directly in a shallow architecture directory.
    count = 6 if "\\common\\int\\" in path else 5
    return "\\".join(parts[:min(count, len(parts) - 1)])


def role_hint(path):
    name = path.rsplit("\\", 1)[-1].lower()
    family = family_path(path).rsplit("\\", 1)[-1].lower()
    if name.startswith(family + "_"):
        name = name[len(family)+1:]
    for role, pattern in (("doorway", r"door|entrance|gate"),
                          ("railing", r"rail|balustr|barrier|fence"), ("window", r"window|glass"),
                          ("ceiling", r"ceiling"), ("floor", r"floor|catwalk|platform"),
                          ("roof", r"roof|canopy"), ("wall", r"wall|facade|backwall"),
                          ("stairs", r"stair|landing|ramp"),
                          ("structure", r"pillar|column|beam|support|frame"), ("trim", r"trim|cornice|gutter|skirt")):
        if re.search(pattern, name):
            return role
    return "specialist"


def glb_geometry(path):
    """Read actual GLB POSITION bounds; the native exporter writes Y-up geometry.

    Transform-free mesh nodes are required for this measurement. We reject
    transformed scenes rather than silently reporting their local-space bounds.
    """
    with Path(path).open("rb") as stream:
        header = stream.read(20)
        if len(header) != 20 or header[:4] != b"glTF" or struct.unpack_from("<I", header, 4)[0] != 2 or header[16:20] != b"JSON":
            raise ValueError("Expected a binary glTF version 2")
        length = struct.unpack_from("<I", header, 12)[0]
        if length > 64 * 1024 * 1024:
            raise ValueError("GLB metadata is too large")
        document = json.loads(stream.read(length))
    if any(any(k in n for k in ("matrix", "translation", "rotation", "scale")) for n in document.get("nodes", [])):
        raise ValueError("GLB node transforms need explicit measurement support")
    positions = []
    vertices = triangles = 0
    for mesh in document.get("meshes", []):
        for primitive in mesh.get("primitives", []):
            accessor = document["accessors"][primitive["attributes"]["POSITION"]]
            lo, hi = accessor["min"], accessor["max"]
            if len(lo) != 3 or len(hi) != 3 or any(not math.isfinite(v) for v in lo + hi):
                raise ValueError("Invalid GLB position bounds")
            positions.append(([lo[0], -hi[2], lo[1]], [hi[0], -lo[2], hi[1]]))
            vertices += accessor["count"]
            if primitive.get("mode", 4) == 4:
                triangles += document["accessors"][primitive["indices"]]["count"] // 3 if "indices" in primitive else accessor["count"] // 3
    if not positions:
        raise ValueError("GLB has no measured render geometry")
    low = [min(p[0][i] for p in positions) for i in range(3)]
    high = [max(p[1][i] for p in positions) for i in range(3)]
    return {"min": low, "max": high, "dimensions": [high[i] - low[i] for i in range(3)],
            "vertices": vertices, "triangles": triangles}


def measure_record(resource, raw, preview=None, *, decode_error=None, preview_error=None, material_error=None):
    identity = resource_id(resource)
    result = {"id": identity, "path": resource, "name": resource.rsplit("\\", 1)[-1].rsplit(".",1)[0],
              "family": family_path(resource), "role": role_hint(resource), "status": "unavailable"}
    if decode_error or not Path(raw).is_file():
        result["error"] = decode_error or "No serialized vanilla resource"
        return result
    data = Path(raw).read_bytes()
    document = json.loads(data)
    root = document["Data"]["RootChunk"]
    if root["$type"] != "CMesh":
        result["error"] = "Resource is not a CMesh"
        return result
    bounds = root.get("boundingBox", {})
    low = [bounds["Min"][axis] for axis in ("X", "Y", "Z")]
    high = [bounds["Max"][axis] for axis in ("X", "Y", "Z")]
    if any(not math.isfinite(v) for v in low + high) or any(a > b for a, b in zip(low, high)):
        raise ValueError("Invalid source mesh bounds")
    appearances = [a.get("Data", a).get("name", {}).get("$value", "default") for a in root.get("appearances", [])]
    result.update(status="measured", bounds={"min": low, "max": high, "dimensions": [b-a for a,b in zip(low, high)]},
                  appearances=list(dict.fromkeys(appearances)) or ["default"], source_json_sha256=hashlib.sha256(data).hexdigest(),
                  source_content_sha256=hashlib.sha256(json.dumps(document["Data"],sort_keys=True,separators=(",", ":")).encode()).hexdigest())
    if preview and Path(preview).is_file() and not preview_error:
        try:
            result["geometry"] = glb_geometry(preview)
            result.update(status="prepared", preview_sha256=hashlib.sha256(Path(preview).read_bytes()).hexdigest())
        except (ValueError, KeyError, OSError, struct.error) as error:
            result["preview_error"] = str(error)
    elif preview_error:
        result["preview_error"] = preview_error
    if material_error:
        result["material_warning"] = material_error
    return result


def discover(evidence=None):
    source=Path(evidence) if evidence is not None else (EVIDENCE if EVIDENCE.is_file() else CATALOG)
    data=json.loads(source.read_bytes())
    if "corpus" in data:
        return data["corpus"]["architecture_resources"]
    # The checked catalogue is sufficient to rebuild caches on a fresh clone.
    return {path:1 for path in [*(record["path"] for record in data["assets"]),*data.get("non_mesh_references",[])]}


def write_manifests(evidence=None):
    resources = sorted(p for p in discover(evidence) if p.endswith(MESH_EXTENSIONS))
    CACHE.mkdir(parents=True, exist_ok=True)
    atomic_write_json(CACHE / "measure-jobs.json", {"jobs": [
        {"resource": p, "output": str((CACHE / "raw" / (resource_id(p) + ".mesh.json")).resolve())} for p in resources]})
    atomic_write_json(CACHE / "preview-jobs.json", {"jobs": [
        {"mesh": p, "output": str((CACHE / "assets" / (resource_id(p) + ".glb")).resolve())} for p in resources]})
    return resources


def prepare(kind, *, threads=4, resume=False):
    from ghostline_red import ensure_schema
    write_manifests()
    manifest = CACHE / (kind + "-jobs.json")
    jobs = json.loads(manifest.read_bytes())["jobs"]
    if resume:
        def complete(job):
            path = Path(job["output"])
            if not path.is_file():
                return False
            try:
                glb_geometry(path) if kind == "preview" else json.loads(path.read_bytes())
                return True
            except (ValueError, KeyError, OSError, struct.error):
                return False
        jobs = [j for j in jobs if not complete(j)]
    if not jobs:
        return
    run_manifest = CACHE / (kind + "-pending-jobs.json")
    atomic_write_json(run_manifest, {"jobs": jobs})
    command = [str(resolve_tool("ghostline_red")), "cr2w-serialize-batch" if kind == "measure" else "mesh-export-batch", str(run_manifest),
               "--schema", str(ensure_schema()), "--archives-root", str(resolve_tool("game") / "archive/pc/content"),
               "--report", str(CACHE / (kind + "-report.json")), "--threads", str(threads)]
    if kind == "preview":
        command += ["--geometry-only"]
    # A failing resource must not prevent inspection of successful sibling jobs.
    previous_report = CACHE / (kind + "-report.json")
    previous = json.loads(previous_report.read_bytes()) if previous_report.is_file() else []
    result = subprocess.run(command, check=False)
    if result.returncode and not (CACHE / (kind + "-report.json")).is_file():
        raise RuntimeError("Native preparation failed without a per-resource report")
    merged = {row.get("resource", row.get("mesh")): row for row in previous}
    merged.update({row.get("resource", row.get("mesh")): row for row in json.loads(previous_report.read_bytes())})
    atomic_write_json(previous_report, list(merged.values()))
    expansion_jobs = [j for j in jobs if j.get("resource", j.get("mesh", "")).startswith("ep1\\")]
    expansion_root = resolve_tool("game") / "archive/pc/ep1"
    if expansion_jobs and expansion_root.is_dir():
        expansion_manifest = CACHE / (kind + "-ep1-jobs.json")
        atomic_write_json(expansion_manifest, {"jobs": expansion_jobs})
        command[2] = str(expansion_manifest)
        command[command.index("--archives-root") + 1] = str(expansion_root)
        command[command.index("--report") + 1] = str(CACHE / (kind + "-ep1-report.json"))
        subprocess.run(command, check=False)


def build_catalog(evidence=None, output=CATALOG):
    resources = discover(evidence)
    reports = {}
    for kind in ("measure", "preview"):
        path = CACHE / (kind + "-report.json")
        reports[kind] = {row.get("resource", row.get("mesh")): row for row in json.loads(path.read_bytes())} if path.is_file() else {}
        expansion = CACHE / (kind + "-ep1-report.json")
        if expansion.is_file():
            reports[kind].update({row.get("resource", row.get("mesh")): row for row in json.loads(expansion.read_bytes())})
    records = []
    for resource in sorted(p for p in resources if p.endswith(MESH_EXTENSIONS)):
        identity = resource_id(resource)
        decode, preview = reports["measure"].get(resource, {}), reports["preview"].get(resource, {})
        try:
            record = measure_record(resource, CACHE / "raw" / (identity + ".mesh.json"), CACHE / "assets" / (identity + ".glb"),
                                    decode_error=decode.get("error"), preview_error=preview.get("error"), material_error=preview.get("material_error"))
        except (KeyError, ValueError, OSError) as error:
            record = {"id": identity, "path": resource, "name": resource.rsplit("\\", 1)[-1], "family": family_path(resource),
                      "role": role_hint(resource), "status": "unavailable", "error": str(error)}
        records.append(record)
    grouped = {}
    for record in records:
        group = grouped.setdefault(record["family"], {"path": record["family"], "name": record["family"].removeprefix("base\\environment\\architecture\\").replace("\\", " / "),
                                                    "assets": 0, "prepared": 0, "measured": 0, "unavailable": 0, "roles": Counter()})
        group["assets"] += 1
        group[record["status"]] += 1
        group["roles"][record["role"]] += 1
    catalog = {"schema_version": 1, "source": "Night City reference corpus; not an exhaustive base-game or expansion archive inventory",
               "preview_materials": "Neutral geometry previews; material dependency completeness is not certified",
               "source_resource_count": len(resources), "mesh_count": len(records), "non_mesh_references": sorted(p for p in resources if not p.endswith(MESH_EXTENSIONS)),
               "counts": dict(Counter(r["status"] for r in records)), "families": list(grouped.values()), "assets": records,
               "limitations": ["Prepared means source bounds, appearances and render geometry were read successfully. It is not an in-game compatibility certificate.",
                               "Role names are filename search hints. Freely placed modules do not create rooms, collision, navigation surfaces or working devices automatically.",
                               "Material warnings are recorded; previews use neutral geometry. Source mesh pivots and dimensions are preserved."]}
    atomic_write_json(output, catalog)
    return catalog


def catalog():
    global _catalog_cache, _catalog_stamp
    if not CATALOG.is_file():
        return {"assets": [], "families": [], "counts": {}}
    props = ROOT / "reference/world/building-props-catalog.json"
    stamp = (CATALOG.stat().st_mtime_ns, CATALOG.stat().st_size, props.stat().st_mtime_ns if props.exists() else 0)
    if stamp != _catalog_stamp:
        _catalog_cache, _catalog_stamp = json.loads(CATALOG.read_bytes()), stamp
        if props.exists():
            additions = json.loads(props.read_bytes())['assets']
            _catalog_cache['assets'].extend(additions)
            for record in additions:
                _catalog_cache['counts'][record['status']] = _catalog_cache['counts'].get(record['status'], 0) + 1
            for family in sorted({r['family'] for r in additions}):
                group = [r for r in additions if r['family'] == family]
                _catalog_cache['families'].append(dict(path=family, name='Office furniture / '+family.rsplit('\\',1)[-1],
                    assets=len(group), prepared=sum(r['status']=='prepared' for r in group)))
        _catalog_cache["by_id"] = {r["id"]: r for r in _catalog_cache["assets"]}
    return _catalog_cache


def asset(identity, *, prepared=True):
    if not isinstance(identity, str):
        raise ValueError("Choose a prepared vanilla architecture module")
    record = catalog().get("by_id", {}).get(identity)
    if record is None and re.fullmatch(r'[a-f0-9]{20}', identity):
        variant = ROOT/'projects/experiments/building-lab/mesh-variants'/(identity+'.json')
        if variant.is_file():
            record = json.loads(variant.read_bytes())
            if record.get('id') != identity or not record.get('authored_raw'):
                raise ValueError('Invalid authored mesh variant')
            raw=(ROOT/record['authored_raw']).resolve()
            owner=(ROOT/'projects/experiments/building-lab/source/raw/mod/building_lab').resolve()
            if not raw.is_relative_to(owner) or hashlib.sha256(raw.read_bytes()).hexdigest()!=record['source_json_sha256']:
                raise ValueError('Authored mesh variant changed; remeasure and review it')
    if not record or (prepared and record["status"] != "prepared"):
        raise ValueError("Choose a prepared vanilla architecture module")
    return record


def search(*, query="", family="", role="", offset=0, limit=48):
    tokens = query.casefold().split()
    rows = [r for r in catalog()["assets"] if (not family or r["family"] == family) and (not role or r["role"] == role)
            and all(token in r["path"].casefold() for token in tokens)]
    return {"total": len(rows), "offset": offset, "assets": rows[offset:offset+limit]}


def compile_modules(scene, world_point):
    """Preserve real vanilla pivots and sizes; never squeeze modules onto a grid."""
    from building_builder import ID, number
    layout = scene["layout"]
    modules = layout.setdefault("modules", [])
    if not isinstance(modules, list) or len(modules) > 256:
        raise ValueError("A building supports at most 256 library modules")
    used = set()
    for module in modules:
        if not isinstance(module, dict) or not isinstance(module.get("id"), str) or not ID.fullmatch(module["id"]) or module["id"] in used:
            raise ValueError("Module ids must be unique lowercase identifiers")
        used.add(module["id"])
        record = asset(module.get("asset"))
        for field, expected in (("source_sha256", record.get("source_content_sha256", record["source_json_sha256"])), ("geometry_sha256", record["preview_sha256"])):
            if module.setdefault(field, expected) != expected:
                raise ValueError("Library source changed; review and reselect this module")
        appearance = module.setdefault("appearance", record["appearances"][0])
        if appearance not in record["appearances"]:
            raise ValueError("Choose an appearance actually present in the selected vanilla mesh")
        point = module.get("position")
        if not isinstance(point, list) or len(point) != 3:
            raise ValueError("Module position needs local X, Y, Z")
        point = [number(v, "Module position", -8000, 8000) for v in point]
        module["position"] = point
        yaw = number(module.setdefault("yaw", 0), "Module yaw", -360, 360)
        scale = module.get("scale", [1, 1, 1])
        if not isinstance(scale, list) or len(scale) != 3:
            raise ValueError("Module scale needs three positive axis values")
        scale = [number(v, "Module scale", .1, 10) for v in scale]
        clear_glass = module.get("clear_glass", False)
        if not isinstance(clear_glass, bool) or (clear_glass and record["id"] != "8d7d3e6409823ceb7395"):
            raise ValueError("Clear glass requires the measured Rancho window variant")
        level = module.setdefault("level", 0)
        if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= 3:
            raise ValueError("Module floor must be 0..3")
        anchor = module.setdefault("anchor", "base-center")
        collision = module.setdefault("collision", "none")
        reference = module.get('reference_only', False)
        if not isinstance(reference, bool) or (reference and collision != 'none'):
            raise ValueError('Existing shell references must be preview-only with no added collision')
        if anchor not in ("pivot", "base-center") or collision not in ("none", "box"):
            raise ValueError("Choose a vanilla pivot or base-centre anchor, and no collision or a solid box")
        rotation = module.get("rotation")
        if rotation is not None:
            if not isinstance(rotation, list) or len(rotation) != 4 or anchor != "pivot" or collision != "none":
                raise ValueError("Full module rotation requires a pivot anchor and no box collision")
            rotation = [number(v, "Module quaternion", -1, 1) for v in rotation]
            if abs(sum(v*v for v in rotation)-1) > 1e-4:
                raise ValueError("Module quaternion must have unit length")
        if collision == "box" and record["role"] not in ("wall", "floor", "ceiling", "structure"):
            raise ValueError("Solid boxes are only suitable for reviewed wall, floor, ceiling or structural modules; they fill every opening")
        bounds = record["geometry"]
        low, high = [[v * s for v, s in zip(bounds[k], scale)] for k in ("min", "max")]
        if any(b - a < 1e-5 for a, b in zip(low, high)):
            if collision == "box":
                raise ValueError("A zero-thickness mesh cannot create a solid collision box")
        center = [(a+b)/2 for a,b in zip(low,high)]
        pivot = point[:]
        angle = math.radians(yaw)
        if anchor == "base-center":
            pivot = [point[0] - center[0]*math.cos(angle) + center[1]*math.sin(angle),
                     point[1] - center[0]*math.sin(angle) - center[1]*math.cos(angle), point[2] - low[2]]
        scene["instances"].append({"id": "module:" + module["id"], "role": "module", "kind": "module", "asset": record["id"],
            "reference_only": reference, "reference_side": module.get('reference_side'), "reference_role": record['role'],
            **({'authored_raw':record['authored_raw'],'authored_sha256':record['source_json_sha256']} if record.get('authored_raw') else {}),
            "name": record["name"], "mesh": r"mod\building_lab\rancho-window-clear.mesh" if clear_glass else record["path"],
            "appearance": appearance, "position": pivot, "yaw": yaw, "scale": scale,
            "appearances": record["appearances"],
            "world_position": world_point(pivot, layout["origin"]), "world_yaw": yaw + layout["origin"]["yaw"], "level": level,
            "room": None, "edge": None, "bounds": {"min": low, "max": high},
            "extent_radius": max(math.sqrt(sum(max(abs(a),abs(b))**2 for a,b in zip(low, high))),
                math.sqrt(sum((max(abs(a),abs(b))*s)**2 for a,b,s in zip(record.get("bounds",bounds)["min"],record.get("bounds",bounds)["max"],scale))))})
        if rotation is not None:
            x,y,z,w = rotation
            a = math.radians(layout["origin"]["yaw"]) / 2
            sine, cosine = math.sin(a), math.cos(a)
            scene["instances"][-1]["local_orientation"] = rotation
            scene["instances"][-1]["world_orientation"] = {"$type":"Quaternion", "i":cosine*x-sine*y,"j":cosine*y+sine*x,"k":cosine*z+sine*w,"r":cosine*w-sine*z}
        if collision == "box":
            center = [pivot[0]+center[0]*math.cos(angle)-center[1]*math.sin(angle),
                      pivot[1]+center[0]*math.sin(angle)+center[1]*math.cos(angle),pivot[2]+center[2]]
            scene["solids"].append({"id": "module:" + module["id"], "role": "module_blocker", "center": center,
                "size": [b-a for a,b in zip(low,high)], "yaw": yaw, "world_center": world_point(center, layout["origin"]),
                "world_yaw": yaw + layout["origin"]["yaw"], "level": level, "edge": None})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("plan", "measure", "preview", "catalog"))
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if args.action == "plan":
        print(json.dumps({"meshes": len(write_manifests()), "cache": str(CACHE)}))
    elif args.action == "catalog":
        result = build_catalog()
        print(json.dumps({"families": len(result["families"]), "counts": result["counts"]}))
    else:
        prepare(args.action, threads=args.threads, resume=args.resume)


if __name__ == "__main__":
    main()
