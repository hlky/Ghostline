from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import item_database


def localization_document(entries: list[dict[str, str]]) -> dict:
    return {
        "Data": {
            "RootChunk": {
                "root": {
                    "Data": {
                        "entries": entries,
                    }
                }
            }
        }
    }


def app_document() -> dict:
    def definition(name: str, mesh: str, appearance: str) -> dict:
        return {
            "Data": {
                "$type": "appearanceAppearanceDefinition",
                "name": {"$value": name},
                "components": [
                    {
                        "$type": "entGarmentSkinnedMeshComponent",
                        "name": {"$value": "primary"},
                        "mesh": {"DepotPath": {"$value": mesh}},
                        "meshAppearance": {"$value": appearance},
                        "isEnabled": 1,
                        "chunkMask": "15",
                    },
                    {
                        "$type": "entSkinnedMeshComponent",
                        "name": {"$value": "item_shadow"},
                        "mesh": {
                            "DepotPath": {
                                "$value": r"base\characters\garment\shadow_meshes\shadow.mesh"
                            }
                        },
                        "meshAppearance": {"$value": "default"},
                        "isEnabled": 1,
                    },
                ],
            }
        }

    return {
        "Data": {
            "RootChunk": {
                "appearances": [
                    definition(
                        "basic_01_m",
                        r"base\characters\garment\player_equipment\feet\family\shoe_pma.mesh",
                        "black_red",
                    ),
                    definition(
                        "basic_01_w",
                        r"base\characters\garment\player_equipment\feet\family\shoe_pwa.mesh",
                        "black_red",
                    ),
                ]
            }
        }
    }


