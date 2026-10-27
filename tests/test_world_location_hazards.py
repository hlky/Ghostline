import json
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from world_locations.config import load_config
from world_locations.hazards import hazard_at_point, apply_hazard_exclusions
from world_locations.model import Vec3, Quaternion
from world_locations.extract import index_sectors
from world_locations.planning import plan_locations
from tests import test_world_location_capture as fixtures


class HazardTests(unittest.TestCase):
    def test_border_and_known_city_location(self):
        config = load_config()
        self.assertIsNotNone(hazard_at_point(Vec3(-2817.558, -5645.129, 101.17), config))
        self.assertIsNone(hazard_at_point(Vec3(-1976.953, 1179.085, 12.14), config))

    def test_native_volumes_preserve_vertical_separation(self):
        config = load_config()
        rules = [r for r in config["hazard_rules"] if r["type"] == "prism"]
        self.assertEqual(len(rules), 36)
        for rule in rules:
            isolated = {**config, "hazard_rules": [rule]}
            x, y = rule["outline"][0]  # Boundary remains inside even for concave outlines.
            rotation = Quaternion.from_mapping(rule["rotation"])
            origin = Vec3.from_mapping(rule["origin"])
            inside = origin + rotation.rotate(Vec3(x, y, (rule["min_z"]+rule["max_z"])/2))
            above = origin + rotation.rotate(Vec3(x, y, rule["max_z"]+100))
            self.assertIsNotNone(hazard_at_point(inside, isolated), rule["id"])
            self.assertIsNone(hazard_at_point(above, isolated), rule["id"])


class QueueHazardTests(unittest.TestCase):
    setUp = fixtures.IndexAndPlanTests.setUp
    tearDown = fixtures.IndexAndPlanTests.tearDown

    def test_exclusions_preserve_poses_and_disable_both_views_only(self):
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        rows = [dict(r) for r in self.connection.execute("SELECT * FROM places ORDER BY location_id")]
        for row in rows[:2]:
            self.connection.execute("UPDATE places SET provenance_json=? WHERE location_id=?",
                                    (json.dumps({"capture_pair_id": "hazard-pair"}), row["location_id"]))
        self.connection.execute("UPDATE places SET named_area='Border Crossing' WHERE location_id=?", (rows[0]["location_id"],))
        self.connection.commit()
        before = {r["location_id"]: dict(r) for r in self.connection.execute("SELECT * FROM places")}
        changes = apply_hazard_exclusions(self.connection, self.config)
        self.assertEqual({c["location_id"] for c in changes}, {r["location_id"] for r in rows[:2]})
        for row in self.connection.execute("SELECT * FROM places"):
            old = before[row["location_id"]]
            if row["location_id"] not in {r["location_id"] for r in rows[:2]}:
                self.assertEqual(dict(row), old)
            for field in ("requested_x", "requested_y", "requested_z", "provenance_json", "anchor_feature_id"):
                self.assertEqual(row[field], old[field])
        self.assertEqual(apply_hazard_exclusions(self.connection, self.config), [])
