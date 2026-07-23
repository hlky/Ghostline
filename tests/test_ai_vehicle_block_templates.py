from __future__ import annotations

import json
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import generate_ai_vehicle_block_templates as templates
import quest_compiler


FIXTURE = ROOT / "tests/fixtures/quest_blocks/ai_vehicle.quest.json"


def walk(value):
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def data_types(document: dict) -> list[str]:
    return [
        value["$type"]
        for value in walk(document)
        if isinstance(value, dict) and isinstance(value.get("$type"), str)
    ]


def scalars(document: dict) -> set[str]:
    result: set[str] = set()
    for value in walk(document):
        if isinstance(value, str):
            result.add(value)
    return result


class AiVehicleBlockTemplateTests(unittest.TestCase):
    def test_generation_is_deterministic_and_matches_checked_in_raw(self):
        first = templates.generate(write=False)
        second = templates.generate(write=False)
        self.assertEqual(first, second)
        for name, document in first.items():
            checked = json.loads(
                (templates.RAW_ROOT / f"{name}.questphase.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(document, checked)
            quest_compiler.validate_handle_graph(document, context=name)

    def test_escort_uses_named_npc_trigger_gates(self):
        document = templates.build_escort()
        types = data_types(document)
        values = scalars(document)
        self.assertEqual(types.count("questTriggerCondition"), 2)
        self.assertIn(templates.COMMUNITY, values)
        self.assertIn(templates.ENTRY, values)
        self.assertIn(templates.DESTINATION_1, values)
        self.assertIn(templates.DESTINATION_2, values)
        trigger_conditions = [
            value
            for value in walk(document)
            if isinstance(value, dict)
            and value.get("$type") == "questTriggerCondition"
        ]
        self.assertTrue(
            all(condition["isPlayerActivator"] == 0 for condition in trigger_conditions)
        )
        self.assertTrue(
            all(
                condition["activatorRef"]["names"][0]["$value"]
                == templates.ENTRY
                for condition in trigger_conditions
            )
        )

    def test_carry_preserves_vanilla_mount_and_compound_destination_shapes(self):
        document = templates.build_carry()
        types = data_types(document)
        self.assertEqual(types.count("questCharacterMount_ConditionType"), 2)
        self.assertIn("questLogicalCondition", types)
        mount_conditions = [
            value
            for value in walk(document)
            if isinstance(value, dict)
            and value.get("$type") == "questCharacterMount_ConditionType"
        ]
        for condition in mount_conditions:
            self.assertEqual(condition["condition"], "OnMount")
            self.assertEqual(condition["parentIsPlayer"], 1)
            self.assertEqual(condition["childIsPlayer"], 0)
            self.assertEqual(condition["vehicleOrigin"], "Any")
            self.assertEqual(condition["vehicleType"], "Any")
        multi = next(
            value
            for value in walk(document)
            if isinstance(value, dict)
            and value.get("$type") == "questLogicalCondition"
        )
        self.assertEqual(multi["operation"], "AND")
        self.assertEqual(len(multi["conditions"]), 2)

    def test_vehicle_delivery_requires_destination_and_complete_stop(self):
        document = templates.build_deliver_vehicle()
        types = data_types(document)
        self.assertIn("questTriggerCondition", types)
        self.assertIn("questVehicleCondition", types)
        self.assertIn("questVehicleSpeed_ConditionType", types)
        speed = next(
            value
            for value in walk(document)
            if isinstance(value, dict)
            and value.get("$type") == "questVehicleSpeed_ConditionType"
        )
        self.assertEqual(speed["comparisonType"], "CT_EQUAL")
        self.assertEqual(speed["speed"], 0)
        self.assertEqual(
            speed["vehicleRef"]["reference"]["$value"], templates.VEHICLE
        )

    def test_ready_fixture_compiles_and_replaces_every_placeholder(self):
        spec, diagnostics = quest_compiler.load_spec(FIXTURE)
        self.assertIsNotNone(spec)
        self.assertFalse(
            [diagnostic for diagnostic in diagnostics if diagnostic.level == "error"]
        )
        assert spec is not None
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "gq_block_ai_vehicle.questphase.json"
            result = quest_compiler.command_compile(
                Namespace(
                    manifest=FIXTURE,
                    out=output,
                    plan=None,
                    allow_planned=False,
                )
            )
            self.assertEqual(result, 0)
            children = list((Path(temp_dir) / "children").rglob("*.json"))
            self.assertEqual(len(children), 3)
            for child in children:
                document = json.loads(child.read_text(encoding="utf-8"))
                quest_compiler.validate_handle_graph(
                    document, context=child.name
                )
                self.assertFalse(
                    {
                        scalar
                        for scalar in scalars(document)
                        if scalar.startswith("{{") and scalar.endswith("}}")
                    }
                )


if __name__ == "__main__":
    unittest.main()
