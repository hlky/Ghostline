"""Gameplay controls without a running game or synthesized user input."""
from __future__ import annotations

import asyncio
import ctypes
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))

from cyberpunk_mcp.cli import install
from cyberpunk_mcp.controller import Gameplay
from cyberpunk_mcp.core import Bridge, GameplayError, Library, atomic_json, file_lock
from cyberpunk_mcp.inputs import Input, WindowsInput, bindings, execute, guard


def state(**changes):
    return {'product': 'cyberpunk_mcp', 'protocol': 1, 'timestamp': time.time(), 'ready': True,
            'session': 'session', 'boot': 'boot', 'mode': 'on_foot', 'frame': 10,
            'freefly_active': False, 'paused': False, 'loading': False,
            'overlay_open': False, **changes}


class Clock:
    def __init__(self):
        self.value = 0

    def now(self):
        return self.value

    def sleep(self, delta):
        self.value += delta


class Device:
    def __init__(self, fail_at=None):
        self.held = set()
        self.events = []
        self.checks = 0
        self.fail_at = fail_at

    def check_initial_keys(self, codes):
        pass

    def check(self):
        self.checks += 1
        if self.checks == self.fail_at:
            raise GameplayError('Focus lost')

    def key(self, code, down):
        self.events.append((code, down))
        if down:
            self.held.add(code)
        else:
            self.held.discard(code)

    def mouse(self, x, y):
        self.events.append(('mouse', x, y))

    def release(self):
        for code in list(self.held):
            self.key(code, False)


