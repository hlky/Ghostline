"""Independent scout transport, library, cancellation and MCP contract tests."""
import asyncio
from contextlib import suppress
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import types
import unittest
from unittest import mock

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from game_scout.core import Bridge, Library, ScoutError, angles, atomic_json, cell, file_lock, number, read_json
from game_scout.controller import Scout


class FakeBridge:
    def __init__(self):
        self.session = None
        self.pose = {'x':0.,'y':0.,'z':1.7,'yaw':0.,'pitch':0.}
        self.commands = []
        self.stopped = False

    def state(self):
        return {'protocol':1,'boot':'test','timestamp':time.time(),'session':self.session,
                'camera':dict(self.pose),'ready':True,'frame':100,'loading':False,'freefly_active':True}

    def begin(self,hide_hud=True):
        self.session = 'test-session'; self.stopped = False
        return self.state()

    def command(self,kind,**args):
        if self.stopped:
            raise ScoutError('Operation stopped')
        self.commands.append((kind,args))
        if kind == 'pose':
            self.pose = args['pose']
        if kind == 'inspect':
            return {'hit':True,'position':{'x':0,'y':10,'z':1.7}}
        return self.state()

    def release(self):
        self.session = None

    def end(self):
        self.release(); return {'released':True}

    def stop(self):
        self.stopped = True


class FakeImages:
    def __init__(self,library):
        self.library = library
        self.saved = 0

    def frame(self,state_reader,**kwargs):
        from PIL import Image
        if kwargs['cancelled']():
            raise ScoutError('Operation stopped')
        return Image.new('RGB',(64,36),(30,80,120)), {'state':state_reader(),'presentation_timestamp':10}

    def preview(self,image):
        from game_scout.images import CameraImages
        return CameraImages.preview(image)

    def save(self,image,evidence,name):
        from game_scout.images import CameraImages
        self.saved += 1
        return CameraImages(self.library).save(image,evidence,name)


class ScoutTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.library = Library(Path(self.directory.name))
        self.bridge = FakeBridge()
        self.images = FakeImages(self.library)
        self.scout = Scout(self.bridge,self.library,self.images)

    def test_coordinates_use_camera_forward_and_world_vertical(self):
        self.scout.move(forward=8,right=2,up=1)
        self.assertEqual(self.bridge.pose,{'x':2.,'y':8.,'z':2.7,'yaw':0.,'pitch':0.})
        self.bridge.pose['yaw'] = 90
        self.scout.move(forward=4)
        self.assertAlmostEqual(self.bridge.pose['x'],-2)
        self.assertAlmostEqual(self.bridge.pose['y'],8)

    def test_long_travel_requires_explicit_teleport(self):
        pose = {**self.bridge.pose,'x':1000}
        with self.assertRaisesRegex(ScoutError,'allow_teleport'):
            self.scout.go_to(pose)
        self.assertEqual(self.bridge.commands,[])
        self.scout.go_to(pose,allow_teleport=True)
        self.assertTrue(self.bridge.commands[-1][1]['teleport'])

    def test_inspection_rejects_stale_image_pose(self):
        self.scout.begin()
        self.assertTrue(self.scout.inspect()['hit'])
        self.bridge.pose['yaw'] += 5
        with self.assertRaisesRegex(ScoutError,'moved'):
            self.scout.inspect()

    def test_locations_connections_and_export_preserve_independent_views(self):
        courtyard = self.scout.save_location('Courtyard',tags=['meeting'])
        street = self.scout.save_location('Street')
        view = self.scout.save_viewpoint('Entrance',location_id=courtyard['id'])
        self.assertEqual(self.library.get(courtyard['id'])['data']['viewpoint_ids'],[view['viewpoint']['id']])
        connection = self.scout.connect(street['id'],courtyard['id'],'passage')
        self.assertEqual(connection['data']['to_id'],courtyard['id'])
        exported = json.loads(Path(self.library.export()).read_text())
        self.assertEqual(len(exported['records']),5)
        image = self.library.get(view['saved_image']['id'])
        self.assertTrue(Path(image['data']['path']).with_suffix('.json').is_file())
        self.assertEqual(len(self.library.list('location','meeting')),1)

    def test_routes_record_completed_poses_and_replay_in_background(self):
        route = self.scout.record_route('Alley')
        self.scout.move(forward=5)
        self.scout.capture()
        finished = self.scout.record_route()
        self.assertEqual(finished['id'],route['id'])
        self.assertEqual(len(finished['data']['waypoints']),3)
        self.scout.start_job('replay',route_id=route['id'])
        self.scout.job_thread.join(3)
        self.assertEqual(self.scout.job['status'],'completed')
        self.assertEqual(self.scout.job['completed'],3)
        self.assertEqual(len(self.library.get(route['id'])['data']['waypoints']),3)
        restored = Scout(self.bridge,self.library,self.images)
        self.assertEqual(restored.job['next_index'],3)
        restored.start_job('replay',route_id=route['id'],start_index=2)
        restored.job_thread.join(3)
        self.assertEqual(restored.job['completed'],1)

    def test_sweep_returns_three_distinct_angles_and_all_images(self):
        result = self.scout.sweep()
        yaws = [v['observation']['state']['camera']['yaw'] for v in result['views']]
        self.assertEqual(yaws,[315,0,45])
        self.assertEqual(len(result['preview_jpegs']),3)
        self.assertEqual(self.images.saved,3)

    def test_orbit_aims_inward_and_keeps_radius(self):
        result = self.scout.orbit({'x':0,'y':10,'z':1.7},radius_m=5,count=4)
        self.assertEqual(len(result['views']),4)
        for view in result['views']:
            pose = view['observation']['state']['camera']
            self.assertAlmostEqual(math.hypot(pose['x'],pose['y']-10),5)

    def test_autonomous_scout_is_bounded_and_persists_replay_route(self):
        self.scout.start_job('scout',maximum_steps=3,radius_m=25,step_m=8,maximum_seconds=10)
        self.scout.job_thread.join(3)
        self.assertEqual(self.scout.job['status'],'completed')
        self.assertLessEqual(self.scout.job['completed'],3)
        route = self.library.get(self.scout.job['route_id'])
        self.assertLessEqual(len(route['data']['waypoints']),4)
        for step in route['data']['waypoints']:
            self.assertLessEqual(math.hypot(step['pose']['x'],step['pose']['y']),25)

    def test_stop_remains_callable_during_job(self):
        reached = threading.Event()
        original = self.bridge.command
        def slow(kind,**kwargs):
            reached.set()
            while not self.scout.cancelled.wait(0.01):
                pass
            return original(kind,**kwargs)
        self.bridge.command = slow
        self.scout.start_job('scout',maximum_steps=10)
        self.assertTrue(reached.wait(1))
        with self.assertRaisesRegex(ScoutError,'running'):
            self.scout.move(1)
        started = time.monotonic()
        self.scout.stop()
        self.assertLess(time.monotonic()-started,0.1)
        self.scout.job_thread.join(2)
        self.assertEqual(self.scout.job['status'],'cancelled')
        self.assertFalse(self.scout.gate.locked())

    def test_coverage_distinguishes_floors_and_headings(self):
        self.library.visit(self.bridge.pose)
        self.assertEqual(self.library.visits(self.bridge.pose),1)
        self.assertNotEqual(cell(self.bridge.pose),cell({**self.bridge.pose,'z':20}))
        with self.assertRaises(ScoutError):
            number(float('nan'),0,1,'test')
        self.assertEqual(angles({'x':0,'y':0,'z':0},{'x':-10,'y':0,'z':0})['yaw'],90)

    def test_mcp_tools_return_real_image_content_and_errors(self):
        from game_scout.server import make_server
        server = make_server(self.scout)
        async def check():
            tools = await server.list_tools()
            names = {t.name for t in tools}
            self.assertTrue({'move','inspect','sweep','orbit','autonomous_scout','replay_route','stop','read_image','connect_locations'} <= names)
            result = await server.call_tool('begin_session',{})
            # FastMCP preserves explicit CallToolResult values.
            self.assertFalse(result.isError)
            self.assertTrue(any(c.type=='image' for c in result.content))
            result = await server.call_tool('go_to',{'pose':{**self.bridge.pose,'x':1000}})
            self.assertTrue(result.isError)
        asyncio.run(check())

    def test_mcp_stop_interrupts_foreground_tool_without_blocking_event_loop(self):
        from game_scout.server import make_server
        server = make_server(self.scout)
        entered = threading.Event()
        def command(kind,**args):
            entered.set()
            self.scout.cancelled.wait(2)
            raise ScoutError('Operation stopped')
        self.bridge.command = command
        async def check():
            moving = asyncio.create_task(server.call_tool('move',{'forward':5}))
            self.assertTrue(await asyncio.to_thread(entered.wait,1))
            result = await asyncio.wait_for(server.call_tool('stop',{}),0.5)
            self.assertFalse(result.isError)
            self.assertTrue((await moving).isError)
        asyncio.run(check())


