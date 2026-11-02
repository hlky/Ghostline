"""Bounded scan-code input. Each action runs in a separate release-owning process.

Windows API contract: https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-sendinput
"""
from __future__ import annotations

import ctypes as C
import json
import os
from pathlib import Path
import sys
import time

from .core import GameplayError, number, read_json

# Physical PC scan codes. Config overrides support rebound game controls.
DEFAULT_BINDINGS = {
    'forward': 0x11, 'back': 0x1F, 'left': 0x1E, 'right': 0x20,
    'interact': 0x21, 'exit_vehicle': 0x21, 'sprint': 0x2A,
    'jump': 0x39, 'crouch': 0x2E, 'handbrake': 0x39,
    'accelerate': 0x11, 'brake_reverse': 0x1F,
}


def bindings(overrides=None):
    result = dict(DEFAULT_BINDINGS)
    for key, value in (overrides or {}).items():
        if key not in result:
            raise GameplayError(f'Unknown binding: {key}')
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 0x7F:
            raise GameplayError('Bindings must be integer, non-extended scan codes 1..127')
        result[key] = value
    return result


def validate_plan(plan):
    duration = number(plan['seconds'], 0.05, 2, 'seconds')
    keys = plan.get('keys', {})
    if not isinstance(keys, dict):
        raise GameplayError('keys must be an object')
    for code, duty in keys.items():
        if not str(code).isdigit() or not 1 <= int(code) <= 127:
            raise GameplayError('Invalid scan code')
        number(duty, 0, 1, 'key duty')
    for axis in ('mouse_dx', 'mouse_dy'):
        number(plan.get(axis, 0), -2000, 2000, axis)
    if plan.get('mode') not in (None, 'on_foot', 'vehicle'):
        raise GameplayError('Invalid gameplay mode')
    return duration


def guard(state, session, boot, mode=None):
    if state.get('product') != 'cyberpunk_mcp' or state.get('protocol') != 1:
        raise GameplayError('Wrong telemetry runtime')
    age = time.time() - state.get('timestamp', 0)
    if not -1 <= age <= 2:
        raise GameplayError('Runtime heartbeat is stale')
    if state.get('boot') != boot or state.get('session') != session or not session:
        raise GameplayError('Gameplay session ended or CET restarted')
    if not state.get('ready') or state.get('freefly_active') or state.get('paused') or state.get('in_menu') or state.get('loading') or state.get('overlay_open'):
        raise GameplayError('Gameplay became unavailable; disable FreeFly and close menus/CET')
    if mode and state.get('mode') != mode:
        raise GameplayError(f'Expected {mode}, runtime is {state.get("mode")}')


class Keyboard(C.Structure):
    _fields_ = [('vk', C.c_uint16), ('scan', C.c_uint16), ('flags', C.c_uint32),
                ('time', C.c_uint32), ('extra', C.c_size_t)]


class Mouse(C.Structure):
    _fields_ = [('dx', C.c_int32), ('dy', C.c_int32), ('data', C.c_uint32),
                ('flags', C.c_uint32), ('time', C.c_uint32), ('extra', C.c_size_t)]


class Hardware(C.Structure):
    _fields_ = [('message', C.c_uint32), ('low', C.c_uint16), ('high', C.c_uint16)]


class Payload(C.Union):
    _fields_ = [('keyboard', Keyboard), ('mouse', Mouse), ('hardware', Hardware)]


class Input(C.Structure):
    _fields_ = [('type', C.c_uint32), ('payload', Payload)]


