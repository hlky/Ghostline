from __future__ import annotations

import json
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import world_location_render_blender as renderer  # noqa: E402


def actual_content(**overrides: int) -> dict[str, int]:
    result = {
        "staged_sector_jsons": 2,
        "imported_sector_jsons": 2,
        "staged_mesh_glbs": 4,
        "imported_mesh_glbs": 4,
        "staged_entity_jsons": 3,
        "staged_appearance_jsons": 2,
        "staged_node_definitions": 6,
        "imported_node_definitions": 6,
        "expected_node_instances": 8,
        "imported_node_instances": 8,
        "imported_instance_records": 12,
    }
    result.update(overrides)
    return result


class ExpectedContentTests(unittest.TestCase):
    def test_legacy_expected_key_is_normalised_to_contract(self) -> None:
        self.assertEqual(
            {"sector_jsons": 2, "mesh_glbs": 4, "node_definitions": 6},
            renderer.normalise_expected_content(
                {"sector_count": 2, "mesh_glbs": "4", "node_definitions": 6}
            ),
        )

    def test_negative_expected_count_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "non-negative integer"):
            renderer.normalise_expected_content({"mesh_glbs": -1})

    def test_complete_content_has_no_error_signals(self) -> None:
        result = renderer.evaluate_content_coverage(
            {"sector_jsons": 2, "mesh_glbs": 4, "node_definitions": 6},
            actual_content(),
        )

        self.assertEqual([], result["signals"])
        self.assertEqual(1.0, result["coverage"]["meshes"]["imported"]["ratio"])

    def test_staged_mesh_superset_can_have_a_smaller_import_contract(self) -> None:
        result = renderer.evaluate_content_coverage(
            {
                "mesh_glbs": 8,
                "imported_mesh_glbs": 4,
            },
            actual_content(staged_mesh_glbs=8, imported_mesh_glbs=4),
        )

        self.assertEqual([], result["signals"])
        self.assertEqual(8, result["coverage"]["meshes"]["staged"]["expected"])
        self.assertEqual(4, result["coverage"]["meshes"]["imported"]["expected"])

    def test_each_import_shortfall_is_an_error(self) -> None:
        result = renderer.evaluate_content_coverage(
            {"sector_jsons": 2, "mesh_glbs": 4, "node_definitions": 6},
            actual_content(
                imported_sector_jsons=1,
                imported_mesh_glbs=3,
                imported_node_definitions=5,
                imported_node_instances=7,
            ),
        )

        codes = {
            signal["code"]
            for signal in result["signals"]
            if signal["severity"] == "error"
        }
        self.assertEqual(
            {
                "imported_sector_shortfall",
                "imported_mesh_shortfall",
                "imported_node_definition_shortfall",
                "imported_node_instance_shortfall",
            },
            codes,
        )

    def test_missing_entity_dependency_json_is_an_error(self) -> None:
        result = renderer.evaluate_content_coverage(
            {"entity_jsons": 3, "appearance_jsons": 2},
            actual_content(staged_entity_jsons=2, staged_appearance_jsons=1),
        )

        self.assertEqual(
            {"staged_entity_json_shortfall", "staged_appearance_json_shortfall"},
            {signal["code"] for signal in result["signals"]},
        )

    def test_content_error_makes_valid_render_partial(self) -> None:
        self.assertEqual(("partial", None), renderer.classify_render_status(4, 0, 1))
        self.assertEqual(("completed", None), renderer.classify_render_status(4, 0, 0))
        self.assertEqual("failed", renderer.classify_render_status(0, 4, 0)[0])

    def test_fail_on_invalid_rejects_content_error_without_invalid_camera(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            jobs_path = Path(temporary) / "jobs.json"
            args = Namespace(
                jobs=jobs_path,
                batch_report=Path(temporary) / "report.json",
                fail_fast=False,
                fail_on_invalid=True,
            )
            tile_report = {
                "tile_id": "incomplete-tile",
                "status": "partial",
                "report_path": str(Path(temporary) / "tile-report.json"),
                "output": str(Path(temporary) / "renders"),
                "view_summary": {
                    "valid_views": 4,
                    "invalid_views": 0,
                    "total_views": 4,
                },
                "content": {"severity_counts": {"error": 1, "warning": 0, "info": 0}},
                "timings": {"total_seconds": 0.1},
            }
            with (
                mock.patch.object(
                    renderer, "parse_job_payload", return_value=[{"tile_id": "x"}]
                ),
                mock.patch.object(renderer, "render_tile", return_value=tile_report),
            ):
                batch, should_fail = renderer.run_batch(args)

        self.assertTrue(should_fail)
        self.assertEqual(1, batch["summary"]["content_errors"])


class PreparedProjectTests(unittest.TestCase):
    def test_installed_addon_missing_color_helper_is_patched_once(self) -> None:
        import_common = type("ImportCommon", (), {})()
        colors = object()

        self.assertEqual(
            ["import_common.bcolors"],
            renderer.apply_cp77_addon_compatibility_shims(import_common, colors),
        )
        self.assertIs(colors, import_common.bcolors)
        self.assertEqual(
            [], renderer.apply_cp77_addon_compatibility_shims(import_common, object())
        )

    def test_material_mode_changes_renderer_fingerprint_and_import_cache_key(
        self,
    ) -> None:
        base = {
            "project": "tile.cpmodproj",
            "resolution": 768,
            "image_quality": 90,
        }
        with_materials = renderer.build_renderer_identity(
            {**base, "with_materials": True},
            engine="BLENDER_EEVEE_NEXT",
            image_format="WEBP",
            blender_version="4.5.0",
            addon_version=[1, 6, 2],
        )
        without_materials = renderer.build_renderer_identity(
            {**base, "with_materials": False},
            engine="BLENDER_EEVEE_NEXT",
            image_format="WEBP",
            blender_version="4.5.0",
            addon_version=[1, 6, 2],
        )

        self.assertTrue(with_materials["with_materials"])
        self.assertFalse(without_materials["with_materials"])
        self.assertNotEqual(
            with_materials["renderer_fingerprint"],
            without_materials["renderer_fingerprint"],
        )
        self.assertNotEqual(
            renderer.cache_key_for_job({**base, "with_materials": True}),
            renderer.cache_key_for_job({**base, "with_materials": False}),
        )

    def test_material_cli_override_wins_without_mutating_jobs_document(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            jobs_path = Path(temporary) / "jobs.json"
            payload = {
                "defaults": {"with_materials": True},
                "jobs": [
                    {
                        "tile_id": "test-tile",
                        "project": "staging/test-tile",
                        "output": "renders/test-tile",
                        "with_materials": True,
                        "viewpoints": [{"id": "test", "position": [0, 0, 1.65]}],
                    }
                ],
            }
            jobs_path.write_text(json.dumps(payload), encoding="utf-8")
            cli = Namespace(
                resolution=None,
                image_format=None,
                image_quality=None,
                horizontal_fov_degrees=None,
                with_materials=False,
                with_static_lights=None,
            )

            jobs = renderer.parse_job_payload(jobs_path, cli)

            self.assertFalse(jobs[0]["with_materials"])
            self.assertEqual(payload, json.loads(jobs_path.read_text(encoding="utf-8")))

    def test_material_cli_flags_are_mutually_exclusive(self) -> None:
        with mock.patch.object(
            sys,
            "argv",
            [
                "blender",
                "--",
                "--jobs",
                "jobs.json",
                "--with-materials",
                "--without-materials",
            ],
        ):
            with self.assertRaises(SystemExit):
                renderer.parse_args()

    def test_scan_counts_sector_definitions_and_instances(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "tile"
            raw = project / "source" / "raw"
            raw.mkdir(parents=True)
            (raw / "tile.streamingsector.json").write_text(
                json.dumps(
                    {
                        "Data": {
                            "RootChunk": {
                                "nodes": [{}, {}],
                                "nodeData": {
                                    "Data": [
                                        {"NodeIndex": 0},
                                        {"NodeIndex": 1},
                                        {"NodeIndex": 1},
                                    ]
                                },
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            (raw / "wall.glb").write_bytes(b"glTF")

            result = renderer.scan_prepared_project(project)

        self.assertEqual(1, result["counts"]["streamingsector_json"])
        self.assertEqual(1, result["counts"]["glb"])
        self.assertEqual(2, result["counts"]["node_definitions"])
        self.assertEqual(3, result["counts"]["node_instances"])
        self.assertEqual([], result["sector_scan_errors"])

    def test_parse_job_prefers_expected_content_over_legacy_expected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            jobs_path = Path(temporary) / "jobs.json"
            jobs_path.write_text(
                json.dumps(
                    {
                        "jobs": [
                            {
                                "tile_id": "test-tile",
                                "project": "staging/test-tile",
                                "output": "renders/test-tile",
                                "expected": {"sector_count": 99},
                                "expected_content": {
                                    "sector_jsons": 1,
                                    "mesh_glbs": 2,
                                    "node_definitions": 3,
                                },
                                "viewpoints": [
                                    {"id": "test", "position": [0, 0, 1.65]}
                                ],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            cli = Namespace(
                resolution=None,
                image_format=None,
                image_quality=None,
                horizontal_fov_degrees=None,
                with_static_lights=None,
            )

            jobs = renderer.parse_job_payload(jobs_path, cli)

        self.assertEqual(
            {"sector_jsons": 1, "mesh_glbs": 2, "node_definitions": 3},
            jobs[0]["expected_content"],
        )


if __name__ == "__main__":
    unittest.main()
