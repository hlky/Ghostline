"""Build per-journal structural dossiers from source-verified quest records.

This reports stored graph structure and data dependencies, not simulated game
execution. Shared family resources are never attributed exclusively to one job.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
from functools import lru_cache
import gzip
import hashlib
import json
import os
from pathlib import Path
import re

from build_quest_deep_dive_evidence import walk


CONTRACTS = {
    "scene_interface": ("questSceneNodeDefinition", "scene + entry + actor/marker bindings", "named exits and cancellation", "Validate every consumed entry/exit and distinguish terminating from notification outputs."),
    "choice_gate": ("scnChoiceNode", "choice + eligibility predicates + commit effects", "selected option or defer/interruption", "Keep knowledge, skill eligibility and persistent decision separate; test return to the choice."),
    "elapsed_time": ("questGameTimeDelay_ConditionType", "clock domain + duration + start/reset condition", "elapsed signal", "Compose objective/contact behavior separately; test time skip and save/load."),
    "realtime_delay": ("questRealtimeDelay_ConditionType", "real-time duration + cancellation owner", "elapsed signal", "Do not substitute game time for real time; retire delayed effects after cancellation."),
    "actor_readiness": ("questCharacterSpawned_ConditionType", "community/entry or actor reference + count policy", "actor available", "Test already-spawned, delayed and missing actors before speech or commands."),
    "community_lifecycle": ("questCommunityTemplate_NodeType", "community + named entries/phases + ownership", "activated/reactivated/deactivated entries", "Spawn, readiness and safe departure cleanup are separate steps."),
    "scan_evidence": ("questScan_ConditionType", "clue reference + exact scan event + required-set policy", "clue observed", "Preserve Started versus Finished, ordering, bypass and reaction joins."),
    "item_state": ("questInventory_ConditionType", "item ID + entity + quantity/comparison", "ownership predicate", "Ownership alone does not prove reading, device interaction or reward delivery."),
    "device_action": ("questDeviceManager_NodeType", "controller class + object + action", "action dispatched", "Bind the matching device completion predicate; dispatch alone is not success."),
    "device_state": ("questDevice_ConditionType", "controller class + object + condition function", "device predicate", "Check already-satisfied state and controller persistence across save/load."),
    "journal_read": ("questJournalEntryVisited_ConditionType", "full journal entry path + visited state", "entry visited", "Verify the actual UI read event in game; keep inventory pickup distinct."),
    "target_resolution": ("questCharacterKilled_ConditionType", "target set + lethal/unconscious/defeated policy", "target resolved", "Review RED defaults, early defeat and per-target deduplication before counter joins."),
    "combat_control": ("questCombatNodeDefinition", "actor + target + combat operation", "command result", "Separate hostility, threat injection, encounter completion and target cleanup."),
    "actor_route": ("questMovePuppetNodeDefinition", "actor + authored route/spline + movement policy", "movement output", "World navigation is a dependency; test blockage, combat and departure recovery."),
    "workspot_performance": ("questUseWorkspotNodeDefinition", "actor + workspot + entry/exit policy", "work started/success/failure", "Wait for actor/spot readiness and restore AI ownership on interruption."),
    "mount_state": ("questCharacterMount_ConditionType", "parent vehicle/puppet + child + role/event", "mount/unmount condition", "Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness."),
    "vehicle_control": ("questVehicleNodeDefinition", "vehicle reference + typed operation + world route", "operation-specific result", "Vehicle spawning, seats, driving, arrival and cleanup have separate owners."),
    "call_lifecycle": ("questPhoneManagerNodeDefinition", "contact + call operation + scene ownership", "connection/end state", "Audio filtering is not call connection; test busy, interrupted and ended calls."),
    "reward_commit": ("questGiveReward_NodeType", "reward record + eligibility + once-only commit", "reward delivered/committed", "Verify inventory/currency and objective state; prevent repeated awards after load."),
    "persistent_decision": ("questSetVar_NodeType", "namespaced fact + explicit write mode/value", "durable state update", "Separate scene-local presentation facts from public outcome state and review omitted defaults."),
    "conditional_route": ("questVarComparison_ConditionType", "fact + exact comparison + branch sockets", "selected branch", "Fact dependencies are not execution edges; identify producers and cancellation."),
    "parallel_join": ("questLogicalAndNodeDefinition", "named branch completion signals + reset policy", "all required inputs observed", "Test either completion order, early events, interruption and save/load at the join."),
    "race_resolution": ("questLogicalXorNodeDefinition", "competing outcome signals + retirement policy", "converged signal", "Review actual graph wiring; an XOR class alone does not prove loser cancellation."),
    "retire_branch": ("questCutControlNodeDefinition", "owned target branch(es) + permanent/reset policy", "branch retired", "Trace every CutSource destination; cancellation must not commit success."),
    "world_variant": ("questTogglePrefabVariant_NodeType", "prefab + variant + desired state + restore policy", "world presentation changed", "Resolve world ownership and restore only this quest's overrides."),
    "content_scope": ("questContentTokenManager_NodeType", "owned token source + block/unblock/spawn operation", "scope acquired/released", "Avoid copying broad UnblockAll behavior without an explicit ownership policy."),
    "braindance": ("scnRewindableSectionNode", "recording/scene + RID and analysis-layer bindings", "playback/analysis outcomes", "RID, seek/rewind, layer events and replay cleanup require separate verification."),
    "spatial_gate": ("questTriggerCondition", "trigger + activator + exact inside/outside event", "spatial predicate", "Resolve the registered NodeRef and test starting inside, exiting, actor activation and return."),
    "journal_transition": ("questJournalNodeDefinition", "typed journal operation + exact path + state socket", "journal operation output", "Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success."),
    "vehicle_ownership": ("questVehicleAvailable_ConditionType", "vehicle record + reconciliation policy", "availability predicate", "Do not equate purchase eligibility, vehicle availability and journal completion; preserve migration context."),
    "weighted_branch": ("questRandomizerNodeDefinition", "ordered output weights + explicit route bindings", "one authored weighted output", "Preserve output ordering, reset scope and persistence; compose difficulty and timing as separate gates."),
    "weather_scope": ("questPlayEnv_SetWeather", "weather operation + named source + reset policy", "weather request/reset dispatched", "Completion follows the caller's full restoration sequence, not an early cleanup fact."),
    "checkpoint": ("questCheckpointNodeDefinition", "checkpoint scope + save eligibility + debug identity", "checkpoint request", "Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone."),
    "save_eligibility": ("questSaveLock_ConditionType", "save-lock predicate + fallback path", "save eligibility branch", "Separate blocked-save fallback from checkpoint creation and verify installed behavior."),
    "loot_binding": ("questInjectLoot_NodeType", "spawned target + item record + operation", "loot injection dispatched", "Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately."),
    "controller_event": ("questEventManagerNodeDefinition", "entity + controller/PS class + typed event", "event dispatched", "Resolve controller ownership and its completion predicate; an event send is not operation success."),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def packed(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode()
    if path.exists() and gzip.decompress(path.read_bytes()) == payload:
        return
    path.write_bytes(gzip.compress(payload, mtime=0))


def esc(value):
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def leaf(path):
    return str(path).replace("\\", "/").split("/")[-1]


def family(depot):
    parts = depot.split("\\")
    zone = parts[0]
    match = re.search(r"\\((?:sq|mq|q)\d{3})\\", depot)
    if match:
        return zone + "-" + match.group(1)
    if "ue_metro" in parts:
        return zone + "-ue-metro"
    match = re.search(r"\\((?:wst|sts|mws|ma|sa)_[^\\]+)\\", depot)
    if match:
        return zone + "-" + match.group(1).replace("_", "-")
    return zone + "-shared"


def role(depot):
    if "\\bugfixing\\" in depot or "bugfix" in leaf(depot).casefold():
        return "repair"
    if re.search(r"\\(?:test|tests|debug)\\|chicken_test|cinedebug", depot, re.I):
        return "test/debug"
    return "content candidate"


def node_rows(record):
    for graph in record.get("graphs", []):
        for node in graph["nodes"]:
            yield "h" + graph["handle"], str(node["data"].get("id", "")), node, graph["edges"]
    for node in record.get("nodes", []):
        yield "scene", str(node["data"]["nodeId"]["id"]), node, record["edges"]


def values(data, key):
    return [value[key] for _, value in walk(data) if isinstance(value, dict) and key in value]


def journals(data):
    return [v for v in values(data, "realPath") if isinstance(v, str)]


def belongs(path, quest_path):
    return path == quest_path or path.startswith(quest_path + "/")


def edges_at(scope, node_id, edges):
    result = []
    for edge in edges:
        if scope == "scene":
            source, dest = edge["source_node"], edge["destination_node"]
            output, inp = edge["source_socket"], edge["destination_socket"]
        else:
            source, dest, output, inp = edge["from"], edge["to"], edge["output"], edge["input"]
        if source == node_id or dest == node_id:
            result.append(f"{source}:{output} → {dest}:{inp}")
    return result


def describe(data):
    core = data.get("questNode", data)
    typ = core.get("$type", "").removeprefix("quest").removesuffix("NodeDefinition")
    facts = []
    for _, value in walk(core):
        if isinstance(value, dict) and "factName" in value:
            detail = str(value["factName"])
            if "comparisonType" in value or "value" in value:
                detail += " " + str(value.get("comparisonType", "write/default comparison")) + " " + str(value.get("value", "RED default"))
            facts.append(detail)
    facts = sorted(set(facts))
    resources = [v for v in values(core, "DepotPath") if isinstance(v, str)]
    refs = [v for v in values(core, "objectRef") + values(core, "triggerAreaRef") if isinstance(v, str)]
    actions = [v for v in values(core, "deviceAction") + values(core, "deviceConditionFunction") if isinstance(v, str)]
    detail = facts or [leaf(v) for v in resources] or actions or refs
    clocks = [v for _, v in walk(core) if isinstance(v, dict) and v.get("$type") in {"questGameTimeDelay_ConditionType", "questRealtimeDelay_ConditionType"}]
    if clocks:
        detail = [json.dumps({k: v for k, v in c.items() if k != "$type"}) for c in clocks]
    return typ + ((": " + "; ".join(detail)) if detail else "")


def mapped_edges(scope, node_id, node, edges):
    """Decode only embedded quest-node mappings; keep raw scene stamps too."""
    if scope != "scene":
        return edges_at(scope, node_id, edges)
    result = edges_at(scope, node_id, edges)
    mappings = node["data"].get("isockMappings", [])
    if mappings:
        result += ["input mappings: " + ", ".join(f"0:{i}={v}" for i, v in enumerate(mappings))]
    return result


@lru_cache(maxsize=128)
def load_record(cache, name):
    return json.loads(gzip.decompress((Path(cache) / name).read_bytes()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--journal", type=Path, default=Path("reference/quests/deep-dives/catalogue/journal-input.json"))
    parser.add_argument("--data-out", type=Path, default=Path("reference/quests/deep-dives/catalogue"))
    parser.add_argument("--docs-out", type=Path, default=Path("docs/reference/vanilla-quests/deep-dives/catalogue"))
    parser.add_argument("--method", default="corpus-method.md")
    parser.add_argument("--contracts", default="expanded-blocks.md")
    args = parser.parse_args()
    index = json.loads((args.cache / "index.json").read_text(encoding="utf-8"))
    metadata = {r["depot"]: r for r in index["resources"] if r["status"] != "failed"}
    quests = json.loads(args.journal.read_text(encoding="utf-8"))["quests"]
    quest_roots = {q['path'] for q in quests}
    for item in metadata.values():
        owners = set()
        for path in item['journal_paths']:
            while path:
                if path in quest_roots:
                    owners.add(path)
                path = path.rsplit('/', 1)[0] if '/' in path else ''
        item['journal_quest_roots'] = sorted(owners)
    args.docs_out.mkdir(parents=True, exist_ok=True)
    args.data_out.mkdir(parents=True, exist_ok=True)
    groups = defaultdict(list)
    for depot, item in metadata.items():
        item["family"] = family(depot)
        item["role"] = role(depot)
        groups[item["family"]].append(item)
    evidence_inventory = []
    for group, items in sorted(groups.items()):
        records = [load_record(str(args.cache), item["cache"]) for item in items]
        target = args.data_out / "evidence" / (group + ".json.gz")
        packed(target, {"schema_version": 1, "family": group, "resources": records})
        evidence_inventory.append({"family": group, "path": target.as_posix(), "sha256": sha(target), "resources": len(items)})
    reverse = defaultdict(set)
    for depot, item in metadata.items():
        for ref in item.get("call_resources", item["graph_resources"]):
            reverse[ref].add(depot)
    catalogue = []
    pattern_usage = defaultdict(list)
    slugs = Counter(("ep1-" if q["path"].startswith("ep1/") else "base-") + leaf(q["path"]) for q in quests)
    for quest in sorted(quests, key=lambda q: (q["title"].casefold(), q["path"])):
        qpath = quest["path"]
        anchors = [depot for depot, item in metadata.items() if any(belongs(j, qpath) for j in item["journal_paths"]) and item["role"] != "test/debug"]
        # Quest roots often contain editor launch/test scaffolding beside a
        # call to the production phase. Keep their journal links separately;
        # actual parent calls still expose them as activation context. Do not
        # import sibling bootstrap graphs as the quest's forward flow.
        root_journal_anchors = [d for d in anchors if d.endswith('.quest')]
        production_anchors = [d for d in anchors if not d.endswith('.quest')]
        if production_anchors:
            anchors = production_anchors
        targets = {qpath}
        poi_only = False
        if not anchors:
            poi = qpath.replace("quests/minor_quest/", "points_of_interest/minor_quests/").replace("quests/side_quest/", "points_of_interest/side_quests/")
            poi_targets = {poi}
            # POI trees flatten region folders that remain in the quest
            # journal. This is an explicit weaker association, not activation.
            for category in ('minor_activities', 'street_stories'):
                if f'quests/{category}/' in qpath:
                    zone = 'ep1/' if qpath.startswith('ep1/') else ''
                    poi_targets.add(zone + 'points_of_interest/' + category + '/' + leaf(qpath))
            poi_anchors = [depot for depot, item in metadata.items() if any(any(belongs(j, p) for p in poi_targets) for j in item["journal_paths"]) and item["role"] != "test/debug"]
            if poi_anchors:
                anchors = poi_anchors
                targets = poi_targets
                poi_only = True
        def match_target(path):
            return any(belongs(path, target) for target in targets)
        seeds = []
        # Track exact anchor graph scopes, so a global root does not become the
        # inferred owner of every unrelated quest in that file.
        scope_resources = set(anchors)
        calls = set()
        anchor_graphs = defaultdict(set)
        anchor_nodes = {}
        for depot in anchors:
            record = load_record(str(args.cache), metadata[depot]["cache"])
            rows = list(node_rows(record))
            selected_scopes = {scope for scope, _, n, _ in rows if any(match_target(j) for j in journals(n["data"]))}
            family_id = metadata[depot]['family']
            expected_id = re.search(r'(?:^|_)((?:q|sq|mq)\d{3})(?:_|$)', leaf(qpath))
            own_family = (family_id.endswith('-' + expected_id.group(1)) if expected_id else
                          family_id.endswith('-' + leaf(qpath).replace('_', '-')))
            cross_quest_context = len(metadata[depot]['journal_quest_roots']) > 1 and not own_family
            shared_master = family_id in {'base-shared', 'ep1-shared', 'dlc-shared'} or cross_quest_context
            if shared_master:
                selected = {(scope, nid) for scope, nid, n, _ in rows if any(match_target(j) for j in journals(n['data']))}
                neighbors = set(selected)
                for scope, nid, node, edges in rows:
                    if (scope, nid) not in selected:
                        continue
                    for edge in edges:
                        source = edge.get('source_node', edge.get('from'))
                        dest = edge.get('destination_node', edge.get('to'))
                        if source == nid or dest == nid:
                            neighbors.update({(scope, source), (scope, dest)})
                # Only embedded graphs owned by selected nodes expand a shared
                # master. Selecting its root graph must not import all siblings.
                owner_pointers = [n['pointer'] for s, i, n, _ in rows if (s, i) in neighbors]
                for graph in record.get('graphs', []):
                    if any(graph['pointer'].startswith(prefix + '/') for prefix in owner_pointers):
                        neighbors.update(('h' + graph['handle'], str(n['data']['id'])) for n in graph['nodes'])
                anchor_nodes[depot] = {scope: sorted(i for s, i in neighbors if s == scope)
                                       for scope in sorted({s for s, _ in neighbors})}
                selected_scopes = set(anchor_nodes[depot])
            # Dedicated family files can contain pre-journal setup/progress in
            # sibling embedded graphs. Retain the whole file as shared context;
            # a global master is deliberately scoped more narrowly.
            if not depot.endswith('.quest') and metadata[depot]["family"] not in {"base-shared", "ep1-shared", "dlc-shared"}:
                selected_scopes.update("h"+g["handle"] for g in record.get("graphs", []))
            # A journal-bearing parent graph owns its embedded gameplay graphs
            # even when the child contains no journal nodes (e.g. Skippy's
            # target counter). Do not accidentally drop those mechanisms.
            selected_pointers = [g["pointer"] for g in record.get("graphs", []) if not shared_master and "h"+g["handle"] in selected_scopes]
            for graph in record.get("graphs", []):
                if any(graph["pointer"].startswith(prefix + "/") for prefix in selected_pointers):
                    selected_scopes.add("h" + graph["handle"])
            anchor_graphs[depot] = selected_scopes
            for scope, nid, node, edges in rows:
                matching = [j for j in journals(node["data"]) if match_target(j)]
                if matching:
                    seeds.append({"depot": depot, "scope": scope, "node": nid, "pointer": node["pointer"],
                                  "paths": matching, "type": describe(node["data"]),
                                  "edges": mapped_edges(scope, nid, node, edges)})
                if scope in selected_scopes:
                    if depot in anchor_nodes and nid not in anchor_nodes[depot].get(scope, []):
                        continue
                    core = node['data'].get('questNode', node['data'])
                    for v in values(node["data"], "DepotPath"):
                        if isinstance(v, str) and (v.endswith('.community') or
                            (core.get('$type') in {'questPhaseNodeDefinition', 'questSceneNodeDefinition'} and
                             v.endswith(('.questphase', '.quest', '.scene')))):
                            calls.add(v)
        queue = deque(sorted(calls))
        unresolved = set()
        historical = set()
        while queue:
            depot = queue.popleft()
            if depot in scope_resources:
                continue
            if depot not in metadata:
                (historical if "\\versions\\" in depot else unresolved).add(depot)
                continue
            if metadata[depot]["role"] == "test/debug":
                continue
            scope_resources.add(depot)
            queue.extend(metadata[depot].get("call_resources", metadata[depot]["graph_resources"]))
        scope_groups = sorted({metadata[d]["family"] for d in scope_resources})
        # Family association without a journal match is only a discovery hint.
        hint = re.search(r"(?:^|_)((?:mq|sq|q)\d{3})", leaf(qpath))
        hinted = [d for d, m in metadata.items() if hint and m["family"].endswith("-" + hint.group(1))]
        status = ("POI-linked; quest activation unresolved" if poi_only else "journal-linked") if seeds else "unresolved attribution"
        slug = ("ep1-" if qpath.startswith("ep1/") else "base-") + leaf(qpath)
        if slugs[slug] > 1:
            slug += "-" + hashlib.sha256(qpath.encode()).hexdigest()[:8]
        filename = slug + ".md"
        selected_rows = []
        signatures = defaultdict(list)
        fact_rows = defaultdict(lambda: {"writers": [], "readers": []})
        for depot in sorted(scope_resources):
            record = load_record(str(args.cache), metadata[depot]["cache"])
            for scope, nid, node, edges in node_rows(record):
                if depot in anchor_graphs and scope not in anchor_graphs[depot]:
                    continue
                if depot in anchor_nodes and nid not in anchor_nodes[depot].get(scope, []):
                    continue
                locator = f"{leaf(depot)} / {scope} / {nid}"
                selected_rows.append((depot, scope, nid, node, edges))
                types = set(values(node["data"], "$type"))
                for name, (signature, _, _, _) in CONTRACTS.items():
                    if signature in types:
                        signatures[name].append(locator)
                for _, value in walk(node["data"]):
                    if isinstance(value, dict) and isinstance(value.get("factName"), str):
                        operation = "writers" if value.get("$type") == "questSetVar_NodeType" else "readers"
                        fact_rows[value["factName"]][operation].append(locator)
        entry = {"title": quest["title"], "quest_type": quest["type"], "journal_path": qpath, "journal_hash": quest["hash"],
                 "status": status, "document": filename, "anchor_nodes": seeds,
                 "root_journal_context": root_journal_anchors,
                 "anchor_graph_scopes": {d: sorted(scopes) for d, scopes in sorted(anchor_graphs.items())},
                 "anchor_node_selection": anchor_nodes,
                 "scope_resources": sorted(scope_resources), "evidence_families": scope_groups,
                 "unresolved_graph_resources": sorted(unresolved),
                 "historical_references": sorted(historical),
                 "family_discovery_hints": sorted(hinted) if not seeds else [],
                 "block_candidates": {k: sorted(set(v)) for k, v in signatures.items()}}
        entry["scope_role_counts"] = dict(sorted(Counter(metadata[d]["role"] for d in scope_resources).items()))
        catalogue.append(entry)
        for block, locators in entry["block_candidates"].items():
            pattern_usage[block].append({"quest": quest["title"], "document": filename, "examples": locators[:3], "occurrences": len(locators)})

        lines = [f"# {quest['title']}", "", f"Journal: `{qpath}` · `{quest['type']}` · hash `{quest['hash']}`.", "",
                 f"**Coverage: {status}.** {len(seeds)} exact {'POI' if poi_only else 'journal'}-linked nodes in {len(anchors)} resources; "
                 f"{len(scope_resources)} resources in the inspected dependency context.", "",
                 "Resource roles in that context: " + ", ".join(f"{count} {kind}" for kind, count in sorted(entry["scope_role_counts"].items())) + ". Role labels describe path/name evidence, not proof of runtime reachability.", "",
                 "Root quest resources with additional journal references: " + ("; ".join('`'+d+'`' for d in root_journal_anchors) or "none indexed") + ". Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.", "",
                 "Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. "
                 "The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, "
                 f"or infer chronology from journal objective order. See [method](../{args.method}).", "",
                 "## Journal objectives and implementation anchors", "",
                 "Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.", "",
                 "| Objective | Journal path |", "| --- | --- |"]
        if quest.get("description"):
            lines[4:4] = ["Journal premise: " + quest["description"].replace("\n", " "), ""]
        for obj in quest["objectives"]:
            lines.append(f"| {esc(obj['description'])} ({esc(obj['type'])}) | `{obj['path']}` |")
        if not quest["objectives"]:
            lines.append("| No objective records in this export | — |")
        lines += ["", "## Exact journal transitions and neighboring signals", "",
                  "Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. "
                  "Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.", "",
                  "| Source locator | Journal target | Connected signals |", "| --- | --- | --- |"]
        for seed in seeds:
            loc = f"{leaf(seed['depot'])} / {seed['scope']} / {seed['node']}"
            lines.append(f"| `{loc}` ({esc(seed['type'])}) | {'; '.join('`'+j+'`' for j in seed['paths'])} | {esc('; '.join(seed['edges']) or 'No connected edge in indexed graph')} |")
        if not seeds:
            lines += ["| No exact journal match | Attribution remains unresolved | Filename/family hints are not treated as a verified trace |"]
        lines += ["", "## Phase calls and scene handoffs", "",
                  "Calls below come from journal-linked graph scopes and their forward resource dependencies. "
                  "Incoming sockets select entries; outgoing sockets show the caller's actual consumers. "
                  "An exposed but unwired output does not advance its parent.", "",
                  "| Call site | Resource / marker | Connected signals |", "| --- | --- | --- |"]
        call_count = 0
        for depot, scope, nid, node, edges in selected_rows:
            core = node["data"].get("questNode", node["data"])
            if core.get("$type") not in {"questPhaseNodeDefinition", "questSceneNodeDefinition"}:
                continue
            refs = [v for v in values(core, "DepotPath") if isinstance(v, str)]
            markers = [v for v in values(core, "nodeRef") if isinstance(v, str)]
            if not refs:
                continue
            call_count += 1
            lines.append(f"| `{leaf(depot)} / {scope} / {nid}` | {'; '.join('`'+v+'`' for v in refs+markers)} | {esc('; '.join(edges_at(scope,nid,edges)) or 'No connections')} |")
        if not call_count:
            lines.append("| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |")
        # Follow actual ancestor call sites without importing all siblings of a
        # shared master graph into the quest's forward dependency context.
        lines += ["", "## Parent orchestration and activation context", "",
                  "Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. "
                  "Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.", "",
                  "| Parent call site | Called resource | Incoming gates and connected outputs |", "| --- | --- | --- |"]
        parents = set()
        parent_rows = []
        frontier = deque(sorted(scope_resources))
        visited = set(scope_resources)
        while frontier:
            child = frontier.popleft()
            for parent in sorted(reverse.get(child, [])):
                if metadata[parent]["role"] == "test/debug":
                    continue
                record = load_record(str(args.cache), metadata[parent]["cache"])
                rows = list(node_rows(record))
                lookup = {(s, i): n for s, i, n, _ in rows}
                actual = False
                for scope, nid, node, edges in rows:
                    core = node["data"].get("questNode", node["data"])
                    if core.get("$type") not in {"questPhaseNodeDefinition", "questSceneNodeDefinition"} or child not in values(core, "DepotPath"):
                        continue
                    actual = True
                    gates = []
                    for edge in edges:
                        source = edge.get("source_node", edge.get("from"))
                        dest = edge.get("destination_node", edge.get("to"))
                        if dest == nid and (scope, source) in lookup:
                            gates.append(f"{source}: {describe(lookup[(scope, source)]['data'])}")
                    parent_rows.append((parent, scope, nid, child, gates, edges_at(scope,nid,edges)))
                if actual:
                    parents.add(parent)
                    if parent not in visited:
                        visited.add(parent)
                        frontier.append(parent)
        for parent, scope, nid, child, gates, edges in parent_rows:
            lines.append(f"| `{parent}` / {scope} / {nid} | `{leaf(child)}` | {esc('; '.join(gates+edges))} |")
        if not parent_rows:
            lines.append("| No resolved parent call in indexed scope | — | Global entry eligibility remains unproven |")
        entry["parent_context_resources"] = sorted(parents)
        entry["parent_evidence_families"] = sorted({metadata[d]["family"] for d in parents})
        lines += ["", "## Scene interfaces and actors", "", "| Scene | Entries → exits | Actors; graph size |", "| --- | --- | --- |"]
        scenes = []
        for depot in sorted(scope_resources):
            if not depot.endswith(".scene"):
                continue
            record = load_record(str(args.cache), metadata[depot]["cache"])
            scenes.append(record)
            actors = "; ".join(str(a.get("name", a.get("actor_id", a))) for a in record.get("actors", []))
            entries = ", ".join(p["name"] for p in record.get("entry_points", []))
            exits = ", ".join(p["name"] for p in record.get("exit_points", []))
            lines.append(f"| `{leaf(depot)}` | {esc(entries)} → {esc(exits)} | {esc(actors)}; {len(record.get('nodes',[]))} nodes / {len(record.get('edges',[]))} edges |")
        if not scenes:
            lines.append("| No resolved scene dependency in this scope | This does not prove the quest has no dialogue | — |")
        lines += ["", "## Choice labels, eligibility and outgoing branches", "",
                  "Text is joined from screenplay option IDs to the embedded localization store. "
                  "An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.", "",
                  "| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |", "| --- | --- | --- | --- |"]
        choice_count = 0
        for record in scenes:
            option_map = {str(v.get("itemId", {}).get("id", "")): v for v in record.get("screenplay_options", [])}
            for node in record.get("nodes", []):
                data = node["data"]
                if data.get("$type") != "scnChoiceNode":
                    continue
                nid = str(data["nodeId"]["id"])
                scene_depot = record['depot']
                if scene_depot in anchor_nodes and nid not in anchor_nodes[scene_depot].get('scene', []):
                    continue
                for number, option in enumerate(data.get("options", [])):
                    screenplay = option_map.get(str(option.get("screenplayOptionId", {}).get("id", "")), {})
                    locid = str(screenplay.get("locstringId", {}).get("ruid", ""))
                    text = record.get("choice_text", {}).get(locid, "Text join unresolved")
                    gates = {key: option[key] for key in ("questCondition", "bluelineCondition", "condition", "paymentCondition") if key in option}
                    outgoing = [f"{e['source_socket']} → {e['destination_node']}:{e['destination_socket']}" for e in record["edges"] if e["source_node"] == nid and e["source_socket"] == f"0:{number}"]
                    lines.append(f"| `{leaf(record['depot'])} / n{nid} / {number}` | {esc(text)} (`{esc(option.get('caption',''))}`) | {esc(json.dumps(gates,ensure_ascii=False) if gates else 'No option-level predicate stored')} | {esc('; '.join(outgoing) or 'No matching 0:ordinal output; inspect raw stamps')} |")
                    choice_count += 1
        if not choice_count:
            lines.append("| No choice option in resolved scene context | — | — | — |")
        lines += ["", "## Persistent state dependencies", "",
                  "A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. "
                  "RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.", "",
                  "| Fact | Writers in context | Readers/conditions in context |", "| --- | --- | --- |"]
        for fact, uses in sorted(fact_rows.items()):
            lines.append(f"| `{fact}` | {esc('; '.join(sorted(set(uses['writers']))) or 'Producer outside selected context')} | {esc('; '.join(sorted(set(uses['readers']))) or 'No reader in selected context')} |")
        if not fact_rows:
            lines.append("| No named fact uses in selected graph context | — | — |")
        control_types = {"questPauseConditionNodeDefinition", "questConditionNodeDefinition", "questSwitchNodeDefinition",
                         "questCutControlNodeDefinition", "questLogicalAndNodeDefinition", "questLogicalXorNodeDefinition"}
        controls = []
        for depot, scope, nid, node, edges in selected_rows:
            core = node["data"].get("questNode", node["data"])
            if core.get("$type") in control_types:
                fields = {k: v for k, v in core.items() if k not in {"$type", "id", "sockets"}}
                controls.append((depot, scope, nid, core["$type"], fields, edges_at(scope,nid,edges)))
        lines += ["", "## Exact gates, joins and cancellation", "",
                  f"<details><summary>{len(controls)} stored control nodes in the selected context</summary>", "",
                  "Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. "
                  "This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.", "",
                  "| Locator | Type and authored fields | Connected signals |", "| --- | --- | --- |"]
        for depot, scope, nid, typ, fields, edges in controls:
            lines.append(f"| `{leaf(depot)} / {scope} / {nid}` | `{typ}` `{esc(json.dumps(fields,ensure_ascii=False,separators=(',',':')))}` | {esc('; '.join(edges))} |")
        if not controls:
            lines.append("| No control nodes in resolved context | — | — |")
        lines += ["", "</details>", ""]
        lines += ["", "## Candidate Ghostline blocks", "",
                  "These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types "
                  "or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.", "",
                  "| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |", "| --- | --- | --- |"]
        for name, locators in sorted(signatures.items()):
            _, inputs, outputs, boundary = CONTRACTS[name]
            unique = sorted(set(locators))
            examples = "; ".join(unique[:4])
            if len(unique) > 4:
                examples += f"; +{len(unique)-4} locations in catalogue.json"
            lines.append(f"| `{name}` | {esc(examples)} | {esc(inputs)} → {esc(outputs)}. {esc(boundary)} |")
        if not signatures:
            lines.append("| No source-backed candidate assigned | Attribution must be resolved first | Do not derive blocks solely from the quest title |")
        lines += ["", "## Dependencies and coverage limits", "",
                  "| Resource | Role | Evidence family |", "| --- | --- | --- |"]
        for depot in sorted(scope_resources):
            lines.append(f"| `{depot}` | {metadata[depot]['role']}; {'journal anchor' if depot in anchors else 'forward dependency'} | `{metadata[depot]['family']}` |")
        linked_groups = sorted(set(scope_groups + entry["parent_evidence_families"]))
        evidence_relative = Path(os.path.relpath(args.data_out / "evidence", args.docs_out)).as_posix()
        lines += ["", "Evidence shards for this dossier (including parent context): " + (", ".join(f"[{g}]({evidence_relative}/{g}.json.gz)" for g in linked_groups) or "none; attribution unresolved") + ".", ""]
        if unresolved:
            lines += ["Unresolved phase/scene/community resources:", ""] + [f"- `{d}`" for d in sorted(unresolved)] + [""]
        if historical:
            lines += ["Historical version references retained as dependency identities, not merged into the current flow:", ""] + [f"- `{d}`" for d in sorted(historical)] + [""]
        if not seeds:
            lines += ["Discovery hints only (not substituted for a source trace):", ""] + [f"- `{d}`" for d in hinted] + [""]
        lines += ["World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins "
                  "and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, "
                  "event locstrings and community entries remain in the evidence shards.", "",
                  "## Required acceptance cases before reuse", "",
                  "Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; "
                  "start with spatial/item/actor predicates already satisfied; save/load across waits and joins; "
                  "cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. "
                  f"Apply the block-specific cases in the [expanded contracts](../{args.contracts}). No installed playtest is claimed.", ""]
        (args.docs_out / filename).write_text("\n".join(lines), encoding="utf-8")
        print(f"{quest['title']}: {status}, {len(seeds)} anchors, {len(scope_resources)} resources", flush=True)
    dump(args.data_out / "catalogue.json", {"schema_version": 1, "quests": catalogue})
    # Cache filenames and cache/index execution status are excluded from the
    # checked resource inventory, so a cached rerun is reproducible.
    dump(args.data_out / "resources.json", {"resources": [{k: v for k, v in item.items() if k not in {"cache", "status"}} for item in metadata.values()], "index_failures": [r for r in index["resources"] if r["status"] == "failed"]})
    dump(args.data_out / "evidence-manifest.json", {"shards": evidence_inventory})
    dump(args.data_out / "block-occurrences.json", dict(sorted(pattern_usage.items())))
    overview = ["# Quest structural catalogue", "", f"{len(catalogue)} journal entries, including base-game and Phantom Liberty paths. "
                "Each document contains exact journal transitions, phase/scene handoffs, state dependencies, candidate contracts and explicit evidence boundaries.", "",
                "The two manually reviewed pilot dossiers remain [Space Oddity](../space-oddity.md) and [Happy Together](../happy-together.md). "
                "This corpus expansion is generated source-backed structural analysis, not a claim of equivalent manual branch-by-branch review or runtime proof. "
                f"See [method and provenance](../{args.method}) and [expanded contracts](../{args.contracts}).", "",
                "| Quest | Journal path | Coverage | Anchors / resources |", "| --- | --- | --- | --- |"]
    for entry in catalogue:
        overview.append(f"| [{esc(entry['title'])}]({entry['document']}) | `{entry['journal_path']}` | {entry['status']} | {len(entry['anchor_nodes'])} / {len(entry['scope_resources'])} |")
    (args.docs_out / "README.md").write_text("\n".join(overview)+"\n", encoding="utf-8")
    contracts = ["# Expanded source-backed block contracts", "",
                 "These contracts were mined from the structural catalogue. A stored type is evidence for a candidate mechanism, "
                 "not proof of a complete isolated block or runtime behavior. Counts include explicitly identified repair/dependency context; "
                 "they are not counts of unique gameplay implementations. See the [cross-quest compositions](cross-quest-patterns.md) "
                 "and the pilot's [12 lifecycle contracts](building-blocks.md).", ""]
    for name, (signature, inputs, outputs, boundary) in sorted(CONTRACTS.items()):
        uses = pattern_usage.get(name, [])
        contracts += [f"## `{name}`", "", f"Stored signature: `{signature}`. Observed in {len(uses)} quest dependency contexts.", "",
                      f"**Inputs:** {inputs}. **Outputs:** {outputs}.", "", boundary, "",
                      "Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; "
                      "test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. "
                      "Structural serialization checks do not replace an installed acceptance run.", "",
                      "| Example quest | Source locations |", "| --- | --- |"]
        examples = uses[:2] + next(([u] for u in uses if u["document"].startswith("ep1-")), [])
        seen = set()
        for use in examples:
            if use["document"] in seen:
                continue
            seen.add(use["document"])
            contracts.append(f"| [{esc(use['quest'])}]({args.docs_out.name}/{use['document']}) | {esc('; '.join(use['examples']))} |")
        if not uses:
            contracts.append("| No matching type in selected contexts | No runtime or implementation claim |")
        contracts += ["", "The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.", ""]
    (args.docs_out.parent / args.contracts).write_text("\n".join(contracts), encoding="utf-8")
    print(json.dumps({"quests": len(catalogue), "status": dict(Counter(q['status'] for q in catalogue)), "shards": len(evidence_inventory)}))


if __name__ == "__main__":
    main()
