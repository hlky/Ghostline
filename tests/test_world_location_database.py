from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import world_location_database as locations  # noqa: E402
from world_location_dependencies import (  # noqa: E402
    DependencyClosure,
    DependencyResource,
    StateDependencyClosure,
)


def sector_document() -> dict:
    return {
        "Data": {
            "RootChunk": {
                "$type": "worldStreamingSector",
                "nodes": [
                    {
                        "Data": {
                            "$type": "worldStaticMeshNode",
                            "debugName": {"$value": "wall"},
                            "mesh": {"DepotPath": {"$value": "base/world/wall.mesh"}},
                            "meshAppearance": {"$value": "concrete"},
                        }
                    },
                    {
                        "Data": {
                            "$type": "worldEntityNode",
                            "debugName": {"$value": "door"},
                            "entityTemplate": {
                                "DepotPath": {"$value": "base/world/door.ent"}
                            },
                        }
                    },
                ],
                "nodeData": {
                    "Data": [
                        {
                            "NodeIndex": 0,
                            "Position": {"X": 1, "Y": 2, "Z": 3},
                        },
                        {
                            "NodeIndex": 0,
                            "Position": {"X": 4, "Y": 5, "Z": 6},
                        },
                        {
                            "NodeIndex": 1,
                            "Position": {"X": 7, "Y": 8, "Z": 9},
                        },
                    ]
                },
            }
        }
    }


