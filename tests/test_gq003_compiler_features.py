from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "gq003_quest_compiler", ROOT / "tools/quest_compiler.py"
)
assert SPEC and SPEC.loader
quest_compiler = importlib.util.module_from_spec(SPEC)
sys.modules["gq003_quest_compiler"] = quest_compiler
SPEC.loader.exec_module(quest_compiler)


class Gq003CompilerFeatureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.path = (
            ROOT / "quests/story/ghostline/gq003/implementation/quest.json"
        )
        cls.spec, cls.diagnostics = quest_compiler.load_spec(cls.path)
        assert cls.spec is not None
        cls.stages = {stage.id: stage for stage in cls.spec.stages}

    def test_manifest_validates_with_only_planned_asset_warnings(self) -> None:
        self.assertFalse(
            [item for item in self.diagnostics if item.level == "error"]
        )
        self.assertEqual(len(self.spec.stages), 36)
        schema = json.loads(
            (ROOT / "tools/quest-schema-v1.json").read_text(encoding="utf-8")
        )
        manifest = json.loads(self.path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator(schema).validate(manifest)

    def test_root_joins_freight_yard_branches_and_sets_retry_checkpoint(self) -> None:
        phase = quest_compiler.build_orchestration_phase(
            self.spec,
            ROOT / "generated/gq003/mod/gq003/phases/gq003.questphase",
        )
        encoded = json.dumps(phase)
        self.assertIn("questLogicalAndNodeDefinition", encoded)
        self.assertIn("gq003_mara_stabilization", encoded)
        self.assertIn('"retryOnFailure": 1', encoded)

    def test_child_prefabs_are_scoped_to_the_stage(self) -> None:
        stage = self.stages["stabilize_mara"]
        phase = quest_compiler.build_stage_phase(
            stage,
            ROOT / "generated/gq003/mod/gq003/phases/stabilize.questphase",
            self.spec.phase_prefabs,
        )
        refs = [
            item["prefabNodeRef"]["$value"]
            for item in phase["Data"]["RootChunk"]["phasePrefabs"]
        ]
        self.assertEqual(refs, ["#gq003_pr_memory_clinic"])

    def test_custom_gaps_are_generated_without_unresolved_handles(self) -> None:
        expected_markers = {
            "breach_dispatch_relay": [
                "WasHackingMinigameSucceeded",
                "gq003_dispatch_breached",
            ],
            "operate_reconstruction_core": [
                "gq003_route_preserved",
                "gq003_route_burned",
                "Items.GhostlineBlackLanternReceipt",
            ],
            "deliver_black_lantern_package": [
                "ReserveItemToThisDropPoint",
                "Items.GhostlineBlackLanternCipher",
                "Items.GhostlineBlackLanternReceipt",
            ],
            "black_lantern_debrief": [
                "gq003_route_preserved",
                "gq003_route_burned",
                "gq003_stealth_succeeded",
                "gq003_stealth_failed",
                "contacts/patch/gq003_36_debrief",
            ],
        }
        for stage_id, markers in expected_markers.items():
            with self.subTest(stage=stage_id):
                phase = quest_compiler.build_stage_phase(
                    self.stages[stage_id],
                    ROOT
                    / f"generated/gq003/mod/gq003/phases/{stage_id}.questphase",
                    self.spec.phase_prefabs,
                )
                encoded = json.dumps(phase)
                for marker in markers:
                    self.assertIn(marker, encoded)

    def test_yard_restraint_clue_grants_auth_and_readable(self) -> None:
        stage = self.stages["investigate_yard"]
        phase = quest_compiler.build_stage_phase(
            stage,
            ROOT / "generated/gq003/mod/gq003/phases/investigate_yard.questphase",
            self.spec.phase_prefabs,
        )
        encoded = json.dumps(phase)
        self.assertIn("Items.GhostlineBlackLanternRouteAuth", encoded)
        self.assertIn("Items.GhostlineExpeditedHandoff", encoded)

    def test_clinic_location_includes_patch_yard_reaction(self) -> None:
        stage = self.stages["clinic_location_call"]
        phase = quest_compiler.build_stage_phase(
            stage,
            ROOT / "generated/gq003/mod/gq003/phases/clinic_location.questphase",
            self.spec.phase_prefabs,
        )
        encoded = json.dumps(phase)
        self.assertIn("contacts/patch/gq003_13_clinic_location/01a_msg_clean_yard", encoded)
        self.assertIn("contacts/patch/gq003_13_clinic_location/01b_msg_detected_yard", encoded)

    def test_outcome_delivery_does_not_require_neutral_fallback_item(self) -> None:
        stage = self.stages["deliver_black_lantern_package"]
        self.assertNotIn("item", stage.data)
        phase = quest_compiler.build_stage_phase(
            stage,
            ROOT / "generated/gq003/mod/gq003/phases/delivery.questphase",
            self.spec.phase_prefabs,
        )
        encoded = json.dumps(phase)
        self.assertNotIn("Items.GhostlineBlackLanternPackage", encoded)

    def test_mara_failure_blocks_child_exit(self) -> None:
        stage = self.stages["stabilize_mara"]
        self.assertTrue(
            quest_compiler.stage_template_resource(stage).endswith(
                "defend_target_retry.questphase"
            )
        )
        phase = quest_compiler.build_stage_phase(
            stage,
            ROOT / "generated/gq003/mod/gq003/phases/stabilize.questphase",
            self.spec.phase_prefabs,
        )
        encoded = json.dumps(phase)
        self.assertIn("gq003_mara_lost", encoded)
        self.assertIn("gq003_mara_stabilized", encoded)

    def test_reach_area_start_fact_no_longer_creates_forward_reference(self) -> None:
        stage = self.stages["reach_freight_yard"]
        phase = quest_compiler.build_stage_phase(
            stage,
            ROOT / "generated/gq003/mod/gq003/phases/reach_yard.questphase",
            self.spec.phase_prefabs,
        )
        quest_compiler.validate_no_forward_handle_refs(
            phase, context="gq003 reach-area regression"
        )

    def test_compile_writes_every_generated_and_template_child(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "gq003.questphase.json"
            with redirect_stdout(io.StringIO()):
                result = quest_compiler.main(
                    [
                        "compile",
                        str(self.path),
                        "--out",
                        str(output),
                        "--allow-planned",
                    ]
                )
            children = list((output.parent / "children").rglob("*.questphase.json"))
            names = {path.name for path in children}
        self.assertEqual(result, 0)
        self.assertEqual(len(children), 36)
        self.assertIn("gq003_breach_dispatch_relay.questphase.json", names)
        self.assertIn("gq003_deliver_black_lantern_package.questphase.json", names)


if __name__ == "__main__":
    unittest.main()
