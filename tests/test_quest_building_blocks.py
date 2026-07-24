from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "quest_compiler_building_blocks", ROOT / "tools/quest_compiler.py"
)
assert SPEC and SPEC.loader
quest_compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = quest_compiler
SPEC.loader.exec_module(quest_compiler)


TEMPLATE = r"mod\gq000\phases\gq000_post_accept.questphase"
PHASE_PREFIX = r"mod\gq_blocks\phases"
OBJECTIVE = "quests/minor_quest/gq_blocks/gq_blocks_01/obj"
DESCRIPTION = f"{OBJECTIVE}/desc"
MAPPIN = f"{OBJECTIVE}/qmp"


def stage(stage_type: str) -> dict:
    common = {
        "id": f"test_{stage_type}",
        "type": stage_type,
        "status": "planned",
        "phase_resource": f"{PHASE_PREFIX}\\{stage_type}.questphase",
    }
    values = {
        "reach_area": {
            "trigger": "#test_reach",
            "objective": OBJECTIVE,
            "description_entry": DESCRIPTION,
            "mappin": MAPPIN,
        },
        "interact_device": {
            "phase_template": TEMPLATE,
            "device": "#test_device",
            "controller_class": "AccessPointController",
            "action": "Extract",
            "completion_function": "OnExtracted",
        },
        "acquire_item": {
            "item": "Items.test_item",
            "source": "inventory",
            # The direct generator currently needs this schema-optional field.
            "objective": OBJECTIVE,
        },
        "combat_encounter": {
            "phase_template": TEMPLATE,
            "community": "#test_community",
            "hostility": "already_hostile",
            "completion": "all_defeated",
        },
        "leave_area": {
            "trigger": "#test_leave",
            "objective": OBJECTIVE,
            "description_entry": DESCRIPTION,
        },
        "read_shard": {
            "item": "Items.test_shard",
            "journal_entry": "onscreens/shards/test_shard",
            "file_entry_index": 1,
            "acquisition_fact": "test_shard_acquired",
            "presentation_delay_seconds": 3,
        },
        "investigate_clues": {
            "phase_template": TEMPLATE,
            "objective": OBJECTIVE,
            "description_entry": DESCRIPTION,
            "clues": [{"id": "clue_a", "object_ref": "#test_clue"}],
        },
        "optional_condition": {
            "phase_template": TEMPLATE,
            "objective": OBJECTIVE,
            "condition": {"kind": "fact", "value": "test_condition"},
            "success_fact": "test_optional_success",
            "failure_fact": "test_optional_failure",
            "evaluation": "at_exit",
        },
        "choice_gate": {
            "phase_template": TEMPLATE,
            "gate_kind": "fact",
            "branches": [
                {"id": "left", "condition": "test_left", "set_fact": "test_chose_left"},
                {"id": "right", "condition": "test_right", "set_fact": "test_chose_right"},
            ],
            "join": True,
        },
        "escort_npc": {
            "phase_template": TEMPLATE,
            "community": "#test_community",
            "entry": "escort",
            "destinations": ["#test_destination_a", "#test_destination_b"],
            "objective": OBJECTIVE,
        },
        "carry_npc": {
            "phase_template": TEMPLATE,
            "community": "#test_community",
            "entry": "carried",
            "destination": "#test_destination",
            "objective": OBJECTIVE,
        },
        "deliver_vehicle": {
            "phase_template": TEMPLATE,
            "vehicle": "#test_vehicle",
            "destination": "#test_destination",
            "objective": OBJECTIVE,
        },
    }
    common.update(values[stage_type])
    return common


BUILDING_BLOCK_TYPES = tuple(
    name
    for name in (
        "reach_area",
        "interact_device",
        "acquire_item",
        "combat_encounter",
        "leave_area",
        "read_shard",
        "investigate_clues",
        "optional_condition",
        "choice_gate",
        "escort_npc",
        "carry_npc",
        "deliver_vehicle",
    )
)


