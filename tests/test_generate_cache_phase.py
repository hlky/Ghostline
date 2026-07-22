from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

SPEC = importlib.util.spec_from_file_location(
    "generate_cache_phase", TOOLS / "generate_cache_phase.py"
)
assert SPEC is not None
generate_cache_phase = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["generate_cache_phase"] = generate_cache_phase
SPEC.loader.exec_module(generate_cache_phase)


def walk(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def handle_map(phase: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        value["HandleId"]: value
        for value in walk(phase)
        if isinstance(value, dict) and "HandleId" in value
    }


def resolve(value: dict[str, Any], handles: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if "HandleRefId" in value:
        return handles[value["HandleRefId"]]
    return value


def scalar(value: Any) -> Any:
    if isinstance(value, dict) and "$value" in value:
        return value["$value"]
    return value


class GenerateCachePhaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.phase = generate_cache_phase.build_phase()
        self.handles = handle_map(self.phase)
        self.nodes = {
            node["Data"]["id"]: node
            for node in self.phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
        }

    def node_payload(self, quest_id: int, key: str) -> dict[str, Any]:
        return resolve(self.nodes[quest_id]["Data"][key], self.handles)["Data"]

    def test_generation_is_deterministic_and_matches_checked_in_source(self) -> None:
        first = json.dumps(self.phase, indent=2) + "\n"
        second = json.dumps(generate_cache_phase.build_phase(), indent=2) + "\n"
        self.assertEqual(first, second)

        checked_in = generate_cache_phase.DEFAULT_OUTPUT.read_text(encoding="utf-8")
        self.assertEqual(first, checked_in)

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "gq000_post_accept.questphase.json"
            generate_cache_phase.write_phase(output)
            self.assertEqual(first, output.read_text(encoding="utf-8"))

    def test_graph_keeps_the_required_main_cache_flow(self) -> None:
        socket_owner: dict[str, tuple[int, str]] = {}
        for quest_id, node in self.nodes.items():
            for socket_value in node["Data"]["sockets"]:
                socket_handle = resolve(socket_value, self.handles)
                socket_owner[socket_handle["HandleId"]] = (
                    quest_id,
                    scalar(socket_handle["Data"]["name"]),
                )

        edges: set[tuple[int, str, int, str]] = set()
        for handle in self.handles.values():
            data = handle.get("Data", {})
            if data.get("$type") != "graphGraphConnectionDefinition":
                continue
            source = resolve(data["source"], self.handles)["HandleId"]
            destination = resolve(data["destination"], self.handles)["HandleId"]
            source_owner = socket_owner[source]
            destination_owner = socket_owner[destination]
            edges.add(
                (
                    source_owner[0],
                    source_owner[1],
                    destination_owner[0],
                    destination_owner[1],
                )
            )

        expected_ids = [0, *range(10, 18), *range(19, 39), 1]
        expected_inputs = [
            "Active",
            "Active",
            "Active",
            "In",
            "In",
            "In",
            "In",
            "In",
            "Succeeded",
            "Inactive",
            "Active",
            "Active",
            "Active",
            "In",
            "In",
            "In",
            "In",
            "In",
            "Succeeded",
            "Inactive",
            "Active",
            "Active",
            "In",
            "Active",
            "Active",
            "In",
            "Succeeded",
            "In",
            "In",
        ]
        expected_main_edges = {
            (source_id, "Out", destination_id, destination_socket)
            for source_id, destination_id, destination_socket in zip(
                expected_ids, expected_ids[1:], expected_inputs
            )
        }
        self.assertTrue(expected_main_edges.issubset(edges))
        self.assertEqual(44, len(edges))
        self.assertEqual(generate_cache_phase.EXPECTED_GRAPH_NODES, len(self.nodes))

    def test_access_point_uses_native_actions_and_hacking_conditions(self) -> None:
        actions = []
        for quest_id in (14, 24, 28):
            manager = self.node_payload(quest_id, "type")
            params = resolve(manager["params"][0], self.handles)["Data"]
            actions.append(scalar(params["deviceAction"]))
            self.assertEqual("AccessPointControllerPS", scalar(params["deviceControllerClass"]))
            self.assertEqual(generate_cache_phase.ACCESS_POINT_REF, scalar(params["objectRef"]))
        self.assertEqual(["ForceDisabled", "ForceEnabled", "ForceDisabled"], actions)

        hacking_condition = self.node_payload(25, "condition")
        hacking_type = resolve(hacking_condition["type"], self.handles)["Data"]
        self.assertEqual(
            "WasHackingMinigameSucceeded",
            scalar(hacking_type["deviceConditionFunction"]),
        )
        self.assertEqual(generate_cache_phase.ACCESS_POINT_REF, scalar(hacking_type["objectRef"]))

        post_hack_delay = self.node_payload(27, "condition")
        delay_type = resolve(post_hack_delay["type"], self.handles)["Data"]
        self.assertEqual("questRealtimeDelay_ConditionType", delay_type["$type"])
        self.assertEqual(1, delay_type["seconds"])

        all_types = {
            value.get("$type")
            for value in walk(self.phase)
            if isinstance(value, dict) and "$type" in value
        }
        self.assertNotIn("questUIElement_ConditionType", all_types)

    def test_guard_activation_is_immediate_and_cleanup_waits_until_player_leaves(self) -> None:
        spawn_actions = []
        for quest_id in (15, 38):
            action = resolve(
                self.nodes[quest_id]["Data"]["actions"][0]["type"], self.handles
            )["Data"]
            spawn_actions.append(action["action"])
            self.assertEqual("None", scalar(action["communityEntryName"]))
            self.assertEqual("None", scalar(action["communityEntryPhaseName"]))
            self.assertEqual(
                generate_cache_phase.GUARD_COMMUNITY_REF,
                scalar(action["spawnerReference"]),
            )
        self.assertEqual(["Activate", "Deactivate"], spawn_actions)

        spawned = self.node_payload(16, "condition")
        spawned_type = resolve(spawned["type"], self.handles)["Data"]
        comparison = resolve(spawned_type["comparisonParams"], self.handles)["Data"]
        self.assertEqual("questCharacterSpawned_ConditionType", spawned_type["$type"])
        self.assertEqual("Greater", comparison["comparisonType"])
        self.assertEqual(0, comparison["count"])
        self.assertEqual(1, comparison["entireCommunity"])
        self.assertEqual(
            generate_cache_phase.GUARD_COMMUNITY_REF,
            scalar(spawned_type["objectRef"]["reference"]),
        )

        arrival = self.node_payload(17, "condition")
        self.assertEqual("IsInside", arrival["type"])
        self.assertEqual(
            generate_cache_phase.ARRIVAL_TRIGGER_REF,
            scalar(arrival["triggerAreaRef"]),
        )
        cleanup = self.node_payload(36, "condition")
        self.assertEqual("IsOutside", cleanup["type"])
        self.assertEqual(
            generate_cache_phase.CLEANUP_TRIGGER_REF,
            scalar(cleanup["triggerAreaRef"]),
        )

        all_types = {
            value.get("$type")
            for value in walk(self.phase)
            if isinstance(value, dict) and "$type" in value
        }
        self.assertIn("questCharacterSpawned_ConditionType", all_types)

    def test_arrival_forces_each_named_guard_hostile_to_player(self) -> None:
        attitude_join = self.nodes[46]["Data"]
        self.assertEqual("questLogicalAndNodeDefinition", attitude_join["$type"])
        self.assertEqual(3, attitude_join["inputSocketCount"])
        self.assertEqual(1, attitude_join["outputSocketCount"])

        for index, entry_name in enumerate(generate_cache_phase.GUARD_ENTRIES):
            for quest_id, expected_group in ((40 + index, "neutral"), (43 + index, "hostile")):
                manager = self.node_payload(quest_id, "type")
                subtype = resolve(manager["subtype"], self.handles)["Data"]
                self.assertEqual(
                    "questCharacterManagerParameters_SetAttitudeGroupForPuppet",
                    subtype["$type"],
                )
                self.assertEqual(expected_group, scalar(subtype["groupName"]))
                self.assertEqual(0, subtype["isPlayer"])
                puppet = subtype["puppetRef"]
                self.assertEqual(
                    generate_cache_phase.GUARD_COMMUNITY_REF,
                    scalar(puppet["reference"]),
                )
                self.assertEqual([entry_name], [scalar(name) for name in puppet["names"]])

            target = self.nodes[47 + index]["Data"]
            self.assertEqual("questCombatNodeDefinition", target["$type"])
            self.assertEqual(
                generate_cache_phase.GUARD_COMMUNITY_REF,
                scalar(target["entityReference"]["reference"]),
            )
            self.assertEqual(
                [entry_name],
                [scalar(name) for name in target["entityReference"]["names"]],
            )
            self.assertEqual("questCombatNodeParams_ShootAt", scalar(target["function"]))
            target_params = resolve(target["params"], self.handles)["Data"]
            self.assertEqual("questCombatNodeParams_CombatTarget", target_params["$type"])
            self.assertEqual(0, target_params["duration"])
            self.assertEqual(1, target_params["immediately"])
            self.assertEqual("0", scalar(target_params["targetNode"]))
            self.assertEqual(
                generate_cache_phase.PLAYER_REF,
                scalar(target_params["targetPuppet"]["reference"]),
            )

            threat = self.nodes[50 + index]["Data"]
            self.assertEqual(
                [entry_name],
                [scalar(name) for name in threat["entityReference"]["names"]],
            )
            threat_params = resolve(threat["params"], self.handles)["Data"]
            self.assertEqual("AIInjectCombatThreatCommandParams", threat_params["$type"])
            self.assertEqual(0, threat_params["dontForceHostileAttitude"])
            self.assertEqual(0, threat_params["duration"])
            self.assertEqual(0, threat_params["isPersistent"])
            self.assertEqual("0", scalar(threat_params["targetNodeRef"]))
            self.assertEqual(
                generate_cache_phase.PLAYER_REF,
                scalar(threat_params["targetPuppetRef"]["reference"]),
            )

    def test_reach_and_extract_stages_use_distinct_mappins(self) -> None:
        expected = {
            12: generate_cache_phase.CACHE_MAPPIN,
            20: generate_cache_phase.CACHE_MAPPIN,
            23: generate_cache_phase.EXTRACT_MAPPIN,
            30: generate_cache_phase.EXTRACT_MAPPIN,
        }
        for quest_id, expected_path in expected.items():
            path = resolve(self.nodes[quest_id]["Data"]["path"], self.handles)["Data"]
            self.assertEqual(expected_path, path["realPath"])
            self.assertEqual("gameJournalQuestMapPin", scalar(path["className"]))
            self.assertEqual(2, path["fileEntryIndex"])

    def test_objectives_shards_and_facts_are_wired_to_the_authored_paths(self) -> None:
        expected_journal = {
            10: (generate_cache_phase.REACH_OBJECTIVE, "gameJournalQuestObjective", 2),
            11: (generate_cache_phase.REACH_DESCRIPTION, "gameJournalQuestDescription", 2),
            19: (generate_cache_phase.REACH_OBJECTIVE, "gameJournalQuestObjective", 2),
            21: (generate_cache_phase.EXTRACT_OBJECTIVE, "gameJournalQuestObjective", 2),
            22: (generate_cache_phase.EXTRACT_DESCRIPTION, "gameJournalQuestDescription", 2),
            29: (generate_cache_phase.EXTRACT_OBJECTIVE, "gameJournalQuestObjective", 2),
            31: (generate_cache_phase.SHARD_PATHS[0], "gameJournalOnscreen", 5),
            32: (generate_cache_phase.SHARD_PATHS[1], "gameJournalOnscreen", 5),
            34: (generate_cache_phase.LEAVE_OBJECTIVE, "gameJournalQuestObjective", 2),
            35: (generate_cache_phase.LEAVE_DESCRIPTION, "gameJournalQuestDescription", 2),
            37: (generate_cache_phase.LEAVE_OBJECTIVE, "gameJournalQuestObjective", 2),
        }
        for quest_id, (expected_path, expected_class, expected_index) in expected_journal.items():
            journal_type = self.node_payload(quest_id, "type")
            path = resolve(journal_type["path"], self.handles)["Data"]
            self.assertEqual(expected_path, path["realPath"])
            self.assertEqual(expected_class, scalar(path["className"]))
            self.assertEqual(expected_index, path["fileEntryIndex"])

        self.assertEqual("gq000_02_started", self.node_payload(13, "type")["factName"])
        acquired = self.node_payload(26, "type")
        self.assertEqual("gq000_cache_acquired", acquired["factName"])
        self.assertEqual(1, acquired["setExactValue"])
        self.assertEqual(1, acquired["value"])

        item_manager = self.node_payload(33, "type")
        params = [resolve(param, self.handles)["Data"] for param in item_manager["params"]]
        self.assertEqual(
            [*generate_cache_phase.SHARD_ITEMS, generate_cache_phase.DATACACHE_ITEM],
            [scalar(param["itemID"]) for param in params],
        )
        for param in params:
            self.assertEqual("AddItem", param["nodeType"])
            self.assertEqual(1, param["sendNotification"])
            player_ref = resolve(param["entityRef"], self.handles)["Data"]
            self.assertEqual(1, player_ref["refLocalPlayer"])

        prefab = self.phase["Data"]["RootChunk"]["phasePrefabs"][0]["prefabNodeRef"]
        self.assertEqual(generate_cache_phase.PHASE_PREFAB_REF, scalar(prefab))


if __name__ == "__main__":
    unittest.main()
