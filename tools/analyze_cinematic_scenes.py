"""Build a reproducible cinematic study from the frozen all-quest evidence.

Only explicit stored fields are counted. Capabilities overlap; they do not
classify a scene as cinematic or establish runtime reachability.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import gzip
import hashlib
import json
from pathlib import Path


GROUPS = {
    "speech": {"scnDialogLineEvent"},
    "skeletal_animation": {"scnPlaySkAnimEvent"},
    "idle_animation": {"scnChangeIdleAnimEvent", "scnAddIdleAnimEvent"},
    "gaze": {"scnLookAtEvent", "scnLookAtAdvancedEvent", "scneventsPlayerLookAtEvent"},
    "ik": {"scnIKEvent"},
    "rid_actor": {"scnPlayRidAnimEvent"},
    "camera": {"scneventsCameraEvent", "scneventsCameraParamsEvent", "scneventsPlayRidCameraAnimEvent", "scneventsCameraPlacementEvent"},
    "rid_camera": {"scneventsPlayRidCameraAnimEvent"},
    "props_equipment": {"scneventsAttachPropToPerformer", "scneventsAttachPropToWorld",
        "scneventsAttachPropToNode", "scneventsEquipItemToPerformer",
        "scneventsUnequipItemFromPerformer", "scneventsUnequipItemFromPerformerByItem"},
    "audio": {"scnAudioEvent", "scnAudioDurationEvent"},
    "vfx": {"scneventsVFXEvent", "scneventsVFXDurationEvent", "scneventsVFXBraindanceEvent"},
    "gameplay_transition": {"scnGameplayTransitionEvent"},
    "socket_signal": {"scneventsSocket"},
    "clues": {"scneventsClueEvent"},
    "animation_state": {"scneventsSetAnimFeatureEvent", "scneventsSetAnimsetWeight", "scnPoseCorrectionEvent", "scnOverridePhantomParamsEvent"},
    "mount_workspot": {"scnUnmountEvent", "scneventsMountEvent", "scnPlayDefaultMountedSlotWorkspotEvent"},
    "gameplay_action": {"scnGameplayActionEvent", "scneventsRagdollEvent"},
    "entity_lifecycle": {"scneventsSpawnEntityEvent", "scneventsDespawnEntityEvent"},
    "bd_visibility_ui": {"scneventsBraindanceVisibilityEvent", "scneventsUIAnimationBraindanceEvent"},
    "video": {"scnPlayVideoEvent"},
}

# Section IDs are local to the exact depot, not global chronological positions.
CASES = {
    "mq010_02_barry_talk.scene": "265",
    "sq012_02a_braindance.scene": "20",
    "q005_07_vip_apartment.scene": "2000",
    "sq030_09_pier.scene": "2680",
    "q306_10_finale.scene": "5550",
    "q305_07_brain_hack.scene": "3453",
}


def read(path):
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == ".gz" else data)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
    path.write_bytes(gzip.compress(data, mtime=0) if path.suffix == ".gz" else data)


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def nested_types(value):
    if isinstance(value, dict):
        if "$type" in value:
            yield value["$type"]
        for child in value.values():
            yield from nested_types(child)
    elif isinstance(value, list):
        for child in value:
            yield from nested_types(child)


def metrics(record):
    types = Counter(e["data"].get("$type", "unknown") for e in record["events"])
    sections = defaultdict(Counter)
    examples = {}
    explicit_fields = Counter()
    components = Counter()
    scaling = Counter()
    for event in record["events"]:
        data = event["data"]
        sections[event["node"]][data["$type"]] += 1
        examples.setdefault(data["$type"], {k: event[k] for k in ("node", "handle", "pointer")})
        for key in ("startTime", "duration", "performer", "scalingData", "FPPControlActive"):
            if key in data:
                explicit_fields[key] += 1
        if "actorComponent" in data:
            components[data["actorComponent"]] += 1
        if isinstance(data.get("scalingData"), dict):
            scaling[data["scalingData"].get("$type", "unknown")] += 1
    return {
        "raw_sha256": record["raw_sha256"], "binary_sha256": record["binary_sha256"],
        "events": sum(types.values()), "event_sections": len(sections),
        "event_types": dict(sorted(types.items())),
        "capabilities": {name: sum(types[t] for t in names) for name, names in GROUPS.items()},
        "section_capabilities": {node: [name for name, names in GROUPS.items()
            if any(counts[t] for t in names)] for node, counts in sections.items()},
        "explicit_event_fields": dict(explicit_fields), "actor_components": dict(components),
        "scaling_types": dict(scaling), "screenplay_lines": len(record["screenplay_lines"]),
        "interruption_scenarios": record["interruption_scenarios"], "event_examples": examples,
    }


def project_inventory(source):
    from explore_scene import SceneExplorer

    rows = []
    # Resolve only registered project source trees; generated previews are excluded.
    catalog_path = Path("projects/catalog.json")
    for project, directory in source(catalog_path)["projects"].items():
        for path in sorted((Path(directory) / "source/raw").rglob("*.scene.json")):
            source(path)
            explorer = SceneExplorer(path)
            counts = Counter()
            for node in explorer.graph_nodes:
                data = explorer.resolve_data(node)
                if not isinstance(data, dict):
                    continue
                for handle in data.get("events", []):
                    event = explorer.resolve_data(handle)
                    if isinstance(event, dict):
                        counts[event.get("$type", "unknown")] += 1
            rows.append({"project": project, "path": path.as_posix(), "raw_sha256": sha(path),
                "event_types": dict(counts), "events": sum(counts.values())})
    return rows


def build(args):
    inputs = {}

    def source(path):
        inputs[path.as_posix()] = sha(path)
        return read(path)

    catalogue = source(args.data / "catalogue.json")["quests"]
    resources = {r["depot"]: r for r in source(args.data / "resources.json")["resources"]}
    summary = source(args.data / "performance-summary.json")
    manifest = source(args.data / "performance-manifest.json")
    scenes, cases = {}, {}
    for shard in manifest["shards"]:
        path = args.data / "performances" / Path(shard["path"]).name
        assert sha(path) == shard["sha256"], f"Changed performance shard: {path}"
        records = source(path)["scenes"]
        assert len(records) == shard["scenes"]
        assert sum(len(r["events"]) for r in records) == shard["events"]
        for record in records:
            depot = record["depot"]
            assert depot not in scenes
            meta = resources[depot]
            assert all(record[k] == meta[k] for k in ("raw_sha256", "binary_sha256"))
            scenes[depot] = {"family": shard["family"], **metrics(record)}
            assert scenes[depot]["events"] == summary["resources"][depot]["events"]
            assert scenes[depot]["event_types"] == summary["resources"][depot]["types"]
            name = depot.rsplit('\\', 1)[-1]
            if name in CASES:
                node = CASES[name]
                cases[depot] = {"node": node, "raw_sha256": record["raw_sha256"],
                    "events": [e for e in record["events"] if e["node"] == node]}
    # Scene graph metadata is joined by exact depot and source hashes, never by filename.
    for family in sorted({s["family"] for s in scenes.values()}):
        for record in source(args.data / "evidence" / (family + ".json.gz"))["resources"]:
            depot = record["depot"]
            if depot not in scenes:
                continue
            scene = scenes[depot]
            assert all(scene[k] == record[k] for k in ("raw_sha256", "binary_sha256"))
            scene.update({"actors": record["actors"], "entry_points": record["entry_points"],
                "exit_points": record["exit_points"], "graph_nodes": len(record["nodes"]),
                "graph_edges": len(record["edges"]), "screenplay_options": record["screenplay_option_count"],
                "choice_nodes": sum(n["data"].get("$type") == "scnChoiceNode" for n in record["nodes"]),
                "end_nodes": [{"node": n["data"].get("nodeId", {}).get("id"),
                    "type": n["data"].get("type", "<omitted>"), "pointer": n["pointer"]}
                    for n in record["nodes"] if n["data"].get("$type") == "scnEndNode"],
                "node_types": dict(Counter(n["data"].get("$type", "unknown") for n in record["nodes"])),
                "embedded_operation_types": dict(Counter(t for n in record["nodes"]
                    for t in nested_types(n["data"].get("questNode", {})))),
                "resource_references": record["references"],
                "acquisition_plans": dict(Counter(a.get("acquisition", "<omitted>") for a in record["actors"]))})
            if depot in cases:
                case = cases[depot]
                case["section"] = next(n for n in record["nodes"]
                    if str(n["data"].get("nodeId", {}).get("id")) == case["node"])
                case["adjacent_edges"] = [e for e in record["edges"]
                    if case["node"] in (e["source_node"], e["destination_node"])]
                case["interruption_scenarios"] = scene["interruption_scenarios"]
    totals = Counter()
    for s in scenes.values():
        totals.update(s["event_types"])
        assert "actors" in s
    assert len(scenes) == summary["scenes"]
    assert dict(totals) == summary["event_types"]
    assert set(totals) <= set.union(*GROUPS.values()), "Unclassified stored event type"
    assert len(cases) == len(CASES)
    quests = []
    for q in catalogue:
        selected = sorted(set(q["scope_resources"]) & scenes.keys())
        parent = sorted((set(q.get("parent_context_resources", [])) & scenes.keys()) - set(selected))
        event_types = Counter()
        capabilities = Counter()
        for depot in selected:
            event_types.update(scenes[depot]["event_types"])
            capabilities.update(scenes[depot]["capabilities"])
        quests.append({k: q[k] for k in ("title", "quest_type", "journal_path", "status", "document")} |
            {"scenes": selected, "parent_context_scenes": parent, "event_types": dict(event_types),
             "capabilities": dict(capabilities), "events": sum(event_types.values())})
    by_type = {}
    for typ in sorted({q["quest_type"] for q in quests}):
        members = [q for q in quests if q["quest_type"] == typ]
        unique = set(d for q in members for d in q["scenes"])
        by_type[typ] = {"journal_entries": len(members), "with_scenes": sum(bool(q["scenes"]) for q in members),
            "unique_scenes": len(unique), "events_in_unique_scenes": sum(scenes[d]["events"] for d in unique)}
    aggregate = {"journal_entries": len(quests), "quests_with_scenes": sum(bool(q["scenes"]) for q in quests),
        "unique_quest_scope_scenes": len({d for q in quests for d in q["scenes"]}),
        "scenes": len(scenes), "events": sum(totals.values()), "event_types": dict(totals.most_common()),
        "by_quest_type": by_type,
        "capabilities": {k: {"scenes": sum(bool(s["capabilities"][k]) for s in scenes.values()),
            "events": sum(s["capabilities"][k] for s in scenes.values())} for k in GROUPS},
        "scenes_with_interruption_scenarios": sum(bool(s["interruption_scenarios"]) for s in scenes.values())}
    result = {"schema_version": 1, "scope": "Frozen vanilla corpus; structural evidence, no installed playback validation",
        "capability_event_types": {k: sorted(v) for k, v in GROUPS.items()},
        "aggregate": aggregate, "quests": quests, "scenes": scenes}
    args.out.mkdir(parents=True, exist_ok=True)
    write_json(args.out / "analysis.json.gz", result)
    write_json(args.out / "case-evidence.json.gz", cases)
    write_json(args.out / "ghostline-scene-inventory.json", project_inventory(source))
    render(args.docs, result)
    inputs[Path(__file__).resolve().relative_to(Path.cwd()).as_posix()] = sha(Path(__file__))
    write_json(args.out / "verification.json", {"inputs": inputs, "aggregate": aggregate,
        "checks": ["Performance shard SHA-256 matches manifest", "Scene hashes match resource and graph evidence",
            "Every scene/event/type total matches performance summary", "All journal identities retained",
            "Primary scope and parent context kept separate"],
        "analysis_sha256": sha(args.out / "analysis.json.gz"),
        "case_evidence_sha256": sha(args.out / "case-evidence.json.gz")})
    print(json.dumps(aggregate, indent=2))


def render(root, result):
    root.mkdir(parents=True, exist_ok=True)
    (root / "quests").mkdir(exist_ok=True)
    scenes, quests, a = result["scenes"], result["quests"], result["aggregate"]
    lines = ["# Cinematic scenes across all quests", "",
        "This study joins the frozen all-quest graph and performance evidence by exact depot and SHA-256. "
        "It covers every journal identity, with overlapping presentation capabilities rather than a guessed cinematic/noncinematic label.", "",
        "Read [the synthesis](synthesis.md), [source case studies](case-studies.md), "
        "[Ghostline comparison](ghostline-comparison.md), [method and reproduction](method.md), or [all scene resources](scene-index.md).", "",
        f"- Journal entries: **{a['journal_entries']:,}**; **{a['quests_with_scenes']:,}** have scenes in their selected forward context.",
        f"- Indexed scenes: **{a['scenes']:,}**; **{a['unique_quest_scope_scenes']:,}** occur in at least one selected quest context.",
        f"- Section event occurrences: **{a['events']:,}** across **{len(a['event_types'])}** event types.",
        "- Scene resources may serve several quests; per-quest and type totals must not be added as global totals.", "",
        "## Presentation capabilities", "", "Counts describe stored events. Camera presence includes holocall cameras and does not prove a locked player camera.", "",
        "| Capability | Scenes containing events | Event occurrences |", "| --- | ---: | ---: |"]
    for name, count in a["capabilities"].items():
        lines.append(f"| {name} | {count['scenes']:,} | {count['events']:,} |")
    lines += ["", "## Quest type coverage", "", "| Stored type | Entries | With scenes | Unique scenes within type |", "| --- | ---: | ---: | ---: |"]
    for typ, count in a["by_quest_type"].items():
        lines.append(f"| {typ} | {count['journal_entries']} | {count['with_scenes']} | {count['unique_scenes']} |")
    lines += ["", "## Every journal identity", "", "No selected scene means no scene evidence in this context; it does not establish that the playable quest has no cinematics.", "",
        "| Quest | Type | Attribution | Scenes | Events |", "| --- | --- | --- | ---: | ---: |"]
    for q in quests:
        lines.append(f"| [{cell(q['title'])}](quests/{q['document']}) | {q['quest_type']} | {cell(q['status'])} | {len(q['scenes'])} | {q['events']:,} |")
        quest_doc(root, q, scenes)
    (root / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    lines = ["# All indexed scene resources", "", "Includes scenes outside exported journal contexts, shared, ambient and test content. Counts do not imply reachability.", "",
        "| Scene depot | Family | Events | Event sections | Choices | Capabilities |", "| --- | --- | ---: | ---: | ---: | --- |"]
    for depot, s in sorted(scenes.items()):
        caps = ", ".join(k for k, v in s["capabilities"].items() if v)
        lines.append(f"| `{depot}` | {s['family']} | {s['events']} | {s['event_sections']} | {s['choice_nodes']} | {caps} |")
    (root / "scene-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def quest_doc(root, q, scenes):
    lines = [f"# {q['title']}: scene presentation", "", f"Journal identity: `{q['journal_path']}`. Stored type: **{q['quest_type']}**. Attribution: **{q['status']}**.", "",
        f"[Full quest flow dossier](../../all-quests/{q['document']}) · [All cinematic studies](../README.md)", "",
        "The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; "
        "it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.", ""]
    if not q["scenes"]:
        lines += ["No indexed scene in this selected context. Consult attribution and unresolved references in the flow dossier before drawing a presentation conclusion.", ""]
    for depot in q["scenes"]:
        s = scenes[depot]
        lines += [f"## `{depot}`", "",
            f"{s['graph_nodes']} graph nodes, {s['graph_edges']} edges; {s['event_sections']} event-bearing sections, {s['events']} events; "
            f"{s['screenplay_lines']} screenplay lines, {s['screenplay_options']} screenplay options, {s['choice_nodes']} choice nodes.", "",
            "Actors: " + "; ".join(f"{x.get('name', '?')} (actor {x.get('actor_id', '?')}, {x.get('acquisition', '<omitted>')})" for x in s["actors"]) + ".", "",
            "Entries: " + "; ".join(f"`{p.get('name', '<omitted>')}` → {p.get('nodeId', {}).get('id', '<omitted>')}" for p in s["entry_points"]) + ".", "",
            "Exits: " + "; ".join(f"`{p.get('name', '<omitted>')}` → {p.get('nodeId', {}).get('id', '<omitted>')}" for p in s["exit_points"]) + ".", "",
            "End nodes: " + "; ".join(f"{p['node']}: `{p['type']}`" for p in s["end_nodes"]) + ". Omitted types are not inferred.", "",
            f"Stored interruption scenarios: {len(s['interruption_scenarios'])}. Their presence alone does not prove a complete interruption/return lifecycle.", "",
            "| Event type | Count | Example section / event handle | Raw source pointer |", "| --- | ---: | --- | --- |"]
        for typ, count in s["event_types"].items():
            e = s["event_examples"][typ]
            lines.append(f"| `{typ}` | {count} | {e['node']} / {e['handle']} | `{e['pointer']}` |")
        lines += ["", "Presentation families coexisting in an event section (counts are sections, not durations):", ""]
        combinations = Counter(tuple(v) for v in s["section_capabilities"].values())
        lines += [f"- {', '.join(k) or 'Other event types'}: {v}" for k, v in combinations.most_common()]
        lines += ["", f"Raw SHA-256: `{s['raw_sha256']}`. Binary SHA-256: `{s['binary_sha256']}`.", "",
            "Query exact event payloads:", "", "```powershell",
            f'py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "{depot}" --events', "```", ""]
    if q["parent_context_scenes"]:
        lines += ["## Parent context (excluded from primary totals)", ""]
        lines += [f"- `{d}`" for d in q["parent_context_scenes"]]
    (root / "quests" / q["document"]).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("reference/quests/deep-dives/all-quests"))
    parser.add_argument("--out", type=Path, default=Path("reference/quests/deep-dives/cinematic-scenes"))
    parser.add_argument("--docs", type=Path, default=Path("docs/reference/vanilla-quests/deep-dives/cinematic-scenes"))
    args = parser.parse_args()
    build(args)


if __name__ == "__main__":
    main()
