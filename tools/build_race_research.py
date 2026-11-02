"""Build a focused race research evidence pack; never modifies game resources.

Graph inputs are the checked all-quest corpus. Optional world/entity inputs are
the scratch exports described in docs/reference/vanilla-quests/deep-dives/races.md.
"""
from __future__ import annotations

import argparse
import copy
import gzip
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "reference/quests/deep-dives/all-quests/evidence"
SELECTION = {
    "base-mq056": {
        "mq056_01_citycenter.questphase": {
            "0": [30], "566": [4, 5, 8, 9],
            "1017": [6, 8, 14, 36, 41],
            "1268": [3, 4, 6, 7, 8, 12, 13, 15, 16],
            "1442": [2, 3, 4, 7, 8, 10],
            "1510": [157, 161, 162, 165, 166, 176],
            "2428": [4, 5, 6, 7, 8, 64], "2773": [2, 3, 4, 5, 6],
            "2917": [3, 8, 13, 14, 19], "3416": [3],
            "3915": [3], "4414": [3], "4908": [2],
            "5078": [3, 58, 86, 90, 118, 119, 124, 126, 128],
            "7262": [7, 17, 18, 21],
        },
        "mq056_01_city_race.scene": {"scene": [20, 22, 24, 30, 32, 38]},
    },
    "base-sq024": {
        "sq024_02_pacifica_race.questphase": {"901": [28, 32]},
        "sq024_03_badlands_race.questphase": {"1070": [28, 32]},
    },
}
WORLD_NAMES = [
    "quest_5aab979acf00452f.streamingsector",
    "quest_47de76de8df02b3e.streamingsector",
    "quest_0e2c89ba4e7e003c.streamingsector",
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk(value, pointer=""):
    if isinstance(value, dict):
        yield pointer, value
        for key, child in value.items():
            escaped = key.replace("~", "~0").replace("/", "~1")
            yield from walk(child, f"{pointer}/{escaped}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{pointer}/{index}")


def build(scratch):
    result = {"schema_version": 1, "status": "static research, no runtime proof",
              "corpus_sources": [], "resources": [], "world": [], "entity": []}
    for family, resources in SELECTION.items():
        source = CORPUS / f"{family}.json.gz"
        result["corpus_sources"].append({"path": source.relative_to(ROOT).as_posix(),
                                         "sha256": digest(source)})
        corpus = json.loads(gzip.decompress(source.read_bytes()))["resources"]
        for basename, selections in resources.items():
            resource, = [r for r in corpus if r["depot"].split("\\")[-1] == basename]
            out = {k: resource[k] for k in ["depot", "binary_sha256", "raw_sha256"]}
            out["graphs"] = []
            for graph, ids in selections.items():
                g = resource if graph == "scene" else next(
                    g for g in resource["graphs"] if g["handle"] == graph)
                nodes = [n for n in g["nodes"] if (
                    n["data"].get("nodeId", {}).get("id") if graph == "scene"
                    else n["data"].get("id")) in ids]
                if len(nodes) != len(ids):
                    raise ValueError(f"Missing selected node: {basename} / {graph}")
                selected = {str(i) for i in ids}
                edges = [e for e in g["edges"] if (
                    e.get("source_node", e.get("from")) in selected or
                    e.get("destination_node", e.get("to")) in selected)]
                out["graphs"].append({"graph": graph, "nodes": nodes,
                                       "incident_edges": edges})
            result["resources"].append(out)
    block = scratch / "all.streamingblock.json"
    if block.exists():
        root = json.loads(block.read_text(encoding="utf-8"))["Data"]["RootChunk"]
        result["world_block"] = {"raw_sha256": digest(block), "descriptors": [
            {"pointer": f"/Data/RootChunk/descriptors/{i}", "data": d}
            for i, d in enumerate(root["descriptors"])
            if d["data"]["DepotPath"].get("$value", "").split("\\")[-1] in WORLD_NAMES]}
    for name in WORLD_NAMES:
        source = scratch / f"{name}.json"
        if not source.exists():
            continue
        root = json.loads(source.read_text(encoding="utf-8"))["Data"]["RootChunk"]
        binary = scratch / "cr2w/base/worlds/03_night_city/_compiled/default" / name
        out = {"depot": "base\\worlds\\03_night_city\\_compiled\\default\\" + name,
               "raw_sha256": digest(source), "binary_sha256": digest(binary),
               "node_count": len(root["nodes"]), "node_refs": root["nodeRefs"],
               "nodes": []}
        for i, node in enumerate(root["nodes"]):
            data = copy.deepcopy(node["Data"])
            if "Spline" not in data["$type"] and data["$type"] != "worldTriggerAreaNode":
                continue
            spline = data.get("splineData", {}).get("Data", {})
            if "points" in spline:
                points = spline.pop("points")
                spline["research_point_count"] = len(points)
                spline["research_points_sha256"] = hashlib.sha256(
                    json.dumps(points, sort_keys=True).encode()).hexdigest()
            out["nodes"].append({"pointer": f"/Data/RootChunk/nodes/{i}", "data": data,
                                 "placements": [p for p in root["nodeData"]["Data"]
                                                if p["NodeIndex"] == i]})
        result["world"].append(out)
    entity = scratch / "wkit/mq056_checkpoint_marker.ent.json"
    if entity.exists():
        value = json.loads(entity.read_text(encoding="utf-8"))
        types = {"FactsDeviceOperation", "ToggleComponentsDeviceOperation",
                 "TriggerVolumeOperationTriggerData", "RaceCheckpointSelector"}
        result["entity"] = [
            {"pointer": p, "data": d} for p, d in walk(value) if d.get("$type") in types]
        binary = scratch / "cr2w/base/quest/minor_quests/mq056/entities/mq056_checkpoint_marker.ent"
        result["entity_source"] = {"depot": "base\\quest\\minor_quests\\mq056\\entities\\mq056_checkpoint_marker.ent",
                                    "raw_sha256": digest(entity),
                                    "binary_sha256": digest(binary), "serializer": "WolvenKit 8.17.4"}
    scripts = scratch / "final.reds"
    if scripts.exists():
        anchors = ["class hudCarRaceController", "class RacingSystem",
                   "sq024_current_race_checkpoint_fact_add", "sq024_current_race_player_position",
                   "func ToggleRaceClock", "func CleanUpRace", "class FactsDeviceOperation",
                   "class TriggerVolumeOperationsTrigger"]
        result["script_source"] = {"decompiled_sha256": digest(scripts),
                                   "anchors": [{"line": i, "text": line.strip()}
                                               for i, line in enumerate(scripts.read_text(encoding="utf-8").splitlines(), 1)
                                               if any(a in line for a in anchors)]}
        provenance = scratch / "script-provenance.json"
        if provenance.exists():
            result["script_source"]["provenance"] = json.loads(provenance.read_text(encoding="utf-8"))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scratch", type=Path, default=ROOT / ".tmp/race-research")
    parser.add_argument("--output", type=Path, default=ROOT / "reference/quests/races/evidence.json")
    args = parser.parse_args()
    result = build(args.scratch)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(result['resources'])} graph resources, {len(result['world'])} world sectors, "
          f"{len(result['entity'])} entity excerpts to {args.output}")


if __name__ == "__main__":
    main()
