from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import character_asset_index


class CharacterAssetIndexTests(unittest.TestCase):
    def test_archive_listing_keeps_only_resolved_depot_paths(self) -> None:
        output = "\n".join(
            [
                "[ 0: Information ] loading",
                r"base\characters\garment\player_equipment\feet\boots\boots_pma.mesh",
                "1234567890",
                r"ep1\characters\common\hair\hair_wa.mesh",
            ]
        )
        self.assertEqual(
            character_asset_index.parse_archive_listing(output),
            [
                r"base\characters\garment\player_equipment\feet\boots\boots_pma.mesh",
                r"ep1\characters\common\hair\hair_wa.mesh",
            ],
        )

    def test_player_equipment_classification_retains_slot_frame_and_family(self) -> None:
        asset = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\torso\1_004_tshirt__longsleeve\1_004_pma_tshirt__longsleeve.mesh",
            "archive/pc/content/basegame_4_appearance.archive",
        )
        self.assertEqual(asset["category"], "clothing")
        self.assertEqual(asset["slot"], "torso")
        self.assertEqual(asset["family"], "1_004_tshirt__longsleeve")
        self.assertEqual(asset["frame_tokens"], ["pma"])
        self.assertTrue(asset["previewable"])
        self.assertTrue(asset["warnings"])

    def test_search_filters_category_slot_frame_and_words(self) -> None:
        shirt = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\torso\shirt\shirt_pma.mesh", "base"
        )
        boots = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\feet\military_boot\military_boot_pwa.mesh",
            "base",
        )
        index = {"assets": [shirt, boots]}
        self.assertEqual(
            character_asset_index.search_assets(index, "military", "clothing", "feet", "pwa"),
            [boots],
        )

    def test_mesh_appearance_metadata_reads_real_cr2w_shape(self) -> None:
        document = {
            "Header": {"DataType": "CR2W"},
            "Data": {
                "RootChunk": {
                    "appearances": [
                        {
                            "Data": {
                                "$type": "meshMeshAppearance",
                                "name": {"$value": "black_red"},
                                "chunkMaterials": [
                                    {"$value": "boot_black_red"},
                                    {"$value": "stitches_black"},
                                ],
                            }
                        },
                        {
                            "Data": {
                                "$type": "meshMeshAppearance",
                                "name": {"$value": "default"},
                                "chunkMaterials": [],
                            }
                        },
                    ]
                }
            }
        }
        self.assertEqual(
            character_asset_index.mesh_appearance_metadata(document),
            [
                {
                    "name": "black_red",
                    "materials": ["boot_black_red", "stitches_black"],
                },
                {"name": "default", "materials": []},
            ],
        )

    def test_mesh_appearance_metadata_rejects_malformed_material_shape(self) -> None:
        document = {
            "Header": {"DataType": "CR2W"},
            "Data": {
                "RootChunk": {
                    "appearances": [
                        {
                            "Data": {
                                "$type": "meshMeshAppearance",
                                "name": {"$value": "default"},
                                "chunkMaterials": None,
                            }
                        }
                    ]
                }
            },
        }
        with self.assertRaises(character_asset_index.CharacterAssetIndexError):
            character_asset_index.mesh_appearance_metadata(document)

    def test_pma_primary_clothing_is_assignable_to_supported_manifest_slot(self) -> None:
        asset = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\feet\boots\s1_001_pma_boots.mesh",
            "base",
        )
        support = character_asset_index.selection_support(asset)
        assignment = character_asset_index.canonical_indexed_override(
            asset, "black_red", ["default", "black_red"]
        )

        self.assertTrue(support["supported"], support["reasons"])
        self.assertEqual(support["manifest_category"], "feet")
        self.assertEqual(assignment["override"]["mesh_appearance"], "black_red")

    def test_pwa_primary_clothing_is_assignable_only_to_female_frame(self) -> None:
        asset = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\torso\shirt\t1_001_pwa_shirt.mesh",
            "base",
        )
        female_support = character_asset_index.selection_support(asset, "pwa")
        assignment = character_asset_index.canonical_indexed_override(
            asset, "default", ["default"], "pwa"
        )

        self.assertTrue(female_support["supported"], female_support["reasons"])
        self.assertEqual(female_support["required_frame"], "pwa")
        self.assertEqual(assignment["manifest_category"], "inner_torso")
        self.assertFalse(character_asset_index.selection_support(asset, "pma")["supported"])

    def test_pwa_torso_clothing_can_target_outer_torso(self) -> None:
        asset = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\torso\jacket\t2_001_pwa_jacket.mesh",
            "base",
        )
        assignment = character_asset_index.canonical_indexed_override(
            asset,
            "black",
            ["default", "black"],
            "pwa",
            "outer_torso",
        )

        self.assertEqual(assignment["manifest_category"], "outer_torso")
        with self.assertRaises(character_asset_index.CharacterAssetIndexError):
            character_asset_index.canonical_indexed_override(
                asset, "black", ["black"], "pwa", "feet"
            )

    def test_assignment_rejects_wrong_frame_companion_and_unknown_appearance(self) -> None:
        wrong_frame = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\feet\boots\s1_001_pwa_boots.mesh",
            "base",
        )
        with self.assertRaises(character_asset_index.CharacterAssetIndexError):
            character_asset_index.canonical_indexed_override(wrong_frame, "default", ["default"])

        companion = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\feet\boots\s1_001_pma_boots_cuff.mesh",
            "base",
        )
        with self.assertRaises(character_asset_index.CharacterAssetIndexError):
            character_asset_index.canonical_indexed_override(companion, "default", ["default"])

        primary = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\feet\boots\s1_001_pma_boots.mesh",
            "base",
        )
        with self.assertRaises(character_asset_index.CharacterAssetIndexError):
            character_asset_index.canonical_indexed_override(primary, "invented", ["default"])

    def test_assignment_uses_filename_frame_not_parent_folder_token(self) -> None:
        asset = character_asset_index.classify_asset(
            r"base\characters\garment\player_equipment\torso\t0_005_pma_body__t_bug\t0_005_pwa_body__t_bug.mesh",
            "base",
        )

        self.assertEqual(asset["frame_tokens"], ["pwa"])
        self.assertEqual(asset["path_frame_tokens"], ["pma", "pwa"])
        self.assertFalse(character_asset_index.selection_support(asset)["supported"])

    def test_preview_cache_id_is_case_and_separator_stable(self) -> None:
        self.assertEqual(
            character_asset_index.preview_cache_id(r"BASE/Characters/Test.mesh"),
            character_asset_index.preview_cache_id(r"base\characters\test.mesh"),
        )

    def test_mesh_preview_cache_changes_with_archive_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "appearance.archive"
            wolvenkit = root / "WolvenKit.CLI.exe"
            game = root / "game"
            executable = game / "bin/x64/Cyberpunk2077.exe"
            executable.parent.mkdir(parents=True)
            archive.write_bytes(b"one")
            wolvenkit.write_bytes(b"tool")
            executable.write_bytes(b"game")
            first = character_asset_index.mesh_preview_cache_key(
                r"base\characters\test.mesh", archive, wolvenkit, game
            )
            archive.write_bytes(b"a changed archive")
            second = character_asset_index.mesh_preview_cache_key(
                r"base\characters\test.mesh", archive, wolvenkit, game
            )

        self.assertNotEqual(first, second)

    def test_failed_preview_refresh_cannot_promote_stale_cache_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / "appearance.archive"
            wolvenkit = root / "WolvenKit.CLI.exe"
            game = root / "game"
            executable = game / "bin/x64/Cyberpunk2077.exe"
            executable.parent.mkdir(parents=True)
            archive.write_bytes(b"archive")
            wolvenkit.write_bytes(b"tool")
            executable.write_bytes(b"game")

            depot_path = (
                r"base\characters\garment\player_equipment\feet\boots\s1_test_pma.mesh"
            )
            asset = character_asset_index.classify_asset(depot_path, "base")
            index = {
                "sources": [{"id": "base", "path": str(archive)}],
                "assets": [asset],
            }
            output = root / "preview"
            relative = Path(*depot_path.split("\\"))
            old_glb = (output / "raw" / relative).with_suffix(".glb")
            old_cooked = output / "dependencies" / relative
            old_metadata = output / "metadata" / f"{relative.name}.json"
            old_glb.parent.mkdir(parents=True)
            old_cooked.parent.mkdir(parents=True)
            old_glb.write_bytes(b"old-glb")
            old_cooked.write_bytes(b"old-mesh")
            character_asset_index.write_json(
                old_metadata,
                {
                    "Header": {"DataType": "CR2W"},
                    "Data": {
                        "RootChunk": {
                            "appearances": [
                                {
                                    "Data": {
                                        "$type": "meshMeshAppearance",
                                        "name": {"$value": "stale"},
                                        "chunkMaterials": [],
                                    }
                                }
                            ]
                        }
                    },
                },
            )
            manifest_path = output / "preview-manifest.json"
            character_asset_index.write_json(manifest_path, {"cache_key": "old-cache-key"})
            failed = mock.Mock(returncode=1, stdout="", stderr="refresh failed")
            misleading_success = mock.Mock(returncode=0, stdout="", stderr="")

            with mock.patch.object(
                character_asset_index.subprocess,
                "run",
                side_effect=[failed, misleading_success],
            ) as run:
                with self.assertRaises(character_asset_index.CharacterAssetIndexError):
                    character_asset_index.prepare_mesh_preview(
                        index, depot_path, output, wolvenkit, game
                    )

            self.assertEqual(run.call_count, 1)
            self.assertEqual(old_glb.read_bytes(), b"old-glb")
            self.assertEqual(old_cooked.read_bytes(), b"old-mesh")
            self.assertEqual(
                character_asset_index.read_json(manifest_path)["cache_key"], "old-cache-key"
            )


if __name__ == "__main__":
    unittest.main()
