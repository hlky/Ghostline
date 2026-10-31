"""Retained fixtures prove legacy graph parity; scenarios check new options."""

import copy
from dataclasses import replace
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import quest_compiler as compiler
from cr2w_validation import canonical_document
from quest_flow import walk
from quest_generated_blocks import BUILDERS
from quest_types import CompiledStage
from test_quest_building_blocks import stage as example_stage
from quest_scope_model import ScopeRun


class GeneratedQuestBlockTests(unittest.TestCase):
    def run_block(self, kind, **fields):
        value = self.stage(kind, **fields)
        return ScopeRun(
            compiler.build_stage_phase(
                value, ROOT / "generated/tests/scenario.questphase"
            )
        )

    def release(self, run, number):
        """Inject a native predicate acknowledgment; no engine simulation claim."""
        handle = next(key for key, node in run.nodes.items() if node["id"] == number)
        self.assertIn(handle, run.active, number)
        run.active.remove(handle)
        run.emit(handle, "Out")
        run.drain()

    def stage(self, kind, **fields):
        if kind == "meet_contact":
            objective = "quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch"
            data = {
                "id": "gq000_patch_meet",
                "type": kind,
                "phase_resource": r"mod\example\meeting.questphase",
                "contact": "patch",
                "community": "#gq000_01_com_patch_bridge",
                "scene": r"mod\gq000\scenes\gq000_patch_meet.scene",
                "objective": objective,
                "description_entry": objective + "/description",
                "mappin": objective + "/gq000_01_qmp_patch_bridge",
                "phase_prefabs": ["#gq000_pr_patch_meet"],
                "setup_trigger": "#gq000_01_tr_setup",
                "scene_origin": "#gq000_01_sm_patch_bridge",
                "accepted_fact": "gq000_job_accepted",
                **fields,
            }
        else:
            data = {**example_stage(kind), **fields}
        data.pop("phase_template", None)
        return CompiledStage(
            0, data["id"], kind, "planned", data["phase_resource"], data
        )

    def test_legacy_graphs_match_retained_fixtures(self):
        for kind in BUILDERS:
            with self.subTest(kind=kind):
                if kind == "deliver_drop_point":
                    continue  # Previously required a quest-specific template.
                value = self.stage(kind)
                if kind == "meet_contact":
                    expected = json.loads(
                        (
                            ROOT
                            / "tests/fixtures/quest_blocks/gq000_meet_contact.questphase.json"
                        ).read_text()
                    )
                    actual = compiler.build_stage_phase(
                        value, ROOT / "generated/tests/generated.questphase"
                    )
                    self.assertEqual(
                        canonical_document(expected), canonical_document(actual)
                    )
                    continue
                fixture = rf"mod\ghostline\quest_blocks\templates\{kind}.questphase"
                if kind == "defend_target" and value.data.get("block_on_failure"):
                    fixture = fixture.replace("defend_target.", "defend_target_retry.")
                expected = compiler.instantiate_stage_phase(
                    replace(value, data={**value.data, "phase_template": fixture}),
                    ROOT / "generated/tests/fixture.questphase",
                )
                actual = compiler.build_stage_phase(
                    value, ROOT / "generated/tests/generated.questphase"
                )
                self.assertEqual(
                    canonical_document(expected), canonical_document(actual)
                )
                self.assertIsNone(compiler.stage_template_resource(value))

    def test_builders_do_not_read_or_mutate_templates_or_inputs(self):
        from unittest.mock import patch

        for kind, builder in BUILDERS.items():
            if kind == "deliver_drop_point":
                continue
            value = self.stage(kind)
            before = copy.deepcopy(value.data)
            with patch.object(
                Path, "read_text", side_effect=AssertionError("template read")
            ):
                document = builder(value, ROOT / "generated/tests/generated.questphase")
            compiler.validate_handle_graph(document, context=kind)
            compiler.validate_no_forward_handle_refs(document, context=kind)
            self.assertNotIn("{{", json.dumps(document))
            self.assertEqual(value.data, before)

    def test_plant_can_retain_item_after_completion(self):
        value = self.stage("plant_item", consume_item=False)
        document = compiler.build_stage_phase(
            value, ROOT / "generated/tests/plant.questphase"
        )
        self.assertFalse(
            any(
                node.get("$type") == "questAddRemoveItem_NodeType"
                for node in walk(document)
            )
        )

    def test_optional_snapshot_and_continuous_legacy_boundaries(self):
        for initial in (0, 1):
            value = self.stage("optional_condition", evaluation="on_entry")
            run = ScopeRun(
                compiler.build_stage_phase(
                    value, ROOT / "generated/tests/condition.questphase"
                ),
                facts={"test_condition": initial},
            )
            self.assertEqual(run.outcomes, ["Out1"])
            self.assertEqual(run.facts.get(value.data["success_fact"], 0), initial)
            self.assertEqual(run.facts.get(value.data["failure_fact"], 0), 1 - initial)

    def test_multiple_detection_facts_and_rescued_entries(self):
        run = self.run_block(
            "stealth_monitor", additional_failure_facts=["alarm_a", "alarm_b"]
        )
        run.events(facts={"alarm_b": 1})
        self.assertEqual(run.outcomes, ["Out1"])
        self.assertNotIn(self.stage("stealth_monitor").data["success_fact"], run.facts)
        rescue = self.run_block(
            "release_or_rescue_npc", additional_entries=["second", "third"]
        )
        for number in (12, 13, 100):
            self.release(rescue, number)
            self.assertFalse(rescue.outcomes)
        self.release(rescue, 101)
        self.assertEqual(rescue.outcomes, ["Out1"])

    def test_drive_and_carry_waypoints_are_ordered_and_completion_is_final(self):
        for kind, initial in [("drive_to", []), ("carry_npc", [11])]:
            run = self.run_block(
                kind, waypoints=["#first", "#second"], completion_fact="delivered"
            )
            for number in [*initial, 100, 101]:
                self.release(run, number)
                self.assertFalse(run.outcomes)
                self.assertNotIn("delivered", run.facts)
            self.release(run, 12)
            self.assertEqual(run.outcomes, ["Out1"])
            self.assertEqual(run.writes("delivered"), 1)

    def test_delivery_requires_arrival_stop_and_explicit_exit(self):
        run = self.run_block(
            "deliver_vehicle", require_player_exit=True, completion_fact="delivered"
        )
        self.release(run, 11)
        self.assertFalse(run.outcomes)
        self.release(run, 12)
        # Unknown/native mounting state is False in this model: already out
        # bypasses an event wait rather than requiring another unmount event.
        self.assertEqual(run.outcomes, ["Out1"])
        self.assertEqual(run.writes("delivered"), 1)
        moving = self.run_block("deliver_vehicle", require_stop=False)
        self.release(moving, 11)
        self.assertEqual(moving.outcomes, ["Out1"])

    def test_passengers_join_in_both_event_orders(self):
        from itertools import permutations

        passengers = [
            {"community": "#contacts", "entry": "second", "slot": "seat_back_left"},
            {"community": "#contacts", "entry": "third", "slot": "seat_back_right"},
        ]
        for order in permutations((12, 13, 1001, 1003)):
            run = self.run_block("ride_with_contact", additional_passengers=passengers)
            for index, number in enumerate(order):
                self.release(run, number)
                self.assertEqual(bool(run.outcomes), index == 3)

    def test_braindance_variable_clues_and_early_exit_restore_without_false_commit(
        self,
    ):
        for count in (1, 2, 3, 5):
            facts = [f"clue_{i}" for i in range(count)]
            for order in (facts, list(reversed(facts))):
                value = self.stage("braindance_analysis", clue_facts=facts)
                run = ScopeRun(
                    compiler.build_stage_phase(
                        value, ROOT / "generated/tests/bd.questphase"
                    )
                )
                for index, fact in enumerate(order):
                    run.events(facts={fact: 1})
                    self.assertEqual(
                        bool(run.facts.get(value.data["completion_fact"])),
                        index == count - 1,
                    )
                self.assertFalse(run.outcomes)
                run.resource(value.data["scene"], "complete")
                run.events(timer=True)
                self.assertFalse(run.outcomes)
                run.events(timer=True)
                self.assertEqual(run.outcomes, ["Out1"])
            early = self.run_block("braindance_analysis", clue_facts=facts)
            early.resource(self.stage("braindance_analysis").data["scene"], "end")
            early.events(timer=True)
            early.events(timer=True)
            self.assertEqual(early.outcomes, ["Out1"])
            self.assertNotIn(
                self.stage("braindance_analysis").data["completion_fact"], early.facts
            )

    def test_meeting_defer_rearms_without_acceptance_and_keeps_spawn_owned(self):
        value = self.stage(
            "meet_contact", defer_policy="rearm", rearm_trigger="#outside"
        )
        run = ScopeRun(
            compiler.build_stage_phase(
                value, ROOT / "generated/tests/meeting.questphase"
            )
        )
        self.release(run, 256)
        self.release(run, 100)
        run.resource(value.data["scene"], "end")
        self.assertFalse(run.outcomes)
        self.assertNotIn(value.data["accepted_fact"], run.facts)
        self.release(run, 303)
        self.release(run, 100)
        run.resource(value.data["scene"], "job_accept")
        self.assertEqual(run.outcomes, ["Out1"])
        self.assertEqual(run.writes(value.data["accepted_fact"]), 1)

    def test_retry_defense_and_explicit_memory_template_are_preserved(self):
        value = self.stage("defend_target", block_on_failure=True)
        legacy = replace(
            value,
            data={
                **value.data,
                "phase_template": r"mod\ghostline\quest_blocks\templates\defend_target_retry.questphase",
            },
        )
        expected = compiler.instantiate_stage_phase(
            legacy, ROOT / "generated/tests/retry.questphase"
        )
        actual = compiler.build_stage_phase(
            value, ROOT / "generated/tests/retry.questphase"
        )
        self.assertEqual(canonical_document(expected), canonical_document(actual))
        document = compiler.read_json(
            compiler.resource_paths(legacy.data["phase_template"])[0]
        )
        from unittest.mock import patch

        with patch.dict(
            compiler.STAGE_BUILDERS,
            {
                compiler.stage_builder_name(value): lambda *args: self.fail(
                    "generator should not run"
                )
            },
        ):
            explicit = compiler.build_stage_phase(
                value,
                ROOT / "generated/tests/retry.questphase",
                template_document=document,
            )
        self.assertEqual(canonical_document(expected), canonical_document(explicit))

    def test_registry_has_no_default_template_dependencies(self):
        from quest_stages import STAGE_REGISTRY

        self.assertEqual(len(STAGE_REGISTRY), 40)
        self.assertTrue(all(entry.builder({}) for entry in STAGE_REGISTRY.values()))
        self.assertTrue(
            all(entry.template({}) is None for entry in STAGE_REGISTRY.values())
        )

    def test_invalid_extended_shapes_report_diagnostics_without_crashing(self):
        from quest_generated_validation import validate_generated

        cases = [
            self.stage(
                "ride_with_contact",
                additional_passengers=[{"community": "#a", "entry": "a", "slot": {}}],
            ),
            self.stage("drive_to", waypoints=[12]),
            self.stage("braindance_analysis", clue_facts=["same", "same"]),
            self.stage("enter_vehicle", inputs=["not_a_mapping"]),
        ]
        for value in cases:
            diagnostics = []
            validate_generated(value.data, "stage", value.id, diagnostics)
            self.assertTrue(diagnostics)

    def test_retained_ui_and_explicit_legacy_binding_selection(self):
        from quest_stages import STAGE_REGISTRY

        run = self.run_block(
            "carry_npc",
            objective_lifecycle={"on_enter": "retain", "on_success": "retain"},
        )
        self.release(run, 11)
        self.release(run, 12)
        self.assertEqual(run.outcomes, ["Out1"])
        self.assertFalse(
            any(node["$type"] == "questJournalNodeDefinition" for node, _ in run.trace)
        )
        value = self.stage("optional_condition")
        bindings = compiler.builtin_template_bindings(value)
        compatible = replace(value, data={**value.data, "template_bindings": bindings})
        self.assertIsNone(STAGE_REGISTRY[value.type].builder(compatible.data))
        generated = compiler.build_stage_phase(
            value, ROOT / "generated/tests/condition.questphase"
        )
        explicit = compiler.build_stage_phase(
            compatible, ROOT / "generated/tests/condition.questphase"
        )
        self.assertEqual(canonical_document(generated), canonical_document(explicit))

    def test_generated_scene_contracts_preserve_legacy_optional_exits(self):
        from quest_interfaces import bound_interfaces, scene_interface

        document = json.loads(
            (
                ROOT
                / "projects/test-quests/gqt005/source/raw/mod/gqt005/scenes/gqt005_braindance_analysis.scene.json"
            ).read_text()
        )
        legacy = self.stage("braindance_analysis")
        _, _, binding = next(bound_interfaces(legacy))
        self.assertFalse(scene_interface(document, **binding))
        explicit = self.stage(
            "braindance_analysis",
            scene_exit_sockets=["misspelled", "Default INT", "Default RET"],
        )
        _, _, binding = next(bound_interfaces(explicit))
        self.assertEqual(binding["exits"], ("misspelled",))
        self.assertTrue(scene_interface(document, **binding))
        meeting = self.stage("meet_contact", accept_exit="accepted", defer_exit="later")
        _, _, binding = next(bound_interfaces(meeting))
        self.assertEqual(binding["exits"], ("accepted", "later"))

    def test_meeting_fixture_matches_frozen_source_identity(self):
        import hashlib

        record = json.loads(
            (
                ROOT / "tests/fixtures/quest_blocks/gq000_meet_contact.provenance.json"
            ).read_text()
        )
        self.assertEqual(
            hashlib.sha256((ROOT / record["fixture"]).read_bytes()).hexdigest(),
            record["fixture_sha256"],
        )


if __name__ == "__main__":
    unittest.main()