class InputTests(unittest.TestCase):
    def run_plan(self, device=None, reader=state, cancel=lambda: False, **plan):
        clock = Clock()
        device = device or Device()
        result = execute({'seconds': .4, 'keys': {'17': 1}, **plan}, device, reader,
                         'session', 'boot', cancel, clock.now, clock.sleep)
        return result, device

    def test_walk_holds_then_releases_and_turns(self):
        result, device = self.run_plan(mouse_dx=123, mouse_dy=-47)
        self.assertEqual(device.held, set())
        self.assertEqual([e for e in device.events if e[0] == 17], [(17, True), (17, False)])
        self.assertEqual(sum(e[1] for e in device.events if e[0] == 'mouse'), 123)
        self.assertEqual(sum(e[2] for e in device.events if e[0] == 'mouse'), -47)
        self.assertLessEqual(result['elapsed_seconds'], .401)

    def test_partial_steering_pulses_and_releases(self):
        _, device = self.run_plan(keys={'32': .5}, mode='vehicle', reader=lambda: state(mode='vehicle'))
        events = [e for e in device.events if e[0] == 32]
        self.assertGreaterEqual(len(events), 4)
        self.assertEqual(events[-1], (32, False))

    def test_focus_loss_releases_held_keys(self):
        device = Device(fail_at=3)
        with self.assertRaisesRegex(GameplayError, 'Focus lost'):
            self.run_plan(device)
        self.assertIn((17, True), device.events)
        self.assertEqual(device.events[-1], (17, False))
        self.assertFalse(device.held)

    def test_stop_releases_held_keys(self):
        device = Device()
        with self.assertRaisesRegex(GameplayError, 'stopped'):
            self.run_plan(device, cancel=lambda: device.checks >= 2)
        self.assertFalse(device.held)
        self.assertEqual(device.events[-1], (17, False))

    def test_runtime_change_releases_keys(self):
        for change in ({'freefly_active': True}, {'paused': True}, {'loading': True},
                       {'overlay_open': True}, {'in_menu': True}, {'session': None}, {'boot': 'new'},
                       {'timestamp': 0}, {'mode': 'vehicle'}, {'ready': False}):
            with self.subTest(change=change):
                device = Device()
                def reader():
                    return state(**change) if device.checks >= 3 else state()
                with self.assertRaises(GameplayError):
                    self.run_plan(device, reader=reader, mode='on_foot')
                self.assertFalse(device.held)
                self.assertEqual(device.events[-1], (17, False))

    def test_invalid_input_never_injects(self):
        for plan in ({'seconds': 3}, {'seconds': float('nan')}, {'mouse_dx': float('inf')},
                     {'keys': {'17': -1}}, {'keys': {'900': 1}}, {'mode': 'flying'}):
            device = Device()
            with self.subTest(plan=plan), self.assertRaises(GameplayError):
                self.run_plan(device, **plan)
            self.assertFalse(device.events)

    def test_no_session_or_wrong_runtime_rejected(self):
        for change in ({'product': 'game_scout'}, {'protocol': 99}, {'session': None}):
            with self.assertRaises(GameplayError):
                guard(state(**change), 'session', 'boot')

    def test_win32_input_abi_size(self):
        self.assertEqual(ctypes.sizeof(Input), 40 if ctypes.sizeof(ctypes.c_void_p) == 8 else 28)

    def test_native_backend_emits_scan_code_down_up_and_relative_mouse(self):
        device = WindowsInput.__new__(WindowsInput)
        device.held = set()
        device.user = Mock()
        events = []
        def send(count, pointer, size):
            self.assertEqual((count, size), (1, ctypes.sizeof(Input)))
            event = ctypes.cast(pointer, ctypes.POINTER(Input)).contents
            if event.type == 1:
                events.append(('key', event.payload.keyboard.scan, event.payload.keyboard.flags))
            else:
                events.append(('mouse', event.payload.mouse.dx, event.payload.mouse.dy, event.payload.mouse.flags))
            return 1
        device.user.SendInput.side_effect = send
        device.key(17, True)
        device.mouse(12, -4)
        device.release()
        self.assertEqual(events, [('key', 17, 8), ('mouse', 12, -4, 1), ('key', 17, 10)])
        self.assertFalse(device.held)

    def test_ambiguous_keydown_failure_still_attempts_release(self):
        device = WindowsInput.__new__(WindowsInput)
        device.held = set()
        device.user = Mock()
        device.user.SendInput.side_effect = [0, 1]
        with self.assertRaisesRegex(GameplayError, 'SendInput failed'):
            device.key(17, True)
        self.assertEqual(device.held, {17})
        device.release()
        self.assertFalse(device.held)

    def test_custom_bindings(self):
        self.assertEqual(bindings({'interact': 18})['interact'], 18)
        for override in ({'forward': True}, {'interact': 999}, {'shoot': 3}):
            with self.assertRaises(GameplayError):
                bindings(override)


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.library = Library(Path(self.temp.name))
        self.bridge = Mock(session='session', root=Path(self.temp.name))
        self.bridge.state.side_effect = lambda: state()
        self.game = Gameplay(self.bridge, self.library, Mock())

    def test_axis_bindings_and_context(self):
        with patch.object(self.game, 'act', side_effect=lambda p, n: p):
            walk = self.game.walk(forward=-1, right=.5, sprint=True)
            self.assertEqual(walk['keys'], {'31': 1, '32': .5, '42': 1})
            self.assertEqual(walk['mode'], 'on_foot')
            drive = self.game.drive(throttle=-1, steer=-.3, handbrake=True)
            self.assertEqual(drive['keys'], {'31': 1, '30': .3, '57': 1})
            self.assertEqual(drive['mode'], 'vehicle')
            self.assertEqual(self.game.press('exit_vehicle', 1)['mode'], 'vehicle')
            self.assertIsNone(self.game.press('interact')['mode'])

    def test_mode_guard_prevents_worker_launch(self):
        with patch.object(self.game, '_run_worker') as worker:
            with self.assertRaisesRegex(GameplayError, 'Expected vehicle'):
                self.game.drive(throttle=1)
            worker.assert_not_called()

    def test_interruption_is_persisted_and_stops_session(self):
        with patch.object(self.game, '_run_worker', side_effect=GameplayError('Focus lost')):
            with self.assertRaisesRegex(GameplayError, 'Focus lost'):
                self.game.walk(forward=1)
        record = self.library.list(kind='action')[0]
        self.assertEqual(record['data']['outcome'], 'interrupted')
        self.bridge.stop.assert_called()

    def test_busy_operation_does_not_block_stop(self):
        with self.game.operation():
            result = self.game.stop()
            self.assertTrue(result['operation_running'])
            self.bridge.release.assert_not_called()
            with self.assertRaisesRegex(GameplayError, 'Another operation'):
                self.game.walk()
        self.bridge.release.assert_called_once()
        self.bridge.stop.assert_called_with(release_when_stopped=False)

    def test_observe_available_after_stop(self):
        self.game.stop()
        with patch.object(self.game, '_observe', return_value={'image_id': 'test'}):
            self.assertEqual(self.game.observe()['image_id'], 'test')
        self.assertFalse(self.game.cancelled.is_set())

    def test_worker_request_stop_and_separate_package(self):
        process = Mock(returncode=0)
        process.communicate.return_value = (json.dumps({'ok': True, 'result': {'inputs_released': True}}), '')
        with patch('cyberpunk_mcp.controller.subprocess.Popen', return_value=process) as popen:
            self.game.cancelled.set()
            def communicate(raw, timeout):
                request = json.loads(raw)
                self.assertTrue(Path(request['cancel_file']).exists())
                self.assertEqual(request['session'], 'session')
                self.assertGreater(request['parent_pid'], 0)
                return json.dumps({'ok': True, 'result': {'inputs_released': True}}), ''
            process.communicate.side_effect = communicate
            result = self.game._run_worker({'seconds': .1}, state())
            self.assertTrue(result['inputs_released'])
            self.assertIn('cyberpunk_mcp.inputs', popen.call_args.args[0])
            self.assertIsNone(self.game.cancel_file)

    def test_success_persists_before_after_and_image(self):
        frames = iter([state(frame=1), state(frame=2), state(frame=3)])
        self.bridge.state.side_effect = lambda: next(frames)
        with patch.object(self.game, '_run_worker', return_value={'inputs_released': True}), \
             patch.object(self.game, '_observe', return_value={'state': state(frame=4), 'image_id': 'image', 'preview_jpeg': b'jpeg'}):
            result = self.game.walk(forward=1)
        record = self.library.get(result['action_id'])
        self.assertEqual(record['data']['before']['frame'], 1)
        self.assertEqual(record['data']['after']['frame'], 4)
        self.assertEqual(record['data']['image_id'], 'image')


