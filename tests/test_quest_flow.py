"""Composition checks exercise malformed routing and independent graph evidence."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import quest_compiler as compiler
from phase_graph import (
    PhaseGraphBuilder,
    cname,
    fact_node,
    input_node,
    output_node,
    phase_document,
)
from quest_flow import (
    validate_flow,
    validate_phase_ports,
    validate_emitted_contract,
    stage_transitions,
    walk,
)
from quest_types import CompiledStage, ParallelGroup, QuestSpec, QuestSpecError


def stage(identifier, **fields):
    data = {
        "id": identifier,
        "type": "time_gate",
        "phase_resource": rf"mod\flow\{identifier}.questphase",
        "duration_seconds": 1,
        **fields,
    }
    return CompiledStage(
        0, identifier, data["type"], "ready", data["phase_resource"], data
    )


def spec(*stages, **fields):
    from dataclasses import replace

    return QuestSpec(
        Path("manifest.json"),
        "flow",
        "Flow",
        "",
        (),
        (),
        None,
        tuple(replace(value, index=index) for index, value in enumerate(stages)),
        **fields,
    )


class QuestFlowTests(unittest.TestCase):
    def codes(self, value):
        return {item.code for item in validate_flow(value)}

    def test_debug_fact_uses_boolean_exact_flag_and_integer_step(self):
        builder = PhaseGraphBuilder()
        operation = compiler.debug_step_node(builder, 20, "debug_step", 30).data[
            "type"
        ]["Data"]
        self.assertEqual(operation["setExactValue"], 1)
        self.assertEqual(operation["value"], 30)

    def test_legacy_linear_routes_remain_concise(self):
        value = spec(stage("one"), stage("two"))
        self.assertEqual(
            stage_transitions(value),
            {"one": {"success": "two"}, "two": {"success": "$end"}},
        )
        self.assertEqual(validate_flow(value), [])

    def test_failure_requires_explicit_route(self):
        self.assertIn(
            "unhandled_outcome",
            self.codes(
                spec(stage("one", outcomes={"success": "Out1", "failure": "Failed"}))
            ),
        )

    def test_unknown_target_and_outcome_are_rejected(self):
        self.assertEqual(
            self.codes(spec(stage("one", on={"misspelled": "missing"}))),
            {"unhandled_outcome", "unknown_outcome", "unknown_transition"},
        )

    def test_unreachable_stage_is_rejected(self):
        self.assertIn(
            "unreachable_stage",
            self.codes(spec(stage("one", on={"success": "$end"}), stage("two"))),
        )

    def test_retry_loop_requires_possible_exit(self):
        self.assertIn(
            "nonterminating_flow", self.codes(spec(stage("one", on={"success": "one"})))
        )
        valid = spec(
            stage(
                "one",
                outcomes={"success": "Out1", "failure": "Failed"},
                on={"success": "$end", "failure": "one"},
            )
        )
        self.assertEqual(validate_flow(valid), [])

    def test_fact_writer_must_precede_reader_on_every_branch(self):
        value = spec(
            stage(
                "choose",
                outcomes={"success": "Out1", "failure": "Failed"},
                on={"success": "writer", "failure": "reader"},
            ),
            stage("writer", contract={"writes_facts": ["key"]}),
            stage("reader", contract={"reads_facts": ["key"]}),
        )
        self.assertIn("missing_fact_producer", self.codes(value))
        self.assertEqual(
            validate_flow(spec(*value.stages, external_facts=("key",))), []
        )

    def test_later_loop_writer_does_not_satisfy_first_entry_read(self):
        value = spec(
            stage("reader", contract={"reads_facts": ["key"]}),
            stage(
                "writer",
                contract={"writes_facts": ["key"]},
                outcomes={"success": "Out1", "again": "Again"},
                on={"success": "$end", "again": "reader"},
            ),
        )
        self.assertIn("missing_fact_producer", self.codes(value))

    def test_external_event_requires_quest_declaration(self):
        value = stage("one", contract={"external_events": ["device.opened"]})
        self.assertIn("undeclared_external_event", self.codes(spec(value)))
        self.assertEqual(
            validate_flow(spec(value, external_events=("device.opened",))), []
        )

    def test_actor_retention_requires_matching_owner_and_cleanup(self):
        common = {"community": "#escort", "entry": "target"}
        escort = stage(
            "escort",
            type="escort_npc",
            **common,
            actor_lifecycle={"on_success": "retain"},
        )
        defend = stage(
            "defend",
            type="defend_target",
            **common,
            actor_lifecycle={"on_enter": "retain"},
        )
        self.assertEqual(validate_flow(spec(escort, defend)), [])
        self.assertIn("ownership_not_acquired", self.codes(spec(defend)))
        self.assertIn("ownership_leak", self.codes(spec(escort)))

    def test_failure_path_cannot_retain_actor_without_owner(self):
        value = stage(
            "escort",
            type="escort_npc",
            community="#escort",
            entry="target",
            actor_lifecycle={"on_failure": "retain"},
            outcomes={"success": "Out1", "failure": "Failed"},
            on={"success": "$end", "failure": "$end"},
        )
        self.assertIn("ownership_leak", self.codes(spec(value)))

    def test_renaming_success_cannot_hide_a_lifecycle_leak(self):
        value = stage(
            "escort",
            type="escort_npc",
            community="#escort",
            entry="target",
            actor_lifecycle={"on_success": "retain"},
            outcomes={"done": "Out1"},
            on={"done": "$end"},
        )
        self.assertIn("ambiguous_lifecycle_outcome", self.codes(spec(value)))

    def test_parallel_contracts_check_reads_then_union_writes_at_join(self):
        from dataclasses import replace

        value = spec(
            stage("one", contract={"writes_facts": ["a"]}),
            stage("two", contract={"reads_facts": ["a"], "writes_facts": ["b"]}),
            stage("after", contract={"reads_facts": ["a", "b"]}),
        )
        value = replace(
            value, parallel_groups=(ParallelGroup("both", (("one",), ("two",))),)
        )
        self.assertIn("missing_fact_producer", self.codes(value))
        valid_two = stage("two", contract={"writes_facts": ["b"]})
        valid = replace(
            spec(value.stages[0], valid_two, value.stages[2]),
            parallel_groups=value.parallel_groups,
        )
        self.assertEqual(validate_flow(valid), [])

    def test_parallel_does_not_skip_terminal_ownership_cleanup(self):
        from dataclasses import replace

        value = spec(
            stage(
                "escort",
                type="escort_npc",
                community="#escort",
                entry="target",
                actor_lifecycle={"on_success": "retain"},
            ),
            stage("other"),
        )
        value = replace(
            value, parallel_groups=(ParallelGroup("both", (("escort",), ("other",))),)
        )
        self.assertIn("ownership_leak", self.codes(value))

    def test_emitted_phase_must_have_declared_outcome(self):
        builder = PhaseGraphBuilder()
        begin, end = input_node(builder), output_node(builder)
        builder.connect_to_earlier_output(begin, end)
        phase = phase_document(builder, Path("phase.questphase"))
        with self.assertRaisesRegex(QuestSpecError, "missing output ports"):
            validate_phase_ports(stage("one", outcomes={"failure": "Failure"}), phase)

    def test_unused_phase_input_cannot_prove_output_reachable_from_start(self):
        builder = PhaseGraphBuilder()
        input_node(builder)
        end = output_node(builder)
        extra = builder.node(
            2,
            "questInputNodeDefinition",
            input_names=(),
            properties={"socketName": cname("Unused")},
        )
        builder.connect_to_earlier_output(extra, end)
        with self.assertRaisesRegex(QuestSpecError, "unreachable output"):
            validate_phase_ports(
                stage("one"), phase_document(builder, Path("phase.questphase"))
            )

    def test_matching_text_does_not_prove_fact_writer(self):
        value = stage("one", contract={"writes_facts": ["done"]})
        with self.assertRaisesRegex(QuestSpecError, "typed fact nodes"):
            validate_emitted_contract(value, {"notes": "done"})
        builder = PhaseGraphBuilder()
        fact_node(builder, 2, "done")
        validate_emitted_contract(
            value, phase_document(builder, Path("phase.questphase"))
        )

    def test_conditional_write_cannot_claim_unconditional_dependency(self):
        value = stage("one", contract={"writes_facts": ["done"]})
        builder = PhaseGraphBuilder()
        begin, end = input_node(builder), output_node(builder)
        done = fact_node(builder, 2, "done")
        builder.connect(begin, done)
        builder.connect_to_earlier_output(done, end)
        builder.connect_to_earlier_output(begin, end)
        with self.assertRaisesRegex(QuestSpecError, "only some outcome paths"):
            validate_emitted_contract(
                value, phase_document(builder, Path("phase.questphase"))
            )

    def test_explicit_graph_wires_failure_back_to_checkpoint_without_forward_handles(
        self,
    ):
        value = spec(
            stage("first", checkpoint="checkpoint", retry_checkpoint=True),
            stage(
                "second",
                outcomes={"success": "Out1", "failure": "Failure"},
                on={"success": "$end", "failure": "first"},
            ),
        )
        phase = compiler.build_orchestration_phase(value, Path("quest.questphase"))
        compiler.validate_handle_graph(phase, context="branch graph")
        compiler.validate_no_forward_handle_refs(phase, context="branch graph")
        nodes = [
            node
            for node in walk(phase)
            if node.get("$type") == "questPhaseNodeDefinition"
        ]
        self.assertEqual(len(nodes), 2)
        definitions = {
            str(item["HandleId"]): item["Data"]
            for item in walk(phase)
            if "HandleId" in item
        }
        sockets = {
            definitions[str(socket.get("HandleId", socket.get("HandleRefId")))]
            .get("name", {})
            .get("$value")
            for socket in nodes[1]["sockets"]
        }
        self.assertIn("Failure", sockets)

    def test_malformed_ports_report_diagnostic_instead_of_exception(self):
        raw = {
            "schema_version": 1,
            "id": "example",
            "title": "Example",
            "stages": [stage("one", outcomes=["wrong"]).data],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(raw))
            loaded, diagnostics = compiler.load_spec(path)
        self.assertIsNone(loaded)
        self.assertIn("invalid_ports", {item.code for item in diagnostics})

    def test_plan_distinguishes_buildability_from_runtime_evidence(self):
        plan = compiler.build_plan(spec(stage("one")), iter(()))
        self.assertTrue(plan["buildable"])
        self.assertFalse(plan["runtime_verified"])
        self.assertEqual(plan["entry_stage"], "one")

    def test_terminal_outcomes_use_real_quest_journal_states(self):
        value = spec(
            stage(
                "one",
                outcomes={"success": "Out1", "failure": "Failure"},
                on={"success": "$end", "failure": "$end"},
            ),
            completion={
                "quest_path": "quests/minor_quest/example",
                "outcomes": {
                    "success": {"state": "Succeeded", "fact": "done"},
                    "failure": {"state": "Failed"},
                },
            },
        )
        phase = compiler.build_orchestration_phase(value, Path("quest.questphase"))
        compiler.validate_no_forward_handle_refs(phase, context="terminal journal")
        self.assertEqual(
            sum(
                node.get("$type") == "questJournalQuestEntry_NodeType"
                for node in walk(phase)
            ),
            2,
        )

    def test_existing_braindance_handoff_uses_manifest_policy(self):
        value, diagnostics = compiler.load_spec(
            ROOT / "projects/test-quests/gqt005/gqt005_braindance_analysis.quest.json"
        )
        self.assertIsNotNone(value, diagnostics)
        meeting = next(item for item in value.stages if item.id == "meet_patch")
        self.assertEqual(meeting.data["objective_lifecycle"]["on_success"], "retain")
        child = compiler.build_stage_phase(meeting, Path("meeting.questphase"))
        compiler.validate_handle_graph(child, context="retained objective")
        compiler.validate_no_forward_handle_refs(child, context="retained objective")

    def test_gqt003_routing_scenarios_use_real_compiler_plan(self):
        from quest_scenarios import run_scenarios

        value, diagnostics = compiler.load_spec(
            ROOT / "projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json"
        )
        self.assertIsNotNone(value, diagnostics)
        scenarios = json.loads(
            (ROOT / "projects/test-quests/scenarios/gqt003.scenarios.json").read_text()
        )
        report = run_scenarios(compiler.build_plan(value, diagnostics), scenarios)
        self.assertTrue(report["passed"], report)


if __name__ == "__main__":
    unittest.main()
