"""Measured double-door replacement and scaled collision survey contracts."""
import struct
import sys
from pathlib import Path
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from building_retrofit import collision_actor_scale, validate_retrofit
from building_features import DOOR_PRESETS, DOOR_CONTROLLER_CRUID, DOOR_OFFMESH_CRUID


class AllenRetrofitTests(unittest.TestCase):
    def validate_node(self, node, deletion):
        root = {'nodes': [{'Data': node}], 'nodeData': {'Data': [{'NodeIndex': 0}]}}
        entry = {'path': r'base\worlds\03_night_city\_compiled\default\test.streamingsector',
                 'source': 'unused', 'sha256': 'unused', 'expectedNodes': 1,
                 'nodeDeletions': [{'index': 0, 'type': node['$type'], **deletion}]}
        with patch('building_retrofit._source', return_value=root):
            return validate_retrofit({'retrofit': {'sectors': [entry]}})

    def test_double_decorative_entity_requires_matching_template(self):
        template = r'base\gameplay\devices\doors\final\double_door_decorative.ent'
        node = {'$type': 'worldEntityNode', 'entityTemplate': {'DepotPath': {'$value': template}}}
        self.validate_node(node, {'expectedTemplate': template})
        with self.assertRaises(ValueError):
            self.validate_node(node, {'expectedTemplate': template.replace('decorative', 'hinged')})

    def test_generic_door_proxy_requires_exact_mesh_and_door_name(self):
        mesh = r'base\worlds\03_night_city\sectors\_external\proxy\2635890516\kitsch_f.mesh'
        node = {'$type': 'worldGenericProxyMeshNode', 'debugName': {'$value': 'double_door_sliding_f_ProxyMesh'},
                'mesh': {'DepotPath': {'$value': mesh}}}
        self.validate_node(node, {'expectedMesh': mesh})
        with self.assertRaises(ValueError):
            self.validate_node(node, {'expectedMesh': 'different.mesh'})
        node['debugName']['$value'] = 'street_mesh_ProxyMesh'
        with self.assertRaises(ValueError):
            self.validate_node(node, {'expectedMesh': mesh})

    def test_actor_scale_follows_positions_and_rotations_in_auxiliary_buffer(self):
        raw = bytearray(48 + 32 + 12 + 16 + 24)
        struct.pack_into('<h', raw, 36, 1)
        struct.pack_into('<3f', raw, 48+32+12+16+12, 9, 10.5, 2)
        node = {'numActors': 1, 'numShapeInfos': 1, 'numShapePositions': 1, 'numShapeRotations': 1, 'numScales': 2}
        self.assertEqual(collision_actor_scale(node, raw, 0), [9, 10.5, 2])
        struct.pack_into('<h', raw, 36, -1)
        self.assertEqual(collision_actor_scale(node, raw, 0), [1, 1, 1])
        struct.pack_into('<h', raw, 36, 2)
        with self.assertRaises(ValueError):
            collision_actor_scale(node, raw, 0)

    def test_native_double_door_uses_measured_controller_identity(self):
        template, appearance, offset = DOOR_PRESETS['sliding_kitsch_double_f']
        self.assertTrue(template.endswith(r'final\double_door.ent'))
        self.assertEqual(appearance, 'doors_double_kitsch_f')
        self.assertEqual(offset, 0)
        self.assertEqual(DOOR_CONTROLLER_CRUID, '1193887807258071040')
        self.assertEqual(DOOR_OFFMESH_CRUID, '1455904520967634944')

    def test_destructible_clutter_requires_pinned_mesh_and_valid_instance(self):
        mesh = r'base\environment\decoration\containers\packaging\foam_box\foam_box_a_lid_a.mesh'
        node = {'$type': 'worldInstancedDestructibleMeshNode',
                'mesh': {'DepotPath': {'$value': mesh}}, 'cookedInstanceTransforms': {'numElements': 3}}
        selection = dict(expectedMesh=mesh, expectedInstances=3, instanceDeletions=[1])
        clean = self.validate_node(node, selection)[0]['nodeDeletions'][0]
        self.assertEqual(clean['instanceDeletions'], [1])
        for wrong in [dict(expectedMesh='other.mesh'), dict(expectedInstances=2), dict(instanceDeletions=[3])]:
            with self.assertRaises(ValueError):
                self.validate_node(node, {**selection, **wrong})

    def test_closed_ceiling_backs_keep_stair_apertures_clear(self):
        from building_builder import compile_layout
        layout = dict(schema_version=1, id='closed-ceiling-test', name='Closed ceiling', kit='common-3m',
                      rooms=[dict(id='lower',name='Lower',x=0,y=0,width=9,depth=12,level=0),
                             dict(id='upper',name='Upper',x=0,y=0,width=9,depth=12,level=1)],
                      stairs=[dict(id='stair',type='return',level=0,x=3,y=3,width=2.6,
                                   flight_width=1.2,run=4.5,landing=1.5,enclosed=True)],
                      close_ceiling_slabs=True)
        scene=compile_layout(layout)
        ceilings=[i for i in scene['instances'] if i['role']=='ceiling' and i['id'].startswith('tile:')]
        caps={i['id']:i for i in scene['instances'] if i['id'].endswith(':ceiling:top') or ':ceiling:' in i['id'] and i['id'].endswith(':top')}
        self.assertEqual(len(caps),len(ceilings))
        for ceiling in ceilings:
            cap=caps[ceiling['id']+':top']
            self.assertEqual(cap['level'],ceiling['level'])
            self.assertAlmostEqual(cap['position'][2],ceiling['position'][2]+ceiling['scale'][2]*.1)
        self.assertTrue(any(s['id'].endswith(':enclosure:right') for s in scene['solids']))
        self.assertFalse(any(s['id'].startswith('corner:') for s in scene['solids']))
        front=next(s for s in scene['solids'] if s['id']=='guard:stair:front')
        centre=next(s for s in scene['solids'] if s['id']=='guard:stair:centre:upper')
        self.assertAlmostEqual(front['center'][0]+front['size'][0]/2,
                               centre['center'][0]+centre['size'][0]/2)
        self.assertAlmostEqual(front['center'][1]-front['size'][1]/2,
                               centre['center'][1]+centre['size'][1]/2)
        left = next(s for s in scene['solids'] if s['id']=='guard:stair:upper:0')
        self.assertAlmostEqual(front['center'][0]-front['size'][0]/2,
                               left['center'][0]-left['size'][0]/2)
        enclosure = next(s for s in scene['solids'] if s['id']=='guard:stair:enclosure:front')
        right = next(s for s in scene['solids'] if s['id']=='guard:stair:enclosure:right')
        self.assertAlmostEqual(enclosure['center'][0]+enclosure['size'][0]/2,
                               right['center'][0]+right['size'][0]/2)
        def covers(solid, x, y):
            return all(abs(p-c) < size/2-1e-6 for p,c,size in zip((x,y),solid['center'],solid['size']))
        # The ceiling closes beneath the guard; the upper walkable floor still
        # excludes its footprint and the actual shaft remains open.
        self.assertTrue(any(covers(s,3.6,7.56) for s in scene['solids'] if s['role']=='ceiling' and s['level']==0))
        self.assertFalse(any(covers(s,3.6,7.56) for s in scene['solids'] if s['role']=='floor' and s['level']==1))
        self.assertFalse(any(covers(s,3.6,7.4) for s in scene['solids'] if s['role']=='ceiling' and s['level']==0))
        layout['stairs'][0]['wall_side']='right'
        layout['stairs'][0]['wall_back']=True
        fitted=compile_layout(layout)
        self.assertFalse(any(s['id'] in ('guard:stair:enclosure:right','guard:stair:upper:1') for s in fitted['solids']))
        self.assertFalse(any(s['id']=='guard:stair:back' for s in fitted['solids']))
        self.assertTrue(any(s['id']=='guard:stair:back' for s in scene['solids']))

    def test_stacked_common_walls_close_the_slab_gap_with_matching_collision(self):
        from building_builder import compile_layout
        layout = dict(schema_version=1, id='stacked-wall-test', name='Stacked walls', kit='common-3m',
                      storey_height=4, rooms=[dict(id=f'room-{i}', name='Room', x=0, y=0,
                                                  width=3, depth=3, level=i) for i in range(3)])
        original = compile_layout(layout)
        layout['join_storey_walls'] = True
        scene = compile_layout(layout)
        for level in (0, 1):
            key = f'{level}:x:0:0'
            wall = next(v for v in scene['instances'] if v['id'] == 'wall:' + key)
            collider = next(v for v in scene['solids'] if v['id'] == 'wall:' + key + ':0')
            render_top = wall['position'][2] + 3.8 * wall['scale'][2]
            self.assertAlmostEqual(render_top, (level + 1) * 4)
            self.assertAlmostEqual(collider['center'][2] + collider['size'][2] / 2, render_top)
        top = next(v for v in scene['instances'] if v['id'] == 'wall:2:x:0:0')
        self.assertEqual(top['scale'][2], 1)
        old = next(v for v in original['instances'] if v['id'] == 'wall:1:x:0:0')
        self.assertAlmostEqual(old['position'][2] + 3.8 * old['scale'][2], 7.8)

    def test_solid_end_extensions_fit_both_facings_and_collision(self):
        from building_builder import compile_layout, BuildingError
        layout = dict(schema_version=1, id='end-join-test', name='End join', kit='common-3m',
                      rooms=[dict(id='a', name='A', x=0, y=0, width=3, depth=3),
                             dict(id='b', name='B', x=0, y=3, width=3, depth=3)],
                      wall_extensions={'0:x:0:1': {'start': .2, 'end': .1}})
        scene = compile_layout(layout)
        faces = [v for v in scene['instances'] if v.get('edge') == '0:x:0:1']
        self.assertEqual(len(faces), 2)
        import math
        for face in faces:
            # Nominal native endpoints, excluding the small trim/end lap.
            a = math.radians(face['yaw'])
            left = face['position'][0] - 3 * face['scale'][0] * math.cos(a)
            right = face['position'][0]
            self.assertAlmostEqual(min(left, right), -.201)
            self.assertAlmostEqual(max(left, right), 3.101)
        collider = next(v for v in scene['solids'] if v.get('edge') == '0:x:0:1')
        self.assertAlmostEqual(collider['center'][0] - collider['size'][0]/2, -.2)
        self.assertAlmostEqual(collider['center'][0] + collider['size'][0]/2, 3.1)
        layout['openings'] = {'0:x:0:1': 'doorway'}
        with self.assertRaises(BuildingError):
            compile_layout(layout)

    def test_wall_hugging_return_stairs_keep_both_floor_connections(self):
        from building_builder import compile_layout
        from building_navigation import route
        from building_return_stairs import flight_edges
        stairs = [dict(id='lower', type='return', level=0, x=3.2, y=4.8, width=2.8,
                       flight_width=1.2, run=4.7, landing=1.6, railings=True, enclosed=True,
                       wall_side='left', wall_back=True),
                  dict(id='upper', type='return', level=1, x=6.2, y=4.8, width=2.6,
                       flight_width=1.2, run=4.55, landing=1.6, railings=True, enclosed=True,
                       wall_side='right', wall_back=True)]
        layout = dict(schema_version=1, id='stair-join-test', name='Stair joins', kit='common-3m',
                      storey_height=4, stairs=stairs,
                      rooms=[dict(id=f'floor-{i}', name='Floor', x=3, y=3, width=6, depth=12,
                                  level=i) for i in range(3)])
        scene = compile_layout(layout)
        self.assertEqual(scene['navigation']['stats']['islands'], 1)
        self.assertTrue(route(scene['navigation'], [8, 13, 0], [8, 13, 8])['reachable'])
        self.assertAlmostEqual(flight_edges(stairs[0], .3, .03)[0], 3.53)
        solids = {v['id']: v for v in scene['solids']}
        self.assertNotIn('guard:lower:upper:0', solids)
        for stair in stairs:
            self.assertNotIn(f"guard:{stair['id']}:back", solids)
            turn = solids[f"stair:{stair['id']}:turn"]
            self.assertAlmostEqual(turn['center'][1] - turn['size'][1]/2, 3.2)
        a, b = solids['guard:lower:upper:1'], solids['guard:upper:enclosure:left']
        # Adjacent storeys share a single partition face. The lower guard
        # stops under the upper enclosure instead of showing a short ledge.
        self.assertAlmostEqual(a['center'][0], b['center'][0])
        self.assertAlmostEqual(a['size'][0], .2)
        self.assertAlmostEqual(a['size'][0], b['size'][0])
        self.assertAlmostEqual(a['center'][2]+a['size'][2]/2,
                               b['center'][2]-b['size'][2]/2)
        self.assertAlmostEqual(a['center'][1]+a['size'][1]/2,
                               b['center'][1]+b['size'][1]/2)
        tail=solids['guard:lower:upper:1:front']
        self.assertAlmostEqual(tail['center'][1]-tail['size'][1]/2,9.35)
        self.assertAlmostEqual(tail['center'][1]+tail['size'][1]/2,9.5)
        # No guard occupies either flight's clear width.
        self.assertAlmostEqual(b['center'][0]-b['size'][0]/2,6)
        self.assertAlmostEqual(b['center'][0]+b['size'][0]/2,6.2)
        # No slab edge may lie on the grey wall face beside either flight.
        # Remove the strip inside that wall while preserving the walking floor.
        for level, x in [(1,3.1),(2,8.9)]:
            self.assertFalse(any(s['role']=='floor' and s['level']==level
                and abs(x-s['center'][0])<s['size'][0]/2-1e-6
                and abs(6-s['center'][1])<s['size'][1]/2-1e-6
                for s in scene['solids']))
        layout['openings']={'2:y:3:3':'passage'}
        passage=compile_layout(layout)
        self.assertTrue(any(s['role']=='floor' and s['level']==2
            and abs(8.9-s['center'][0])<s['size'][0]/2-1e-6
            and abs(9.2-s['center'][1])<s['size'][1]/2-1e-6
            for s in passage['solids']))

    def test_common_wall_faces_meet_at_t_junction_without_corner_columns(self):
        from building_builder import compile_layout
        layout=dict(schema_version=1,id='wall-join-test',name='Wall join',kit='common-3m',
                    rooms=[dict(id='west',name='West',x=0,y=0,width=3,depth=6),
                           dict(id='south',name='South',x=3,y=0,width=3,depth=3),
                           dict(id='north',name='North',x=3,y=3,width=3,depth=3)])
        scene=compile_layout(layout)
        faces={i['id']:i for i in scene['instances']}
        west=faces['wall:0:y:1:1:reverse']
        south=faces['wall:0:x:1:1:reverse']
        # Native wall's main decorated plane is Y=.20, normal +Y. The
        # opposing skins must meet at the nominal room corner (3,3).
        self.assertAlmostEqual(west['position'][0]+.20,3)
        self.assertAlmostEqual(south['position'][1]+.20,3)
        # End overlap spans the corner on both sides, without a separate strip.
        self.assertLess(south['position'][0]-3*south['scale'][0],3)
        self.assertGreater(south['position'][0]-3*south['scale'][0],2.998)
        self.assertEqual(scene['kit']['wall_thickness'],.23)
        self.assertFalse(any(i['id'].startswith('corner:') for i in scene['instances']))


if __name__ == '__main__':
    unittest.main()
