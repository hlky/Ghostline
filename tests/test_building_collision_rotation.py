"""Retained tilted geometry and its replacement boxes share world rotation."""
import base64
import math
import struct
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from building_builder import compile_layout, collision_node, BuildingError


class RotatedCollisionTests(unittest.TestCase):
    def layout(self):
        return dict(schema_version=1, id='tilted-box', name='Tilted box', kit='common-3m',
                    origin=dict(x=10, y=20, z=3, yaw=30),
                    rooms=[dict(id='room', name='Room', x=0, y=0, width=3, depth=3)],
                    shell_blockers=[dict(center=[5, 1, .2], size=[2, 3, .2],
                                         rotation=[0, math.sin(.1), 0, math.cos(.1)])])

    def test_cooked_box_preserves_tilt_and_origin_yaw(self):
        scene = compile_layout(self.layout())
        box = next(v for v in scene['solids'] if v['id'] == 'shell:blocker:0')
        node = collision_node(box, 1)
        data = base64.b64decode(node['compiledData']['Bytes'])
        expected = [-math.sin(math.pi/12)*math.sin(.1), math.cos(math.pi/12)*math.sin(.1),
                    math.sin(math.pi/12)*math.cos(.1), math.cos(math.pi/12)*math.cos(.1)]
        for actual, value in zip(struct.unpack_from('<4f', data, 16), expected):
            self.assertAlmostEqual(actual, value, places=7)
        for actual, value in zip(struct.unpack_from('<3i', data), box['world_center']):
            self.assertLess(abs(actual/131072-value), 1/131072)
        self.assertEqual(struct.unpack_from('<3f', data, 48)[:2], (1, 1.5))

    def test_invalid_collision_rotation_is_rejected(self):
        for rotation in ([0, 0, 0, 2], [0, 0, 0], [0, float('nan'), 0, 1]):
            with self.subTest(rotation=rotation), self.assertRaises(BuildingError):
                layout = self.layout()
                layout['shell_blockers'][0]['rotation'] = rotation
                compile_layout(layout)
