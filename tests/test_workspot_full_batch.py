"""Full-batch source deduplication and bounded frame cleanup."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from workspot_full_batch import canonical_plan, cleanup_frames


class FullBatchTests(unittest.TestCase):
    def test_dedup_uses_resolved_bytes_and_priority_and_preserves_pilot_id(self):
        def job(key, sets, rig="man"):
            return {"id": key, "rig": rig, "animsets": sets, "animation_name": "sit",
                    "uses": [{"workspot": key}]}
        jobs = [job("new", ["a"]), job("pilot", ["b"]), job("different", ["c", "a"]),
                job("woman", ["d"], "woman"), job("missing", ["absent"])]
        index = {n: {"sha256": sha, "rig": rig, "animations": {"sit": {}}}
                 for n, sha, rig in [("a", "same", "man"), ("b", "same", "man"),
                                     ("c", "different", "man"), ("d", "same", "woman")]}
        original = copy.deepcopy(jobs)
        result = canonical_plan({"jobs": jobs}, index, {"jobs": [jobs[1]]})
        self.assertEqual(len(result["jobs"]), 3)
        self.assertEqual(result["jobs"][0]["id"], "pilot")
        self.assertEqual(result["jobs"][0]["aliases"], ["pilot", "new"])
        self.assertEqual(len(result["jobs"][0]["uses"]), 2)
        self.assertEqual(result["jobs"][1]["resolved_animset"], "c")
        self.assertEqual(result["unresolved"][0]["id"], "missing")
        self.assertEqual(jobs, original)

    def test_cleanup_keeps_media_receipts_and_unrelated_files(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / "clip"
            frames = folder / "frames"
            frames.mkdir(parents=True)
            (frames / "frame_0001.png").write_bytes(b"frame")
            (frames / "notes.txt").write_text("keep")
            (folder / "preview.mp4").write_bytes(b"video")
            cleanup_frames(folder)
            self.assertFalse((frames / "frame_0001.png").exists())
            self.assertTrue((frames / "notes.txt").exists())
            self.assertTrue((folder / "preview.mp4").exists())


if __name__ == "__main__":
    unittest.main()
