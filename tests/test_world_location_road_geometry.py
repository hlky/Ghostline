"""Geometry regressions for baked road curves and their calibration queue."""

import copy
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from world_locations.database import connect
from world_locations.config import load_config
from world_locations.model import Vec3, interpolate_polyline
from world_locations.planning import plan_locations
from world_locations.road_geometry import deformation_centerline, deformation_tangent, rebuild_deformed_roads


def road_node():
    return {
        "$type": "worldBendedMeshNode", "isBendedRoad": True,
        "mesh": {"DepotPath": {"$value": r"base\road_meshes\bended\br_street.mesh"}},
        "deformedBox": {"Min": {"X": 0, "Y": 0, "Z": 0}, "Max": {"X": 25, "Y": 35, "Z": 5}},
        "deformationData": [
            {"W": {"X": x, "Y": y, "Z": z, "W": 1}, "Y": {"X": tx, "Y": ty, "Z": 0}}
            for x, y, z, tx, ty in [(10, 20, 1, 1, 1), (15, 25, 2, 1, .8), (20, 28, 3, 1, .6)]
        ],
    }


def road_instance():
    return {
        "NodeIndex": 0, "Position": {"X": 100, "Y": 200, "Z": 30},
        "Orientation": {"i": 0, "j": 0, "k": math.sqrt(.5), "r": math.sqrt(.5)},
        "Scale": {"X": 2, "Y": 3, "Z": 4},
    }


class DeformedRoadTests(unittest.TestCase):
    def test_station_world_transform_includes_local_offset_scale_and_rotation(self):
        points, tangents = deformation_centerline(road_node(), road_instance())
        for actual, expected in zip(points, [Vec3(40, 220, 34), Vec3(25, 230, 38), Vec3(16, 240, 42)]):
            self.assertLess((actual - expected).length(), 1e-8)
        expected_tangent = Vec3(-3, 2, 0).normalized()
        self.assertLess((tangents[0] - expected_tangent).length(), 1e-8)
        # The station curve is far from the old instance/proxy origin.
        midpoint, _ = interpolate_polyline(points, (points[1]-points[0]).length())
        self.assertLess((midpoint-points[1]).length(), 1e-8)
        self.assertGreater(midpoint.distance_2d(Vec3(100, 200, 30)), 70)

    def test_heading_uses_native_tangents_instead_of_long_chord(self):
        points = [Vec3(0, 0, 0), Vec3(5, 10, 0)]
        tangents = [Vec3(0, 1, 0), Vec3(1, 0, 0)]
        actual = deformation_tangent(points, tangents, (points[1]-points[0]).length()/2)
        self.assertLess((actual-Vec3(1, 1, 0).normalized()).length(), 1e-8)

    def test_invalid_deformation_is_rejected_instead_of_falling_back_to_origin(self):
        for mutate in (
            lambda n: n['deformationData'][0]['W'].update(X=float('nan')),
            lambda n: n['deformationData'][0]['W'].update(X=1000),
            lambda n: n['deformationData'][0]['Y'].update(X=-1, Y=-1),
            lambda n: n['deformationData'][0]['W'].pop('Z'),
        ):
            node = road_node()
            mutate(node)
            with self.assertRaises((ValueError, KeyError)):
                deformation_centerline(node, road_instance())

    def test_rebuild_keeps_instances_separate_and_excludes_cables_and_metro(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            street = road_node()
            metro = copy.deepcopy(street)
            metro['mesh']['DepotPath']['$value'] = r'base\road_meshes\bended\br_metro.mesh'
            cable = copy.deepcopy(street)
            cable['isBendedRoad'] = False
            instances = [road_instance(), road_instance(), road_instance(), road_instance()]
            instances[1]['Position']['X'] += 500
            instances[2]['NodeIndex'] = 1
            instances[3]['NodeIndex'] = 2
            document = {'Data': {'RootChunk': {'nodes': [{'Data': n} for n in [street, metro, cable]], 'nodeData': {'Data': instances}}}}
            (root/'test.streamingsector.json').write_text(json.dumps(document))
            connection = connect(root/'test.sqlite3')
            try:
                result = rebuild_deformed_roads(connection, root, 'test')
                self.assertEqual(result['roads'], 2)
                self.assertFalse(result['rejected'])
                lengths = [r[0] for r in connection.execute('SELECT length_m FROM roads')]
                self.assertTrue(all(length < 40 for length in lengths))
                self.assertEqual(connection.execute('SELECT count(*) FROM features').fetchone()[0], 0)
                selected = connection.execute('SELECT road_id FROM roads ORDER BY road_id LIMIT 1').fetchone()[0]
                config = load_config()
                config['scope_rules'] = []
                config['hazard_rules'] = []
                config['road_rules']['geometry_source'] = 'bended_deformation'
                config['workspace'] = {'require_road_calibration': True, 'calibration_capture_road_ids': [selected]}
                for _ in range(2):
                    plan_locations(connection, config, category='road')
                    views = list(connection.execute('SELECT * FROM places'))
                    self.assertEqual(len(views), 2)
                    self.assertTrue(all(v['queue_status'] == 'pending' and v['review_status'] == 'needs_calibration' for v in views))
                    provenance = [json.loads(v['provenance_json']) for v in views]
                    self.assertEqual(provenance[0]['capture_pair_id'], provenance[1]['capture_pair_id'])
                    self.assertEqual(provenance[0]['paired_location_id'], views[1]['location_id'])
                    self.assertEqual(provenance[0]['geometry_status'], 'awaiting_in_game_review')
                    self.assertAlmostEqual((views[0]['requested_yaw']-views[1]['requested_yaw']) % 360, 180)
                # Expanding the category uses spacing across segment boundaries,
                # retains opposing views together, and releases calibration holds.
                config['workspace'] = {'require_road_calibration': False, 'deformation_method_validated': True}
                config['road_rules']['global_minimum_separation_m'] = 600
                plan_locations(connection, config, category='road')
                pending = list(connection.execute("SELECT * FROM places WHERE queue_status='pending'"))
                self.assertEqual(len(pending), 2)
                self.assertEqual({v['direction'] for v in pending}, {'along', 'against'})
                self.assertTrue(all(v['review_status'] != 'needs_calibration' for v in pending))
            finally:
                connection.close()