class TransportTests(unittest.TestCase):
    def test_install_only_writes_its_own_mod(self):
        from game_scout.cli import install
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            capture = root/'game/bin/x64/plugins/cyber_engine_tweaks/mods/world_location_capture/init.lua'
            capture.parent.mkdir(parents=True)
            capture.write_text('leave this running')
            result = install(root/'game',root/'data',root/'config.json')
            self.assertTrue((Path(result['mod'])/'engine.lua').is_file())
            self.assertEqual(capture.read_text(),'leave this running')

    def test_competing_capture_lock_prevents_scout_begin(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            bridge=Bridge(root/'scout',root/'capture/controller.lock')
            try:
                with file_lock(root/'capture/controller.lock'):
                    with self.assertRaisesRegex(ScoutError,'Another controller'):
                        bridge.begin()
                self.assertFalse((root/'scout/command.json').exists())
            finally:
                bridge.close()

    def test_server_speaks_mcp_over_stdio_without_a_running_game(self):
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client
        repo=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            config=root/'config.json'
            atomic_json(config,{'schema_version':1,'runtime':str(root/'runtime'),'data_root':str(root/'library')})
            async def check():
                params=StdioServerParameters(command=sys.executable,args=[str(repo/'tools/game_scout_mcp.py'),'--config',str(config),'serve'])
                async with stdio_client(params) as (read,write):
                    async with ClientSession(read,write) as session:
                        initialized=await session.initialize()
                        self.assertEqual(initialized.serverInfo.name,'game_scout')
                        tools=await session.list_tools()
                        self.assertGreaterEqual(len(tools.tools),24)
                        result=await session.call_tool('search_library',{})
                        self.assertFalse(result.isError)
                        self.assertEqual(result.structuredContent['records'],[])
                        self.assertTrue((await session.call_tool('state',{})).isError)
            asyncio.run(check())

    def test_exclusive_lock_and_stale_runtime(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with file_lock(root/'lock'):
                with self.assertRaises(ScoutError):
                    with file_lock(root/'lock'):
                        pass
            atomic_json(root/'state.json',{'protocol':1,'timestamp':time.time()-60})
            bridge = Bridge(root)
            try:
                with self.assertRaisesRegex(ScoutError,'stale'):
                    bridge.state()
            finally:
                bridge.close()

    def test_transport_correlates_response_and_releases_on_stop(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            ended = threading.Event()
            active = None
            seen = None
            def runtime():
                nonlocal active,seen
                while not ended.wait(0.01):
                    try:
                        command = read_json(root/'command.json')
                        if command['id'] != seen:
                            seen = command['id']
                            active = command['session'] if command['kind']=='begin' else active
                            if command['kind']=='end': active=None
                            atomic_json(root/'response.json',{'id':seen,'session':command['session'],'boot':'test','ok':True,'result':{'session':active}})
                    except ScoutError:
                        pass
                    with suppress(ScoutError):
                        if read_json(root/'stop.json').get('session')==active:
                            active=None
                    atomic_json(root/'state.json',{'boot':'test','protocol':1,'session':active,'timestamp':time.time()})
            atomic_json(root/'state.json',{'boot':'test','protocol':1,'timestamp':time.time()})
            worker = threading.Thread(target=runtime)
            worker.start()
            bridge = Bridge(root)
            try:
                self.assertIsNotNone(bridge.begin()['session'])
                self.assertEqual(bridge.command('inspect')['session'],bridge.session)
                bridge.stop()
                deadline=time.monotonic()+2
                while bridge.session and time.monotonic()<deadline:
                    time.sleep(0.02)
                self.assertIsNone(bridge.session)
                with file_lock(root/'controller.lock'):
                    pass
            finally:
                bridge.close(); ended.set(); worker.join(2)

    @unittest.skipUnless(shutil.which('lua'),'Lua required')
    def test_native_camera_collision_loading_and_cleanup_harness(self):
        repo=Path(__file__).resolve().parents[1]
        result=subprocess.run(['lua',str(repo/'tests/game_scout_engine_harness.lua'),str(repo/'tools/game_scout/cet/engine.lua')],capture_output=True,text=True,timeout=10)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)


class ImageTests(unittest.TestCase):
    def test_fresh_frame_waits_out_loading_and_records_actual_pixels(self):
        import numpy as np
        from game_scout.images import CameraImages
        started=time.monotonic()
        ticks=0
        instances=[]
        def state():
            nonlocal ticks
            ticks+=1
            return {'boot':'test','frame':ticks,'loading':time.monotonic()-started<0.05,
                    'ready':True,'camera':{'x':1,'y':2,'z':3,'yaw':0,'pitch':0}}
        class Backend:
            def __init__(self,**kwargs):
                assert kwargs['draw_border'] is None
                self.handlers={};self.finished=threading.Event();instances.append(self)
            def event(self,function):
                self.handlers[function.__name__]=function
            def stop(self):
                # The capture owner must stop the backend, never its callback.
                assert threading.current_thread() is not self.worker
                self.finished.set()
                self.worker.join(1)
                assert not self.worker.is_alive()
            def is_finished(self):
                return self.finished.is_set()
            def start_free_threaded(self):
                def emit():
                    for stamp in range(400):
                        if self.finished.wait(0.005): return
                        pixels=np.full((36,64,4),255,dtype='uint8')
                        pixels[:,:,:3]=[20,80,200]
                        self.handlers['on_frame_arrived'](types.SimpleNamespace(timespan=stamp,frame_buffer=pixels,width=64,height=36),self)
                self.worker=threading.Thread(target=emit)
                self.worker.start();return self
        with tempfile.TemporaryDirectory() as directory:
            images=CameraImages(Library(Path(directory)))
            with mock.patch('game_scout.images.game_window',return_value='fake'), mock.patch.dict(sys.modules,{'windows_capture':types.SimpleNamespace(WindowsCapture=Backend)}):
                try:
                    image,evidence=images.frame(state,timeout=2)
                    self.assertEqual(image.getpixel((0,0)),(200,80,20))
                    self.assertFalse(evidence['state']['loading'])
                    self.assertEqual(evidence['state']['camera']['z'],3)
                finally:
                    instances[0].worker.join(1)


if __name__=='__main__':
    unittest.main()
