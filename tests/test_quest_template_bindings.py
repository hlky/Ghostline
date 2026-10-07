"""Live template instantiation must bind its runtime scalars completely."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import quest_compiler as compiler
from quest_types import CompiledStage, QuestSpecError
from tests.test_quest_block_builders import GraphRun, objects


def cleanup(**fields):
    data = {
        "phase_template": r"mod\gqt004\templates\gqt004_final_cleanup.questphase",
        "completion_fact": "test_completed",
        "player_vehicle_record": "Vehicle.test",
        **fields,
    }
    return CompiledStage(
        0, "cleanup", "vehicle_cleanup", "ready", r"mod\test\cleanup.questphase", data
    )


def template(vehicle="{{player_vehicle_record}}", **fields):
    return {
        "Header": {"ArchiveFileName": "donor", "notes": "{{header_metadata}}"},
        "Data": {
            "RootChunk": {"vehicle": vehicle, "fact": "{{completion_fact}}", **fields}
        },
    }


def instantiate(stage, document):
    return compiler.instantiate_stage_phase(
        stage, ROOT / "generated/tests/cleanup.questphase", template_document=document
    )


class QuestTemplateBindingTests(unittest.TestCase):
    def test_vehicle_record_is_bound_only_when_requested_by_template(self):
        document = template()
        original = copy.deepcopy(document)
        result = instantiate(cleanup(), document)
        self.assertEqual(
            result["Data"]["RootChunk"],
            {"vehicle": "Vehicle.test", "fact": "test_completed"},
        )
        self.assertEqual(document, original)
        self.assertEqual(result["Header"]["notes"], "{{header_metadata}}")
        constant = instantiate(cleanup(), template("Vehicle.quest_owned_constant"))
        self.assertEqual(
            constant["Data"]["RootChunk"]["vehicle"], "Vehicle.quest_owned_constant"
        )

    def test_missing_vehicle_field_does_not_leave_a_live_token(self):
        stage = cleanup()
        stage.data.pop("player_vehicle_record")
        with self.assertRaisesRegex(
            QuestSpecError, r"cleanup.*unresolved.*\{\{player_vehicle_record\}\}"
        ):
            instantiate(stage, template())

    def test_explicit_bindings_remain_authoritative_and_checked(self):
        bindings = {
            "{{completion_fact}}": "explicit_completed",
            "{{player_vehicle_record}}": "Vehicle.explicit",
        }
        result = instantiate(cleanup(template_bindings=bindings), template())
        self.assertEqual(
            result["Data"]["RootChunk"],
            {"vehicle": "Vehicle.explicit", "fact": "explicit_completed"},
        )
        with self.assertRaisesRegex(QuestSpecError, "map strings to strings"):
            instantiate(
                cleanup(template_bindings={"{{completion_fact}}": 1}), template()
            )
        with self.assertRaisesRegex(QuestSpecError, "not present"):
            instantiate(
                cleanup(template_bindings={**bindings, "{{typo}}": "unused"}),
                template(),
            )
        with self.assertRaisesRegex(QuestSpecError, "unresolved"):
            instantiate(
                cleanup(template_bindings={"{{completion_fact}}": "partial"}),
                template(),
            )

    def test_nested_embedded_and_reintroduced_tokens_are_rejected(self):
        for value in (
            [{"label": "{{unbound}}"}],
            {"{{unbound}}": 1},
            "prefix {{unbound}} suffix",
        ):
            with (
                self.subTest(value=value),
                self.assertRaisesRegex(QuestSpecError, "unresolved.*unbound"),
            ):
                instantiate(cleanup(), template(extra=value))
        with self.assertRaisesRegex(QuestSpecError, "unresolved.*another"):
            instantiate(cleanup(player_vehicle_record="{{another}}"), template())

    def test_gqt004_cleanup_uses_the_reviewed_vehicle_record(self):
        path = ROOT / "projects/test-quests/gqt004/gqt004_vehicle_lab.quest.json"
        spec, diagnostics = compiler.load_spec(path)
        self.assertFalse([item for item in diagnostics if item.level == "error"])
        stage = next(
            stage for stage in spec.stages if stage.id == "cleanup_test_vehicle"
        )
        raw, archive = compiler.resource_paths(stage.phase_resource)
        reviewed = json.loads(raw.read_text(encoding="utf-8"))
        result = compiler.build_stage_phase(stage, archive, spec.phase_prefabs)

        def vehicles(document):
            return [
                item["vehicle"]
                for item in objects(document)
                if item.get("$type") == "questEnablePlayerVehicle_NodeType"
            ]

        self.assertEqual(vehicles(result), vehicles(reviewed))
        self.assertEqual(vehicles(result), ["Vehicle.GhostlineGQT004Theft"])
        self.assertNotIn("{{", json.dumps(result["Data"]))

    def test_gqt004_stolen_fact_is_on_the_only_completion_route(self):
        spec, _ = compiler.load_spec(
            ROOT / "projects/test-quests/gqt004/gqt004_vehicle_lab.quest.json"
        )
        stage = next(stage for stage in spec.stages if stage.id == "steal_test_vehicle")
        _, archive = compiler.resource_paths(stage.phase_resource)
        graph = GraphRun(compiler.build_stage_phase(stage, archive, spec.phase_prefabs))
        fact_nodes = [
            handle
            for handle, node in graph.nodes.items()
            if any(
                item.get("factName") == "gqt004_vehicle_stolen"
                for item in objects(node)
            )
        ]
        self.assertEqual(len(fact_nodes), 1)
        fact = fact_nodes[0]
        end = next(
            handle
            for handle, node in graph.nodes.items()
            if node["$type"] == "questOutputNodeDefinition"
        )
        incoming = [
            source
            for source, destinations in graph.edges.items()
            if any(target[0] == fact for target in destinations)
        ]
        endings = [
            source
            for source, destinations in graph.edges.items()
            if any(target[0] == end for target in destinations)
        ]
        self.assertEqual(len(incoming), 1)
        self.assertEqual(endings, [(fact, "Out")])
        self.assertEqual(graph.edges[fact, "Out"], [(end, "In")])


if __name__ == "__main__":
    unittest.main()
