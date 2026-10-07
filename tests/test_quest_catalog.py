from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import quest_catalog as catalog
from quest_stages import STAGE_REGISTRY


class QuestCatalogTests(unittest.TestCase):
    def test_catalog_expands_recipes_and_indexes_story_manifests(self):
        examples, errors = catalog.manifest_examples(ROOT)
        self.assertEqual(errors, [])
        paths = {
            example["manifest"] for values in examples.values() for example in values
        }
        self.assertIn("quests/examples/recipes/rescue.quest.json", paths)
        self.assertIn("projects/ghostline/quests/gq002/implementation/quest.json", paths)
        rescue = [
            example
            for example in examples["escort_npc"]
            if example["manifest"].endswith("recipes/rescue.quest.json")
        ]
        self.assertTrue(rescue)
        self.assertFalse(rescue[0]["data"]["objective"].startswith("@"))

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.resource = self.root / "source/raw/mod/test/fixture.questphase.json"
        self.resource.parent.mkdir(parents=True)
        self.resource.write_text('{"fixture": 1}', encoding="utf-8")
        self.entry = {
            "id": "fixture-build",
            "level": "build",
            "passed": True,
            "stage_types": ["reach_area"],
            "summary": "Structural fixture only",
            "resources": {
                self.resource.relative_to(self.root).as_posix(): catalog.sha256(
                    self.resource
                )
            },
            "outputs": {"reach": "a" * 64},
        }

    def test_resource_change_or_removal_invalidates_evidence(self):
        self.assertEqual(
            catalog.assess_evidence(self.entry, root=self.root)["binding_status"],
            "current",
        )
        self.resource.write_text('{"fixture": 2}', encoding="utf-8")
        changed = catalog.assess_evidence(self.entry, root=self.root)
        self.assertEqual(changed["binding_status"], "stale")
        self.assertIn("Changed", changed["binding_errors"][0])
        self.resource.unlink()
        self.assertIn(
            "Missing",
            catalog.assess_evidence(self.entry, root=self.root)["binding_errors"][0],
        )

    def test_runtime_claim_requires_packed_resource_observations_and_bound_report(self):
        self.entry.update(
            level="in_game",
            observations=["Player completed the encounter"],
            run_report="projects/test-quests/run.md",
        )
        self.assertEqual(
            catalog.assess_evidence(self.entry, root=self.root)["binding_status"],
            "invalid",
        )
        packed = self.root / "source/archive/mod/test/fixture.questphase"
        packed.parent.mkdir(parents=True)
        packed.write_bytes(b"CR2W fixture")
        report = self.root / self.entry["run_report"]
        report.parent.mkdir(parents=True)
        report.write_text(
            "Explicit fixture report, not an actual game run", encoding="utf-8"
        )
        for path in (packed, report):
            self.entry["resources"][path.relative_to(self.root).as_posix()] = (
                catalog.sha256(path)
            )
        self.assertEqual(
            catalog.assess_evidence(self.entry, root=self.root)["binding_status"],
            "current",
        )
        report.write_text("Changed report", encoding="utf-8")
        self.assertEqual(
            catalog.assess_evidence(self.entry, root=self.root)["binding_status"],
            "stale",
        )

    def test_malformed_or_escaping_evidence_never_counts_as_current(self):
        cases = [
            None,
            {},
            {**self.entry, "stage_types": None},
            {**self.entry, "level": "verified"},
            {**self.entry, "outputs": {}},
            {**self.entry, "resources": {"../outside": "a" * 64}},
            {**self.entry, "resources": {"C:/outside": "a" * 64}},
            {**self.entry, "resources": {"source\\outside": "a" * 64}},
        ]
        for entry in cases:
            with self.subTest(entry=entry):
                self.assertEqual(
                    catalog.assess_evidence(entry, root=self.root)["binding_status"],
                    "invalid",
                )

    def test_registry_fields_limits_and_examples_are_derived(self):
        result = catalog.build_catalog(root=ROOT, evidence_paths=[])
        blocks = {block["type"]: block for block in result["blocks"]}
        self.assertEqual(set(blocks), set(STAGE_REGISTRY))
        for name, block in blocks.items():
            self.assertTrue(STAGE_REGISTRY[name].fields <= set(block["fields"]))
            self.assertIn("phase_resource", block["fields"])
            self.assertEqual(
                block["limits"]["unsupported_default_template_fields"],
                sorted(STAGE_REGISTRY[name].implementation.unsupported_fields),
            )
            self.assertFalse(block["in_game_pass_recorded"])
            self.assertFalse(block["structural_build_recorded"])
        self.assertTrue(blocks["reach_area"]["examples"])
        self.assertIn(
            "reads_facts",
            blocks["reach_area"]["fields"]["contract"]["schema"]["properties"],
        )
        self.assertIn("## `reach_area`", catalog.catalog_markdown(result))

    def test_stale_evidence_does_not_grant_build_status(self):
        evidence = self.root / "evidence.json"
        evidence.write_text(
            json.dumps({"schema_version": 1, "entries": [self.entry]}), encoding="utf-8"
        )
        result = catalog.build_catalog(root=self.root, evidence_paths=[evidence])
        block = next(
            block for block in result["blocks"] if block["type"] == "reach_area"
        )
        self.assertTrue(block["structural_build_recorded"])
        self.resource.write_text("changed", encoding="utf-8")
        result = catalog.build_catalog(root=self.root, evidence_paths=[evidence])
        block = next(
            block for block in result["blocks"] if block["type"] == "reach_area"
        )
        self.assertFalse(block["structural_build_recorded"])
        self.assertEqual(len(result["evidence_errors"]), 1)

    def test_duplicate_evidence_ids_are_rejected(self):
        evidence = self.root / "evidence.json"
        evidence.write_text(
            json.dumps(
                {"schema_version": 1, "entries": [self.entry, deepcopy(self.entry)]}
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "Duplicate evidence ID"):
            catalog.read_evidence([evidence], root=self.root)

    def test_recorded_build_runs_real_compiler_and_binds_inputs(self):
        evidence = catalog.record_build(
            ROOT / "quests/examples/direct_building_blocks.quest.json"
        )
        entry = evidence["entries"][0]
        self.assertEqual(entry["level"], "build")
        self.assertEqual(len(entry["outputs"]), 5)
        self.assertIn("tools/quest_compiler.py", entry["resources"])
        self.assertIn(
            "tools/generate_advanced_quest_block_templates.py", entry["resources"]
        )
        self.assertIn("tools/quest_encounter.py", entry["resources"])
        self.assertIn(
            "quests/examples/direct_building_blocks.quest.json", entry["resources"]
        )
        self.assertEqual(catalog.assess_evidence(entry)["binding_status"], "current")
        self.assertIn("No native serialization", entry["summary"])

    def test_composition_outputs_keep_unique_hashes_and_bind_donors(self):
        generated = ROOT / "generated"
        generated.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=generated) as directory:
            manifest = Path(directory) / "fixture.quest.json"
            manifest.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "id": "gq_evidence_fixture",
                        "title": "Evidence composition fixture",
                        "composition": {"objectives": {"wait": {"text": "Wait."}}},
                        "stages": [
                            {
                                "id": "wait",
                                "type": "time_gate",
                                "status": "ready",
                                "phase_resource": "mod\\gq_evidence_fixture\\phases\\wait.questphase",
                                "seconds": 1,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            entry = catalog.record_build(manifest)["entries"][0]
        self.assertEqual(len(entry["outputs"]), 4)
        self.assertIn("$root", entry["outputs"])
        self.assertTrue(
            any(name.endswith(".journal.json") for name in entry["outputs"])
        )
        self.assertTrue(any(name.endswith(".json.json") for name in entry["outputs"]))
        self.assertIn("quests/templates/journal/catalog.json", entry["resources"])
        for donor in ("gq001_shapes.journal.json", "onscreen_container.json.json"):
            self.assertIn(
                f"quests/templates/source/raw/mod/ghostline/journal_templates/{donor}",
                entry["resources"],
            )


if __name__ == "__main__":
    unittest.main()
