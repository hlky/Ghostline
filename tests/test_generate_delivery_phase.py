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
    "generate_delivery_phase",
    TOOLS / "generate_delivery_phase.py",
)
assert SPEC is not None
generate_delivery_phase = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["generate_delivery_phase"] = generate_delivery_phase
SPEC.loader.exec_module(generate_delivery_phase)


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


def resolve(
    value: dict[str, Any],
    handles: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    if "HandleRefId" in value:
        return handles[value["HandleRefId"]]
    return value


def scalar(value: Any) -> Any:
    if isinstance(value, dict) and "$value" in value:
        return value["$value"]
    return value


class GenerateDeliveryPhaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.phase = generate_delivery_phase.build_phase()
        self.handles = handle_map(self.phase)
        self.nodes = {
            node["Data"]["id"]: node
            for node in self.phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
        }

    def node_payload(self, quest_id: int, key: str) -> dict[str, Any]:
        return resolve(self.nodes[quest_id]["Data"][key], self.handles)["Data"]

    def graph_edges(self) -> set[tuple[int, str, int, str]]:
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
            edges.add((*socket_owner[source], *socket_owner[destination]))
        return edges

    def journal_node_path(self, quest_id: int) -> tuple[str, str, int]:
        journal_type = self.node_payload(quest_id, "type")
        path = resolve(journal_type["path"], self.handles)["Data"]
        return (
            path["realPath"],
            scalar(path["className"]),
            path["fileEntryIndex"],
        )

    def test_generation_is_deterministic_and_matches_checked_in_source(self) -> None:
        first = json.dumps(self.phase, indent=2) + "\n"
        second = json.dumps(generate_delivery_phase.build_phase(), indent=2) + "\n"
        self.assertEqual(first, second)

        self.assertTrue(
            generate_delivery_phase.DEFAULT_OUTPUT.is_file(),
            "run tools/generate_delivery_phase.py to create the checked-in raw phase",
        )
        checked_in = generate_delivery_phase.DEFAULT_OUTPUT.read_text(encoding="utf-8")
        self.assertEqual(first, checked_in)

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "gq000_delivery.questphase.json"
            generate_delivery_phase.write_phase(output)
            self.assertEqual(first, output.read_text(encoding="utf-8"))

    def test_graph_has_exact_delivery_and_phone_branch_topology(self) -> None:
        expected_edges = {
            (0, "Out", 10, "Active"),
            (10, "Out", 11, "Active"),
            (11, "Out", 12, "Active"),
            (12, "Out", 13, "In"),
            (13, "Out", 14, "In"),
            (13, "Out", 15, "In"),
            (15, "Out", 16, "In"),
            (16, "Out", 17, "Succeeded"),
            (17, "Out", 18, "Inactive"),
            (18, "Out", 19, "In"),
            (19, "Out", 20, "Active"),
            (20, "Out", 21, "Active"),
            (21, "Out", 22, "Active"),
            (22, "Out", 23, "In"),
            (22, "Out", 24, "In"),
            (23, "Out", 25, "Active"),
            (24, "Out", 26, "Active"),
            (25, "Out", 27, "In1"),
            (26, "Out", 27, "In2"),
            (27, "Out1", 28, "Active"),
            (28, "Out", 29, "In"),
            (29, "Out", 30, "In"),
            (30, "Out", 31, "In"),
            (31, "Out", 32, "Succeeded"),
            (32, "Out", 1, "In"),
        }
        edges = self.graph_edges()
        self.assertEqual(expected_edges, edges)
        self.assertEqual(generate_delivery_phase.EXPECTED_GRAPH_EDGES, len(edges))
        self.assertEqual(generate_delivery_phase.EXPECTED_GRAPH_NODES, len(self.nodes))

        response_join = self.nodes[27]["Data"]
        self.assertEqual("questLogicalXorNodeDefinition", response_join["$type"])
        self.assertEqual(2, response_join["inputSocketCount"])
        self.assertEqual(1, response_join["outputSocketCount"])

    def test_drop_point_reservation_uses_the_live_kabuki_device(self) -> None:
        self.assertEqual(
            "$/03_night_city/c_watson/kabuki/"
            "kabuki_drop_points_prefabAR4NTYY/drop_point_009_prefabBIYNP3Y",
            generate_delivery_phase.DROP_POINT_REF,
        )

        inventory = self.node_payload(13, "condition")
        inventory_type = resolve(inventory["type"], self.handles)["Data"]
        self.assertEqual("questObjectCondition", inventory["$type"])
        self.assertEqual("questInventory_ConditionType", inventory_type["$type"])
        self.assertEqual("GreaterOrEqual", inventory_type["comparisonType"])
        self.assertEqual(1, inventory_type["isPlayer"])
        self.assertEqual(generate_delivery_phase.DATACACHE_ITEM, scalar(inventory_type["itemID"]))
        self.assertEqual(1, inventory_type["quantity"])

        reserve = self.nodes[14]["Data"]
        self.assertEqual("questEventManagerNodeDefinition", reserve["$type"])
        self.assertEqual("DropPointManager", reserve["managerName"])
        self.assertEqual("controller", scalar(reserve["componentName"]))
        self.assertEqual("DropPointControllerPS", scalar(reserve["PSClassName"]))
        self.assertEqual(0, reserve["isObjectPlayer"])
        self.assertEqual(0, reserve["isUiEvent"])
        self.assertEqual(
            generate_delivery_phase.DROP_POINT_REF,
            scalar(reserve["objectRef"]["reference"]),
        )

        event = resolve(reserve["event"], self.handles)["Data"]
        self.assertEqual("ReserveItemToThisDropPoint", event["$type"])
        self.assertEqual(generate_delivery_phase.DATACACHE_ITEM, scalar(event["item"]))
        self.assertEqual(0, event["shouldActivateDevice"])
        self.assertEqual("None", scalar(event["actionName"]))

        deposited = self.node_payload(15, "condition")
        deposited_type = resolve(deposited["type"], self.handles)["Data"]
        self.assertEqual("questFactsDBCondition", deposited["$type"])
        self.assertEqual("questVarComparison_ConditionType", deposited_type["$type"])
        self.assertEqual("Greater", deposited_type["comparisonType"])
        self.assertEqual(generate_delivery_phase.DATACACHE_DEPOSIT_FACT, deposited_type["factName"])
        self.assertEqual(0, deposited_type["value"])

        self.assertEqual([], self.phase["Data"]["RootChunk"]["phasePrefabs"])

    def test_delivery_journal_and_facts_use_authored_paths(self) -> None:
        expected_journal = {
            10: (
                generate_delivery_phase.DELIVERY_OBJECTIVE,
                "gameJournalQuestObjective",
                2,
            ),
            11: (
                generate_delivery_phase.DELIVERY_DESCRIPTION,
                "gameJournalQuestDescription",
                2,
            ),
            17: (
                generate_delivery_phase.DELIVERY_OBJECTIVE,
                "gameJournalQuestObjective",
                2,
            ),
        }
        for quest_id, expected in expected_journal.items():
            self.assertEqual(expected, self.journal_node_path(quest_id))

        for quest_id in (12, 18):
            path = resolve(self.nodes[quest_id]["Data"]["path"], self.handles)["Data"]
            self.assertEqual(generate_delivery_phase.DELIVERY_MAPPIN, path["realPath"])
            self.assertEqual("gameJournalQuestMapPin", scalar(path["className"]))
            self.assertEqual(2, path["fileEntryIndex"])

        self.assertEqual(1, self.nodes[12]["Data"]["disablePreviousMappins"])
        self.assertEqual(0, self.nodes[18]["Data"]["disablePreviousMappins"])

        delivered = self.node_payload(16, "type")
        self.assertEqual("gq000_cache_delivered", delivered["factName"])
        self.assertEqual(1, delivered["setExactValue"])
        self.assertEqual(1, delivered["value"])

        completed = self.node_payload(31, "type")
        self.assertEqual("gq000_completed", completed["factName"])
        self.assertEqual(1, completed["setExactValue"])
        self.assertEqual(1, completed["value"])

        self.assertEqual(
            (
                generate_delivery_phase.QUEST_PATH,
                "gameJournalQuest",
                2,
            ),
            self.journal_node_path(32),
        )
        completion_type = self.node_payload(32, "type")
        self.assertEqual(1, completion_type["sendNotification"])
        self.assertEqual(1, completion_type["trackQuest"])

        reward_type = self.node_payload(30, "type")
        self.assertEqual("questGiveReward_NodeType", reward_type["$type"])
        self.assertEqual(
            [generate_delivery_phase.COMPLETION_REWARD],
            [scalar(reward) for reward in reward_type["rewards"]],
        )

    def test_morrow_phone_exchange_uses_both_authored_choices(self) -> None:
        expected_phone = {
            20: (
                generate_delivery_phase.MORROW_CACHE_AUTHENTICATED,
                "gameJournalPhoneMessage",
                1,
            ),
            21: (
                generate_delivery_phase.MORROW_ROUTE_FOUND,
                "gameJournalPhoneMessage",
                1,
            ),
            22: (
                generate_delivery_phase.MORROW_RESPONSE_GROUP,
                "gameJournalPhoneChoiceGroup",
                1,
            ),
            25: (
                generate_delivery_phase.MORROW_PAY_REPLY,
                "gameJournalPhoneMessage",
                1,
            ),
            26: (
                generate_delivery_phase.MORROW_ROUTE_REPLY,
                "gameJournalPhoneMessage",
                1,
            ),
            28: (
                generate_delivery_phase.MORROW_MORE_WORK,
                "gameJournalPhoneMessage",
                1,
            ),
        }
        for quest_id, expected in expected_phone.items():
            self.assertEqual(expected, self.journal_node_path(quest_id))

        expected_choices = {
            23: generate_delivery_phase.MORROW_PAY_CHOICE,
            24: generate_delivery_phase.MORROW_ROUTE_CHOICE,
        }
        for quest_id, expected_path in expected_choices.items():
            condition = self.node_payload(quest_id, "condition")
            condition_type = resolve(condition["type"], self.handles)["Data"]
            path = resolve(condition_type["path"], self.handles)["Data"]
            self.assertEqual("questJournalCondition", condition["$type"])
            self.assertEqual("questJournalEntryState_ConditionType", condition_type["$type"])
            self.assertEqual(expected_path, path["realPath"])
            self.assertEqual("gameJournalPhoneChoiceEntry", scalar(path["className"]))
            self.assertEqual(1, path["fileEntryIndex"])
            self.assertEqual(0, condition_type["inverted"])
            self.assertEqual("Succeeded", condition_type["state"])

        final_condition = self.node_payload(29, "condition")
        final_type = resolve(final_condition["type"], self.handles)["Data"]
        final_path = resolve(final_type["path"], self.handles)["Data"]
        self.assertEqual("questJournalEntryVisited_ConditionType", final_type["$type"])
        self.assertEqual(generate_delivery_phase.MORROW_MORE_WORK, final_path["realPath"])
        self.assertEqual("gameJournalPhoneMessage", scalar(final_path["className"]))
        self.assertEqual(1, final_type["visited"])

        delay = self.node_payload(19, "condition")
        delay_type = resolve(delay["type"], self.handles)["Data"]
        self.assertEqual("questRealtimeDelay_ConditionType", delay_type["$type"])
        self.assertEqual(1, delay_type["seconds"])


if __name__ == "__main__":
    unittest.main()
