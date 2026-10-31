"""Verify corpus coverage, source identities, graph topology and dossier links."""

from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import re


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def resolve(document, pointer):
    value = document
    for part in pointer.split("/")[1:]:
        key = part.replace("~1", "/").replace("~0", "~")
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("reference/quests/deep-dives/catalogue"))
    parser.add_argument("--docs", type=Path, default=Path("docs/reference/vanilla-quests/deep-dives"))
    parser.add_argument("--raw-root", type=Path)
    parser.add_argument("--binary-root", type=Path)
    parser.add_argument("--dossier-subdir", default="catalogue")
    args = parser.parse_args()
    journal = load(args.data / "journal-input.json")["quests"]
    catalogue = load(args.data / "catalogue.json")["quests"]
    quests = {q["journal_path"]: q for q in catalogue}
    assert len(quests) == len(catalogue) == len(journal), "Duplicate/missing quest"
    assert set(quests) == {q["path"] for q in journal}, "Journal coverage mismatch"
    selection = {r["depot"]: r for r in load(args.data / "source-selection.json")["resources"]}
    metadata = {r["depot"]: r for r in load(args.data / "resources.json")["resources"]}
    assert set(selection) == set(metadata), "Resource selection mismatch"
    assert not load(args.data / "resources.json")["index_failures"], "Unresolved index failure"
    resources, pointers, graphs, scene_nodes = set(), 0, 0, 0
    for shard in load(args.data / "evidence-manifest.json")["shards"]:
        path = Path(shard["path"])
        assert sha(path) == shard["sha256"], f"Shard hash mismatch: {path}"
        records = json.loads(gzip.decompress(path.read_bytes()))["resources"]
        assert len(records) == shard["resources"]
        for record in records:
            depot = record["depot"]
            assert depot not in resources, f"Duplicate depot: {depot}"
            resources.add(depot)
            for key in ("binary_sha256", "raw_sha256"):
                assert record[key] == selection[depot][key] == metadata[depot][key]
            raw = None
            if args.raw_root:
                source = args.raw_root / (depot.replace("\\", "/") + ".json")
                assert sha(source) == record["raw_sha256"]
                raw = load(source)
            if args.binary_root:
                assert sha(args.binary_root / depot.replace("\\", "/")) == record["binary_sha256"]
            for graph in record.get("graphs", []):
                graphs += 1
                ids = [str(n["data"].get("id", "")) for n in graph["nodes"]]
                assert len(ids) == len(set(ids))
                assert all(e["from"] in ids and e["to"] in ids for e in graph["edges"])
                for node in graph["nodes"]:
                    if raw is not None:
                        assert resolve(raw, node["pointer"])["Data"]["id"] == node["data"]["id"]
                    pointers += 1
            ids = {str(n["data"]["nodeId"]["id"]) for n in record.get("nodes", [])}
            assert all(e["source_node"] in ids and e["destination_node"] in ids for e in record.get("edges", []))
            for node in record.get("nodes", []):
                if raw is not None:
                    assert resolve(raw, node["pointer"])["Data"]["nodeId"] == node["data"]["nodeId"]
                pointers += 1
                scene_nodes += 1
            if raw is not None:
                for ref in record["references"]:
                    resolve(raw, ref["pointer"])
                for fact in record["fact_uses"]:
                    assert resolve(raw, fact["pointer"]) == fact["data"]
        if len(resources) % 200 < len(records):
            print(f"Verified {len(resources)}/{len(selection)} resources", flush=True)
    assert resources == set(selection)
    performance_scenes, performance_events = 0, 0
    performance_manifest = args.data / 'performance-manifest.json'
    if performance_manifest.exists():
        for shard in load(performance_manifest)['shards']:
            path = Path(shard['path'])
            assert sha(path) == shard['sha256'], f'Performance shard changed: {path}'
            records = json.loads(gzip.decompress(path.read_bytes()))['scenes']
            assert len(records) == shard['scenes']
            assert sum(len(r['events']) for r in records) == shard['events']
            for record in records:
                depot = record['depot']
                assert record['raw_sha256'] == selection[depot]['raw_sha256']
                assert record['binary_sha256'] == selection[depot]['binary_sha256']
                raw = load(args.raw_root / (depot.replace('\\', '/') + '.json')) if args.raw_root else None
                for event in record['events']:
                    if raw is not None:
                        source = resolve(raw, event['pointer'])['Data']
                        assert source['$type'] == event['data']['$type']
                        for key in ('startTime', 'duration', 'executionTagFlags'):
                            assert source.get(key) == event['data'].get(key)
                    performance_events += 1
                performance_scenes += 1
    for quest in catalogue:
        assert (args.docs / args.dossier_subdir / quest["document"]).is_file()
        assert set(quest["scope_resources"] + quest.get("parent_context_resources", [])) <= resources
        if quest["status"] == "unresolved attribution":
            assert not quest["anchor_nodes"] and not quest["block_candidates"]
    # Regression checks for mechanisms that an objective-only inventory misses.
    skippy = next(q for q in catalogue if q["title"] == "Machine Gun")
    assert any("mq007.questphase / h606 / 70" in p for p in skippy["block_candidates"]["conditional_route"]), "Embedded milestone graph dropped"
    assert load(args.data / "block-occurrences.json").get("braindance"), "Rewindable scene sections omitted"
    if args.dossier_subdir == 'all-quests':
        japan = next(q for q in catalogue if q['title'] == 'Big in Japan')
        assert not any(d.endswith('additional_game_elements.questphase') for d in japan['scope_resources']), 'Root launch scaffolding imported into production flow'
        ending = next(q for q in catalogue if q['title'] == 'Who Wants to Live Forever')
        assert ending.get('anchor_node_selection'), 'Shared master lost its node-level scope boundary'
        assert not any('\\q003\\' in d for d in ending['scope_resources']), 'Unrelated Pickup family imported through shared master'
    links = 0
    for path in args.docs.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            assert (path.parent / target.split("#")[0]).resolve().exists(), f"Broken link: {path}: {target}"
            links += 1
    provenance = args.data / "provenance.json"
    if provenance.exists():
        for item in load(provenance).get("artifacts", []) + load(provenance).get("tools", []):
            assert sha(item["path"]) == item["sha256"], f"Provenance hash changed: {item['path']}"
    print(json.dumps({"status": "passed", "quests": len(catalogue), "coverage": dict(Counter(q["status"] for q in catalogue)),
                      "resources": len(resources), "phase_graphs": graphs, "phase_nodes": pointers-scene_nodes,
                      "scene_nodes": scene_nodes, "node_pointers": pointers, "local_links": links,
                      "performance_scenes": performance_scenes, "performance_event_pointers": performance_events,
                      "raw_source_pointers_rechecked": args.raw_root is not None,
                      "binary_hashes_rechecked": args.binary_root is not None}))


if __name__ == "__main__":
    main()
