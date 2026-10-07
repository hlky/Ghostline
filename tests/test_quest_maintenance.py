"""Independent regression checks for authoring boundaries and publication failures."""

from __future__ import annotations

import copy
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import artifact_io
import generate_scene
import generate_world
import quest_compiler as compiler
import quest_content
import quest_stages
from jsonschema import Draft202012Validator


class ArtifactPublicationTests(unittest.TestCase):
    def test_serialization_failure_preserves_every_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            first, second = (
                Path(directory) / name for name in ("first.json", "second.json")
            )
            first.write_bytes(b"original")
            with self.assertRaises(TypeError):
                artifact_io.publish_json_artifacts(
                    {first: {"new": 1}, second: object()}
                )
            self.assertEqual(first.read_bytes(), b"original")
            self.assertFalse(second.exists())
            self.assertEqual(list(Path(directory).iterdir()), [first])

    def test_failed_later_replace_rolls_back_previous_files_and_ownership(self):
        with tempfile.TemporaryDirectory() as directory:
            first, second, ownership = (
                Path(directory) / name
                for name in ("first.json", "second.json", "outputs.json")
            )
            first.write_bytes(b"original")
            artifact_io.atomic_write_json(
                ownership,
                {"schema_version": 1, "outputs": [str(first)], "obsolete": []},
            )
            previous_ownership = ownership.read_bytes()
            replace = os.replace

            def fail_second(source, destination):
                if Path(destination) == second:
                    raise OSError("injected publication failure")
                replace(source, destination)

            with patch.object(artifact_io.os, "replace", side_effect=fail_second):
                with self.assertRaisesRegex(OSError, "injected"):
                    artifact_io.publish_json_artifacts(
                        {first: {"new": 1}, second: {}}, ownership_path=ownership
                    )
            self.assertEqual(first.read_bytes(), b"original")
            self.assertFalse(second.exists())
            self.assertEqual(ownership.read_bytes(), previous_ownership)
            self.assertFalse(list(Path(directory).glob("*.tmp")))

    def test_rollback_failure_retains_recovery_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            first, second = (
                Path(directory) / name for name in ("first.json", "second.json")
            )
            first.write_bytes(b"original")
            replace = os.replace
            calls = 0

            def fail_after_first(source, destination):
                nonlocal calls
                calls += 1
                if calls > 1:
                    raise OSError("injected locked destination")
                replace(source, destination)

            with patch.object(artifact_io.os, "replace", side_effect=fail_after_first):
                with self.assertRaisesRegex(RuntimeError, "backup:"):
                    artifact_io.publish_json_artifacts({first: {}, second: {}})
            backups = list(Path(directory).glob("*.tmp"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_bytes(), b"original")

    def test_retired_outputs_are_reported_and_retained_and_unchanged_files_not_rewritten(
        self,
    ):
        with tempfile.TemporaryDirectory() as directory:
            first, second, ownership = (
                Path(directory) / name
                for name in ("first.json", "second.json", "outputs.json")
            )
            artifact_io.publish_json_artifacts(
                {first: {"value": 1}, second: {}}, ownership_path=ownership
            )
            modified = first.stat().st_mtime_ns
            report = artifact_io.publish_json_artifacts(
                {first: {"value": 1}}, ownership_path=ownership
            )
            self.assertEqual(report.obsolete_paths, (second.resolve(),))
            self.assertTrue(second.is_file())
            self.assertEqual(first.stat().st_mtime_ns, modified)
            report = artifact_io.publish_json_artifacts(
                {first: {"value": 1}}, ownership_path=ownership
            )
            self.assertEqual(report.obsolete_paths, (second.resolve(),))

    def test_alias_destinations_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "one.json"
            alias = Path(directory) / "nested" / ".." / "one.json"
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                artifact_io.publish_json_artifacts({first: {}, alias: {}})
            self.assertFalse(first.exists())

    def test_late_phase_failure_has_no_side_effects(self):
        spec, diagnostics = compiler.load_spec(
            ROOT / "projects/ghostline/quests/gq001/implementation/quest.json"
        )
        self.assertFalse([item for item in diagnostics if item.level == "error"])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            existing = root / "root.questphase.json"
            existing.write_bytes(b"previous root")
            last = spec.stages[-1].id

            def fail(_stage, _archive):
                raise ValueError("late child failed")

            with self.assertRaisesRegex(ValueError, "late child"):
                compiler.compile_artifacts(
                    spec,
                    existing,
                    root / "archive",
                    child_root=root / "children",
                    stage_overrides={last: fail},
                )
            self.assertEqual(existing.read_bytes(), b"previous root")
            self.assertFalse((root / "children").exists())


class AuthoringContractTests(unittest.TestCase):
    def test_current_manifests_conform_to_schema_and_compiler(self):
        validator = Draft202012Validator(quest_stages.SCHEMA)
        manifests = sorted(
            path
            for directory in (ROOT / "quests", ROOT / "projects")
            for path in directory.rglob("*.json")
            if path.name == "quest.json" or path.name.endswith(".quest.json")
        )
        self.assertGreaterEqual(len(manifests), 14)
        for path in manifests:
            with self.subTest(manifest=str(path.relative_to(ROOT))):
                raw = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(list(validator.iter_errors(raw)), [])
                from quest_authoring import normalize_spec

                normalized = normalize_spec(raw)
                self.assertNotIn("composition", normalized)
                self.assertEqual(list(validator.iter_errors(normalized)), [])
                spec, diagnostics = compiler.load_spec(path)
                self.assertIsNotNone(spec)
                self.assertFalse(
                    [item for item in diagnostics if item.level == "error"]
                )

    def test_registry_matches_generated_stage_reference(self):
        text = (ROOT / "tools/quest_spec.md").read_text(encoding="utf-8")
        self.assertIn(quest_stages.reference_table(), text)
        self.assertEqual(
            set(quest_stages.STAGE_REGISTRY), set(quest_stages.IMPLEMENTATIONS)
        )
        for name, definition in quest_stages.STAGE_REGISTRY.items():
            self.assertEqual(
                definition.fields, set(definition.structure["properties"]) - {"type"}
            )

    def test_meeting_paths_are_typed_child_contracts_and_description_is_root_owned(
        self,
    ):
        spec, _ = compiler.load_spec(
            ROOT / "projects/ghostline/quests/gq001/implementation/quest.json"
        )
        original = next(stage for stage in spec.stages if stage.type == "meet_contact")
        _, archive = compiler.resource_paths(original.phase_resource)
        phase = compiler.build_stage_phase(original, archive, spec.phase_prefabs)
        for field in ("objective", "mappin"):
            stage = copy.deepcopy(original)
            stage.data[field] += "_typo"
            corrupt = copy.deepcopy(phase)
            corrupt["debug_expected_value"] = stage.data[field]
            with (
                self.subTest(field=field),
                self.assertRaisesRegex(compiler.QuestSpecError, field),
            ):
                compiler.validate_meeting_journal_bindings(stage, corrupt)
        root_owned = copy.deepcopy(original)
        root_owned.data["description_entry"] = (
            "quests/minor_quest/root_only_description"
        )
        compiler.validate_meeting_journal_bindings(root_owned, phase)

    def test_journal_templates_are_stable_sources_and_cloned_handles_remap(self):
        catalog = json.loads(
            (ROOT / "quests/templates/journal/catalog.json").read_text(encoding="utf-8")
        )["templates"]
        for name, entry in catalog.items():
            self.assertIn("mod/ghostline/journal_templates/", entry["path"])
            self.assertTrue(quest_content.journal_template_path(name).is_file())
        handles = quest_content.Handles({"HandleId": "1", "Data": {}}, minimum_next=100)
        donor = {
            "HandleId": "5",
            "Data": {
                "child": {
                    "HandleId": "6",
                    "Data": {
                        "parent": {"HandleRefId": "5"},
                        "external": {"HandleRefId": "9"},
                    },
                }
            },
        }
        clone = handles.clone(donor)
        self.assertEqual(clone["HandleId"], "100")
        self.assertEqual(clone["Data"]["child"]["Data"]["parent"]["HandleRefId"], "100")
        self.assertEqual(clone["Data"]["child"]["Data"]["external"]["HandleRefId"], "9")
        self.assertEqual(donor["HandleId"], "5")

    def test_all_journal_builders_preserve_reviewed_resource_payloads(self):
        for path in sorted((ROOT / "quests").glob("**/implementation/build.py")):
            qid = path.parents[1].name
            module_spec = importlib.util.spec_from_file_location(
                f"maintenance_{qid}", path
            )
            module = importlib.util.module_from_spec(module_spec)
            sys.modules[module_spec.name] = module
            module_spec.loader.exec_module(module)
            if not hasattr(module, "generate_journal"):
                continue
            for kind, raw, archive in (
                ("journal", module.JOURNAL_RAW, module.JOURNAL_ARCHIVE),
                ("onscreens", module.ONSCREEN_RAW, module.ONSCREEN_ARCHIVE),
            ):
                with self.subTest(quest=qid, resource=kind):
                    expected = json.loads(raw.read_text(encoding="utf-8"))
                    expected["Header"]["ArchiveFileName"] = str(archive.resolve())
                    actual = getattr(module, f"generate_{kind}")()
                    if qid == "gqt003":
                        # Shared scaffolding reallocates handles and omits empty
                        # donor folders; preserve every runtime path and value.
                        from tests.test_quest_authoring import (
                            journal_contract,
                            onscreen_contract,
                        )

                        contract = (
                            journal_contract if kind == "journal" else onscreen_contract
                        )
                        self.assertEqual(contract(actual), contract(expected))
                    else:
                        self.assertEqual(actual, expected)


class SceneAndWorldIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scene_spec = generate_scene.load_json(
            ROOT
            / "projects/ghostline/quests/gq000/implementation/scenes/patch-meet.scene-spec.json"
        )
        cls.scene = generate_scene.build_scene(cls.scene_spec)
        cls.world_spec = generate_world.load_json(
            ROOT
            / "projects/ghostline/quests/gq000/implementation/world/patch-meet.world.json"
        )

    def test_every_locale_payload_index_and_variant_is_checked(self):
        for corruption in ("index", "variant"):
            scene = copy.deepcopy(self.scene)
            store = scene["Data"]["RootChunk"]["locStore"]
            descriptor = next(
                item for item in store["vdEntries"] if item.get("localeId") == "en_us"
            )
            if corruption == "index":
                descriptor["vpeIndex"] = 999999
            else:
                descriptor["variantId"]["ruid"] = "999999"
            errors = generate_scene.validate_scene(scene, self.scene_spec)
            self.assertTrue(
                any("locStore descriptor" in error for error in errors), errors
            )

    def test_exit_must_target_an_existing_end_node(self):
        for node_id in (999999, 1):
            scene = copy.deepcopy(self.scene)
            scene["Data"]["RootChunk"]["exitPoints"][0]["nodeId"]["id"] = node_id
            errors = generate_scene.validate_scene(scene, self.scene_spec)
            self.assertTrue(any("Exit point" in error for error in errors), errors)

    def test_actor_set_out_of_bounds_remains_invalid(self):
        scene = copy.deepcopy(self.scene)
        scene["Data"]["RootChunk"]["actors"][0]["animSets"] = [
            {"$type": "scnAnimSetSRRefId", "id": 99999}
        ]
        errors = generate_scene.validate_scene(scene, self.scene_spec)
        self.assertTrue(any("99999" in error for error in errors), errors)

    def test_duplicate_world_identity_fails_before_writing(self):
        spec = copy.deepcopy(self.world_spec)
        spec["markers"].append(copy.deepcopy(spec["markers"][0]))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(SystemExit, "Duplicate world NodeRef"):
                generate_world.build_world(spec, root / "raw", root / "archive")
            self.assertFalse((root / "raw").exists())

    def test_world_aliases_are_explicit_and_full_paths_distinguish_leaf_names(self):
        spec = copy.deepcopy(self.world_spec)
        spec["markers"].extend(
            [
                {"ref": "#left/#shared", "position": {"from": "origin"}},
                {"ref": "#right/#shared", "position": {"from": "origin"}},
            ]
        )
        alias = spec["triggers"][0]["ref"]
        spec["always_loaded_node_refs"] = [alias]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generate_world.build_world_documents(spec, root / "raw", root / "archive")
            spec["always_loaded_node_refs"].append(alias)
            with self.assertRaisesRegex(SystemExit, "Duplicate AlwaysLoaded alias"):
                generate_world.build_world_documents(
                    spec, root / "raw", root / "archive"
                )

    def test_same_world_identity_cannot_be_owned_by_both_sectors(self):
        spec = copy.deepcopy(self.world_spec)
        marker = copy.deepcopy(spec["markers"][0])
        marker["sector"] = (
            "quest" if marker.get("sector") == "always_loaded" else "always_loaded"
        )
        spec["markers"].append(marker)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(SystemExit, "Duplicate world NodeRef"):
                generate_world.build_world_documents(
                    spec, root / "raw", root / "archive"
                )

    def test_world_generation_is_deterministic_with_optional_provenance_time(self):
        spec = copy.deepcopy(self.world_spec)
        spec.pop("exported_datetime", None)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = generate_world.build_world_documents(
                spec, root / "raw", root / "archive"
            )
            second = generate_world.build_world_documents(
                spec, root / "raw", root / "archive"
            )
            self.assertEqual(first, second)
            self.assertFalse((root / "raw").exists())
            self.assertEqual(
                {value["Header"]["ExportedDateTime"] for value in first[1].values()},
                {"1970-01-01T00:00:00Z"},
            )
            spec["exported_datetime"] = "2026-09-05T00:00:00Z"
            _, documents = generate_world.build_world_documents(
                spec, root / "raw", root / "archive"
            )
            self.assertEqual(
                {value["Header"]["ExportedDateTime"] for value in documents.values()},
                {spec["exported_datetime"]},
            )


if __name__ == "__main__":
    unittest.main()
