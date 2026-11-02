"""Gameplay operations and evidence, independent of camera control."""
from __future__ import annotations

from contextlib import contextmanager
import json
import os
from pathlib import Path
import subprocess
import sys
import threading
import time

from .core import GameplayError, atomic_json, identifier, number
from .inputs import bindings, guard, validate_plan


class Gameplay:
    def __init__(self, bridge, library, images, binding_overrides=None):
        self.bridge, self.library, self.images = bridge, library, images
        self.bindings = bindings(binding_overrides)
        self.busy = threading.Lock()
        self.cancelled = threading.Event()
        self.cancel_file = None

    @contextmanager
    def operation(self):
        if not self.busy.acquire(blocking=False):
            raise GameplayError('Another operation is running; use stop to interrupt')
        try:
            yield
        finally:
            if self.cancelled.is_set():
                self.bridge.release()
            self.busy.release()

    def state(self):
        state = self.bridge.state()
        if state.get('product') != 'cyberpunk_mcp':
            raise GameplayError('Configuration points to a different CET mod')
        return state

    def begin(self):
        with self.operation():
            self.cancelled.clear()
            return self.bridge.begin(hide_hud=False)

    def stop(self):
        self.cancelled.set()
        path = self.cancel_file
        try:
            if path:
                atomic_json(path, {'stop': True})
        finally:
            # Retain exclusion locks until the input operation's finally runs.
            self.bridge.stop(release_when_stopped=False)
            if not self.busy.locked():
                self.bridge.release()
        return {'stop_requested': True, 'operation_running': self.busy.locked(),
                'message': 'Active input worker releases on its next check; actions are bounded to two seconds.'}

    def end(self):
        self.stop()
        # Never compete for the operation lock with a worker that is releasing.
        with self.operation():
            return self.bridge.end()

    def _observe(self, name='Gameplay observation'):
        image, evidence = self.images.frame(self.state, require_ready=False,
                                            cancelled=self.cancelled.is_set, timeout=8)
        record = self.images.save(image, evidence, name)
        return {'state': evidence['state'], 'image_id': record['id'],
                'path': record['data']['path'], 'preview_jpeg': self.images.preview(image)}

    def observe(self):
        with self.operation():
            self.cancelled.clear()
            return self._observe()

    def _run_worker(self, plan, before):
        self.cancel_file = self.library.root / 'runtime' / f'{identifier("cancel")}.json'
        request = {'plan': plan, 'parent_pid': os.getpid(), 'runtime': str(self.bridge.root.resolve()),
                   'session': self.bridge.session, 'boot': before['boot'],
                   'cancel_file': str(self.cancel_file.resolve())}
        # python -m keeps imports local to this separate package. No game_scout dependency.
        process = subprocess.Popen([sys.executable, '-m', 'cyberpunk_mcp.inputs'],
                                   cwd=Path(__file__).resolve().parent.parent,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
        try:
            if self.cancelled.is_set():
                atomic_json(self.cancel_file, {'stop': True})
            try:
                stdout, stderr = process.communicate(json.dumps(request), timeout=6)
            except subprocess.TimeoutExpired:
                atomic_json(self.cancel_file, {'stop': True})
                # Give the worker time to execute its release-finally before termination.
                try:
                    process.communicate(timeout=2)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.communicate()
                raise GameplayError('Input worker exceeded its deadline; inspect game input state')
            if process.returncode:
                raise GameplayError(f'Input worker failed: {stderr.strip()}')
            result = json.loads(stdout)
            if not result['ok']:
                raise GameplayError(result['error'])
            return result['result']
        finally:
            self.cancel_file.unlink(missing_ok=True)
            self.cancel_file = None

    def act(self, plan, name):
        validate_plan(plan)
        with self.operation():
            before = self.state()
            guard(before, self.bridge.session, before['boot'], plan.get('mode'))
            if self.cancelled.is_set():
                raise GameplayError('Stopped; begin a new session')
            started = time.time()
            evidence = {'plan': plan, 'before': before, 'started_at': started}
            try:
                evidence['input_result'] = self._run_worker(plan, before)
                # Wait for telemetry newer than the action, not the pre-action snapshot.
                baseline = self.state()['frame']
                deadline = time.monotonic() + 2
                while True:
                    after = self.state()
                    guard(after, self.bridge.session, before['boot'])
                    if after['frame'] > baseline:
                        break
                    if self.cancelled.is_set() or time.monotonic() >= deadline:
                        raise GameplayError('No fresh post-action telemetry')
                    time.sleep(0.025)
                observation = self._observe(name)
                evidence['after'] = observation['state']
                evidence['image_id'] = observation['image_id']
                evidence['outcome'] = 'completed_input'
                record = self.library.put('action', name, evidence)
                return {'action_id': record['id'], **evidence, **observation}
            except BaseException as error:
                self.stop()
                evidence.update(outcome='interrupted', error=str(error))
                self.library.put('action', name, evidence)
                raise

    def walk(self, forward=0, right=0, seconds=0.4, sprint=False, mouse_dx=0, mouse_dy=0):
        keys = self._axes(forward, right, 'forward', 'back')
        if sprint:
            keys[str(self.bindings['sprint'])] = 1
        return self.act({'keys': keys, 'seconds': seconds, 'mode': 'on_foot',
                         'mouse_dx': mouse_dx, 'mouse_dy': mouse_dy}, 'Walk')

    def _axes(self, forward, right, positive, negative):
        forward = number(forward, -1, 1, 'forward/throttle')
        right = number(right, -1, 1, 'right/steer')
        result = {}
        if forward:
            result[str(self.bindings[positive if forward > 0 else negative])] = abs(forward)
        if right:
            result[str(self.bindings['right' if right > 0 else 'left'])] = abs(right)
        return result

    def drive(self, throttle=0, steer=0, seconds=0.4, handbrake=False):
        keys = self._axes(throttle, steer, 'accelerate', 'brake_reverse')
        if handbrake:
            keys[str(self.bindings['handbrake'])] = 1
        return self.act({'keys': keys, 'seconds': seconds, 'mode': 'vehicle'}, 'Drive')

    def look(self, mouse_dx=0, mouse_dy=0, seconds=0.2):
        return self.act({'seconds': seconds, 'mouse_dx': mouse_dx, 'mouse_dy': mouse_dy}, 'Look')

    def press(self, action='interact', seconds=0.15):
        if action not in ('interact', 'exit_vehicle', 'jump', 'crouch'):
            raise GameplayError('Action must be interact, exit_vehicle, jump or crouch')
        mode = 'vehicle' if action == 'exit_vehicle' else 'on_foot' if action in ('jump', 'crouch') else None
        return self.act({'keys': {str(self.bindings[action]): 1}, 'seconds': seconds, 'mode': mode}, action)