class QuestBuildingBlockTests(unittest.TestCase):
    def write_manifest(self, root: Path, stages: list[dict]) -> Path:
        path = root / "quest.json"
        path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "id": "gq_blocks",
                    "title": "Building block acceptance",
                    "stages": stages,
                }
            ),
            encoding="utf-8",
        )
        return path

    def load(self, stages: list[dict]):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        return quest_compiler.load_spec(
            self.write_manifest(Path(temporary.name), stages)
        )

    def test_all_twelve_minimal_manifests_validate(self) -> None:
        for stage_type in BUILDING_BLOCK_TYPES:
            with self.subTest(stage_type=stage_type):
                spec, diagnostics = self.load([stage(stage_type)])
                self.assertIsNotNone(
                    spec,
                    [diagnostic.as_dict() for diagnostic in diagnostics],
                )
                self.assertFalse(
                    [item for item in diagnostics if item.level == "error"]
                )

    def test_stage_fields_are_strictly_type_specific(self) -> None:
        for stage_type in BUILDING_BLOCK_TYPES:
            value = stage(stage_type)
            value["accepted_fact"] = "field_from_phone_offer"
            with self.subTest(stage_type=stage_type):
                spec, diagnostics = self.load([value])
                self.assertIsNone(spec)
                self.assertIn(
                    "unknown_stage_field",
                    {item.code for item in diagnostics},
                )

    def test_complex_blocks_resolve_builtin_templates(self) -> None:
        for stage_type in sorted(quest_compiler.TEMPLATE_REQUIRED_STAGE_TYPES):
            value = stage(stage_type)
            del value["phase_template"]
            with self.subTest(stage_type=stage_type):
                spec, diagnostics = self.load([value])
                self.assertIsNotNone(
                    spec,
                    [diagnostic.as_dict() for diagnostic in diagnostics],
                )
                assert spec is not None
                self.assertEqual(
                    quest_compiler.stage_template_resource(spec.stages[0]),
                    quest_compiler.BUILTIN_TEMPLATE_RESOURCES[stage_type],
                )

    def test_builtin_templates_reject_fields_their_graph_does_not_implement(
        self,
    ) -> None:
        value = stage("deliver_vehicle")
        del value["phase_template"]
        value["require_player_exit"] = True
        spec, diagnostics = self.load([value])
        self.assertIsNone(spec)
        self.assertIn(
            "unsupported_builtin_fields",
            {diagnostic.code for diagnostic in diagnostics},
        )

        value["phase_template"] = TEMPLATE
        spec, diagnostics = self.load([value])
        self.assertIsNotNone(
            spec,
            [diagnostic.as_dict() for diagnostic in diagnostics],
        )

    def test_schema_and_compiler_stage_type_enums_match(self) -> None:
        schema = json.loads(
            (ROOT / "tools/quest-schema-v1.json").read_text(encoding="utf-8")
        )
        schema_types = set(
            schema["$defs"]["baseStage"]["properties"]["type"]["enum"]
        )
        self.assertEqual(schema_types, quest_compiler.SUPPORTED_STAGE_TYPES)

    def test_all_twelve_minimal_manifests_match_json_schema(self) -> None:
        schema = json.loads(
            (ROOT / "tools/quest-schema-v1.json").read_text(encoding="utf-8")
        )
        for stage_type in BUILDING_BLOCK_TYPES:
            manifest = {
                "schema_version": 1,
                "id": "gq_blocks",
                "title": "Building block acceptance",
                "stages": [stage(stage_type)],
            }
            with self.subTest(stage_type=stage_type):
                jsonschema.Draft202012Validator(schema).validate(manifest)

    def test_builtin_template_acceptance_manifest_compiles_all_eight_children(
        self,
    ) -> None:
        manifest = (
            ROOT
            / "source/quests/examples/template_building_blocks.quest.json"
        )
        spec, diagnostics = quest_compiler.load_spec(manifest)
        self.assertIsNotNone(
            spec,
            [diagnostic.as_dict() for diagnostic in diagnostics],
        )
        assert spec is not None
        self.assertEqual(len(spec.stages), 8)
        for stage_value in spec.stages:
            child = quest_compiler.build_stage_phase(
                stage_value,
                ROOT
                / "source/archive/mod/gq_blocks_template/phases"
                / f"{stage_value.id}.questphase",
            )
            encoded = json.dumps(child)
            self.assertNotIn("{{", encoded)
            quest_compiler.validate_handle_graph(
                child, context=stage_value.id
            )

    def test_reach_area_direct_generator_is_deterministic_and_complete(self) -> None:
        self.assert_direct_phase(
            "reach_area",
            ("questTriggerCondition", "#test_reach", OBJECTIVE, MAPPIN),
        )

    def test_leave_area_direct_generator_is_deterministic_and_complete(self) -> None:
        self.assert_direct_phase(
            "leave_area",
            ("questTriggerCondition", "#test_leave", OBJECTIVE, DESCRIPTION),
        )

    def test_acquire_item_inventory_waits_without_granting(self) -> None:
        value = stage("acquire_item")
        phase = self.build_direct(copy.deepcopy(value))
        self.assertEqual(
            json.dumps(phase, sort_keys=True),
            json.dumps(self.build_direct(copy.deepcopy(value)), sort_keys=True),
        )
        encoded = json.dumps(phase, sort_keys=True)
        self.assertIn("questInventory_ConditionType", encoded)
        self.assertIn("Items.test_item", encoded)
        self.assertNotIn("questAddRemoveItem_NodeType", encoded)

    def test_acquire_item_grant_adds_then_waits_for_inventory(self) -> None:
        value = stage("acquire_item")
        value.update({"source": "grant", "quantity": 2})
        phase = self.build_direct(copy.deepcopy(value))
        self.assertEqual(
            json.dumps(phase, sort_keys=True),
            json.dumps(self.build_direct(copy.deepcopy(value)), sort_keys=True),
        )
        encoded = json.dumps(phase, sort_keys=True)
        self.assertIn("questAddRemoveItem_NodeType", encoded)
        self.assertIn("questInventory_ConditionType", encoded)
        self.assertIn("Items.test_item", encoded)

    def test_read_shard_direct_generator_is_deterministic_and_complete(self) -> None:
        self.assert_direct_phase(
            "read_shard",
            (
                "questFactsDBCondition",
                "test_shard_acquired",
                "questRealtimeDelay_ConditionType",
            ),
        )

    def test_investigate_clues_generates_variable_ordered_scan_flow(self) -> None:
        value = stage("investigate_clues")
        value.pop("phase_template")
        value.update(
            {
                "clues": [
                    {
                        "id": "relay",
                        "object_ref": "#test_clue_relay",
                        "completion_fact": "test_clue_relay_scanned",
                    },
                    {
                        "id": "medical",
                        "object_ref": "#test_clue_medical",
                        "journal_entry": "onscreens/emails/quests/minor_quest/test/shards/medical",
                    },
                    {
                        "id": "backup",
                        "object_ref": "#test_clue_backup",
                        "mappin": MAPPIN,
                    },
                ],
                "required_count": 3,
                "completion_fact": "test_investigation_complete",
            }
        )
        phase = self.build_direct(copy.deepcopy(value))
        encoded = json.dumps(phase, sort_keys=True)
        self.assertEqual(encoded.count("questScan_ConditionType"), 3)
        self.assertNotIn("SetDefaultHighlightEvent", encoded)
        for expected in (
            "#test_clue_relay",
            "#test_clue_medical",
            "#test_clue_backup",
            "test_clue_relay_scanned",
            "test_investigation_complete",
        ):
            self.assertIn(expected, encoded)

    def test_investigate_clues_rejects_partial_generated_threshold(self) -> None:
        value = stage("investigate_clues")
        value.pop("phase_template")
        value["clues"].append({"id": "clue_b", "object_ref": "#test_clue_b"})
        value["required_count"] = 1
        spec, diagnostics = self.load([value])
        self.assertIsNone(spec)
        self.assertIn(
            "unsupported_clue_threshold",
            {diagnostic.code for diagnostic in diagnostics},
        )

    def test_leave_area_can_deactivate_a_community(self) -> None:
        value = stage("leave_area")
        value["cleanup_community"] = "#test_community"
        encoded = json.dumps(self.build_direct(value), sort_keys=True)
        self.assertIn("questSpawnManagerNodeDefinition", encoded)
        self.assertIn("#test_community", encoded)
        self.assertIn('"action": "Deactivate"', encoded)

    def test_direct_generators_emit_valid_handle_graphs(self) -> None:
        for stage_type in (
            "reach_area",
            "leave_area",
            "acquire_item",
            "read_shard",
            "investigate_clues",
        ):
            with self.subTest(stage_type=stage_type):
                value = stage(stage_type)
                value.pop("phase_template", None)
                phase = self.build_direct(value)
                quest_compiler.validate_handle_graph(
                    phase, context=f"{stage_type} acceptance"
                )

    def test_handle_validation_rejects_duplicate_and_dangling_handles(self) -> None:
        with self.assertRaisesRegex(quest_compiler.QuestSpecError, "duplicate HandleId"):
            quest_compiler.validate_handle_graph(
                [{"HandleId": "1"}, {"HandleId": "1"}],
                context="duplicate",
            )
        with self.assertRaisesRegex(
            quest_compiler.QuestSpecError, "unresolved HandleRefId"
        ):
            quest_compiler.validate_handle_graph(
                {"HandleId": "1", "child": {"HandleRefId": "2"}},
                context="dangling",
            )

    def build_direct(self, value: dict) -> dict:
        spec, diagnostics = self.load([value])
        self.assertIsNotNone(spec, [item.as_dict() for item in diagnostics])
        assert spec is not None
        return quest_compiler.build_stage_phase(
            spec.stages[0],
            ROOT / "source/archive/mod/gq_blocks/phases/test.questphase",
        )

    def assert_direct_phase(
        self, stage_type: str, expected_strings: tuple[str, ...]
    ) -> None:
        value = stage(stage_type)
        first = self.build_direct(copy.deepcopy(value))
        second = self.build_direct(copy.deepcopy(value))
        self.assertEqual(
            json.dumps(first, sort_keys=True),
            json.dumps(second, sort_keys=True),
        )
        encoded = json.dumps(first, sort_keys=True)
        for expected in expected_strings:
            self.assertIn(expected, encoded)


if __name__ == "__main__":
    unittest.main()
