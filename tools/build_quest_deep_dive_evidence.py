"""Index extracted vanilla quests using the existing graph explorers.

Research output only: omitted RED defaults are not inferred, embedded graphs
have separate namespaces, and historical scene versions remain identified.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path

from explore_questphase import QuestphaseExplorer
from explore_scene import SceneExplorer


def pointer(parts):
    if parts and parts[0] == "$":
        parts = parts[1:]
    return "/" + "/".join(str(p).replace("~", "~0").replace("/", "~1") for p in parts)


def walk(value, path=()):
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, path + (index,))


def compact(value, explorer, seen=frozenset()):
    """Resolve handles but keep nested graphs separate and events in aggregates."""
    if isinstance(value, list):
        return [compact(child, explorer, seen) for child in value]
    if not isinstance(value, dict):
        return value
    if "$value" in value:
        return value["$value"]
    if "HandleRefId" in value:
        handle = str(value["HandleRefId"])
        if handle in seen or handle not in explorer.handle_map:
            return {"handle_ref": handle}
        return compact(explorer.handle_map[handle], explorer, seen | {handle})
    if "HandleId" in value:
        return compact(value.get("Data", {}), explorer, seen | {str(value["HandleId"])})
    return {
        key: compact(child, explorer, seen)
        for key, child in value.items()
        if key not in {"sockets", "phaseGraph", "outputSockets", "events"}
    }


def phase_graphs(explorer):
    graphs = []
    original = explorer.data
    for handle, wrapper in explorer.handle_map.items():
        data = wrapper.get("Data", {})
        if data.get("$type") != "questGraphDefinition":
            continue
        explorer.data = {"Data": {"RootChunk": {"graph": {"Data": data}}}}
        explorer.nodes_by_handle = {}
        explorer.node_data_by_handle = {}
        explorer.socket_info_by_handle = {}
        explorer.edges_by_handle = {}
        explorer._index_nodes()
        explorer._index_edges()
        nodes = []
        for node_handle, node in explorer.node_data_by_handle.items():
            nodes.append({"handle": node_handle,
                          "pointer": pointer(explorer.handle_paths[node_handle]),
                          "sockets": [{"name": explorer.socket_info_by_handle[s].name,
                                       "type": explorer.socket_info_by_handle[s].type}
                                      for s in explorer.nodes_by_handle[node_handle].socket_handles
                                      if s in explorer.socket_info_by_handle],
                          "data": compact(node, explorer)})
        edges = []
        for edge in explorer.edges_by_handle.values():
            if edge.source_node not in explorer.nodes_by_handle or edge.destination_node not in explorer.nodes_by_handle:
                raise ValueError(f"Unresolved graph endpoint in {explorer.path}: {edge}")
            edges.append({"from": explorer.nodes_by_handle[edge.source_node].quest_id,
                          "output": edge.source_socket_name,
                          "to": explorer.nodes_by_handle[edge.destination_node].quest_id,
                          "input": edge.destination_socket_name})
        graphs.append({"handle": handle, "pointer": pointer(explorer.handle_paths[handle]),
                       "nodes": nodes, "edges": edges})
    explorer.data = original
    return graphs


def resource_record(raw, raw_root, binary_root):
    relative = raw.relative_to(raw_root).as_posix()
    depot = relative.removesuffix(".json").replace("/", "\\")
    binary = binary_root / relative.removesuffix(".json")
    document = json.loads(raw.read_text(encoding="utf-8-sig"))
    record = {"depot": depot, "historical_version": "/versions/" in relative,
              "binary_sha256": hashlib.sha256(binary.read_bytes()).hexdigest(),
              "raw_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
              "references": [], "fact_uses": []}
    if record["historical_version"]:
        record["analysis"] = "Identity only; historical versions are not merged into the current graph."
        return record
    for path, value in walk(document):
        if not isinstance(value, dict):
            continue
        kind = value.get("$type")
        if kind in {"ResourcePath", "NodeRef", "TweakDBID"} and value.get("$value") not in (None, "", "0"):
            record["references"].append({"kind": kind, "value": value["$value"], "pointer": pointer(path)})
        if "realPath" in value:
            record["references"].append({"kind": "journal", "value": value["realPath"], "pointer": pointer(path)})
        if "factName" in value:
            record["fact_uses"].append({"pointer": pointer(path), "data": value})
    if raw.name.endswith((".questphase.json", ".quest.json")):
        record["graphs"] = phase_graphs(QuestphaseExplorer(raw))
    elif raw.name.endswith(".scene.json"):
        explorer = SceneExplorer(raw)
        record["actors"] = [asdict(actor) for actor in explorer.actors()]
        record["entry_points"] = compact(explorer.root_chunk.get("entryPoints", []), explorer)
        record["exit_points"] = compact(explorer.root_chunk.get("exitPoints", []), explorer)
        record["notable_points"] = compact(explorer.root_chunk.get("notablePoints", []), explorer)
        record["nodes"] = [{"handle": handle, "pointer": pointer(explorer.handle_paths[handle]),
                            "data": compact(explorer.resolve_data(explorer.handle_map[handle]), explorer)}
                           for handle in explorer.nodes_by_handle]
        record["edges"] = [asdict(edge) for edge in explorer.edges()]
        ids = set(explorer.nodes_by_id)
        if any(edge["source_node"] not in ids or edge["destination_node"] not in ids for edge in record["edges"]):
            raise ValueError(f"Unresolved scene endpoint in {raw}")
        record["event_types"] = {}
        for event in explorer.events():
            key = event.event_type
            record["event_types"][key] = record["event_types"].get(key, 0) + 1
        record["screenplay_line_count"] = len(explorer.screenplay_lines_by_item_id)
        record["screenplay_option_count"] = len(explorer.screenplay_options_by_item_id)
        record["choice_text"] = explorer.loc_payload_by_locstring
        record["line_bindings"] = [asdict(event) for event in explorer.events() if event.screenplay_line_id]
    elif raw.name.endswith(".community.json"):
        record["community"] = compact(document["Data"]["RootChunk"], QuestphaseExplorer(raw))
    elif raw.name.endswith(".gamedef.json"):
        record["launch_definition"] = compact(document["Data"]["RootChunk"], QuestphaseExplorer(raw))
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-root", type=Path, required=True)
    parser.add_argument("--binary-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    records = [resource_record(path, args.raw_root, args.binary_root)
               for path in sorted(args.raw_root.rglob("*.json"))]
    args.out.mkdir(parents=True, exist_ok=True)
    for quest in ("mq003", "mq010"):
        selected = [record for record in records if f"\\{quest}\\" in record["depot"]]
        output = {"schema_version": 1, "quest": quest,
                  "scope": "Extracted local resources; static structure, no runtime proof; RED defaults remain omitted.",
                  "resources": selected}
        (args.out / f"{quest}.evidence.json").write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"{quest}: {len(selected)} resources")


if __name__ == "__main__":
    main()
