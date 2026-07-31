from __future__ import annotations

import base64
import json
import hashlib
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import threading
import time
import struct
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from world_locations.capture import (  # noqa: E402
    CaptureController,
    SessionProtocolError,
    _nearest_runtime_area,
    recover_interrupted_queue,
    validate_image,
    validate_ready_event,
)
from world_locations.config import load_config  # noqa: E402
from world_locations import database as database_module  # noqa: E402
from world_locations.database import connect, transaction  # noqa: E402
from world_locations.extract import extract_sector, index_sectors  # noqa: E402
from world_locations.model import Quaternion, Vec3, game_yaw_degrees, outward_vector  # noqa: E402
from world_locations.planning import (  # noqa: E402
    _deduplicate_candidate_coordinates,
    _deduplicate_physical_locations,
    _deduplicate_sparse_road_places,
    evaluate_scope,
    plan_locations,
    resolve_metadata,
    sample_road_points,
)
from world_locations.protocol import (  # noqa: E402
    ProtocolError,
    RuntimeProtocol,
    RuntimeTimeout,
    _unlink_protocol_file,
    atomic_write_json,
)


def sector_document() -> dict:
    nodes = [
        {
            "Data": {
                "$type": "worldEntityNode",
                "debugName": {"$type": "CName", "$value": "vending"},
                "entityTemplate": {
                    "DepotPath": {
                        "$type": "ResourcePath",
                        "$value": r"base\gameplay\devices\vending_machines\vending_machine_1.ent",
                    }
                },
                "appearanceName": {"$value": "vending_test"},
            }
        },
        {
            "Data": {
                "$type": "worldEntityNode",
                "entityTemplate": {
                    "DepotPath": {
                        "$value": r"base\gameplay\devices\fast_travel\gate.ent"
                    }
                },
                "point": {
                    "$type": "gameFastTravelPointData",
                    "markerRef": {"$value": "Kabuki Market"},
                    "pointRecord": "FastTravelPoints.kabuki_market",
                },
            }
        },
    ]
    for index in range(3):
        nodes.append(
            {
                "Data": {
                    "$type": "worldRoadProxyMeshNode",
                    "mesh": {
                        "DepotPath": {
                            "$value": rf"base\worlds\03_night_city\sectors\_external\road_meshes\r_roadsplinenode_test\prx{index}.mesh"
                        }
                    },
                }
            }
        )
    nodes.append(
        {
            "Data": {
                "$type": "worldGenericAreaShapeNode",
                "debugName": {"$value": "named_area_kabuki"},
            }
        }
    )
    node_data = [
        {
            "NodeIndex": 0,
            "Id": "vending-1",
            "Position": {"X": 0, "Y": 0, "Z": 0},
            "Orientation": {"i": 0, "j": 0, "k": 0, "r": 1},
            "Bounds": {
                "Min": {"X": -0.5, "Y": -0.5, "Z": 0},
                "Max": {"X": 0.5, "Y": 0.5, "Z": 2},
            },
        },
        {
            "NodeIndex": 1,
            "Position": {"X": 50, "Y": 0, "Z": 0},
            "Orientation": {"i": 0, "j": 0, "k": 0, "r": 1},
        },
    ]
    node_data.extend(
        {
            "NodeIndex": index + 2,
            "Position": {"X": index * 100, "Y": 10, "Z": 0},
            "Orientation": {"i": 0, "j": 0, "k": 0, "r": 1},
        }
        for index in range(3)
    )
    node_data.append(
        {
            "NodeIndex": 5,
            "Position": {"X": 0, "Y": 0, "Z": 0},
            "Orientation": {"i": 0, "j": 0, "k": 0, "r": 1},
            "Bounds": {
                "Min": {"X": -1000, "Y": -1000, "Z": -100},
                "Max": {"X": 1000, "Y": 1000, "Z": 100},
            },
        }
    )
    return {"Data": {"RootChunk": {"nodes": nodes, "nodeData": {"Data": node_data}}}}


class GeometryTests(unittest.TestCase):
    def test_identity_rotation_faces_positive_y_and_uses_game_yaw_zero(self) -> None:
        forward = outward_vector(Quaternion(), "+y")
        self.assertAlmostEqual(0.0, forward.x)
        self.assertAlmostEqual(1.0, forward.y)
        self.assertAlmostEqual(0.0, game_yaw_degrees(forward))

    def test_metadata_precedence_is_runtime_then_spatial_then_override(self) -> None:
        resolved, provenance = resolve_metadata(
            {"district": "runtime-district"},
            {"district": "spatial-district", "street": "spatial-street"},
            {
                "district": "override-district",
                "street": "override-street",
                "area": "override-area",
            },
        )
        self.assertEqual("runtime-district", resolved["district"])
        self.assertEqual("spatial-street", resolved["street"])
        self.assertEqual("override-area", resolved["area"])
        self.assertEqual("runtime", provenance["district"])

    def test_road_samples_enforce_arc_and_straight_line_separation(self) -> None:
        points = [Vec3(0, 0, 0), Vec3(100, 0, 0), Vec3(200, 0, 0), Vec3(300, 0, 0)]
        samples = sample_road_points(
            points,
            {
                "short_road_threshold_m": 100,
                "endpoint_inset_m": 50,
                "interval_m": 100,
                "minimum_arc_separation_m": 100,
                "minimum_straight_separation_m": 100,
            },
        )
        self.assertEqual([50.0, 150.0, 250.0], [sample[0] for sample in samples])
        for left_index, left in enumerate(samples):
            for right in samples[left_index + 1 :]:
                self.assertGreaterEqual(right[0] - left[0], 100.0)
                self.assertGreaterEqual(left[1].distance_2d(right[1]), 100.0)

        # The third point is 100 m along the centerline from the second but
        # loops back to within 80 m of the first, so it must be excluded.
        looping = sample_road_points(
            [
                Vec3(-50, 0, 0),
                Vec3(0, 0, 0),
                Vec3(100, 0, 0),
                Vec3(32, 73.321211, 0),
                Vec3(-36, 146.642422, 0),
            ],
            {
                "short_road_threshold_m": 100,
                "endpoint_inset_m": 50,
                "interval_m": 100,
                "minimum_arc_separation_m": 100,
                "minimum_straight_separation_m": 100,
            },
        )
        self.assertEqual([50.0, 150.0], [sample[0] for sample in looping])

    def test_q000_border_rule_separates_outside_from_night_city(self) -> None:
        config = load_config()
        outside = evaluate_scope(
            Vec3(-2845.607666015625, -5675.216796875, 100.12057495117188),
            config,
        )
        inside = evaluate_scope(
            Vec3(-2799.475830078125, -5589.72705078125, 87.41756439208984),
            config,
        )
        boundary = evaluate_scope(
            Vec3(-2818.559814453125, -5650.1533203125, 102.40483093261719),
            config,
        )
        self.assertEqual("out_of_scope", outside["scope_status"])
        self.assertEqual("in_scope", inside["scope_status"])
        self.assertEqual("in_scope", boundary["scope_status"])
        self.assertEqual(
            "q000_nomad_southern_border_wall_v1", outside["scope_rule_id"]
        )


class IndexAndPlanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.source = self.root / "sectors"
        self.source.mkdir()
        self.sector = self.source / "fixture.streamingsector.json"
        self.sector.write_text(json.dumps(sector_document()), encoding="utf-8")
        self.config = load_config()
        self.connection = connect(self.root / "locations.sqlite3")

    def tearDown(self) -> None:
        self.connection.close()
        self.temporary.cleanup()

    def test_candidate_deduplication_uses_configured_3d_spacing(self) -> None:
        def candidate(
            location_id: str, category: str, x: float, y: float, z: float
        ) -> dict[str, object]:
            return {
                "location_id": location_id,
                "category": category,
                "requested_x": x,
                "requested_y": y,
                "requested_z": z,
            }

        retained, removed = _deduplicate_candidate_coordinates(
            [
                candidate("a", "vending_machine", 0.0, 0.0, 0.0),
                candidate("b", "vending_machine", 2.9, 0.0, 0.0),
                candidate("c", "vending_machine", 3.1, 0.0, 0.0),
                candidate("d", "vending_machine", 0.0, 0.0, 4.0),
                candidate("e", "shop", 0.0, 0.0, 0.0),
            ],
            {"vending_machine": 3.0},
        )

        self.assertEqual(1, removed)
        self.assertEqual(["a", "c", "d", "e"], [row["location_id"] for row in retained])

    def test_global_spacing_prefers_useful_anchors_and_preserves_road_views(self) -> None:
        def candidate(
            location_id: str,
            category: str,
            x: float,
            y: float,
            z: float,
            *,
            direction: str = "outward",
            anchor: str | None = None,
            road_id: str | None = None,
        ) -> dict[str, object]:
            return {
                "location_id": location_id,
                "category": category,
                "requested_x": x,
                "requested_y": y,
                "requested_z": z,
                "direction": direction,
                "anchor_feature_id": anchor,
                "road_id": road_id,
                "scope_status": "in_scope",
            }

        retained, removed = _deduplicate_physical_locations(
            [
                candidate("vending", "vending_machine", 0.0, 0.0, 0.0, anchor="v"),
                candidate("terminal", "terminal", 5.0, 0.0, 0.0, anchor="t"),
                candidate(
                    "road-along", "road", 20.0, 0.0, 0.0,
                    direction="along", road_id="road-a"
                ),
                candidate(
                    "road-against", "road", 20.0, 0.0, 0.0,
                    direction="against", road_id="road-a"
                ),
                candidate(
                    "road-other", "road", 20.0, 0.0, 0.0,
                    direction="along", road_id="road-b"
                ),
                candidate("parking", "parking_space", 30.0, 0.0, 0.0, anchor="p"),
                candidate("upper-floor", "loot_container", 30.0, 0.0, 10.0, anchor="l"),
            ],
            10.0,
            ["terminal", "parking_space", "loot_container", "vending_machine", "road"],
        )

        self.assertEqual(2, removed)
        self.assertEqual(
            ["parking", "road-against", "road-along", "terminal", "upper-floor"],
            [row["location_id"] for row in retained],
        )

    def test_nearest_runtime_area_is_bounded_and_requires_runtime_provenance(self) -> None:
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        place = self.connection.execute(
            "SELECT * FROM places WHERE category='vending_machine'"
        ).fetchone()
        provenance = json.loads(place["provenance_json"])
        provenance["named_area"] = "runtime"
        with transaction(self.connection):
            self.connection.execute(
                "UPDATE places SET named_area='Test Area',provenance_json=? WHERE location_id=?",
                (json.dumps(provenance), place["location_id"]),
            )

        nearby = _nearest_runtime_area(
            self.connection, place["requested_x"] + 10.0, place["requested_y"], 50.0
        )
        distant = _nearest_runtime_area(
            self.connection, place["requested_x"] + 100.0, place["requested_y"], 50.0
        )

        self.assertEqual("Test Area", nearby["named_area"])
        self.assertEqual({}, distant)

    def test_sparse_roads_are_globally_spaced_away_from_objects(self) -> None:
        def road(location_id: str, x: float, direction: str) -> dict[str, object]:
            return {
                "location_id": location_id,
                "requested_x": x,
                "requested_y": 0.0,
                "requested_z": 0.0,
                "direction": direction,
            }

        roads = [
            road("a1", 0.0, "along"),
            road("a2", 0.0, "against"),
            road("b1", 300.0, "along"),
            road("b2", 300.0, "against"),
            road("c1", 400.0, "along"),
            road("c2", 400.0, "against"),
            road("d1", 600.0, "along"),
            road("d2", 600.0, "against"),
        ]
        objects = [
            {
                "requested_x": 300.0,
                "requested_y": 0.0,
                "requested_z": 0.0,
            }
        ]

        retained, removed = _deduplicate_sparse_road_places(
            roads,
            objects,
            {"object_proximity_m": 50.0, "minimum_separation_m": 500.0},
        )

        self.assertEqual(2, removed)
        self.assertEqual(
            ["a1", "a2", "b1", "b2", "d1", "d2"],
            [row["location_id"] for row in retained],
        )

    def test_streamed_extraction_is_stable_and_classifies_known_features(self) -> None:
        first = extract_sector(self.sector, self.sector.name, self.config)
        second = extract_sector(self.sector, self.sector.name, self.config)
        self.assertEqual(
            [row["feature_id"] for row in first], [row["feature_id"] for row in second]
        )
        self.assertEqual(
            {"vending_machine", "fast_travel", "road", "area"},
            {row["category"] for row in first},
        )
        vending = next(row for row in first if row["category"] == "vending_machine")
        self.assertEqual(
            r"base\gameplay\devices\vending_machines\vending_machine_1.ent",
            vending["resource_path"],
        )

    def test_extended_anchor_rules_use_precise_resources_and_node_types(self) -> None:
        document = {"Data": {"RootChunk": {"nodes": [], "nodeData": {"Data": []}}}}
        root = document["Data"]["RootChunk"]

        def add_node(
            node_type: str,
            *,
            resource: str | None = None,
            debug_name: str | None = None,
        ) -> None:
            index = len(root["nodes"])
            data: dict[str, object] = {"$type": node_type}
            if resource:
                data["entityTemplate"] = {"DepotPath": {"$value": resource}}
            if debug_name:
                data["debugName"] = {"$value": debug_name}
            root["nodes"].append({"Data": data})
            root["nodeData"]["Data"].append(
                {
                    "NodeIndex": index,
                    "Id": f"fixture-{index}",
                    "Position": {"X": index * 20, "Y": 0, "Z": 0},
                    "Orientation": {"i": 0, "j": 0, "k": 0, "r": 1},
                }
            )

        add_node("worldAISpotNode", debug_name="sit_bar")
        add_node("worldCrowdParkingSpaceNode", debug_name="parkingSpace_001")
        add_node(
            "worldDeviceNode",
            resource=r"base\gameplay\devices\masters\computers\computer_1.ent",
        )
        add_node(
            "worldDeviceNode",
            resource=r"base\gameplay\devices\masters\access_points\router_wall.ent",
        )
        add_node(
            "worldDeviceNode",
            resource=r"base\gameplay\devices\masters\access_points\virtual_accesspoint.ent",
        )
        add_node(
            "worldEntityNode",
            resource=r"base\gameplay\devices\doors\final\single_door.ent",
        )
        add_node(
            "worldEntityNode",
            resource=r"base\gameplay\devices\doors\final\single_door_decorative.ent",
        )
        add_node(
            "worldEntityNode",
            resource=r"base\gameplay\devices\masters\fuse_box\generator.ent",
        )
        add_node(
            "worldEntityNode",
            resource=r"base\gameplay\devices\drop_points\drop_point.ent",
        )
        add_node(
            "worldDeviceNode",
            resource=r"base\gameplay\devices\distractors\plate_antenna_large.ent",
        )
        add_node(
            "worldDeviceNode",
            resource=r"base\gameplay\devices\security_system\cameras\surveillance_camera.ent",
        )
        add_node("worldCommunityRegistryNode", debug_name="vanilla_community")
        add_node("worldQuestAreaNode", debug_name="vanilla_quest_area")
        add_node(
            "worldEntityNode",
            resource=r"base\gameplay\loot\containers\crates\crate_small.ent",
        )
        add_node(
            "worldEntityNode",
            resource=r"base\gameplay\loot\containers\bodies\ma_corpse_container.ent",
            debug_name="vendor_body_false_positive",
        )
        self.sector.write_text(json.dumps(document), encoding="utf-8")

        rows = extract_sector(self.sector, self.sector.name, self.config)
        categories = [row["category"] for row in rows]
        self.assertEqual(
            [
                "ai_workspot",
                "parking_space",
                "terminal",
                "access_point",
                "virtual_access_point",
                "door_gate",
                "utility_device",
                "drop_point",
                "antenna",
                "security_device",
                "vanilla_occupancy",
                "quest_ownership",
                "loot_container",
            ],
            categories,
        )
        self.assertNotIn("shop", categories)
        roles = {
            row["category"]: json.loads(row["metadata_json"])["anchor_roles"]
            for row in rows
        }
        self.assertIn("capture_origin", roles["ai_workspot"])
        self.assertEqual(["ownership_risk"], roles["quest_ownership"])
        self.assertIn("semantic_evidence", roles["security_device"])

    def test_location_area_outline_supplies_named_polygon(self) -> None:
        document = sector_document()
        area = document["Data"]["RootChunk"]["nodes"][-1]["Data"]
        area["$type"] = "worldLocationAreaNode"
        area["debugName"] = {"$value": "{biotechnica_flats}"}
        vertices = [(-10.0, -10.0), (10.0, -10.0), (10.0, 10.0), (-10.0, 10.0)]
        buffer = struct.pack("<I", len(vertices)) + b"".join(
            struct.pack("<ffff", x, y, 0.0, 1.0) for x, y in vertices
        )
        area["outline"] = {
            "Data": {
                "$type": "AreaShapeOutline",
                "buffer": base64.b64encode(buffer).decode("ascii"),
            }
        }
        area["notifiers"] = [
            {"Data": {"districtID": {"$value": "114669226962"}}}
        ]
        self.sector.write_text(json.dumps(document), encoding="utf-8")

        index_sectors(self.connection, self.source, self.config)
        result = plan_locations(self.connection, self.config)
        area_row = self.connection.execute("SELECT * FROM areas").fetchone()
        place = self.connection.execute(
            "SELECT * FROM places WHERE category='vending_machine'"
        ).fetchone()

        self.assertEqual(1, result["areas"])
        self.assertEqual("Biotechnica Flats", area_row["name"])
        self.assertEqual("Biotechnica Flats", place["named_area"])
        provenance = json.loads(area_row["provenance_json"])
        self.assertEqual("114669226962", provenance["district_id"])
        self.assertEqual(4, len(provenance["polygon_xy"]))

    def test_resource_orientation_correction_is_applied(self) -> None:
        corrected = json.loads(json.dumps(self.config))
        corrected["orientation_corrections"] = [
            {
                "id": "fixture_reverse_vending",
                "resource_pattern": "vending_machine_1.ent",
                "forward_axis": "-y",
                "yaw_correction_degrees": 0,
            }
        ]
        rows = extract_sector(self.sector, self.sector.name, corrected)
        vending = next(row for row in rows if row["category"] == "vending_machine")
        self.assertAlmostEqual(-1.0, vending["forward_y"])
        metadata = json.loads(vending["metadata_json"])
        self.assertEqual(
            "fixture_reverse_vending", metadata["orientation_correction_id"]
        )

    def test_incremental_index_rtree_fts_and_planner(self) -> None:
        indexed = index_sectors(self.connection, self.source, self.config)
        unchanged = index_sectors(self.connection, self.source, self.config)
        self.assertEqual(1, indexed["indexed"])
        self.assertEqual(1, unchanged["unchanged"])
        self.assertEqual(
            6,
            self.connection.execute("SELECT COUNT(*) FROM feature_rtree").fetchone()[0],
        )
        self.assertIsNotNone(
            self.connection.execute(
                "SELECT rowid FROM feature_fts WHERE feature_fts MATCH 'vending'"
            ).fetchone()
        )
        with transaction(self.connection):
            self.connection.execute(
                """INSERT INTO metadata_overrides(
                       target_type,target_id,field_name,value_json,reviewed_by,reviewed_at,reason)
                   VALUES('road','r_roadsplinenode_test','name',?,'test','2026-01-01','fixture')""",
                (json.dumps("Kabuki Road"),),
            )
        result = plan_locations(self.connection, self.config)
        self.assertEqual(2, result["object_places"])
        self.assertEqual(2, result["road_places"])
        vending = self.connection.execute(
            "SELECT * FROM places WHERE category='vending_machine'"
        ).fetchone()
        # 0.5 m oriented half-bound plus 1.0 m clearance, facing outward.
        self.assertAlmostEqual(0.0, vending["requested_x"], delta=0.1)
        self.assertAlmostEqual(1.5, vending["requested_y"], delta=0.1)
        self.assertAlmostEqual(0.0, vending["requested_yaw"], delta=2.0)
        road_rows = self.connection.execute(
            "SELECT * FROM places WHERE category='road' ORDER BY requested_x,direction"
        ).fetchall()
        self.assertEqual(2, len(road_rows))
        unique_points = sorted({round(row["requested_x"], 3) for row in road_rows})
        self.assertEqual([100.0], unique_points)
        self.assertEqual("Kabuki Road", road_rows[0]["nearest_street_name"])
        self.assertEqual(
            3, self.connection.execute("PRAGMA user_version").fetchone()[0]
        )

    def test_planner_preserves_features_but_disables_out_of_scope_places(self) -> None:
        index_sectors(self.connection, self.source, self.config)
        scoped = json.loads(json.dumps(self.config))
        scoped["scope_rule_version"] = "fixture-v1"
        scoped["scope_rules"] = [
            {
                "id": "fixture_boundary",
                "type": "exclude_negative_half_plane",
                "boundary_origin": {"x": 0.0, "y": 1000.0},
                "boundary_tangent": {"x": 1.0, "y": 0.0},
                "in_scope_reference": {"x": 0.0, "y": 1001.0},
                "out_of_scope_reference": {"x": 0.0, "y": 999.0},
            }
        ]
        result = plan_locations(self.connection, scoped)
        self.assertEqual(result["places"], result["out_of_scope"])
        self.assertEqual(
            result["places"],
            self.connection.execute(
                "SELECT COUNT(*) FROM places WHERE queue_status='disabled'"
            ).fetchone()[0],
        )
        self.assertEqual(
            6, self.connection.execute("SELECT COUNT(*) FROM features").fetchone()[0]
        )

    def test_schema_one_database_migrates_to_three(self) -> None:
        legacy_path = self.root / "legacy.sqlite3"
        legacy = sqlite3.connect(legacy_path)
        legacy.executescript(database_module._SCHEMA_V1)
        legacy.execute("PRAGMA user_version = 1")
        legacy.commit()
        legacy.close()

        upgraded = connect(legacy_path)
        try:
            self.assertEqual(3, upgraded.execute("PRAGMA user_version").fetchone()[0])
            capture_columns = {
                row["name"] for row in upgraded.execute("PRAGMA table_info(captures)")
            }
            place_columns = {
                row["name"] for row in upgraded.execute("PRAGMA table_info(places)")
            }
            self.assertIn("thumbnail_sha256", capture_columns)
            self.assertIn("scope_status", place_columns)
            self.assertIn("scope_rule_version", place_columns)
        finally:
            upgraded.close()

    def test_changed_sector_parse_error_removes_stale_features(self) -> None:
        index_sectors(self.connection, self.source, self.config)
        self.sector.write_text("{broken", encoding="utf-8")
        os.utime(self.sector, None)
        result = index_sectors(self.connection, self.source, self.config)
        self.assertEqual(1, result["errors"])
        self.assertEqual(
            0, self.connection.execute("SELECT COUNT(*) FROM features").fetchone()[0]
        )


