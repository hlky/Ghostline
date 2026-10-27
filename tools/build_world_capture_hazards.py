"""Rebuild reviewed exclusions from serialized native lethal-area geometry."""

from __future__ import annotations

import base64
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import struct
import subprocess

from world_locations.extract import _items, _area_outline
from world_locations.model import Quaternion, Vec3, stable_id, unwrap


def build(root: Path) -> dict:
    paths = subprocess.check_output(
        ["rg", "-l", "gameKillTriggerNode|q000_nomad_tr_border_crossing_loc_area_", str(root), "-g", "*.json"],
        text=True,
    ).splitlines()
    rules = []
    for filename in sorted(paths):
        path = Path(filename)
        nodes = {}
        for index, node in enumerate(_items(path, "Data.RootChunk.nodes.item")):
            data = node.get("Data", node)
            name = str(unwrap(data.get("debugName")) or "")
            border = "q000_nomad_tr_border_crossing_loc_area_" in name.lower()
            if data.get("$type") == "gameKillTriggerNode" or border:
                outline = _area_outline(data)
                raw = base64.b64decode(unwrap(data["outline"]["Data"]["buffer"]), validate=True)
                count = struct.unpack_from("<I", raw)[0]
                if not outline or len(raw) != 8 + count*16:
                    raise ValueError(f"Unsupported lethal-area shape: {path}:{index}")
                height = struct.unpack_from("<f", raw, 4+count*16)[0]
                nodes[index] = (data, outline, height, border)
        for instance in _items(path, "Data.RootChunk.nodeData.Data.item"):
            index = int(unwrap(instance["NodeIndex"]))
            if index not in nodes:
                continue
            data, outline, height, border = nodes[index]
            position = Vec3.from_mapping(instance["Position"])
            rotation = Quaternion.from_mapping(instance.get("Orientation"))
            scale = instance.get("Scale", {})
            axes = [float(unwrap(scale.get(axis, 1))) for axis in "XYZ"]
            points = [Vec3(p["x"]*axes[0], p["y"]*axes[1], p["z"]*axes[2]) for p in outline]
            evidence = {"node_type": data["$type"], "debug_name": unwrap(data.get("debugName")),
                        "source_sector": str(path.relative_to(root)).replace("\\", "/"),
                        "node_index": index, "instance_id": str(unwrap(instance.get("Id"))),
                        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            if border:
                world = [position + rotation.rotate(p) for p in points]
                rule = {"id": "border_crossing", "type": "polygon", "margin_m": 25,
                        "outline": [[p.x, p.y] for p in world],
                        "reason": "Border Crossing excluded after live capture encountered hostile border behavior"}
            else:
                rule = {"id": stable_id("kill_volume", evidence["source_sector"], index, evidence["instance_id"]),
                        "type": "prism", "margin_m": 5,
                        "origin": position.as_dict(), "rotation": asdict(rotation),
                        "outline": [[p.x, p.y] for p in points],
                        "min_z": min(p.z for p in points) + min(0, height*axes[2]),
                        "max_z": max(p.z for p in points) + max(0, height*axes[2]),
                        "reason": "Native gameKillTriggerNode lethal volume, with 5 m safety clearance"}
            rules.append({**rule, "evidence": evidence})
    if not any(rule["id"] == "border_crossing" for rule in rules):
        raise ValueError("No authored Border Crossing location volume found")
    border_count = 0
    for rule in rules:
        if rule["id"] == "border_crossing":
            border_count += 1
            if border_count > 1:
                rule["id"] = stable_id("border_crossing", rule["evidence"])
    return {"hazard_rule_version": "1.0.0", "hazard_rules": rules}


if __name__ == "__main__":
    root = Path("converted/world-location-database/full-world/serialized-sectors")
    result = build(root)
    from world_locations.hazards import validate_hazard_rules
    validate_hazard_rules(result)
    output = Path("tools/world-location-hazard-exclusions-v1.json")
    output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "rules": len(result["hazard_rules"])}))
