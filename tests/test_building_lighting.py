"""Practical light placement must survive world anchoring and reject bad input."""
import copy
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from building_builder import world_point
from building_lighting import compile_lights, light_node
from generate_world import HandleAllocator, cname


class PracticalLightingTests(unittest.TestCase):
    def scene(self):
        return {'layout': {'origin': {'x': 20, 'y': 40, 'z': 3, 'yaw': 90},
                           'lights': [{'id': 'ceiling', 'position': [2, 5, 7.4],
                                       'color': [255, 224, 190], 'radius': 4, 'intensity': 32}]}}

    def test_light_uses_same_world_anchor_as_its_fixture(self):
        scene = self.scene()
        compile_lights(scene, world_point)
        light = scene['lights'][0]
        for actual, expected in zip(light['world_position'], [15, 42, 10.4]):
            self.assertAlmostEqual(actual, expected)
        node = light_node(light, HandleAllocator(), cname)['Data']
        self.assertEqual(node['$type'], 'worldStaticLightNode')
        self.assertEqual(node['color']['Green'], 224)
        self.assertEqual(node['radius'], 4)
        self.assertEqual(node['intensity'], 32)

    def test_rejects_invalid_or_ambiguous_light_specs(self):
        for change in ({'color': [255, -1, 4]}, {'intensity': float('nan')},
                       {'radius': 100}, {'position': [1, 2]}, {'id': 'bad id'}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                scene = self.scene()
                scene['layout']['lights'][0].update(change)
                compile_lights(scene, world_point)
        scene = self.scene()
        scene['layout']['lights'].append(copy.deepcopy(scene['layout']['lights'][0]))
        with self.assertRaises(ValueError):
            compile_lights(scene, world_point)
