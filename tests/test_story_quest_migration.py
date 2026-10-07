"""Migration contracts captured before replacing story-specific content builders.

Digests cover every original stage input, journal property, localized entry, and
compiled phase payload. Reviewed source corrections are asserted separately
before restoring only those fields for comparison with the old generated
digests. Journal handle numbering is not a runtime identity.
"""

from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import quest_compiler
from quest_authoring import compose, normalize_spec
from quest_types import QuestSpecError

EXPECTED = {
    "gq001": {
        "manifest": "7fd73f3ed6fde7981d05c9837a199a6bcb10cd069b10508754ec0a109227f12c",
        "journal": "3c8a78c63106a391a3a73933e8c2ed09bf20e2622a5622024c144335e7a65b33",
        "onscreens": "3be0489e5e8b35cf7c338d8552abbfbd1d9c164781808534d905da0236b6995e",
        "phases": "2984e0b91c20143d0ec280235f83acdbd639c419803040970c9b00d98b39f813",
        "phase_count": 6,
        "stage_count": 5,
        "text_count": 36,
    },
    "gq002": {
        # Reviewed series-order correction: wait for GQ001, then 12 game hours.
        "manifest": "7d02ffb2b8db2f5e66a48e9ed777d608cb5e746cedc817f8342f505c06d1cfe3",
        "journal": "fc8f092c799bb9b757a945a1871ea1759fe8358a79a15acfb422204645cc5211",
        "onscreens": "4bf6da550e35d2d51c0c6ee17e56925c685618d5db300b2bea6feb946664a9c5",
        "phases": "6bfb20019ca7f75aa2bcbd915a3e253c9399219d45b0565e04ae420400509f02",
        "phase_count": 13,
        "stage_count": 12,
        "text_count": 50,
    },
    "gq003": {
        "manifest": "f76fc4895a25693e34f4da705ec0b93daeaf0a55cc395a12f6a9ccdbddec087a",
        "journal": "a7d1df7ce9222123894c5982dc6ed16964b518facc96db1494dc5c17b5461c0b",
        "onscreens": "25b25f72ed9e5319e0a3eb9efa003d87673b058307f4c8f68049d53cbdcec41b",
        "phases": "a766d217d2100213abbabeb53586a87046967581087c21fb75d41178af68770f",
        "phase_count": 37,
        "stage_count": 36,
        "text_count": 151,
    },
}

# The old compiler inherited every root prefab into every child. These scopes
# instead retain the reviewed source/raw resources captured before publication.
REVIEWED_PREFAB_SCOPES = {
    "gq001": {
        "patch_job_offer": [],
        "meet_patch": ["#gq000_pr_patch_meet"],
        "hack_relay": ["#gq000_pr_patch_meet"],
        "meet_iris": ["#gq001_pr_iris_meet"],
        "deliver_cache": [],
    },
    "gq002": {
        "patch_job_offer": [],
        "meet_cinder": ["#gq002_pr_machine_stops"],
        "reach_relay": [],
        "investigate_relay": [],
        "read_hostage_circuit": [],
        "return_to_relay": [],
        "relay_security": [],
        "relay_decision": [],
        "relay_choice": [],
        "operate_relay": [],
        "leave_relay": [],
        "cinder_debrief": [],
    },
}

REVIEWED_THREAT_FUNCTION = {
    "$type": "CName",
    "$storage": "string",
    "$value": "questCombatNodeParams_ShootAt",
}


def digest(value):
    return hashlib.sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
        ).encode("utf-8")
    ).hexdigest()


def journal_values(value):
    if isinstance(value, dict):
        if "HandleId" in value:
            return journal_values(value["Data"])
        return {key: journal_values(child) for key, child in value.items()}
    if isinstance(value, list):
        return [journal_values(child) for child in value]
    return value


def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)


class StoryQuestMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.authored = {}
        cls.artifacts = {}
        for quest in EXPECTED:
            manifest = (
                ROOT / f"projects/ghostline/quests/{quest}/implementation/quest.json"
            )
            raw = json.loads(manifest.read_text(encoding="utf-8"))
            cls.authored[quest] = (raw, compose(raw))
            cls.artifacts[quest] = quest_compiler.compile_manifest_artifacts(
                manifest,
                ROOT / f"generated/tests/story-migration/{quest}/root.questphase.json",
                ROOT / f"source/archive/mod/{quest}/phases/{quest}.questphase",
                child_root=ROOT / f"generated/tests/story-migration/{quest}/children",
                allow_planned=quest == "gq003",
            )

    def test_authored_manifests_validate_against_the_editor_schema(self):
        schema = json.loads(
            (ROOT / "tools/quest-schema-v1.json").read_text(encoding="utf-8")
        )
        validator = Draft202012Validator(schema)
        for quest, (raw, _) in self.authored.items():
            with self.subTest(quest=quest):
                validator.validate(raw)

    def test_normalized_stage_inputs_preserve_all_original_flow_and_bindings(self):
        for quest, (raw, _) in self.authored.items():
            with self.subTest(quest=quest):
                normalized = normalize_spec(raw)
                for stage in normalized["stages"]:
                    if quest in REVIEWED_PREFAB_SCOPES:
                        self.assertEqual(
                            stage.pop("phase_prefabs"),
                            REVIEWED_PREFAB_SCOPES[quest][stage["id"]],
                        )
                    if quest == "gq002" and stage["id"] == "relay_security":
                        self.assertEqual(
                            stage.pop("threat_function"),
                            REVIEWED_THREAT_FUNCTION["$value"],
                        )
                        self.assertEqual(stage.pop("threat_duration_seconds"), 0)
                self.assertEqual(digest(normalized), EXPECTED[quest]["manifest"])
                self.assertEqual(
                    len(normalized["stages"]), EXPECTED[quest]["stage_count"]
                )
                self.assertTrue(
                    all(
                        raw["composition"][key]
                        for key in (
                            "objectives",
                            "contacts",
                            "readables",
                            "locations",
                            "facts",
                        )
                    )
                )

    def test_every_journal_property_matches_original_semantics(self):
        for quest, (_, authored) in self.authored.items():
            with self.subTest(quest=quest):
                journal = authored.documents[rf"mod\{quest}\journal\{quest}.journal"]
                self.assertEqual(
                    digest(journal_values(journal["Data"])), EXPECTED[quest]["journal"]
                )

    def test_every_localized_key_text_and_variant_is_preserved(self):
        for quest, (_, authored) in self.authored.items():
            with self.subTest(quest=quest):
                onscreens = authored.documents[
                    rf"mod\{quest}\localization\en-us\onscreens\{quest}.json"
                ]
                entries = onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
                self.assertEqual(len(entries), EXPECTED[quest]["text_count"])
                self.assertEqual(
                    digest({entry["secondaryKey"]: entry for entry in entries}),
                    EXPECTED[quest]["onscreens"],
                )

    def test_complete_builds_preserve_phases_except_reviewed_source_corrections(self):
        for quest, artifacts in self.artifacts.items():
            with self.subTest(quest=quest):
                count = EXPECTED[quest]["phase_count"]
                self.assertEqual(len(artifacts), count + 2)
                self.assertEqual(
                    len({artifact.raw_path for artifact in artifacts}), count + 2
                )
                documents = [
                    copy.deepcopy(artifact.document["Data"])
                    for artifact in artifacts[:count]
                ]
                root_prefabs = documents[0]["RootChunk"]["phasePrefabs"]
                for artifact, document in zip(artifacts[1:count], documents[1:]):
                    if quest in REVIEWED_PREFAB_SCOPES:
                        self.assertEqual(
                            [
                                entry["prefabNodeRef"]["$value"]
                                for entry in document["RootChunk"]["phasePrefabs"]
                            ],
                            REVIEWED_PREFAB_SCOPES[quest][artifact.stage_id],
                        )
                        # Restore only this approved difference before checking
                        # every other byte of the former generated payload.
                        document["RootChunk"]["phasePrefabs"] = copy.deepcopy(
                            root_prefabs
                        )
                    if quest == "gq002" and artifact.stage_id == "relay_security":
                        attacks = [
                            item
                            for item in objects(document)
                            if item.get("$type") == "questCombatNodeDefinition"
                        ]
                        self.assertEqual(len(attacks), 3)
                        for attack in attacks:
                            self.assertEqual(
                                attack.pop("function"), REVIEWED_THREAT_FUNCTION
                            )
                            self.assertEqual(attack["params"]["Data"]["duration"], 0)
                            attack["params"]["Data"]["duration"] = 0.5
                self.assertEqual(digest(documents), EXPECTED[quest]["phases"])
                self.assertTrue(
                    any(
                        artifact.archive_path.suffix == ".journal"
                        for artifact in artifacts
                    )
                )

    def test_gq003_remains_planned_and_requires_explicit_scratch_build(self):
        raw, authored = self.authored["gq003"]
        self.assertEqual(
            {stage["status"] for stage in authored.manifest["stages"]}, {"planned"}
        )
        self.assertEqual(authored.manifest["parallel_groups"], raw["parallel_groups"])
        with self.assertRaisesRegex(QuestSpecError, "planned stages"):
            quest_compiler.compile_manifest_artifacts(
                ROOT / "projects/ghostline/quests/gq003/implementation/quest.json",
                ROOT / "generated/tests/story-migration/refused.json",
                ROOT / "generated/tests/story-migration/refused.questphase",
            )
        build = self.build_module("gq003")
        with self.assertRaises(SystemExit), redirect_stderr(io.StringIO()):
            build.main(["--allow-planned"])

    def test_gq003_conflicting_duplicate_pin_keeps_first_marker_backed_entry(self):
        # The old generator emitted this path twice, first with the marker and
        # then the trigger. Preserve the first entry and eliminate ambiguity.
        journal = self.authored["gq003"][1].documents[
            r"mod\gq003\journal\gq003.journal"
        ]
        pins = [
            item
            for item in objects(journal)
            if item.get("$type") == "gameJournalQuestMapPin"
            and item.get("id") == "gq003_18_qmp_escort_gate_01"
        ]
        self.assertEqual(len(pins), 1)
        self.assertEqual(
            pins[0]["reference"]["reference"]["$value"], "#gq003_18_mp_escort_gate_01"
        )

    @staticmethod
    def build_module(quest):
        module_spec = importlib.util.spec_from_file_location(
            f"story_migration_{quest}",
            ROOT / f"projects/ghostline/quests/{quest}/implementation/build.py",
        )
        assert module_spec and module_spec.loader
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        return module

    def test_content_compatibility_wrappers_use_the_shared_authoring_source(self):
        for quest, (_, authored) in self.authored.items():
            with self.subTest(quest=quest):
                build = self.build_module(quest)
                self.assertEqual(
                    build.generate_journal(), authored.documents[build.JOURNAL_RESOURCE]
                )
                self.assertEqual(
                    build.generate_onscreens(),
                    authored.documents[build.ONSCREEN_RESOURCE],
                )

    def test_story_build_entry_points_publish_complete_scratch_sets(self):
        for quest in EXPECTED:
            with self.subTest(quest=quest), tempfile.TemporaryDirectory() as directory:
                build = self.build_module(quest)
                argv = ["--out-root", directory]
                if quest == "gq003":
                    argv.append("--allow-planned")
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(build.main(argv), 0)
                # Read actual publication products rather than trusting the plan.
                docs = []
                for path in Path(directory).rglob("*.json"):
                    value = json.loads(path.read_text(encoding="utf-8"))
                    if "Header" in value and "Data" in value:
                        docs.append(value)
                self.assertEqual(len(docs), EXPECTED[quest]["phase_count"] + 2)


if __name__ == "__main__":
    unittest.main()
