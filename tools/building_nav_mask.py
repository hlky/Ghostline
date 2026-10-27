"""Preserve a vanilla Human resource while disabling ground inside a shell.

Only the two polygon flag bytes can change. Tiles, topology, off-mesh data,
metadata and every polygon crossing the shell boundary remain intact.
"""
from __future__ import annotations

import base64
import copy
import hashlib
import json
import math
import struct

from shapely.geometry import Polygon

from world_location_nav import decode_vnav_buffer, load_navigation_sector, vand_position_to_world


def mask_resource(resource, origin, outline, height_range):
    from building_builder import world_point
    if not isinstance(outline, list) or not 3 <= len(outline) <= 64 or any(
            not isinstance(p, list) or len(p) != 2 or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or abs(v) > 100 for v in p) for p in outline):
        raise ValueError("Navigation mask needs 3..64 finite local XY points")
    if not isinstance(height_range, list) or len(height_range) != 2 or any(
            isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or abs(v) > 20 for v in height_range) or height_range[0] >= height_range[1]:
        raise ValueError("Navigation mask needs increasing local height limits in -20..20 m")
    polygon = Polygon([world_point([*p, 0], origin)[:2] for p in outline]).buffer(.025)
    if not polygon.is_valid or polygon.area <= 0:
        raise ValueError("Navigation mask needs a valid shell footprint")
    result, changes = copy.deepcopy(resource), []
    if resource.get("agentSize") != "Human":
        raise ValueError("Only Human terrain navigation may be masked")
    decoded = load_navigation_sector({"Data": {"RootChunk": resource}})
    bounds = []
    for tile in decoded.buffers:
        index = tile.source.buffer_index
        original = base64.b64decode(resource["tileBuffers"][index]["Bytes"])
        raw = bytearray(original)
        disabled = []
        for face in tile.faces:
            offset = 100 + tile.header.vertex_count * 12 + face.index * 20
            if raw[offset + 18] != 3:
                continue  # Preserve special/off-mesh polygons verbatim.
            points = [vand_position_to_world(v) for v in tile.face_vertices(face)]
            bounds.extend([[v.x, v.y, v.z] for v in points])
            if any(not origin["z"] + height_range[0] <= v.z <= origin["z"] + height_range[1] for v in points):
                continue
            shape = Polygon([(v.x, v.y) for v in points])
            if polygon.covers(shape) and struct.unpack_from("<H", raw, offset + 16)[0]:
                struct.pack_into("<H", raw, offset + 16, 0)
                disabled.append(face.index)
        decode_vnav_buffer(raw)  # Validate the unchanged native layout.
        result["tileBuffers"][index]["Bytes"] = base64.b64encode(raw).decode()
        allowed = {100 + tile.header.vertex_count * 12 + face * 20 + byte for face in disabled for byte in (16, 17)}
        if len(raw) != len(original) or any(i not in allowed for i, (a, b) in enumerate(zip(raw, original)) if a != b):
            raise ValueError("Navigation mask changed bytes outside polygon flags")
        if disabled:
            changes.append({"buffer": index, "polygons": disabled, "before_sha256": hashlib.sha256(original).hexdigest(),
                            "after_sha256": hashlib.sha256(raw).hexdigest()})
    if not changes:
        raise ValueError("Navigation mask did not select any terrain polygons")
    return result, changes, [[min(p[a] for p in bounds) for a in range(3)], [max(p[a] for p in bounds) for a in range(3)]]


def build_mask_document(scene, output):
    from building_builder import ROOT
    from generate_world import resource_path, cname, streaming_sector
    settings = scene["layout"]["navigation"].get("terrain_mask")
    if not settings:
        return None
    source = (ROOT / settings["source"]).resolve()
    if not source.is_relative_to(ROOT) or hashlib.sha256(source.read_bytes()).hexdigest() != settings["sha256"]:
        raise ValueError("Terrain navigation source changed; survey it again")
    document = json.loads(source.read_bytes())
    embedded = document["Data"]["EmbeddedFiles"][settings["resource_index"]]
    resource, changes, bounds = mask_resource(embedded["Content"], scene["layout"]["origin"], settings["outline"], settings["height_range"])
    root = document["Data"]["RootChunk"]
    placement = copy.deepcopy(root["nodeData"]["Data"][settings["placement_index"]])
    node = root["nodes"][placement["NodeIndex"]]["Data"]
    original_path = embedded["FileName"]["$value"]
    if node["$type"] != "worldNavigationNode" or node["navigationTileResource"]["DepotPath"]["$value"] != original_path:
        raise ValueError("Terrain resource does not belong to the selected navigation node")
    if not any(p["path"] == settings["sector"] and any(n["index"] == settings["placement_index"] and n["type"] == "worldNavigationNode" for n in p["nodeDeletions"]) for p in scene["retrofit_patches"]):
        raise ValueError("Terrain replacement must remove its original navigation node")
    name = scene["layout"]["id"] + "_retained_navigation.streamingsector"
    depot = "mod\\building_lab\\" + name.removesuffix(".streamingsector") + ".navmesh"
    node = {"HandleId": "0", "Data": {"$type": "worldNavigationNode", "debugName": cname("retained_human_navigation"),
            "navigationTileResource": {**resource_path(depot), "Flags": "Embedded"}}}
    placement["NodeIndex"] = 0
    sector = streaming_sector("Navigation", 3, output / "source/archive/mod/building_lab" / name, [placement], [], [node])
    sector["Data"]["RootChunk"]["cookingPlatform"] = "PLATFORM_PC"
    sector["Data"]["RootChunk"]["localInplaceResource"] = [{**resource_path(depot), "Flags": "Embedded"}]
    sector["Data"]["EmbeddedFiles"] = [{"FileName": resource_path(depot)["DepotPath"], "Content": resource}]
    return {"name": name, "document": sector, "bounds": bounds, "changes": changes,
            "original_resource": original_path, "preserved_buffers": len(resource["tileBuffers"])}
