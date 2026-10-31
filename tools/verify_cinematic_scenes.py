"""Verify cinematic research inputs, totals and selected raw section bindings."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from analyze_cinematic_scenes import read, sha, write_json


def resolve(document, pointer):
    value = document
    for part in pointer.split("/")[1:]:
        key = part.replace("~1", "/").replace("~0", "~")
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def rid_binding(root, data):
    kind = data["$type"]
    if kind == "scnPlayRidAnimEvent":
        table, field = "ridAnimations", "animResRefId"
    elif kind == "scneventsPlayRidCameraAnimEvent":
        table, field = "ridCameraAnimations", "animSRRefId"
    else:
        return None
    index = data[field]["id"]
    ref = root["resouresReferences"][table][index]
    resource_id = ref["resourceId"]["id"]
    handlers = [r for r in root["ridResources"] if r["id"]["id"] == resource_id]
    assert len(handlers) == 1
    return {"table": table, "index": index, "resource_id": resource_id,
        "serial_number": ref["animationSN"]["serialNumber"],
        "depot": handlers[0]["ridResource"]["DepotPath"]["$value"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("reference/quests/deep-dives/cinematic-scenes"))
    parser.add_argument("--raw-root", type=Path, default=Path(".tmp/quest-deep-dives/universal/raw"))
    parser.add_argument("--docs", type=Path, default=Path("docs/reference/vanilla-quests/deep-dives/cinematic-scenes"))
    args = parser.parse_args()
    frozen = read(args.data / "verification.json")
    for path, expected in frozen["inputs"].items():
        assert sha(Path(path)) == expected, f"Input changed: {path}"
    assert sha(args.data / "analysis.json.gz") == frozen["analysis_sha256"]
    assert sha(args.data / "case-evidence.json.gz") == frozen["case_evidence_sha256"]
    study = read(args.data / "analysis.json.gz")
    cases = read(args.data / "case-evidence.json.gz")
    scenes = study["scenes"]
    totals = Counter()
    for s in scenes.values():
        totals.update(s["event_types"])
        assert sum(s["event_types"].values()) == s["events"]
    assert dict(totals) == study["aggregate"]["event_types"]
    assert len({q["journal_path"] for q in study["quests"]}) == study["aggregate"]["journal_entries"]
    for q in study["quests"]:
        assert (args.docs / "quests" / q["document"]).is_file()
        assert set(q["scenes"]).isdisjoint(q["parent_context_scenes"])
        assert q["events"] == sum(scenes[d]["events"] for d in q["scenes"])
    # This validates source identity and section/event pointers, not engine execution.
    bindings, checked_events = {}, 0
    for depot, case in cases.items():
        path = args.raw_root / (depot.replace("\\", "/") + ".json")
        assert sha(path) == case["raw_sha256"]
        raw = read(path)
        root = raw["Data"]["RootChunk"]
        section = resolve(raw, case["section"]["pointer"])["Data"]
        assert str(section["nodeId"]["id"]) == case["node"]
        assert len(section["events"]) == len(case["events"])
        rows = []
        for event in case["events"]:
            data = resolve(raw, event["pointer"])["Data"]
            assert data["$type"] == event["data"]["$type"]
            assert data.get("id") == event["data"].get("id")
            for key in ("startTime", "duration", "performer", "animResRefId", "animSRRefId"):
                assert data.get(key) == event["data"].get(key)
                assert (key in data) == (key in event["data"])
            binding = rid_binding(root, data)
            if binding:
                rows.append({"handle": event["handle"], "pointer": event["pointer"], **binding})
            checked_events += 1
        bindings[depot] = {"section": case["node"], "raw_sha256": case["raw_sha256"], "rid_bindings": rows}
    context = []
    selected_context = {
        "mq010_02_barry_talk.questphase": {"9", "22"},
        "q306_05_launchpad.questphase": {"10", "41"},
        "q306_10_finale.scene": {"5551"},
    }
    for family in ("base-mq010", "ep1-q306"):
        path = next(Path(p) for p in frozen["inputs"] if p.endswith(f"/evidence/{family}.json.gz"))
        for record in read(path)["resources"]:
            name = record["depot"].rsplit("\\", 1)[-1]
            if name not in selected_context:
                continue
            wanted = selected_context[name]
            raw_path = args.raw_root / (record["depot"].replace("\\", "/") + ".json")
            assert sha(raw_path) == record["raw_sha256"]
            raw = read(raw_path)
            scopes = record.get("graphs", [{"handle": "scene", "nodes": record.get("nodes", []), "edges": record.get("edges", [])}])
            for scope in scopes:
                if str(scope["handle"]) not in ("0", "scene"):
                    continue
                nodes = [n for n in scope["nodes"] if str(n["data"].get("id", n["data"].get("nodeId", {}).get("id"))) in wanted]
                if not nodes:
                    continue
                for node in nodes:
                    assert resolve(raw, node["pointer"])["Data"]["$type"] == node["data"]["$type"]
                edges = [e for e in scope["edges"] if
                    str(e.get("from", e.get("source_node"))) in wanted or
                    str(e.get("to", e.get("destination_node"))) in wanted]
                context.append({"depot": record["depot"], "raw_sha256": record["raw_sha256"],
                    "graph": str(scope["handle"]), "nodes": nodes, "edges": edges})
    assert sum(len(r["nodes"]) for r in context) == 5
    write_json(args.data / "caller-evidence.json", context)
    write_json(args.data / "raw-case-verification.json", {
        "verifier_sha256": sha(Path(__file__)), "case_evidence_sha256": frozen["case_evidence_sha256"],
        "input_hashes_checked": len(frozen["inputs"]), "raw_scenes_checked": len(cases),
        "raw_section_events_checked": checked_events, "cases": bindings,
        "raw_caller_or_gate_nodes_checked": 5, "caller_evidence_sha256": sha(args.data / "caller-evidence.json"),
        "limits": "RID table bindings checked; RID payload, runtime reachability and playback not validated."})
    print(f"Verified {len(study['quests'])} quest dossiers, {len(scenes)} scenes, "
          f"{sum(totals.values())} events; raw checks: {len(cases)} sections / {checked_events} events.")


if __name__ == "__main__":
    main()
