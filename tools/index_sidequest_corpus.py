"""Index a serialized quest research corpus into resumable, compressed records.

Uses the pilot's graph explorers; never writes a game/project source tree.
Run before build_sidequest_catalogue.py. Historical versions are not analyzed.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import gzip
import hashlib
import json
from pathlib import Path
import time

from build_quest_deep_dive_evidence import resource_record
from build_sidequest_catalogue import node_rows, values


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def receipt(record, target, status):
    calls = set()
    for _, _, node, _ in node_rows(record):
        core = node['data'].get('questNode', node['data'])
        refs = [v for v in values(core, 'DepotPath') if isinstance(v, str)]
        if core.get('$type') in {'questPhaseNodeDefinition', 'questSceneNodeDefinition'}:
            calls.update(v for v in refs if v.endswith(('.questphase', '.scene', '.quest')))
        calls.update(v for v in refs if v.endswith('.community'))
    return {"depot": record["depot"], "cache": target.name, "status": status,
            "call_resources": sorted(calls),
            "binary_sha256": record["binary_sha256"], "raw_sha256": record["raw_sha256"],
            "journal_paths": sorted({r["value"] for r in record["references"] if r["kind"] == "journal"}),
            "graph_resources": sorted({str(r["value"]) for r in record["references"]
                                       if r["kind"] == "ResourcePath" and str(r["value"]).endswith((".questphase", ".quest", ".gamedef", ".scene", ".community"))}),
            "phase_graphs": len(record.get("graphs", [])),
            "phase_nodes": sum(len(g["nodes"]) for g in record.get("graphs", [])),
            "scene_nodes": len(record.get("nodes", [])),
            "verified_node_pointers": record.get("verification", {}).get("source_node_pointers_checked", 0)}


def index_one(job):
    raw, raw_root, binary_root, cache = map(Path, job)
    relative = raw.relative_to(raw_root).as_posix()
    depot = relative.removesuffix(".json").replace("/", "\\")
    target = cache / (hashlib.sha256(depot.encode()).hexdigest()[:24] + ".json.gz")
    binary = binary_root / relative.removesuffix(".json")
    identity = {"binary_sha256": digest(binary), "raw_sha256": digest(raw)}
    if target.exists():
        previous = json.loads(gzip.decompress(target.read_bytes()))
        if previous.get("index_version") == 2 and all(previous.get(k) == v for k, v in identity.items()):
            return receipt(previous, target, "cached")
    try:
        record = resource_record(raw, raw_root, binary_root)
        document = json.loads(raw.read_text(encoding="utf-8-sig"))
        record["index_version"] = 2
        if raw.name.endswith(".scene.json"):
            record["screenplay_options"] = document["Data"]["RootChunk"].get("screenplayStore", {}).get("options", [])

        def resolve(pointer):
            value = document
            for part in pointer.split("/")[1:]:
                key = part.replace("~1", "/").replace("~0", "~")
                value = value[int(key)] if isinstance(value, list) else value[key]
            return value

        count = 0
        for graph in record.get("graphs", []):
            ids = [str(n["data"].get("id", "")) for n in graph["nodes"]]
            if len(ids) != len(set(ids)):
                raise ValueError(f"Duplicate node ID in graph h{graph['handle']}")
            for node in graph["nodes"]:
                if resolve(node["pointer"])["Data"]["id"] != node["data"]["id"]:
                    raise ValueError("Phase node pointer mismatch")
                count += 1
        for node in record.get("nodes", []):
            if resolve(node["pointer"])["Data"]["nodeId"] != node["data"]["nodeId"]:
                raise ValueError("Scene node pointer mismatch")
            count += 1
        for ref in record["references"]:
            resolve(ref["pointer"])
        for fact in record["fact_uses"]:
            if resolve(fact["pointer"]) != fact["data"]:
                raise ValueError("Fact pointer mismatch")
        record["verification"] = {"source_node_pointers_checked": count,
                                  "graph_endpoints": "resolved",
                                  "reference_and_fact_pointers": "resolved"}
        payload = json.dumps(record, ensure_ascii=False, separators=(",", ":")).encode()
        target.write_bytes(gzip.compress(payload, mtime=0))
        return receipt(record, target, "indexed")
    except Exception as error:
        return {"depot": depot, "status": "failed", "error": f"{type(error).__name__}: {error}"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-root", type=Path, required=True)
    parser.add_argument("--binary-root", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    files = [p for p in sorted(args.raw_root.rglob("*.json"))
             if "versions" not in p.parts and p.name.endswith((".scene.json", ".questphase.json", ".quest.json", ".gamedef.json", ".community.json"))]
    if not files:
        parser.error("No serialized resources found")
    args.cache.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    results = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(index_one, (str(p), str(args.raw_root), str(args.binary_root), str(args.cache))) for p in files]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            if len(results) % 100 == 0 or result["status"] == "failed":
                print(f"{len(results)}/{len(files)} ({time.monotonic()-start:.1f}s) {result.get('error', '')}", flush=True)
    results.sort(key=lambda row: row["depot"])
    (args.cache / "index.json").write_text(json.dumps({"resources": results}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"resources": len(results), "failures": [r for r in results if r["status"] == "failed"]}), flush=True)


if __name__ == "__main__":
    main()
