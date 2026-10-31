"""Scenario tests over emitted graphs; engine/save behavior is not simulated."""

import copy
from itertools import permutations
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import quest_compiler as compiler
from quest_interfaces import audit_bound_interfaces, phase_interface, scene_interface
from quest_mechanism_validation import validate_mechanism
from quest_types import CompiledStage
from quest_scope_model import ScopeRun


EXAMPLE = ROOT / "quests/examples/owned-lifecycle-blocks.quest.json"


class OwnedMechanismTests(unittest.TestCase):
    def setUp(self):
        self.examples = {
            data["type"]: data
            for data in json.loads(EXAMPLE.read_text(encoding="utf-8"))["stages"]
        }

    def stage(self, kind, **fields):
        data = {**copy.deepcopy(self.examples[kind]), **fields}
        return CompiledStage(
            0, data["id"], kind, data["status"], data["phase_resource"], data
        )

    def build(self, kind, **fields):
        stage = self.stage(kind, **fields)
        diagnostics = []
        validate_mechanism(stage.data, "stage", stage.id, diagnostics)
        self.assertEqual(diagnostics, [], [d.as_dict() for d in diagnostics])
        return compiler.build_stage_phase(
            stage, ROOT / "generated/tests/mechanism.questphase"
        )

    def test_all_examples_schema_load_and_compile_without_mutation(self):
        from jsonschema import Draft202012Validator
        from quest_stages import SCHEMA

        raw = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        Draft202012Validator(SCHEMA).validate(raw)
        spec, diagnostics = compiler.load_spec(EXAMPLE)
        self.assertIsNotNone(spec, diagnostics)
        self.assertFalse([d for d in diagnostics if d.level == "error"])
        for kind in self.examples:
            with self.subTest(kind=kind):
                before = copy.deepcopy(self.examples[kind])
                self.build(kind)
                self.assertEqual(before, self.examples[kind])

    def test_notifications_are_nonterminal_and_restore_ack_is_final_fence(self):
        doc = self.build("owned_scope")
        run = ScopeRun(doc)
        work = self.examples["owned_scope"]["child"]["phase"]
        restore = self.examples["owned_scope"]["restore"][1]["phase"]
        run.resource(work, "Progress", notification=True)
        self.assertEqual(run.facts["lifecycle_demo_progress"], 1)
        self.assertFalse(run.outcomes)
        run.resource(work)
        self.assertTrue(run.has_resource(restore))
        self.assertNotIn("lifecycle_demo_scope_done", run.facts)
        run.resource(restore)
        self.assertEqual(run.outcomes, ["Out1"])
        self.assertEqual(run.facts["lifecycle_demo_scope_done"], 1)
        replay = ScopeRun(doc, facts=run.facts)
        self.assertEqual(replay.outcomes, ["Out1"])
        self.assertFalse(replay.active)

    def test_cancellation_before_entry_and_during_cleanup(self):
        doc = self.build(
            "owned_scope",
            cancellation_fact="cancel",
            outcomes={"success": "Out1", "cancelled": "Cancelled"},
            effects={"success": [{"kind": "fact", "fact": "success_effect"}]},
        )
        work = self.examples["owned_scope"]["child"]["phase"]
        restore = self.examples["owned_scope"]["restore"][1]["phase"]
        cancelled = ScopeRun(doc, facts={"cancel": 1})
        self.assertFalse(cancelled.has_resource(work))
        self.assertTrue(cancelled.has_resource(restore))
        cancelled.resource(restore)
        self.assertEqual(cancelled.outcomes, ["Cancelled"])
        self.assertNotIn("success_effect", cancelled.facts)
        run = ScopeRun(doc)
        run.resource(work)
        run.events(facts={"cancel": 1})
        self.assertTrue(run.has_resource(restore))
        run.resource(restore)
        self.assertEqual(run.outcomes, ["Out1"])
        self.assertEqual(run.writes("success_effect"), 1)

    def test_cancel_during_asynchronous_setup_retires_setup_child(self):
        setup = r"mod\lifecycle_demo\bindings\setup.questphase"
        doc = self.build(
            "owned_scope",
            cancellation_fact="cancel",
            setup=[{"kind": "phase", "phase": setup, "entry": "In1", "exit": "Out1"}],
            outcomes={"success": "Out1", "cancelled": "Cancelled"},
        )
        run = ScopeRun(doc)
        self.assertTrue(run.has_resource(setup))
        run.events(facts={"cancel": 1})
        self.assertFalse(run.has_resource(setup))
        restore = self.examples["owned_scope"]["restore"][1]["phase"]
        self.assertTrue(run.has_resource(restore))
        run.resource(restore)
        self.assertEqual(run.outcomes, ["Cancelled"])

    def test_queued_competing_outcomes_commit_only_one_route(self):
        doc = self.build("contact_fallback")
        scene = self.examples["contact_fallback"]["call"]["scene"]
        for order in permutations(("connected", "rejected")):
            run = ScopeRun(doc)
            handle = next(key for key in run.active if run.has_resource(scene))
            for socket in order:
                run.emit(handle, socket)
            run.drain()
            self.assertEqual(len(run.outcomes), 1)
            self.assertEqual(
                run.writes("lifecycle_demo_message_delivered")
                + run.writes("lifecycle_demo_connected"),
                1,
            )

    def test_acquisition_existing_and_new_both_require_application(self):
        doc = self.build("acquire_or_use")
        application = self.examples["acquire_or_use"]["application"]["phase"]
        for existing in (False, True):
            with self.subTest(existing=existing):
                run = ScopeRun(doc, items={"Items.money": 1} if existing else {})
                self.assertEqual(run.has_resource(application), existing)
                if not existing:
                    run.events(items={"Items.money": 1})
                self.assertFalse(run.outcomes)
                self.assertEqual(
                    run.facts.get("lifecycle_demo_existing", 0), int(existing)
                )
                self.assertEqual(
                    run.facts.get("lifecycle_demo_acquired", 0), int(not existing)
                )
                run.resource(application)
                self.assertEqual(run.outcomes, ["Out1"])

    def test_alternative_routes_retire_loser_before_shared_application(self):
        doc = self.build("access_routes")
        data = self.examples["access_routes"]
        for winner in range(2):
            run = ScopeRun(doc)
            run.resource(data["routes"][winner]["phase"])
            self.assertFalse(run.has_resource(data["routes"][1 - winner]["phase"]))
            self.assertTrue(run.has_resource(data["application"]["phase"]))
            run.resource(data["application"]["phase"])
            self.assertEqual(run.outcomes, ["Out1"])

    def test_scan_and_reaction_joins_all_event_orders_and_duplicate_scans(self):
        doc = self.build("investigate_reactions")
        clues = self.examples["investigate_reactions"]["clues"]
        for order in permutations(("scan_a", "react_a", "scan_b", "react_b")):
            if order.index("react_a") < order.index("scan_a") or order.index(
                "react_b"
            ) < order.index("scan_b"):
                continue
            run = ScopeRun(doc)
            for index, event in enumerate(order):
                clue = clues[0 if event.endswith("a") else 1]
                if event.startswith("scan"):
                    run.events(scan=clue["object_ref"])
                    run.events(scan=clue["object_ref"])
                else:
                    run.resource(clue["reaction"]["scene"], "end")
                self.assertEqual(bool(run.outcomes), index == 3, order)
            for clue in clues:
                self.assertEqual(run.writes(clue["scan_fact"]), 1)
                self.assertEqual(run.writes(clue["completion_fact"]), 1)

    def test_investigation_resume_bypass_and_cancel_retire_reactions(self):
        data = self.examples["investigate_reactions"]
        doc = self.build(
            "investigate_reactions",
            cancellation_fact="cancel",
            outcomes={"success": "Out1", "cancelled": "Cancelled"},
        )
        first, second = data["clues"]
        run = ScopeRun(doc, facts={first["completion_fact"]: 1, second["scan_fact"]: 1})
        self.assertTrue(run.has_resource(second["reaction"]["scene"]))
        self.assertFalse(run.has_resource(first["reaction"]["scene"]))
        run.events(facts={data["discovery_fact"]: 1})
        self.assertEqual(run.outcomes, ["Out1"])
        self.assertFalse(run.active)
        cancel = ScopeRun(doc)
        cancel.events(scan=first["object_ref"])
        cancel.events(facts={"cancel": 1})
        self.assertEqual(cancel.outcomes, ["Cancelled"])
        self.assertFalse(cancel.active)

    def test_resolution_reporting_and_independent_later_death(self):
        resolver = ScopeRun(self.build("resolve_and_report"))
        observer = ScopeRun(self.build("observe_lethal"))
        resolver.events(targets={"target": "unconscious"})
        self.assertEqual(resolver.facts["lifecycle_demo_resolved"], 1)
        self.assertNotIn("lifecycle_demo_reported", resolver.facts)
        observer.events(targets={"target": "unconscious"})
        self.assertNotIn("lifecycle_demo_killed", observer.facts)
        observer.events(targets={"target": "killed"})
        observer.events(targets={"target": "killed"})
        self.assertEqual(observer.writes("lifecycle_demo_killed"), 1)
        resolver.resource(self.examples["resolve_and_report"]["report"]["phase"])
        self.assertEqual(resolver.facts["lifecycle_demo_reported"], 1)
        self.assertFalse(observer.outcomes)
        observer.events(facts={"lifecycle_demo_observer_stop": 1})
        self.assertEqual(observer.outcomes, ["Out1"])
        closed = ScopeRun(
            self.build("observe_lethal"),
            facts={"lifecycle_demo_observer_stop": 1},
            targets={"target": "killed"},
        )
        self.assertEqual(closed.outcomes, ["Out1"])
        self.assertNotIn("lifecycle_demo_killed", closed.facts)

    def test_reward_commit_verifies_inventory_and_does_not_regrant_after_sale(self):
        doc = self.build("reward_commit")
        for owned in (0, 10):
            run = ScopeRun(doc, items={"Items.money": owned})
            self.assertFalse(run.outcomes)
            run.events(facts={"lifecycle_demo_reported": 1})
            self.assertEqual(run.items["Items.money"], 10)
            # Model emits an inventory condition change on an explicit event.
            run.events()
            self.assertEqual(run.outcomes, ["Out1"])
            replay = ScopeRun(doc, facts=run.facts, items={"Items.money": 0})
            self.assertEqual(replay.items["Items.money"], 0)
            self.assertEqual(replay.outcomes, ["Out1"])

    def test_contact_connected_rejected_muted_busy_and_cancel(self):
        data = self.examples["contact_fallback"]
        for case in ("connected", "rejected", "muted", "busy", "cancel"):
            doc = self.build(
                "contact_fallback",
                cancellation_fact="cancel",
                outcomes={
                    "connected": "Connected",
                    "fallback": "Fallback",
                    "cancelled": "Cancelled",
                },
            )
            facts = (
                {f"lifecycle_demo_{case}": 1}
                if case in {"muted", "busy"}
                else ({"cancel": 1} if case == "cancel" else {})
            )
            run = ScopeRun(doc, facts=facts)
            if case in {"connected", "rejected"}:
                run.resource(data["call"]["scene"], case)
            self.assertEqual(
                run.outcomes,
                [
                    {"connected": "Connected", "cancel": "Cancelled"}.get(
                        case, "Fallback"
                    )
                ],
            )
            self.assertEqual(
                run.writes(data["message_fact"]),
                int(case in {"rejected", "muted", "busy"}),
            )

    def test_timer_profiles_all_choices_deferral_release_timeout_and_cancel(self):
        for choice in (1, 2, 3):
            doc = self.build(
                "adaptive_timer",
                cancellation_fact="cancel",
                outcomes={"success": "Out1", "cancelled": "Cancelled"},
            )
            for busy in (False, True):
                for release in (False, True):
                    run = ScopeRun(
                        doc,
                        random_choice=choice,
                        facts={"lifecycle_demo_reading": int(busy)},
                    )
                    run.events(timer=True)
                    self.assertEqual(bool(run.outcomes), not busy)
                    if busy:
                        run.events(
                            facts={"lifecycle_demo_reading": 0} if release else None,
                            timer=not release,
                        )
                    self.assertEqual(run.outcomes, ["Out1"])
            cancelled = ScopeRun(doc)
            cancelled.events(facts={"cancel": 1}, timer=True)
            self.assertEqual(len(cancelled.outcomes), 1)
            self.assertFalse(cancelled.active)
        hard = ScopeRun(self.build("adaptive_timer"), facts={"lifecycle_demo_hard": 1})
        durations = [
            hard.condition(hard.nodes[key]).get("seconds") for key in hard.active
        ]
        self.assertIn(15, durations)
        self.assertNotIn(25, durations)

    def test_entitlement_retires_offer_without_reward_and_is_repeatable(self):
        doc = self.build("entitlement_reconcile")
        for entitled in (False, True):
            run = ScopeRun(
                doc, facts={"lifecycle_demo_vehicle_entitled": int(entitled)}
            )
            self.assertEqual(run.outcomes, ["Owned" if entitled else "Unowned"])
            self.assertEqual(
                run.facts.get("lifecycle_demo_offer_retired", 0), int(entitled)
            )
            self.assertFalse(run.items)

    def test_invalid_bindings_fail_authoring_validation(self):
        cases = [
            ("reward_commit", {"commit_fact": "bad fact"}),
            ("adaptive_timer", {"max_deferral_seconds": 0}),
            ("adaptive_timer", {"clock": "wall_clock"}),
            ("adaptive_timer", {"choices": [{"seconds": 1, "weight": 256}]}),
            (
                "owned_scope",
                {
                    "child": {
                        "phase": r"mod\..\private.questphase",
                        "entry": "In1",
                        "exits": {"success": "Out1"},
                    }
                },
            ),
            ("owned_scope", {"notifications": {"missing": "fact"}}),
            ("access_routes", {"route_facts": {"missing": "fact"}}),
            ("investigate_reactions", {"required_count": 3}),
            ("owned_scope", {"restore": [{"kind": "item", "item": "Items.money"}]}),
            (
                "entitlement_reconcile",
                {"retire": [{"kind": "message", "path": "offer", "state": "Active"}]},
            ),
        ]
        for kind, fields in cases:
            diagnostics = []
            value = self.stage(kind, **fields)
            validate_mechanism(value.data, "stage", value.id, diagnostics)
            self.assertTrue(diagnostics, (kind, fields))

    def test_child_notification_and_termination_contracts_are_enforced(self):
        from phase_graph import (
            PhaseGraphBuilder,
            input_node,
            output_node,
            phase_document,
        )

        builder = PhaseGraphBuilder()
        start, end = input_node(builder), output_node(builder)
        builder.connect_to_earlier_output(start, end)
        phase = phase_document(builder, Path("child.questphase"))
        self.assertFalse(phase_interface(phase, entry="In1", exits={"success": "Out1"}))
        self.assertTrue(
            phase_interface(phase, entry="Wrong", exits={"success": "Out1"})
        )
        self.assertTrue(
            phase_interface(
                phase, entry="In1", exits={"note": "Out1"}, notifications={"note"}
            )
        )
        end.data["type"] = "NonTerminating"
        self.assertFalse(
            phase_interface(
                phase, entry="In1", exits={"note": "Out1"}, notifications={"note"}
            )
        )
        self.assertTrue(phase_interface(phase, entry="In1", exits={"success": "Out1"}))

    def test_missing_bound_interfaces_are_errors_for_ready_stages(self):
        stage = self.stage("owned_scope", status="ready")

        def missing(_):
            raise FileNotFoundError("no evidence")

        diagnostics = audit_bound_interfaces(stage, missing)
        self.assertTrue(diagnostics)
        self.assertTrue(all(d.level == "error" for d in diagnostics))

    def test_preview_conversion_failure_preserves_previous_publication(self):
        import build_lifecycle_preview as preview

        (ROOT / "generated").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / "generated") as directory:
            output = Path(directory)
            sentinel = output / "source/raw/previous.json"
            sentinel.parent.mkdir(parents=True)
            sentinel.write_text("previous publication", encoding="utf-8")
            with patch.object(
                preview, "convert_batch", side_effect=RuntimeError("bad readback")
            ):
                with self.assertRaisesRegex(RuntimeError, "bad readback"):
                    preview.build(EXAMPLE, output, deserialize=True)
            self.assertEqual(
                sentinel.read_text(encoding="utf-8"), "previous publication"
            )
            self.assertEqual(list((output / "source/raw").rglob("*.json")), [sentinel])
            self.assertFalse((output / "preview-report.json").exists())

    def test_preview_rejects_source_tree_and_reports_planned_binding_gaps(self):
        import build_lifecycle_preview as preview

        with self.assertRaises(ValueError):
            preview.build(EXAMPLE, ROOT / "projects/ghostline/source/raw")
        with tempfile.TemporaryDirectory(dir=ROOT / "generated") as directory:
            report = preview.build(EXAMPLE, Path(directory))
            self.assertEqual(report["artifact_count"], 11)
            self.assertFalse(report["typed_readback"])
            self.assertTrue(report["resource_diagnostics"])
            self.assertTrue(
                all(d["level"] == "warning" for d in report["resource_diagnostics"])
            )
            self.assertTrue(report["source_sha256"])

    def test_scene_entry_is_checked_against_start_node(self):
        scene = {
            "Data": {
                "RootChunk": {
                    "entryPoints": [{"name": {"$value": "start"}, "nodeId": {"id": 1}}],
                    "exitPoints": [{"name": {"$value": "end"}, "nodeId": {"id": 2}}],
                    "sceneGraph": {
                        "nodes": [
                            {"$type": "scnStartNode", "nodeId": {"id": 1}},
                            {"$type": "scnEndNode", "nodeId": {"id": 2}},
                        ]
                    },
                }
            }
        }
        self.assertFalse(scene_interface(scene, entries=["start"], exits=["end"]))
        self.assertTrue(scene_interface(scene, entries=["resume"], exits=["end"]))

    def test_parallel_blocks_cannot_own_the_same_actual_resource(self):
        from test_quest_flow import spec, stage
        from quest_flow import validate_flow
        from quest_types import ParallelGroup

        one = stage(
            "one",
            type="owned_scope",
            restore=[
                {
                    "kind": "prefab_variant",
                    "prefab": "#world",
                    "variant": "default",
                    "show": True,
                }
            ],
        )
        two = stage(
            "two",
            type="owned_scope",
            restore=[
                {
                    "kind": "prefab_variant",
                    "prefab": "#world",
                    "variant": "default",
                    "show": False,
                }
            ],
        )
        from dataclasses import replace

        value = replace(
            spec(one, two),
            parallel_groups=(ParallelGroup("both", (("one",), ("two",))),),
        )
        self.assertIn(
            "parallel_ownership_conflict", {d.code for d in validate_flow(value)}
        )

    def test_native_vehicle_predicate_and_adapter_are_exclusive(self):
        from quest_flow import walk

        value = copy.deepcopy(self.examples["entitlement_reconcile"])
        value.pop("entitled_fact")
        value["vehicle_record"] = "Vehicle.v_standard2_archer_quartz_player"
        stage = CompiledStage(
            0, value["id"], value["type"], "planned", value["phase_resource"], value
        )
        doc = compiler.build_stage_phase(
            stage, ROOT / "generated/tests/native-vehicle.questphase"
        )
        predicate = next(
            x
            for x in walk(doc)
            if x.get("$type") == "questVehicleAvailable_ConditionType"
        )
        self.assertEqual(predicate["vehicleName"], value["vehicle_record"])
        value["entitled_fact"] = "upstream"
        diagnostics = []
        validate_mechanism(value, "stage", stage.id, diagnostics)
        self.assertTrue(diagnostics)


if __name__ == "__main__":
    unittest.main()
