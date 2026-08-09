from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.indoor_location_candidates import build_manifest, cet_manifest, classify_site


def handle(node_type: str, name: str) -> dict:
    return {
        "HandleId": "1",
        "Data": {
            "$type": node_type,
            "debugName": {"$value": name},
            "outline": {
                "Data": {
                    "$type": "AreaShapeOutline",
                    "height": 3,
                    "points": [
                        {"X": -2, "Y": -1, "Z": 0},
                        {"X": 2, "Y": -1, "Z": 0},
                        {"X": 2, "Y": 1, "Z": 0},
                        {"X": -2, "Y": 1, "Z": 0},
                    ],
                }
            },
        },
    }


def placement(index: int, x: float, quest_ref: str = "0") -> dict:
    return {
        "NodeIndex": index,
        "Position": {"X": x, "Y": 2, "Z": 3},
        "Scale": {"X": 2, "Y": 2, "Z": 2},
        "QuestPrefabRefHash": {"$value": quest_ref},
    }


class IndoorLocationCandidatesTests(unittest.TestCase):
    def write_sector(self, root: Path, name: str, nodes: list[dict], placements: list[dict]) -> None:
        path = root / name
        path.write_text(
            json.dumps({"Data": {"RootChunk": {"nodes": nodes, "nodeData": {"Data": placements}}}}),
            encoding="utf-8",
        )

    def test_labels_unowned_and_collects_support(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_sector(
                root,
                "exterior_1_1_0_0.streamingsector.json",
                [handle("worldInteriorAreaNode", "quiet_room"), handle("worldAISpotNode", "sit_at_bar"), handle("worldEntityNode", "front_door")],
                [placement(0, 0), placement(1, 3), placement(2, 4)],
            )
            result = build_manifest(root, support_radius=10, quest_radius=20)
            candidate = result["candidates"][0]
            self.assertEqual("likely_unowned", candidate["ownership"])
            self.assertEqual(1, candidate["nearby_signals"]["workspots"])
            self.assertEqual(1, candidate["nearby_signals"]["doors"])
            self.assertEqual({"points": 4, "width": 8.0, "depth": 4.0, "height": 6.0}, candidate["outline"])

    def test_labels_nearby_quest_identifier(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_sector(
                root,
                "exterior_2_2_0_0.streamingsector.json",
                [handle("worldInteriorAreaNode", "back_room"), handle("worldEntityNode", "sq021_control")],
                [placement(0, 0), placement(1, 8, "$/loc_sq021_trailer")],
            )
            result = build_manifest(root, support_radius=10, quest_radius=20)
            candidate = result["candidates"][0]
            self.assertEqual("quest_linked", candidate["ownership"])
            self.assertEqual(["sq021"], candidate["quest_evidence"]["quest_ids"])
            self.assertEqual(8.0, candidate["quest_evidence"]["nearest_distance"])

    def test_does_not_treat_outdoor_or_lifted_as_indoor_signals(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_sector(
                root,
                "exterior_3_3_0_0.streamingsector.json",
                [handle("worldInteriorAreaNode", "room"), handle("worldMeshNode", "outdoor_bench"), handle("worldMeshNode", "advertising_lifted_a")],
                [placement(0, 0), placement(1, 2), placement(2, 3)],
            )
            candidate = build_manifest(root, support_radius=10, quest_radius=20)["candidates"][0]
            self.assertNotIn("doors", candidate["nearby_signals"])
            self.assertNotIn("elevators", candidate["nearby_signals"])
            self.assertEqual(1, candidate["nearby_signals"]["seating"])

    def test_minor_activity_is_content_linked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_sector(
                root,
                "exterior_4_4_0_0.streamingsector.json",
                [handle("worldInteriorAreaNode", "room"), handle("worldEntityNode", "ma_hey_rey_06_access_point")],
                [placement(0, 0), placement(1, 4)],
            )
            candidate = build_manifest(root, support_radius=10, quest_radius=20)["candidates"][0]
            self.assertEqual("quest_linked", candidate["ownership"])
            self.assertEqual(["ma_hey_rey_06"], candidate["quest_evidence"]["quest_ids"])

    def test_cet_export_is_compact_and_filterable(self) -> None:
        source = {
            "schema_version": 1,
            "candidates": [
                {
                    "candidate_id": "indoor_a",
                    "debug_name": "room_a",
                    "ownership": "likely_unowned",
                    "review_score": 72,
                    "position": {"x": 1, "y": 2, "z": 3},
                    "source": {"sector": "exterior_a.streamingsector.json"},
                    "quest_evidence": {"quest_ids": []},
                    "nearby_signals": {"doors": 2},
                },
                {
                    "candidate_id": "indoor_b",
                    "ownership": "quest_linked",
                    "review_score": 99,
                    "position": {"x": 4, "y": 5, "z": 6},
                },
            ],
        }
        result = cet_manifest(source, ownership="likely_unowned", minimum_score=70)
        self.assertEqual(1, result["count"])
        self.assertEqual("indoor_a", result["locations"][0]["id"])
        self.assertEqual({"doors": 2}, result["locations"][0]["signals"])

    def test_classifies_retail_and_story_locations(self) -> None:
        self.assertEqual(("clothing_shop", True, False), classify_site("{wbr_jpn_cloth_01_interior_area}"))
        self.assertEqual(("ripperdoc", True, False), classify_site("{std_arr_ripdoc_01_interior}"))
        self.assertEqual(("story_landmark", False, True), classify_site("{loc_arasaka_tower_interior_area_jungle}"))


if __name__ == "__main__":
    unittest.main()
