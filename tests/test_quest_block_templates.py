from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


sys.path.insert(0, str(ROOT / "tools"))
quest_compiler = load_module(
    "quest_compiler_template_tests", ROOT / "tools/quest_compiler.py"
)
templates = load_module(
    "quest_block_template_tests",
    ROOT / "tools/generate_quest_block_templates.py",
)


TEMPLATE_DEPOT = r"mod\ghostline\quest_blocks\templates"
PHASE_DEPOT = r"mod\gq_template_tests\phases"
OBJECTIVE = "quests/minor_quest/gq_template_tests/phase/objective"
DESCRIPTION = f"{OBJECTIVE}/description"


def common(stage_type: str) -> dict:
    return {
        "id": f"test_{stage_type}",
        "type": stage_type,
        "status": "ready",
        "phase_resource": f"{PHASE_DEPOT}\\{stage_type}.questphase",
        "phase_template": f"{TEMPLATE_DEPOT}\\{stage_type}.questphase",
    }


def template_stages() -> dict[str, dict]:
    interact = common("interact_device")
    interact.update(
        {
            "device": "#test_device",
            "controller_class": "AccessPointControllerPS",
            "action": "ForceEnabled",
            "completion_function": "WasHackingMinigameSucceeded",
            "template_bindings": {
                templates.DEVICE: "#test_device",
                templates.CONTROLLER: "AccessPointControllerPS",
                templates.ACTION: "ForceEnabled",
                templates.COMPLETION_FUNCTION: "WasHackingMinigameSucceeded",
            },
        }
    )

    combat = common("combat_encounter")
    combat.update(
        {
            "community": "#test_guards",
            "hostility": "already_hostile",
            "completion": "all_defeated",
            "template_bindings": {
                templates.COMMUNITY: "#test_guards",
            },
        }
    )

    investigate = common("investigate_clues")
    investigate.update(
        {
            "objective": OBJECTIVE,
            "description_entry": DESCRIPTION,
            "clues": [
                {
                    "id": "relay",
                    "object_ref": "#test_clue",
                }
            ],
            "required_count": 1,
            "template_bindings": {
                templates.OBJECTIVE: OBJECTIVE,
                templates.DESCRIPTION: DESCRIPTION,
                templates.CLUE_OBJECT: "#test_clue",
            },
        }
    )

    optional = common("optional_condition")
    optional.update(
        {
            "objective": OBJECTIVE,
            "condition": {"kind": "fact", "value": "test_stealth"},
            "success_fact": "test_optional_success",
            "failure_fact": "test_optional_failure",
            "evaluation": "at_exit",
            "template_bindings": {
                templates.OBJECTIVE: OBJECTIVE,
                templates.CONDITION_FACT: "test_stealth",
                templates.SUCCESS_FACT: "test_optional_success",
                templates.FAILURE_FACT: "test_optional_failure",
            },
        }
    )

    choice = common("choice_gate")
    choice.update(
        {
            "gate_kind": "fact",
            "branches": [
                {
                    "id": "left",
                    "condition": "test_choose_left",
                    "set_fact": "test_chose_left",
                },
                {
                    "id": "right",
                    "condition": "test_choose_right",
                    "set_fact": "test_chose_right",
                },
            ],
            "join": True,
            "template_bindings": {
                templates.BRANCH_A_CONDITION: "test_choose_left",
                templates.BRANCH_A_FACT: "test_chose_left",
                templates.BRANCH_B_CONDITION: "test_choose_right",
                templates.BRANCH_B_FACT: "test_chose_right",
            },
        }
    )
    return {
        stage["type"]: stage
        for stage in (interact, combat, investigate, optional, choice)
    }


class QuestBlockTemplateTests(unittest.TestCase):
    def load_stage(self, stage: dict):
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "quest.json"
            manifest.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "id": "gq_template_tests",
                        "title": "Template tests",
                        "stages": [stage],
                    }
                ),
                encoding="utf-8",
            )
            spec, diagnostics = quest_compiler.load_spec(manifest)
        self.assertIsNotNone(spec, [item.as_dict() for item in diagnostics])
        assert spec is not None
        return spec.stages[0]

    def test_checked_in_templates_are_generator_exact(self) -> None:
        for name, builder in templates.BUILDERS.items():
            with self.subTest(name=name):
                checked_in = json.loads(
                    (
                        ROOT
                        / "source/raw/mod/ghostline/quest_blocks/templates"
                        / f"{name}.questphase.json"
                    ).read_text(encoding="utf-8")
                )
                self.assertEqual(checked_in, builder())

    def test_templates_have_valid_handles_and_conventional_sockets(self) -> None:
        for name in templates.BUILDERS:
            with self.subTest(name=name):
                raw = json.loads(
                    (
                        ROOT
                        / "source/raw/mod/ghostline/quest_blocks/templates"
                        / f"{name}.questphase.json"
                    ).read_text(encoding="utf-8")
                )
                quest_compiler.validate_handle_graph(raw, context=name)
                encoded = json.dumps(raw)
                self.assertIn('"$value": "In1"', encoded)
                self.assertIn('"$value": "Out1"', encoded)

    def test_canonical_bindings_compile_and_implement_typed_contracts(self) -> None:
        for name, stage_value in template_stages().items():
            with self.subTest(name=name):
                stage = self.load_stage(stage_value)
                result = quest_compiler.build_stage_phase(
                    stage,
                    ROOT
                    / "source/archive/mod/gq_template_tests/phases"
                    / f"{name}.questphase",
                )
                quest_compiler.validate_handle_graph(result, context=name)
                encoded = json.dumps(result)
                self.assertNotIn("{{", encoded)

    def test_builtin_templates_need_no_author_written_template_fields(self) -> None:
        for name, stage_value in template_stages().items():
            with self.subTest(name=name):
                stage_value = dict(stage_value)
                stage_value.pop("phase_template")
                stage_value.pop("template_bindings")
                stage = self.load_stage(stage_value)
                result = quest_compiler.build_stage_phase(
                    stage,
                    ROOT
                    / "source/archive/mod/gq_template_tests/phases"
                    / f"{name}.questphase",
                )
                encoded = json.dumps(result)
                self.assertNotIn("{{", encoded)
                expected = (
                    None
                    if name in quest_compiler.DIRECT_STAGE_TYPES
                    else f"{TEMPLATE_DEPOT}\\{name}.questphase"
                )
                self.assertEqual(quest_compiler.stage_template_resource(stage), expected)

    def test_template_placeholders_are_explicit_and_all_are_bound(self) -> None:
        for name, stage_value in template_stages().items():
            with self.subTest(name=name):
                raw = (
                    ROOT
                    / "source/raw/mod/ghostline/quest_blocks/templates"
                    / f"{name}.questphase.json"
                ).read_text(encoding="utf-8")
                placeholders = {
                    value
                    for value in templates.__dict__.values()
                    if isinstance(value, str) and value.startswith("{{")
                    and value in raw
                }
                self.assertEqual(
                    placeholders, set(stage_value["template_bindings"])
                )


if __name__ == "__main__":
    unittest.main()
