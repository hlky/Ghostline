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

import index_drop_points


KABUKI_009 = (
    "$/03_night_city/c_watson/kabuki/"
    "kabuki_drop_points_prefabAR4NTYY/drop_point_009_prefabBIYNP3Y"
)
KABUKI_004 = (
    "$/03_night_city/c_watson/kabuki/"
    "kabuki_drop_points_prefabAR4NTYY/drop_point_004_prefabBIYNP3Y"
)


def write(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def sector_document(node_ref: str, position: tuple[float, float, float]) -> dict:
    return {
        "Data": {
            "RootChunk": {
                "nodes": [
                    {
                        "HandleId": "1",
                        "Data": {
                            "$type": "worldEntityNode",
                            "appearanceName": {"$value": "default"},
                            "debugName": {"$value": "drop_point_009"},
                            "entityTemplate": {
                                "DepotPath": {"$value": index_drop_points.DROP_POINT_TEMPLATE}
                            },
                        },
                    }
                ],
                "nodeData": {
                    "Data": [
                        {
                            "NodeIndex": 0,
                            "Position": {"X": position[0], "Y": position[1], "Z": position[2]},
                            "Orientation": {"i": 0, "j": 0, "k": 1, "r": 0},
                            "QuestPrefabRefHash": {"$value": node_ref},
                        }
                    ]
                },
            }
        }
    }


class DropPointIndexTests(unittest.TestCase):
    def test_sector_scan_extracts_native_drop_point_transform(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "exterior_-19_20_0_0.streamingsector.json"
            write(path, sector_document(KABUKI_009, (-1168.66333, 1309.51709, 19.9768238)))
            rows, warnings = index_drop_points.drop_point_rows(root)

        self.assertEqual([], warnings)
        self.assertEqual(1, len(rows))
        self.assertEqual(KABUKI_009, rows[0]["node_ref"])
        self.assertEqual("watson", rows[0]["region"])
        self.assertEqual("kabuki", rows[0]["area"])
        self.assertAlmostEqual(180.0, rows[0]["yaw_degrees"])

    def test_build_keeps_physical_mappin_and_accessibility_evidence_separate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            sectors = root / "sectors"
            write(
                sectors / "exterior_-19_20_0_0.streamingsector.json",
                sector_document(KABUKI_009, (-1168.66333, 1309.51709, 19.9768238)),
            )
            mappins = root / "03_night_city.mappins.json"
            write(
                mappins,
                {
                    "Data": {
                        "Version": 195,
                        "RootChunk": {
                            "cookedData": [
                                {
                                    "journalPathHash": 123,
                                    "position": {"X": -1168.66333, "Y": 1309.51709, "Z": 19.9768238},
                                }
                            ],
                            "cookedMultiData": [],
                        },
                    }
                },
            )
            journals = root / "journals"
            write(journals / "fixture.journal.json", {"ref": {"$value": KABUKI_009}})
            curation = root / "curation.json"
            write(
                curation,
                {
                    "fallback_nodes": [],
                    "annotations": {
                        KABUKI_009: {
                            "accessibility": "verified",
                            "runtime_map_label": "verified",
                        }
                    },
                },
            )
            manifest = index_drop_points.build_index(sectors, mappins, journals, curation)

        row = manifest["drop_points"][0]
        self.assertTrue(row["mappin_evidence"]["backed"])
        self.assertEqual("verified", row["mappin_evidence"]["status"])
        self.assertEqual("verified", row["accessibility"])
        self.assertTrue(row["selection_eligible"])

    def test_checked_manifest_has_expected_exhaustive_and_curated_counts(self) -> None:
        manifest = index_drop_points.read_json(index_drop_points.DEFAULT_MANIFEST)
        self.assertEqual(
            {
                "physical_entities": 103,
                "sectors": 101,
                "mappin_backed_entities": 99,
                "canonical_multi_mappin_entities": 98,
                "runtime_verified_accessible": 1,
                "rejected": 1,
                "selection_eligible": 1,
                "missing_orientation": 1,
            },
            manifest["summary"],
        )
        by_ref = {row["node_ref"]: row for row in manifest["drop_points"]}
        self.assertTrue(by_ref[KABUKI_009]["selection_eligible"])
        self.assertEqual("rejected", by_ref[KABUKI_004]["accessibility"])
        fallback = by_ref[
            "$/03_night_city/#c_city_center/corpo_plaza/"
            "corpo_plaza_drop_points_prefabXUE62AA/drop_point_003_prefabXWGYJHY"
        ]
        self.assertIsNone(fallback["orientation"])
        self.assertIn("serialization_fallback", fallback)

    def test_default_filter_excludes_unvetted_and_rejected_rows(self) -> None:
        manifest = index_drop_points.read_json(index_drop_points.DEFAULT_MANIFEST)
        rows = index_drop_points.filtered_rows(
            manifest,
            include_unvetted=False,
            region=None,
            area=None,
        )
        self.assertEqual([KABUKI_009], [row["node_ref"] for row in rows])


if __name__ == "__main__":
    unittest.main()
