"""Contract checks for alias expansion and donor-based journal scaffolding."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import quest_authoring as authoring
import quest_compiler as compiler
import quest_authoring_schema as authoring_schema
from jsonschema import Draft202012Validator


def journal_contract(document: dict) -> dict:
    """Compare runtime entry paths/data independently of donor handle allocation."""
    groups = {
        "gameJournalRootFolderEntry",
        "gameJournalPrimaryFolderEntry",
        "gameJournalFolderEntry",
        "gameJournalPointOfInterestGroup",
        "gameJournalOnscreenGroup",
    }
    result = {}

    def clean(value):
        if isinstance(value, dict):
            return {
                key: clean(child)
                for key, child in value.items()
                if key not in {"HandleId", "HandleRefId", "entries"}
            }
        if isinstance(value, list):
            return [clean(child) for child in value]
        return value

    def visit(wrapper, parent=""):
        data = wrapper["Data"]
        path = "/".join(part for part in (parent, data.get("id", "")) if part)
        if data["$type"] not in groups:
            if path in result:
                raise AssertionError(f"Duplicate journal path: {path}")
            result[path] = clean(data)
        for child in data.get("entries", []):
            visit(child, path)

    visit(document["Data"]["RootChunk"]["entry"])
    return result


def onscreen_contract(document: dict) -> dict:
    result = copy.deepcopy(document)
    entries = result["Data"]["RootChunk"]["root"]["Data"]["entries"]
    entries.sort(key=lambda value: value["secondaryKey"])
    return result


def fixture() -> dict:
    return {
        "schema_version": 1,
        "id": "gq_authoring",
        "title": "Relay evidence",
        "description": "Follow the signal.",
        "composition": {
            "locations": {
                "relay": {
                    "ref": "#gq_authoring_marker",
                    "trigger": "#gq_authoring_trigger",
                }
            },
            "facts": {"accepted": None},
            "clues": {"relay": {"object_ref": "@locations.relay.ref"}},
            "objectives": {
                "reach": {
                    "text": "Reach the relay.",
                    "phase_id": "gq_authoring_01",
                    "id": "gq_authoring_01_objective",
                    "localization_key": "gl_preserved_objective_key",
                    "mappins": {
                        "relay": {"ref": "@locations.relay.ref", "text": "Relay"}
                    },
                }
            },
        },
        "stages": [
            {
                "id": "reach",
                "type": "reach_area",
                "status": "planned",
                "trigger": "@locations.relay.trigger",
                "objective": "@objectives.reach.path",
                "description_entry": "@objectives.reach.description_entry",
                "mappin": "@objectives.reach.mappin",
            }
        ],
    }


class QuestAuthoringTests(unittest.TestCase):
    def test_localization_aliases_resolve_before_collision_checks(self):
        raw = fixture()
        raw["composition"]["locations"]["labels"] = {
            "ref": "#labels",
            "key": "gl_resolved_objective",
            "caption": "Reach the relay.",
        }
        raw["composition"]["objectives"]["reach"].update(
            localization_key="@locations.labels.key", text="@locations.labels.caption"
        )
        result = authoring.compose(raw)
        onscreens = next(
            document
            for depot, document in result.documents.items()
            if depot.endswith(".json")
        )
        entries = onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
        self.assertIn(
            ("gl_resolved_objective", "Reach the relay."),
            {(entry["secondaryKey"], entry["femaleVariant"]) for entry in entries},
        )
        raw["composition"].setdefault("text", {})["gl_resolved_objective"] = (
            "Conflicting text"
        )
        with self.assertRaisesRegex(
            authoring.AuthoringError, "Conflicting localization text"
        ):
            authoring.normalize_spec(raw)

    def test_aliases_preserve_escaped_literal_text(self):
        raw = fixture()
        raw["composition"]["locations"]["label"] = {
            "ref": "#label",
            "text": "@@literal",
        }
        raw["composition"]["objectives"]["reach"]["text"] = "@locations.label.text"
        result = authoring.compose(raw)
        self.assertEqual(result.bindings["objectives"]["reach"]["text"], "@literal")
        onscreens = next(
            document
            for depot, document in result.documents.items()
            if depot.endswith(".json")
        )
        self.assertTrue(
            any(
                entry["femaleVariant"] == "@literal"
                for entry in onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
            )
        )

    def test_plain_inputs_stay_unchanged_and_normalization_has_no_donor_io(self):
        plain = {
            "schema_version": 1,
            "id": "existing",
            "title": "Existing",
            "stages": [{"id": "stage"}],
        }
        original = copy.deepcopy(plain)
        with patch.object(
            authoring, "load", side_effect=AssertionError("unexpected donor read")
        ):
            normalized = authoring.normalize_spec(plain)
            authoring.normalize_spec(fixture())
        self.assertEqual(normalized, original)
        normalized["stages"][0]["id"] = "changed"
        self.assertEqual(plain, original)

    def test_aliases_are_deterministic_and_preserve_explicit_identifiers(self):
        raw = fixture()
        original = copy.deepcopy(raw)
        result = authoring.compose(raw)
        self.assertEqual(raw, original)
        self.assertEqual(result, authoring.compose(raw))
        self.assertEqual(authoring.normalize_spec(result.manifest), result.manifest)
        stage = result.manifest["stages"][0]
        self.assertEqual(
            stage["phase_resource"],
            r"mod\gq_authoring\phases\gq_authoring_reach.questphase",
        )
        self.assertEqual(
            stage["objective"],
            "quests/minor_quest/gq_authoring/gq_authoring_01/gq_authoring_01_objective",
        )
        self.assertEqual(result.bindings["facts"]["accepted"], "gq_authoring_accepted")
        self.assertEqual(
            result.bindings["clues"]["relay"]["object_ref"], "#gq_authoring_marker"
        )
        self.assertEqual(
            result.bindings["clues"]["relay"]["completion_fact"],
            "gq_authoring_clue_relay_scanned",
        )
        self.assertEqual(
            result.bindings["objectives"]["reach"]["localization_key"],
            "gl_preserved_objective_key",
        )

    def test_bad_aliases_cycles_and_localization_collisions_are_rejected(self):
        raw = fixture()
        raw["stages"][0]["trigger"] = "@locations.missing.ref"
        with self.assertRaisesRegex(authoring.AuthoringError, "Unknown alias"):
            authoring.normalize_spec(raw)
        raw = fixture()
        raw["composition"]["facts"] = {"one": "@facts.two", "two": "@facts.one"}
        with self.assertRaisesRegex(authoring.AuthoringError, "Alias cycle"):
            authoring.normalize_spec(raw)
        raw = fixture()
        raw["composition"]["text"] = {"gl_preserved_objective_key": "Conflicting text"}
        with self.assertRaisesRegex(
            authoring.AuthoringError, "Conflicting localization"
        ):
            authoring.normalize_spec(raw)

    def test_bad_names_markers_and_duplicate_journal_paths_are_rejected(self):
        for change, error in (
            (lambda c: c.update(namespace="../escape"), "identifier"),
            (lambda c: c.update(unknown=True), "Unknown composition"),
            (
                lambda c: c["objectives"]["reach"]["mappins"]["relay"].update(ref=""),
                "NodeRef",
            ),
            (
                lambda c: c["objectives"].update(
                    duplicate=copy.deepcopy(c["objectives"]["reach"])
                ),
                "Duplicate objective path",
            ),
            (
                lambda c: c.update(
                    points_of_interest={
                        "first": {"id": "same", "ref": "#one"},
                        "second": {"id": "same", "ref": "#two"},
                    }
                ),
                "Duplicate point-of-interest",
            ),
        ):
            raw = fixture()
            change(raw["composition"])
            with (
                self.subTest(error=error),
                self.assertRaisesRegex(authoring.AuthoringError, error),
            ):
                authoring.normalize_spec(raw)

    def test_expansion_is_whole_value_only_and_overrides_remain_explicit(self):
        raw = fixture()
        raw["stages"][0].update(
            phase_resource=r"mod\legacy\phase.questphase",
            notes="Use @locations.relay.ref later.",
        )
        result = authoring.normalize_spec(raw)
        self.assertEqual(
            result["stages"][0]["phase_resource"], r"mod\legacy\phase.questphase"
        )
        self.assertEqual(
            result["stages"][0]["notes"], "Use @locations.relay.ref later."
        )

    def test_generated_phone_and_objective_paths_and_localization_are_closed(self):
        raw = json.loads(
            (ROOT / "quests/examples/recipes/investigation.quest.json").read_text(
                encoding="utf-8"
            )
        )
        result = authoring.compose(raw)
        journal = result.documents[result.bindings["resources"]["journal"]]
        onscreens = result.documents[result.bindings["resources"]["onscreens"]]
        compiler.validate_handle_graph(journal, context="authored journal")
        paths = journal_contract(journal)
        localized = {
            row["secondaryKey"]
            for row in onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
        }

        def strings(value):
            if isinstance(value, str):
                yield value
            elif isinstance(value, dict):
                for child in value.values():
                    yield from strings(child)
            elif isinstance(value, list):
                for child in value:
                    yield from strings(child)

        for stage in result.manifest["stages"]:
            for value in strings(stage):
                if value.startswith(("quests/", "contacts/")):
                    self.assertIn(value, paths)
        for value in strings(journal):
            if value.startswith("gl_"):
                self.assertIn(value, localized)
        self.assertTrue(
            all(
                row["primaryKey"] == "0"
                for row in onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
            )
        )

    def test_every_recipe_expands_to_valid_existing_stage_contracts(self):
        for path in sorted((ROOT / "quests/examples/recipes").glob("*.quest.json")):
            with (
                self.subTest(recipe=path.stem),
                tempfile.TemporaryDirectory() as directory,
            ):
                raw = json.loads(path.read_text(encoding="utf-8"))
                result = authoring.compose(raw)
                normalized = Path(directory) / "quest.json"
                normalized.write_text(json.dumps(result.manifest), encoding="utf-8")
                spec, diagnostics = compiler.load_spec(normalized)
                self.assertIsNotNone(spec, diagnostics)
                self.assertFalse(
                    [item for item in diagnostics if item.level == "error"]
                )
                recipe = raw["composition"]["recipes"][0]
                self.assertEqual(
                    [stage["type"] for stage in result.manifest["stages"]],
                    [kind for _, kind in authoring.RECIPES[recipe["name"]]],
                )
                if "reward" in recipe:
                    self.assertEqual(
                        result.manifest["stages"][-1]["reward"], recipe["reward"]
                    )

    def test_recipe_shape_and_expanded_stage_collisions_fail_early(self):
        with self.assertRaisesRegex(authoring.AuthoringError, "exactly"):
            authoring.expand_recipe("rescue_escort_defense_extraction", {})
        with self.assertRaisesRegex(authoring.AuthoringError, "explicit reward"):
            authoring.expand_recipe(
                "encounter_evidence_report_reward",
                {"encounter": {}, "evidence": {}, "report": {}},
            )
        raw = json.loads(
            (ROOT / "quests/examples/recipes/encounter.quest.json").read_text(
                encoding="utf-8"
            )
        )
        raw["stages"] = [{"id": "report", "type": "time_gate"}]
        with self.assertRaisesRegex(
            authoring.AuthoringError, "Duplicate expanded stage"
        ):
            authoring.normalize_spec(raw)

    def test_gqt003_pilot_preserves_runtime_journal_and_text_contracts(self):
        module_spec = importlib.util.spec_from_file_location(
            "authoring_gqt003", ROOT / "projects/test-quests/gqt003/implementation/build.py"
        )
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        previous = json.loads(module.JOURNAL_RAW.read_text(encoding="utf-8"))
        generated = module.generate_journal()
        self.assertEqual(journal_contract(generated), journal_contract(previous))
        compiler.validate_handle_graph(generated, context="GQT003 scaffold")
        previous_text = json.loads(module.ONSCREEN_RAW.read_text(encoding="utf-8"))
        self.assertEqual(
            onscreen_contract(module.generate_onscreens()),
            onscreen_contract(previous_text),
        )

    def test_cli_publication_uses_isolated_raw_paths_and_invalid_input_preserves_outputs(
        self,
    ):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest, output = root / "source.json", root / "output"
            manifest.write_text(json.dumps(fixture()), encoding="utf-8")
            self.assertEqual(
                authoring.main([str(manifest), "--output", str(output)]), 0
            )
            previous = {
                path: path.read_bytes() for path in output.rglob("*") if path.is_file()
            }
            self.assertTrue(any("source/raw" in path.as_posix() for path in previous))
            bad = fixture()
            bad["stages"][0]["objective"] = "@unknown.objective"
            manifest.write_text(json.dumps(bad), encoding="utf-8")
            with self.assertRaises(authoring.AuthoringError):
                authoring.main([str(manifest), "--output", str(output)])
            self.assertEqual(
                previous,
                {
                    path: path.read_bytes()
                    for path in output.rglob("*")
                    if path.is_file()
                },
            )


class QuestEditorSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(
            authoring_schema.SCHEMA_PATH.read_text(encoding="utf-8")
        )
        cls.validator = Draft202012Validator(cls.schema)

    def test_generated_schema_is_current_and_preserves_canonical_registry(self):
        Draft202012Validator.check_schema(self.schema)
        refreshed = authoring_schema.refresh_schema(self.schema)
        self.assertEqual(refreshed, self.schema)
        self.assertEqual(refreshed["$defs"]["stage"], self.schema["$defs"]["stage"])
        self.assertEqual(
            refreshed["$defs"]["baseStage"], self.schema["$defs"]["baseStage"]
        )

    def test_new_canonical_fields_require_refresh_and_keep_literal_constraints(self):
        changed = copy.deepcopy(self.schema)
        changed["$defs"]["baseStage"]["properties"]["review_priority"] = {
            "type": "integer",
            "minimum": 0,
        }
        refreshed = authoring_schema.refresh_schema(changed)
        self.assertNotEqual(changed, refreshed)
        self.assertEqual(changed["$defs"]["stage"], refreshed["$defs"]["stage"])
        validator = Draft202012Validator(refreshed)
        raw = fixture()
        raw["composition"]["locations"]["relay"]["priority"] = 2
        raw["stages"][0]["review_priority"] = "@locations.relay.priority"
        self.assertEqual(list(validator.iter_errors(raw)), [])
        self.assertEqual(list(validator.iter_errors(authoring.normalize_spec(raw))), [])
        raw["stages"][0]["review_priority"] = -1
        self.assertTrue(list(validator.iter_errors(raw)))

    def test_raw_recipes_and_normalized_manifests_both_validate(self):
        paths = list((ROOT / "quests/examples/recipes").glob("*.quest.json"))
        paths.append(ROOT / "projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json")
        self.assertEqual(len(paths), 4)
        for path in paths:
            with self.subTest(path=path):
                raw = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(list(self.validator.iter_errors(raw)), [])
                normalized = authoring.normalize_spec(raw)
                self.assertNotIn("composition", normalized)
                self.assertEqual(list(self.validator.iter_errors(normalized)), [])

    def test_aliases_cover_nested_values_arrays_objects_and_top_level_fields(self):
        raw = fixture()
        raw["external_facts"] = ["@facts.accepted"]
        raw["completion"] = {
            "quest_path": "@quest.path",
            "outcomes": {"success": {"state": "Succeeded", "fact": "@facts.accepted"}},
        }
        raw["stages"] = [
            {
                "id": "inspect",
                "type": "investigate_clues",
                "objective": "@objectives.reach.path",
                "description_entry": "@objectives.reach.description_entry",
                "clues": ["@clues.relay"],
                "contract": {"reads_facts": ["@facts.accepted"]},
            }
        ]
        self.assertEqual(list(self.validator.iter_errors(raw)), [])
        self.assertEqual(
            list(self.validator.iter_errors(authoring.normalize_spec(raw))), []
        )
        raw["composition"]["locations"]["relay"]["seconds"] = 4
        raw["stages"] = [
            {"id": "wait", "type": "time_gate", "seconds": "@locations.relay.seconds"}
        ]
        self.assertEqual(list(self.validator.iter_errors(raw)), [])
        self.assertEqual(
            list(self.validator.iter_errors(authoring.normalize_spec(raw))), []
        )
        raw["composition"]["locations"]["relay"]["seconds"] = "invalid duration"
        self.assertEqual(list(self.validator.iter_errors(raw)), [])
        self.assertTrue(list(self.validator.iter_errors(authoring.normalize_spec(raw))))

    def test_literals_missing_fields_and_canonical_paths_remain_strict(self):
        for mutate in (
            lambda raw: raw["stages"][0].update(trigger=42),
            lambda raw: raw["stages"][0].update(objective="missing_path_segments"),
            lambda raw: raw["stages"][0].update(unknown_property="unexpected"),
            lambda raw: raw["stages"][0].pop("trigger"),
            lambda raw: raw["stages"][0].update(id="@quest.id"),
        ):
            raw = fixture()
            mutate(raw)
            self.assertTrue(list(self.validator.iter_errors(raw)), raw)
        canonical = authoring.normalize_spec(fixture())
        canonical["stages"][0].pop("phase_resource")
        self.assertTrue(list(self.validator.iter_errors(canonical)))
        canonical = authoring.normalize_spec(fixture())
        canonical["stages"][0]["objective"] = "@objectives.reach.path"
        self.assertTrue(list(self.validator.iter_errors(canonical)))
        for raw in (
            {"schema_version": 1, "id": "empty", "title": "Empty"},
            {"schema_version": 1, "id": "empty", "title": "Empty", "composition": {}},
            {
                "schema_version": 1,
                "id": "empty",
                "title": "Empty",
                "composition": {"recipes": []},
                "stages": [],
            },
        ):
            self.assertTrue(list(self.validator.iter_errors(raw)))

    def test_recipe_slots_use_their_default_stage_contract_and_explicit_type_override(
        self,
    ):
        original = json.loads(
            (ROOT / "quests/examples/recipes/rescue.quest.json").read_text(
                encoding="utf-8"
            )
        )
        for change in (
            lambda recipe: recipe["steps"].pop("escort"),
            lambda recipe: recipe["steps"].update(unexpected={}),
            lambda recipe: recipe["steps"]["defense"].update(duration_seconds=-1),
            lambda recipe: recipe["steps"]["rescue"].pop("device"),
            lambda recipe: recipe.update(reward="QuestRewards.unexpected"),
        ):
            raw = copy.deepcopy(original)
            change(raw["composition"]["recipes"][0])
            self.assertTrue(list(self.validator.iter_errors(raw)))
        raw = copy.deepcopy(original)
        raw["composition"]["recipes"][0]["steps"]["rescue"] = {
            "type": "time_gate",
            "seconds": 1,
        }
        self.assertEqual(list(self.validator.iter_errors(raw)), [])
        self.assertEqual(
            list(self.validator.iter_errors(authoring.normalize_spec(raw))), []
        )


if __name__ == "__main__":
    unittest.main()
