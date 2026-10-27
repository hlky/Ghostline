from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from quest_types import QuestSpecError
from runtime_job_plan import build_runtime_plan, config_source

JOBS = ROOT / "projects/experiments/npc-runtime/implementation/jobs"


class RuntimeJobPlanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = json.loads((JOBS / "data-theft.quest.json").read_text())
        self.runtime = json.loads((JOBS / "data-theft.runtime.json").read_text())
        self.catalog = json.loads((ROOT / self.runtime["binding"]["catalog"]).read_text())

    def build(self):
        manifest, runtime = self.root / "job.json", self.root / "runtime.json"
        catalog = self.root / self.runtime["binding"]["catalog"]
        catalog.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(json.dumps(self.manifest))
        runtime.write_text(json.dumps(self.runtime))
        catalog.write_text(json.dumps(self.catalog))
        return build_runtime_plan(manifest, runtime, root=self.root)

    def test_extracted_identity_and_timed_interaction(self):
        plan = self.build()
        self.assertEqual([s["type"] for s in plan["stages"]], ["reach_area", "interact_device", "choice_gate"])
        self.assertTrue(plan["target"]["node_ref"].startswith("$/03_night_city/"))
        self.assertEqual(plan["target"]["debug_name"], self.runtime["binding"]["debug_name"])
        self.assertEqual(plan["transfer_duration"], 5)
        self.assertIn("Duration() -> Float = 5.0", config_source(plan))
        self.assertNotIn("WasHackingMinigameSucceeded", config_source(plan))
        self.assertEqual(plan["sha256"], self.build()["sha256"])

    def test_stale_plan_revision_changes_with_target_or_duration(self):
        original = self.build()
        self.runtime["transfer_duration"] = 6
        self.assertNotEqual(original["revision"], self.build()["revision"])

    def test_unsupported_action_is_rejected(self):
        self.manifest["stages"][1]["action"] = "ForceEnabled"
        with self.assertRaises(QuestSpecError): self.build()

    def test_completion_cannot_use_old_breach_flag(self):
        self.manifest["stages"][1]["completion_function"] = "WasHackingMinigameSucceeded"
        with self.assertRaises(QuestSpecError): self.build()

    def test_no_background_device_command(self):
        self.manifest["stages"][1]["send_action"] = True
        with self.assertRaises(QuestSpecError): self.build()

    def test_outcome_facts_cannot_mutate_other_quests(self):
        self.manifest["stages"][2]["branches"][0]["set_fact"] = "q115_done"
        with self.assertRaises(QuestSpecError): self.build()

    def test_inherited_branch_operations_are_rejected(self):
        self.manifest["stages"][2]["branches"][0]["add_items"] = ["Items.money"]
        with self.assertRaises(QuestSpecError): self.build()

    def test_ambiguous_catalogue_selector(self):
        entry = next(x for x in self.catalog["instances"] if x["debug_name"] == self.runtime["binding"]["debug_name"])
        self.catalog["instances"].append(entry.copy())
        with self.assertRaises(QuestSpecError): self.build()

    def test_catalogue_position_must_be_finite(self):
        entry = next(x for x in self.catalog["instances"] if x["debug_name"] == self.runtime["binding"]["debug_name"])
        entry["position"]["x"] = float("nan")
        with self.assertRaises(QuestSpecError): self.build()

    def test_duration_and_payment_bounds(self):
        for key, values in [("transfer_duration", [True, 0, 31, float("inf")]), ("reward_amount", [True, -1, 10001, 1.5])]:
            original = self.runtime[key]
            for value in values:
                with self.subTest(key=key, value=value):
                    self.runtime[key] = value
                    with self.assertRaises(QuestSpecError): self.build()
            self.runtime[key] = original


if __name__ == "__main__":
    unittest.main()
