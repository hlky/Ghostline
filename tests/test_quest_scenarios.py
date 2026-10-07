from __future__ import annotations

import contextlib
from copy import deepcopy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import quest_scenarios as scenarios


class QuestScenarioTests(unittest.TestCase):
    def setUp(self):
        self.plan = scenarios.load_plan(
            ROOT / "projects/test-quests/scenarios/contract-routing.plan.json"
        )
        self.suite = json.loads(
            (ROOT / "projects/test-quests/scenarios/contract-routing.scenarios.json").read_text(
                encoding="utf-8"
            )
        )

    def test_checked_in_success_failure_interruption_repeat_and_reload_scenarios(self):
        report = scenarios.run_scenarios(self.plan, self.suite)
        self.assertTrue(report["passed"], report)
        self.assertEqual(len(report["scenarios"]), 5)
        self.assertFalse(report["runtime_verified"])
        outcomes = {
            entry["final_state"]["terminal_outcome"] for entry in report["scenarios"]
        }
        self.assertEqual(outcomes, {"success", "failure", "interrupted"})

    def test_snapshot_survives_json_reordering_and_rejects_changed_contract(self):
        model = scenarios.ScenarioModel(self.plan)
        event = {"event_id": "z-first", "stage": "approach", "outcome": "success"}
        model.signal(event)
        model.signal(
            {"event_id": "a-second", "stage": "encounter", "outcome": "success"}
        )
        snapshot = json.loads(json.dumps(model.snapshot(), sort_keys=True))
        restored = scenarios.ScenarioModel(self.plan)
        restored.restore(snapshot)
        self.assertEqual(restored.state(), model.state())
        self.assertEqual(restored.signal(event)["result"], "duplicate")
        for change in ("route", "port", "contract"):
            with self.subTest(change=change):
                changed = deepcopy(self.plan)
                if change == "route":
                    changed["transitions"]["encounter"]["failure"] = "cleanup"
                elif change == "port":
                    changed["stages"][1]["outcomes"]["failure"] = "DifferentSocket"
                else:
                    changed["contracts"]["encounter"] = {
                        "reads_facts": ["new_requirement"]
                    }
                with self.assertRaisesRegex(scenarios.ScenarioError, "does not match"):
                    scenarios.ScenarioModel(changed).restore(snapshot)

    def test_corrupt_snapshot_does_not_mutate_state(self):
        model = scenarios.ScenarioModel(self.plan)
        original = model.snapshot()
        for mutation in ("position", "journal", "terminal"):
            with self.subTest(mutation=mutation):
                invalid = deepcopy(original)
                if mutation == "position":
                    invalid["active_stage"] = "cleanup"
                elif mutation == "journal":
                    invalid["processed_events"] = [
                        {"event_id": "x", "stage": "approach", "outcome": "unknown"}
                    ]
                else:
                    invalid["active_stage"] = None
                    invalid["terminal_outcome"] = "invented"
                with self.assertRaises(scenarios.ScenarioError):
                    model.restore(invalid)
                self.assertEqual(model.snapshot(), original)

    def test_reusing_event_id_for_different_signal_is_error(self):
        model = scenarios.ScenarioModel(self.plan)
        model.signal({"event_id": "same", "stage": "approach", "outcome": "success"})
        original = model.snapshot()
        with self.assertRaisesRegex(scenarios.ScenarioError, "different content"):
            model.signal(
                {"event_id": "same", "stage": "encounter", "outcome": "failure"}
            )
        self.assertEqual(model.snapshot(), original)

    def test_invalid_graphs_and_parallel_plans_are_not_silently_simulated(self):
        mutations = [
            lambda plan: plan["transitions"]["approach"].update(success="missing"),
            lambda plan: plan["transitions"].pop("cleanup"),
            lambda plan: plan.update(entry_stage="missing"),
            lambda plan: plan["stages"].append(deepcopy(plan["stages"][0])),
            lambda plan: plan["parallel_groups"].append(
                {"id": "parallel", "branches": [["approach"], ["encounter"]]}
            ),
            lambda plan: plan["transitions"]["encounter"].pop("failure"),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                plan = deepcopy(self.plan)
                mutate(plan)
                with self.assertRaises(scenarios.ScenarioError):
                    scenarios.ScenarioModel(plan)

    def test_assertion_failure_and_unknown_event_make_scenario_fail(self):
        for mutation in ("expectation", "outcome", "checkpoint", "missing_expectation"):
            with self.subTest(mutation=mutation):
                suite = deepcopy(self.suite)
                scenario = suite["scenarios"][0]
                if mutation == "expectation":
                    scenario["expect"]["terminal_outcome"] = "failure"
                elif mutation == "outcome":
                    scenario["steps"][0]["event"]["outcome"] = "invented"
                elif mutation == "checkpoint":
                    scenario["steps"].insert(0, {"load": "missing"})
                else:
                    scenario.pop("expect")
                report = scenarios.run_scenarios(self.plan, suite)
                self.assertFalse(report["passed"])
                self.assertFalse(report["scenarios"][0]["passed"])
                self.assertTrue(report["scenarios"][0]["error"])
                self.assertTrue(report["scenarios"][1]["passed"])

    def test_mermaid_uses_safe_node_ids_and_labels(self):
        self.plan["stages"][0]["type"] = 'odd "<script>" type'
        graph = scenarios.graph_markdown(self.plan)
        self.assertIn("stage_0", graph)
        self.assertIn("&lt;script&gt;", graph)
        self.assertNotIn("<script>", graph)
        self.assertIn('stage_1 -->|"failure"| quest_end', graph)

    def test_compiler_plan_can_be_previewed_without_running_game(self):
        plan = scenarios.load_plan(
            ROOT / "quests/examples/direct_building_blocks.quest.json", manifest=True
        )
        model = scenarios.ScenarioModel(plan)
        for index, stage in enumerate(plan["stages"]):
            result = model.signal(
                {"event_id": str(index), "stage": stage["id"], "outcome": "success"}
            )
            self.assertEqual(result["result"], "advanced")
        self.assertEqual(
            model.state(), {"active_stage": None, "terminal_outcome": "success"}
        )

    def test_cli_writes_graph_report_and_nonzero_on_failed_expectation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            suite = deepcopy(self.suite)
            suite["scenarios"][0]["expect"]["terminal_outcome"] = "failure"
            suite_path = root / "scenarios.json"
            suite_path.write_text(json.dumps(suite), encoding="utf-8")
            argv = [
                "quest_scenarios.py",
                "--plan",
                str(ROOT / "projects/test-quests/scenarios/contract-routing.plan.json"),
                "--scenarios",
                str(suite_path),
                "--output",
                str(root / "report.json"),
                "--graph",
                str(root / "graph.md"),
            ]
            with (
                patch.object(sys, "argv", argv),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(scenarios.main(), 1)
            self.assertFalse(json.loads((root / "report.json").read_text())["passed"])
            self.assertIn("```mermaid", (root / "graph.md").read_text())


if __name__ == "__main__":
    unittest.main()
