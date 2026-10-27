"""Prevent false clip/rig matches and unsafe shared-buffer reads."""
import base64
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import workspot_preview as preview


def resource(value):
    return {"DepotPath": {"$value": value}}


class WorkspotPreviewTests(unittest.TestCase):
    def test_extent_guard_accepts_horizontal_body_but_rejects_collapsed_geometry(self):
        skeleton = {"bone_count": 2, "bones": [{"name": "Hips", "parent": -1}, {"name": "Head", "parent": 0}]}
        document = {"Data": {"RootChunk": {"animations": [{"animation": {"name": "body"}}]}}}
        decoded = SimpleNamespace(duration=1, frame_count=2, bytes_consumed=1, payload_bytes=1,
                                  translations=[[[0, 0, 0]] * 2] * 2,
                                  rotations=[[[0, 0, 0, 1]] * 2] * 2,
                                  scales=[[[1, 1, 1]] * 2] * 2)
        job = {"id": "clip", "rig": "man.rig", "animsets": ["clip.anims"], "animation_name": "body"}
        for end in ([0, 0, 1.8], [0, 1.8, .1], [1.8, 0, .1], [0, 0, 0]):
            frames = [[[0, 0, 0], end]] * 2
            with self.subTest(end=end), patch.multiple(preview, read=lambda p: document, digest=lambda p: "source",
                    build_contract=lambda *a: skeleton, animation_buffer=lambda *a: {"$type": "animAnimationBufferCompressed"},
                    validate_joint_layout=lambda *a: {}, decode_compressed_buffer=lambda *a: decoded,
                    _model_positions=lambda *a: frames):
                if end == [0, 0, 0]:
                    with self.assertRaisesRegex(ValueError, "small spatial extent"):
                        preview.decode_job(job, Path("cache"), fps=1)
                else:
                    result = preview.decode_job(job, Path("cache"), fps=1)
                    self.assertEqual(result["actors"][0]["frames"], frames)

    def test_rig_matching_is_exact_and_default_priority_is_128(self):
        def group(rig, values):
            return {"rig": resource(rig), "animations": {"cinematics": values}}
        document = {"Data": {"RootChunk": {"workspotTree": {"Data": {
            "finalAnimsets": [
                group("woman_base.rig", [{"animSet": resource("wrong.anims"), "priority": 255}]),
                group("man_base.rig", [{"animSet": resource("default.anims")},
                                       {"animSet": resource("low.anims"), "priority": 1},
                                       {"animSet": resource("high.anims"), "priority": 200}]),
            ]}}}}}
        self.assertEqual(preview.registrations(document, "man_base.rig"), ["high.anims", "default.anims", "low.anims"])

    def test_tempbuffer_and_shared_chunk_address_yield_same_bytes(self):
        root = {"animationDataChunks": [{"buffer": {"Bytes": base64.b64encode(b"prefixPAYLOADsuffix").decode()}}]}
        animation = {"animBuffer": {"dataAddress": {"unkIndex": 0, "fsetInBytes": 6, "zeInBytes": 7}}}
        result = preview.animation_buffer(root, animation, lambda x: x)
        self.assertEqual(base64.b64decode(result["defferedBuffer"]["Bytes"]), b"PAYLOAD")
        animation = {"animBuffer": {"tempBuffer": {"Bytes": base64.b64encode(b"PAYLOAD").decode()}}}
        result = preview.animation_buffer({}, animation, lambda x: x)
        self.assertEqual(base64.b64decode(result["defferedBuffer"]["Bytes"]), b"PAYLOAD")

    def test_chunk_slice_does_not_silently_truncate(self):
        root = {"animationDataChunks": [{"buffer": {"Bytes": "AA=="}}]}
        with self.assertRaisesRegex(ValueError, "out of bounds"):
            preview.animation_buffer(root, {"animBuffer": {"dataAddress": {"unkIndex": 0, "fsetInBytes": 1, "zeInBytes": 8}}}, lambda x: x)

    def test_opaque_buffer_is_not_a_renderable_animation(self):
        with self.assertRaisesRegex(ValueError, "Opaque"):
            preview.animation_buffer({}, {"animBuffer": {"$rawData": "AA=="}}, lambda x: x)

    def test_declared_extra_channels_are_not_mistaken_for_body_bones(self):
        result = preview.validate_joint_layout({"numJoints": 72, "numExtraJoints": 1, "extraDataNames": [{"$value": "syncTrajectory"}]}, {"bone_count": 71})
        self.assertEqual(result, {"body_joints": 71, "extra_joints_omitted": 1, "extra_data_names": ["syncTrajectory"]})
        with self.assertRaisesRegex(ValueError, "joint mismatch"):
            preview.validate_joint_layout({"numJoints": 72}, {"bone_count": 71})

    def test_depot_identity_preserves_duplicate_basenames_and_rejects_escape(self):
        root = Path("cache")
        self.assertNotEqual(preview.raw_path(root, "base/a/same.anims"), preview.raw_path(root, "base/b/same.anims"))
        with self.assertRaises(ValueError):
            preview.raw_path(root, "base/../../outside.anims")

    def test_plan_samples_lifecycle_roles_before_extra_variations(self):
        rig = r"base\characters\base_entities\man_base\man_base.rig"
        spot = r"base\workspots\example.workspot"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = preview.raw_path(root, spot)
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({"Data": {"RootChunk": {"workspotTree": {"Data": {"finalAnimsets": [{"rig": resource(rig), "animations": {"cinematics": [{"animSet": resource("base/test.anims")}]}}]}}}}}))
            entries = [{"type": "workSequence", "id": 1, "settings": {"idleAnim": "idle"}}]
            entries += [{"type": "workAnimClip", "id": i + 2, "settings": {"animName": f"variation_{i}"}} for i in range(10)]
            entries += [{"type": "workEntryAnim", "id": 40, "settings": {"animName": "enter"}}, {"type": "workExitAnim", "id": 50, "settings": {"animName": "leave"}}]
            catalog = {"workspots": [{"depot_path": spot, "source": {"binary_sha256": "hash"}, "rigs": [rig], "entries": entries}]}
            result = preview.make_plan(catalog, root, [spot], max_clips=4)
            self.assertEqual({j["animation_name"] for j in result["jobs"]}, {"idle", "variation_0", "enter", "leave"})
            self.assertEqual(result["scope"], "Individual body clips; not workspot-tree simulation")


if __name__ == "__main__":
    unittest.main()
