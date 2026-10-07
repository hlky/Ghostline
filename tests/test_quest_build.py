from __future__ import annotations

import contextlib
import copy
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import artifact_io
import quest_build as build
from quest_authoring import AuthoringError, compose, normalize_spec, resolve_bindings
from quest_compiler import QuestArtifact
from quest_content import journal_template_path
from quest_journal import template_names


def artifact(root: Path, name: str) -> QuestArtifact:
    raw = root / "source/raw/mod/test" / f"{name}.questphase.json"
    archive = root / "source/archive/mod/test" / f"{name}.questphase"
    return QuestArtifact(
        raw,
        archive,
        {"Header": {"ArchiveFileName": str(archive)}, "Data": {"value": name}},
    )


class QuestBuildTests(unittest.TestCase):
    def test_preview_relocation_is_idempotent_and_preserves_source_document(self):
        source = artifact(ROOT, "one")
        original = copy.deepcopy(source.document)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            result = build.relocate_artifacts([source], output)
            again = build.relocate_artifacts(result, output)
            self.assertEqual(result, again)
            self.assertEqual(
                result[0].raw_path, output / "source/raw/mod/test/one.questphase.json"
            )
            self.assertEqual(
                result[0].document["Header"]["ArchiveFileName"],
                str(result[0].archive_path),
            )
        self.assertEqual(source.document, original)

    def test_raw_and_binary_publication_roll_back_together(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            item = artifact(root, "one")
            item.raw_path.parent.mkdir(parents=True)
            item.archive_path.parent.mkdir(parents=True)
            item.raw_path.write_bytes(b"old raw")
            item.archive_path.write_bytes(b"CR2Wold")
            rig = root / "source/archive/mod/test/rig.rid"
            rig.write_bytes(b"CR2Wold rig")
            rig_source = root / "new.rid"
            rig_source.write_bytes(b"CR2Wnew rig")
            real_replace = artifact_io.os.replace

            def replace(source, target):
                if (
                    Path(target) == item.archive_path
                    and b"CR2Wnew" == Path(source).read_bytes()
                ):
                    raise OSError("archive replacement failed")
                return real_replace(source, target)

            def convert(raw, candidate, template, **options):
                candidate.write_bytes(b"CR2Wnew")

            with (
                mock.patch.object(build, "ROOT", root),
                mock.patch.object(build, "_convert", side_effect=convert),
                mock.patch.object(artifact_io.os, "replace", side_effect=replace),
            ):
                with self.assertRaisesRegex(OSError, "archive replacement failed"):
                    build.publish_build(
                        [item],
                        namespace="test",
                        deserialize=True,
                        binary_assets={rig: rig_source},
                    )
            self.assertEqual(item.raw_path.read_bytes(), b"old raw")
            self.assertEqual(item.archive_path.read_bytes(), b"CR2Wold")
            self.assertEqual(rig.read_bytes(), b"CR2Wold rig")
            self.assertFalse(
                (root / "generated/quest-builds/test/outputs.json").exists()
            )

    def test_missing_prerequisite_and_duplicate_archive_fail_before_conversion(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            item = artifact(root, "one")
            other = QuestArtifact(
                root / "second.json", item.archive_path, item.document
            )
            with (
                mock.patch.object(build, "ROOT", root),
                mock.patch.object(build, "_convert") as convert,
            ):
                with self.assertRaisesRegex(ValueError, "duplicate archive"):
                    build.publish_build(
                        [item, other], namespace="test", deserialize=True
                    )
                with self.assertRaises(FileNotFoundError):
                    build.publish_build(
                        [item],
                        namespace="test",
                        deserialize=True,
                        binary_assets={root / "rig.rid": root / "missing.rid"},
                    )
                bad = root / "bad.rid"
                bad.write_bytes(b"not a resource")
                with self.assertRaisesRegex(ValueError, "not a CR2W resource"):
                    build.publish_build(
                        [item],
                        namespace="test",
                        deserialize=True,
                        binary_assets={root / "rig.rid": bad},
                    )
                convert.assert_not_called()
                self.assertFalse(item.raw_path.exists())

    def test_new_native_layout_uses_wolvenkit_fallback_and_requires_cr2w(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw, template, candidate = (
                root / "one.json",
                root / "template",
                root / "one",
            )
            template.write_bytes(b"CR2Wdonor")
            document = {"Header": {}, "Data": {"RootChunk": {"$type": "Probe", "value": 1}}}
            raw.write_text(json.dumps(document), encoding="utf-8")
            schema = root / "schema.json"
            schema.write_text("{}", encoding="utf-8")

            def fallback(command, **options):
                if "-d" in command:
                    candidate.write_bytes(b"CR2Wfallback")
                else:
                    (Path(command[-1]) / "one.json").write_text(json.dumps(document), encoding="utf-8")

            with (
                mock.patch("ghostline_red.ensure_schema", return_value=schema),
                mock.patch.object(
                    build,
                    "native_deserialize",
                    side_effect=subprocess.CalledProcessError(1, ["native"]),
                ),
                mock.patch.object(build.subprocess, "run", side_effect=fallback) as run,
            ):
                build._convert(
                    raw,
                    candidate,
                    template,
                    serializer="native",
                    wolvenkit=Path("wkit"),
                )
                self.assertEqual(run.call_args_list[0].args[0][:3], ["wkit", "cr2w", "-d"])
                self.assertEqual(run.call_args_list[1].args[0][:3], ["wkit", "cr2w", "-s"])
                self.assertEqual(candidate.read_bytes(), b"CR2Wfallback")
            with mock.patch("ghostline_red.ensure_schema", return_value=schema), mock.patch.object(
                build.subprocess,
                "run",
                side_effect=lambda *args, **kw: candidate.write_bytes(b"bad"),
            ):
                with self.assertRaisesRegex(RuntimeError, "invalid WolvenKit"):
                    build._convert(
                        raw,
                        candidate,
                        None,
                        serializer="wolvenkit",
                        wolvenkit=Path("wkit"),
                    )

    def test_native_voice_tag_loss_uses_the_verified_wolvenkit_fallback(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw, template, candidate = root / "one.json", root / "template", root / "one"
            template.write_bytes(b"CR2Wdonor")
            document = {"Header": {}, "Data": {"RootChunk": {"$type": "Probe", "voicetagId": {"$type": "scnVoicetagId", "id": "13635884494759391413"}}}}
            raw.write_text(json.dumps(document), encoding="utf-8")
            schema = root / "schema.json"
            schema.write_text("{}", encoding="utf-8")

            def native(*args, **options):
                candidate.write_bytes(b"CR2Wnative")

            def oracle(command, **options):
                if "-d" in command:
                    candidate.write_bytes(b"CR2Wwolvenkit")
                else:
                    decoded = json.loads(json.dumps(document))
                    if candidate.read_bytes() == b"CR2Wnative":
                        decoded["Data"]["RootChunk"]["voicetagId"]["id"] = "0"
                    (Path(command[-1]) / "one.json").write_text(json.dumps(decoded), encoding="utf-8")

            with (
                mock.patch("ghostline_red.ensure_schema", return_value=schema),
                mock.patch.object(build, "native_deserialize", side_effect=native),
                mock.patch.object(build.subprocess, "run", side_effect=oracle),
            ):
                build.convert_resource(raw, candidate, template, serializer="native", wolvenkit=Path("wkit"))
            self.assertEqual(candidate.read_bytes(), b"CR2Wwolvenkit")

    def test_planned_build_requires_isolated_destination(self):
        manifest = ROOT / "projects/ghostline/quests/gq003/implementation/quest.json"
        with (
            mock.patch.object(build, "compile_manifest_artifacts") as compile_mock,
            contextlib.redirect_stderr(io.StringIO()),
        ):
            for options in (
                ["--allow-planned"],
                ["--allow-planned", "--out-root", str(ROOT)],
                ["--allow-planned", "--out-root", str(ROOT / "source/raw/prototype")],
            ):
                with self.subTest(options=options), self.assertRaises(SystemExit):
                    build.main(manifest, r"mod\gq003\phases\gq003.questphase", options)
            compile_mock.assert_not_called()


class MigratedCompositionTests(unittest.TestCase):
    def test_all_ten_active_quests_use_composition_and_keep_planned_status(self):
        paths = [
            *sorted((ROOT / "projects/test-quests").rglob("*.quest.json")),
            *sorted((ROOT / "projects/ghostline/quests").glob("**/implementation/quest.json")),
        ]
        self.assertEqual(len(paths), 10)
        for path in paths:
            raw = json.loads(path.read_text(encoding="utf-8"))
            with self.subTest(path=path):
                self.assertIn("composition", raw)
                self.assertTrue(resolve_bindings(raw)["objectives"])
                if "gq003" in path.parts:
                    self.assertEqual(
                        {stage["status"] for stage in normalize_spec(raw)["stages"]},
                        {"planned"},
                    )

    def test_shared_phase_and_explicit_phone_ids_preserve_order(self):
        raw = json.loads(
            (ROOT / "projects/ghostline/quests/gq001/implementation/quest.json").read_text(
                encoding="utf-8"
            )
        )
        result = compose(raw)
        objectives = list(result.bindings["objectives"].values())
        cache = [item for item in objectives if item["phase_id"] == "gq001_02"]
        self.assertEqual(len(cache), 3)
        phones = [
            entry
            for contact in result.bindings["contacts"].values()
            for thread in contact["threads"].values()
            for entry in thread["entries"].values()
        ]
        self.assertTrue(any(entry["id"].startswith("01_") for entry in phones))
        duplicate = copy.deepcopy(raw)
        duplicate["composition"]["objectives"]["duplicate"] = copy.deepcopy(
            next(iter(raw["composition"]["objectives"].values()))
        )
        with self.assertRaisesRegex(AuthoringError, "Duplicate objective path"):
            compose(duplicate)

    def test_custom_donors_and_file_donor_are_bound_in_evidence(self):
        modern = json.loads(
            (ROOT / "projects/test-quests/gqt006/gqt006_goth_baddie_cyberpsycho.quest.json").read_text(
                encoding="utf-8"
            )
        )
        legacy = json.loads(
            (ROOT / "projects/test-quests/gqt001/gqt001_signal_delay.quest.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertIn("regina_cyberpsycho", template_names(modern["composition"]))
        self.assertIn("file_group", template_names(legacy["composition"]))
        from quest_catalog import record_build

        receipt = record_build(
            ROOT / "projects/test-quests/gqt006/gqt006_goth_baddie_cyberpsycho.quest.json"
        )
        bound = receipt["entries"][0]["resources"]
        self.assertIn(
            journal_template_path("regina_cyberpsycho").relative_to(ROOT).as_posix(),
            bound,
        )


if __name__ == "__main__":
    unittest.main()
