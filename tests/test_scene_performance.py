"""Composed performance bindings and failure-boundary tests; no engine simulation."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import generate_scene
import scene_performance
from build_scene_performance_library import expand, walk


class ScenePerformanceTests(unittest.TestCase):
    def setUp(self):
        self.spec = json.loads((ROOT / "quests/examples/interaction-performance.scene-spec.json").read_text(encoding="utf-8"))

    def build(self):
        return generate_scene.build_scene(self.spec)

    def test_example_compiles_without_mutation_with_complete_bindings(self):
        before = copy.deepcopy(self.spec)
        scene = self.build()
        self.assertEqual(generate_scene.validate_scene(scene, self.spec), [])
        self.assertEqual(self.spec, before)
        self.assertEqual(scene, self.build())
        root = scene["Data"]["RootChunk"]
        body = [e for e in walk(root) if e.get("$type") == "scnPlaySkAnimEvent"]
        self.assertEqual(len(body), 9)
        self.assertTrue(root["resouresReferences"]["cinematicAnimSets"])
        paths = [ref["asyncAnimSet"]["DepotPath"]["$value"] for ref in root["resouresReferences"]["cinematicAnimSets"]]
        self.assertEqual(len(paths), len(set(paths)))

    def test_all_frozen_events_match_source_pointers_and_source_hashes(self):
        catalog = json.loads(scene_performance.CATALOG.read_text())
        for key in catalog["blocks"]:
            donor = scene_performance.recipe(key)
            path = ROOT / donor["source"]["path"]
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), donor["source"]["sha256"])
            raw = json.loads(path.read_text(encoding="utf-8"))
            handles = {str(v["HandleId"]): v for v in walk(raw) if "HandleId" in v}
            for expected, pointer in zip(donor["events"], donor["source"]["event_pointers"], strict=True):
                value = raw
                for part in pointer.split("/")[1:]:
                    value = value[int(part)] if isinstance(value, list) else value[part]
                self.assertEqual(expected, expand(value, handles))

    def test_non_player_donor_257_remaps_to_npc_instead_of_real_v(self):
        root = self.build()["Data"]["RootChunk"]
        node = next(n["Data"] for n in root["sceneGraph"]["Data"]["graph"] if n["Data"]["nodeId"]["id"] == 70)
        performers = {e["Data"]["performer"]["id"] for e in node["events"] if e["Data"]["$type"] == "scnPlaySkAnimEvent"}
        self.assertEqual(performers, {1, 513})

    def test_real_player_cannot_bind_npc_body_role(self):
        self.spec["performance_blocks"][1]["actors"]["speaker"] = "v"
        with self.assertRaisesRegex(generate_scene.SceneBuildError, "NPC/player kind"):
            self.build()

    def test_root_motion_cannot_inherit_barry_apartment_offset(self):
        del self.spec["performance_blocks"][1]["root_motion"]
        with self.assertRaisesRegex(generate_scene.SceneBuildError, "placement required"):
            self.build()

    def test_placement_and_pose_corrections_survive_rebinding(self):
        root = self.build()["Data"]["RootChunk"]
        node = next(n["Data"] for n in root["sceneGraph"]["Data"]["graph"] if n["Data"]["nodeId"]["id"] == 20)
        motion = node["events"][0]["Data"]["rootMotionData"]
        self.assertEqual(motion["originOffset"]["position"]["X"], 0)
        self.assertEqual(motion["originMarker"]["nodeRef"]["$value"], "#performance_preview_chair_origin")
        self.assertEqual(sum(e["Data"]["$type"] == "scnPoseCorrectionEvent" for e in node["events"]), 3)

    def test_missing_timed_output_consumer_is_rejected(self):
        del self.spec["performance_blocks"][4]["on"]
        with self.assertRaisesRegex(generate_scene.SceneBuildError, "every preset port"):
            self.build()

    def test_timed_outputs_cannot_enter_cut_socket(self):
        self.spec["performance_blocks"][4]["on"]["idle_only"][0]["input_ordinal"] = 0
        with self.assertRaisesRegex(generate_scene.SceneBuildError, "executable input"):
            self.build()

    def test_output_stamp_is_allocated_and_connected(self):
        root = self.build()["Data"]["RootChunk"]
        node = next(n["Data"] for n in root["sceneGraph"]["Data"]["graph"] if n["Data"]["nodeId"]["id"] == 60)
        event = next(e["Data"] for e in node["events"] if e["Data"]["$type"] == "scneventsSocket")
        self.assertEqual(event["startTime"], 0)
        port = next(s for s in node["outputSockets"] if s["stamp"] == event["osockStamp"])
        self.assertEqual(port["destinations"][0]["nodeId"]["id"], 80)

    def test_overlapping_body_blocks_are_rejected(self):
        other = copy.deepcopy(self.spec["performance_blocks"][2])
        other["key"] = "collision"
        self.spec["performance_blocks"].append(other)
        with self.assertRaisesRegex(generate_scene.SceneBuildError, "overlapping full-body"):
            self.build()

    def test_anchor_uses_target_dialogue_timing(self):
        section = self.spec["sections"][1]
        section["lines"] *= 2
        with self.assertRaisesRegex(generate_scene.SceneBuildError, "exactly once"):
            self.build()

    def test_move_is_not_a_teleport_and_keeps_work_started_distinct(self):
        expanded = scene_performance.expand_moves(self.spec)
        move = expanded["quest_nodes"][0]
        self.assertFalse(move["teleport"])
        self.assertFalse(move["instant"])
        self.assertNotEqual(move["on_success"], move["on_work_started"])
        root = self.build()["Data"]["RootChunk"]
        stop = next(v for v in walk(root) if v.get("$type") == "questUseWorkspotParamsV1" and v.get("function") == "StopWorkspot")
        self.assertEqual(stop["exitEntryId"]["id"], 4294967295)
        idle = next(v for v in walk(root) if v.get("$type") == "questUseWorkspotParamsV1" and v.get("function") == "IdleOnlyMode")
        self.assertEqual(idle["enableIdleMode"], 1)

    def test_independent_validation_detects_lost_resource_and_timed_socket(self):
        scene = self.build()
        root = scene["Data"]["RootChunk"]
        root["actors"][0]["bodyCinematicAnimSets"] = []
        for node in root["sceneGraph"]["Data"]["graph"]:
            if node["Data"]["nodeId"]["id"] == 60:
                node["Data"]["outputSockets"] = node["Data"]["outputSockets"][:2]
        errors = generate_scene.validate_scene(scene, self.spec)
        self.assertTrue(any("resource/name" in e for e in errors))
        self.assertTrue(any("matching output socket" in e for e in errors))

    def test_unknown_fields_cannot_silently_change_choreography(self):
        self.spec["performance_blocks"][2]["speed"] = 2
        with self.assertRaisesRegex(generate_scene.SceneBuildError, "unsupported fields"):
            self.build()


if __name__ == "__main__":
    unittest.main()
