from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import synthesize_lipsync_line as synthesis  # noqa: E402


class SynthesizeLipsyncLineTests(unittest.TestCase):
    def test_interpolates_phone_template_across_aligned_interval(self) -> None:
        model = {
            "tracks": ["jaw"],
            "phase": [0.0, 0.5, 1.0],
            "silence": {"median": [0.0]},
            "phones": {"AA": {"curves": {"median": [[0.0], [0.5], [1.0]]}}},
            "contexts": {"previous": [], "next": []},
            "boundaries": {
                "AA": {
                    "anticipation_ms": 0,
                    "anticipation_censored": False,
                    "release_ms": 0,
                    "release_censored": False,
                }
            },
        }
        report = {
            "audio_duration": 1.0,
            "animation_duration": 1.0,
            "alignment": [{"phone": "AA", "start": 0.0, "end": 1.0}],
        }
        predicted, phone_only = synthesis.synthesize(
            model,
            report,
            np.asarray([0.0, 0.5, 1.0]),
            context_weight=0.5,
            fallback_transition_ms=40,
            maximum_transition_ms=120,
        )
        np.testing.assert_allclose(predicted[:, 0], [0.0, 0.5, 1.0])
        np.testing.assert_allclose(phone_only, predicted)

    def test_context_delta_improves_prediction(self) -> None:
        original = np.asarray([[0.0], [1.0], [0.0]])
        phone_only = np.asarray([[0.0], [0.5], [0.0]])
        predicted = np.asarray([[0.0], [0.9], [0.0]])
        metrics = synthesis.comparison_metrics(
            original,
            predicted,
            phone_only,
            np.asarray([0.0]),
            ["AA", "AA", "AA"],
            ["jaw"],
        )
        self.assertLess(
            metrics["active_frames"]["synthesized"]["rmse"],
            metrics["active_frames"]["phone_only"]["rmse"],
        )


if __name__ == "__main__":
    unittest.main()
