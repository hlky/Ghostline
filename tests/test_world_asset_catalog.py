import json
import tempfile
import unittest
from pathlib import Path

import jsonschema

from tools.world_asset_catalog import (
    area_from_ref,
    build_catalog,
    discover_categories,
    filter_assets,
    selected_discovery_rows,
)


def sector_document() -> dict:
    return {
        "Data": {
            "RootChunk": {
                "$type": "worldStreamingSector",
                "nodes": [
                    {
                        "HandleId": "1",
                        "Data": {
                            "$type": "worldDeviceNode",
                            "debugName": {"$value": "kab_test_computer"},
                            "entityTemplate": {
                                "DepotPath": {
                                    "$value": "base\\gameplay\\devices\\computers\\computer.ent"
                                }
                            },
                        },
                    },
                    {
                        "HandleId": "2",
                        "Data": {
                            "$type": "worldEntityNode",
                            "debugName": {"$value": "weapon_case_small"},
                            "entityTemplate": {
                                "DepotPath": {
                                    "$value": "base\\gameplay\\loot\\containers\\weapon_case_small.ent"
                                }
                            },
                        },
                    },
                ],
                "nodeData": {
                    "Data": [
                        {
                            "NodeIndex": 0,
                            "QuestPrefabRefHash": {
                                "$value": "$/03_night_city/c_watson/kabuki/loc_test/#computer"
                            },
                            "Position": {"X": 1.0, "Y": 2.0, "Z": 3.0},
                            "Orientation": {"i": 0.0, "j": 0.0, "k": 0.0, "r": 1.0},
                            "Scale": {"X": 1.0, "Y": 1.0, "Z": 1.0},
                        },
                        {
                            "NodeIndex": 1,
                            "QuestPrefabRefHash": {
                                "$value": "$/03_night_city/c_watson/kabuki/loc_test/#loot"
                            },
                            "Position": {"X": 5.0, "Y": 6.0, "Z": 7.0},
                            "Orientation": {"i": 0.0, "j": 0.0, "k": 0.0, "r": 1.0},
                            "Scale": {"X": 1.0, "Y": 1.0, "Z": 1.0},
                        },
                    ]
                },
            }
        }
    }


class WorldAssetCatalogTests(unittest.TestCase):
    def test_binary_discovery_categories(self) -> None:
        categories = discover_categories(
            b"foo COMPUTER bar access_point baz weapon_case satellite"
        )
        self.assertIn("terminal", categories)
        self.assertIn("access_point", categories)
        self.assertIn("loot_anchor", categories)
        self.assertIn("antenna", categories)

    def test_area_is_read_from_world_ref(self) -> None:
        region, area = area_from_ref(
            "$/03_night_city/c_watson/kabuki/loc_sts_wat_kab_101/#device"
        )
        self.assertEqual(("watson", "kabuki"), (region, area))

    def test_deterministic_category_sampling(self) -> None:
        discovery = {
            "sectors": [
                {"path": f"{index}.streamingsector", "categories": ["terminal"]}
                for index in range(10)
            ]
        }
        first = selected_discovery_rows(
            discovery, {"terminal"}, limit_per_category=3, seed="same"
        )
        second = selected_discovery_rows(
            discovery, {"terminal"}, limit_per_category=3, seed="same"
        )
        self.assertEqual(first, second)
        self.assertEqual(3, len(first))

    def test_build_classifies_and_applies_curation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            sectors = root / "sectors"
            sectors.mkdir()
            (sectors / "exterior_0_0_0_0.streamingsector.json").write_text(
                json.dumps(sector_document()), encoding="utf-8"
            )
            curation = root / "curation.json"
            curation.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "annotations": {
                            "$/03_night_city/c_watson/kabuki/loc_test/#computer": {
                                "accessibility": "verified",
                                "quest_safety": "verified",
                                "interior": "exterior",
                                "add_tags": ["readable_terminal"],
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            catalog = build_catalog(sectors, curation)
            catalog_schema = json.loads(
                (
                    Path(__file__).parents[1]
                    / "tools"
                    / "world-asset-catalog-schema-v1.json"
                ).read_text(encoding="utf-8")
            )
            curation_schema = json.loads(
                (
                    Path(__file__).parents[1]
                    / "tools"
                    / "world-asset-curation-schema-v1.json"
                ).read_text(encoding="utf-8")
            )
            jsonschema.Draft202012Validator(catalog_schema).validate(catalog)
            jsonschema.Draft202012Validator(curation_schema).validate(
                json.loads(curation.read_text(encoding="utf-8"))
            )
        self.assertEqual(2, catalog["summary"]["assets"])
        terminal = next(row for row in catalog["assets"] if "terminal" in row["categories"])
        self.assertTrue(terminal["selection_eligible"])
        self.assertIn("readable_terminal", terminal["tags"])
        loot = next(row for row in catalog["assets"] if "loot_anchor" in row["categories"])
        self.assertFalse(loot["selection_eligible"])
        self.assertIn("npc_staging_candidate", loot["tags"])

    def test_filters_require_review_by_default_and_support_distance(self) -> None:
        catalog = {
            "assets": [
                {
                    "id": "a",
                    "categories": ["terminal"],
                    "tags": ["readable_terminal"],
                    "region": "watson",
                    "area": "kabuki",
                    "position": {"x": 0, "y": 0, "z": 0},
                    "selection_eligible": True,
                },
                {
                    "id": "b",
                    "categories": ["terminal"],
                    "tags": ["readable_terminal"],
                    "region": "watson",
                    "area": "kabuki",
                    "position": {"x": 50, "y": 0, "z": 0},
                    "selection_eligible": False,
                },
            ]
        }
        rows = filter_assets(
            catalog,
            categories={"terminal"},
            tags={"readable_terminal"},
            region="watson",
            area=None,
            near=(0, 0, 0),
            radius=10,
            include_unvetted=False,
        )
        self.assertEqual(["a"], [row["id"] for row in rows])


if __name__ == "__main__":
    unittest.main()
