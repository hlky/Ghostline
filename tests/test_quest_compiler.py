from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "quest_compiler", ROOT / "tools/quest_compiler.py"
)
assert SPEC and SPEC.loader
quest_compiler = importlib.util.module_from_spec(SPEC)
sys.modules["quest_compiler"] = quest_compiler
SPEC.loader.exec_module(quest_compiler)


class QuestCompilerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.path = ROOT / "source/quests/gq001.quest.json"
        self.raw = json.loads(self.path.read_text(encoding="utf-8"))

    def write_manifest(self, root: Path, value: dict) -> Path:
        path = root / "quest.json"
        path.write_text(json.dumps(value), encoding="utf-8")
        return path

    def test_checked_manifest_represents_requested_linear_flow(self) -> None:
        spec, diagnostics = quest_compiler.load_spec(self.path)
        self.assertIsNotNone(spec)
        assert spec is not None
        self.assertEqual(
            [stage.id for stage in spec.stages],
            [
                "patch_job_offer",
                "meet_patch",
                "hack_relay",
                "meet_iris",
                "deliver_cache",
            ],
        )
        self.assertEqual(
            [stage.type for stage in spec.stages],
            [
                "phone_job_offer",
                "meet_contact",
                "hack_access_point",
                "meet_contact",
                "deliver_drop_point",
            ],
        )
        self.assertFalse([item for item in diagnostics if item.level == "error"])

    def test_checked_manifest_resources_are_complete(self) -> None:
        spec, _ = quest_compiler.load_spec(self.path)
        assert spec is not None
        diagnostics = quest_compiler.audit_resources(spec)
        self.assertFalse(diagnostics)

    def test_compiler_emits_one_phase_node_per_stage(self) -> None:
        spec, _ = quest_compiler.load_spec(self.path)
        assert spec is not None
        phase = quest_compiler.build_orchestration_phase(
            spec, ROOT / "source/archive/mod/gq001/phases/gq001.questphase"
        )
        graph = phase["Data"]["RootChunk"]["graph"]["Data"]
        phase_nodes = [
            node["Data"]
            for node in graph["nodes"]
            if node["Data"]["$type"] == "questPhaseNodeDefinition"
        ]
        self.assertEqual([node["id"] for node in phase_nodes], [10, 11, 12, 13, 14])
        self.assertEqual(
            [
                node["phaseResource"]["DepotPath"]["$value"]
                for node in phase_nodes
            ],
            [stage.phase_resource for stage in spec.stages],
        )
        self.assertEqual(
            phase["Data"]["RootChunk"]["phasePrefabs"][0]["prefabNodeRef"]["$value"],
            "#gq000_pr_patch_meet",
        )

    def test_duplicate_stage_ids_are_rejected(self) -> None:
        value = copy.deepcopy(self.raw)
        value["stages"][1]["id"] = value["stages"][0]["id"]
        with tempfile.TemporaryDirectory() as temporary:
            spec, diagnostics = quest_compiler.load_spec(
                self.write_manifest(Path(temporary), value)
            )
        self.assertIsNone(spec)
        self.assertIn("duplicate_stage_id", {item.code for item in diagnostics})

    def test_stage_specific_required_fields_are_rejected(self) -> None:
        value = copy.deepcopy(self.raw)
        del value["stages"][2]["device"]
        with tempfile.TemporaryDirectory() as temporary:
            spec, diagnostics = quest_compiler.load_spec(
                self.write_manifest(Path(temporary), value)
            )
        self.assertIsNone(spec)
        self.assertIn("invalid_string", {item.code for item in diagnostics})

    def test_unknown_fields_are_rejected(self) -> None:
        value = copy.deepcopy(self.raw)
        value["stages"][0]["surprise"] = True
        with tempfile.TemporaryDirectory() as temporary:
            spec, diagnostics = quest_compiler.load_spec(
                self.write_manifest(Path(temporary), value)
            )
        self.assertIsNone(spec)
        self.assertIn("unknown_stage_field", {item.code for item in diagnostics})

    def test_plan_marks_completed_prototype_shipping_ready(self) -> None:
        spec, _ = quest_compiler.load_spec(self.path)
        assert spec is not None
        plan = quest_compiler.build_plan(spec, quest_compiler.audit_resources(spec))
        self.assertTrue(plan["shipping_ready"])
        self.assertEqual(plan["linear_flow"][3], "meet_iris")

    def test_ordinary_compile_rejects_planned_stage(self) -> None:
        value = copy.deepcopy(self.raw)
        value["stages"][2]["status"] = "planned"
        with tempfile.TemporaryDirectory() as temporary:
            manifest = self.write_manifest(Path(temporary), value)
            args = type(
                "Args",
                (),
                {
                    "manifest": manifest,
                    "out": Path(temporary) / "phase.json",
                    "plan": None,
                    "allow_planned": False,
                },
            )()
            self.assertEqual(quest_compiler.command_compile(args), 1)
            self.assertFalse(args.out.exists())

    def test_all_acceptance_child_phases_are_instantiated(self) -> None:
        spec, _ = quest_compiler.load_spec(self.path)
        assert spec is not None
        for stage in spec.stages:
            phase = quest_compiler.build_stage_phase(
                stage,
                ROOT / "source/archive" / Path(*stage.phase_resource.split("\\")),
            )
            self.assertEqual(
                phase["Data"]["RootChunk"]["$type"],
                "questQuestPhaseResource",
            )
            self.assertIn(
                stage.phase_resource.replace("\\", "/").split("/")[-1],
                phase["Header"]["ArchiveFileName"],
            )

        iris = quest_compiler.build_stage_phase(
            spec.stages[3],
            ROOT / "source/archive/mod/gq001/phases/gq001_iris_meet.questphase",
        )
        encoded = json.dumps(iris)
        self.assertIn("gq001_iris_meet", encoded)
        self.assertIn('"iris"', encoded)
        self.assertNotIn("gq000_job_accepted", encoded)

    def test_phone_stage_builds_choice_branches_and_completion_fact(self) -> None:
        value = {
            "schema_version": 1,
            "id": "gq_phone_test",
            "title": "Phone test",
            "stages": [
                {
                    "id": "morrow_followup",
                    "type": "phone_conversation",
                    "phase_resource": "mod\\gq_phone_test\\phases\\morrow_followup.questphase",
                    "contact": "morrow",
                    "thread": "contacts/morrow/gq_phone_test",
                    "messages": [
                        "contacts/morrow/gq_phone_test/01_message",
                        "contacts/morrow/gq_phone_test/02_message",
                    ],
                    "choice_group": "contacts/morrow/gq_phone_test/03_choices",
                    "choices": [
                        {
                            "choice": "contacts/morrow/gq_phone_test/03_choices/03a_choice",
                            "reply": "contacts/morrow/gq_phone_test/04a_reply",
                        },
                        {
                            "choice": "contacts/morrow/gq_phone_test/03_choices/03b_choice",
                            "reply": "contacts/morrow/gq_phone_test/04b_reply",
                        },
                    ],
                    "final_message": "contacts/morrow/gq_phone_test/05_final",
                    "completion_fact": "gq_phone_test_completed",
                }
            ],
        }
        with tempfile.TemporaryDirectory() as temporary:
            spec, diagnostics = quest_compiler.load_spec(
                self.write_manifest(Path(temporary), value)
            )
        self.assertIsNotNone(spec)
        self.assertFalse([item for item in diagnostics if item.level == "error"])
        assert spec is not None
        self.assertFalse(quest_compiler.audit_resources(spec))
        phase = quest_compiler.build_phone_phase(
            spec.stages[0],
            ROOT / "source/archive/mod/gq_phone_test/phases/morrow_followup.questphase",
        )
        encoded = json.dumps(phase)
        self.assertIn("questLogicalXorNodeDefinition", encoded)
        self.assertIn("03a_choice", encoded)
        self.assertIn("03b_choice", encoded)
        self.assertIn("05_final", encoded)
        self.assertIn("gq_phone_test_completed", encoded)

    def test_phone_stage_rejects_unpaired_choices(self) -> None:
        value = copy.deepcopy(self.raw)
        value["stages"] = [
            {
                "id": "bad_phone",
                "type": "phone_conversation",
                "phase_resource": "mod\\gq001\\phases\\bad_phone.questphase",
                "contact": "morrow",
                "thread": "contacts/morrow/gq001",
                "messages": ["contacts/morrow/gq001/01"],
                "choice_group": "contacts/morrow/gq001/02",
                "choices": [{"choice": "contacts/morrow/gq001/02/a"}],
                "final_message": "contacts/morrow/gq001/03",
            }
        ]
        with tempfile.TemporaryDirectory() as temporary:
            spec, diagnostics = quest_compiler.load_spec(
                self.write_manifest(Path(temporary), value)
            )
        self.assertIsNone(spec)
        self.assertIn("invalid_phone_choices", {item.code for item in diagnostics})

    def test_handle_validation_rejects_dangling_references(self) -> None:
        with self.assertRaisesRegex(
            quest_compiler.QuestSpecError, "unresolved HandleRefId"
        ):
            quest_compiler.validate_handle_graph(
                {"HandleId": "1", "child": {"HandleRefId": "2"}},
                context="broken phase",
            )

    def test_stage_contract_rejects_manifest_template_drift(self) -> None:
        spec, _ = quest_compiler.load_spec(self.path)
        assert spec is not None
        stage = spec.stages[2]
        broken = copy.deepcopy(stage.data)
        broken["success_fact"] = "fact_not_present_in_child"
        broken_stage = quest_compiler.CompiledStage(
            stage.index,
            stage.id,
            stage.type,
            stage.status,
            stage.phase_resource,
            broken,
        )
        with self.assertRaisesRegex(
            quest_compiler.QuestSpecError, "does not implement typed fields"
        ):
            quest_compiler.build_stage_phase(
                broken_stage,
                ROOT / "source/archive/mod/gq001/phases/broken.questphase",
            )


if __name__ == "__main__":
    unittest.main()
