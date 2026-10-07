from __future__ import annotations

import contextlib
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import build_quest_reference as reference


class OfflineQuestReferenceTests(unittest.TestCase):
    def test_offline_snapshot_reproduces_pages_links_and_input_identities(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            journal, snapshot = root / "journal.json", root / "indexes.json"
            output, link_map = root / "pages", root / "link-map.json"
            journal.write_text(json.dumps([
                {"title": "The Streetkid", "type": "MainQuest", "path": "base/streetkid", "hash": 123,
                 "phases": [{"path": "phase/one", "objectives": [{
                     "path": "objective/talk", "type": "Objective", "description": "Talk to the contact",
                     "entries": [{"type": "MapPin", "ref": "contact/pin"}],
                 }]}]},
                {"title": "The Streetkid", "type": "MainQuest", "path": "ep1/streetkid", "hash": 999},
            ]), encoding="utf-8")
            snapshot.write_text(json.dumps({"schema_version": 1, "indexes": {
                "main-jobs": [{"title": "The Street Kid", "url": "https://www.ign.com/wikis/cyberpunk-2077/The_Streetkid"}],
                "side-jobs": [{"title": "Retained unmatched link", "url": "https://www.ign.com/wikis/cyberpunk-2077/Unknown"}],
                "gigs": [],
            }}), encoding="utf-8")
            arguments = ["--quest-json", str(journal), "--index-snapshot", str(snapshot),
                         "--output", str(output), "--link-map", str(link_map)]
            # Offline generation must work without the optional networking and
            # HTML packages installed, even when the source indexes have moved.
            with mock.patch.dict(sys.modules, {"requests": None, "bs4": None}), \
                 mock.patch.object(reference, "get_index_links", side_effect=AssertionError("network access")), \
                 contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(reference.main(arguments), 0)
                first = {path.name: path.read_bytes() for path in output.iterdir()}
                first["link-map.json"] = link_map.read_bytes()
                self.assertEqual(reference.main(arguments), 0)
            second = {path.name: path.read_bytes() for path in output.iterdir()}
            second["link-map.json"] = link_map.read_bytes()
            self.assertEqual(first, second)
            mapping = json.loads(link_map.read_text(encoding="utf-8"))
            self.assertEqual(mapping["indexes"]["main-jobs"]["matches"][0]["quest_path"], "base/streetkid")
            self.assertEqual(len(mapping["indexes"]["side-jobs"]["unmatched_index_links"]), 1)
            for name, path in (("journal", journal), ("index_snapshot", snapshot),
                               ("generator", Path(reference.__file__).resolve())):
                self.assertEqual(mapping["inputs"][name]["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
            page = (output / "main-jobs.md").read_text(encoding="utf-8")
            self.assertIn("Talk to the contact", page)
            self.assertIn("contact/pin", page)
            self.assertNotIn("ep1/streetkid", page)

    def test_invalid_snapshot_fails_before_replacing_existing_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            journal, snapshot, output = root / "journal.json", root / "indexes.json", root / "pages"
            journal.write_text("[]", encoding="utf-8")
            output.mkdir()
            existing = output / "main-jobs.md"
            existing.write_text("previous valid reference", encoding="utf-8")
            for invalid in ({"schema_version": 2}, {"schema_version": 1, "indexes": []},
                            {"schema_version": 1, "indexes": {"main-jobs": [], "side-jobs": [], "gigs": [{}]}}):
                with self.subTest(snapshot=invalid):
                    snapshot.write_text(json.dumps(invalid), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        reference.main(["--quest-json", str(journal), "--index-snapshot", str(snapshot),
                                        "--output", str(output), "--link-map", str(root / "links.json")])
                    self.assertEqual(existing.read_text(encoding="utf-8"), "previous valid reference")


if __name__ == "__main__":
    unittest.main()