class ItemDatabaseTests(unittest.TestCase):
    def test_tweak_parser_resolves_namespaced_inheritance_and_tags(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "base.tweak").write_text(
                """
                package Items
                using RTDB
                [ notQueryable ]
                FootBase : Clothing
                {
                    fk< EquipmentArea > equipArea = "EquipmentArea.Feet";
                    CName entityName = "player_feet_item";
                    CName[] tags +=
                    [
                        "Clothing", "FeetClothing"
                    ];
                }
                Boots : FootBase
                {
                    fk< ItemType > itemType = "ItemType.Clo_Feet";
                }
                """,
                encoding="utf-8",
            )
            (root / "items.tweak").write_text(
                """
                package Items
                Boots_01_basic_01 : Boots
                {
                    displayName = "LocKey#101";
                    localizedDescription = "LocKey#102";
                    appearanceName = "s1_boots_01_basic_01_";
                    tags +=
                    [
                        "Streetwear", "TygerClaws"
                    ];
                }
                """,
                encoding="utf-8",
            )
            records = item_database.load_tweak_records(root)
            resolved = item_database.resolve_record(
                "Items.Boots_01_basic_01", records, {}
            )

        self.assertEqual(resolved["scalars"]["equipArea"], "EquipmentArea.Feet")
        self.assertEqual(resolved["scalars"]["entityName"], "player_feet_item")
        self.assertEqual(
            resolved["tags"],
            ["Clothing", "FeetClothing", "Streetwear", "TygerClaws"],
        )
        self.assertIn("Items.FootBase", resolved["lineage"])

    def test_localization_indexes_primary_and_secondary_keys(self) -> None:
        values = item_database.localization_entries(
            localization_document(
                [
                    {
                        "primaryKey": "101",
                        "secondaryKey": "",
                        "femaleVariant": "Heavy boots",
                        "maleVariant": "",
                    },
                    {
                        "primaryKey": "0",
                        "secondaryKey": "custom_name",
                        "femaleVariant": "",
                        "maleVariant": "Custom",
                    },
                ]
            )
        )
        self.assertEqual(values["101"], "Heavy boots")
        self.assertEqual(values["custom_name"], "Custom")

    def test_app_rows_choose_primary_and_retain_companions(self) -> None:
        rows = item_database.app_appearance_rows(
            app_document(),
            r"base\characters\appearances\player\items\feet\s1_boots_01.app",
        )

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["lookup"], "s1_boots_01_basic_01")
        self.assertEqual(rows[0]["frame"], "pma")
        self.assertEqual(rows[0]["mesh_appearance"], "black_red")
        self.assertEqual(len(rows[0]["components"]), 2)
        self.assertTrue(rows[0]["components"][1]["shadow"])

    def test_database_build_joins_item_to_both_body_frames(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            tweaks = root / "tweaks"
            apps = root / "apps/base/characters/appearances/player/items/feet"
            tweaks.mkdir()
            apps.mkdir(parents=True)
            (tweaks / "items.tweak").write_text(
                """
                package Items
                FootBase : Clothing
                {
                    equipArea = "EquipmentArea.Feet";
                    entityName = "player_feet_item";
                    itemType = "ItemType.Clo_Feet";
                }
                Boots_01_basic_01 : FootBase
                {
                    displayName = "LocKey#101";
                    localizedDescription = "LocKey#102";
                    appearanceName = "s1_boots_01_basic_01_";
                    tags += [ "Streetwear", "TygerClaws" ];
                }
                """,
                encoding="utf-8",
            )
            app = app_document()
            app["Header"] = {
                "ArchiveFileName": (
                    r"base\characters\appearances\player\items\feet\s1_boots_01.app"
                )
            }
            (apps / "s1_boots_01.app.json").write_text(
                json.dumps(app), encoding="utf-8"
            )
            localization = root / "onscreens.json.json"
            localization.write_text(
                json.dumps(
                    localization_document(
                        [
                            {
                                "primaryKey": "101",
                                "secondaryKey": "",
                                "femaleVariant": "Night City boots",
                                "maleVariant": "",
                            },
                            {
                                "primaryKey": "102",
                                "secondaryKey": "",
                                "femaleVariant": "Built for bad pavement.",
                                "maleVariant": "",
                            },
                        ]
                    )
                ),
                encoding="utf-8",
            )
            database = root / "items.sqlite3"
            summary = item_database.build_database(
                database, tweaks, root / "apps", [localization], root / "catalog.json"
            )
            connection = item_database.connect(database)
            variants = item_database.query_variants(
                connection, query="pavement", tag="TygerClaws"
            )
            total = item_database.count_variants(
                connection, query="pavement", tag="TygerClaws"
            )
            connection.close()

        self.assertEqual(summary["items"], 1)
        self.assertEqual(summary["variants"], 2)
        self.assertEqual({row["frame"] for row in variants}, {"pma", "pwa"})
        self.assertEqual(variants[0]["title"], "Night City boots")
        self.assertEqual(total, 2)

    def test_caption_export_keeps_game_tags_separate_from_generated_schema(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            connection = item_database.connect(root / "items.sqlite3")
            item_database.create_schema(connection)
            connection.execute(
                "INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    "Items.Test",
                    "Test item",
                    "Description",
                    "",
                    "",
                    "EquipmentArea.Feet",
                    "feet",
                    "ItemType.Clo_Feet",
                    "player_feet_item",
                    "test_",
                    '["Military"]',
                    "test.tweak",
                    "[]",
                ),
            )
            connection.execute(
                "INSERT INTO variants VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    "Items.Test:pma:test",
                    "Items.Test",
                    "pma",
                    "test.app",
                    "default_m",
                    "base_game",
                    "test.mesh",
                    "default",
                    "[]",
                ),
            )
            connection.execute(
                "INSERT INTO renders VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    "render",
                    "Items.Test:pma:test",
                    str(root / "hero.png"),
                    json.dumps([str(root / "hero.png")]),
                    "fingerprint",
                    "Blender",
                    "complete",
                    "",
                ),
            )
            connection.commit()
            connection.close()
            output = root / "jobs.jsonl"
            result = item_database.caption_jobs(
                root / "items.sqlite3", output, only_rendered=True, limit=10
            )
            job = json.loads(output.read_text(encoding="utf-8"))

        self.assertEqual(result["jobs"], 1)
        self.assertEqual(job["game_tags"], ["Military"])
        self.assertEqual(job["caption_schema"]["style"], [])
        self.assertEqual(job["images"][0], str(root / "hero.png"))


if __name__ == "__main__":
    unittest.main()
