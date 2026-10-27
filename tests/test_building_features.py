"""Stairs, device gates, native tiles and entrance patch regression contracts."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from building_builder import BuildingError, collision_node, compile_layout, export_project, kits
from building_navigation import navigation_resource, route
from building_retrofit import survey, survey_nearby, validate_retrofit
from package_manifest import PackageError, filter_registration, minimum_archive_version
from world_location_nav import load_navigation_sector


class BuildingFeatureTests(unittest.TestCase):
    def test_akpp_entrance_matches_survey_and_preserves_ru_lai_boundary(self):
        from building_builder import native_documents
        layout=json.loads((ROOT/'projects/experiments/building-lab/buildings/akpp-logistics-open-shell.building.json').read_bytes())
        scene=compile_layout(layout)
        self.assertEqual(len(scene['doors']),1)
        door=scene['doors'][0]
        self.assertEqual(door['appearance'],'doors_single_hinged_e')
        self.assertEqual(door['mode'],'INTERACTIVE')
        for actual,expected in zip(door['world_position'],[-1106.8994140625,1377.3619384765625,5.859007835388184+1311/131072]):
            self.assertAlmostEqual(actual,expected)
        deletions=[d for patch in scene['retrofit_patches'] for d in patch['nodeDeletions']]
        self.assertEqual([d['index'] for d in deletions if d['type']=='worldStaticMeshNode'],[4738,4739,4362,4741])
        self.assertEqual({d['index']:d['actorDeletions'] for d in deletions if d['type']=='worldCollisionNode'},
                         {3579:[48],3526:[22],3581:[121]})
        self.assertFalse(any(d['index']==3536 for d in deletions))
        sector,_,_=native_documents(scene,ROOT/'.tmp/akpp-door-test')
        nodes=[n['Data'] for n in sector['Data']['RootChunk']['nodes']]
        self.assertEqual(sum(n['$type']=='worldDeviceNode' for n in nodes),1)
        self.assertEqual([n.get('debugName',{}).get('$value') for n in nodes
                          if n.get('debugName',{}).get('$value','').startswith('module:shell-')],['module:shell-4362'])
        self.assertTrue(route(scene['navigation'],[3,3,0],door['endpoints'][1])['reachable'])

    def test_akpp_lining_closes_facade_backs_but_keeps_door_route(self):
        import math
        layout=json.loads((ROOT/'projects/experiments/building-lab/buildings/akpp-logistics-open-shell.building.json').read_bytes())
        scene=compile_layout(layout)
        # Every liner has both visible facings; neither can disappear just
        # because the camera crossed the original exterior shell plane.
        faces=[i for i in scene['instances'] if i['id'].startswith('shell:liner:')]
        self.assertEqual(len(faces),16)  # five full walls plus three aperture pieces
        for face in faces:
            self.assertEqual(face['mesh'],scene['kit']['pieces']['wall']['mesh'])
            self.assertAlmostEqual(face['position'][2],0 if ':3:1' not in face['id'] else 2.48)
        solids=[v for v in scene['solids'] if v['id'].startswith('shell:liner:')]
        def contains(v,p):
            angle=math.radians(-v['yaw']);dx=p[0]-v['center'][0];dy=p[1]-v['center'][1]
            q=[dx*math.cos(angle)-dy*math.sin(angle),dx*math.sin(angle)+dy*math.cos(angle),p[2]-v['center'][2]]
            return all(abs(a)<b/2+1e-6 for a,b in zip(q,v['size']))
        # Probe backs of the north/south/rear facades and the top doorway band.
        for point in ([2,.35,1.7],[2,5.65,1.7],[.35,3,1.7],[4,2,1.7],[4,3.9,3]):
            self.assertTrue(any(contains(v,point) for v in solids),point)
        # The fixed casing spans Y=centre +/- .75. Lining overlaps it
        # by 5 cm on either side, hiding the original yellow return behind.
        centre=layout['shell_doors'][0]['from'][1]
        self.assertAlmostEqual(layout['shell_liners'][3]['openings'][0]['width'],1.4)
        self.assertAlmostEqual(layout['shell_liners'][3]['openings'][0]['height'],2.48)
        for liner in layout['shell_liners'][4:6]:
            self.assertAlmostEqual(max(liner['start'][0],liner['end'][0]),5.075)
            self.assertAlmostEqual(abs(liner['start'][1]-centre),.7)
        # Closed leaf's rear surface is X~5.089: returns stop behind it,
        # while overlapping the casing's rear surface X~5.068.
        for liner in layout['shell_liners'][4:6]:
            end=max(liner['start'][0],liner['end'][0])
            self.assertGreater(end,5.068)
            self.assertLess(end,5.089)
        # Full standing-height passage through the lining and recess remains.
        for x in [3.8,4,4.3,4.8,5.2]:
            for y in [3.4,3.9,4.4]:
                for z in [.1,1,2.3]:
                    self.assertFalse(any(contains(v,[x,y,z]) for v in solids),(x,y,z))
        door=scene['doors'][0]
        for start in ([1,1,0],[3,4,0],[3,3,0]):
            self.assertTrue(route(scene['navigation'],start,door['endpoints'][1])['reachable'],start)
        occluders=[d for p in scene['retrofit_patches'] for d in p['nodeDeletions'] if d['type']=='worldInstancedOccluderNode']
        self.assertEqual(occluders,[{'index':2521,'type':'worldInstancedOccluderNode'}])
        # Source evidence pins both AKPP matrices; Ru Lai's adjacent group is retained.
        evidence=json.loads((ROOT/'projects/experiments/building-lab/surveys/akpp-logistics-occlusion.json').read_bytes())
        self.assertEqual(evidence['count'],2)
        self.assertEqual(hashlib.sha256((ROOT/evidence['source']).read_bytes()).hexdigest(),evidence['source_sha256'])

    def test_akpp_floor_cap_covers_sidewalk_without_patching_street(self):
        layout=json.loads((ROOT/'projects/experiments/building-lab/buildings/akpp-logistics-open-shell.building.json').read_bytes())
        scene=compile_layout(layout)
        cap=next(v for v in scene['solids'] if v['id']=='shell:plinth:0')
        self.assertEqual(cap['role'],'floor')
        self.assertAlmostEqual(cap['center'][2]+cap['size'][2]/2,.05)
        # Surveyed sidewalk reaches +3.061 cm in the room; cap clears it.
        self.assertGreater(cap['center'][2]+cap['size'][2]/2,.030605+.01)
        self.assertLess(cap['center'][0]+cap['size'][0]/2,4.12)
        self.assertGreater(cap['center'][1]-cap['size'][1]/2,0)
        self.assertFalse(any('exterior_-5_5_0_2' in p['path'] for p in scene['retrofit_patches']))
        for start in ([1,1,0],[3,4,0],[3,3,0]):
            self.assertTrue(route(scene['navigation'],start,scene['doors'][0]['endpoints'][1])['reachable'])
        for field,value in [('center',[2.18,3,.125]),('size',[3.5,5.1,.25]),('center',[5.5,3,.025]),('walkable','yes')]:
            bad=copy.deepcopy(layout);bad['shell_plinths'][0][field]=value
            with self.assertRaises(ValueError):
                compile_layout(bad)

    def test_akpp_back_panel_open_in_every_lod_without_deforming_facade(self):
        import base64
        import struct
        import numpy as np
        from building_mesh_panel import open_shop_panel
        from building_wall_uv import elements
        source=json.loads((ROOT/'generated/building-editor/library/raw/f2a7565f70d74fe30f02.mesh.json').read_bytes())
        edited,report=open_shop_panel(source)
        self.assertEqual([r['lod_mask'] for r in report],[1,2,4])
        old=source['Data']['RootChunk'];new=edited['Data']['RootChunk']
        self.assertEqual(old['materialEntries'],new['materialEntries'])
        self.assertEqual(old['appearances'],new['appearances'])
        self.assertFalse(any(p.get('Data',{}).get('$type')=='meshMeshParamOccluderData' for p in new['parameters']))
        def triangles(root):
            blob=root['renderResourceBlob']['Data'];header=blob['header'];raw=base64.b64decode(blob['renderBuffer']['Bytes'])
            for chunk in header['renderChunkInfos']:
                vertex=chunk['chunkVertices'];offsets=elements(vertex['byteOffsets']);strides=elements(vertex['vertexLayout']['slotStrides'])
                points=np.array([struct.unpack_from('<3h',raw,offsets[0]+i*strides[0]) for i in range(chunk['numVertices'])])/32767
                points=points*[header['quantizationScale'][a] for a in 'XYZ']+[header['quantizationOffset'][a] for a in 'XYZ']
                start=header['indexBufferOffset']+chunk['chunkIndices'].get('teOffset',0)
                indices=np.array(struct.unpack_from('<'+'H'*chunk['numIndices'],raw,start)).reshape((-1,3))
                yield chunk,raw[start:start+chunk['numIndices']*2],points[indices]
        def covers(tris,x,z):
            for tri in tris:
                if not np.all(abs(tri[:,1]+1.654931545)<.002):continue
                a,b,c=tri[:,[0,2]]
                matrix=np.column_stack((b-a,c-a))
                if abs(np.linalg.det(matrix))<1e-8:continue
                u,v=np.linalg.solve(matrix,np.array([x,z])-a)
                if u>=0 and v>=0 and u+v<=1:return True
            return False
        for (chunk,before,old_tris),(_,after,new_tris) in zip(triangles(old),triangles(new)):
            self.assertEqual(before,after)
            selected=np.all(abs(old_tris[:,:,1]+1.654931545)<.002,axis=1)
            np.testing.assert_equal(old_tris[~selected],new_tris[~selected])
            if chunk.get('numVertices')==44:continue
            for x in (-4.5,-4,-3.3):
                self.assertTrue(covers(old_tris,x,1.2))
                self.assertFalse(covers(new_tris,x,1.2))
            self.assertTrue(covers(new_tris,-2,1.2))

    def test_resized_wall_uvs_keep_both_paint_channels_at_world_height(self):
        import base64
        import struct
        from building_wall_uv import align_document
        vertices=b''.join(struct.pack('<4h',*p,32767) for p in ((0,0,0),(32767,0,0),(0,0,32767)))
        first=b''.join(struct.pack('<ee',*uv) for uv in ((0,0),(3,0),(0,4)))
        second=b''.join(struct.pack('<ee',*uv) for uv in ((0,0),(0,3),(4,0)))
        original=vertices+first+second+struct.pack('<3H',0,1,2)
        document={'Data':{'RootChunk':{'renderResourceBlob':{'Data':{
            'renderBuffer':{'Bytes':base64.b64encode(original).decode()},
            'header':{'quantizationScale':dict(X=3,Y=1,Z=4),
                      'quantizationOffset':dict(X=0,Y=0,Z=0),'indexBufferOffset':48,
                      'renderChunkInfos':[{'numVertices':3,'numIndices':3,'chunkIndices':{},
                        'chunkVertices':{'byteOffsets':[0,24,36],'vertexLayout':{
                            'slotStrides':[8,4,4],'elements':[
                                dict(type='PT_Short4N',usage='PS_Position'),
                                dict(type='PT_Float16_2',usage='PS_TexCoord',streamIndex=1),
                                dict(type='PT_Float16_2',usage='PS_TexCoord',streamIndex=2)]}}}]}}}}}}
        baked=align_document(document,.5,1)
        data=base64.b64decode(baked['Data']['RootChunk']['renderResourceBlob']['Data']['renderBuffer']['Bytes'])
        self.assertEqual(data[:24],original[:24])
        self.assertEqual(data[48:],original[48:])
        self.assertEqual([struct.unpack_from('<ee',data,24+i*4) for i in range(3)],[(0,1),(3,1),(0,3)])
        self.assertEqual([struct.unpack_from('<ee',data,36+i*4) for i in range(3)],[(1,0),(1,3),(3,0)])

    def test_open_plan_native_windows_enclosure_and_garage_door(self):
        layout=json.loads((ROOT/'projects/experiments/building-lab/buildings/rancho-open-plan-right-stair.building.json').read_bytes())
        layout.pop('retrofit')
        scene=compile_layout(layout)
        self.assertEqual(scene['navigation']['stats']['islands'],1)
        self.assertFalse(any(v['id'].startswith('reveal:') for v in scene['instances']))
        linings=[v for v in scene['instances'] if v.get('align_wall_uv')]
        self.assertEqual(len(linings),2)
        self.assertTrue(all(v['appearance']=='plaster_blue' for v in linings))
        solids=scene['solids']
        self.assertFalse(any(':slope:' in v['id'] for v in solids))
        self.assertTrue(any(':enclosure:left' in v['id'] for v in solids))
        self.assertFalse(any(v['id']=='guard:right-return:upper:1' for v in solids))
        self.assertTrue(route(scene['navigation'],[-6,-7,-.35],[-1.5,-1.5,0])['reachable'])
        locked=copy.deepcopy(layout)
        locked.setdefault('door_states',{})['garage-back-door']='LOCKED'
        sealed=compile_layout(locked)
        self.assertFalse(route(sealed['navigation'],[-6,-7,-.35],[-1.5,-1.5,0])['reachable'])

    def test_open_plan_garage_infill_fits_unchanged_native_panel(self):
        from building_builder import native_documents, runtime_contract
        layout = json.loads((ROOT/'projects/experiments/building-lab/buildings/rancho-open-plan-right-stair.building.json').read_bytes())
        layout.pop('retrofit')
        scene = compile_layout(layout)
        door = next(d for d in scene['doors'] if d['id'] == 'garage-door')
        self.assertEqual(runtime_contract(scene)['restore_auto_close'], [door['ref']])
        self.assertFalse(door['component_scale'])
        self.assertEqual(door['scale'], [1, 1, 1])
        opening = layout['shell_rooms'][0]['walls']['south']['openings'][0]
        # Measured stock closed panel bounds; the surround sits inside them.
        self.assertLess(opening['width']/2, 1.491860270500183)
        self.assertGreater(-opening['width']/2, -1.50445556640625)
        self.assertLess(layout['shell_rooms'][0]['position'][2]+opening['height'],
                        door['position'][2]+2.659499168395996)
        sector, _, _ = native_documents(scene, ROOT/'generated/building-editor/stock-garage-test')
        node = next(n['Data'] for n in sector['Data']['RootChunk']['nodes']
                    if n['Data'].get('debugName', {}).get('$value') == door['ref'])
        chunks = node['instanceData']['Data']['buffer']['Data']['Chunks']
        self.assertEqual([c['$type'] for c in chunks], ['DoorController', 'AIOffMeshConnectionComponent'])

    def test_lower_annex_ceiling_join_closes_partial_bays_without_blocking_walkway(self):
        layout = {
            'schema_version': 1, 'id': 'ceiling-join-test', 'name': 'Ceiling join', 'kit': 'rancho-3m',
            'rooms': [dict(id='main', name='Main', x=0, y=0, width=6, depth=3,
                           level=0, ceiling_height=3.5)],
            'shell_rooms': [dict(id='annex', name='Annex', position=[2, -3, 0],
                                 width=4, depth=3, height=2.7, walls={'north': False})],
            'openings': {'0:x:0:0': 'passage', '0:x:1:0': 'passage'},
        }
        scene = compile_layout(layout)
        bands = [s for s in scene['solids'] if 'ceiling-join:' in s['id']]
        self.assertEqual(len(bands), 2)
        # Perpendicular walls need an overlapping corner, otherwise their
        # thickness is left as a visible slit on the opposite wall face.
        self.assertAlmostEqual(sum(s['size'][0] for s in bands), 4)
        for band in bands:
            self.assertAlmostEqual(band['center'][2]-band['size'][2]/2, 2.7)
            self.assertAlmostEqual(band['center'][2]+band['size'][2]/2, 3.6)
            self.assertGreaterEqual(band['center'][0]-band['size'][0]/2, 2)
        # A pre-existing full-height liner must not get coplanar infill.
        layout['shell_liners'] = [dict(start=[2, 0, 0], end=[6, 0, 0], height=3.6)]
        self.assertFalse(any('ceiling-join:' in s['id'] for s in compile_layout(layout)['solids']))
        layout.pop('shell_liners')
        layout['shell_rooms'][0]['height'] = 3.5
        self.assertFalse(any('ceiling-join:' in s['id'] for s in compile_layout(layout)['solids']))

    def test_rear_bulkhead_reaches_offset_stair_enclosure(self):
        import math
        layout=json.loads((ROOT/'projects/experiments/building-lab/buildings/rancho-open-plan-right-stair.building.json').read_bytes())
        layout.pop('retrofit')
        scene=compile_layout(layout)
        def contains(solid, point):
            dx,dy,dz=[a-b for a,b in zip(point,solid['center'])]
            angle=math.radians(solid['yaw'])
            local=[dx*math.cos(angle)+dy*math.sin(angle),-dx*math.sin(angle)+dy*math.cos(angle),dz]
            return all(abs(v)<=size/2+1e-6 for v,size in zip(local,solid['size']))
        walls=[s for s in scene['solids'] if s['role'] in ('wall','guard')]
        # Cross the previous 18 cm slit up to the outer stair face, from
        # both sides of the bulkhead, throughout its visible height.
        for x in (5.99,6.05,6.15,6.19,6.29):
            for y in (-8.99,-8.86):
                for z in (2.81,3.1,3.49):
                    self.assertTrue(any(contains(s,[x,y,z]) for s in walls),(x,y,z))
        # The bridge stays above the lower ceiling and leaves the route open.
        bridge=next(s for s in walls if s['center'][0]==6.15 and abs(s['center'][1]+8.925)<1e-6)
        self.assertAlmostEqual(bridge['center'][2]-bridge['size'][2]/2,2.7)

    def setUp(self):
        self.layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/navigation-lab.building.json").read_bytes())

    def test_rancho_reuses_original_door_and_keeps_swing_inside(self):
        import math
        from building_features import door_node
        from generate_world import HandleAllocator
        layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/rancho-retrofit.building.json").read_bytes())
        collision = next(s for s in layout["retrofit"]["sectors"] if s["path"].endswith("exterior_-2_-3_0_3.streamingsector"))
        fake_leaf = next(n for n in collision["nodeDeletions"] if n["index"] == 850)
        self.assertEqual(fake_leaf["actorDeletions"], [[123, 0]])
        # The original static leaf has its own fixed collision, separate from
        # both casing actor 17 and door-bay actor 124. It fills the aperture.
        survey_data = json.loads((ROOT / "projects/experiments/building-lab/surveys/rancho-original-door.json").read_bytes())
        low, high = survey_data["collision_replacement"]["old_fake_leaf_box"]["bounds_local"]
        self.assertTrue(low[0] < -1.5 < high[0])
        self.assertTrue(low[1] < -3.07 < high[1])
        self.assertTrue(low[2] < 1 < high[2])
        # Game-owned survey snapshots are validated by the export, not needed
        # to exercise authored geometry and native preset placement here.
        layout.pop("retrofit")
        scene = compile_layout(layout)
        self.assertEqual(set(layout["openings"]), {"0:x:-1:-1"})
        door = scene["doors"][0]
        node = door_node(door, HandleAllocator(), 90)["Data"]
        self.assertTrue(node["entityTemplate"]["DepotPath"]["$value"].endswith("single_door_hinged.ent"))
        self.assertEqual(node["appearanceName"]["$value"], "doors_single_hinged_h")
        # Native hinged_h casing is centred at hinge X=-89129/131072.
        self.assertAlmostEqual(door["position"][0] + 89129 / 131072, -1.4991345191555054)
        # Sweep the measured physical leaf bounds through the stock +90 clip.
        for degrees in range(91):
            a = math.radians(door["yaw"] + degrees)
            for x in (-1.4100682735443115 + .005, .03002822771668434 + .005):
                for y in (-.09126460552215576, .08732765167951584):
                    px = door["position"][0] + x * math.cos(a) - y * math.sin(a)
                    py = door["position"][1] + x * math.sin(a) + y * math.cos(a)
                    self.assertTrue(-3 < px < 0)
                    self.assertTrue(-3.2 < py < 0)
        header = next(s for s in scene["solids"] if s["id"] == "wall:0:x:-1:-1:2")
        self.assertAlmostEqual(header["center"][2] - header["size"][2] / 2, 2.5)
        layout["door_devices"][door["id"]]["preset"] = "unreviewed"
        with self.assertRaises(BuildingError):
            compile_layout(layout)

    def test_kits_have_distinct_measured_walls(self):
        catalogs = kits()
        self.assertTrue({"common-3m", "industrial-3m", "rancho-3m"}.issubset({k["id"] for k in catalogs}))
        self.assertEqual(len({k["pieces"]["wall"]["mesh"] for k in catalogs}), len(catalogs))
        for catalog in catalogs:
            layout = copy.deepcopy(self.layout)
            layout["kit"] = catalog["id"]
            layout["wall_appearance"] = catalog["wall_appearances"][0]
            scene = compile_layout(layout)
            self.assertTrue(any(i["mesh"] == catalog["pieces"]["wall"]["mesh"] for i in scene["instances"]))

    def test_residential_house_routes_every_room_via_retained_porch(self):
        from building_builder import runtime_contract, native_documents
        layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/rancho-residential-house.building.json").read_bytes())
        layout.pop("retrofit")
        scene = compile_layout(layout)
        self.assertEqual(scene["stats"]["area"], 287)
        self.assertEqual(scene["stats"]["rooms"], 11)
        self.assertEqual(scene["kit"]["storey_height"], 4)
        self.assertEqual(scene["stats"]["islands"], 1)
        points = runtime_contract(scene)["points"]
        for point in points[2:]:
            if point["name"] in ("Garage approach", "Rear approach"):
                continue  # These probes require the retained vanilla Human tile.
            self.assertTrue(route(scene["navigation"], points[1]["local"], point["local"])["reachable"], point["name"])
        sector, _, _ = native_documents(scene, ROOT / "generated/building-editor/house-test")
        self.assertEqual(sum(n["Data"]["$type"] == "worldStaticLightNode" for n in sector["Data"]["RootChunk"]["nodes"]), 11)
        layout["door_states"] = {"0:x:-1:0": "LOCKED"}
        locked = compile_layout(layout)
        self.assertFalse(route(locked["navigation"], points[1]["local"], points[2]["local"])["reachable"])
        layout["navigation"]["surfaces"] = [[[0, 0, 0], [1, 0, 0], [0, 1, 2]]]
        with self.assertRaises(BuildingError):
            compile_layout(layout)

    def test_house_garage_extension_keeps_notch_and_opens_living(self):
        from shapely.geometry import box, Point
        from shapely.ops import unary_union
        layout = json.loads((ROOT / 'projects/experiments/building-lab/buildings/rancho-residential-house.building.json').read_bytes())
        layout.pop('retrofit')
        scene = compile_layout(layout)
        garage = next(r for r in scene['shell_rooms'] if r['id']=='garage')
        footprint = unary_union([box(*r) for r in garage['footprints']])
        self.assertTrue(footprint.covers(Point(-2.4,-6)))
        self.assertFalse(footprint.covers(Point(-2.4,-9.5)))
        self.assertAlmostEqual(footprint.area,49.2)
        self.assertTrue(route(scene['navigation'],[-.8,-6,0],[3,-6,0])['reachable'])
        self.assertTrue(route(scene['navigation'],[-2.4,-7.5,-.35],[-6.5,-8.5,-.35])['reachable'])
        self.assertFalse(any(r['id']=='mudroom' for r in layout['rooms']))
        import math
        from shapely.geometry import Polygon
        walls=[]
        for solid in scene['solids']:
            if solid['role']!='wall' or not solid['center'][2]-solid['size'][2]/2 < 1 < solid['center'][2]+solid['size'][2]/2:
                continue
            x,y=solid['center'][:2]
            w,h=solid['size'][:2]
            a=math.radians(solid['yaw'])
            walls.append(Polygon([(x+u*math.cos(a)-v*math.sin(a),y+u*math.sin(a)+v*math.cos(a)) for u,v in ((-w/2,-h/2),(w/2,-h/2),(w/2,h/2),(-w/2,h/2))]))
        coverage=unary_union(walls)
        self.assertTrue(coverage.covers(Point(-3.08,-9.5)))
        self.assertTrue(coverage.covers(Point(-.9,-8.92)))
        stair=scene['stairs'][0]
        from building_stair_frame import shaft
        flight=box(*shaft(stair))
        internal_door=next(d for d in scene['doors'] if d['id']=='garage-house-door')
        for endpoint in internal_door['endpoints']:
            self.assertGreater(flight.distance(Point(endpoint[:2])),1)
        broken=copy.deepcopy(layout)
        broken['shell_rooms'][0]['extensions'][0]['position']=[0,-6]
        with self.assertRaises(BuildingError):
            compile_layout(broken)

    def test_house_casings_span_both_wall_facings(self):
        import math
        layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/rancho-residential-house.building.json").read_bytes())
        layout.pop("retrofit")
        scene = compile_layout(layout)
        for door in scene["doors"]:
            if door.get("gate"):
                continue  # Surveyed shell apertures have their own casing anchors.
            wall = next(v for v in scene["instances"] if v["edge"] == door["id"])
            a = math.radians(wall["yaw"])
            # The native casing is 26 cm deep; both faces of the 17.5 cm
            # wall must fall inside it, including at reversed door yaw.
            center_depth = -(door["position"][0] - wall["position"][0]) * math.sin(a) + (door["position"][1] - wall["position"][1]) * math.cos(a)
            self.assertLess(center_depth - .13, 0)
            self.assertGreater(center_depth + .13, scene["kit"]["wall_thickness"])
            if door["id"] != "0:x:-1:0":
                self.assertAlmostEqual(center_depth, scene["kit"]["wall_thickness"] / 2)

    def test_house_open_leaves_clear_walk_surfaces_and_device_links(self):
        from shapely.geometry import Polygon, LineString
        from building_features import open_door_leaf
        layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/rancho-residential-house.building.json").read_bytes())
        layout.pop("retrofit")
        scene = compile_layout(layout)
        radius = scene["navigation"]["radius"]
        for door in scene["doors"]:
            leaf = open_door_leaf(door)
            if leaf is None:
                continue
            polygon = Polygon(leaf)
            self.assertGreaterEqual(polygon.distance(LineString([p[:2] for p in door["endpoints"]])), radius)
            for triangle in scene["navigation"]["triangles"]:
                if any(abs(p[2] - door["level"] * 4) > 1e-6 for p in triangle):
                    continue
                walk = Polygon([p[:2] for p in triangle])
                self.assertGreaterEqual(walk.distance(polygon) + 1e-6, radius, door["id"])

    def test_house_floor_caps_and_wall_foundations_do_not_overlap(self):
        layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/rancho-residential-house.building.json").read_bytes())
        layout.pop("retrofit")
        scene = compile_layout(layout)
        for solid in scene["solids"]:
            if solid["role"] == "wall" and solid["edge"]:
                lo = solid["center"][2] - solid["size"][2]/2
                hi = solid["center"][2] + solid["size"][2]/2
                if solid["level"] == 0:
                    self.assertLess(hi, 3.8)
                else:
                    self.assertGreaterEqual(lo, 4)
        for tile in (v for v in scene["instances"] if v["role"] == "floor" and v["id"].startswith("tile:")):
            # The vanilla floor is 3.005 m wide including its two lips.
            for axis in (0, 1):
                low = tile["position"][axis] - 3.0025 * tile["scale"][axis]
                high = tile["position"][axis] + .0025 * tile["scale"][axis]
                self.assertAlmostEqual(high-low, 3.005 * tile["scale"][axis])
                # Shaft cuts include the 12 cm guard footprint.
                self.assertAlmostEqual(high*100, round(high*100))

    def test_house_corner_stairs_and_measured_shell_access(self):
        from building_builder import runtime_contract
        layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/rancho-residential-house.building.json").read_bytes())
        layout.pop("retrofit")
        scene = compile_layout(layout)
        points = {p["name"]: p["local"] for p in runtime_contract(scene)["points"]}
        for actual, expected in zip(points["house stairs foot"], [-8.5, -2.2, 0]):
            self.assertAlmostEqual(actual,expected)
        for actual, expected in zip(points["house stairs top"], [-1.1, -2.2, 4]):
            self.assertAlmostEqual(actual,expected)
        steps = sorted([v for v in scene["solids"] if v["role"] == "stair" and v["id"].startswith("stair:house:")], key=lambda v:v["center"][0])
        self.assertEqual(len(steps), 20)
        self.assertLess(steps[0]["size"][2], steps[-1]["size"][2])
        self.assertEqual({d["id"] for d in scene["shell_doors"]}, {"rear-entrance", "balcony-door", "garage-door", "garage-house-door"})
        garage = next(r for r in scene["shell_rooms"] if r["id"] == "garage")
        self.assertEqual(garage["z"], -.35)
        self.assertEqual(garage["bounds"], [-9, -10, -3, -3])
        for target in ("Garage workshop", "Rear vestibule", "Rear porch", "Balcony doorway", "Balcony front"):
            self.assertTrue(route(scene["navigation"], points["Front porch"], points[target])["reachable"], target)
        for bad in ("bad", float("nan")):
            broken = copy.deepcopy(layout)
            broken["shell_rooms"][0]["width"] = bad
            with self.assertRaises(BuildingError):
                compile_layout(broken)

    def test_compact_house_stairs_have_exact_shaft_and_roof_clearance(self):
        from shapely.geometry import box
        layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/rancho-residential-house.building.json").read_bytes())
        layout.pop("retrofit")
        scene = compile_layout(layout)
        stair = scene["stairs"][0]
        from building_stair_frame import shaft as stair_shaft, point
        shaft = box(*stair_shaft(stair))
        for slab in scene["solids"]:
            if (slab["role"], slab["level"]) not in (("ceiling", 0), ("floor", 1)):
                continue
            x, y = slab["center"][:2]
            w, d = slab["size"][:2]
            self.assertLess(shaft.intersection(box(x-w/2, y-d/2, x+w/2, y+d/2)).area, 1e-8)
        # Measured roof edge 125 reaches x=3.978, y=-11.528..-9.643,
        # z=3.127..4.353. It must lie outside the new room, not behind a
        # ceiling lowered to conceal an oversized room.
        bedroom = next(r for r in layout["rooms"] if r["id"] == "bedroom_b")
        footprint = box(bedroom["x"], bedroom["y"], bedroom["x"]+bedroom["width"], bedroom["y"]+bedroom["depth"])
        self.assertEqual(footprint.intersection(box(.974, -11.528, 3.978, -9.643)).area, 0)
        self.assertEqual(bedroom["ceiling_height"], 3.5)
        # The top flight must meet physical floor immediately, including the
        # 12 cm strip occupied by the guard on the other half of the opening.
        from shapely.geometry import Point
        exit_point = Point(point(stair, stair['width']/2, stair['run']+.01, 4)[:2])
        self.assertTrue(any(box(s['center'][0]-s['size'][0]/2,s['center'][1]-s['size'][1]/2,
                                s['center'][0]+s['size'][0]/2,s['center'][1]+s['size'][1]/2).covers(exit_point)
                            for s in scene['solids'] if s['role']=='floor' and s['level']==1))

    def test_garage_device_matches_scaled_shell_and_native_component(self):
        from building_builder import native_documents
        layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/rancho-residential-house.building.json").read_bytes())
        layout.pop('retrofit')
        scene = compile_layout(layout)
        door = next(d for d in scene['doors'] if d['id'] == 'garage-door')
        self.assertEqual(door['scale'], [1.47733581, 1, 1.24567723])
        garage = next(r for r in layout['shell_rooms'] if r['id'] == 'garage')
        self.assertEqual(garage['walls']['south']['openings'][0]['width'], 4.3)
        sector, _, _ = native_documents(scene, ROOT/'generated/building-editor/garage-test')
        root = sector['Data']['RootChunk']
        for placement in root['nodeData']['Data']:
            node = root['nodes'][placement['NodeIndex']]['Data']
            if node.get('entityTemplate', {}).get('DepotPath', {}).get('$value') != door['template']:
                continue
            self.assertEqual([placement['Scale'][k] for k in ('X','Y','Z')], [1,1,1])
            package = node['instanceData']['Data']['buffer']['Data']
            self.assertEqual(package['CruidDict']['0'], '1563417374541762560')
            self.assertEqual(package['Chunks'][0]['persistentState']['Data']['doorProperties']['isShutter'], 1)
            frame, animated, collider = package['Chunks'][2:]
            self.assertEqual([frame['visualScale'][k] for k in 'XYZ'],door['scale'])
            self.assertEqual(animated['rig']['DepotPath']['$value'],r'mod\building_lab\rancho-garage.rig')
            rig=json.loads((ROOT/'projects/experiments/building-lab/source/raw/mod/building_lab/rancho-garage.rig.json').read_bytes())['Data']['RootChunk']
            self.assertEqual([rig['boneTransforms'][0]['Scale'][k] for k in 'XYZ'],door['scale'])
            self.assertEqual(collider['colliders'][0]['Data']['halfExtents']['X'],1.5*door['scale'][0])
            break
        else:
            self.fail('Garage device not exported')
        locked = copy.deepcopy(layout)
        locked['door_states'] = {'garage-house-door':'LOCKED', 'garage-door':'LOCKED'}
        blocked = compile_layout(locked)
        self.assertFalse(route(blocked['navigation'], [-6.012,-10.7,-.6], [-6.5,-8.5,-.35])['reachable'])

    def test_return_stairs_have_continuous_half_storey_turn_and_clear_landings(self):
        from shapely.geometry import Polygon
        from building_return_stairs import navigation
        stair = {'id':'return','type':'return','x':0,'y':0,'width':2.6,'flight_width':1.2,'run':3,'landing':1.2,'level':0}
        triangles = navigation(stair, 4, .3)
        # Each ramp has a 2 m rise over 3 m; the turning landing is flat at 2 m.
        for triangle in triangles:
            levels = [p[2] for p in triangle]
            self.assertTrue(all(0 <= z <= 4 for z in levels))
            if max(levels) != min(levels):
                self.assertAlmostEqual(max(levels)-min(levels), 2)
        landing = [Polygon([p[:2] for p in t]) for t in triangles if all(p[2] == 2 for p in t)]
        self.assertAlmostEqual(sum(p.area for p in landing), 2*.9)
        # The turn keeps the full clearance-eroded width instead of two
        # disconnected 60 cm flight strips.
        from shapely.ops import unary_union
        self.assertTrue(unary_union(landing).buffer(1e-8).covers(Polygon([[.3,-.9],[2.3,-.9],[2.3,-.01],[.3,-.01]])))
        bad = copy.deepcopy(self.layout)
        bad['stairs'][0].update(type='return',width=2.6,run=3,flight_width=1.3)
        with self.assertRaises(BuildingError):
            compile_layout(bad)

    def test_house_windows_keep_collision_and_use_clear_material(self):
        layout = json.loads((ROOT / "projects/experiments/building-lab/buildings/rancho-residential-house.building.json").read_bytes())
        layout.pop("retrofit")
        scene = compile_layout(layout)
        for edge in layout["windows"]:
            pieces = [v for v in scene["instances"] if v["edge"] == edge]
            self.assertEqual(len(pieces), 4)
            self.assertTrue(all(p["mesh"] == scene["kit"]["pieces"]["wall"]["mesh"] for p in pieces))
            # Glass is a visual opening, never a walkable route outside.
            self.assertTrue(any(s["edge"] == edge and s["size"][0] == 3 for s in scene["solids"]))
        windows = [v for v in scene["instances"] if v["mesh"].endswith("rancho-window-clear.mesh")]
        self.assertEqual(len(windows), 2)
        root = json.loads((ROOT / "projects/experiments/building-lab/source/raw/mod/building_lab/rancho-window-clear.mesh.json").read_bytes())["Data"]["RootChunk"]
        glass = next(e for e in root["materialEntries"] if e["name"]["$value"] == "glass")
        self.assertFalse(glass["isLocalInstance"])
        self.assertEqual(glass["index"], 0)
        self.assertTrue(root["externalMaterials"][0]["DepotPath"]["$value"].endswith("window_generic_glass.mi"))

    def test_terrain_mask_changes_only_flags_and_preserves_other_floors(self):
        import base64
        import struct
        from building_nav_mask import mask_resource
        scene = compile_layout(self.layout)
        resource = navigation_resource(scene)
        original = copy.deepcopy(resource)
        masked, changes, _ = mask_resource(resource, scene["layout"]["origin"],
                                          [[-1, -1], [20, -1], [20, 20], [-1, 20]], [-.1, .1])
        self.assertEqual(resource, original)
        self.assertTrue(changes)
        permitted = {}
        for change in changes:
            raw = base64.b64decode(original["tileBuffers"][change["buffer"]]["Bytes"])
            vertices = struct.unpack_from("<i", raw, 28)[0]
            permitted[change["buffer"]] = {100 + vertices*12 + face*20 + k for face in change["polygons"] for k in (16, 17)}
        decoded = load_navigation_sector({"Data": {"RootChunk": masked}})
        for index, (before, after) in enumerate(zip(original["tileBuffers"], masked["tileBuffers"])):
            a, b = base64.b64decode(before["Bytes"]), base64.b64decode(after["Bytes"])
            self.assertEqual(len(a), len(b))
            self.assertTrue({i for i, (x, y) in enumerate(zip(a, b)) if x != y} <= permitted.get(index, set()))
        self.assertEqual(len(decoded.buffers), len(resource["tileBuffers"]))
        with self.assertRaises(ValueError):
            mask_resource(resource, scene["layout"]["origin"], [[0, 0], [.01, 0], [.01, .01], [0, .01]], [-.1, .1])

    def test_stairs_cut_floor_and_ceiling_and_connect_floors(self):
        scene = compile_layout(self.layout)
        self.assertFalse(any(i["id"] == "tile:1:1:1:floor" for i in scene["instances"]))
        self.assertFalse(any(s["id"] == "tile:0:1:1:ceiling" for s in scene["solids"]))
        steps = [s for s in scene["solids"] if s["role"] == "stair"]
        self.assertEqual(len(steps), 22)
        self.assertAlmostEqual(max(s["center"][2] + s["size"][2] / 2 for s in steps), 4.4)
        self.assertTrue(route(scene["navigation"], [1.5, 1.5, 0], [1.5, 1.5, 4.4])["reachable"])
        self.layout["stairs"] = []
        no_stairs = compile_layout(self.layout)
        self.assertFalse(route(no_stairs["navigation"], [1.5, 1.5, 0], [1.5, 1.5, 4.4])["reachable"])

    def test_cross_node_references_register_absolute_paths(self):
        from building_builder import native_documents
        from generate_world import node_ref_hash
        scene = compile_layout(self.layout)
        sector, _, _ = native_documents(scene, ROOT / "generated/building-editor/reference-test")
        registered = {v["$value"] for v in sector["Data"]["RootChunk"]["nodeRefs"]}
        self.assertTrue(registered)
        self.assertTrue(all(ref.startswith("$/") for ref in registered))
        for door in scene["doors"]:
            self.assertIn(door["ref"], registered)
            self.assertIn(door["connection_ref"], registered)
            link = next(link for link in scene["navigation"]["links"] if link["ref"] == door["connection_ref"])
            self.assertEqual(int(link["id"]), node_ref_hash(door["connection_ref"]))
        self.layout["navigation"]["connections"] = [{"id":"street","from":[4.5,1.5,0],"to":[4.5,-1,0]}]
        scene = compile_layout(self.layout)
        self.assertTrue(next(link for link in scene["navigation"]["links"] if link.get("kind")=="entrance")["ref"].startswith("$/"))

    def test_shared_wall_faces_both_rooms_without_moving_door(self):
        scene = compile_layout(self.layout)
        for edge in scene["edges"]:
            if not edge["shared"] or edge["opening"] == "passage":
                continue
            front, back = [v for v in scene["instances"] if v["edge"] == edge["id"]]
            import math
            def centre(v):
                a = math.radians(v["yaw"])
                # Transform the normalized wall-volume midpoint, accounting for
                # the mesh offset independently of the facing orientation.
                off = scene["kit"]["pieces"][v["role"]].get("offset", [0, 0, 0])
                x, y = -1.5 - off[0], scene["kit"]["wall_thickness"] / 2 - off[1]
                return [v["position"][0]+x*math.cos(a)-y*math.sin(a),
                        v["position"][1]+x*math.sin(a)+y*math.cos(a)]
            for a, b in zip(centre(front), centre(back)):
                self.assertAlmostEqual(a, b)
            self.assertEqual(back["yaw"]-front["yaw"], 180)
        self.assertEqual(len(scene["doors"]), 2)

    def test_storey_slabs_close_gap_and_guards_do_not_overlap(self):
        scene = compile_layout(self.layout)
        solids = {v["id"]: v for v in scene["solids"]}
        ceiling, floor = solids["tile:0:0:0:ceiling"], solids["tile:1:0:0:floor"]
        self.assertAlmostEqual(ceiling["center"][2]+ceiling["size"][2]/2,
                               floor["center"][2]-floor["size"][2]/2)
        guards = [v for v in scene["solids"] if v["role"] == "guard"]
        for index, a in enumerate(guards):
            for b in guards[index+1:]:
                overlaps = [min(a["center"][i]+a["size"][i]/2,b["center"][i]+b["size"][i]/2)
                            -max(a["center"][i]-a["size"][i]/2,b["center"][i]-b["size"][i]/2) for i in range(3)]
                self.assertFalse(all(v>1e-6 for v in overlaps), (a["id"],b["id"]))

    def test_slab_edges_meet_guard_exteriors_without_volume_overlap(self):
        scene = compile_layout(self.layout)
        guards = [s for s in scene["solids"] if s["role"] == "guard"]
        slabs = [s for s in scene["solids"] if s["role"] in ("floor", "ceiling")]
        for a in guards:
            for b in slabs:
                overlap = [min(a["center"][i]+a["size"][i]/2,b["center"][i]+b["size"][i]/2)
                           -max(a["center"][i]-a["size"][i]/2,b["center"][i]-b["size"][i]/2) for i in range(3)]
                self.assertFalse(all(v > 1e-6 for v in overlap), (a["id"], b["id"]))
        left = next(s for s in slabs if s["id"] == "tile:0:0:1:ceiling")
        self.assertAlmostEqual(left["center"][0]+left["size"][0]/2, 2.88)
        self.assertTrue(route(scene["navigation"], [1.5,1.5,0], [1.5,1.5,4.4])["reachable"])

    def test_stair_visuals_enclose_the_solid_column(self):
        scene = compile_layout(self.layout)
        for solid in (s for s in scene["solids"] if s["role"] == "stair"):
            body, cap = [v for v in scene["instances"] if v["id"].startswith(solid["id"]+":")]
            self.assertEqual(body["role"], "ceiling")
            self.assertEqual(body["appearance"], "concrete")
            self.assertAlmostEqual(body["position"][2], solid["center"][2]-solid["size"][2]/2)
            self.assertAlmostEqual(cap["position"][2], solid["center"][2]+solid["size"][2]/2)
            self.assertAlmostEqual(body["position"][2]+.1*body["scale"][2], cap["position"][2]-.2*cap["scale"][2])
            for axis in (0,1):
                self.assertAlmostEqual(cap["position"][axis]+.0025*cap["scale"][axis],
                                       solid["center"][axis]+solid["size"][axis]/2)
                self.assertAlmostEqual(cap["position"][axis]-3.0025*cap["scale"][axis],
                                       solid["center"][axis]-solid["size"][axis]/2)

    def test_invalid_stairs_reject_missing_landings_and_overlaps(self):
        for field, value in (("y", 0), ("width", 1.1), ("level", 1), ("run", 3), ("x", float("nan"))):
            with self.subTest(field=field, value=value):
                layout = copy.deepcopy(self.layout)
                layout["stairs"][0][field] = value
                with self.assertRaises(BuildingError):
                    compile_layout(layout)
        self.layout["stairs"].append({**self.layout["stairs"][0], "id": "duplicate"})
        with self.assertRaises(BuildingError):
            compile_layout(self.layout)

    def test_locked_device_door_gates_offline_and_native_navigation(self):
        start, end = [7.5, 4.5, 0], [10.5, 4.5, 0]
        open_scene = compile_layout(self.layout)
        self.assertTrue(route(open_scene["navigation"], start, end)["reachable"])
        self.layout["door_states"] = {"0:y:3:1": "LOCKED"}
        locked = compile_layout(self.layout)
        self.assertFalse(route(locked["navigation"], start, end)["reachable"])
        resource = navigation_resource(locked)
        self.assertEqual(sorted(resource["tilesData"][0]["offMeshConnections"]["flags"]), [0, 3])
        decoded = load_navigation_sector({"Data": {"RootChunk": resource}})
        offmesh = [f for b in decoded.buffers for f in b.faces if f.num_indices == 2]
        self.assertEqual(len(offmesh), 2)
        self.assertEqual(sorted(f.three for f in offmesh), [0, 3])
        self.assertEqual(sum(len(b.bounds_records) for b in decoded.buffers), 2)

    def test_native_bv_tree_covers_each_ground_polygon_and_has_valid_escapes(self):
        scene = compile_layout(self.layout)
        resource = navigation_resource(scene)
        decoded = load_navigation_sector({"Data": {"RootChunk": resource}})
        for tile in decoded.buffers:
            count = tile.header.index_record_count
            self.assertEqual(len(tile.info_records), count * 2)
            nodes = []
            for entry in tile.info_records[:-1]:
                values = [int.from_bytes(bytes((a & 255, b & 255)), "little") for a,b in entry.values]
                index = entry.unknown if entry.unknown < 2**31 else entry.unknown - 2**32
                nodes.append((values[:3], values[3:], index))
            self.assertEqual(sorted(n[2] for n in nodes if n[2]>=0), list(range(count)))
            def visit(offset):
                lower, upper, index = nodes[offset]
                self.assertTrue(all(a<=b for a,b in zip(lower,upper)))
                if index >= 0:
                    vertices = [tile.vertices[v] for v in tile.faces[index].vertex_indices]
                    bounds = tile.bounds.minimum
                    for axis in range(3):
                        values = [getattr(v, ('x','y','z')[axis]) for v in vertices]
                        origin = getattr(bounds, ('x','y','z')[axis])
                        self.assertLessEqual(lower[axis]/10+origin, min(values)+.101)
                        self.assertGreaterEqual(upper[axis]/10+origin, max(values)-.101)
                    return offset+1
                end = offset-index
                self.assertEqual(visit(visit(offset+1)), end)
                return end
            self.assertEqual(visit(0), count*2-1)

    def test_native_tiles_are_deterministic_and_use_reciprocal_adjacency(self):
        scene = compile_layout(self.layout)
        first = navigation_resource(scene)
        self.assertEqual(first, navigation_resource(scene))
        decoded = load_navigation_sector({"Data": {"RootChunk": first}})
        for tile in decoded.buffers:
            self.assertEqual(tile.header.unknown_1, 8)
            for face in tile.faces:
                for link in face.connected_faces:
                    if link.index and not link.flagged:
                        self.assertLess(link.index, len(tile.faces) + 1)
                        self.assertIn(face.index + 1, [other.raw for other in tile.faces[link.index - 1].connected_faces])

    def test_rotated_negative_world_tiles_have_portals_and_layer(self):
        self.layout["origin"] = {"x": 30, "y": -5, "z": 700, "yaw": 37}
        resource = navigation_resource(compile_layout(self.layout))
        decoded = load_navigation_sector({"Data": {"RootChunk": resource}})
        self.assertEqual(len(decoded.buffers), 4)
        self.assertTrue(any(t["tileY"] < 0 for t in resource["tilesData"]))
        self.assertTrue(any(c.flagged for b in decoded.buffers for f in b.faces for c in f.connected_faces))
        self.assertTrue(all(b.header.unknown_2 == 200 for b in decoded.buffers))

    def test_export_contains_navigation_devices_and_registration(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            export_project(compile_layout(self.layout), output)
            files = list((output / "source/raw/mod/building_lab").glob("*.json"))
            self.assertEqual(len(files), 4)
            nav_sector = json.loads((output / "source/raw/mod/building_lab/navigation-lab_navigation.streamingsector.json").read_bytes())["Data"]
            self.assertEqual(nav_sector["RootChunk"]["nodes"][0]["Data"]["navigationTileResource"]["Flags"], "Embedded")
            self.assertEqual(nav_sector["EmbeddedFiles"][0]["Content"]["$type"], "worldNavigationTileResource")
            self.assertTrue(nav_sector["EmbeddedFiles"][0]["Content"]["tileBuffers"])
            sector = json.loads((output / "source/raw/mod/building_lab/navigation-lab.streamingsector.json").read_bytes())["Data"]["RootChunk"]
            types = [n["Data"]["$type"] for n in sector["nodes"]]
            self.assertEqual(types.count("worldDeviceNode"), 2)
            self.assertEqual(types.count("worldOffMeshConnectionNode"), 2)
            ids = [n["Data"]["instanceData"]["Data"]["buffer"]["BufferId"] for n in sector["nodes"] if n["Data"]["$type"] == "worldDeviceNode"]
            self.assertEqual(len(set(ids)), 2)
            profiles = json.loads((output / "packaging/profiles.json").read_bytes())["profiles"]
            self.assertNotIn("include_loose", profiles["building-lab"])
            self.assertEqual(len(profiles["building-lab-test"]["include_loose"]), 2)
            contract = json.loads((output / "source/resources/bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_building_lab/contract.json").read_bytes())
            self.assertFalse(contract["runtime_verified"])
            self.assertEqual(len(contract["doors"]), 2)
            self.assertTrue(all(d["connection_ref"] for d in contract["doors"]))
            for point in contract["points"]:
                self.assertTrue(route(compile_layout(self.layout)["navigation"], point["local"], point["local"])["reachable"])

    def test_retrofit_room_supports_lower_ceiling_and_street_points(self):
        from building_builder import runtime_contract
        layout = copy.deepcopy(self.layout)
        layout.update(rooms=[{"id":"inside","name":"Interior","x":0,"y":0,"width":6,"depth":3,"level":0,"ceiling_height":3.5}],
                      stairs=[],openings={"0:y:0:0":"door_auto"})
        layout["navigation"].update(test_points=[{"name":"Street approach","position":[-1.7,1.5,-.05]}],
                                    door_connections={"0:y:0:0":{"from":[.9,1.5,0],"to":[-1.7,1.5,-.05]}})
        scene = compile_layout(layout)
        self.assertTrue(all(abs(v["position"][2]-3.5)<1e-6 for v in scene["instances"] if v["role"]=="ceiling"))
        self.assertEqual(runtime_contract(scene)["points"][0]["name"], "Street approach")
        self.assertGreater(scene["doors"][0]["endpoints"][0][0],0)
        self.assertTrue(scene["navigation"]["links"][0]["external"])
        layout["navigation"]["door_connections"]["0:y:0:0"]["from"]=[-1,1.5,0]
        with self.assertRaises(BuildingError):
            compile_layout(layout)
        layout["navigation"]["door_connections"]={}
        layout["rooms"][0]["ceiling_height"]=1
        with self.assertRaises(BuildingError):
            compile_layout(layout)

    def test_default_exterior_door_orders_its_inside_endpoint_first(self):
        scene = compile_layout(self.layout)
        from building_navigation import locate_face
        exterior = [link for link in scene["navigation"]["links"] if link["external"]]
        self.assertTrue(exterior)
        for link in exterior:
            self.assertIsNotNone(locate_face(scene["navigation"]["triangles"],link["endpoints"][0]))
            self.assertIsNone(locate_face(scene["navigation"]["triangles"],link["endpoints"][1]))

    def test_external_entrance_links_are_explicit_and_height_limited(self):
        self.layout["navigation"]["connections"] = [{"id": "street", "from": [4.5, 1.5, 0], "to": [4.5, -1, 0]}]
        scene = compile_layout(self.layout)
        link = next(link for link in scene["navigation"]["links"] if link.get("kind") == "entrance")
        self.assertTrue(link["external"])
        self.assertEqual(link["area"], 3)  # Floor/Regular; 12 is Jump.
        self.assertFalse(route(scene["navigation"], [4.5, 1.5, 0], [4.5, -1, 0])["reachable"])
        self.layout["navigation"]["connections"][0]["to"][2] = 1.0
        with self.assertRaises(BuildingError):
            compile_layout(self.layout)

    def test_export_layer_zero_is_rejected_instead_of_colliding_with_vanilla(self):
        self.layout["navigation"]["layer"] = 0
        with self.assertRaises(BuildingError):
            compile_layout(self.layout)
        self.layout["navigation"]["export"] = False
        self.assertIsNotNone(compile_layout(self.layout))


class RetrofitTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=ROOT / ".tmp")
        self.addCleanup(self.temporary.cleanup)
        self.source = Path(self.temporary.name) / "shell.streamingsector.json"
        solid = {"id": "wall", "world_center": [10, 20, 30], "world_yaw": 0, "size": [3, .2, 4]}
        collision = collision_node(solid, 1)
        root = {"nodes": [{"Data": {"$type": "worldMeshNode"}}, {"Data": collision}],
                "nodeData": {"Data": [{"NodeIndex": i, "Position": {"X": 10, "Y": 20, "Z": 30}} for i in (0, 1)]}}
        self.source.write_text(json.dumps({"Data": {"RootChunk": root}}), encoding="utf-8")
        self.entry = {"source": self.source.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(self.source.read_bytes()).hexdigest(),
                      "path": r"base\worlds\03_night_city\_compiled\default\exterior_0_0_0_0.streamingsector", "expectedNodes": 2,
                      "nodeDeletions": [{"index": 0, "type": "worldMeshNode"},
                                        {"index": 1, "type": "worldCollisionNode", "expectedActors": 1, "actorDeletions": [[0, 0]]}]}

    def test_patch_retains_actor_relative_shape_selection(self):
        patches = validate_retrofit({"retrofit": {"sectors": [self.entry]}})
        self.assertEqual(patches[0]["nodeDeletions"][1]["actorDeletions"], [[0, 0]])
        self.assertNotIn("source", patches[0])
        self.assertEqual(self.source.read_bytes()[:1], b"{")

    def test_instanced_occluder_requires_reviewed_whole_group(self):
        import base64
        import struct
        doc = json.loads(self.source.read_bytes())
        raw = bytes([2]) + struct.pack("<16f", *([0.] * 16)) * 2
        doc["Data"]["RootChunk"]["nodes"][0]["Data"] = {"$type": "worldInstancedOccluderNode", "$rawTail": base64.b64encode(raw).decode()}
        self.source.write_text(json.dumps(doc), encoding="utf-8")
        entry = copy.deepcopy(self.entry)
        entry["sha256"] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        deletion = {"index": 0, "type": "worldInstancedOccluderNode", "expectedInstances": 2, "removeWholeGroup": True}
        entry["nodeDeletions"] = [deletion]
        self.assertEqual(validate_retrofit({"retrofit": {"sectors": [entry]}})[0]["nodeDeletions"], [{"index": 0, "type": "worldInstancedOccluderNode"}])
        for key, value in (("expectedInstances", 1), ("removeWholeGroup", False), ("instanceDeletions", [0])):
            bad = copy.deepcopy(entry)
            bad["nodeDeletions"][0][key] = value
            with self.assertRaises(ValueError):
                validate_retrofit({"retrofit": {"sectors": [bad]}})

    def test_entity_replacement_requires_pinned_decorative_template(self):
        from generate_world import resource_path
        doc = json.loads(self.source.read_bytes())
        template = r"base\gameplay\devices\doors\final\single_door_decorative.ent"
        doc["Data"]["RootChunk"]["nodes"][0]["Data"] = {"$type": "worldEntityNode", "entityTemplate": resource_path(template)}
        self.source.write_text(json.dumps(doc), encoding="utf-8")
        entry = copy.deepcopy(self.entry)
        entry["sha256"] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        entry["nodeDeletions"] = [{"index": 0, "type": "worldEntityNode"}]
        with self.assertRaises(ValueError):
            validate_retrofit({"retrofit": {"sectors": [entry]}})
        entry["nodeDeletions"][0]["expectedTemplate"] = template
        self.assertEqual(validate_retrofit({"retrofit": {"sectors": [entry]}})[0]["nodeDeletions"][0]["type"], "worldEntityNode")
        doc["Data"]["RootChunk"]["nodes"][0]["Data"]["entityTemplate"] = resource_path(r"base\characters\npc.ent")
        self.source.write_text(json.dumps(doc), encoding="utf-8")
        entry["sha256"] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        with self.assertRaises(ValueError):
            validate_retrofit({"retrofit": {"sectors": [entry]}})

    def test_changed_source_and_out_of_range_actor_are_rejected(self):
        for key, value in (("sha256", "bad"), ("expectedNodes", 3)):
            entry = {**self.entry, key: value}
            with self.assertRaises(ValueError):
                validate_retrofit({"retrofit": {"sectors": [entry]}})
        entry = copy.deepcopy(self.entry)
        entry["nodeDeletions"][1]["actorDeletions"] = [[0, 1]]
        with self.assertRaises(ValueError):
            validate_retrofit({"retrofit": {"sectors": [entry]}})

    def test_survey_finds_visual_and_collision_candidates(self):
        result = survey(self.source, self.entry["path"], [10, 20, 30], 2)
        self.assertEqual(len(result["candidates"]), 2)
        self.assertEqual(result["selection"]["sha256"], self.entry["sha256"])

    def test_area_survey_reports_missing_and_unbounded_sectors(self):
        from world_location_world import AABB
        with tempfile.TemporaryDirectory(dir=ROOT / ".tmp") as directory:
            root = Path(directory)
            depot = self.entry["path"]
            target = root / (depot.replace("\\", "/") + ".json")
            target.parent.mkdir(parents=True)
            target.write_bytes(self.source.read_bytes())
            descriptors = [SimpleNamespace(depot_path=depot, bounds=AABB(0, 0, 0, 100, 100, 100)),
                           SimpleNamespace(depot_path=depot.replace("exterior_0", "exterior_1"), bounds=AABB(0, 0, 0, 100, 100, 100)),
                           SimpleNamespace(depot_path="always_loaded.streamingsector", bounds=AABB(-1e30, -1e30, -1e30, 1e30, 1e30, 1e30))]
            with patch("world_location_world.WorldSectorIndex.from_streaming_blocks") as factory:
                factory.return_value.query.return_value = descriptors
                report = survey_nearby([], root, [10, 20, 30], 2, root / "output")
            self.assertEqual(report["scanned_cached_sectors"], 1)
            self.assertEqual(len(report["missing_cached_sectors"]), 1)
            self.assertEqual(len(report["unbounded_descriptors_skipped"]), 1)
            self.assertEqual(report["surveys"][0]["collision_candidates"], 1)
            self.assertTrue((root / "output" / report["surveys"][0]["survey"]).is_file())

    def test_archive_xl_indices_address_placements_not_definitions(self):
        document = json.loads(self.source.read_bytes())
        root = document["Data"]["RootChunk"]
        root["nodeData"]["Data"].insert(1, {"NodeIndex": 0, "Position": {"X": 20, "Y": 30, "Z": 40}})
        self.source.write_text(json.dumps(document), encoding="utf-8")
        entry = copy.deepcopy(self.entry)
        entry["sha256"] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        entry["expectedNodes"] = 3
        entry["nodeDeletions"][1]["index"] = 2
        result = validate_retrofit({"retrofit": {"sectors": [entry]}})
        self.assertEqual(result[0]["expectedNodes"], 3)
        self.assertEqual(result[0]["nodeDeletions"][1]["index"], 2)
        entry["expectedNodes"] = 2
        with self.assertRaises(ValueError):
            validate_retrofit({"retrofit": {"sectors": [entry]}})

    def test_instanced_facade_requires_a_precise_instance_selection(self):
        document = json.loads(self.source.read_bytes())
        document["Data"]["RootChunk"]["nodes"][0]["Data"] = {"$type": "worldInstancedMeshNode", "worldTransformsBuffer": {"numElements": 4}}
        self.source.write_text(json.dumps(document), encoding="utf-8")
        entry = copy.deepcopy(self.entry)
        entry["sha256"] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        entry["nodeDeletions"] = [{"index": 0, "type": "worldInstancedMeshNode"}]
        with self.assertRaises(ValueError):
            validate_retrofit({"retrofit": {"sectors": [entry]}})
        entry["nodeDeletions"][0].update(expectedInstances=4, instanceDeletions=[2])
        result = validate_retrofit({"retrofit": {"sectors": [entry]}})
        self.assertEqual(result[0]["nodeDeletions"][0]["instanceDeletions"], [2])

    def test_minimum_version_preserves_mesh_alias_requirement(self):
        self.assertEqual(minimum_archive_version({"minimum_archivexl": "1.10"}, {"alias": []}), "1.14")
        self.assertEqual(minimum_archive_version({"minimum_archivexl": "1.27.0"}, {"alias": []}), "1.27.0")
        with self.assertRaises(PackageError):
            minimum_archive_version({"minimum_archivexl": "latest"}, {})

    def test_packager_preserves_only_explicit_sector_patch_selection(self):
        document = {"streaming": {"sectors": [{"path": self.entry["path"], "expectedNodes": 2, "nodeDeletions": self.entry["nodeDeletions"]}]}}
        profile = {"active_quests": [], "streaming_sectors": [self.entry["path"]]}
        result = filter_registration(document, profile, {"building_lab"})
        self.assertEqual(result["streaming"]["sectors"], document["streaming"]["sectors"])
        self.assertNotIn("sectors", filter_registration(document, {"active_quests": []}, {"building_lab"})["streaming"])
        profile["streaming_sectors"].append("missing")
        with self.assertRaises(PackageError):
            filter_registration(document, profile, {"building_lab"})


if __name__ == "__main__":
    unittest.main()
