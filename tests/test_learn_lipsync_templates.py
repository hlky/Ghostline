from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import learn_lipsync_templates as learner  # noqa: E402


class LearnLipsyncTemplatesTests(unittest.TestCase):
    def test_samples_curve_matrix_with_interpolation_and_clamping(self) -> None:
        times = np.asarray([0.0, 1.0, 2.0])
        values = np.asarray([[0.0, 2.0], [1.0, 4.0], [0.0, 8.0]])
        sampled = learner.sample_matrix(times, values, np.asarray([-1.0, 0.5, 1.5, 3.0]))
        np.testing.assert_allclose(
            sampled,
            [[0.0, 2.0], [0.5, 3.0], [0.5, 6.0], [0.0, 8.0]],
        )

    def test_summarizes_each_occurrence_with_equal_weight(self) -> None:
        phase = np.linspace(0.0, 1.0, 5)
        first = np.ones((5, 2), dtype=np.float32)
        second = np.full((5, 2), 3.0, dtype=np.float32)
        occurrences = [
            learner.Occurrence("1", "M", "SIL", "AA", 0.1, 0.9, first, first, first),
            learner.Occurrence("2", "M", "AA", "SIL", 0.3, 0.8, second, second, second),
        ]
        summaries, medians = learner.summarize_phones(occurrences, phase)
        self.assertEqual(summaries["M"]["occurrences"], 2)
        self.assertEqual(summaries["M"]["duration_ms"]["median"], 200.0)
        np.testing.assert_allclose(medians["M"], 2.0)

    def test_clusters_similar_phone_templates(self) -> None:
        medians = {
            "B": np.asarray([[0.0], [0.0], [0.0], [0.0], [0.0]]),
            "M": np.asarray([[0.01], [0.01], [0.01], [0.01], [0.01]]),
            "AA": np.asarray([[1.0], [1.0], [1.0], [1.0], [1.0]]),
            "AE": np.asarray([[1.01], [1.01], [1.01], [1.01], [1.01]]),
        }
        clusters, mapping, _score, scale = learner.cluster_visemes(
            medians,
            {phone: 10 for phone in medians},
            2,
            ["jaw_mid_openLipsyncPoseOutput"],
            1,
        )
        self.assertEqual(len(clusters), 2)
        self.assertEqual(mapping["B"], mapping["M"])
        self.assertEqual(mapping["AA"], mapping["AE"])
        self.assertGreater(scale[0], 0)

    def test_threshold_offset_selects_earliest_or_latest_crossing(self) -> None:
        offsets = np.asarray([-0.12, -0.08, -0.04, 0.0])
        values = np.asarray([0.1, 0.3, 0.6, 0.8])
        self.assertEqual(learner.threshold_offset(offsets, values, 0.25, True), -80)
        self.assertEqual(learner.threshold_offset(offsets, values, 0.25, False), 0)


if __name__ == "__main__":
    unittest.main()
