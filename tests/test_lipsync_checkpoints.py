from __future__ import annotations
import argparse
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import build_lipsync_corpus as corpus
from build_lipsync_dataset import PhoneAlignment


class LipsyncCheckpointTests(unittest.TestCase):
    def test_resampling_reuses_alignment_but_changed_audio_or_text_does_not(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audio, glb = root / "audio.wem", root / "animation.glb"
            audio.write_bytes(b"audio")
            glb.write_bytes(b"animation")
            row = {
                "locstring_id": "42",
                "subtitle": "Hello",
                "wem_path": str(audio),
                "glb_path": str(glb),
                "animation_duration": 1.0,
            }
            args = argparse.Namespace(
                work=root,
                model="test-v1",
                device="cpu",
                alignment_workers=1,
                alignment_batch_size=1,
                fps=30,
                track_set="mouth",
            )
            alignment = [PhoneAlignment("AA", 0.0, 1.0, 0.9, 0.0, 1.0)]

            def sample(*values):
                return [{"time": values[5], "track_set": values[6]}], {"jaw": []}

            with (
                patch.object(corpus, "CTCPhoneAligner") as aligner,
                patch.object(corpus, "text_to_phones", return_value=["AA"]),
                patch.object(corpus, "decode_wem"),
                patch.object(corpus, "read_glb_json", return_value={}),
                patch.object(corpus, "LipsyncExplorer"),
                patch.object(corpus, "dataset_rows", side_effect=sample) as sampling,
            ):
                aligner.return_value.align_batch.return_value = [
                    (alignment, 1.0, "cpu")
                ]
                corpus.align_catalog(args, [row])
                corpus.align_catalog(args, [row])
                self.assertEqual(aligner.call_count, 1)
                self.assertEqual(sampling.call_count, 1)
                args.fps, args.track_set = 60, "all-dynamic"
                corpus.align_catalog(args, [row])
                self.assertEqual(aligner.call_count, 1)
                self.assertEqual(sampling.call_count, 2)
                self.assertIn("60,all-dynamic", (root / "lines/42.csv").read_text())
                glb.write_bytes(b"changed animation")
                corpus.align_catalog(args, [row])
                self.assertEqual(aligner.call_count, 1)
                row["subtitle"] = "Changed text"
                corpus.align_catalog(args, [row])
                self.assertEqual(aligner.call_count, 2)
                audio.write_bytes(b"changed audio")
                corpus.align_catalog(args, [row])
                self.assertEqual(aligner.call_count, 3)
                status = json.loads((root / "alignment.status.json").read_text())
                self.assertEqual(status["failed"], {})
                self.assertEqual(set(status["completed"]), {"42"})


if __name__ == "__main__":
    unittest.main()
