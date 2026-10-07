from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import phase_graph
import quest_compiler
import quest_encounter
from quest_types import CompiledStage


class QuestEncounterTests(unittest.TestCase):
    def test_generated_bytes_match_five_pre_extraction_cases(self):
        # Captured from the original builder before extraction, using a portable
        # archive filename. Covers real GQT006 plus distinct optional branches.
        fixture = json.loads(
            (ROOT / "tests/fixtures/quest_encounter_cases.json").read_text(
                encoding="utf-8"
            )
        )
        for name, case in fixture["cases"].items():
            with self.subTest(case=name):
                data = deepcopy(case["data"])
                before = deepcopy(data)
                stage = CompiledStage(
                    0,
                    data["id"],
                    data["type"],
                    data.get("status", "ready"),
                    data["phase_resource"],
                    data,
                )
                document = quest_encounter.build_cyberpsycho_encounter_phase(
                    stage, Path("fixture.questphase")
                )
                rendered = json.dumps(document, ensure_ascii=False, indent=2) + "\n"
                self.assertEqual(
                    hashlib.sha256(rendered.encode()).hexdigest(), case["sha256"]
                )
                self.assertEqual(data, before)
                quest_compiler.validate_handle_graph(document, context=name)
                quest_compiler.validate_no_forward_handle_refs(document, context=name)

    def test_compiler_reexports_encounter_api_without_duplicate_implementations(self):
        for name in (
            "build_cyberpsycho_encounter_phase",
            "scene_flow_node",
            "named_character_spawned_node",
            "character_mortality_node",
            "clear_ai_role_node",
        ):
            self.assertIs(getattr(quest_compiler, name), getattr(quest_encounter, name))
        self.assertIs(quest_compiler.resource_ref, phase_graph.resource_ref)


if __name__ == "__main__":
    unittest.main()
