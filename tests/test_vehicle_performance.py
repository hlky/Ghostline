"""Focused checks for configured speed and RED curve evaluation."""
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from vehicle_performance import HUD_RESOURCE, evaluate_curve, performance_stats, speed_values


def curve(points, kind='BezierCubic'):
    return {'InterpolationType': kind, 'Elements': [{'Point': x, 'Value': y} for x, y in points]}


class VehiclePerformanceTests(unittest.TestCase):
    def test_bezier_solves_time_axis_instead_of_treating_handles_as_samples(self):
        nonlinear = curve([(0, 0), (0, 1 / 3), (0, 2 / 3), (1, 1)])
        # x=t^3 and y=t. At x=1/8 the value is 1/2, not 1/8.
        self.assertAlmostEqual(evaluate_curve(nonlinear, .125), .5)
        self.assertEqual(evaluate_curve(nonlinear, -1), 0)
        self.assertEqual(evaluate_curve(nonlinear, 2), 1)

    def test_multiple_segments_and_exact_knot(self):
        value = curve([(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 3)])
        self.assertAlmostEqual(evaluate_curve(value, 1.5), 1.5)
        self.assertAlmostEqual(evaluate_curve(value, 3), 3)
        self.assertAlmostEqual(evaluate_curve(value, 5), 3)

    def test_linear_and_constant_boundaries(self):
        self.assertAlmostEqual(evaluate_curve(curve([(0, 0), (2, 4)], 'Linear'), 1), 2)
        values = curve([(0, 1), (1, 2), (2, 3)], 'Constant')
        self.assertEqual(evaluate_curve(values, .5), 1)
        self.assertEqual(evaluate_curve(values, 1), 2)

    def test_caliburn_gear_ceiling_uses_distinct_world_and_hud_conversions(self):
        hud = curve([(0, 4.6), (30, 4.6), (60, 4.6), (100, 4.6)])
        values = speed_values(45, hud)
        self.assertAlmostEqual(values['mph'], 100.66213314244808)
        self.assertEqual(values['kmh'], 162)
        self.assertAlmostEqual(values['hud_mph'], 207)
        self.assertAlmostEqual(values['hud_kmh'], 333.13338)

    def test_reverse_is_excluded_and_all_gears_get_converted(self):
        hud = curve([(0, 4), (30, 4), (60, 4), (100, 4)])
        torque = curve([(0, .5), (.3, 1), (.6, 1), (1, .9)])
        data = {'curves': {HUD_RESOURCE: {'speed_to_multiplier': hud}, 'engine.curveset': {'1': torque}}}
        result = performance_stats({'gearCurvesPath': 'engine.curveset'},
                                   [{'maxSpeed': 99}, {'maxSpeed': 20}, {'maxSpeed': 30}], data)
        self.assertEqual(result['gear_index'], 2)
        self.assertEqual(result['top_speed_mps'], 30)
        self.assertAlmostEqual(result['hud_top_speed_mph'], 120)
        self.assertTrue(result['gears'][0]['reverse'])
        self.assertEqual(result['torque_curve_at_normalized_rpm_1'], {'1': .9})

    def test_missing_or_invalid_inputs_do_not_invent_speed(self):
        for value in (None, float('nan'), float('inf'), -1, True):
            self.assertIsNone(speed_values(value)['mps'])
        result = performance_stats({}, [{'maxSpeed': 100}])
        self.assertIsNone(result['top_speed_mph'])
        self.assertIsNone(result['hud_top_speed_mph'])
        result = performance_stats({}, [{'maxSpeed': 10}, {'maxSpeed': 20}])
        self.assertIsNotNone(result['top_speed_mph'])
        self.assertIsNone(result['hud_top_speed_mph'])

    def test_malformed_and_nonmonotonic_curves_fail_explicitly(self):
        invalid = [curve([]), curve([(0, 0), (1, 1)]),
                   curve([(0, 0), (2, 1), (1, 1), (3, 1)]),
                   curve([(0, 0), (1, math.inf)], 'Linear'), curve([(0, 0)], 'Unknown')]
        for value in invalid:
            with self.subTest(curve=value), self.assertRaises(ValueError):
                evaluate_curve(value, 0)


if __name__ == '__main__':
    unittest.main()
