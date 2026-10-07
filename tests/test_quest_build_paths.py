"""Depot input and publication boundaries for authored raw and binary resources."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import quest_build as build
import quest_compiler as compiler
from quest_compiler import QuestArtifact, QuestSpecError


def artifact(root: Path) -> QuestArtifact:
    raw = root / "source/raw/mod/test/one.questphase.json"
    archive = root / "source/archive/mod/test/one.questphase"
    return QuestArtifact(raw, archive, {"Header": {"ArchiveFileName": str(archive)}, "Data": {"value": 1}})


class QuestDepotPathTests(unittest.TestCase):
    def test_traversal_absolute_paths_and_windows_aliases_are_rejected(self):
        invalid = (
            r"mod\..\..\archive\mod\probe\phase.questphase",
            r"mod\folder\..\phase.questphase", r"mod\.\phase.questphase",
            "mod\\\\phase.questphase", "mod\\phase.questphase\\",
            r"mod\folder/../../archive/target", r"mod\C:\target", r"C:\mod\target",
            r"mod\name.", "mod\\name ", r"mod\NUL", r"mod\CON.questphase",
            r"mod\file:stream", "mod\\bad\x00name", r"mod\bad*name",
        )
        for value in invalid:
            with self.subTest(path=value):
                diagnostics = []
                self.assertEqual(compiler.validate_depot_path(value, field="phase_resource", stage_id="wait", diagnostics=diagnostics), "")
                self.assertEqual([item.code for item in diagnostics], ["invalid_depot_path"])
                with self.assertRaises(QuestSpecError):
                    compiler.resource_paths(value)

    def test_valid_depot_names_keep_the_existing_paths(self):
        for value in (r"mod\test\one.questphase", r"base\Folder Name\asset-name.json", r"ep1\quest\q301.scene"):
            with self.subTest(path=value):
                relative = Path(*value.split("\\"))
                project = ROOT / "projects/ghostline"
                self.assertEqual(compiler.resource_paths(value), (
                    project / "source/raw" / (str(relative) + ".json"), project / "source/archive" / relative,
                ))

    def test_manifest_escape_is_diagnosed_before_compilation(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "quest.json"
            path.write_text(json.dumps({"schema_version": 1, "id": "probe", "title": "Probe", "stages": [
                {"id": "wait", "type": "time_gate", "seconds": 1,
                 "phase_resource": r"mod\..\..\archive\mod\probe\phase.questphase"},
            ]}), encoding="utf-8")
            _, diagnostics = compiler.load_spec(path)
            self.assertIn("invalid_depot_path", {item.code for item in diagnostics})


class QuestPublicationPathTests(unittest.TestCase):
    def test_raw_cannot_replace_an_archive_and_archive_cannot_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            valid = artifact(root)
            packed_json = root / "source/archive/mod/test/localization.json"
            packed_json.parent.mkdir(parents=True)
            packed_json.write_bytes(b"CR2Woriginal localization")
            outside = root / "outside.bin"
            outside.write_bytes(b"original unrelated data")
            invalid = (
                QuestArtifact(packed_json, valid.archive_path, valid.document),
                QuestArtifact(valid.raw_path, outside, valid.document),
            )
            with patch.object(build, "ROOT", root), patch.object(build, "_convert") as convert:
                for value in invalid:
                    with self.subTest(raw=value.raw_path, archive=value.archive_path), self.assertRaisesRegex(ValueError, "destination must stay within"):
                        build.publish_build([value], namespace="test", deserialize=True)
                convert.assert_not_called()
            self.assertEqual(packed_json.read_bytes(), b"CR2Woriginal localization")
            self.assertEqual(outside.read_bytes(), b"original unrelated data")
            self.assertFalse(valid.raw_path.exists())
            self.assertFalse((root / "generated").exists())

    def test_binary_asset_destination_is_checked_before_conversion_or_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "rig.rid"
            source.write_bytes(b"CR2Wprerequisite")
            with patch.object(build, "ROOT", root), patch.object(build, "_convert") as convert:
                for target in (root / "escaped.rid", root / "source/raw/escaped.rid"):
                    with self.subTest(target=target), self.assertRaisesRegex(ValueError, "Binary asset destination"):
                        build.publish_build([artifact(root)], namespace="test", deserialize=True, binary_assets={target: source})
                    self.assertFalse(target.exists())
                convert.assert_not_called()
            self.assertFalse((root / "generated").exists())

    def test_isolated_relocation_is_idempotent_and_preserves_valid_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            candidate = Path(directory) / "candidate"
            with patch.object(build, "ROOT", root):
                source = artifact(root)
                relocated = build.relocate_artifacts([source], candidate)
                self.assertEqual(build.relocate_artifacts(relocated, candidate), relocated)
                outputs = build.publish_build(relocated, namespace="test", output_root=candidate)
            self.assertEqual(outputs, [(relocated[0].raw_path, relocated[0].archive_path)])
            self.assertTrue(relocated[0].raw_path.is_file())
            self.assertFalse(source.raw_path.exists())
            self.assertTrue((candidate / "generated/quest-builds/test/outputs.json").is_file())

    def test_candidate_roots_inside_source_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(build, "ROOT", root):
                for output in (root / "source", root / "source/raw/preview", root / "source/archive/preview"):
                    with self.subTest(output=output), self.assertRaisesRegex(ValueError, "outside.*source tree"):
                        build.publish_build([artifact(root)], namespace="test", output_root=output)
            self.assertFalse((root / "source").exists())

    def test_symlink_escape_is_rejected_by_both_resource_paths_and_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            outside = Path(directory) / "outside"
            outside.mkdir()
            link = root / "source/raw/mod"
            link.parent.mkdir(parents=True)
            try:
                link.symlink_to(outside, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"Directory symlinks are unavailable: {exc}")
            with patch.object(compiler, "ROOT", root), patch.object(build, "ROOT", root):
                with self.assertRaisesRegex(QuestSpecError, "escapes"):
                    compiler.resource_paths(r"mod\one.questphase")
                with self.assertRaisesRegex(ValueError, "Raw artifact destination"):
                    build.publish_build([artifact(root)], namespace="test")
            self.assertEqual(list(outside.iterdir()), [])

    def test_ownership_symlink_cannot_redirect_json_into_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "source/archive"
            archive.mkdir(parents=True)
            link = root / "generated/quest-builds"
            link.parent.mkdir()
            try:
                link.symlink_to(archive, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"Directory symlinks are unavailable: {exc}")
            with patch.object(build, "ROOT", root), self.assertRaisesRegex(ValueError, "Ownership record destination"):
                build.publish_build([artifact(root)], namespace="test")
            self.assertEqual(list(archive.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
