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
