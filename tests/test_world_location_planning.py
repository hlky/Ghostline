from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from world_locations.config import load_config, validate_planning_config
from world_locations.database import connect
from world_locations.extract import index_sectors
from world_locations.model import Vec3
from world_locations import planning
from tests.test_world_location_capture import sector_document
from reset_world_location_queue import reset_queue


class PlanningReliabilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        self.connection = connect(self.root / "locations.sqlite3")
        self.addCleanup(self.connection.close)
        self.source = self.root / "sectors"
        self.source.mkdir()
        (self.source / "fixture.streamingsector.json").write_text(
            json.dumps(sector_document()), encoding="utf-8"
        )
        self.config = load_config()
        self.config["scope_rules"] = []
        index_sectors(self.connection, self.source, self.config)

    def vending(self):
        return dict(
            self.connection.execute(
                "SELECT * FROM places WHERE category='vending_machine'"
            ).fetchone()
        )

    def test_replan_preserves_queue_failures_active_work_and_runtime_evidence(self):
        planning.plan_locations(self.connection, self.config)
        initial = self.vending()
        for state in ("failed", "in_progress", "captured"):
            provenance = json.loads(initial["provenance_json"])
            provenance.update(
                {field: "runtime" for field in planning.REQUIRED_NAME_FIELDS}
            )
            with self.connection:
                self.connection.execute(
                    """UPDATE places SET queue_status=?,failure_code='streaming_timeout',failure_detail='retained failure',
                    actual_x=7,publishable=1,nearest_fast_travel_name='Runtime FT',nearest_street_name='Runtime Street',
                    named_area='Runtime Area',review_status='resolved',provenance_json=? WHERE location_id=?""",
                    (state, json.dumps(provenance), initial["location_id"]),
                )
            planning.plan_locations(self.connection, self.config)
            after = self.vending()
            self.assertEqual(after["queue_status"], state)
            self.assertEqual(after["failure_detail"], "retained failure")
            self.assertEqual(after["actual_x"], 7)
            self.assertEqual(after["named_area"], "Runtime Area")
            self.assertEqual(after["review_status"], "resolved")
            self.assertEqual(after["publishable"], int(state == "captured"))
            self.assertEqual(
                json.loads(after["provenance_json"])["named_area"], "runtime"
            )

    def test_changed_pose_requeues_without_rewriting_capture_history(self):
        planning.plan_locations(self.connection, self.config)
        initial = self.vending()
        with self.connection:
            self.connection.execute(
                "UPDATE places SET queue_status='captured',actual_x=7,publishable=1 WHERE location_id=?",
                (initial["location_id"],),
            )
            self.connection.execute(
                "INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,runtime_path,started_at,status) VALUES('s','test','{}','none','now','completed')"
            )
            self.connection.execute(
                "INSERT INTO capture_attempts(attempt_id,session_id,location_id,command_id,attempt_number,status) VALUES('a','s',?,'c',1,'captured')",
                (initial["location_id"],),
            )
            self.connection.execute(
                "UPDATE features SET metadata_json=json_set(metadata_json,'$.clearance_m',8) WHERE feature_id=?",
                (initial["anchor_feature_id"],),
            )
        planning.plan_locations(self.connection, self.config)
        after = self.vending()
        self.assertEqual(after["location_id"], initial["location_id"])
        self.assertNotEqual(after["requested_y"], initial["requested_y"])
        self.assertEqual(after["queue_status"], "pending")
        self.assertEqual(after["publishable"], 0)
        self.assertIsNone(after["actual_x"])
        self.assertEqual(
            self.connection.execute(
                "SELECT status FROM capture_attempts WHERE attempt_id='a'"
            ).fetchone()[0],
            "captured",
        )
        planning._upsert_places(self.connection, [])
        self.assertEqual(self.vending()["queue_status"], "disabled")
        self.assertEqual(
            self.connection.execute("SELECT COUNT(*) FROM capture_attempts").fetchone()[
                0
            ],
            1,
        )

    def test_streaming_reference_bounds_do_not_displace_object_camera(self):
        planning.plan_locations(self.connection, self.config)
        before = self.vending()
        with self.connection:
            self.connection.execute(
                "UPDATE features SET min_x=-9999,min_y=-5000,min_z=-2000,max_x=9999,max_y=5000,max_z=2000 WHERE feature_id=?",
                (before["anchor_feature_id"],),
            )
        planning.plan_locations(self.connection, self.config)
        after = self.vending()
        self.assertEqual(after["requested_y"], before["requested_y"])
        self.assertEqual(
            json.loads(after["provenance_json"])["front_extent"], "reviewed_rule"
        )

    def candidate(self, identifier, y, category="terminal"):
        return planning._place_record(
            location_id=identifier,
            anchor_feature_id=None,
            category=category,
            direction="outward",
            requested=Vec3(0, y, 0),
            forward=Vec3(0, 1, 0),
            resource_path="fixture.ent",
            source_sector="fixture",
            road_id=None,
            extraction_version="1",
            placement_version="1",
            metadata={},
            provenance={},
            review_status="needs_metadata",
        )

    def test_scope_is_applied_before_category_deduplication(self):
        config = copy.deepcopy(self.config)
        config["scope_rules"] = [
            {
                "id": "boundary",
                "type": "exclude_negative_half_plane",
                "boundary_origin": {"x": 0, "y": 0},
                "boundary_tangent": {"x": 1, "y": 0},
                "in_scope_reference": {"x": 0, "y": 1},
            }
        ]
        config["classification_rules"] = [
            {
                "id": "terminal",
                "category": "terminal",
                "minimum_candidate_separation_m": 10,
            }
        ]
        candidates = [self.candidate("a-out", -1), self.candidate("z-in", 1)]
        with (
            mock.patch.object(planning, "_object_places", return_value=candidates),
            mock.patch.object(planning, "_road_places", return_value=[]),
        ):
            result = planning.plan_locations(self.connection, config)
        self.assertEqual(result["in_scope"], 1)
        self.assertEqual(
            self.connection.execute(
                "SELECT location_id FROM places WHERE queue_status='pending'"
            ).fetchone()[0],
            "z-in",
        )

    def test_captured_representative_survives_new_same_category_neighbor(self):
        config = copy.deepcopy(self.config)
        config["classification_rules"] = [
            {
                "id": "terminal",
                "category": "terminal",
                "minimum_candidate_separation_m": 10,
            }
        ]
        existing = self.candidate("z-captured", 10)
        with (
            mock.patch.object(
                planning, "_object_places", return_value=[copy.deepcopy(existing)]
            ),
            mock.patch.object(planning, "_road_places", return_value=[]),
        ):
            planning.plan_locations(self.connection, config)
        with self.connection:
            self.connection.execute(
                "UPDATE places SET queue_status='captured' WHERE location_id='z-captured'"
            )
        with (
            mock.patch.object(
                planning,
                "_object_places",
                return_value=[self.candidate("a-new", 11), copy.deepcopy(existing)],
            ),
            mock.patch.object(planning, "_road_places", return_value=[]),
        ):
            planning.plan_locations(self.connection, config)
        rows = self.connection.execute(
            "SELECT location_id,queue_status FROM places"
        ).fetchall()
        self.assertEqual([tuple(row) for row in rows], [("z-captured", "captured")])

    def test_nearest_fast_travel_checks_beyond_first_nonempty_square(self):
        features = [
            row[0]
            for row in self.connection.execute(
                "SELECT feature_id FROM features LIMIT 2"
            )
        ]
        with self.connection:
            for identifier, feature, xy in (
                ("far", features[0], (99, 99)),
                ("near", features[1], (101, 0)),
            ):
                self.connection.execute(
                    "INSERT INTO fast_travel_points(fast_travel_id,feature_id,name,x,y,z,source_sector) VALUES(?,?,?,?,?,0,'fixture')",
                    (identifier, feature, identifier, *xy),
                )
        result = planning._nearest_fast_travel(self.connection, Vec3(0, 0, 0))
        self.assertEqual(result["nearest_fast_travel_id"], "near")
        self.assertEqual(result["nearest_fast_travel_distance_m"], 101)

    def test_nearest_road_checks_exact_segments_beyond_first_aabb(self):
        with self.connection:
            for identifier, points in (
                ("corner", [(90, 90), (100, 90)]),
                ("near", [(105, 0), (105, 1)]),
            ):
                self.connection.execute(
                    "INSERT INTO roads(road_id,name,points_json,length_m,min_x,max_x,min_y,max_y,source_json,provenance_json,planning_rule_version) VALUES(?,?,?,10,?,?,?,?, '[]','{}','1')",
                    (
                        identifier,
                        identifier,
                        json.dumps([dict(x=x, y=y, z=0) for x, y in points]),
                        min(p[0] for p in points),
                        max(p[0] for p in points),
                        min(p[1] for p in points),
                        max(p[1] for p in points),
                    ),
                )
        result = planning._nearest_road(self.connection, Vec3(0, 0, 0))
        self.assertEqual(result["nearest_street_road_id"], "near")
        self.assertEqual(result["nearest_street_distance_m"], 105)

    def test_nearby_runtime_area_is_fallback_and_never_erases_exact_metadata(self):
        with (
            mock.patch.object(planning, "_nearest_fast_travel", return_value={}),
            mock.patch.object(planning, "_nearest_road", return_value={}),
            mock.patch.object(
                planning,
                "_containing_area",
                return_value={"named_area": "Exact area", "district": "Exact district"},
            ),
        ):
            metadata, provenance = planning._metadata_for_point(
                self.connection,
                Vec3(0, 0, 0),
                "location",
                runtime_area_observations=[
                    {
                        "requested_x": 1,
                        "requested_y": 1,
                        "named_area": "Neighbor",
                        "district": None,
                        "subdistrict": "Inferred subdistrict",
                    }
                ],
            )
        self.assertEqual(metadata["named_area"], "Exact area")
        self.assertEqual(metadata["district"], "Exact district")
        self.assertEqual(provenance["subdistrict"], "spatial:nearby_runtime")

    def test_invalid_planning_distances_fail_before_queue_mutation(self):
        planning.plan_locations(self.connection, self.config)
        before = [tuple(row) for row in self.connection.execute("SELECT * FROM places")]
        for value in (0, -1, float("nan"), float("inf"), True, "invalid"):
            with self.subTest(interval=value):
                config = copy.deepcopy(self.config)
                config["road_rules"]["interval_m"] = value
                with self.assertRaises(ValueError):
                    planning.plan_locations(self.connection, config)
        self.assertEqual(
            [tuple(row) for row in self.connection.execute("SELECT * FROM places")],
            before,
        )
        with self.assertRaises(ValueError):
            planning.sample_road_points(
                [Vec3(0, 0, 0), Vec3(500, 0, 0)], {"interval_m": 0}
            )
        with self.assertRaises(ValueError):
            validate_planning_config(
                {"classification_rules": [{"id": "bad", "clearance_m": -1}]}
            )
        for invalid in (float("nan"), float("inf"), "bad"):
            config = copy.deepcopy(self.config)
            config["scope_rules"] = [
                {
                    "id": "bad",
                    "boundary_origin": {"x": invalid, "y": 0},
                    "boundary_tangent": {"x": 1, "y": 0},
                    "in_scope_reference": {"x": 0, "y": 1},
                }
            ]
            with self.assertRaisesRegex(ValueError, "scope rule"):
                planning.plan_locations(self.connection, config)
        self.assertEqual(
            [tuple(row) for row in self.connection.execute("SELECT * FROM places")],
            before,
        )

    def test_reset_retries_only_eligible_failures_and_leaves_recovery_to_controller(
        self,
    ):
        planning.plan_locations(self.connection, self.config)
        rows = self.connection.execute(
            "SELECT location_id FROM places ORDER BY location_id"
        ).fetchall()
        self.assertEqual(len(rows), 4)
        with self.connection:
            self.connection.execute(
                "UPDATE places SET queue_status='failed',failure_code='streaming_timeout'"
            )
            self.connection.execute(
                "UPDATE places SET queue_status='in_progress' WHERE location_id=?",
                (rows[1][0],),
            )
            self.connection.execute(
                "UPDATE places SET review_status='rejected' WHERE location_id=?",
                (rows[2][0],),
            )
            self.connection.execute(
                "UPDATE places SET scope_status='out_of_scope' WHERE location_id=?",
                (rows[3][0],),
            )
        before, reset, after, pending = reset_queue(self.root / "locations.sqlite3")
        self.assertEqual(before, {"failed": 3, "in_progress": 1})
        self.assertEqual(reset, 1)
        self.assertEqual(after, {"failed": 2, "in_progress": 1})
        self.assertEqual(pending, 1)

    def test_reset_refuses_running_session_without_queue_changes(self):
        planning.plan_locations(self.connection, self.config)
        with self.connection:
            self.connection.execute(
                "UPDATE places SET queue_status='failed',failure_code='streaming_timeout'"
            )
            self.connection.execute(
                "INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,runtime_path,started_at,status) VALUES('live','test','{}','none','now','running')"
            )
        before = [tuple(row) for row in self.connection.execute("SELECT * FROM places")]
        with self.assertRaisesRegex(ValueError, "capture session"):
            reset_queue(self.root / "locations.sqlite3")
        self.assertEqual(
            [tuple(row) for row in self.connection.execute("SELECT * FROM places")],
            before,
        )

    def test_malformed_position_fails_sector_instead_of_creating_origin_capture(self):
        sector = self.source / "fixture.streamingsector.json"
        for invalid in (None, "broken", float("nan"), float("inf"), True):
            with self.subTest(position=invalid):
                document = sector_document()
                position = document["Data"]["RootChunk"]["nodeData"]["Data"][0][
                    "Position"
                ]
                if invalid is None:
                    del position["X"]
                else:
                    position["X"] = invalid
                sector.write_text(json.dumps(document), encoding="utf-8")
                result = index_sectors(self.connection, self.source, self.config)
                self.assertEqual(result["errors"], 1)
                self.assertEqual(
                    self.connection.execute("SELECT COUNT(*) FROM features").fetchone()[
                        0
                    ],
                    0,
                )


if __name__ == "__main__":
    unittest.main()