class LocationSpecTests(unittest.TestCase):
    def test_tile_and_state_ids_cannot_escape_output_roots(self) -> None:
        spec = json.loads(locations.DEFAULT_SPEC.read_text(encoding="utf-8"))
        spec["tiles"][0]["id"] = "../escape"
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "unsafe.json"
            path.write_text(json.dumps(spec), encoding="utf-8")
            with self.assertRaisesRegex(locations.LocationDatabaseError, "tile id"):
                locations.load_tile_states(path)

        spec = json.loads(locations.DEFAULT_SPEC.read_text(encoding="utf-8"))
        spec["tiles"][0]["states"][0]["id"] = r"c:\escape"
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "unsafe.json"
            path.write_text(json.dumps(spec), encoding="utf-8")
            with self.assertRaisesRegex(locations.LocationDatabaseError, "state id"):
                locations.load_tile_states(path)

    def test_depot_paths_reject_absolute_parent_and_drive_segments(self) -> None:
        for value in (r"..\escape.mesh", r"C:\escape.mesh", r"base\bad:part.mesh"):
            with self.subTest(value=value):
                with self.assertRaises(locations.LocationDatabaseError):
                    locations.depot_relative_path(value)

        self.assertEqual(
            Path("base") / "world" / "wall.mesh",
            locations.depot_relative_path(r"Base\World\Wall.mesh"),
        )

    def test_render_forwards_material_override_without_mutating_source_jobs(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            blender = output / "blender.exe"
            blender.write_bytes(b"fixture")
            database = output / "locations.sqlite3"
            database.write_bytes(b"fixture")
            jobs_path = output / "jobs.json"
            payload = {
                "schema_version": 1,
                "defaults": {"with_materials": True},
                "jobs": [{"tile_id": "tile-a", "with_materials": True}],
            }
            jobs_path.write_text(json.dumps(payload), encoding="utf-8")
            (output / "six-tile-render-report.json").write_text(
                json.dumps({"tiles": []}), encoding="utf-8"
            )
            process = mock.Mock(stdout=[])

            def finish_render() -> int:
                (output / "six-tile-render-report.json").write_text(
                    json.dumps({"tiles": []}), encoding="utf-8"
                )
                return 0

            process.wait.side_effect = finish_render
            with (
                mock.patch.object(
                    locations.subprocess, "Popen", return_value=process
                ) as popen,
                mock.patch.object(
                    locations, "ingest_render_report", return_value={"images": 0}
                ),
                mock.patch.object(
                    locations, "write_poc_report", return_value={"checks": []}
                ),
            ):
                locations.render_poc(
                    output_root=output,
                    blender=blender,
                    jobs_path=jobs_path,
                    selected_tiles={"tile-a"},
                    with_materials=False,
                )

            command = popen.call_args.args[0]
            self.assertIn("--without-materials", command)
            self.assertNotIn("--with-materials", command)
            self.assertEqual(payload, json.loads(jobs_path.read_text(encoding="utf-8")))

    def test_render_and_poc_material_flags_default_to_job_configuration(self) -> None:
        parser = locations.create_parser()

        self.assertIsNone(parser.parse_args(["render"]).with_materials)
        self.assertFalse(
            parser.parse_args(["render", "--without-materials"]).with_materials
        )
        self.assertTrue(parser.parse_args(["poc", "--with-materials"]).with_materials)

    def test_material_flags_are_mutually_exclusive(self) -> None:
        parser = locations.create_parser()

        with self.assertRaises(SystemExit):
            parser.parse_args(["render", "--with-materials", "--without-materials"])

    def test_checked_in_contract_has_six_tiles_and_variant_state(self) -> None:
        _spec, states = locations.load_tile_states(locations.DEFAULT_SPEC)

        self.assertEqual(6, len({state.tile_id for state in states}))
        self.assertEqual(7, len(states))
        afterlife = [state for state in states if state.tile_id.startswith("afterlife")]
        self.assertEqual(
            {"open-world", "q005-heist"}, {state.state_id for state in afterlife}
        )
        self.assertTrue(all(128 <= state.size <= 256 for state in states))

    def test_resource_scan_counts_instances_and_placements(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "tile.streamingsector.json"
            path.write_text(json.dumps(sector_document()), encoding="utf-8")
            scan = locations.scan_sector_resources([path])
            placements = locations.staged_placements([path])

        resources = {row["depot_path"]: row for row in scan["resources"]}
        self.assertEqual(2, resources[r"base\world\wall.mesh"]["instance_count"])
        self.assertEqual(
            ["concrete"], resources[r"base\world\wall.mesh"]["appearances"]
        )
        self.assertEqual(1, resources[r"base\world\door.ent"]["instance_count"])
        self.assertEqual(3, len(placements))
        self.assertEqual("wall", placements[0]["debug_name"])

    def test_embedded_foliage_is_materialized_as_blender_compatible_json(
        self,
    ) -> None:
        document = {
            "Data": {
                "EmbeddedFiles": [
                    {
                        "FileName": {"$value": r"base\worlds\generated\tile.cfoliage"},
                        "Content": {
                            "$type": "worldFoliageCompiledResource",
                            "populationCount": 3,
                        },
                    },
                    {
                        "FileName": {"$value": r"base\worlds\generated\skip.mesh"},
                        "Content": {"$type": "CMesh"},
                    },
                ]
            }
        }

        resources = list(locations.embedded_render_documents(document))

        self.assertEqual(1, len(resources))
        depot_path, resource = resources[0]
        self.assertEqual(r"base\worlds\generated\tile.cfoliage", depot_path)
        self.assertEqual(
            "worldFoliageCompiledResource",
            resource["Data"]["RootChunk"]["$type"],
        )
        self.assertIn("8.17", resource["Header"]["WolvenKitVersion"])

    def test_dependency_resources_extend_the_render_content_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "tile.streamingsector.json"
            path.write_text(json.dumps(sector_document()), encoding="utf-8")
            scan = locations.scan_sector_resources([path])
            extended = locations.augment_resource_scan(
                scan,
                [
                    {
                        "resource": r"base\world\door.app",
                        "resource_type": "app",
                    },
                    {
                        "resource": r"base\world\door_handle.mesh",
                        "resource_type": "mesh",
                    },
                ],
            )
            _spec, states = locations.load_tile_states(locations.DEFAULT_SPEC)
            job = locations.state_job(
                states[0],
                {
                    "project_root": Path(temporary) / "project",
                    "content_fingerprint": "fixture-content",
                    "sector_rows": [],
                    "places": [],
                    "resource_scan": extended,
                    "direct_resource_summary": scan["summary"],
                },
                Path(temporary) / "output",
            )

        self.assertEqual(4, extended["summary"]["resources"])
        self.assertEqual(2, extended["summary"]["meshes"])
        self.assertEqual(1, extended["summary"]["entities"])
        self.assertEqual(1, extended["summary"]["appearances"])
        self.assertEqual(2, extended["summary"]["node_definitions"])
        self.assertEqual(1, job["expected_content"]["entity_jsons"])
        self.assertEqual(1, job["expected_content"]["appearance_jsons"])
        self.assertEqual(1, job["expected_content"]["imported_mesh_glbs"])

    def test_runtime_community_spawners_are_metadata_not_render_dependencies(
        self,
    ) -> None:
        self.assertFalse(
            locations.requires_render_dependency(
                {
                    "resource_type": "ent",
                    "depot_path": (
                        r"base\quest\sq004\characters\communities"
                        r"\raffen_drone_spawner.ent"
                    ),
                }
            )
        )
        self.assertTrue(
            locations.requires_render_dependency(
                {
                    "resource_type": "ent",
                    "depot_path": r"base\gameplay\devices\computers\laptop.ent",
                }
            )
        )


class LocationDatabaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.database = self.root / "locations.sqlite3"
        self.spec, self.states = locations.load_tile_states(locations.DEFAULT_SPEC)
        self.state = self.states[0]
        connection = locations.connect(self.database)
        locations.create_schema(connection)
        locations.begin_run(
            connection,
            locations.DEFAULT_SPEC,
            self.spec,
            [self.state],
            {"block_identity": {"test": True}, "sectors_root": "fixture"},
        )
        project = self.root / "project"
        manifest = self.root / "assembly.json"
        manifest.write_text("{}", encoding="utf-8")
        context = {
            "project_root": project,
            "manifest_path": manifest,
            "content_fingerprint": "assembly-1",
            "status": "prepared",
            "error": "",
            "sector_rows": [
                {
                    "depot_path": "base/world/tile.streamingsector",
                    "category": "exterior",
                    "level": 0,
                    "source_sector_path": "source.json",
                    "staged_path": "staged.json",
                    "active_variants": [],
                    "source_instance_count": 3,
                    "retained_instance_count": 2,
                    "retained_node_count": 1,
                }
            ],
            "resource_scan": {
                "resources": [
                    {
                        "depot_path": "base/world/wall.mesh",
                        "resource_type": "mesh",
                        "node_types": ["worldStaticMeshNode"],
                        "instance_count": 2,
                    },
                    {
                        "depot_path": "base/world/door.ent",
                        "resource_type": "ent",
                        "node_types": ["worldEntityNode"],
                        "instance_count": 1,
                    },
                ]
            },
            "asset_report": {"assets": [], "failed": []},
            "asset_status": "not_requested",
            "islands": [
                {
                    "island_id": "island-1",
                    "agent_type": "Human",
                    "source_sector": "navigation.navmesh",
                    "polygon_count": 4,
                    "walkable_area": 100.0,
                    "bounds": {"min": {"x": 0}, "max": {"x": 10}},
                    "level_key": "1",
                }
            ],
            "places": [
                {
                    "place_id": "place-1",
                    "island_id": "island-1",
                    "x": self.state.anchor[0],
                    "y": self.state.anchor[1],
                    "z": self.state.anchor[2],
                    "yaw_degrees": 90.0,
                    "interior": False,
                    "source": "navigation",
                    "status": "candidate",
                    "structural": {"enclosure": "alley"},
                    "nearby_resources": ["base/world/wall.mesh"],
                }
            ],
            "metrics": {
                "stage_seconds": {"value": 1.25, "unit": "seconds"},
                "render_directions_per_place": {
                    "value": 1,
                    "unit": "directions",
                },
            },
        }
        locations.store_state_context(connection, self.state, context)
        connection.close()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_search_and_vlm_export_use_place_level_records(self) -> None:
        connection = locations.connect(self.database)
        rows = locations.location_rows(connection, "alley")
        summary = locations.database_summary(connection)
        connection.close()
        jobs = locations.vlm_jobs(
            self.database, self.root / "jobs.jsonl", include_unrendered=True
        )

        self.assertEqual("place-1", rows[0]["place_id"])
        self.assertEqual(1, summary["places"])
        self.assertEqual(1, jobs["jobs"])
        job = json.loads((self.root / "jobs.jsonl").read_text(encoding="utf-8"))
        self.assertIn("combat_suitability", job["caption_schema"])

    def test_renderer_report_updates_images_metrics_and_structural_facts(self) -> None:
        image = self.root / "view.webp"
        image.write_bytes(b"RIFFfixture")
        tile_report = self.root / "tile-report.json"
        tile_report.write_text(
            json.dumps(
                {
                    "tile_id": self.state.key,
                    "status": "completed",
                    "content_fingerprint": "assembly-1",
                    "renderer": {
                        "renderer_fingerprint": "renderer-1",
                        "resolution": 768,
                    },
                    "timings": {"import_seconds": 2.0, "total_seconds": 3.0},
                    "view_summary": {"valid_views": 1, "invalid_views": 0},
                    "views": [
                        {
                            "viewpoint_id": "place-1",
                            "yaw_degrees": 90.0,
                            "valid": True,
                            "output": str(image),
                            "image": {
                                "path": str(image),
                                "sha256": locations.sha256_file(image),
                            },
                            "position_validation": {
                                "valid": True,
                                "estimated_ceiling_height": 3.2,
                                "horizontal_openness": {
                                    "mean": 3.0,
                                    "minimum": 1.0,
                                    "maximum": 7.0,
                                },
                            },
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        batch_report = self.root / "batch.json"
        batch_report.write_text(
            json.dumps(
                {"tiles": [{"tile_id": self.state.key, "report": str(tile_report)}]}
            ),
            encoding="utf-8",
        )

        result = locations.ingest_render_report(self.database, batch_report)
        connection = locations.connect(self.database)
        place = connection.execute(
            "SELECT status, structural_json FROM places WHERE place_id='place-1'"
        ).fetchone()
        image_row = connection.execute("SELECT * FROM images").fetchone()
        connection.close()

        self.assertEqual(1, result["images"])
        self.assertEqual("rendered", place["status"])
        self.assertEqual("enclosed", json.loads(place["structural_json"])["enclosure"])
        self.assertEqual("complete", image_row["status"])

    def test_renderer_report_rejects_stale_assembly_fingerprint(self) -> None:
        tile_report = self.root / "stale-tile-report.json"
        tile_report.write_text(
            json.dumps(
                {
                    "tile_id": self.state.key,
                    "status": "completed",
                    "content_fingerprint": "old-assembly",
                    "views": [],
                }
            ),
            encoding="utf-8",
        )
        batch_report = self.root / "stale-batch.json"
        batch_report.write_text(
            json.dumps(
                {"tiles": [{"tile_id": self.state.key, "report": str(tile_report)}]}
            ),
            encoding="utf-8",
        )

        result = locations.ingest_render_report(self.database, batch_report)
        connection = locations.connect(self.database)
        status = connection.execute(
            "SELECT status FROM tile_states WHERE state_key=?", (self.state.key,)
        ).fetchone()[0]
        connection.close()

        self.assertEqual(1, result["stale_reports"])
        self.assertEqual("render_stale", status)

    def test_vlm_import_populates_searchable_tag_fields(self) -> None:
        source = self.root / "vlm-results.jsonl"
        source.write_text(
            json.dumps(
                {
                    "place_id": "place-1",
                    "tags": {
                        "atmosphere": ["oppressive"],
                        "quest_themes": ["infiltration"],
                        "confidence": 0.91,
                    },
                }
            )
            + "\n",
            encoding="utf-8",
        )

        result = locations.import_vlm_tags(self.database, source)
        connection = locations.connect(self.database)
        rows = locations.location_rows(connection, "infiltration")
        connection.close()

        self.assertEqual(1, result["imported"])
        self.assertEqual(["oppressive"], rows[0]["vlm_tags"]["atmosphere"])

    def test_vlm_export_is_not_limited_to_interactive_search_cap(self) -> None:
        connection = locations.connect(self.database)
        connection.executemany(
            """
            INSERT INTO places(
                place_id, state_key, island_id, x, y, z, yaw_degrees, interior,
                source, status, structural_json, nearby_resources_json,
                renderer_fingerprint, vlm_tags_json
            ) VALUES (?, ?, NULL, 0, 0, 0, 0, 0, 'navigation', 'candidate',
                      '{}', '[]', '', '{}')
            """,
            ((f"bulk-place-{index:04d}", self.state.key) for index in range(1001)),
        )
        connection.commit()
        connection.close()

        result = locations.vlm_jobs(
            self.database,
            self.root / "bulk-jobs.jsonl",
            include_unrendered=True,
        )

        self.assertEqual(1002, result["jobs"])

    def test_selective_run_preserves_untouched_state(self) -> None:
        other = self.states[1]
        connection = locations.connect(self.database)
        locations.begin_run(
            connection,
            locations.DEFAULT_SPEC,
            self.spec,
            [self.state, other],
            {"block_identity": {"test": True}, "sectors_root": "fixture"},
            active_state_keys={other.key},
        )
        statuses = {
            row["state_key"]: row["status"]
            for row in connection.execute(
                "SELECT state_key, status FROM tile_states"
            ).fetchall()
        }
        connection.close()

        self.assertEqual("prepared", statuses[self.state.key])
        self.assertEqual("pending", statuses[other.key])

    def test_changed_input_generation_clears_stale_state_owned_rows(self) -> None:
        other = self.states[1]
        connection = locations.connect(self.database)
        previous_run = connection.execute(
            "SELECT value FROM metadata WHERE key='active_run_id'"
        ).fetchone()[0]

        next_run = locations.begin_run(
            connection,
            locations.DEFAULT_SPEC,
            self.spec,
            [self.state, other],
            {"block_identity": {"test": "changed"}, "sectors_root": "fixture"},
            active_state_keys={other.key},
        )
        states = connection.execute(
            "SELECT state_key, run_id, status FROM tile_states ORDER BY state_key"
        ).fetchall()
        place_count = connection.execute("SELECT COUNT(*) FROM places").fetchone()[0]
        connection.close()

        self.assertNotEqual(previous_run, next_run)
        self.assertEqual(0, place_count)
        self.assertEqual(
            {self.state.key, other.key}, {row["state_key"] for row in states}
        )
        self.assertTrue(all(row["run_id"] == next_run for row in states))
        self.assertTrue(all(row["status"] == "pending" for row in states))

    def test_install_file_replaces_same_size_changed_derived_asset(self) -> None:
        source = self.root / "source.glb"
        target = self.root / "staged.glb"
        source.write_bytes(b"new!")
        target.write_bytes(b"old!")

        action = locations.install_file(source, target)

        self.assertEqual("replaced", action)
        self.assertEqual(b"new!", target.read_bytes())

    def test_geometry_asset_installs_when_material_sidecar_is_unavailable(self) -> None:
        source_glb = self.root / "cache/asset.glb"
        source_glb.parent.mkdir(parents=True)
        source_glb.write_bytes(b"glTFfixture")
        project_raw = self.root / "tile/source/raw"
        stale_sidecar = project_raw / "base/world/wall.Material.json"
        stale_sidecar.parent.mkdir(parents=True)
        stale_sidecar.write_text("stale", encoding="utf-8")
        scan = {
            "resources": [
                {
                    "depot_path": r"base\world\wall.mesh",
                    "resource_type": "mesh",
                }
            ]
        }
        union = {
            "assets": [
                {
                    "depot_path": r"base\world\wall.mesh",
                    "fingerprint": "mesh-fingerprint",
                    "glb": str(source_glb),
                    "material_json": "",
                    "material_error": "malformed material fixture",
                }
            ],
            "failed": [],
        }

        report = locations.install_exported_assets(scan, union, project_raw)

        self.assertTrue((project_raw / "base/world/wall.glb").is_file())
        self.assertFalse(stale_sidecar.exists())
        self.assertEqual([], report["failed"])
        self.assertEqual(1, len(report["material_warnings"]))
        self.assertEqual("not_available", report["assets"][0]["install_actions"][1])

    def test_metadata_report_does_not_claim_mesh_exports_succeeded(self) -> None:
        report = locations.write_poc_report(self.database, self.root / "report.json")

        self.assertFalse(report["checks"]["all_mesh_exports_succeeded"])
        self.assertFalse(report["checks"]["all_entity_dependencies_staged"])

    def test_state_dependency_staging_installs_ready_json_and_prunes_stale(
        self,
    ) -> None:
        cached = self.root / "cache/entity.json"
        cached.parent.mkdir(parents=True)
        cached.write_text(
            '{"Data": {"RootChunk": {"$type": "entEntityTemplate"}}}',
            encoding="utf-8",
        )
        entity = r"base\world\door.ent"
        resource = DependencyResource(
            resource=entity,
            extension=".ent",
            kind="entity",
            serializable=True,
            status="ready",
            dependencies=(),
            cache_fingerprint="entity-fingerprint",
            json_path=cached,
        )
        closure = DependencyClosure(
            roots=(entity,),
            resources=(resource,),
            batches=(),
            identity_fingerprint="closure-fingerprint",
        )
        state_dependencies = StateDependencyClosure(
            closure=closure,
            state_resources={self.state.key: (entity,)},
        )
        project_raw = self.root / "dependency-project/source/raw"
        stale = project_raw / "base/world/stale.app.json"
        stale.parent.mkdir(parents=True)
        stale.write_text("stale", encoding="utf-8")

        report = locations.stage_state_dependencies(
            state_dependencies, self.state.key, project_raw
        )

        self.assertTrue((project_raw / "base/world/door.ent.json").is_file())
        self.assertFalse(stale.exists())
        self.assertEqual(1, report["summary"]["installed"])
        self.assertEqual(1, report["summary"]["pruned"])


if __name__ == "__main__":
    unittest.main()
