"""Site pairs must use actual resource families and safe ground references."""

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from world_locations.config import load_config, validate_planning_config
from world_locations.database import connect
from world_locations.extract import index_sectors
from world_locations.planning import plan_locations


class SiteSurveyTests(unittest.TestCase):
    def test_device_context_uses_standing_references_instead_of_door_or_model_front(self):
        self.add(r"base\gameplay\devices\masters\computers\computer_1.ent", 0)
        self.add(r"base\gameplay\devices\doors\final\single_door_decorative.ent", 4)
        self.add("standing.workspot", 8, kind="worldAISpotNode")
        self.index()
        self.config["site_survey_rules"] = {"terminal": {
            "mode": "ground_context", "view_labels": ["device_context", "surroundings"],
            "ground_reference_categories": ["ai_workspot", "parking_space"],
            "minimum_ground_reference_distance_m": 3,
            "maximum_ground_reference_distance_m": 20,
        }}
        plan_locations(self.connection, self.config, category="terminal")
        views = list(self.connection.execute("SELECT * FROM places"))
        self.assertEqual(len(views), 2)
        for view in views:
            self.assertEqual(view["requested_x"], 8)
            self.assertEqual(json.loads(view["provenance_json"])["ground_reference"]["category"], "ai_workspot")
        self.assertAlmostEqual((views[0]["requested_yaw"]-views[1]["requested_yaw"]) % 360, 180)

    def test_fast_travel_usable_side_has_distinct_outward_and_terminal_poses(self):
        import math

        self.add(r"base\gameplay\devices\fast_travel\data_term_1.ent", 10, y=20, z=5)
        self.chunk["nodeData"]["Data"][0]["Orientation"] = {"i": 0, "j": 0, "k": math.sqrt(.5), "r": math.sqrt(.5)}
        self.index()
        self.config["site_survey_rules"]["fast_travel"] = {
            "mode": "usable_side_pair", "front_axis": "+x", "near_distance_m": 1.5,
            "far_distance_m": 5, "minimum_anchor_separation_m": 5,
            "view_labels": ["arrival_area", "terminal"],
        }
        self.config["workspace"] = {"active_category": "fast_travel", "category_capture_approved": True}
        plan_locations(self.connection, self.config, category="fast_travel")
        views = {r["direction"]: r for r in self.connection.execute("SELECT * FROM places")}
        self.assertEqual(set(views), {"arrival_area", "terminal"})
        self.assertAlmostEqual(views["arrival_area"]["requested_x"], 10)
        self.assertAlmostEqual(views["arrival_area"]["requested_y"], 21.5)
        self.assertAlmostEqual(views["arrival_area"]["requested_yaw"] % 360, 0)
        self.assertAlmostEqual(views["terminal"]["requested_y"], 25)
        self.assertAlmostEqual(views["terminal"]["requested_yaw"], 180)
        self.assertEqual(views["terminal"]["requested_z"], 5)
        self.assertEqual(json.loads(views["arrival_area"]["provenance_json"])["paired_location_id"], views["terminal"]["location_id"])

    def test_vending_outward_views_are_spaced_capped_and_category_scoped(self):
        for x in (0, 1, 20, 40, 60, 80):
            self.add(r"base\gameplay\devices\vending_machines\vending_machine_1.ent", x, z=5)
        self.add(r"base\gameplay\devices\intercom\intercom_entropy.ent", 300)
        self.index()
        plan_locations(self.connection, self.config, category="intercom")
        before = [dict(r) for r in self.connection.execute("SELECT * FROM places WHERE category='intercom'")]
        self.config["vending_machine_rules"] = {"minimum_separation_m": 15, "maximum_locations": 3}
        self.config["scope_rules"] = []
        self.config["hazard_rules"] = []
        retained_ids = None
        for _ in range(2):
            result = plan_locations(self.connection, self.config, category="vending_machine")
            self.assertEqual(result["places"], 3)
            views = list(self.connection.execute("SELECT * FROM places WHERE category='vending_machine' AND queue_status='pending'"))
            self.assertEqual(len(views), 3)
            ids = {v["location_id"] for v in views}
            if retained_ids is not None:
                self.assertEqual(retained_ids, ids)
            retained_ids = ids
            for i, view in enumerate(views):
                self.assertEqual(view["direction"], "outward")
                self.assertEqual(view["requested_yaw"], 0)
                self.assertEqual(view["requested_z"], 5)
                self.assertAlmostEqual(view["requested_y"], 1.45)
                for other in views[i+1:]:
                    self.assertGreaterEqual(abs(view["requested_x"]-other["requested_x"]), 15)
        self.assertEqual(before, [dict(r) for r in self.connection.execute("SELECT * FROM places WHERE category='intercom'")])

    def test_fast_travel_pilot_preserves_other_categories_and_pairs(self):
        for x in (0, 100, 200):
            self.add(r"base\gameplay\devices\fast_travel\data_term_1.ent", x)
        self.add(r"base\gameplay\devices\intercom\intercom_entropy.ent", 300)
        self.index()
        plan_locations(self.connection, self.config, category="intercom")
        before = [dict(r) for r in self.connection.execute("SELECT * FROM places WHERE category='intercom'")]
        self.config["site_survey_rules"]["fast_travel"] = {
            "mode": "entrance_lobby", "near_distance_m": 3,
            "minimum_anchor_separation_m": 5, "view_labels": ["terminal", "arrival_area"],
        }
        self.config["workspace"] = {"active_category": "fast_travel", "require_category_calibration": True}
        plan_locations(self.connection, self.config, category="fast_travel")
        self.assertEqual(self.connection.execute("SELECT count(*) FROM places WHERE category='fast_travel' AND queue_status='pending'").fetchone()[0], 0)
        anchor = self.connection.execute("SELECT feature_id FROM features WHERE category='fast_travel' ORDER BY feature_id LIMIT 1").fetchone()[0]
        self.config["workspace"]["calibration_capture_anchor_ids"] = [anchor]
        for _ in range(2):
            plan_locations(self.connection, self.config, category="fast_travel")
            views = list(self.connection.execute("SELECT * FROM places WHERE category='fast_travel' AND queue_status='pending' ORDER BY direction"))
            self.assertEqual(len(views), 2)
            self.assertEqual({v["direction"] for v in views}, {"terminal", "arrival_area"})
            self.assertTrue(all(v["review_status"] == "needs_calibration" and v["requested_y"] == 3 for v in views))
            self.assertAlmostEqual((views[0]["requested_yaw"]-views[1]["requested_yaw"]) % 360, 180)
            provenance = [json.loads(v["provenance_json"]) for v in views]
            self.assertEqual(provenance[0]["capture_pair_id"], provenance[1]["capture_pair_id"])
            self.assertEqual(provenance[0]["paired_location_id"], views[1]["location_id"])
        self.assertEqual(before, [dict(r) for r in self.connection.execute("SELECT * FROM places WHERE category='intercom'")])
        self.config["workspace"] = {"active_category": "fast_travel", "require_category_calibration": False, "category_capture_approved": True}
        plan_locations(self.connection, self.config, category="fast_travel")
        enabled = list(self.connection.execute("SELECT * FROM places WHERE category='fast_travel' AND queue_status='pending'"))
        self.assertEqual(len(enabled), 6)
        self.assertTrue(all(v["review_status"] != "needs_calibration" for v in enabled))
        self.assertTrue(all(json.loads(v["provenance_json"])["capture_approval"] == "user_requested_full_category" for v in enabled))
        self.assertEqual(before, [dict(r) for r in self.connection.execute("SELECT * FROM places WHERE category='intercom'")])

    def test_drop_points_get_opposing_views_at_the_ground_anchor_height(self):
        self.add(r"base\gameplay\devices\drop_points\drop_point.ent", 10, z=12)
        self.index()
        self.config["site_survey_rules"] = {"drop_point": {
            "mode": "entrance_lobby", "near_distance_m": 3,
            "minimum_anchor_separation_m": 5, "view_labels": ["drop_point", "surroundings"],
        }}
        self.config["workspace"] = {"active_category": "drop_point", "category_capture_approved": True}
        plan_locations(self.connection, self.config, category="drop_point")
        views = list(self.connection.execute("SELECT * FROM places"))
        self.assertEqual(len(views), 2)
        self.assertEqual({v["direction"] for v in views}, {"drop_point", "surroundings"})
        self.assertTrue(all(v["requested_z"] == 12 and v["requested_y"] == 3 and v["queue_status"] == "pending" for v in views))
        self.assertAlmostEqual((views[0]["requested_yaw"]-views[1]["requested_yaw"]) % 360, 180)
        self.assertEqual(json.loads(views[0]["provenance_json"])["paired_location_id"], views[1]["location_id"])

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.source = self.root / "sectors"
        self.source.mkdir()
        self.file = self.source / "fixture.streamingsector.json"
        self.chunk = {"nodes": [], "nodeData": {"Data": []}}
        self.config = load_config()
        self.connection = connect(self.root / "locations.sqlite3")
        self.addCleanup(self.connection.close)

    def add(self, resource, x, y=0, z=0, kind="worldEntityNode"):
        index = len(self.chunk["nodes"])
        self.chunk["nodes"].append({"Data": {"$type": kind, "debugName": {"$value": "stand"}, "entityTemplate": {"DepotPath": {"$value": resource}}}})
        self.chunk["nodeData"]["Data"].append({"NodeIndex": index, "Id": str(index), "Position": {"X": x, "Y": y, "Z": z}, "Orientation": {"i": 0, "j": 0, "k": 0, "r": 1}})

    def index(self):
        self.file.write_text(json.dumps({"Data": {"RootChunk": self.chunk}}), encoding="utf-8")
        index_sectors(self.connection, self.source, self.config)

    def populate(self):
        self.add(r"base\gameplay\devices\intercom\intercom_entropy.ent", 100)
        self.add(r"base\gameplay\devices\doors\elevator\common_lift_door.ent", 120)
        self.add(r"base\gameplay\devices\security_systems\security_gate_and_locker\security_gate.ent", 140)
        self.add(r"base\gameplay\devices\traffic\road_blockade\road_barrier_poor.ent", 160)
        self.add(r"base\gameplay\devices\security_systems\surveillance_cameras\surveillance_camera.ent", 200, z=6)
        self.add(r"base\gameplay\devices\security_systems\security_turret\ceiling_turret.ent", 212, z=6)
        self.add(r"base\gameplay\devices\distractors\plate_antenna_large.ent", 240, z=10)
        self.add(r"base\gameplay\devices\masters\access_points\antenna_access_point.ent", 270, z=10)
        for x in (186, 224, 262, 292):
            self.add("ground.workspot", x, z=0, kind="worldAISpotNode")
        self.index()

    def test_plural_security_path_and_new_entrance_families_are_indexed(self):
        self.populate()
        counts = dict(self.connection.execute("SELECT category,COUNT(*) FROM features GROUP BY category"))
        self.assertEqual(counts["security_device"], 2)
        self.assertEqual(counts["security_checkpoint"], 1)
        for family in ("intercom", "elevator", "road_barrier", "antenna"):
            self.assertEqual(counts[family], 1)
        self.assertEqual(counts["access_point"], 1, "Existing antenna/access-point identity must be retained")
        for row in self.connection.execute("SELECT tags FROM features WHERE category IN ('security_device','security_checkpoint')"):
            self.assertIn("ownership_risk", row[0])

    def test_pairs_ground_height_geometry_and_scoped_queue_preservation(self):
        self.populate()
        self.connection.execute("INSERT INTO places(location_id,category,requested_x,requested_y,requested_z,requested_yaw,forward_x,forward_y,forward_z,extraction_rule_version,placement_rule_version,queue_order,created_at,updated_at,queue_status) VALUES('legacy','shop',0,0,0,0,0,1,0,'old','old',0,'old','old','captured')")
        self.connection.commit()
        before = tuple(self.connection.execute("SELECT * FROM places WHERE location_id='legacy'").fetchone())
        result = plan_locations(self.connection, self.config, category="site_surveys")
        self.assertEqual(result["site_survey_pairs"], 8)
        self.assertFalse(result["unresolved_ground_references"])
        self.assertEqual(before, tuple(self.connection.execute("SELECT * FROM places WHERE location_id='legacy'").fetchone()))
        groups = {}
        for row in self.connection.execute("SELECT * FROM places WHERE category!='shop'"):
            provenance = json.loads(row["provenance_json"])
            groups.setdefault(provenance["capture_pair_id"], []).append(row)
            if row["category"] in ("security_device", "antenna"):
                self.assertEqual(row["requested_z"], 0)
                self.assertIsNotNone(provenance["ground_reference"])
                self.assertGreater(provenance["target_anchor"]["z"], row["requested_z"])
        for pair in groups.values():
            self.assertEqual(len(pair), 2)
            self.assertEqual(json.loads(pair[0]["provenance_json"])["paired_location_id"], pair[1]["location_id"])
        intercom = {r["direction"]: r for r in self.connection.execute("SELECT * FROM places WHERE category='intercom'")}
        self.assertEqual(intercom["entrance"]["requested_y"], 2)
        self.assertEqual(intercom["approach"]["requested_y"], 12)
        self.assertEqual(intercom["entrance"]["requested_yaw"], 180)
        barrier = sorted(tuple(r) for r in self.connection.execute("SELECT requested_y,requested_yaw FROM places WHERE category='road_barrier'"))
        self.assertEqual(barrier, [(-8, 0), (8, 180)])
        ids = {r[0] for r in self.connection.execute("SELECT location_id FROM places")}
        plan_locations(self.connection, self.config, category="site_surveys")
        self.assertEqual(ids, {r[0] for r in self.connection.execute("SELECT location_id FROM places")})

    def test_elevated_devices_without_ground_reference_are_reported_not_teleported_to(self):
        self.add(r"base\gameplay\devices\security_systems\surveillance_cameras\surveillance_camera.ent", 0, z=100)
        self.add("ground.workspot", 0, z=0, kind="worldAISpotNode")
        self.index()
        result = plan_locations(self.connection, self.config, category="security_device")
        self.assertEqual(result["site_survey_pairs"], 0)
        self.assertEqual(result["unresolved_ground_references"][0]["reason"], "no_nearby_ground_reference")
        self.assertEqual(self.connection.execute("SELECT COUNT(*) FROM places").fetchone()[0], 0)

    def test_ground_context_avoids_reference_directly_below_an_overhead_device(self):
        self.add(r"base\gameplay\devices\security_systems\surveillance_cameras\surveillance_camera.ent", 0, z=6)
        self.add("ground.workspot", 1, z=0, kind="worldAISpotNode")
        self.add("ground.workspot", 15, z=0, kind="worldAISpotNode")
        self.index()
        plan_locations(self.connection, self.config, category="security_device")
        positions = {row[0] for row in self.connection.execute("SELECT requested_x FROM places")}
        self.assertEqual(positions, {15})

    def test_two_devices_sharing_identical_context_views_do_not_duplicate_the_pair(self):
        self.add(r"base\gameplay\devices\security_systems\surveillance_cameras\surveillance_camera.ent", -15, z=6)
        self.add(r"base\gameplay\devices\security_systems\security_turret\ceiling_turret.ent", 15, z=6)
        self.add("ground.workspot", 0, z=0, kind="worldAISpotNode")
        self.index()
        result = plan_locations(self.connection, self.config, category="security_device")
        self.assertEqual(result["categories"]["security_device"]["anchors"], 2)
        self.assertEqual(result["categories"]["security_device"]["deduplicated_viewpoint_pairs"], 1)
        self.assertEqual(result["site_survey_pairs"], 1)

    def test_anchor_spacing_never_removes_just_one_partner(self):
        self.add(r"base\gameplay\devices\intercom\intercom_entropy.ent", 0)
        self.add(r"base\gameplay\devices\intercom\intercom_kitsch.ent", 1)
        self.index()
        result = plan_locations(self.connection, self.config, category="intercom")
        self.assertEqual(result["site_survey_pairs"], 1)
        self.assertEqual(result["categories"]["intercom"]["deduplicated_anchors"], 1)
        self.assertEqual(self.connection.execute("SELECT COUNT(*) FROM places").fetchone()[0], 2)

    def test_invalid_profiles_fail_before_planning(self):
        for changes in ({"mode": "unknown"}, {"view_labels": ["same", "same"]}, {"near_distance_m": float("nan")}, {"maximum_ground_reference_drop_m": -1}):
            config = copy.deepcopy(self.config)
            config["site_survey_rules"]["security_device"].update(changes)
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                validate_planning_config(config)


if __name__ == "__main__":
    unittest.main()