class InstallTests(unittest.TestCase):
    def test_install_is_independent_and_preserves_bindings(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mods = root / 'game/bin/x64/plugins/cyber_engine_tweaks/mods'
            (mods / 'game_scout').mkdir(parents=True)
            scout = mods / 'game_scout/init.lua'
            scout.write_text('existing scout')
            config = root / 'config.json'
            install(root / 'game', root / 'library', config)
            data = json.loads(config.read_text())
            data['bindings'] = {'interact': 18}
            atomic_json(config, data)
            again = install(root / 'game', root / 'library', config)
            self.assertEqual(scout.read_text(), 'existing scout')
            self.assertTrue((mods / 'cyberpunk_mcp/init.lua').exists())
            self.assertTrue(Path(again['backup']).is_dir())
            self.assertEqual(json.loads(config.read_text())['bindings'], {'interact': 18})

    def test_competing_scout_lock_blocks_gameplay(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            bridge = Bridge(root / 'runtime', [root / 'scout/controller.lock'])
            try:
                with file_lock(root / 'scout/controller.lock'):
                    with self.assertRaisesRegex(GameplayError, 'Another controller'):
                        bridge.begin()
                self.assertIsNone(bridge.session)
            finally:
                bridge.close()

    @unittest.skipUnless(shutil.which('lua'), 'Lua interpreter unavailable')
    def test_lua_runtime_harness(self):
        result = subprocess.run(['lua', str(ROOT / 'tests/cyberpunk_mcp_runtime.lua'),
                                 str(ROOT / 'tools/cyberpunk_mcp/cet')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_mcp_surface(self):
        from cyberpunk_mcp.server import make_server
        tools = asyncio.run(make_server(Mock()).list_tools())
        names = {tool.name for tool in tools}
        self.assertTrue({'walk', 'look', 'interact', 'drive', 'stop', 'begin_session', 'observe'} <= names)
        self.assertNotIn('go_to', names)

    def test_real_stdio_server_without_touching_game(self):
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client

        async def check(config):
            params = StdioServerParameters(command=sys.executable, args=[
                str(ROOT / 'tools/cyberpunk_mcp.py'), '--config', str(config), 'serve'],
                cwd=str(config.parent))
            async with stdio_client(params) as (reader, writer):
                async with ClientSession(reader, writer) as client:
                    await client.initialize()
                    listed = await client.list_tools()
                    self.assertIn('drive', {tool.name for tool in listed.tools})
                    capabilities = await client.call_tool('capabilities', {})
                    self.assertFalse(capabilities.isError)
                    self.assertTrue(capabilities.structuredContent['freefly_must_be_disabled'])
                    missing = await client.call_tool('state', {})
                    self.assertTrue(missing.isError)
                    # No runtime, so input must be rejected before a worker starts.
                    rejected = await client.call_tool('walk', {'forward': 1, 'seconds': .1})
                    self.assertTrue(rejected.isError)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            config = root / 'config.json'
            atomic_json(config, {'schema_version': 1, 'runtime': str(root / 'runtime'),
                                 'data_root': str(root / 'library'), 'competing_locks': []})
            asyncio.run(asyncio.wait_for(check(config), timeout=20))

if __name__ == '__main__':
    unittest.main()
