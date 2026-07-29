from __future__ import annotations

import base64
import copy
import importlib.util
import math
import struct
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
SPEC_PATH = ROOT / "braindance/tests/gqt005_braindance_analysis.json"

MODULE_SPEC = importlib.util.spec_from_file_location(
    "braindance_rid", TOOLS / "braindance_rid.py"
)
assert MODULE_SPEC is not None
braindance_rid = importlib.util.module_from_spec(MODULE_SPEC)
assert MODULE_SPEC.loader is not None
sys.modules["braindance_rid"] = braindance_rid
MODULE_SPEC.loader.exec_module(braindance_rid)

SCENE_MODULE_SPEC = importlib.util.spec_from_file_location(
    "braindance_scene_for_rid_tests", TOOLS / "braindance_scene.py"
)
assert SCENE_MODULE_SPEC is not None
braindance_scene = importlib.util.module_from_spec(SCENE_MODULE_SPEC)
assert SCENE_MODULE_SPEC.loader is not None
sys.modules["braindance_scene_for_rid_tests"] = braindance_scene
SCENE_MODULE_SPEC.loader.exec_module(braindance_scene)


def cname(value: str) -> dict[str, object]:
    return {"$type": "CName", "$storage": "string", "$value": value}


def tag(value: str, serial: int) -> dict[str, object]:
    return {
        "$type": "scnRidTag",
        "serialNumber": {
            "$type": "scnRidSerialNumber",
            "serialNumber": serial,
        },
        "signature": cname(value),
    }


def buffer(handle_id: str, duration: float, *, camera: bool = False) -> dict[str, object]:
    payload = (
        b""
        if camera
        else b"".join(
            [
                struct.pack("<HHfff", 0, 2, 0.0, 0.0, 0.0),
                struct.pack("<HHfff", 0, 0x2002, 0.0, 0.0, 0.0),
            ]
        )
    )
    return {
        "HandleId": handle_id,
        "Data": {
            "$type": "animAnimationBufferCompressed",
            "defferedBuffer": {
                "BufferId": handle_id,
                "Flags": 0,
                "Bytes": base64.b64encode(payload).decode("ascii"),
            },
            "duration": duration,
            "numFrames": 2,
            "numJoints": 1 if camera else 71,
            "numTracks": 7 if camera else 13,
            "numAnimKeys": 0,
            "numAnimKeysRaw": 0 if camera else 2,
            "numConstAnimKeys": 0,
            "numTrackKeys": 0,
            "numConstTrackKeys": 0,
        },
    }


def actor(signature: str, serial: int, handle_base: int) -> dict[str, object]:
    def auxiliary(
        suffix: str,
        handle_id: int,
        *,
        joints: int,
        tracks: int,
    ) -> dict[str, object]:
        value = {
            "$type": "scnAnimationRid",
            "tag": tag(f"{signature}_anim_{suffix}_0", serial + 20),
            "animation": {
                "HandleId": str(handle_id),
                "Data": {
                    "$type": "animAnimation",
                    "name": cname(f"template_{signature}_{suffix}"),
                    "duration": 30.0,
                    "animBuffer": buffer(str(handle_id + 1), 30.0),
                },
            },
            "events": None,
            "motionExtracted": 0,
            "bonesCount": joints,
            "trajectoryBoneIndex": -1,
            "offset": {},
        }
        value["animation"]["Data"]["animBuffer"]["Data"]["numJoints"] = joints
        value["animation"]["Data"]["animBuffer"]["Data"]["numTracks"] = tracks
        return value

    return {
        "$type": "scnActorRid",
        "tag": tag(signature, serial),
        "animations": [
            {
                "$type": "scnAnimationRid",
                "tag": tag(f"{signature}_anim_body_0", serial + 1),
                "animation": {
                    "HandleId": str(handle_base),
                    "Data": {
                        "$type": "animAnimation",
                        "name": cname(f"template_{signature}"),
                        "duration": 30.0,
                        "animBuffer": buffer(str(handle_base + 1), 30.0),
                        "motionExtraction": {
                            "HandleId": str(handle_base + 2),
                            "Data": {
                                "$type": "animSplineCompressedMotionExtraction",
                                "duration": 30.0,
                                "posKeysData": [0] * 16,
                                "rotKeysData": [0, 0, 0, 32] + [0] * 12,
                            },
                        },
                    },
                },
                "events": None,
                "motionExtracted": 1,
                "bonesCount": 71,
                "trajectoryBoneIndex": 1,
                "offset": {},
            }
        ],
        "facialAnimations": [
            auxiliary("head", handle_base + 50, joints=344, tracks=414)
        ],
        "cyberwareAnimations": [
            auxiliary("cyb", handle_base + 60, joints=30, tracks=0)
        ],
    }