class WindowsInput:
    def __init__(self, parent_pid=None):
        if os.name != 'nt':
            raise GameplayError('Gameplay input requires Windows')
        self.user = C.WinDLL('user32', use_last_error=True)
        self.kernel = C.WinDLL('kernel32', use_last_error=True)
        self.user.SendInput.argtypes = [C.c_uint32, C.POINTER(Input), C.c_int]
        self.user.SendInput.restype = C.c_uint32
        self.user.GetForegroundWindow.restype = C.c_void_p
        self.user.GetWindowThreadProcessId.argtypes = [C.c_void_p, C.POINTER(C.c_uint32)]
        self.user.GetAsyncKeyState.argtypes = [C.c_int]
        self.user.GetAsyncKeyState.restype = C.c_short
        self.kernel.OpenProcess.argtypes = [C.c_uint32, C.c_int, C.c_uint32]
        self.kernel.OpenProcess.restype = C.c_void_p
        self.kernel.QueryFullProcessImageNameW.argtypes = [C.c_void_p, C.c_uint32, C.c_wchar_p, C.POINTER(C.c_uint32)]
        self.kernel.CloseHandle.argtypes = [C.c_void_p]
        self.kernel.WaitForSingleObject.argtypes = [C.c_void_p, C.c_uint32]
        self.held = set()
        self.parent = self.kernel.OpenProcess(0x100000, False, parent_pid) if parent_pid else None
        if parent_pid and not self.parent:
            raise GameplayError('Cannot monitor input controller process')

    def focused(self):
        hwnd = self.user.GetForegroundWindow()
        pid = C.c_uint32()
        self.user.GetWindowThreadProcessId(hwnd, C.byref(pid))
        handle = self.kernel.OpenProcess(0x1000, False, pid.value)
        if not handle:
            return False
        try:
            path = C.create_unicode_buffer(32768)
            length = C.c_uint32(len(path))
            return bool(self.kernel.QueryFullProcessImageNameW(handle, 0, path, C.byref(length))) and Path(path.value).name.lower() == 'cyberpunk2077.exe'
        finally:
            self.kernel.CloseHandle(handle)

    def check(self):
        if self.parent and self.kernel.WaitForSingleObject(self.parent, 0) != 0x102:
            raise GameplayError('Input controller exited')
        if self.user.GetAsyncKeyState(0x77) & 0x8000:  # F8; no game binding required.
            raise GameplayError('Emergency stop (F8)')
        if not self.focused():
            raise GameplayError('Cyberpunk2077.exe must remain the foreground application')

    def check_initial_keys(self, codes):
        for code in codes:
            vk = self.user.MapVirtualKeyW(code, 3)
            if self.user.GetAsyncKeyState(vk) & 0x8000:
                raise GameplayError('A requested control is already held; release manual controls before agent input')

    def send(self, event):
        if self.user.SendInput(1, C.byref(event), C.sizeof(Input)) != 1:
            raise GameplayError('SendInput failed; game and MCP must run at the same privilege level')

    def key(self, code, down):
        event = Input(type=1)
        event.payload.keyboard = Keyboard(scan=code, flags=0x8 | (0 if down else 0x2))
        if down:
            # Track before injecting so even ambiguous failures trigger key-up.
            self.held.add(code)
        self.send(event)
        if not down:
            self.held.discard(code)

    def mouse(self, dx, dy):
        if dx or dy:
            event = Input(type=0)
            event.payload.mouse = Mouse(dx=dx, dy=dy, flags=0x1)
            self.send(event)

    def release(self):
        errors = []
        for code in list(self.held):
            try:
                self.key(code, False)
            except GameplayError as error:
                errors.append(str(error))
        if errors:
            raise GameplayError('Input release failed: ' + '; '.join(errors))

    def close(self):
        try:
            self.release()
        finally:
            if self.parent:
                self.kernel.CloseHandle(self.parent)
                self.parent = None


def execute(plan, device, state_reader, session, boot, cancelled=lambda: False,
            clock=time.monotonic, sleep=time.sleep):
    """Run at most two seconds; validate before every tick and always release."""
    duration = validate_plan(plan)
    keys = {int(k): float(v) for k, v in plan.get('keys', {}).items()}
    start = clock()
    sent_x = sent_y = 0
    ticks = 0
    try:
        device.check_initial_keys(keys)
        while True:
            elapsed = clock() - start
            if cancelled():
                raise GameplayError('Operation stopped')
            device.check()
            guard(state_reader(), session, boot, plan.get('mode'))
            if elapsed >= duration:
                break
            # 200 ms pulse-width modulation permits fractional driving inputs.
            phase = (elapsed % 0.2) / 0.2
            wanted = {code for code, duty in keys.items() if duty > phase}
            for code in sorted(device.held - wanted):
                device.key(code, False)
            for code in sorted(wanted - device.held):
                device.key(code, True)
            fraction = min(1, (elapsed + 0.02) / duration)
            x, y = (round(plan.get(axis, 0) * fraction) for axis in ('mouse_dx', 'mouse_dy'))
            device.mouse(x - sent_x, y - sent_y)
            sent_x, sent_y = x, y
            ticks += 1
            sleep(min(0.02, max(0, duration - (clock() - start))))
    finally:
        device.release()
    return {'elapsed_seconds': clock() - start, 'ticks': ticks, 'inputs_released': True,
            'mouse_counts': {'dx': sent_x, 'dy': sent_y}}


def main():
    request = json.load(sys.stdin)
    device = WindowsInput(request['parent_pid'])
    try:
        result = execute(request['plan'], device,
                         lambda: read_json(Path(request['runtime']) / 'state.json'),
                         request['session'], request['boot'],
                         lambda: Path(request['cancel_file']).exists())
        print(json.dumps({'ok': True, 'result': result}))
    except (GameplayError, OSError, ValueError, KeyError) as error:
        print(json.dumps({'ok': False, 'error': str(error)}))
    finally:
        device.close()


if __name__ == '__main__':
    main()
