from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import index_world_assets


PLATE_ANTENNA = r"base\gameplay\devices\distractors\plate_antenna_large.ent"


class WorldAssetIndexTests(unittest.TestCase):
    def test_indexes_all_placements_for_an_exact_resource(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = {
                "Data": {
                    "RootChunk": {
                        "nodes": [
                            {
                                "Data": {
                                    "$type": "worldEntityNode",
                                    "debugName": {"$value": "plate_antenna_large"},
                                    "entityTemplate": {"DepotPath": {"$value": PLATE_ANTENNA}},
                                }
                            }
                        ],
                        "nodeData": {
                            "Data": [
                                {
                                    "NodeIndex": 0,
                                    "Position": {"X": 1, "Y": 2, "Z": 3},
                                    "Orientation": {"i": 0, "j": 0, "k": 0, "r": 1},
                                    "QuestPrefabRefHash": {"$value": "$/fixture/antenna_a"},
                                },
                                {
                                    "NodeIndex": 0,
                                    "Position": {"X": 4, "Y": 5, "Z": 6},
                                    "Orientation": {"i": 0, "j": 0, "k": 1, "r": 0},
                                    "QuestPrefabRefHash": {"$value": "$/fixture/antenna_b"},
                                },
                            ]
                        },
                    }
                }
            }
            path = root / "exterior_0_0_0_0.streamingsector.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            manifest = index_world_assets.build_index(root, {PLATE_ANTENNA})

        self.assertEqual(2, manifest["summary"]["instances"])
        self.assertEqual(
            ["$/fixture/antenna_a", "$/fixture/antenna_b"],
            [row["node_ref"] for row in manifest["instances"]],
        )

    def test_near_query_sorts_and_filters_instances(self) -> None:
        manifest = {
            "instances": [
                {"resource": PLATE_ANTENNA, "position": {"x": 10, "y": 0, "z": 0}},
                {"resource": PLATE_ANTENNA, "position": {"x": 2, "y": 0, "z": 0}},
                {"resource": PLATE_ANTENNA, "position": None},
            ]
        }
        rows = index_world_assets.filtered_rows(
            manifest,
            resource="plate_antenna",
            near=(0, 0, 0),
            radius=5,
        )
        self.assertEqual([2.0], [row["distance"] for row in rows])


if __name__ == "__main__":
    unittest.main()