def camera() -> dict[str, object]:
    return {
        "$type": "scnCameraRid",
        "tag": tag("Camera", 20),
        "animations": [
            {
                "$type": "scnCameraAnimationRid",
                "tag": tag("Camera_anim_0", 21),
                "animation": buffer("20", 30.0, camera=True),
                "cameraAnimationLOD": {
                    "$type": "scnCameraAnimationLOD",
                    "tracks": {"Elements": []},
                    "trajectory": {"Elements": []},
                },
            }
        ],
    }


def template() -> dict[str, object]:
    return {
        "Header": {"DataType": "CR2W"},
        "Data": {
            "Version": 195,
            "RootChunk": {
                "$type": "scnRidResource",
                "actors": [
                    actor("TemplateA", 10, 0),
                    actor("TemplateB", 12, 5),
                    actor("Unused", 14, 10),
                ],
                "cameras": [camera()],
                "cookingPlatform": "PLATFORM_PC",
                "nextSerialNumber": {
                    "$type": "scnRidSerialNumber",
                    "serialNumber": 22,
                },
                "version": 5,
            },
        },
    }


def animation_samples() -> dict[str, object]:
    frames = range(361)

    def actor_row(actor_id: str, direction: float) -> dict[str, object]:
        return {
            "id": actor_id,
            "armature": None,
            "bone_order": [],
            "bone_count": None,
            "trajectory_joint_index": 1,
            "joints": [
                {
                    "index": 1,
                    "name": "__ghostline_trajectory__",
                    "samples": [
                        {
                            "frame": frame,
                            "translation": [direction * frame / 360.0, 0.0, 0.0],
                            "rotation": [0.0, 0.0, 0.0, 1.0],
                            "scale": [1.0, 1.0, 1.0],
                        }
                        for frame in frames
                    ],
                }
            ],
        }

    return {
        "schema_version": 1,
        "coordinate_space": "blender_local_z_up_right_handed",
        "frame_start": 0,
        "frame_end": 360,
        "sample_rate": 30,
        "actors": [
            actor_row("patch", 1.0),
            actor_row("guard", -1.0),
        ],
        "camera": {
            "id": "recording_camera",
            "samples": [
                {
                    "frame": frame,
                    "translation": [frame / 360.0, -2.0, 1.6],
                    "rotation": [math.sqrt(0.5), 0.0, 0.0, math.sqrt(0.5)],
                    "scale": [1.0, 1.0, 1.0],
                    "focal_length": 35.0 + 7.0 * frame / 360.0,
                }
                for frame in frames
            ],
        },
    }


def strip_actor_rig_contracts(handoff: dict[str, object]) -> None:
    for actor_value in handoff["actors"]:
        actor_value["rig"] = None
        actor_value["body_animation"] = None


