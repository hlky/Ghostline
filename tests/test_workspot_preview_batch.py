"""Check batch reuse and separation of visual evidence from filename hints."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import workspot_preview_batch as batch


class WorkspotBatchTests(unittest.TestCase):
    def fixtures(self):
        spot = r"base\workspots\phone.workspot"
        use = {"workspot": spot, "workspot_sha256": "source", "entry_id": 7,
               "entry_type": "workAnimClip", "role": "clip"}
        job = {"id": "clip", "rig": batch.MAN_RIG, "animsets": ["base/test.anims"],
               "animation_name": "phone_talk", "uses": [use]}
        result = {"id": "clip", "status": "rendered_proxy", "outputs": {"preview.mp4": "media"},
                  "renderer": "skinned_source_mesh", "limitations": ["Props omitted"],
                  "provenance": {"sample_times_seconds": [0, 1], "source_duration_seconds": 2}}
        record = {"depot_path": spot, "source": {"binary_sha256": "source"},
                  "entries": [{"id": 7, "settings": {"itemActions": ["phone"]}}],
                  "tree_settings": {"globalProps": ["phone"]}}
        return {"jobs": [job]}, [result], {"workspots": [record]}

    def test_paired_jobs_share_media_without_leaking_names_into_visual_input(self):
        plan, results, catalog = self.fixtures()
        visual, context = batch.caption_jobs(plan, results, catalog, "paired")
        self.assertNotIn("context", visual)
        self.assertNotIn("phone", str(visual))
        self.assertEqual(visual["media_sha256"], context["media_sha256"])
        self.assertEqual(context["context"]["animation_name"], "phone_talk")
        self.assertEqual(context["context"]["workspots"][0]["item_actions"], ["phone"])
        self.assertIn("report the conflict", context["prompt"])

    def test_stale_workspot_context_is_rejected(self):
        plan, results, catalog = self.fixtures()
        catalog["workspots"][0]["source"]["binary_sha256"] = "changed"
        with self.assertRaisesRegex(ValueError, "Source workspot changed"):
            batch.caption_jobs(plan, results, catalog)

    def test_expansion_is_idempotent_and_keeps_existing_job_identity(self):
        previous, _, _ = self.fixtures()
        original = copy.deepcopy(previous)
        idle = {**previous["jobs"][0], "id": "idle", "animation_name": "idle",
                "uses": [{**previous["jobs"][0]["uses"][0], "role": "idle"}]}
        reaction = {**idle, "id": "reaction", "animation_name": "phone_bump",
                    "uses": [{**idle["uses"][0], "role": "clip"}]}
        spec = {"schema_version": 1, "id": "test", "selection_basis": "hints",
                "clips_per_workspot": 2, "workspots": [{"depot_path": "base/workspots/phone.workspot", "prefer": ["phone"]}]}
        with patch.object(batch, "make_plan", return_value={"jobs": [reaction, idle, previous["jobs"][0]]}):
            expanded = batch.expand_plan(previous, {}, Path("unused"), spec)
            again = batch.expand_plan(expanded, {}, Path("unused"), spec)
        self.assertEqual(expanded, again)
        self.assertEqual(previous, original)
        self.assertEqual(expanded["jobs"][0], original["jobs"][0])
        self.assertEqual(set(expanded["batch"]["coverage"][0]["jobs"]), {"idle", "clip"})

    def test_prepare_does_not_touch_existing_serialized_dependencies(self):
        plan, _, _ = self.fixtures()
        with tempfile.TemporaryDirectory() as directory:
            assets = Path(directory)
            for name in [plan["jobs"][0]["rig"], *plan["jobs"][0]["animsets"]]:
                path = batch.raw_path(assets / "raw", name)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("cached")
            with patch.object(batch.subprocess, "run") as run:
                self.assertEqual(batch.prepare_missing(plan, assets, Path("absent"), Path("absent")), {"required": 2, "new": 0})
                run.assert_not_called()

    def test_selection_prefers_characteristic_idle_and_action_over_generic_idle(self):
        previous, _, _ = self.fixtures()
        base = previous["jobs"][0]
        def job(key, name, role):
            return {**base, "id": key, "animation_name": name,
                    "uses": [{**base["uses"][0], "role": role}]}
        candidates = [job("generic", "stand", "idle"), job("characteristic", "rh_cigarette", "idle"),
                      job("variation", "rh_cigarette_drop_ash", "clip")]
        spec = {"schema_version": 1, "id": "test", "selection_basis": "hints",
                "clips_per_workspot": 2, "workspots": [{"depot_path": "base/workspots/phone.workspot", "prefer": ["cigarette"]}]}
        with patch.object(batch, "make_plan", return_value={"jobs": candidates}):
            expanded = batch.expand_plan({"jobs": []}, {}, Path("unused"), spec)
        self.assertEqual(expanded["batch"]["coverage"][0]["jobs"], ["characteristic", "variation"])


if __name__ == "__main__":
    unittest.main()
