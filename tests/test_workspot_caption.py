"""Caption parsing must retain the evidence/context boundary."""
from pathlib import Path
import json
import sys
import tempfile
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from workspot_caption import parse_caption, prepare_inputs, semantic_identity, trim_generated
from workspot_caption_vllm import completed, messages, load_jobs, uploads_complete
from workspot_caption import sha256


class CaptionTests(unittest.TestCase):
    def test_uploaded_jobs_require_matching_media_and_final_manifest_marker(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            video = root / "video.mp4"
            video.write_bytes(b"verified video")
            row = {"id": "clip", "video": "video.mp4", "media_sha256": {"video.mp4": sha256(video)}}
            jobs = root / "jobs.jsonl"
            jobs.write_text(json.dumps(row) + "\n")
            self.assertEqual(load_jobs(jobs, root), [row])
            marker = root / "UPLOAD_COMPLETE"
            self.assertFalse(uploads_complete(marker, jobs, 1))
            marker.write_text(json.dumps({"count": 1, "jobs_sha256": sha256(jobs)}))
            self.assertTrue(uploads_complete(marker, jobs, 1))
            with self.assertRaises(ValueError):
                uploads_complete(marker, jobs, 2)
            video.write_bytes(b"changed video")
            with self.assertRaisesRegex(ValueError, "changed video"):
                load_jobs(jobs, root)

    def test_fenced_json_preserves_observations_and_inference(self):
        value = parse_caption('```json\n{"observed_motion":{"right_hand":"near ear"},"inferred_context":{"likely_action":"phone use"},"unverified":["phone absent"],"uncertainties":[]}\n```')
        self.assertEqual(value["observed_motion"]["right_hand"], "near ear")
        self.assertEqual(value["inferred_context"]["likely_action"], "phone use")

    def test_flat_or_incomplete_answer_cannot_be_accepted(self):
        for text in ('{"caption":"phone call"}', '[]', '{"observed_motion":"phone call","inferred_context":{},"unverified":[],"uncertainties":[]}'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_caption(text)

    def test_batch_keeps_each_video_and_context_in_its_own_conversation(self):
        processor = Mock()
        rows = [{"video": "a/preview.mp4", "prompt": "Describe", "context": {"name": "phone"}},
                {"video": "b/preview.mp4", "prompt": "Describe", "context": {"name": "boxing"}}]
        prepare_inputs(processor, rows, Path("inputs"), 24)
        args, kwargs = processor.apply_chat_template.call_args
        self.assertEqual(len(args[0]), 2)
        self.assertIn("phone", str(args[0][0]))
        self.assertNotIn("boxing", str(args[0][0]))
        self.assertTrue(kwargs["padding"])
        self.assertIsNone(kwargs["fps"])

    def test_eos_terminates_each_output_before_other_batch_members_padding(self):
        self.assertEqual(trim_generated([1, 2, 99, 0, 0], {99}), ([1, 2], True))
        self.assertEqual(trim_generated([1, 2, 3], {99}), ([1, 2, 3], False))

    def test_resume_reuses_matching_model_inputs_across_batch_sizes_only(self):
        settings = {key: "value" for key in ("model", "revision", "dtype", "attention", "frames", "max_new_tokens", "enable_thinking", "do_sample", "video_size")}
        first = semantic_identity({"video": "a"}, {**settings, "batch_size": 1})
        self.assertEqual(first, semantic_identity({"video": "a"}, {**settings, "batch_size": 4}))
        self.assertNotEqual(first, semantic_identity({"video": "b"}, settings))
        self.assertNotEqual(first, semantic_identity({"video": "a"}, {**settings, "revision": "new"}))

    def test_backend_switch_requires_same_source_prompt_model_and_frame_budget(self):
        row = {"id": "a", "video": "a/preview.mp4", "prompt": "Describe"}
        settings = {"model": "qwen", "revision": "revision", "frames": 24, "max_new_tokens": 1024}
        records = [{"status": "captioned", "input": row, "settings": settings}]
        self.assertTrue(completed(row, records, "qwen", "revision", 24))
        self.assertFalse(completed({**row, "prompt": "Different"}, records, "qwen", "revision", 24))
        self.assertFalse(completed(row, records, "qwen", "revision", 32))
        self.assertFalse(completed(row, records, "qwen", "revision", 24, 512))
        self.assertTrue(messages(row, Path("inputs"))[0]["content"][0]["video_url"]["url"].startswith("file:"))

    def test_shared_clip_metadata_is_bounded_without_mutating_source_input(self):
        row = {"video": "a/preview.mp4", "prompt": "Describe",
               "context": {"animation_name": "sit", "workspots": [{"filename": str(i)} for i in range(100)]}}
        text = messages(row, Path("inputs"))[0]["content"][1]["text"]
        self.assertIn('"additional_workspot_associations_omitted": 96', text)
        self.assertNotIn('"filename": "4"', text)
        self.assertEqual(len(row["context"]["workspots"]), 100)


if __name__ == "__main__":
    unittest.main()
