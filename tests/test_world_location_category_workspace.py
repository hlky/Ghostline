"""An archived collection stays immutable; category experiments stay isolated."""

from pathlib import Path
import json
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from world_locations import cli
from world_locations.extract import index_sectors
from world_locations.planning import plan_locations
from tests import test_world_location_capture as fixtures


class CategoryWorkspaceTests(unittest.TestCase):
    setUp = fixtures.IndexAndPlanTests.setUp
    tearDown = fixtures.IndexAndPlanTests.tearDown

    def test_road_calibration_plan_does_not_touch_other_categories(self):
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        before = [dict(r) for r in self.connection.execute("SELECT * FROM places WHERE category!='road' ORDER BY location_id")]
        self.config["workspace"] = {"active_category": "road", "require_road_calibration": True}
        result = plan_locations(self.connection, self.config, category="road")
        self.assertTrue(result["requires_geometry_calibration"])
        self.assertEqual(before, [dict(r) for r in self.connection.execute("SELECT * FROM places WHERE category!='road' ORDER BY location_id")])
        roads = list(self.connection.execute("SELECT * FROM places WHERE category='road'"))
        self.assertTrue(roads)
        for road in roads:
            self.assertEqual(road["queue_status"], "disabled")
            self.assertEqual(road["review_status"], "needs_calibration")
            self.assertEqual(json.loads(road["provenance_json"])["geometry_status"], "unvalidated_proxy_centerline")

    def test_archive_guard_prevents_materialization(self):
        (self.root / "ARCHIVED.json").write_text("{}")
        with self.assertRaisesRegex(cli.CliError, "archived"):
            cli._materialize({"root": self.root}, {})
        self.assertFalse((self.root / "capture-config.json").exists())

    def test_capture_rejects_another_category_before_writing(self):
        args = cli.create_parser().parse_args(["capture", "--category", "fake_door"])
        with self.assertRaisesRegex(cli.CliError, "one category: road"):
            cli.command_capture(args, {"workspace": {"active_category": "road"}}, {})
