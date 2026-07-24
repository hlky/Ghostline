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
        self.assertEqual(len(first), 11)
        for name, document in first.items():
            checked = json.loads(
                (templates.RAW_ROOT / f"{name}.questphase.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(document, checked)
            quest_compiler.validate_handle_graph(document, context=name)

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

    def test_vehicle_family_preserves_vanilla_condition_and_cleanup_shapes(self):
        enter = templates.build_enter_vehicle()
        ride = templates.build_ride_with_contact()
        cleanup = templates.build_vehicle_cleanup()
        self.assertIn("questCharacterMount_ConditionType", json.dumps(enter))
        self.assertEqual(
            json.dumps(ride).count("questCharacterMount_ConditionType"), 2
        )
        self.assertIn("questEnablePlayerVehicle_NodeType", json.dumps(cleanup))


if __name__ == "__main__":
    unittest.main()
