from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import build_lipsync_dataset as dataset  # noqa: E402
from explore_lipsync import LipsyncExplorer  # noqa: E402


def fixture_document() -> dict:
    return {
        "accessors": [{"max": [1.0]}],
        "skins": [
            {
                "extras": {
                    "trackNames": ["lipSyncEnvelope", "jaw_mid_openLipsyncPoseOutput"],
                }
            }
        ],
        "animations": [
            {
                "name": "f_000000000000002A",
                "samplers": [{"input": 0}],
                "extras": {
                    "trackKeys": [
                        {"trackIndex": 0, "time": 0.0, "value": 0.0},
                        {"trackIndex": 0, "time": 1.0, "value": 1.0},
                        {"trackIndex": 1, "time": 0.0, "value": 0.0},
                        {"trackIndex": 1, "time": 0.5, "value": 1.0},
                        {"trackIndex": 1, "time": 1.0, "value": 0.0},
                    ],
                    "constTrackKeys": [],
                },
            }
        ],
    }


class LipsyncDatasetTests(unittest.TestCase):
    def test_normalizes_stressed_arpabet(self) -> None:
        self.assertEqual(dataset.normalize_phones("HH UW1 IH0 Z AO1"), ["HH", "UW", "IH", "Z", "AA"])

    def test_extracts_nonblank_token_runs_and_expands_boundaries(self) -> None:
        runs = dataset.token_runs(
            [0, 2, 2, 0, 0, 3, 0],
            [1.0, 0.8, 1.0, 1.0, 1.0, 0.6, 1.0],
        )
        self.assertEqual([(run.token_id, run.start_frame, run.end_frame) for run in runs], [(2, 1, 3), (3, 5, 6)])
        aligned = dataset.expand_token_runs(["HH", "UW"], runs, 0.1)
        self.assertAlmostEqual(aligned[0].start, 0.1)
        self.assertAlmostEqual(aligned[0].end, 0.375)
        self.assertAlmostEqual(aligned[1].end, 0.6)

    def test_linearly_interpolates_curves(self) -> None:
        keys = [(0.0, 0.0), (0.5, 1.0), (1.0, 0.0)]
        self.assertEqual(dataset.curve_value(keys, -1.0), 0.0)
        self.assertAlmostEqual(dataset.curve_value(keys, 0.25), 0.5)
        self.assertAlmostEqual(dataset.curve_value(keys, 0.75), 0.5)

    def test_joins_scaled_phonemes_to_animation_frames(self) -> None:
        explorer = LipsyncExplorer(fixture_document())
        alignments = [
            dataset.PhoneAlignment("HH", 0.2, 0.6, 0.9, 0.25, 0.3),
            dataset.PhoneAlignment("UW", 0.6, 1.8, 0.8, 1.0, 1.1),
        ]
        rows, curves = dataset.dataset_rows(
            explorer,
            "42",
            "Who",
            alignments,
            audio_duration=2.0,
            fps=4.0,
            track_set="mouth",
        )
        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[0]["phoneme"], "SIL")
        self.assertEqual(rows[1]["phoneme"], "HH")
        self.assertEqual(rows[2]["phoneme"], "UW")
        self.assertAlmostEqual(rows[1]["jaw_mid_openLipsyncPoseOutput"], 0.5)
        self.assertIn("lipSyncEnvelope", curves)


if __name__ == "__main__":
    unittest.main()
