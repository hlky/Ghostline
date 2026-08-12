from __future__ import annotations

import struct
import sys
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import compile_lipsync_line as compiler


class CompileLipsyncLineTests(unittest.TestCase):
    def test_replaces_pose_outputs_and_creates_negative_override_pair(self) -> None:
        document = {
            "skins": [
                {
                    "extras": {
                        "trackNames": [
                            "jaw_mid_openLipsyncPoseOutput",
                            "jaw_mid_openAnimOverrideWeight",
                            "eye_l_blinkLipsyncPoseOutput",
                            "unrelated",
                        ]
                    }
                }
            ],
            "animations": [
                {
                    "name": "source",
                    "channels": [
                        {"sampler": 0, "target": {"node": 0, "path": "translation"}},
                        {"sampler": 1, "target": {"node": 1, "path": "rotation"}},
                    ],
                    "samplers": [{"input": 0}, {"input": 1}],
                    "extras": {
                        "trackKeys": [
                            {"trackIndex": 0, "time": 0.0, "value": 0.9},
                            {"trackIndex": 1, "time": 0.0, "value": -0.9},
                            {"trackIndex": 2, "time": 0.0, "value": 0.8},
                            {"trackIndex": 3, "time": 0.0, "value": 0.4},
                        ],
                        "constTrackKeys": [],
                    },
                }
            ],
        }
        stats = compiler.replace_lipsync_tracks(
            document,
            "source",
            "generated",
            ["jaw_mid_openLipsyncPoseOutput"],
            np.asarray([0.0, 1.0]),
            np.asarray([[0.1], [0.7]]),
            strip_donor_skeleton=True,
        )
        animation = document["animations"][-1]
        keys = animation["extras"]["trackKeys"]
        self.assertEqual(stats["override_tracks"], 1)
        self.assertEqual(stats["removed_skeletal_channels"], 1)
        self.assertEqual(len(animation["channels"]), 1)
        self.assertEqual(len(animation["samplers"]), 1)
        self.assertFalse(any(key["trackIndex"] == 3 for key in keys))
        self.assertFalse(any(key["trackIndex"] == 2 for key in keys))
        self.assertEqual(
            [(key["time"], key["value"]) for key in keys if key["trackIndex"] == 0],
            [(0.0, 0.1), (1.0, 0.7)],
        )
        self.assertEqual(
            [(key["time"], key["value"]) for key in keys if key["trackIndex"] == 1],
            [(0.0, -0.1), (1.0, -0.7)],
        )

    def test_speech_window_is_neutral_outside_the_spoken_interval(self) -> None:
        times = np.asarray([0.0, 0.3, 0.4, 1.0, 1.1, 1.2])
        values = np.ones((len(times), 2), dtype=np.float64)
        faded = compiler.apply_speech_window(
            times,
            values,
            speech_start=0.4,
            speech_end=1.1,
            anticipation_ms=100.0,
            release_ms=100.0,
        )
        np.testing.assert_allclose(faded[0], 0.0)
        np.testing.assert_allclose(faded[1], 0.0)
        np.testing.assert_allclose(faded[2], 1.0)
        np.testing.assert_allclose(faded[4], 1.0)
        np.testing.assert_allclose(faded[-1], 0.0)

    def test_matching_rig_mode_retains_reference_pose_channels(self) -> None:
        document = {
            "skins": [{"extras": {"trackNames": ["jaw_mid_openLipsyncPoseOutput"]}}],
            "animations": [
                {
                    "name": "source",
                    "channels": [
                        {"sampler": 0, "target": {"node": 0, "path": "translation"}},
                        {"sampler": 1, "target": {"node": 1, "path": "rotation"}},
                    ],
                    "samplers": [{"input": 0}, {"input": 1}],
                    "extras": {"trackKeys": [], "constTrackKeys": []},
                }
            ],
        }
        stats = compiler.replace_lipsync_tracks(
            document,
            "source",
            "generated",
            ["jaw_mid_openLipsyncPoseOutput"],
            np.asarray([0.0, 1.0]),
            np.asarray([[0.0], [0.0]]),
        )
        animation = document["animations"][-1]
        self.assertEqual(stats["removed_skeletal_channels"], 0)
        self.assertEqual(len(animation["channels"]), 2)
        self.assertEqual(len(animation["samplers"]), 2)

    def test_clear_donor_controls_preserves_reference_channels(self) -> None:
        document = {
            "skins": [
                {
                    "extras": {
                        "trackNames": [
                            "jaw_mid_openLipsyncPoseOutput",
                            "jaw_mid_openAnimOverrideWeight",
                            "muzzleBrows",
                        ]
                    }
                }
            ],
            "animations": [
                {
                    "name": "source",
                    "channels": [
                        {"sampler": 0, "target": {"node": 0, "path": "translation"}},
                        {"sampler": 1, "target": {"node": 1, "path": "rotation"}},
                    ],
                    "samplers": [{"input": 0}, {"input": 1}],
                    "extras": {
                        "trackKeys": [
                            {"trackIndex": 2, "time": 0.0, "value": 0.7},
                        ],
                        "constTrackKeys": [
                            {"trackIndex": 2, "value": 0.3},
                        ],
                    },
                }
            ],
        }
        stats = compiler.replace_lipsync_tracks(
            document,
            "source",
            "generated",
            ["jaw_mid_openLipsyncPoseOutput"],
            np.asarray([0.0, 1.0]),
            np.asarray([[0.1], [0.7]]),
            clear_donor_controls=True,
        )
        animation = document["animations"][-1]
        self.assertTrue(stats["cleared_all_donor_controls"])
        self.assertEqual(stats["removed_skeletal_channels"], 0)
        self.assertEqual(len(animation["channels"]), 2)
        self.assertEqual(len(animation["samplers"]), 2)
        self.assertEqual(
            animation["extras"]["constTrackKeys"],
            [{"trackIndex": 2, "time": 0.0, "value": 0.0}],
        )
        self.assertEqual(stats["neutral_constant_tracks"], 1)
        self.assertFalse(
            any(key["trackIndex"] == 2 for key in animation["extras"]["trackKeys"])
        )

    def test_neutral_skeleton_uses_step_constants_and_two_key_duration_marker(self) -> None:
        document = {
            "buffers": [{"byteLength": 0}],
            "bufferViews": [],
            "accessors": [],
            "nodes": [
                {"name": "Root"},
                {
                    "name": "face_root_JNT",
                    "translation": [1.0, 2.0, 3.0],
                    "rotation": [0.1, 0.2, 0.3, 0.9],
                },
            ],
            "animations": [
                {
                    "name": "generated",
                    "channels": [
                        {"sampler": 0, "target": {"node": 0, "path": "translation"}},
                        {"sampler": 1, "target": {"node": 1, "path": "translation"}},
                        {"sampler": 2, "target": {"node": 1, "path": "rotation"}},
                    ],
                    "samplers": [{}, {}, {}],
                }
            ],
        }
        chunks = [(compiler.BIN_CHUNK, b"")]
        stats = compiler.build_neutral_skeletal_channels(
            document, chunks, "generated", 10.0
        )
        samplers = document["animations"][0]["samplers"]
        self.assertEqual(stats["neutralized_skeletal_channels"], 3)
        self.assertEqual(stats["constant_skeletal_channels"], 2)
        self.assertEqual(stats["duration_marker_node"], "face_root_JNT")
        self.assertEqual(samplers[0]["interpolation"], "STEP")
        self.assertEqual(samplers[1]["interpolation"], "LINEAR")
        self.assertEqual(samplers[2]["interpolation"], "STEP")
        marker_times = document["accessors"][samplers[1]["input"]]
        marker_values = document["accessors"][samplers[1]["output"]]
        self.assertEqual(marker_times["count"], 2)
        self.assertEqual(marker_times["min"], [0.0])
        self.assertEqual(marker_times["max"], [10.0])
        self.assertEqual(marker_values["count"], 2)
        self.assertEqual(marker_values["min"], [1.0, 2.0, 3.0])
        self.assertEqual(marker_values["max"], [1.0, 2.0, 3.0])

    def test_zero_track_prefixes_masks_only_the_selected_controls(self) -> None:
        values = np.asarray([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
        masked, names = compiler.zero_track_prefixes(
            [
                "jaw_mid_openLipsyncPoseOutput",
                "neck_throat_openLipsyncPoseOutput",
                "neck_throat_compressLipsyncPoseOutput",
            ],
            values,
            ["neck_throat_"],
        )
        self.assertEqual(
            names,
            [
                "neck_throat_openLipsyncPoseOutput",
                "neck_throat_compressLipsyncPoseOutput",
            ],
        )
        np.testing.assert_allclose(masked[:, 0], values[:, 0])
        np.testing.assert_allclose(masked[:, 1:], 0.0)

    def test_duration_marker_uses_an_isolated_float_accessor(self) -> None:
        document = {
            "animations": [{"name": "generated", "samplers": [{"input": 0}]}],
            "accessors": [{"bufferView": 0}],
            "bufferViews": [{"buffer": 0, "byteLength": 4, "byteOffset": 0}],
            "buffers": [{"byteLength": 4}],
        }
        chunks = [(compiler.BIN_CHUNK, struct.pack("<f", 1.0))]
        compiler.set_animation_duration(document, chunks, "generated", 3.28)
        accessor = document["accessors"][-1]
        self.assertEqual(document["animations"][0]["samplers"][0]["input"], 1)
        self.assertEqual(accessor["max"], [3.28])
        self.assertAlmostEqual(struct.unpack_from("<f", chunks[0][1], 4)[0], 3.28, places=5)
        self.assertEqual(document["buffers"][0]["byteLength"], 8)


if __name__ == "__main__":
    unittest.main()
