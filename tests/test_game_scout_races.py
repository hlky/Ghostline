"""Targeted race survey, persistence, coordinate and world-export contracts."""
import asyncio
import json
import math
from pathlib import Path
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
from game_scout.core import Library, ScoutError
from game_scout.controller import Scout
from game_scout.races import RacePlans, station
from tests.test_game_scout import FakeBridge, FakeImages
import generate_world


class RaceSurveyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.library = Library(Path(self.tmp.name))
        self.bridge = FakeBridge()
        self.scout = Scout(self.bridge, self.library, FakeImages(self.library))
        self.races = self.scout.races
        self.race = self.races.create('Test course', 'gqt_race')['id']

    def mark(self, role, x=0, y=0, z=0, **kwargs):
        return self.scout.mark_race(self.race,role,source='manual',
            position={'x':x,'y':y,'z':z},yaw=30,**kwargs)['mark']

    def complete(self):
        self.mark('spline_point',100,200,10)
        self.mark('spline_point',130,200,10)
        self.mark('spline_point',160,200,10)
        for role in ('checkpoint','start_grid','player_start','staging','activation','finish'):
            self.mark(role,130,200,10)

    def test_manual_marks_survive_restart_and_library_export_without_game_control(self):
        first = self.mark('spline_point',x=10)
        self.mark('spline_point',x=20)
        restored = RacePlans(Library(Path(self.tmp.name))).get(self.race)
        self.assertEqual([m['order'] for m in restored['data']['marks']],[0,1])
        self.assertEqual(restored['data']['marks'][0]['id'],first['id'])
        exported = json.loads(Path(self.library.export()).read_text())
        self.assertEqual(exported['records'][0]['kind'],'race')
        self.assertEqual(self.bridge.commands,[])
        self.assertIsNone(self.bridge.session)

    def test_surface_mark_uses_hit_not_camera_and_rejects_stale_image(self):
        self.scout.begin()
        original = self.bridge.command
        def command(kind, **args):
            if kind == 'inspect':
                return {'hit':True,'position':{'x':4,'y':8,'z':0},'group':'Static'}
            return original(kind,**args)
        self.bridge.command = command
        result = self.scout.mark_race(self.race,'checkpoint')
        self.assertEqual(result['mark']['position'],{'x':4.,'y':8.,'z':0.})
        self.assertEqual(result['mark']['evidence']['hit']['group'],'Static')
        self.bridge.pose['yaw'] += 10
        with self.assertRaisesRegex(ScoutError,'moved'):
            self.scout.mark_race(self.race,'checkpoint')
        self.assertEqual(len(self.races.get(self.race)['data']['marks']),1)

    def test_no_hit_and_cancellation_do_not_append_marks(self):
        self.scout.begin()
        self.bridge.command = lambda kind,**args: {'hit':False}
        with self.assertRaisesRegex(ScoutError,'No surface hit'):
            self.scout.mark_race(self.race,'spline_point')
        def stopped(kind,**args):
            self.scout.stop()
            return {'hit':True,'position':{'x':0,'y':0,'z':0}}
        self.bridge.command = stopped
        with self.assertRaisesRegex(ScoutError,'stopped'):
            self.scout.mark_race(self.race,'spline_point')
        self.assertEqual(self.races.get(self.race)['data']['marks'],[])

    def test_edit_remove_and_failed_changes_preserve_other_marks(self):
        a = self.mark('spline_point',x=10)
        b = self.mark('spline_point',x=20)
        with self.assertRaisesRegex(ScoutError,'role/order'):
            self.races.edit(self.race,b['id'],order=0)
        self.races.edit(self.race,a['id'],order=3,notes='last point',position={'x':30,'y':0,'z':0})
        record = self.races.get(self.race)
        self.assertEqual(record['data']['marks'][0]['evidence']['source'],'manual_edit')
        self.races.remove(self.race,b['id'])
        self.assertEqual(len(self.races.get(self.race)['data']['marks']),1)
        with self.assertRaisesRegex(ScoutError,'belong'):
            self.races.remove(self.race,b['id'])

    def test_concurrent_marks_have_unique_order_and_no_lost_updates(self):
        def mark(i):
            return RacePlans(Library(Path(self.tmp.name))).mark(self.race,'spline_point',{'x':i,'y':0,'z':0},0)
        with ThreadPoolExecutor(max_workers=4) as pool:
            list(pool.map(mark,range(16)))
        marks = self.races.get(self.race)['data']['marks']
        self.assertEqual(sorted(m['order'] for m in marks),list(range(16)))

    def test_complete_export_builds_world_with_stable_refs_and_native_headings(self):
        self.complete()
        self.mark('speed_change',120,200,10,options={'speed_mps':5})
        self.mark('width_change',110,200,10,options={'left_m':2,'right_m':3})
        self.mark('prop',120,205,10,options={'entity_template':'mod/example/barrier.ent'})
        exported = self.races.export(self.race)
        spec = json.loads(Path(exported['world_spec_path']).read_text())
        plan = json.loads(Path(exported['manifest_path']).read_text())
        self.assertEqual(exported['status'],'geometry_complete')
        self.assertEqual(spec['race_splines'][0]['points'],[[0,0,0],[30,0,0],[60,0,0]])
        self.assertEqual(spec['race_splines'][0]['speed_sections'][1],{'start':20,'end':20,'speed_mps':5})
        self.assertEqual(spec['race_splines'][0]['width_sections'][0],{'from':10,'to':60,'left':2,'right':3})
        self.assertTrue(all(m['yaw']==30 for m in spec['markers']))
        self.assertEqual(len(spec['entities']),1)
        files, documents = generate_world.build_world_documents(spec,Path('raw'),Path('archive'))
        sector = documents[next(f.raw_path for f in files if f.kind=='quest_sector')]['Data']['RootChunk']
        refs = {r['$value'].split('/')[-1] for r in sector['nodeRefs']}
        for binding in plan['bindings']:
            self.assertIn(binding['ref'],refs)
            if 'trigger_ref' in binding:
                self.assertIn(binding['trigger_ref'],refs)
        generated_triggers = [n['Data'] for n in sector['nodes'] if n['Data']['$type']=='worldTriggerAreaNode']
        self.assertEqual(len(generated_triggers),3)
        self.assertEqual(generated_triggers[0]['outline']['Data']['height'],4)
        rotation = sector['nodeData']['Data'][0]['Orientation']
        self.assertAlmostEqual(rotation['k'],math.sin(math.radians(15)))
        again = self.races.export(self.race)
        self.assertEqual(json.loads(Path(again['world_spec_path']).read_text()),spec)
        self.assertNotEqual(again['manifest_path'],exported['manifest_path'])

    def test_draft_and_complete_export_report_missing_roles(self):
        with self.assertRaisesRegex(ScoutError,'Incomplete race'):
            self.races.export(self.race)
        draft = self.races.export(self.race,False)
        self.assertEqual(draft['status'],'draft')
        self.assertIn('finish',draft['missing'])
        self.assertIsNone(self.bridge.session)

    def test_loop_closure_and_tuning_use_three_dimensional_stations(self):
        self.complete()
        self.races.configure(self.race,looped=True,width_default=7,speed_mps=12)
        exported = self.races.export(self.race)
        spec = json.loads(Path(exported['world_spec_path']).read_text())
        self.assertTrue(spec['race_splines'][0]['looped'])
        self.assertEqual(exported['centreline_length_m'],120)
        self.assertEqual(spec['race_splines'][0]['width_default'],7)
        self.assertEqual(station({'x':5,'y':0,'z':10},[
            {'x':0,'y':0,'z':0},{'x':10,'y':0,'z':0},
            {'x':10,'y':0,'z':10},{'x':0,'y':0,'z':10}]),(25,0))

    def test_invalid_marks_and_metadata_leave_survey_unchanged(self):
        cases = [('unknown',{}),('speed_change',{}),('width_change',{'left_m':3}),
                 ('checkpoint',{'width_m':0}),('checkpoint',{'width_m':float('nan')}),
                 ('prop',{'entity_template':'../bad.ent'}),('reward',{'unknown':1})]
        for role,options in cases:
            with self.subTest(role=role,options=options), self.assertRaises(ScoutError):
                self.mark(role,options=options)
        with self.assertRaises(ScoutError):
            self.races.create('bad','../escape')
        self.assertEqual(self.races.get(self.race)['data']['marks'],[])

    def test_camera_marks_warn_and_duplicate_route_points_fail_export(self):
        self.complete()
        self.scout.mark_race(self.race,'spectator',source='camera')
        self.assertTrue(self.races.export(self.race)['warnings'])
        self.mark('spline_point',160,200,10)
        with self.assertRaisesRegex(ScoutError,'Adjacent'):
            self.races.export(self.race)

    def test_player_source_and_busy_controller_are_explicit(self):
        original = self.bridge.state
        self.bridge.state = lambda: {**original(),'player':{'x':4,'y':6,'z':8}}
        mark = self.scout.mark_race(self.race,'player_start',source='player')['mark']
        self.assertEqual(mark['position'],{'x':4.,'y':6.,'z':8.})
        self.scout.gate.acquire()
        try:
            with self.assertRaisesRegex(ScoutError,'operation is running'):
                self.scout.mark_race(self.race,'checkpoint')
        finally:
            self.scout.gate.release()

    def test_distinct_plans_share_owner_prefix_without_sharing_depot_identity(self):
        a = self.races.export(self.race,False)
        other = self.races.create('Another course','gqt_race')['id']
        b = self.races.export(other,False)
        sa = json.loads(Path(a['world_spec_path']).read_text())
        sb = json.loads(Path(b['world_spec_path']).read_text())
        self.assertNotEqual(sa['prefab_root'],sb['prefab_root'])
        self.assertNotEqual(sa['block_path'],sb['block_path'])
        self.assertTrue(sa['block_path'].startswith('mod\\gqt_race\\races\\'))

    def test_mcp_exposes_mark_edit_and_export_with_structured_results(self):
        from game_scout.server import make_server
        server = make_server(self.scout)
        async def check():
            names = {t.name for t in await server.list_tools()}
            self.assertTrue({'create_race','configure_race','mark_race','edit_race_mark','remove_race_mark','export_race','build_race'} <= names)
            result = await server.call_tool('mark_race',{'race_id':self.race,'role':'checkpoint','source':'manual',
                'position':{'x':0,'y':10,'z':0},'yaw':0,'options':{'width_m':12}})
            self.assertFalse(result.isError)
            result = await server.call_tool('export_race',{'race_id':self.race})
            self.assertTrue(result.isError)
            result = await server.call_tool('export_race',{'race_id':self.race,'require_complete':False})
            self.assertFalse(result.isError)
            self.assertEqual(result.structuredContent['status'],'draft')
        asyncio.run(check())


if __name__ == '__main__':
    unittest.main()
