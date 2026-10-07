from __future__ import annotations

import copy
import io
import json
import struct
import sys
import tempfile
import unittest
from collections import Counter
from contextlib import redirect_stderr
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import character_builder as builder
import character_cache as cache
import character_full_preview as full_preview
import character_ui as ui
import braindance_scene
import kimodo_braindance as kimodo


def glb_bytes() -> bytes:
    payload = json.dumps({"meshes": []}).encode()
    return struct.pack("<4sIIII", b"glTF", 2, 20 + len(payload), len(payload), 0x4E4F534A) + payload


class CharacterIdentityTests(unittest.TestCase):
    def test_ui_preserves_identity_and_validators_reject_mismatched_outputs(self):
        manifest = builder.load_manifest(ROOT / "projects/shared/ghostline-runtime/characters/patch.character.json")
        edited = copy.deepcopy(manifest)
        edited.update(id="clone", namespace=r"mod\ghostline\characters\clone")
        merged = ui.editable_manifest(edited)
        self.assertEqual((merged["id"], merged["namespace"]), (manifest["id"], manifest["namespace"]))
        catalog = builder.load_catalog(edited)
        report = builder.validate_manifest(edited, catalog)
        self.assertFalse(report.ok)
        self.assertTrue(any("must match character identity" in error for error in report.errors))
        entity, appearance, *_ = builder.generate_documents(edited, catalog)
        self.assertFalse(builder.validate_generated(edited, entity, appearance).ok)

    def test_build_parses_each_input_once_and_keeps_copies_isolated(self):
        reads = Counter()
        original = builder._read_json_document

        def read(path):
            reads[path.resolve()] += 1
            return original(path)

        with mock.patch.object(builder, "_read_json_document", side_effect=read):
            with builder.build_session():
                manifest = builder.load_manifest(ROOT / "projects/test-quests/gqt006/characters/goth_baddie.character.json")
                catalog = builder.load_catalog(manifest)
                self.assertTrue(builder.validate_manifest(manifest, catalog).ok)
                entity, appearance, *_ = builder.generate_documents(manifest, catalog)
                self.assertTrue(builder.validate_generated(manifest, entity, appearance).ok)
                donor_path = ROOT / "quests/templates/characters/components/donors/npv-female.app.json"
                altered = builder.read_json(donor_path)
                altered.clear()
                self.assertIn("Data", builder.read_json(donor_path))
        self.assertTrue(reads)
        self.assertEqual(set(reads.values()), {1})


