"""Explicit combat metadata preserves reviewed resources without global defaults."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from phase_graph import PhaseGraphBuilder, combat_threat_node
from quest_compiler import build_combat_encounter_phase
from quest_stage_validation import validate_combat_encounter
from quest_types import CompiledStage


def dictionaries(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from dictionaries(child)
    elif isinstance(value, list):
        for child in value:
            yield from dictionaries(child)


def stage_data(**settings):
    return {
        "id": "security",
        "type": "combat_encounter",
        "status": "planned",
        "phase_resource": r"mod\test_threat\phases\security.questphase",
        "community": "#test_security",
        "entries": ["ranged", "melee"],
        "hostility": "already_hostile",
        "completion": "all_defeated",
        "completion_fact": "test_security_defeated",
        "cleanup_on_exit": True,
        **settings,
    }


def build(**settings):
    data = stage_data(**settings)
    stage = CompiledStage(
        0, "security", "combat_encounter", "planned", data["phase_resource"], data
    )
    return build_combat_encounter_phase(
        stage, ROOT / "generated/tests/threat/security.questphase"
    )


class CombatThreatSettingsTests(unittest.TestCase):
    def test_omitted_settings_preserve_default_commands_and_shared_primitive(self):
        attacks = [
            node
            for node in dictionaries(build())
            if node.get("$type") == "questCombatNodeDefinition"
        ]
        self.assertEqual(len(attacks), 2)
        for attack in attacks:
            self.assertNotIn("function", attack)
            self.assertEqual(attack["params"]["Data"]["duration"], 0.5)
        builder = PhaseGraphBuilder()
        shared = combat_threat_node(builder, 10, "#other_community", "guard")
        self.assertNotIn("function", shared.data)
        self.assertEqual(shared.data["params"]["Data"]["duration"], 0.5)

    def test_overrides_change_only_requested_metadata_on_every_attacker(self):
        baseline = build()
        for settings in (
            {"threat_duration_seconds": 0},
            {"threat_duration_seconds": 2.25},
            {"threat_function": "questCombatNodeParams_ShootAt"},
            {
                "threat_function": "questCombatNodeParams_ShootAt",
                "threat_duration_seconds": 0,
            },
        ):
            with self.subTest(settings=settings):
                document = build(**settings)
                attacks = [
                    node
                    for node in dictionaries(document)
                    if node.get("$type") == "questCombatNodeDefinition"
                ]
                self.assertEqual(len(attacks), 2)
                for attack in attacks:
                    if "threat_function" in settings:
                        self.assertEqual(
                            attack.pop("function"),
                            {
                                "$type": "CName",
                                "$storage": "string",
                                "$value": settings["threat_function"],
                            },
                        )
                    if "threat_duration_seconds" in settings:
                        self.assertEqual(
                            attack["params"]["Data"]["duration"],
                            settings["threat_duration_seconds"],
                        )
                        attack["params"]["Data"]["duration"] = 0.5
                self.assertEqual(document, baseline)

    def test_invalid_settings_are_rejected_semantically(self):
        cases = [
            ({"threat_duration_seconds": value}, "invalid_combat_threat_duration")
            for value in (-1, True, "0", None, float("inf"), float("nan"))
        ]
        cases += [
            ({"threat_function": value}, "invalid_combat_threat_function")
            for value in ("", "unsupported_function", None, False)
        ]
        cases += [
            (
                {"threat_duration_seconds": 0, "entries": []},
                "unsupported_combat_threat_settings",
            ),
            (
                {
                    "threat_function": "questCombatNodeParams_ShootAt",
                    "phase_template": r"mod\test\phase.questphase",
                },
                "unsupported_combat_threat_settings",
            ),
        ]
        for settings, expected in cases:
            with self.subTest(settings=settings):
                diagnostics = []
                validate_combat_encounter(
                    stage_data(**settings), "stages[0]", "security", diagnostics
                )
                self.assertIn(expected, {diagnostic.code for diagnostic in diagnostics})

    def test_schema_accepts_overrides_and_rejects_ignored_template_settings(self):
        schema = json.loads(
            (ROOT / "tools/quest-schema-v1.json").read_text(encoding="utf-8")
        )
        manifest = {
            "schema_version": 1,
            "id": "test_threat",
            "title": "Threat settings",
            "stages": [
                stage_data(
                    threat_function="questCombatNodeParams_ShootAt",
                    threat_duration_seconds=0,
                )
            ],
        }
        validator = Draft202012Validator(schema)
        validator.validate(manifest)
        invalid = copy.deepcopy(manifest)
        invalid["stages"][0]["phase_template"] = r"mod\test\phase.questphase"
        self.assertTrue(list(validator.iter_errors(invalid)))
        invalid = copy.deepcopy(manifest)
        del invalid["stages"][0]["entries"]
        self.assertTrue(list(validator.iter_errors(invalid)))


if __name__ == "__main__":
    unittest.main()
