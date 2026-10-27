"""A supervisor failure must still trigger verified pod shutdown."""
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import workspot_caption_stream as stream


class StreamingTests(unittest.TestCase):
    def test_final_render_state_reconciles_results_before_completion_marker(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = root / "full-batch"
            folder.mkdir()
            (folder / "plan.json").write_text(json.dumps({"jobs": [{"id": "a"}, {"id": "b"}]}))
            (folder / "results.json").write_text("[]")
            (root / "catalog.json").write_text("{}")
            (folder / "state.json").write_text(json.dumps({"stage": "ready_for_captioning", "caption_jobs": 2, "counts": {"rendered_proxy": 2}}))
            rows = []
            for key in ("a", "b"):
                path = root / "previews" / key / "preview.mp4"
                path.parent.mkdir(parents=True)
                path.write_bytes(key.encode())
                rows.append({"id": key, "video": f"{key}/preview.mp4", "media_sha256": {"preview.mp4": stream.digest(path)}})
            stream.write_manifest(folder / "uploaded-jobs.jsonl", rows[:1])
            args = SimpleNamespace(output=root, alias="test-pod", chunk_size=512)
            # The first snapshot predates the final state. The final read has b.
            with patch.object(stream, "caption_jobs", side_effect=[rows[:1], rows, rows, rows]), \
                    patch.object(stream, "ssh"), patch.object(stream, "command"):
                stream.upload(args)
            marker = json.loads((folder / "upload/UPLOAD_COMPLETE").read_text())
            self.assertEqual(marker["count"], 2)
            self.assertEqual(marker["jobs_sha256"], stream.digest(folder / "uploaded-jobs.jsonl"))

    def test_setup_or_ssh_failure_still_stops_pod_and_retains_failure_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "full-batch").mkdir()
            args = SimpleNamespace(output=root, alias="test-pod", pod_id="pod-id")
            with patch.object(stream, "ssh", side_effect=RuntimeError("connection failed")), \
                    patch.object(stream, "command", side_effect=RuntimeError("copy failed")), \
                    patch.object(stream, "stop_pod", return_value={"id": "pod-id", "desiredStatus": "EXITED"}) as stop:
                stream.supervise(args)
            stop.assert_called_once_with("pod-id")
            receipt = json.loads((root / "full-batch/caption-run-receipt.json").read_text())
            self.assertEqual(receipt["pod"]["desiredStatus"], "EXITED")
            self.assertEqual(receipt["stage"], "needs_attention")
            self.assertIn("connection failed", receipt["errors"])


if __name__ == "__main__":
    unittest.main()