class CharacterCacheTests(unittest.TestCase):
    def test_failed_promotion_rolls_back_every_previous_file(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "cache"
            output.mkdir()
            paths = [Path("geometry.glb"), Path("manifest.json")]
            for path in paths:
                (output / path).write_bytes(b"old")

            def export(staging):
                for path in paths:
                    (staging / path).write_bytes(b"new")

            replace = Path.replace

            def fail_manifest(path, target):
                if path.name == "manifest.json" and ".previous" not in path.parts:
                    raise PermissionError("locked manifest")
                return replace(path, target)

            with mock.patch.object(Path, "replace", new=fail_manifest):
                with self.assertRaises(PermissionError):
                    cache.refresh_export(output, paths, export)
            self.assertEqual([(output / path).read_bytes() for path in paths], [b"old", b"old"])

    def test_head_preview_failed_refresh_preserves_geometry_and_fingerprint(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "head.morphtarget").write_bytes(b"changed")
            tool = root / "tool.exe"
            tool.write_bytes(b"tool")
            game = root / "game"
            game.mkdir()
            output = root / "preview"
            (output / "models").mkdir(parents=True)
            model = output / "models/head.morphtarget.glb"
            model.write_bytes(glb_bytes())
            old_cache = output / "preview-cache.json"
            old_cache.write_text('{"cache_key":"old"}')
            manifest = {"id": "test", "frame": "male_average", "head": {
                "morphtarget_source": str(source), "morphtargets": ["head.morphtarget"],
                "preview_morphtargets": ["head.morphtarget"],
            }}
            with mock.patch.object(builder, "load_manifest", return_value=manifest), \
                 mock.patch.object(builder, "validate_manifest", return_value=builder.ValidationReport()), \
                 mock.patch.object(builder.subprocess, "run", return_value=mock.Mock(returncode=1, stdout="", stderr="failed")):
                with self.assertRaises(builder.CharacterBuildError):
                    builder.prepare_head_preview(root / "manifest.json", output, tool, game)
            self.assertEqual(model.read_bytes(), glb_bytes())
            self.assertEqual(json.loads(old_cache.read_text())["cache_key"], "old")

    def test_head_build_refreshes_unverified_morphs_before_blender(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            morph = root / "head.morphtarget"
            mesh = root / builder.mesh_name_for_morphtarget(morph.name)
            template = root / "head.blend"
            tool = root / "tool.exe"
            for path in (morph, mesh, template, tool):
                path.write_bytes(b"source")
            workspace = root / "work"
            old = workspace / "head/morphtargets/head.morphtarget.glb"
            old.parent.mkdir(parents=True)
            old.write_bytes(glb_bytes())
            manifest = {"frame": "male_average", "head": {
                "shapes": {name: 1 for name in builder.SHAPE_NAMES},
                "blend_template": str(template), "morphtarget_source": str(root),
                "mesh_source": str(root), "morphtargets": [morph.name],
            }}
            with mock.patch.object(builder, "load_manifest", return_value=manifest), \
                 mock.patch.object(builder, "validate_manifest", return_value=builder.ValidationReport()), \
                 mock.patch.object(builder.subprocess, "run", return_value=mock.Mock(returncode=1, stdout="", stderr="failed")) as run:
                result = builder.head_build(root / "manifest.json", workspace, {}, tool, tool, root, False)
            self.assertFalse(result["ok"])
            self.assertEqual(run.call_count, 1)
            self.assertEqual(run.call_args.args[0][1], "export")
            self.assertEqual(old.read_bytes(), glb_bytes())

    def test_full_preview_tracks_nested_archive_changes_and_required_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "game/archive/pc/content/base.archive"
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b"old")
            tool = root / "tool.exe"
            tool.write_bytes(b"tool")
            layers = [{"depot_path": r"base\test.mesh"}]
            before = full_preview.preview_cache_key(layers, root / "generated", tool, root / "game")
            archive.write_bytes(b"new archive contents")
            after = full_preview.preview_cache_key(layers, root / "generated", tool, root / "game")
            self.assertNotEqual(before, after)
            manifest = root / "cache.json"
            manifest.write_text(json.dumps({"cache_key": after}))
            self.assertFalse(cache.cache_matches(manifest, after, [root / "missing.glb"]))


class MotionPreflightTests(unittest.TestCase):
    def test_default_braindance_fixture_is_shared_and_exists(self):
        self.assertEqual(kimodo.DEFAULT_SPEC, braindance_scene.DEFAULT_SPEC)
        self.assertTrue(braindance_scene.DEFAULT_SPEC.is_file())
        for command in ("validate", "plan", "build", "bake"):
            self.assertEqual(braindance_scene.parse_args([command]).spec, braindance_scene.DEFAULT_SPEC)

    def test_incompatible_kimodo_bake_is_rejected_before_subprocess_or_dry_run(self):
        spec = {"actors": [{"id": "patch"}], "outputs": {"blend": "base.blend"}}
        joints = ("Hips", "Spine1", "LeftArm", "RightArm", "LeftLeg", "RightLeg")
        for dry in ([], ["--dry-run"]):
            with mock.patch.object(kimodo, "load_spec", return_value=spec), \
                 mock.patch.object(kimodo, "inspect_bvh", return_value=(joints, 100)), \
                 mock.patch.object(kimodo, "run_checked") as run, redirect_stderr(io.StringIO()):
                result = kimodo.main(["--bvh", "clip.bvh", "--output-blend", "different.blend", "--bake-after", *dry])
            self.assertEqual(result, 1)
            run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
