"""Fresh Windows game-window images, independent of the batch capture backend."""
from __future__ import annotations

import ctypes
from ctypes import wintypes
from io import BytesIO
import os
from pathlib import Path
import threading
import time

from .core import ScoutError, identifier


def game_window():
    if os.name != 'nt':
        raise ScoutError('Live game capture requires Windows')
    user = ctypes.WinDLL('user32', use_last_error=True)
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.OpenProcess.argtypes = [wintypes.DWORD,wintypes.BOOL,wintypes.DWORD]
    kernel.OpenProcess.restype = wintypes.HANDLE
    kernel.QueryFullProcessImageNameW.argtypes = [wintypes.HANDLE,wintypes.DWORD,wintypes.LPWSTR,ctypes.POINTER(wintypes.DWORD)]
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    user.IsWindowVisible.argtypes = [wintypes.HWND]
    user.GetWindowThreadProcessId.argtypes = [wintypes.HWND,ctypes.POINTER(wintypes.DWORD)]
    user.GetWindowTextW.argtypes = [wintypes.HWND,wintypes.LPWSTR,ctypes.c_int]
    found = []
    callback_type = ctypes.WINFUNCTYPE(wintypes.BOOL,wintypes.HWND,wintypes.LPARAM)
    def candidate(hwnd, _):
        if not user.IsWindowVisible(hwnd):
            return True
        title = ctypes.create_unicode_buffer(1024)
        user.GetWindowTextW(hwnd,title,1024)
        if 'cyberpunk' not in title.value.lower():
            return True
        pid = wintypes.DWORD()
        user.GetWindowThreadProcessId(hwnd,ctypes.byref(pid))
        handle = kernel.OpenProcess(0x1000,False,pid.value)
        if handle:
            try:
                executable = ctypes.create_unicode_buffer(32768)
                length = wintypes.DWORD(len(executable))
                if kernel.QueryFullProcessImageNameW(handle,0,executable,ctypes.byref(length)) and Path(executable.value).name.lower() == 'cyberpunk2077.exe':
                    found.append(title.value)
            finally:
                kernel.CloseHandle(handle)
        return True
    callback = callback_type(candidate)
    user.EnumWindows(callback,0)
    if len(found) != 1:
        raise ScoutError(f'Expected one visible Cyberpunk2077.exe window, found {len(found)}')
    return found[0]


class CameraImages:
    def __init__(self, library):
        self.library = library

    def frame(self, state_reader, *, require_ready=True, cancelled=lambda:False, timeout=40):
        from PIL import Image
        from windows_capture import WindowsCapture
        title = game_window()
        baseline = state_reader()
        if baseline.get('overlay_open'):
            raise ScoutError('Close the CET overlay before taking an image')
        # Leave border control at the OS default, as world-location capture does.
        # Explicitly toggling it is unsupported on older Windows builds.
        capture = WindowsCapture(window_name=title,cursor_capture=False,draw_border=None)
        done = threading.Event()
        result, errors = [], []
        last_stamp = None
        start = time.monotonic()

        @capture.event
        def on_frame_arrived(frame, control):
            nonlocal last_stamp
            if done.is_set():
                return
            try:
                if cancelled():
                    raise ScoutError('Operation stopped')
                state = state_reader()
                if state.get('overlay_open'):
                    raise ScoutError('CET overlay opened during capture')
                if state['boot'] != baseline['boot']:
                    raise ScoutError('CET restarted during capture')
                stamp = getattr(frame,'timespan',None)
                if not isinstance(stamp,int) or (last_stamp is not None and stamp <= last_stamp):
                    return
                last_stamp = stamp
                if state.get('loading') or state.get('paused') or (require_ready and not state.get('ready')) or state.get('frame',0) <= baseline.get('frame',0):
                    return
                if state.get('camera') is None:
                    raise ScoutError('No active camera pose')
                image = Image.frombytes('RGB', (frame.width, frame.height),
                                        frame.frame_buffer.tobytes(), 'raw', 'BGRX')
                result.append((image, {'state':state,'presentation_timestamp':stamp,'wait_seconds':time.monotonic()-start}))
                done.set()
            except Exception as error:
                errors.append(error); done.set()

        @capture.event
        def on_closed():
            if not result:
                errors.append(ScoutError('Game window closed during capture'))
            done.set()

        control = capture.start_free_threaded()
        try:
            while not done.wait(0.05):
                if cancelled():
                    raise ScoutError('Operation stopped')
                if time.monotonic()-start >= timeout:
                    raise ScoutError('No fresh game frame within the image deadline')
                state_reader()  # Detect dead CET even if WGC supplies no frames.
                if control.is_finished():
                    break
        finally:
            done.set()
            if not control.is_finished():
                control.stop()
        if errors:
            raise ScoutError(str(errors[0]))
        if not result:
            raise ScoutError('Game capture returned no image')
        return result[0]

    @staticmethod
    def preview(image):
        image = image.copy()
        image.thumbnail((1280,720))
        buffer = BytesIO()
        image.save(buffer,'JPEG',quality=85)
        return buffer.getvalue()

    def save(self, image, evidence, name):
        rid = identifier('image')
        path = self.library.root/'images'/f'{rid}.png'
        path.parent.mkdir(exist_ok=True)
        image.save(path,'PNG')
        record = self.library.put('image',name, {'path':str(path.resolve()),'width':image.width,'height':image.height,**evidence},rid)
        from .core import atomic_json
        atomic_json(path.with_suffix('.json'),record)
        return record
