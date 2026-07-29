from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import generate_advanced_quest_block_templates as templates
import quest_compiler


def walk(value):
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


class AdvancedQuestBlockTemplateTests(unittest.TestCase):
    def test_generation_is_deterministic_and_matches_checked_in_raw(self):
        first = templates.generate(write=False)
        second = templates.generate(write=False)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 12)
        for name, document in first.items():
            checked = json.loads(
                (templates.RAW_ROOT / f"{name}.questphase.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(document, checked)
            quest_compiler.validate_handle_graph(document, context=name)
            quest_compiler.validate_no_forward_handle_refs(
                document,
                context=name,
            )

    def test_terminal_document_waits_for_scene_emitted_fact(self):
        document = templates.BUILDERS["read_terminal_document"]()
        types = {
            value["$type"]
            for value in walk(document)
            if isinstance(value, dict) and isinstance(value.get("$type"), str)
        }
        encoded = json.dumps(document)
        self.assertIn("questFactsDBCondition", types)
        self.assertIn(templates.COMPLETION_FACT, encoded)
        self.assertNotIn("questJournalEntryState_ConditionType", types)

    def test_monitors_have_success_and_failure_paths(self):
        for name in ("stealth_monitor", "defend_target"):
            document = templates.BUILDERS[name]()
            types = [
                value["$type"]
                for value in walk(document)
                if isinstance(value, dict) and isinstance(value.get("$type"), str)
            ]
            self.assertIn("questLogicalXorNodeDefinition", types)
            encoded = json.dumps(document)
            self.assertIn(templates.FAILURE_FACT, encoded)

    def test_escort_assigns_and_clears_follower_role(self):
        document = templates.build_escort()
        encoded = json.dumps(document)
        self.assertIn("AIFollowerRole", encoded)
        self.assertIn('"$value": "#player"', encoded)
        self.assertEqual(encoded.count("AIAssignRoleCommandParams"), 1)
        self.assertEqual(encoded.count('"$type": "AIClearRoleCommandParams"'), 1)
        self.assertEqual(encoded.count("questMiscAICommandNode"), 2)
        self.assertEqual(encoded.count("questMappinManagerNodeDefinition"), 6)
        self.assertIn(templates.ESCORT_MAPPIN_1, encoded)
        self.assertIn(templates.ESCORT_MAPPIN_2, encoded)
        self.assertIn(templates.ESCORT_MAPPIN_3, encoded)

    def test_vehicle_family_preserves_vanilla_condition_and_cleanup_shapes(self):
        enter = templates.build_enter_vehicle()
        ride = templates.build_ride_with_contact()
        steal = templates.build_steal_vehicle()
        cleanup = templates.build_vehicle_cleanup()
        self.assertIn("questCharacterMount_ConditionType", json.dumps(enter))
        self.assertEqual(
            json.dumps(ride).count("questCharacterMount_ConditionType"), 2
        )
        self.assertNotIn("questSpawnManagerNodeDefinition", json.dumps(steal))
        self.assertNotIn('"action": "Activate"', json.dumps(steal))
        self.assertIn(templates.VEHICLE_COMMUNITY, json.dumps(steal))
        self.assertIn(templates.VEHICLE_ENTRY, json.dumps(steal))
        self.assertNotIn("questEnablePlayerVehicle_NodeType", json.dumps(cleanup))
        self.assertIn(templates.COMPLETION_FACT, json.dumps(cleanup))

    def test_braindance_template_owns_player_handoff(self):
        document = templates.build_braindance_analysis()
        encoded = json.dumps(document)
        self.assertEqual(encoded.count("questSceneNodeDefinition"), 1)
        self.assertEqual(encoded.count("questTeleportPuppetNodeDefinition"), 2)
        self.assertEqual(encoded.count("questShowWorldNode_NodeType"), 2)
        self.assertEqual(encoded.count("questReplacer_NodeType"), 0)
        self.assertEqual(encoded.count("questSpawnSet_NodeType"), 0)
        self.assertEqual(
            encoded.count("questCharacterSpawned_ConditionType"),
            0,
        )
        self.assertIn("scnWorldMarker", encoded)
        self.assertIn(templates.SCENE, encoded)
        self.assertNotIn("questTriggerCondition", encoded)
        self.assertIn(templates.SCENE_ORIGIN, encoded)
        self.assertIn(templates.PLAYER_ANCHOR, encoded)
        self.assertIn(templates.PLAYER_RETURN, encoded)
        self.assertEqual(
            encoded.count("questJournalNodeDefinition"),
            5,
        )
        self.assertEqual(encoded.count(templates.OBJECTIVE), 5)
        self.assertEqual(
            encoded.count(
                "questJournalQuestObjectiveCounter_NodeType"
            ),
            3,
        )
        self.assertEqual(encoded.count("questFactsDBCondition"), 3)
        self.assertIn("questLogicalAndNodeDefinition", encoded)
        self.assertIn(templates.CLUE_FACT_1, encoded)
        self.assertIn(templates.CLUE_FACT_2, encoded)
        self.assertIn(templates.CLUE_FACT_3, encoded)
        self.assertIn("questEnableBraindanceFinish_NodeType", encoded)
        self.assertNotIn("questSpawnManagerNodeDefinition", encoded)
        self.assertIn('"$value": "complete"', encoded)

        definitions = {
            str(item["HandleId"]): item
            for item in walk(document)
            if isinstance(item, dict)
            and "HandleId" in item
            and isinstance(item.get("Data"), dict)
        }

        def resolve(wrapper):
            handle_id = wrapper.get(
                "HandleId",
                wrapper.get("HandleRefId"),
            )
            return definitions[str(handle_id)]

        graph = document["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
        socket_owners = {}
        for node in graph:
            for wrapper in node["Data"]["sockets"]:
                definition = resolve(wrapper)
                socket_owners[str(definition["HandleId"])] = (
                    node["Data"]["id"],
                    definition["Data"]["name"]["$value"],
                )
        edges = {
            (
                socket_owners[
                    str(
                        resolve(connection["Data"]["source"])[
                            "HandleId"
                        ]
                    )
                ],
                socket_owners[
                    str(
                        resolve(connection["Data"]["destination"])[
                            "HandleId"
                        ]
                    )
                ],
            )
            for connection in (
                item
                for item in walk(document)
                if isinstance(item, dict)
                and item.get("Data", {}).get("$type")
                == "graphGraphConnectionDefinition"
            )
        }
        self.assertTrue(
            {
                ((9, "Out"), (11, "In")),
                ((11, "Out"), (12, "start")),
                ((19, "Out"), (14, "In")),
                ((14, "Out"), (15, "In")),
                ((15, "Out"), (16, "In")),
                ((21, "Out"), (26, "Increment")),
                ((22, "Out"), (27, "Increment")),
                ((23, "Out"), (28, "Increment")),
                ((26, "Out"), (24, "In1")),
                ((27, "Out"), (24, "In2")),
                ((28, "Out"), (24, "In3")),
            }.issubset(edges)
        )
        self.assertFalse(
            any(
                source[0] in {21, 22, 23}
                and destination[0] == 24
                for source, destination in edges
            )
        )


if __name__ == "__main__":
    unittest.main()