def full_rig_actor_samples(
    actor_handoff: dict[str, object],
    *,
    armature: str,
    direction: float = 1.0,
) -> dict[str, object]:
    rig = actor_handoff["rig"]
    assert isinstance(rig, dict)
    bone_order = rig["bone_order"]
    assert isinstance(bone_order, list)
    trajectory_joint_index = rig["trajectory_joint_index"]
    assert isinstance(trajectory_joint_index, int)
    frames = range(361)

    return {
        "id": actor_handoff["id"],
        "armature": armature,
        "bone_order": copy.deepcopy(bone_order),
        "bone_count": len(bone_order),
        "rig_contract_sha256": rig["contract_sha256"],
        "trajectory_joint_index": trajectory_joint_index,
        "joints": [
            {
                "index": joint_index,
                "name": joint_name,
                "samples": [
                    {
                        "frame": frame,
                        "translation": (
                            [direction * frame / 360.0, 0.0, 0.0]
                            if joint_index == trajectory_joint_index
                            else [
                                2.0 + direction * frame / 360.0,
                                0.5,
                                0.0,
                            ]
                            if joint_name == "reference_joint"
                            else [0.0, 0.0, 0.0]
                        ),
                        "rotation": (
                            [
                                math.sin(frame / 360.0 * math.pi / 8.0),
                                0.0,
                                0.0,
                                math.cos(frame / 360.0 * math.pi / 8.0),
                            ]
                            if joint_index == 5
                            else [0.0, 0.0, 0.0, 1.0]
                        ),
                        "scale": [1.0, 1.0, 1.0],
                    }
                    for frame in frames
                ],
            }
            for joint_index, joint_name in enumerate(bone_order)
        ],
    }


class BraindanceRidTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        spec = braindance_scene.load_json(SPEC_PATH)
        cls.production_handoff = braindance_scene.build_handoff_manifest(
            spec,
            SPEC_PATH,
        )
        cls.handoff = copy.deepcopy(cls.production_handoff)
        strip_actor_rig_contracts(cls.handoff)
        cls.handoff["animation_samples"] = animation_samples()
        cls.handoff["rid_status"] = "custom_animation_compile_ready"

    def full_rig_handoff(self) -> dict[str, object]:
        handoff = copy.deepcopy(self.handoff)
        production_actor = self.production_handoff["actors"][0]
        handoff["actors"][0]["rig"] = copy.deepcopy(
            production_actor["rig"]
        )
        handoff["actors"][0]["body_animation"] = copy.deepcopy(
            production_actor["body_animation"]
        )
        handoff["animation_samples"]["actors"][0] = full_rig_actor_samples(
            production_actor,
            armature="PatchArmature",
        )
        return handoff

    def test_checked_handoff_validates(self) -> None:
        report = braindance_rid.validate_handoff(self.handoff)

        self.assertTrue(report.ok, report.errors)
        self.assertEqual(report.details["actor_count"], 2)
        self.assertEqual(report.details["duration_seconds"], 12.0)

    def test_compile_retags_prunes_retimes_and_places_slots(self) -> None:
        compiled, report = braindance_rid.compile_rid_document(
            self.handoff,
            template(),
            actor_template_signatures=["TemplateB", "TemplateA"],
        )
        root = compiled["Data"]["RootChunk"]

        self.assertEqual(
            [
                braindance_rid._tag_signature(value)
                for value in root["actors"]
            ],
            ["patch", "guard"],
        )
        self.assertEqual(len(root["actors"]), 2)
        self.assertEqual(len(root["cameras"]), 1)
        self.assertEqual(root["nextSerialNumber"]["serialNumber"], 7)
        patch_body = root["actors"][0]["animations"][0]
        self.assertEqual(
            patch_body["animation"]["Data"]["name"]["$value"],
            "gqt005_braindance_analysis_anim_sn2",
        )
        self.assertEqual(patch_body["animation"]["Data"]["duration"], 12.0)
        self.assertEqual(
            patch_body["animation"]["Data"]["animBuffer"]["Data"]["duration"],
            12.0,
        )
        position = patch_body["offset"]["position"]
        self.assertAlmostEqual(position["X"], 2.6)
        self.assertAlmostEqual(position["Y"], 0.45)
        orientation = patch_body["offset"]["orientation"]
        self.assertAlmostEqual(orientation["k"], math.sqrt(0.5))
        self.assertAlmostEqual(orientation["r"], math.sqrt(0.5))
        trajectory = root["cameras"][0]["animations"][0][
            "cameraAnimationLOD"
        ]["trajectory"]["Elements"]
        self.assertEqual(len(trajectory), 3)
        self.assertEqual([item["time"] for item in trajectory], [0.0, 6.0, 12.0])
        self.assertEqual(trajectory[-1]["transform"]["position"]["W"], 1.0)
        self.assertEqual(
            report["animation_source"]["mode"],
            "authored_blender_samples_encoded",
        )
        self.assertFalse(report["animation_source"]["custom_skeletal_animation"])
        self.assertTrue(report["animation_source"]["custom_camera_buffer"])
        self.assertEqual(
            [
                item["layout_template_actor"]
                for item in report["animation_source"]["actors"]
            ],
            ["TemplateB", "TemplateA"],
        )
        self.assertEqual(
            report["animation_source"]["actors"][0][
                "template_pose_fallback"
            ]["raw_transform_keys"],
            2,
        )
        motion = report["animation_source"]["actors"][0]["motion_extraction"]
        self.assertEqual(motion["position_keys"], 361)
        self.assertEqual(motion["rotation_keys"], 361)
        self.assertEqual(
            {
                (channel["joint_index"], channel["channel"])
                for channel in report["animation_source"]["actors"][0][
                    "channels"
                ]
            },
            {(1, "translation"), (1, "rotation")},
        )

    def test_compile_does_not_mutate_inputs(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        source_template = template()
        expected_handoff = copy.deepcopy(handoff)
        expected_template = copy.deepcopy(source_template)

        braindance_rid.compile_rid_document(handoff, source_template)

        self.assertEqual(handoff, expected_handoff)
        self.assertEqual(source_template, expected_template)

    def test_proxy_pose_advances_with_authored_travel_and_freezes_on_hold(
        self,
    ) -> None:
        handoff = copy.deepcopy(self.handoff)
        patch_samples = handoff["animation_samples"]["actors"][0]["joints"][0][
            "samples"
        ]
        for sample in patch_samples:
            frame = int(sample["frame"])
            if frame <= 120:
                distance = frame / 120.0 * 0.5
            elif frame <= 240:
                distance = 0.5
            else:
                distance = 0.5 + (frame - 240) / 120.0 * 0.5
            sample["translation"] = [distance, 0.0, 0.0]

        source_template = template()
        source_body = source_template["Data"]["RootChunk"]["actors"][0][
            "animations"
        ][0]
        source_buffer = source_body["animation"]["Data"]["animBuffer"]["Data"]
        source_pose = b"".join(
            braindance_rid._pack_raw_transform_key(
                time,
                30.0,
                5,
                0,
                (time, 0.0, 0.0),
            )
            for time in (0.0, 20.0, 25.0, 30.0)
        )
        source_buffer["defferedBuffer"]["Bytes"] = base64.b64encode(
            source_pose
        ).decode("ascii")
        source_buffer["numAnimKeysRaw"] = 4
        motion = source_body["animation"]["Data"]["motionExtraction"]["Data"]
        motion["posKeysData"] = list(
            b"".join(
                braindance_rid._pack_raw_transform_key(
                    time,
                    30.0,
                    0,
                    0,
                    position,
                )
                for time, position in (
                    (0.0, (0.0, 0.0, 0.0)),
                    (20.0, (0.0, 0.0, 0.0)),
                    (25.0, (5.0, 0.0, 0.0)),
                    (30.0, (10.0, 0.0, 0.0)),
                )
            )
        )
        motion["rotKeysData"] = list(
            b"".join(
                braindance_rid._pack_raw_transform_key(
                    time,
                    30.0,
                    0,
                    1,
                    (0.0, 0.0, 0.0, 1.0),
                )
                for time in (0.0, 30.0)
            )
        )

        compiled, report = braindance_rid.compile_rid_document(
            handoff,
            source_template,
            actor_template_signatures=["TemplateA", "TemplateB"],
        )
        compiled_buffer = compiled["Data"]["RootChunk"]["actors"][0][
            "animations"
        ][0]["animation"]["Data"]["animBuffer"]["Data"]
        payload = base64.b64decode(
            compiled_buffer["defferedBuffer"]["Bytes"]
        )
        pose_rows = []
        for offset in range(
            0,
            int(compiled_buffer["numAnimKeysRaw"]) * 16,
            16,
        ):
            time, joint_index, component, values = (
                braindance_rid._unpack_raw_transform_key(
                    payload[offset : offset + 16],
                    duration=12.0,
                )
            )
            if joint_index == 5 and component == 0:
                pose_rows.append((time, values))

        self.assertEqual(len(pose_rows), 361)
        self.assertAlmostEqual(pose_rows[0][1][0], 20.0)
        self.assertGreater(pose_rows[120][1][0], pose_rows[0][1][0])
        self.assertAlmostEqual(
            pose_rows[120][1][0],
            pose_rows[240][1][0],
            places=5,
        )
        self.assertGreater(pose_rows[-1][1][0], pose_rows[240][1][0])
        sync = report["animation_source"]["actors"][0][
            "template_pose_fallback"
        ]["motion_sync"]
        self.assertEqual(sync["mode"], "authored_travel_distance")
        self.assertAlmostEqual(sync["source_start_seconds"], 20.0)
        self.assertAlmostEqual(sync["source_end_seconds"], 30.0)
        self.assertAlmostEqual(sync["authored_path_distance"], 1.0)
        self.assertEqual(sync["frozen_samples"], 120)

    def test_compiled_document_has_unique_handles_and_serials(self) -> None:
        compiled, _ = braindance_rid.compile_rid_document(
            self.handoff,
            template(),
        )
        report = braindance_rid.validate_compiled_document(
            compiled,
            expected_name="gqt005_braindance_analysis",
            expected_duration=12.0,
            expected_actor_signatures=["patch", "guard"],
        )

        self.assertTrue(report.ok, report.errors)
        self.assertEqual(report.details["serial_numbers"], [1, 2, 3, 4, 5, 6])
        self.assertEqual(report.details["camera_trajectory_samples"], 3)
        self.assertEqual(
            report.details["camera_animation_buffer"]["track_indices"],
            list(range(7)),
        )
        self.assertEqual(
            [
                details["posKeysData"]["key_count"]
                for details in report.details["actor_motion_extractions"]
            ],
            [361, 361],
        )
        self.assertTrue(
            all(
                details["posKeysData"]["last"]["time_ratio"] == 65535
                and details["rotKeysData"]["last"]["time_ratio"] == 65535
                for details in report.details["actor_motion_extractions"]
            )
        )
        focal_track = next(
            item
            for item in report.details["camera_animation_buffer"][
                "track_checkpoints"
            ]
            if item["track_index"] == 1
        )
        self.assertAlmostEqual(focal_track["first"]["value"], 35.0)
        self.assertAlmostEqual(focal_track["middle"]["value"], 38.5)
        self.assertAlmostEqual(focal_track["last"]["value"], 42.0)
        self.assertNotEqual(
            report.details["actor_motion_extractions"][0][
                "posKeysData"
            ]["sha256"],
            report.details["actor_motion_extractions"][1][
                "posKeysData"
            ]["sha256"],
        )

    def test_compile_rejects_missing_named_template_actor(self) -> None:
        with self.assertRaisesRegex(
            braindance_rid.RidCompileError,
            "Missing",
        ):
            braindance_rid.compile_rid_document(
                self.handoff,
                template(),
                actor_template_signatures=["TemplateA", "Missing"],
            )

    def test_origin_rotates_and_translates_actor_offset(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        handoff["origin"]["location"] = [10.0, 20.0, 1.0]
        handoff["origin"]["rotation_degrees"] = [0.0, 0.0, 90.0]

        compiled, _ = braindance_rid.compile_rid_document(handoff, template())
        position = compiled["Data"]["RootChunk"]["actors"][0]["animations"][0][
            "offset"
        ]["position"]

        self.assertAlmostEqual(position["X"], 9.55)
        self.assertAlmostEqual(position["Y"], 22.6)
        self.assertAlmostEqual(position["Z"], 1.0)

    def test_rigged_actor_bone_channels_are_encoded(self) -> None:
        handoff = self.full_rig_handoff()
        rig = handoff["actors"][0]["rig"]
        self.assertEqual(rig["bone_count"], 71)
        self.assertEqual(
            handoff["animation_samples"]["actors"][0]["bone_order"],
            rig["bone_order"],
        )
        self.assertEqual(
            handoff["animation_samples"]["actors"][0][
                "rig_contract_sha256"
            ],
            rig["contract_sha256"],
        )

        compiled, report = braindance_rid.compile_rid_document(
            handoff,
            template(),
        )
        validation = braindance_rid.validate_compiled_document(compiled)
        expected_pose_indices = list(range(71))

        self.assertTrue(validation.ok, validation.errors)
        self.assertEqual(
            validation.details["actor_animation_buffers"][0][
                "pose_joint_indices"
            ],
            expected_pose_indices,
        )
        encoded_actor = report["animation_source"]["actors"][0]
        self.assertEqual(encoded_actor["armature"], "PatchArmature")
        self.assertEqual(encoded_actor["bone_count"], 71)
        self.assertIsNone(encoded_actor["template_pose_fallback"])
        self.assertFalse(encoded_actor["template_pose_fallback_used"])
        self.assertEqual(encoded_actor["expected_pose_joint_count"], 71)
        self.assertEqual(encoded_actor["authored_pose_joint_count"], 71)
        self.assertEqual(encoded_actor["const_float_track_keys"], 4)
        self.assertTrue(
            validation.details["actor_animation_buffers"][0][
                "is_scale_constant"
            ]
        )
        self.assertNotEqual(
            encoded_actor["buffer_sha256"],
            encoded_actor["layout_template_buffer_sha256"],
        )
        self.assertTrue(
            any(
                channel["joint_index"] == 5
                and channel["channel"] == "rotation"
                for channel in encoded_actor["channels"]
            )
        )
        reference_translation = next(
            channel
            for channel in encoded_actor["channels"]
            if channel["joint_index"] == 3
            and channel["channel"] == "translation"
        )
        self.assertEqual(reference_translation["storage"], "raw")
        self.assertEqual(reference_translation["sample_count"], 361)

    def test_rigged_actor_contract_rejects_bad_bakes(self) -> None:
        cases: list[tuple[str, dict[str, object], str]] = []

        wrong_order = self.full_rig_handoff()
        order = wrong_order["animation_samples"]["actors"][0]["bone_order"]
        order[5], order[6] = order[6], order[5]
        cases.append(
            (
                "order",
                wrong_order,
                "bone_order must match its rig contract",
            )
        )

        wrong_hash = self.full_rig_handoff()
        wrong_hash["animation_samples"]["actors"][0][
            "rig_contract_sha256"
        ] = "0" * 64
        cases.append(
            (
                "hash",
                wrong_hash,
                "rig contract hash does not match the handoff",
            )
        )

        wrong_name = self.full_rig_handoff()
        wrong_name["animation_samples"]["actors"][0]["joints"][5][
            "name"
        ] = "WrongLeftUpLeg"
        cases.append(
            (
                "name",
                wrong_name,
                "joint 5 name does not match its rig contract",
            )
        )

        missing_joint = self.full_rig_handoff()
        missing_joint["animation_samples"]["actors"][0]["joints"].pop()
        cases.append(
            (
                "missing joint",
                missing_joint,
                "must cover every rig joint",
            )
        )

        for label, broken, expected_error in cases:
            with self.subTest(label=label):
                report = braindance_rid.validate_handoff(broken)
                self.assertFalse(report.ok)
                self.assertTrue(
                    any(
                        expected_error in error
                        for error in report.errors
                    ),
                    report.errors,
                )

    def test_moving_rigged_actor_requires_animated_reference_joint(self) -> None:
        handoff = self.full_rig_handoff()
        reference_joint = next(
            joint
            for joint in handoff["animation_samples"]["actors"][0][
                "joints"
            ]
            if joint["name"] == "reference_joint"
        )
        for sample in reference_joint["samples"]:
            sample["translation"] = [0.0, 0.0, 0.0]
            sample["rotation"] = [0.0, 0.0, 0.0, 1.0]

        with self.assertRaisesRegex(
            braindance_rid.RidCompileError,
            "constant reference_joint",
        ):
            braindance_rid.compile_rid_document(handoff, template())

    def test_rigged_actor_must_match_template_bone_count(self) -> None:
        handoff = self.full_rig_handoff()
        rig = handoff["actors"][0]["rig"]
        rig["bone_count"] = 70
        rig["bone_order"] = rig["bone_order"][:70]
        rig["contract_sha256"] = "1" * 64
        sampled_actor = full_rig_actor_samples(
            handoff["actors"][0],
            armature="WrongRig",
        )
        handoff["animation_samples"]["actors"][0] = sampled_actor

        with self.assertRaisesRegex(
            braindance_rid.RidCompileError,
            "requires 71",
        ):
            braindance_rid.compile_rid_document(handoff, template())

    def test_facial_and_cyberware_curves_are_encoded(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        handoff["actors"][0]["facial"] = {
            "armature": "FaceRig",
            "tracks": [],
        }
        handoff["actors"][0]["cyberware"] = {
            "armature": "CyberRig",
            "tracks": [],
        }
        sampled_actor = handoff["animation_samples"]["actors"][0]
        sampled_actor["facial"] = {
            "armature": "FaceRig",
            "bone_count": 344,
            "joints": [],
            "tracks": [
                {
                    "index": 17,
                    "samples": [
                        {"frame": frame, "value": frame / 360.0}
                        for frame in range(361)
                    ],
                }
            ],
        }
        sampled_actor["cyberware"] = {
            "armature": "CyberRig",
            "bone_count": 30,
            "joints": [
                {
                    "index": 3,
                    "name": "cyber_joint_3",
                    "samples": [
                        {
                            "frame": frame,
                            "translation": [0.0, 0.0, frame / 3600.0],
                            "rotation": [0.0, 0.0, 0.0, 1.0],
                            "scale": [1.0, 1.0, 1.0],
                        }
                        for frame in range(361)
                    ],
                }
            ],
            "tracks": [],
        }

        compiled, report = braindance_rid.compile_rid_document(
            handoff,
            template(),
        )
        validation = braindance_rid.validate_compiled_document(compiled)

        self.assertTrue(validation.ok, validation.errors)
        root = compiled["Data"]["RootChunk"]
        self.assertEqual(len(root["actors"][0]["facialAnimations"]), 1)
        self.assertEqual(len(root["actors"][0]["cyberwareAnimations"]), 1)
        self.assertTrue(report["animation_source"]["custom_facial_animation"])
        self.assertTrue(report["animation_source"]["custom_cyberware_animation"])
        facial = next(
            item
            for item in validation.details["auxiliary_animation_buffers"]
            if item["actor"] == "patch" and item["channel"] == "facial"
        )
        cyberware = next(
            item
            for item in validation.details["auxiliary_animation_buffers"]
            if item["actor"] == "patch" and item["channel"] == "cyberware"
        )
        self.assertEqual(facial["track_indices"], [17])
        self.assertEqual(cyberware["joint_indices"], [3])
        hashes = braindance_rid._validation_buffer_hashes(validation)
        self.assertEqual(
            {(item["actor"], item["channel"]) for item in hashes["auxiliary"]},
            {("patch", "facial"), ("patch", "cyberware")},
        )


if __name__ == "__main__":
    unittest.main()
