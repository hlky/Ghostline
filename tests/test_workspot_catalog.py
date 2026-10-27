"""Evidence boundaries and real-resource regression tests for workspot discovery."""
import copy
from contextlib import closing
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import workspot_catalog as catalog


def cname(value):
    return {"$type": "CName", "$value": value}


def resource(value):
    return {"DepotPath": {"$type": "ResourcePath", "$value": value}}


def fixture():
    # Deliberately use unrelated entry IDs and handle IDs; engines use entry IDs.
    return {"Data": {"RootChunk": {
        "$type": "workWorkspotResource",
        "workspotTree": {"HandleRefId": "90"},
        "definitions": [{"HandleId": "90", "Data": {
            "$type": "workWorkspotTree",
            "finalAnimsets": [{"rig": resource("base/rigs/man.rig"), "animations": {
                "gameplay": [{"animSet": resource("base/anims/idle.anims")}]}}],
            "globalProps": [{"prop": resource("base/props/tablet.ent")}],
            "rootEntry": {"HandleId": "91", "Data": {
                "$type": "workSequence", "id": {"id": 1}, "list": [
                    {"HandleId": "92", "Data": {"$type": "workEntryAnim", "id": {"id": 17}, "animName": cname("sit_down")}},
                    {"HandleId": "93", "Data": {"$type": "workSequence", "id": {"id": 23}, "idleAnim": cname("hands_on_knees"), "loopInfinitely": 1, "list": [
                        {"HandleId": "94", "Data": {"$type": "workAnimClipWithItem", "id": {"id": 24}, "animName": cname("use_tablet"), "itemActions": [{"Data": {"$type": "workEquipItemAction", "item": cname("Items.Tablet")}}]}},
                        {"HandleRefId": "94"},
                    ]}},
                    {"HandleId": "95", "Data": {"$type": "workExitAnim", "id": {"id": 31}, "animName": cname("stand_up")}},
                ]}},
        }}],
    }}}


class WorkspotCatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.raw = self.root / "raw"
        self.path = self.raw / "base/workspots/unhelpful.workspot.json"
        self.path.parent.mkdir(parents=True)
        self.path.write_text(json.dumps(fixture()), encoding="utf-8")
        self.notes = self.root / "annotations.json"
        self.notes.write_text('{"schema_version":1,"workspots":{}}', encoding="utf-8")

    def test_shared_handles_entry_ids_and_prop_evidence(self):
        record = catalog.inspect_workspot(self.path, self.raw)
        self.assertEqual(record["entry_animation_ids"], [17])
        self.assertEqual(record["loop_entry_ids"], [23])
        self.assertEqual(record["exit_animation_ids"], [31])
        self.assertEqual(record["animations"], ["hands_on_knees", "sit_down", "stand_up", "use_tablet"])
        self.assertEqual(record["entry_counts"]["workAnimClipWithItem"], 1)
        self.assertIn("base\\props\\tablet.ent", record["resource_references"])
        self.assertEqual(record["rigs"], ["base\\rigs\\man.rig"])
        self.assertNotIn("annotation", record)

    def test_transition_sentinel_is_not_a_clip_and_sync_entry_is_an_entry(self):
        doc = fixture()
        tree = doc["Data"]["RootChunk"]["definitions"][0]["Data"]
        tree["rootEntry"]["Data"]["idleAnim"] = cname("<no_auto_transition>")
        tree["rootEntry"]["Data"]["list"][0]["Data"]["$type"] = "workSyncMasterEntryAnim"
        self.path.write_text(json.dumps(doc), encoding="utf-8")
        record = catalog.inspect_workspot(self.path, self.raw)
        self.assertNotIn("<no_auto_transition>", record["animations"])
        self.assertEqual(record["entry_animation_ids"], [17])

    def test_turn_and_reaction_face_animations_are_searchable(self):
        doc = fixture()
        sequence = doc["Data"]["RootChunk"]["definitions"][0]["Data"]["rootEntry"]["Data"]
        sequence["list"].append({"Data": {"$type": "workLookAtDrivenTurn", "id": {"id": 42}, "turnAnimName": cname("turn_toward_speaker")}})
        sequence["facialIdleFemaleAnimation"] = cname("reaction_face")
        self.path.write_text(json.dumps(doc), encoding="utf-8")
        record = catalog.inspect_workspot(self.path, self.raw)
        self.assertIn("turn_toward_speaker", record["animations"])
        self.assertIn("reaction_face", record["animations"])

    def test_search_finds_animation_instead_of_filename_and_survives_rebuild(self):
        out = self.root / "out"
        first = catalog.build(self.raw, out, self.notes)
        result = catalog.search(out / "workspots.sqlite3", "hands knees")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["depot_path"], "base\\workspots\\unhelpful.workspot")
        self.assertEqual(len(catalog.search(out / "workspots.sqlite3", "props tablet")), 1)
        self.assertEqual(catalog.search(out / "workspots.sqlite3", '" OR 1=1 --'), [])
        second = catalog.build(self.raw, out, self.notes)
        self.assertEqual(first, second)
        with closing(sqlite3.connect(out / "workspots.sqlite3")) as db:
            self.assertEqual(db.execute("SELECT count(*) FROM workspots").fetchone()[0], 1)

    def test_stale_review_cannot_claim_current_runtime_verification(self):
        doc = {"schema_version": 1, "workspots": {"base\\workspots\\unhelpful.workspot": {
            "label": "Seated tablet use", "status": "runtime_verified", "source_sha256": "old",
            "evidence": ["capture.mp4"],
        }}}
        self.notes.write_text(json.dumps(doc), encoding="utf-8")
        record = catalog.build(self.raw, self.root / "out", self.notes)["workspots"][0]
        self.assertTrue(record["annotation_stale"])
        self.assertEqual(record["review_status"], "stale")
        self.assertEqual(catalog.read(self.notes), doc)

    def test_review_requires_evidence_and_hash(self):
        self.notes.write_text(json.dumps({"schema_version": 1, "workspots": {
            "base\\x.workspot": {"status": "visually_reviewed"}
        }}), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "requires evidence"):
            catalog.annotations(self.notes)

    def test_decode_failure_is_reported_alongside_valid_resources(self):
        broken = copy.deepcopy(fixture())
        broken["Data"]["RootChunk"]["workspotTree"]["HandleRefId"] = "missing"
        (self.path.parent / "broken.workspot.json").write_text(json.dumps(broken), encoding="utf-8")
        result = catalog.build(self.raw, self.root / "out", self.notes)
        self.assertEqual(result["summary"]["resources"], 1)
        self.assertEqual(result["summary"]["failures"], 1)
        self.assertIn("unresolved handle", result["failures"][0]["error"])

    def test_usage_preserves_exact_reference_pointer(self):
        usage = self.root / "scenes"
        usage.mkdir()
        (usage / "example.scene.json").write_text(json.dumps({"workspots": [
            {"workspotResource": resource("base/workspots/unhelpful.workspot")}
        ]}), encoding="utf-8")
        result = catalog.build(self.raw, self.root / "out", self.notes, usage_roots=[usage])
        self.assertEqual(result["summary"]["with_usage"], 1)
        ref = result["workspots"][0]["usage"][0]
        self.assertEqual(ref["pointer"], "/workspots/0/workspotResource")
        self.assertEqual(len(ref["sha256"]), 64)

    def test_missing_decode_is_a_coverage_failure(self):
        binary = self.root / "binary/base/workspots"
        binary.mkdir(parents=True)
        (binary / "not_decoded.workspot").write_bytes(b"CR2W")
        result = catalog.build(self.raw, self.root / "out", self.notes, self.root / "binary")
        self.assertEqual(result["summary"]["failures"], 1)
        self.assertIn("Missing decoded", result["failures"][0]["error"])

    def test_opaque_tree_is_rejected(self):
        doc = fixture()
        doc["Data"]["RootChunk"]["definitions"][0]["Data"]["unknown"] = {"$rawData": "opaque"}
        self.path.write_text(json.dumps(doc), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "opaque workspot data"):
            catalog.inspect_workspot(self.path, self.raw)

    def test_checked_gqt006_custom_resource(self):
        raw = ROOT / "projects/test-quests/gqt006/source/raw"
        path = raw / "mod/gqt006/workspots/gqt006_goth_baddie_down.workspot.json"
        record = catalog.inspect_workspot(path, raw)
        self.assertEqual(record["depot_path"], "mod\\gqt006\\workspots\\gqt006_goth_baddie_down.workspot")
        self.assertTrue(record["animations"])
        self.assertTrue(record["animsets"])
        self.assertTrue(record["entries"])

    def test_html_escapes_untrusted_embedded_script(self):
        data = {"summary": {"failures": 0}, "workspots": [{"depot_path": "base\\example.workspot", "source": {"binary_sha256": "hash"}, "annotation": {"label": "</script><script>alert(1)</script>"}}]}
        target = self.root / "review.html"
        catalog.review(data, target)
        self.assertNotIn("</script><script>alert", target.read_text(encoding="utf-8"))

    def test_report_embeds_only_source_and_media_matched_previews(self):
        out = self.root / "out"
        data = catalog.build(self.raw, out, self.notes)
        record = data["workspots"][0]
        key = "a" * 20
        folder = out / "previews" / key
        folder.mkdir(parents=True)
        for name in ("preview.mp4", "contact.png"):
            (folder / name).write_bytes(b"test-media")
        plan = {"jobs": [{"id": key, "animation_name": "visible_clip_test", "uses": [{
            "workspot": record["depot_path"], "workspot_sha256": record["source"]["raw_sha256"], "role": "idle"
        }]}]}
        (out / "preview-plan.json").write_text(json.dumps(plan))
        (out / "previews/results.json").write_text(json.dumps([{
            "id": key, "status": "rendered_proxy", "outputs": {name: catalog.digest(folder / name) for name in ("preview.mp4", "contact.png")}
        }]))
        target = out / "review.html"
        catalog.review(data, target)
        self.assertIn("visible_clip_test", target.read_text(encoding="utf-8"))
        (folder / "preview.mp4").write_bytes(b"changed-media")
        catalog.review(data, target)
        self.assertNotIn("visible_clip_test", target.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
