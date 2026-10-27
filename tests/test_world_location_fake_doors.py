"""Decorative-door surveys retain both views and existing capture identities."""

import copy
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from world_locations.config import load_config, validate_planning_config
from world_locations.config import output_paths
from world_locations.capture import CaptureController
from world_locations.cli import command_export, create_parser
from world_locations.database import connect, transaction
from world_locations.extract import extract_sector, index_sectors
from world_locations.planning import plan_locations
from tests.test_world_location_capture import sector_document


class FakeDoorTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        self.source = self.root / "sectors"
        self.source.mkdir()
        self.file = self.source / "doors.streamingsector.json"
        self.config = load_config()
        self.document = sector_document()
        chunk = self.document["Data"]["RootChunk"]
        for offset, name in enumerate(("single", "double")):
            index = len(chunk["nodes"])
            chunk["nodes"].append({"Data": {
                "$type": "worldEntityNode",
                "entityTemplate": {"DepotPath": {"$value": rf"base\gameplay\devices\doors\final\{name}_door_decorative.ent"}},
            }})
            chunk["nodeData"]["Data"].append({
                "NodeIndex": index, "Id": f"door-{name}",
                # Nearby ordinary anchor deliberately exercises spacing bypass.
                "Position": {"X": 1 + offset * 3, "Y": 1, "Z": 0},
                "Orientation": {"i": 0, "j": 0, "k": math.sqrt(0.5), "r": math.sqrt(0.5)},
            })
        self.file.write_text(json.dumps(self.document), encoding="utf-8")
        self.connection = connect(self.root / "locations.sqlite3")
        self.addCleanup(self.connection.close)

    def test_both_templates_generate_two_rotated_views_without_spacing_loss(self):
        index_sectors(self.connection, self.source, self.config)
        result = plan_locations(self.connection, self.config)
        self.assertEqual(result["fake_door_places"], 4)
        features = self.connection.execute("SELECT * FROM features WHERE category='fake_door'").fetchall()
        self.assertEqual(len(features), 2)
        for feature in features:
            rows = {r["direction"]: r for r in self.connection.execute(
                "SELECT * FROM places WHERE anchor_feature_id=?", (feature["feature_id"],),
            )}
            self.assertEqual(set(rows), {"outward", "building"})
            for direction, distance, yaw in (("outward", 1.5, 90), ("building", 15, 270)):
                row = rows[direction]
                self.assertAlmostEqual(row["requested_x"], feature["x"] - distance)
                self.assertAlmostEqual(row["requested_y"], feature["y"])
                self.assertAlmostEqual(row["requested_yaw"], yaw)
                self.assertEqual(row["queue_status"], "pending")
                provenance = json.loads(row["provenance_json"])
                other = rows["building" if direction == "outward" else "outward"]
                self.assertEqual(provenance["paired_location_id"], other["location_id"])
                self.assertEqual(provenance["capture_pair_id"], json.loads(other["provenance_json"])["capture_pair_id"])
                self.assertEqual(provenance["source_instance_id"], feature["instance_id"])
                self.assertEqual(row["queue_order"], other["queue_order"])
        self.assertEqual(self.connection.execute("SELECT COUNT(DISTINCT json_extract(provenance_json,'$.capture_pair_id')) FROM places WHERE category='fake_door'").fetchone()[0], 2)

    def test_additive_reindex_preserves_old_feature_ids_and_successful_places(self):
        old = copy.deepcopy(self.config)
        old["extraction_rule_version"] = "1.1.0"
        old.pop("feature_identity_version")
        old["classification_rules"] = [r for r in old["classification_rules"] if r["category"] != "fake_door"]
        index_sectors(self.connection, self.source, old)
        plan_locations(self.connection, old)
        original_features = {r[0] for r in self.connection.execute("SELECT feature_id FROM features")}
        place = self.connection.execute("SELECT * FROM places WHERE category='vending_machine'").fetchone()
        with transaction(self.connection):
            self.connection.execute("INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,runtime_path,started_at,status) VALUES('s','test','{}','none','now','completed')")
            self.connection.execute("INSERT INTO capture_attempts(attempt_id,session_id,location_id,command_id,attempt_number,status) VALUES('a','s',?,'c',1,'captured')", (place["location_id"],))
            self.connection.execute("UPDATE places SET queue_status='captured',actual_x=42 WHERE location_id=?", (place["location_id"],))
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        self.assertTrue(original_features <= {r[0] for r in self.connection.execute("SELECT feature_id FROM features")})
        retained = self.connection.execute("SELECT * FROM places WHERE location_id=?", (place["location_id"],)).fetchone()
        self.assertEqual(retained["queue_status"], "captured")
        self.assertEqual(retained["actual_x"], 42)
        self.assertEqual(retained["anchor_feature_id"], place["anchor_feature_id"])
        before = [tuple(r) for r in self.connection.execute("SELECT location_id,requested_x,requested_y,requested_yaw,queue_status FROM places ORDER BY location_id")]
        plan_locations(self.connection, self.config)
        self.assertEqual(before, [tuple(r) for r in self.connection.execute("SELECT location_id,requested_x,requested_y,requested_yaw,queue_status FROM places ORDER BY location_id")])

    def test_scope_still_disables_excluded_fake_door_views(self):
        self.config["scope_rules"] = [{
            "id": "fixture", "type": "exclude_negative_half_plane", "enabled": True,
            "boundary_origin": {"x": 0, "y": 100}, "boundary_tangent": {"x": 1, "y": 0},
            "in_scope_reference": {"x": 0, "y": 101},
        }]
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        rows = self.connection.execute("SELECT queue_status FROM places WHERE category='fake_door'").fetchall()
        self.assertEqual([r[0] for r in rows], ["disabled"] * 4)

    def test_shared_pair_id_and_view_survive_image_sidecars_and_export(self):
        from PIL import Image

        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        feature_id = self.connection.execute("SELECT feature_id FROM features WHERE category='fake_door' LIMIT 1").fetchone()[0]
        rows = self.connection.execute("SELECT * FROM places WHERE anchor_feature_id=? ORDER BY direction", (feature_id,)).fetchall()
        controller = CaptureController.__new__(CaptureController)
        controller.connection = self.connection
        controller.config = self.config
        controller.capture_config = self.config["capture"]
        controller.captures_root = self.root / "captures"
        controller.game_profile = "fixture"
        with transaction(self.connection):
            self.connection.execute("INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,runtime_path,started_at,status) VALUES('s','test','{}','none','now','completed')")
        sidecars = []
        for index, place in enumerate(rows):
            attempt = f"a{index}"
            command = f"c{index}"
            with transaction(self.connection):
                self.connection.execute("INSERT INTO capture_attempts(attempt_id,session_id,location_id,command_id,attempt_number,status) VALUES(?,'s',?,?,1,'ready')", (attempt, place["location_id"], command))
            controller._save_capture(
                session_id="s", attempt_id=attempt, command_id=command, place=place,
                image=Image.new("RGB", (64, 36), "blue"),
                event={"actual_pose": {axis: place[f"requested_{axis}"] for axis in ("x", "y", "z", "yaw", "pitch", "roll")}},
                validation={"valid": True}, sent_monotonic=0, ready_monotonic=1, captured_monotonic=2,
            )
            path = self.connection.execute("SELECT sidecar_path FROM captures WHERE attempt_id=?", (attempt,)).fetchone()[0]
            sidecars.append(json.loads(Path(path).read_text(encoding="utf-8")))
        self.assertTrue(sidecars[0]["capture_pair_id"])
        self.assertEqual(sidecars[0]["capture_pair_id"], sidecars[1]["capture_pair_id"])
        self.assertEqual({s["capture_view"] for s in sidecars}, {"building", "outward"})
        self.assertEqual(sidecars[0]["paired_location_id"], sidecars[1]["location_id"])
        self.config["output_root"] = str(self.root)
        args = create_parser().parse_args(["export", "--include-unpublishable"])
        result = command_export(args, self.config, output_paths(self.config))
        self.assertEqual(result["exported"], 2)
        exported = json.loads(Path(result["json"]).read_text(encoding="utf-8"))["places"]
        self.assertEqual({r["capture_pair_id"] for r in exported}, {sidecars[0]["capture_pair_id"]})
        self.assertEqual({r["capture_view"] for r in exported}, {"building", "outward"})

    def test_proxy_and_non_decorative_templates_are_not_fake_doors(self):
        chunk = self.document["Data"]["RootChunk"]
        chunk["nodes"][-1]["Data"]["$type"] = "worldEntityProxyMeshNode"
        chunk["nodes"][-2]["Data"]["entityTemplate"]["DepotPath"]["$value"] = r"base\gameplay\devices\doors\final\single_door_hinged.ent"
        self.file.write_text(json.dumps(self.document), encoding="utf-8")
        self.assertFalse(any(r["category"] == "fake_door" for r in extract_sector(self.file, self.file.name, self.config)))

    def test_unchanged_sector_features_do_not_cascade_away_queue_state(self):
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        row = self.connection.execute("SELECT * FROM places WHERE category='fake_door' LIMIT 1").fetchone()
        before = [tuple(r) for r in self.connection.execute("SELECT feature_pk,feature_id FROM features ORDER BY feature_id")]
        with transaction(self.connection):
            self.connection.execute("UPDATE places SET queue_status='failed',failure_code='fixture' WHERE location_id=?", (row["location_id"],))
        changed = {**self.config, "extraction_rule_version": "cache-refresh-only"}
        index_sectors(self.connection, self.source, changed)
        self.assertEqual(before, [tuple(r) for r in self.connection.execute("SELECT feature_pk,feature_id FROM features ORDER BY feature_id")])
        retained = self.connection.execute("SELECT queue_status,failure_code FROM places WHERE location_id=?", (row["location_id"],)).fetchone()
        self.assertEqual(tuple(retained), ("failed", "fixture"))

    def test_scoped_door_planning_preserves_every_other_category_including_legacy_captures(self):
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        with transaction(self.connection):
            self.connection.execute("UPDATE places SET queue_status='captured',anchor_feature_id=NULL WHERE category='vending_machine'")
        before = [tuple(r) for r in self.connection.execute("SELECT * FROM places WHERE category!='fake_door' ORDER BY location_id")]
        self.assertTrue(before)
        result = plan_locations(self.connection, self.config, category="fake_door")
        self.assertEqual(result["fake_door_places"], 4)
        self.assertEqual(before, [tuple(r) for r in self.connection.execute("SELECT * FROM places WHERE category!='fake_door' ORDER BY location_id")])

    def test_fake_garage_template_joins_pairs_without_including_functional_shutters(self):
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config, category="fake_door")
        original_ids = {r[0] for r in self.connection.execute("SELECT location_id FROM places WHERE category='fake_door'")}
        chunk = self.document["Data"]["RootChunk"]
        for template in (
            r"base\gameplay\devices\doors\final\gate_decorative.ent",
            r"base\gameplay\devices\doors\gates\mall_shutter_w300_h250.ent",
        ):
            index = len(chunk["nodes"])
            chunk["nodes"].append({"Data": {"$type": "worldEntityNode", "entityTemplate": {"DepotPath": {"$value": template}}}})
            chunk["nodeData"]["Data"].append({"NodeIndex": index, "Id": f"garage-{index}", "Position": {"X": 40, "Y": 40, "Z": 0}, "Orientation": {"i": 0, "j": 0, "k": 0, "r": 1}})
        self.file.write_text(json.dumps(self.document), encoding="utf-8")
        index_sectors(self.connection, self.source, self.config)
        result = plan_locations(self.connection, self.config, category="fake_door")
        self.assertEqual(result["fake_door_pairs"], 3)
        self.assertEqual(result["fake_door_places"], 6)
        self.assertTrue(original_ids <= {r[0] for r in self.connection.execute("SELECT location_id FROM places WHERE category='fake_door'")})
        garage = self.connection.execute("SELECT * FROM features WHERE rule_id='fake_garage_door_v1'").fetchall()
        self.assertEqual(len(garage), 1)
        self.assertIn("fake-garage-door", garage[0]["tags"])
        views = self.connection.execute("SELECT * FROM places WHERE anchor_feature_id=?", (garage[0]["feature_id"],)).fetchall()
        self.assertEqual({r["direction"] for r in views}, {"outward", "building"})
        self.assertEqual(len({json.loads(r["provenance_json"])["capture_pair_id"] for r in views}), 1)
        self.assertEqual({json.loads(r["provenance_json"])["door_kind"] for r in views}, {"garage_gate"})

    def test_invalid_view_distances_fail_before_planning_mutates_the_queue(self):
        for distance in (0, -1, float("nan"), float("inf"), True):
            config = copy.deepcopy(self.config)
            config["fake_door_rules"]["building_distance_m"] = distance
            with self.subTest(distance=distance), self.assertRaises(ValueError):
                validate_planning_config(config)
        self.config["fake_door_rules"]["building_distance_m"] = 1
        with self.assertRaisesRegex(ValueError, "must exceed"):
            validate_planning_config(self.config)


if __name__ == "__main__":
    unittest.main()