class ProtocolTests(unittest.TestCase):
    def test_protocol_unlink_retries_windows_sharing_violation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "ack.json"
            destination.write_text("{}", encoding="utf-8")
            real_unlink = Path.unlink
            attempts = 0

            def unlink_after_two_failures(path: Path, *args: object, **kwargs: object) -> None:
                nonlocal attempts
                attempts += 1
                if attempts < 3:
                    raise PermissionError(32, "file is open by CET")
                real_unlink(path, *args, **kwargs)

            with (
                mock.patch.object(
                    Path,
                    "unlink",
                    autospec=True,
                    side_effect=unlink_after_two_failures,
                ),
                mock.patch("world_locations.protocol.time.sleep") as retry_yield,
            ):
                _unlink_protocol_file(destination)

            self.assertFalse(destination.exists())
            self.assertEqual(3, attempts)
            self.assertEqual(2, retry_yield.call_count)

    def test_atomic_writer_retries_windows_sharing_violation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "heartbeat.json"
            real_replace = os.replace
            attempts = 0

            def replace_after_two_failures(source: object, target: object) -> None:
                nonlocal attempts
                attempts += 1
                if attempts < 3:
                    raise PermissionError(5, "destination is open by CET")
                real_replace(source, target)

            with (
                mock.patch(
                    "world_locations.protocol.os.replace",
                    side_effect=replace_after_two_failures,
                ),
                mock.patch("world_locations.protocol.time.sleep") as retry_yield,
            ):
                atomic_write_json(destination, {"ready": True})

            self.assertEqual({"ready": True}, json.loads(destination.read_text()))
            self.assertEqual(3, attempts)
            self.assertEqual(2, retry_yield.call_count)

    def test_black_loading_and_blurred_frames_are_rejected(self) -> None:
        from PIL import Image

        black = validate_image(
            Image.new("RGB", (64, 64), (0, 0, 0)),
            ready_report={"errors": []},
            validation_config={"hud_templates": []},
            config_root=ROOT,
        )
        self.assertFalse(black["valid"])

        loading_image = Image.new("RGB", (1000, 1000), (0, 0, 0))
        for x in range(100, 900):
            for y in range(10):
                loading_image.putpixel((x, y), (255, 32, 16))
        loading = validate_image(
            loading_image,
            ready_report={"errors": []},
            validation_config={"hud_templates": []},
            config_root=ROOT,
        )
        self.assertFalse(loading["valid"])
        self.assertGreater(loading["black_fraction"], 0.98)

        blurred = validate_image(
            Image.new("RGB", (64, 64), (100, 100, 100)),
            ready_report={"errors": []},
            validation_config={
                "hud_templates": [],
                "sharpness_laplacian_threshold": 30.0,
            },
            config_root=ROOT,
        )
        self.assertFalse(blurred["valid"])
        self.assertEqual(0.0, blurred["sharpness_laplacian_variance"])

    def test_ready_event_records_wrong_fov_without_rejecting_frame(self) -> None:
        place = {
            "requested_x": 1.0,
            "requested_y": 2.0,
            "requested_z": 3.0,
            "requested_yaw": 90.0,
            "requested_pitch": 0.0,
            "requested_roll": 0.0,
        }
        readiness = {
            "streaming_complete": True,
            "player_attached": True,
            "camera_attached": True,
            "loading_screen": False,
            "menu_open": False,
            "paused": False,
            "position_valid": True,
            "position_stable": True,
            "ground_probe": True,
            "ui_suppressed": True,
            "weapon_suppressed": True,
            "presented_frame": 1,
        }
        report = validate_ready_event(
            {
                "readiness": readiness,
                "actual_pose": {"x": 1, "y": 2, "z": 3, "yaw": 90},
                "actual_fov": 75,
            },
            place,
            {"profile": {"fov": 80}, "fov_tolerance_degrees": 0.25},
        )
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(5.0, report["fov_delta_degrees"])

    def test_ready_event_records_heading_drift_without_rejecting_frame(self) -> None:
        place = {
            "requested_x": 1.0,
            "requested_y": 2.0,
            "requested_z": 3.0,
            "requested_yaw": 90.0,
            "requested_pitch": 0.0,
            "requested_roll": 0.0,
        }
        report = validate_ready_event(
            {
                "readiness": {
                    "streaming_complete": True,
                    "player_attached": True,
                    "camera_attached": True,
                    "loading_screen": False,
                    "menu_open": False,
                    "paused": False,
                    "position_valid": True,
                    "position_stable": True,
                    "ground_probe": True,
                    "ui_suppressed": True,
                    "weapon_suppressed": True,
                    "presented_frame": 1,
                },
                "actual_pose": {"x": 1, "y": 2, "z": 3, "yaw": 92.9},
                "actual_fov": 80,
            },
            place,
            {"profile": {"fov": 80}, "fov_tolerance_degrees": 0.25},
        )
        self.assertTrue(report["valid"], report["errors"])
        self.assertAlmostEqual(2.9, report["heading_delta_degrees"])

    def test_ready_event_has_no_wall_clock_minimum(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            protocol = RuntimeProtocol(Path(temporary), poll_seconds=0.001)
            protocol.prepare()
            command_id = "command-immediate"
            atomic_write_json(
                protocol.event_paths["ready"],
                {"schema_version": 1, "command_id": command_id, "event": "ready"},
            )
            started = time.monotonic()
            event = protocol.wait_for_event(
                command_id=command_id,
                accepted_types={"ready"},
                timeout_seconds=5,
                session_id="session-test",
            )
            self.assertEqual("ready", event["event"])
            self.assertLess(time.monotonic() - started, 0.1)

    def test_delayed_streaming_cannot_capture_before_ready(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            protocol = RuntimeProtocol(Path(temporary), poll_seconds=0.001)
            protocol.prepare()
            command_id = "command-delayed"
            capture_called = threading.Event()

            def runtime() -> None:
                time.sleep(0.04)
                self.assertFalse(capture_called.is_set())
                atomic_write_json(
                    protocol.event_paths["ready"],
                    {
                        "schema_version": 1,
                        "command_id": command_id,
                        "event": "ready",
                        "readiness": {"presented_frame": 77},
                    },
                )

            worker = threading.Thread(target=runtime)
            worker.start()
            event = protocol.wait_for_event(
                command_id=command_id,
                accepted_types={"ready"},
                timeout_seconds=1,
                session_id="session-test",
            )
            capture_called.set()
            worker.join()
            self.assertEqual(77, event["readiness"]["presented_frame"])

    def test_timeout_reports_malformed_event(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            protocol = RuntimeProtocol(Path(temporary), poll_seconds=0.001)
            protocol.prepare()
            protocol.event_paths["ready"].write_text("not-json", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeTimeout, "malformed"):
                protocol.wait_for_event(
                    command_id="missing",
                    accepted_types={"ready"},
                    timeout_seconds=0.02,
                    session_id="session-test",
                )

    def test_completion_barrier_ignores_the_acknowledged_error_event(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            protocol = RuntimeProtocol(Path(temporary), poll_seconds=0.001)
            protocol.prepare()
            command_id = "command-failed"
            atomic_write_json(
                protocol.event_paths["error"],
                {
                    "schema_version": 1,
                    "command_id": command_id,
                    "event": "error",
                    "error_code": "streaming_timeout",
                },
            )

            def runtime() -> None:
                time.sleep(0.02)
                atomic_write_json(
                    protocol.event_paths["completed"],
                    {
                        "schema_version": 1,
                        "command_id": command_id,
                        "event": "completed",
                        "success": False,
                    },
                )

            worker = threading.Thread(target=runtime)
            worker.start()
            event = protocol.wait_for_completion(
                command_id=command_id,
                timeout_seconds=1,
                session_id="session-test",
            )
            worker.join()
            self.assertIs(event["success"], False)

    def test_stale_heartbeat_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            protocol = RuntimeProtocol(Path(temporary))
            atomic_write_json(protocol.cet_heartbeat_path, {"schema_version": 1})
            old = time.time() - 60
            os.utime(protocol.cet_heartbeat_path, (old, old))
            with self.assertRaisesRegex(ProtocolError, "stale"):
                protocol.assert_runtime_alive(maximum_age_seconds=5)

    def test_restore_requires_positive_runtime_verification(self) -> None:
        class Runtime:
            restored = False

            def send(self, _command: dict) -> None:
                return None

            def wait_for_event(self, **_kwargs: object) -> dict:
                return {"restoration_verified": self.restored}

        controller = object.__new__(CaptureController)
        controller.runtime = Runtime()
        self.assertFalse(controller._restore("session-test"))
        controller.runtime.restored = True
        self.assertTrue(controller._restore("session-test"))

    def test_cet_contract_arms_on_update_and_emits_ready_on_draw(self) -> None:
        lua = (TOOLS / "world_location_capture_cet" / "init.lua").read_text(
            encoding="utf-8"
        )
        update = lua.index("registerForEvent('onUpdate'")
        draw = lua.index("registerForEvent('onDraw'")
        self.assertLess(update, draw)
        self.assertIn("state.stage = 'armed'", lua[update:draw])
        self.assertIn("state.stage = 'preflight'", lua)
        self.assertIn("beginCaptureWhenGameplayIsReady()", lua[update:draw])
        self.assertIn("Menu, pause, and loading state are final readiness predicates", lua)
        self.assertNotIn(
            "if state.loadingScreen or state.menuOpen or getPaused()",
            lua,
        )
        self.assertIn("preflight = state.preflightEvidence", lua)
        self.assertIn("readiness = state.lastReadiness", lua)
        self.assertNotIn("failCommand('obstructed'", lua)
        self.assertIn("streamingIsComplete(groundReady, groundGroup)", lua)
        self.assertIn("cameraAttached and positionValid and stable", lua)
        self.assertIn("playerPositionIsStable(actual, delta)", lua)
        self.assertIn("positionStableSeconds + frameDeltaSeconds", lua)
        self.assertNotIn("GetVelocity()", lua)
        self.assertIn("'Static', 'Terrain'", lua)
        self.assertIn("prepareGroundPose", lua)
        self.assertIn("ground_probe_staging_height_m", lua)
        self.assertIn("ground_probe_sample_radius_m", lua)
        self.assertIn("ground_offset_m", lua)
        self.assertIn(
            '"ground_offset_m": 0.3',
            (ROOT / "tools" / "world_location_capture_cet" / "config.example.json").read_text(),
        )
        self.assertIn("ground_snap_timeout", lua)
        self.assertIn("table.sort(hits", lua)
        self.assertNotIn("tryNextLateralPose", lua)
        self.assertNotIn("anchorProbe", lua)
        self.assertIn("state.lastControllerHeartbeatUnix = heartbeat.unix_seconds", lua)
        self.assertNotIn("SetZoom(", lua)
        self.assertNotIn("SetFOV(", lua)
        self.assertNotIn("GetZoom(", lua)
        self.assertIn("actualFov = camera:GetFOV()", lua)
        self.assertIn("restoreCaptureMode('controller rejected capture')", lua)
        self.assertIn("ack.success ~= false", lua)
        self.assertIn("writeEvent('ready'", lua[draw:])
        self.assertNotIn("sleep(", lua.lower())
        self.assertIn("world_location_capture_emergency_restore", lua)
        self.assertIn("restoreCaptureMode('emergency hotkey')", lua)

    def test_cet_settings_are_explicit_and_avoid_unsafe_group_lookup(self) -> None:
        source = TOOLS / "world_location_capture_cet"
        lua = (source / "init.lua").read_text(encoding="utf-8")
        config = json.loads((source / "config.example.json").read_text("utf-8"))
        settings = config["settings_vars"]
        self.assertNotIn("settings_groups", config)
        self.assertNotIn("GetGroup(", lua)
        self.assertNotIn("Streaming/IsTeleporting", lua)
        self.assertTrue(settings)
        self.assertTrue(
            all(item.get("path") and item.get("name") for item in settings)
        )
        subtitle_paths = {
            item["path"] for item in settings if item["name"] == "Cinematic"
        }
        self.assertEqual({"/accessibility/subtitles"}, subtitle_paths)
        holocall_targets = {
            item["name"]: item.get("capture_value")
            for item in settings
            if item["path"] == "/gameplay/muteholocalls"
        }
        self.assertEqual(
            {"ncpd_dispatcher": True, "fixer_briefs_and_debriefs": True},
            holocall_targets,
        )
        self.assertNotIn("PhoneCallGameController", lua)
        self.assertNotIn("gameuiGenericNotificationGameController", lua)


class ResumeAndRetryTests(unittest.TestCase):
    setUp = IndexAndPlanTests.setUp
    tearDown = IndexAndPlanTests.tearDown

    def test_interrupted_queue_is_resumable(self) -> None:
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        with transaction(self.connection):
            self.connection.execute(
                "UPDATE places SET queue_status='in_progress' WHERE place_pk=(SELECT MIN(place_pk) FROM places)"
            )
            self.connection.execute(
                """INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,
                       runtime_path,started_at,status)
                   VALUES('session-interrupted','test','{}','test','2026-01-01','running')"""
            )
        self.assertEqual(1, recover_interrupted_queue(self.connection))
        row = self.connection.execute(
            "SELECT * FROM places WHERE failure_code='interrupted_session'"
        ).fetchone()
        self.assertEqual("pending", row["queue_status"])
        session = self.connection.execute(
            "SELECT * FROM capture_sessions WHERE session_id='session-interrupted'"
        ).fetchone()
        self.assertEqual("error", session["status"])
        self.assertIsNotNone(session["ended_at"])

    def test_capture_files_and_hashes_are_committed_together(self) -> None:
        from PIL import Image

        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        place = self.connection.execute(
            "SELECT * FROM places WHERE category='vending_machine'"
        ).fetchone()
        planned_pose = tuple(
            place[column]
            for column in (
                "requested_x",
                "requested_y",
                "requested_z",
                "requested_yaw",
                "requested_pitch",
                "requested_roll",
            )
        )
        session_id = "session-files"
        attempt_id = "attempt-files"
        with transaction(self.connection):
            self.connection.execute(
                """INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,
                       runtime_path,started_at,status) VALUES(?,?,?,?,?,'running')""",
                (session_id, "test", "{}", "test", "2026-01-01"),
            )

        controller = object.__new__(CaptureController)
        controller.connection = self.connection
        controller.captures_root = self.root / "captures"
        controller.capture_config = {
            "thumbnail_width": 16,
            "profile": {"time": "10:00", "weather": "clear", "fov": 80},
        }
        controller.game_profile = "test"
        controller._insert_attempt(
            attempt_id=attempt_id,
            session_id=session_id,
            location_id=place["location_id"],
            command_id="command-files",
            attempt_number=1,
        )
        capture_id = controller._save_capture(
            session_id=session_id,
            attempt_id=attempt_id,
            command_id="command-files",
            place=place,
            image=Image.new("RGB", (64, 36), (40, 80, 120)),
            event={
                "actual_pose": {"x": 1, "y": 2, "z": 3, "yaw": 0},
                "effective_pose": {
                    "x": 101,
                    "y": 102,
                    "z": 103,
                    "yaw": 104,
                    "pitch": 105,
                    "roll": 106,
                },
                "actual_fov": 80,
                "runtime_location": {
                    "district": "Watson",
                    "named_area": "Watson",
                },
                "readiness": {"presented_frame": 4},
                "teleport_to_ready_ms": 5.0,
            },
            validation={"publication_ready": True},
            sent_monotonic=1.0,
            ready_monotonic=1.005,
            captured_monotonic=1.006,
        )
        row = self.connection.execute(
            "SELECT * FROM captures WHERE capture_id=?", (capture_id,)
        ).fetchone()
        self.assertIsNone(row["perceptual_hash"])
        self.assertIn(f"{os.sep}Watson{os.sep}", row["png_path"])
        for path_column, hash_column in (
            ("png_path", "image_sha256"),
            ("sidecar_path", "metadata_sha256"),
            ("thumbnail_path", "thumbnail_sha256"),
        ):
            payload = Path(row[path_column]).read_bytes()
            self.assertEqual(hashlib.sha256(payload).hexdigest(), row[hash_column])
        sidecar = json.loads(Path(row["sidecar_path"]).read_text(encoding="utf-8"))
        self.assertEqual("vending_machine", sidecar["anchor"]["category"])
        self.assertIn("capture_origin", sidecar["anchor"]["roles"])
        self.assertIn("vending", sidecar["anchor"]["tags"])
        self.assertEqual(row["image_sha256"], sidecar["files"]["png_sha256"])
        self.assertIn("location_metadata", sidecar)
        self.assertEqual(
            planned_pose,
            tuple(
                sidecar["requested_pose"][column]
                for column in ("x", "y", "z", "yaw", "pitch", "roll")
            ),
        )
        self.assertEqual(101, sidecar["effective_pose"]["x"])
        saved_place = self.connection.execute(
            "SELECT * FROM places WHERE location_id=?", (place["location_id"],)
        ).fetchone()
        self.assertEqual(
            planned_pose,
            tuple(
                saved_place[column]
                for column in (
                    "requested_x",
                    "requested_y",
                    "requested_z",
                    "requested_yaw",
                    "requested_pitch",
                    "requested_roll",
                )
            ),
        )
        self.assertEqual(
            (1, 2, 3),
            tuple(saved_place[c] for c in ("actual_x", "actual_y", "actual_z")),
        )

    def test_controller_exhausts_exactly_three_attempts_without_retry_sleep(
        self,
    ) -> None:
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        place = self.connection.execute(
            "SELECT * FROM places WHERE category='vending_machine'"
        ).fetchone()
        with transaction(self.connection):
            self.connection.execute(
                """INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,
                       runtime_path,started_at,status) VALUES('session-test','test','{}','test',?,'running')""",
                ("2026-01-01",),
            )

        class FailingRuntime:
            sends = 0
            heartbeats = 0

            def heartbeat(self, _session_id: str) -> None:
                self.heartbeats += 1

            def send(self, _command: dict) -> None:
                self.sends += 1

            def wait_for_event(self, **kwargs: object) -> dict:
                if kwargs["accepted_types"] == {"accepted"}:
                    return {"event": "accepted", "timestamp": "2026-01-01"}
                raise ProtocolError("fixture failure")

            def acknowledge(self, *_args: object, **_kwargs: object) -> None:
                return None

            def wait_for_completion(self, **_kwargs: object) -> dict:
                return {"event": "completed", "success": False}

        controller = object.__new__(CaptureController)
        controller.connection = self.connection
        controller.capture_config = {
            "maximum_attempts": 3,
            "loading_timeout_seconds": 1,
            "profile": {"time": "10:00", "weather": "clear", "fov": 80},
        }
        controller.runtime = FailingRuntime()
        started = time.monotonic()
        success, _error = controller._capture_place("session-test", place)
        self.assertFalse(success)
        self.assertEqual(3, controller.runtime.sends)
        self.assertEqual(3, controller.runtime.heartbeats)
        self.assertLess(time.monotonic() - started, 0.5)
        attempts = self.connection.execute(
            "SELECT COUNT(*) FROM capture_attempts WHERE location_id=?",
            (place["location_id"],),
        ).fetchone()[0]
        self.assertEqual(3, attempts)

    def test_missing_completion_aborts_before_sending_a_retry(self) -> None:
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        place = self.connection.execute(
            "SELECT * FROM places WHERE category='vending_machine'"
        ).fetchone()
        with transaction(self.connection):
            self.connection.execute(
                """INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,
                       runtime_path,started_at,status) VALUES('session-wedge','test','{}','test',?,'running')""",
                ("2026-01-01",),
            )

        class WedgedRuntime:
            sends = 0

            def heartbeat(self, _session_id: str) -> None:
                return None

            def send(self, _command: dict) -> None:
                self.sends += 1

            def wait_for_event(self, **kwargs: object) -> dict:
                if kwargs["accepted_types"] == {"accepted"}:
                    return {"event": "accepted", "timestamp": "2026-01-01"}
                raise ProtocolError("streaming timeout")

            def acknowledge(self, *_args: object, **_kwargs: object) -> None:
                return None

            def wait_for_completion(self, **_kwargs: object) -> dict:
                raise RuntimeTimeout("CET remained busy")

        controller = object.__new__(CaptureController)
        controller.connection = self.connection
        controller.capture_config = {
            "maximum_attempts": 3,
            "loading_timeout_seconds": 1,
            "command_completion_timeout_seconds": 1,
            "profile": {"time": "10:00", "weather": "clear", "fov": 80},
        }
        controller.runtime = WedgedRuntime()

        with self.assertRaisesRegex(SessionProtocolError, "aborting session"):
            controller._capture_place("session-wedge", place)
        self.assertEqual(1, controller.runtime.sends)
        saved = self.connection.execute(
            "SELECT queue_status FROM places WHERE location_id=?",
            (place["location_id"],),
        ).fetchone()
        self.assertEqual("in_progress", saved["queue_status"])


if __name__ == "__main__":
    unittest.main()
