from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
SPEC_PATH = ROOT / "braindance/tests/gqt005_braindance_analysis.json"

MODULE_SPEC = importlib.util.spec_from_file_location(
    "braindance_scene", TOOLS / "braindance_scene.py"
)
assert MODULE_SPEC is not None
braindance_scene = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC.loader is not None
sys.modules["braindance_scene"] = braindance_scene
MODULE_SPEC.loader.exec_module(braindance_scene)


class BraindanceSceneTests(unittest.TestCase):
    def setUp(self) -> None:
        self.spec = braindance_scene.load_json(SPEC_PATH)

    def test_checked_fixture_validates(self) -> None:
        report = braindance_scene.validate_spec(self.spec)

        self.assertTrue(report.ok, report.errors)
        self.assertEqual(report.warnings, ())
        self.assertEqual(report.details["actor_count"], 2)
        self.assertEqual(report.details["clue_count"], 3)
        self.assertEqual(report.details["duration_seconds"], 12.0)

    def test_normalized_plan_assigns_scene_performer_ids(self) -> None:
        source = copy.deepcopy(self.spec)
        plan = braindance_scene.normalized_plan(source)

        self.assertEqual(
            [(actor["actor_id"], actor["performer_id"]) for actor in plan["actors"]],
            [(0, 1), (1, 257)],
        )
        self.assertEqual(plan["recording_camera"]["interpolation"], "BEZIER")
        self.assertEqual(source, self.spec, "normalization must not mutate the source spec")

    def test_handoff_manifest_is_deterministic_and_links_objects(self) -> None:
        first = braindance_scene.build_handoff_manifest(self.spec, SPEC_PATH)
        second = braindance_scene.build_handoff_manifest(self.spec, SPEC_PATH)

        self.assertEqual(first, second)
        self.assertEqual(first["kind"], "ghostline_braindance_animation_handoff")
        self.assertEqual(
            first["source_spec"],
            "braindance/tests/gqt005_braindance_analysis.json",
        )
        self.assertEqual(first["actors"][0]["root_object"], "ACTOR_patch")
        self.assertEqual(first["actors"][0]["rid_signature"], "patch")
        for actor in first["actors"]:
            rig = actor["rig"]
            self.assertEqual(
                rig["contract"],
                "braindance/rigs/man_base.skeleton.json",
            )
            self.assertEqual(rig["name"], "man_base")
            self.assertEqual(rig["bone_count"], 71)
            self.assertEqual(rig["trajectory_joint_index"], 1)
            self.assertEqual(len(rig["bone_order"]), 71)
            self.assertEqual(
                rig["bone_order"][:7],
                [
                    "Root",
                    "Trajectory",
                    "Hips",
                    "reference_joint",
                    "Spine",
                    "LeftUpLeg",
                    "RightUpLeg",
                ],
            )
            self.assertEqual(len(rig["contract_sha256"]), 64)
            self.assertEqual(
                actor["body_animation"]["type"],
                "walk_from_root_motion",
            )
        self.assertEqual(first["recording_camera"]["object"], "CAMERA_recording_camera")
        self.assertEqual(first["recording_camera"]["rid_signature"], "Camera")
        self.assertEqual(first["clues"][0]["object"], "CLUE_encrypted_shard")
        self.assertEqual(first["rid_status"], "requires_blender_bake")
        self.assertEqual(len(first["source_sha256"]), 64)

    def test_validation_rejects_duplicate_actor_and_clue_ids(self) -> None:
        broken = copy.deepcopy(self.spec)
        broken["actors"][1]["id"] = broken["actors"][0]["id"]
        broken["actors"][1]["actor_id"] = broken["actors"][0]["actor_id"]
        broken["clues"][1]["id"] = broken["clues"][0]["id"]

        report = braindance_scene.validate_spec(broken)

        self.assertIn("Duplicate actor id: patch", report.errors)
        self.assertIn("Duplicate actor actor_id: 0", report.errors)
        self.assertIn("Duplicate clue id: encrypted_shard", report.errors)

    def test_validation_rejects_bad_timeline_and_camera_contract(self) -> None:
        broken = copy.deepcopy(self.spec)
        broken["actors"][0]["keys"][1]["frame"] = 0
        broken["recording_camera"]["keys"][0]["rotation_degrees"] = [0, 0, 0]
        broken["recording_camera"]["recorded_actor"] = "missing"

        report = braindance_scene.validate_spec(broken)

        self.assertTrue(any("duplicate frame 0" in error for error in report.errors))
        self.assertTrue(any("strictly ordered" in error for error in report.errors))
        self.assertTrue(any("exactly one" in error for error in report.errors))
        self.assertIn(
            "recording_camera.recorded_actor must reference an actor id",
            report.errors,
        )

    def test_validation_rejects_camera_fields_on_actor_keys(self) -> None:
        broken = copy.deepcopy(self.spec)
        broken["actors"][0]["keys"][0]["look_at"] = [0, 0, 0]

        report = braindance_scene.validate_spec(broken)

        self.assertTrue(
            any("camera-only look_at" in error for error in report.errors),
            report.errors,
        )

    def test_output_paths_cannot_escape_the_repository(self) -> None:
        broken = copy.deepcopy(self.spec)
        broken["outputs"]["blend"] = "../outside.blend"

        report = braindance_scene.validate_spec(broken)

        self.assertIn(
            "outputs.blend must stay inside the repository root",
            report.errors,
        )

    def test_facial_track_contract_is_preserved_in_handoff(self) -> None:
        source = copy.deepcopy(self.spec)
        source["actors"][0]["facial"] = {
            "armature": "FaceRig",
            "tracks": [
                {
                    "index": 17,
                    "object": "FaceMesh",
                    "data_path": (
                        'data.shape_keys.key_blocks["JawOpen"].value'
                    ),
                }
            ],
        }

        report = braindance_scene.validate_spec(source)
        handoff = braindance_scene.build_handoff_manifest(
            source,
            SPEC_PATH,
        )

        self.assertTrue(report.ok, report.errors)
        self.assertEqual(
            handoff["actors"][0]["facial"]["tracks"][0]["index"],
            17,
        )

    def test_facial_track_indices_must_be_unique(self) -> None:
        source = copy.deepcopy(self.spec)
        track = {
            "index": 3,
            "object": "FaceMesh",
            "data_path": '["value"]',
        }
        source["actors"][0]["facial"] = {
            "tracks": [track, copy.deepcopy(track)],
        }

        report = braindance_scene.validate_spec(source)

        self.assertFalse(report.ok)
        self.assertTrue(
            any("duplicates index 3" in error for error in report.errors)
        )

    def test_explicit_blender_path_and_build_command(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            blender = Path(tmp) / "blender.exe"
            blender.touch()
            resolved = braindance_scene.find_blender(blender)
            command = braindance_scene.build_command(
                resolved,
                SPEC_PATH,
                no_glb=True,
            )

        self.assertEqual(Path(command[0]), resolved)
        self.assertIn("--factory-startup", command)
        self.assertEqual(command[-1], "--no-glb")

    def test_bake_command_loads_the_existing_blend(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            blender = Path(tmp) / "blender.exe"
            blender.touch()
            command = braindance_scene.build_command(
                blender,
                SPEC_PATH,
                bake_existing=True,
            )

        self.assertEqual(command[-1], "--bake-existing")

    def test_plan_json_is_serializable(self) -> None:
        encoded = json.dumps(braindance_scene.normalized_plan(self.spec))
        self.assertIn("gqt005_braindance_analysis", encoded)


if __name__ == "__main__":
    unittest.main()
