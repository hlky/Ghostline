from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

SPEC = importlib.util.spec_from_file_location("generate_scene", TOOLS / "generate_scene.py")
assert SPEC is not None
generate_scene = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["generate_scene"] = generate_scene
SPEC.loader.exec_module(generate_scene)


class GenerateSceneTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec = generate_scene.load_json(TOOLS / "gq000_patch_meet.scene-spec.json")
        cls.scene = generate_scene.build_scene(cls.spec)
        cls.root = cls.scene["Data"]["RootChunk"]

    def test_fixture_shape(self) -> None:
        self.assertEqual(self.scene["Header"]["ExportedDateTime"], self.spec["exported_datetime"])
        self.assertEqual(len(self.root["actors"]), 1)
        self.assertEqual(len(self.root["playerActors"]), 1)
        self.assertEqual(len(self.root["sceneGraph"]["Data"]["graph"]), 17)
        edge_count = sum(len(socket.get("destinations", [])) for node in self.root["sceneGraph"]["Data"]["graph"] for socket in node["Data"].get("outputSockets", []))
        self.assertEqual(edge_count, 18)
        self.assertEqual(len(self.root["screenplayStore"]["lines"]), 13)
        self.assertEqual(len(self.root["screenplayStore"]["options"]), 5)
        self.assertTrue(any(point["name"]["$value"] == "start" for point in self.root["entryPoints"]))
        self.assertTrue(any(point["name"]["$value"] == "job_accept" for point in self.root["exitPoints"]))

    def test_fixture_graph_matches_reduced_scene_order(self) -> None:
        node_ids = [node["Data"]["nodeId"]["id"] for node in self.root["sceneGraph"]["Data"]["graph"]]
        self.assertEqual(node_ids, [1, 10, 11, 12, 13, 2, 15, 16, 17, 8, 3, 4, 5, 9, 6, 7, 18])

    def test_fixture_poi_is_deactivated_before_objective_activation(self) -> None:
        edges = []
        for node in self.root["sceneGraph"]["Data"]["graph"]:
            source = node["Data"]["nodeId"]["id"]
            for socket in node["Data"].get("outputSockets", []):
                for destination in socket.get("destinations", []):
                    edges.append(
                        (
                            source,
                            destination["nodeId"]["id"],
                            destination["isockStamp"]["ordinal"],
                        )
                    )
        self.assertIn((11, 12, 2), edges)
        self.assertIn((2, 15, 1), edges)
        self.assertIn((15, 16, 1), edges)
        self.assertIn((16, 8, 0), edges)
        self.assertNotIn((16, 17, 1), edges)
        self.assertNotIn((17, 8, 0), edges)
        self.assertEqual([edge for edge in edges if edge[0] == 17 or edge[1] == 17], [])
        self.assertIn((3, 8, 0), edges)
        self.assertIn((4, 8, 0), edges)
        self.assertIn((5, 9, 0), edges)
        self.assertIn((9, 6, 0), edges)
        self.assertIn((9, 7, 0), edges)
        self.assertIn((6, 9, 0), edges)
        self.assertIn((7, 18, 0), edges)

    def test_screenplay_ids_use_vanilla_pattern(self) -> None:
        line_ids = [line["itemId"]["id"] for line in self.root["screenplayStore"]["lines"]]
        option_ids = [option["itemId"]["id"] for option in self.root["screenplayStore"]["options"]]
        self.assertEqual(line_ids, [1, 257, 513, 769, 1025, 1281, 1537, 1793, 2049, 2305, 2561, 2817, 3073])
        self.assertEqual(option_ids, [2, 258, 514, 770, 1026])

    def test_fixture_choice_node_has_padded_sockets_and_locstore_entries(self) -> None:
        choices = [
            node["Data"]
            for node in self.root["sceneGraph"]["Data"]["graph"]
            if node["Data"]["$type"] == "scnChoiceNode"
        ]
        self.assertEqual(len(choices), 2)
        self.assertEqual([socket["stamp"]["name"] for socket in choices[0]["outputSockets"]], [0, 0, 0, 1, 2, 3, 4, 5, 6])
        self.assertEqual([socket["stamp"]["name"] for socket in choices[1]["outputSockets"]], [0, 0, 1, 2, 3, 4, 5, 6])
        self.assertEqual([option["isSingleChoice"] for option in choices[0]["options"]], [0, 0, 0])
        self.assertEqual([option["isSingleChoice"] for option in choices[1]["options"]], [0, 0])
        self.assertEqual([option["type"]["properties"] for option in choices[0]["options"]], [0, 0, 1])
        self.assertEqual([option["type"]["properties"] for option in choices[1]["options"]], [0, 1])
        self.assertEqual(len(self.root["locStore"]["vdEntries"]), 20)
        self.assertEqual(len(self.root["locStore"]["vpEntries"]), 20)
        first_choice_locstring = self.root["screenplayStore"]["options"][0]["locstringId"]["ruid"]
        first_choice_rows = [
            entry
            for entry in self.root["locStore"]["vdEntries"]
            if entry["locstringId"]["ruid"] == first_choice_locstring
        ]
        self.assertEqual([entry["localeId"] for entry in first_choice_rows], ["db_db", "db_db", "pl_pl", "en_us"])
        self.assertEqual(self.root["locStore"]["vpEntries"][first_choice_rows[0]["vpeIndex"]]["content"], "")

    def test_validation_passes_and_event_ids_are_not_placeholders(self) -> None:
        self.assertEqual(generate_scene.validate_scene(self.scene, self.spec), [])
        event_ids = []
        for node in self.root["sceneGraph"]["Data"]["graph"]:
            for event in node["Data"].get("events", []):
                event_ids.append(event["Data"]["id"]["id"])
        self.assertEqual(len(event_ids), len(set(event_ids)))
        self.assertNotIn(generate_scene.MAX_INT64, event_ids)

    def test_spoken_only_scene_does_not_require_choice_lines(self) -> None:
        spec = copy.deepcopy(self.spec)
        spec["name"] = "test_spoken_only"
        spec["spoken_line_order"] = ["line_a"]
        spec["choice_line_order"] = []
        spec["sections"] = [{"key": "opening_line", "node_id": 2, "lines": ["line_a"], "on_end": [{"node_id": 18}]}]
        spec["choices"] = []
        spec["quest_nodes"] = []
        spec["xor_nodes"] = []
        spec["start_node"] = {"node_id": 1, "on_start": [{"node_id": 2}]}
        spec["end_node"] = {"node_id": 18}
        spec["entry_point"] = {"name": "start", "node_id": 1}
        spec["exit_points"] = [{"name": "job_accept", "node_id": 18}]
        spec.pop("graph_order", None)

        manifest = {
            "spoken_lines": [
                {
                    "key": "line_a",
                    "string_id": "1000",
                    "speaker": "Patch",
                    "addressee": "V",
                    "text": "You made it.",
                    "duration_ms": 1000,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = Path(tmp) / "manifest.json"
            base_path = Path(tmp) / "base.scene.json"
            base = generate_scene.load_json(ROOT / spec["base_scene"])
            base["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"] = [
                wrapper
                for wrapper in base["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
                if wrapper.get("Data", {}).get("$type") != "scnChoiceNode"
            ]
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            base_path.write_text(json.dumps(base), encoding="utf-8")
            spec["manifest"] = str(manifest_path)
            spec["base_scene"] = str(base_path)
            scene = generate_scene.build_scene(spec)

        root = scene["Data"]["RootChunk"]
        self.assertEqual(root["screenplayStore"]["options"], [])
        self.assertEqual(root["locStore"]["vdEntries"], [])
        self.assertEqual(root["locStore"]["vpEntries"], [])
        self.assertEqual(generate_scene.validate_scene(scene, spec), [])

    def test_locstore_variant_ids_are_reserved_and_unique(self) -> None:
        spec = {
            "name": "test_locstore",
            "choice_line_order": ["choice_a", "choice_b"],
            "choice_locales": ["db_db", "en_us"],
        }
        choice_manifest = {
            "choice_a": {"key": "choice_a", "string_id": "1000", "text": "A"},
            "choice_b": {"key": "choice_b", "string_id": "1004", "text": "B"},
        }
        spoken_manifest = {
            "line_a": {"key": "line_a", "string_id": "1008", "text": "Line"},
        }

        loc_store = generate_scene.build_loc_store(spec, choice_manifest, spoken_manifest)
        variant_ids = [entry["variantId"]["ruid"] for entry in loc_store["vpEntries"]]

        self.assertEqual(len(variant_ids), len(set(variant_ids)))
        self.assertTrue(set(variant_ids).isdisjoint({"1000", "1004", "1008"}))

    def test_validation_rejects_locstore_variant_locstring_collision(self) -> None:
        scene = copy.deepcopy(self.scene)
        root = scene["Data"]["RootChunk"]
        collision = root["screenplayStore"]["lines"][0]["locstringId"]["ruid"]
        root["locStore"]["vpEntries"].append({"variantId": {"ruid": collision}})

        errors = generate_scene.validate_scene(scene, self.spec)

        self.assertTrue(any("locStore variant ids collide with screenplay locstrings" in error for error in errors))

    def test_validation_rejects_wrong_journal_file_entry_index(self) -> None:
        scene = copy.deepcopy(self.scene)
        root = scene["Data"]["RootChunk"]
        for journal_path in generate_scene.iter_journal_paths(root):
            if journal_path.get("realPath", "").endswith("gq000_01_qmp_patch_bridge"):
                journal_path["fileEntryIndex"] = 1

        errors = generate_scene.validate_scene(scene, self.spec)

        self.assertTrue(
            any("gq000_01_qmp_patch_bridge" in error and "expected 2" in error for error in errors)
        )

    def test_validation_rejects_graph_order_drift(self) -> None:
        scene = copy.deepcopy(self.scene)
        graph = scene["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
        graph[8], graph[9] = graph[9], graph[8]

        errors = generate_scene.validate_scene(scene, self.spec)

        self.assertTrue(any("Scene graph order mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
