from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

SPEC = importlib.util.spec_from_file_location("explore_questphase", TOOLS / "explore_questphase.py")
assert SPEC is not None
explore_questphase = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["explore_questphase"] = explore_questphase
SPEC.loader.exec_module(explore_questphase)


class StabilityBaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.explorer = explore_questphase.QuestphaseExplorer(
            ROOT / "source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json"
        )
        cls.nodes_by_id = {node.quest_id: node for node in cls.explorer.nodes_by_handle.values()}

    def test_meeting_phase_restores_spawn_readiness_gate(self) -> None:
        self.assertEqual(len(self.explorer.nodes_by_handle), 10)
        self.assertEqual(len(self.explorer.edges_by_handle), 10)
        self.assertEqual(
            {quest_id: node.short_type for quest_id, node in self.nodes_by_id.items()},
            {
                "0": "Input",
                "1": "Output",
                "10": "SpawnManager",
                "100": "PauseCondition",
                "44": "Checkpoint",
                "256": "PauseCondition",
                "11": "Scene",
                "300": "Journal",
                "301": "MappinManager",
                "302": "FactsDBManager",
            },
        )

        edge_flow = {
            (
                self.explorer.nodes_by_handle[edge.source_node].quest_id,
                edge.source_socket_name,
                self.explorer.nodes_by_handle[edge.destination_node].quest_id,
                edge.destination_socket_name,
            )
            for edge in self.explorer.edges_by_handle.values()
        }
        self.assertEqual(
            edge_flow,
            {
                ("0", "Out", "10", "In"),
                ("10", "Out", "256", "In"),
                ("256", "Out", "100", "In"),
                ("100", "Out", "44", "In"),
                ("44", "Out", "11", "start"),
                ("11", "end", "1", "In"),
                ("11", "job_accept", "300", "Succeeded"),
                ("300", "Out", "301", "Inactive"),
                ("301", "Out", "302", "In"),
                ("302", "Out", "1", "In"),
            },
        )

    def test_meeting_phase_activates_and_waits_for_the_same_community(self) -> None:
        spawn = self.explorer.node_data_by_handle[self.nodes_by_id["10"].handle]
        spawn_action = spawn["actions"][0]["type"]["Data"]
        spawned_condition = self.explorer.node_data_by_handle[self.nodes_by_id["256"].handle]["condition"]["Data"]["type"]["Data"]

        self.assertEqual(spawn_action["action"], "Activate")
        self.assertEqual(spawn_action["communityEntryName"]["$value"], "patch")
        self.assertEqual(spawn_action["communityEntryPhaseName"]["$value"], "default")
        self.assertEqual(spawn_action["spawnerReference"]["$value"], "#gq000_01_com_patch_bridge")
        self.assertEqual(spawned_condition["$type"], "questCharacterSpawned_ConditionType")
        self.assertEqual(spawned_condition["objectRef"]["reference"]["$value"], "#gq000_01_com_patch_bridge")

    def test_meeting_phase_handle_refs_are_backward_resolvable(self) -> None:
        path = ROOT / "source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        seen: set[str] = set()
        unresolved: list[str] = []

        def walk(value: object) -> None:
            if isinstance(value, dict):
                if "HandleId" in value:
                    seen.add(str(value["HandleId"]))
                if "HandleRefId" in value and str(value["HandleRefId"]) not in seen:
                    unresolved.append(str(value["HandleRefId"]))
                for child in value.values():
                    walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)

        walk(document)

        self.assertEqual(unresolved, [])


if __name__ == "__main__":
    unittest.main()
