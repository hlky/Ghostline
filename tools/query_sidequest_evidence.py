"""Query checked compressed quest evidence without unpacking game archives."""

from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path

from build_sidequest_catalogue import describe, edges_at, node_rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("reference/quests/deep-dives/catalogue"))
    parser.add_argument("--quest", help="Exact title or full journal path")
    parser.add_argument("--resource", help="Depot path or unique substring")
    parser.add_argument("--graph", help="Graph handle, e.g. h0, or scene")
    parser.add_argument("--node", help="Graph-local node ID")
    parser.add_argument("--facts", help="Fact-name substring")
    parser.add_argument("--refs", help="Reference-value substring")
    parser.add_argument("--events", action="store_true", help="Read section performance events from the extended corpus")
    parser.add_argument("--event-type", help="Performance event type substring (implies --events)")
    args = parser.parse_args()
    items = json.loads((args.root / "resources.json").read_text(encoding="utf-8"))["resources"]
    if args.quest:
        quests = json.loads((args.root / "catalogue.json").read_text(encoding="utf-8"))["quests"]
        matches = [q for q in quests if args.quest.casefold() in {q["title"].casefold(), q["journal_path"].casefold()}]
        if len(matches) != 1:
            parser.error("Quest must match one exact title/path; use a journal path for duplicate NO_TITLE entries")
        quest = matches[0]
        scope = set(quest["scope_resources"] + quest.get("parent_context_resources", []))
        items = [item for item in items if item["depot"] in scope]
    if args.resource:
        items = [item for item in items if args.resource.casefold() in item["depot"].casefold()]
    if not items:
        parser.error("No indexed resource matches; consult coverage in catalogue.json")
    if args.events or args.event_type:
        if args.graph not in (None, 'scene'):
            parser.error('Performance events use the scene graph namespace')
        result = []
        for family in sorted({item['family'] for item in items}):
            shard = args.root / 'performances' / (family + '.json.gz')
            if not shard.exists():
                continue
            wanted = {item['depot'] for item in items}
            for record in json.loads(gzip.decompress(shard.read_bytes()))['scenes']:
                if record['depot'] not in wanted:
                    continue
                events = [event for event in record['events'] if
                          (args.node is None or event['node'] == args.node) and
                          (args.event_type is None or args.event_type.casefold() in event['data'].get('$type', '').casefold())]
                if events:
                    result.append({'depot': record['depot'], 'events': events})
        print(json.dumps(result, indent=2, ensure_ascii=True))
        return
    if not (args.graph or args.node or args.facts or args.refs):
        print(json.dumps(items, indent=2, ensure_ascii=True))
        return
    if args.node and not args.graph:
        parser.error("--node requires --graph because IDs repeat across embedded graphs")
    families = sorted({item["family"] for item in items})
    wanted = {item["depot"] for item in items}
    result = []
    for family in families:
        shard = args.root / "evidence" / (family + ".json.gz")
        for record in json.loads(gzip.decompress(shard.read_bytes()))["resources"]:
            if record["depot"] not in wanted:
                continue
            row = {"depot": record["depot"], "binary_sha256": record["binary_sha256"]}
            if args.facts is not None:
                row["fact_uses"] = [f for f in record["fact_uses"] if args.facts.casefold() in str(f["data"].get("factName", "")).casefold()]
            if args.refs is not None:
                row["references"] = [r for r in record["references"] if args.refs.casefold() in str(r["value"]).casefold()]
            if args.graph:
                selected = [(scope, nid, node, edges) for scope, nid, node, edges in node_rows(record) if scope == args.graph and (args.node is None or nid == args.node)]
                row["nodes"] = [{"graph": scope, "node": nid, "pointer": node["pointer"],
                                  "operation": describe(node["data"]),
                                  **({"data": node["data"]} if args.node is not None else {}),
                                  "edges": edges_at(scope, nid, edges)} for scope, nid, node, edges in selected]
            if any(row.get(key) for key in ("fact_uses", "references", "nodes")):
                result.append(row)
    print(json.dumps(result, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
