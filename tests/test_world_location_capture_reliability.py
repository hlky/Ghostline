"""Capture failures must remain bounded, attributable, and safe to retry."""

from __future__ import annotations

import json
import copy
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

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from world_locations import capture
from world_locations.capture import (
    CaptureController,
    CaptureError,
    GameWindow,
    SessionProtocolError,
    validate_ready_event,
)
from world_locations.protocol import (
    ProtocolError,
    RuntimeProtocol,
    atomic_write_json,
    read_json,
)
from world_locations.database import transaction
from world_locations.extract import index_sectors
from world_locations.planning import plan_locations
from tests import test_world_location_capture as capture_fixtures


def ready_event(place, width=1920, height=1080):
    pose = {
        axis: place[f"requested_{axis}"]
        for axis in ("x", "y", "z", "yaw", "pitch", "roll")
    }
    return {
        "schema_version": 1,
        "session_id": "session-test",
        "command_id": "command-test",
        "event": "ready",
        "stage": "ready",
        "frame": 10,
        "actual_pose": pose,
        "effective_pose": dict(pose),
        "actual_fov": 80,
        "readiness": {
            **dict.fromkeys(
                (
                    "streaming_complete",
                    "player_attached",
                    "camera_attached",
                    "position_valid",
                    "position_stable",
                    "ground_probe",
                    "ui_suppressed",
                    "weapon_suppressed",
                ),
                True,
            ),
            "loading_screen": False,
            "menu_open": False,
            "paused": False,
            "presented_frame": 10,
            "display_width": width,
            "display_height": height,
        },
    }


PLACE = {f"requested_{axis}": 0.0 for axis in ("x", "y", "z", "yaw", "pitch", "roll")}


class ReadyEvidenceTests(unittest.TestCase):
    def test_ui_weapon_display_frame_and_numeric_pose_are_enforced(self):
        for change in (
            "ui",
            "weapon",
            "display",
            "frame",
            "nan",
            "distance",
            "redirected",
        ):
            event = ready_event(PLACE)
            if change == "ui":
                event["readiness"]["ui_suppressed"] = False
            elif change == "weapon":
                event["readiness"]["weapon_suppressed"] = False
            elif change == "display":
                event["readiness"]["display_width"] = 1280
            elif change == "frame":
                event["readiness"]["presented_frame"] = True
            elif change == "nan":
                event["actual_pose"]["x"] = float("nan")
            elif change == "distance":
                event["actual_pose"]["x"] = 5
            else:
                event["effective_pose"]["x"] = event["actual_pose"]["x"] = 5
            with self.subTest(change=change):
                report = validate_ready_event(event, PLACE, {})
                self.assertFalse(report["valid"], report)
                self.assertEqual(report["error_codes"], ["readiness_invalid"])

    def test_session_mismatch_and_malformed_schema_fail_as_protocol_errors(self):
        with tempfile.TemporaryDirectory() as folder:
            protocol = RuntimeProtocol(Path(folder))
            for kind in ("ready", "completed"):
                event = {**ready_event(PLACE), "event": kind, "session_id": "other"}
                atomic_write_json(protocol.event_paths[kind], event)
                method = (
                    protocol.wait_for_completion
                    if kind == "completed"
                    else protocol.wait_for_event
                )
                kwargs = {} if kind == "completed" else {"accepted_types": {"ready"}}
                with self.assertRaisesRegex(ProtocolError, "different session"):
                    method(
                        command_id="command-test",
                        session_id="session-test",
                        timeout_seconds=0.05,
                        **kwargs,
                    )
            event = {**ready_event(PLACE), "schema_version": "broken"}
            atomic_write_json(protocol.event_paths["ready"], event)
            with self.assertRaisesRegex(ProtocolError, "schema_version"):
                protocol.wait_for_event(
                    command_id="command-test",
                    session_id="session-test",
                    timeout_seconds=0.05,
                    accepted_types={"ready"},
                )
            protocol.acknowledge("command-test", False, session_id="session-test")
            self.assertEqual(read_json(protocol.ack_path)["session_id"], "session-test")

    def test_readiness_loss_after_ready_is_not_hidden_by_old_ready_file(self):
        with tempfile.TemporaryDirectory() as folder:
            protocol = RuntimeProtocol(Path(folder))
            event = ready_event(PLACE)
            atomic_write_json(protocol.cet_heartbeat_path, event)
            kwargs = dict(
                command_id="command-test",
                session_id="session-test",
                minimum_frame=10,
                maximum_age_seconds=5,
            )
            self.assertEqual(protocol.capture_evidence(**kwargs)["frame"], 10)
            atomic_write_json(
                protocol.event_paths["error"],
                {
                    **event,
                    "event": "error",
                    "error_code": "readiness_lost",
                    "error_detail": "overlay opened",
                },
            )
            with self.assertRaises(ProtocolError) as raised:
                protocol.capture_evidence(**kwargs)
            self.assertEqual(raised.exception.code, "readiness_lost")
            self.assertEqual(raised.exception.event["error_detail"], "overlay opened")

    def test_failed_restore_blocks_retry_even_when_completion_says_unsuccessful(self):
        controller = object.__new__(CaptureController)
        controller.capture_config = {}
        controller.runtime = mock.Mock()
        controller.runtime.wait_for_completion.return_value = {
            "success": False,
            "restoration_verified": False,
        }
        with self.assertRaisesRegex(SessionProtocolError, "did not verify restoration"):
            controller._require_completion(
                session_id="session-test",
                command_id="command-test",
                expected_success=False,
            )


class WindowCaptureTests(unittest.TestCase):
    def backend(self, timestamps):
        import numpy as np

        owner = self

        class Backend:
            def __init__(self, **kwargs):
                self.handlers = {}
                self.stopped = threading.Event()
                owner.instance = self

            def event(self, function):
                self.handlers[function.__name__] = function

            def stop(self):
                self.stopped.set()

            def is_finished(self):
                return self.stopped.is_set()

            def start_free_threaded(self):
                def emit():
                    for stamp in timestamps:
                        if self.stopped.wait(0.005):
                            return
                        pixels = np.zeros((8, 8, 4), dtype=np.uint8)
                        pixels[:, :, :3] = [20, 80, 200]
                        frame = types.SimpleNamespace(
                            width=8, height=8, timespan=stamp, frame_buffer=pixels
                        )
                        self.handlers["on_frame_arrived"](frame, self)

                self.worker = threading.Thread(target=emit)
                self.worker.start()
                return self

        return types.SimpleNamespace(WindowsCapture=Backend)

    def capture(self, timestamps, **kwargs):
        window = object.__new__(GameWindow)
        window.find = lambda: 42
        with mock.patch.dict(
            sys.modules, {"windows_capture": self.backend(timestamps)}
        ):
            try:
                return window.capture(
                    8, 8, visual_settle_seconds=0, visual_timeout_seconds=0.08, **kwargs
                )
            finally:
                self.instance.worker.join(1)

    def test_no_frames_and_repeated_old_frames_have_external_deadlines(self):
        for timestamps in ([], [100, 100, 100]):
            with self.subTest(timestamps=timestamps):
                started = time.monotonic()
                with self.assertRaises(CaptureError) as raised:
                    self.capture(timestamps)
                self.assertEqual(raised.exception.code, "frame_timeout")
                self.assertLess(time.monotonic() - started, 1)
                self.assertTrue(self.instance.stopped.is_set())

    def test_only_advancing_presentations_are_copied_and_guarded(self):
        check = mock.Mock()
        image = self.capture([100, 100, 101], readiness_check=check)
        self.assertEqual(image.getpixel((0, 0)), (200, 80, 20))
        self.assertEqual(image.info["capture_frame"]["frames_observed"], 2)
        self.assertEqual(image.info["capture_frame"]["captured_timespan"], 101)
        check.assert_called()
        with self.assertRaisesRegex(ProtocolError, "lost"):
            self.capture(
                [], readiness_check=mock.Mock(side_effect=ProtocolError("lost"))
            )
        self.assertTrue(self.instance.stopped.is_set())


class CapturePersistenceTests(unittest.TestCase):
    setUp = capture_fixtures.IndexAndPlanTests.setUp
    tearDown = capture_fixtures.IndexAndPlanTests.tearDown

    def controller(self):
        index_sectors(self.connection, self.source, self.config)
        plan_locations(self.connection, self.config)
        controller = object.__new__(CaptureController)
        controller.connection = self.connection
        controller.config = self.config
        controller.config_root = ROOT
        controller.capture_config = {
            "maximum_attempts": 1,
            "width": 64,
            "height": 36,
            "thumbnail_width": 16,
            "profile": {"fov": 80},
        }
        controller.captures_root = self.root / "captures"
        controller.game_profile = "test"
        with transaction(self.connection):
            self.connection.execute(
                "INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,runtime_path,started_at,status) VALUES('session-test','test','{}','test','2026-01-01','running')"
            )
        return controller

    def runtime(self, place):
        class Runtime:
            def heartbeat(self, _session):
                pass

            def send(self, command):
                self.command = command

            def event(self):
                return {
                    **ready_event(place, 64, 36),
                    "command_id": self.command["command_id"],
                }

            def wait_for_event(self, **kwargs):
                return {**self.event(), "event": next(iter(kwargs["accepted_types"]))}

            def capture_evidence(self, **kwargs):
                return self.event()

            def acknowledge(self, command_id, success, detail, **kwargs):
                self.success = success

            def wait_for_completion(self, **kwargs):
                return {"success": self.success, "restoration_verified": True}

        return Runtime()

    def test_rejected_blur_keeps_ready_pose_reason_and_image(self):
        from PIL import Image

        controller = self.controller()
        place = self.connection.execute(
            "SELECT * FROM places WHERE category='vending_machine'"
        ).fetchone()
        controller.runtime = self.runtime(place)
        controller.window = mock.Mock()
        controller.window.capture.return_value = Image.new("RGB", (64, 36), "white")
        self.assertFalse(controller._capture_place("session-test", place)[0])
        row = self.connection.execute("SELECT * FROM capture_attempts").fetchone()
        self.assertEqual(row["error_code"], "blurred_frame")
        self.assertEqual(
            json.loads(row["ready_event_json"])["readiness"]["presented_frame"], 10
        )
        self.assertEqual(json.loads(row["actual_pose_json"])["x"], place["requested_x"])
        detail = json.loads(row["error_detail"])
        self.assertEqual(detail["validation"]["sharpness_laplacian_variance"], 0)
        self.assertTrue(Path(detail["rejected_image"]["path"]).is_file())
        self.assertEqual(detail["rejected_image"]["kind"], "diagnostic_preview")
        self.assertEqual(
            detail["rejected_image"]["original_dimensions"], {"width": 64, "height": 36}
        )
        self.assertLessEqual(detail["rejected_image"]["dimensions"]["width"], 16)
        self.assertEqual(
            self.connection.execute("SELECT count(*) FROM captures").fetchone()[0], 0
        )

    def test_success_persists_perceptual_hash_and_repeated_other_location_is_rejected(
        self,
    ):
        from PIL import Image
        import numpy as np

        controller = self.controller()
        places = self.connection.execute(
            "SELECT * FROM places WHERE scope_status='in_scope' LIMIT 2"
        ).fetchall()
        pixels = np.random.default_rng(7).integers(0, 256, (36, 64, 3), dtype=np.uint8)
        controller.window = mock.Mock()
        controller.window.capture.return_value = Image.fromarray(pixels)
        controller.runtime = self.runtime(places[0])
        self.assertTrue(controller._capture_place("session-test", places[0])[0])
        row = self.connection.execute("SELECT * FROM captures").fetchone()
        self.assertTrue(row["perceptual_hash"].startswith("dhash64:"))
        self.assertEqual(
            json.loads(row["validation_json"])["perceptual_hash"],
            row["perceptual_hash"],
        )
        controller.runtime = self.runtime(places[1])
        self.assertFalse(controller._capture_place("session-test", places[1])[0])
        failed = self.connection.execute(
            "SELECT error_code,error_detail FROM capture_attempts WHERE status='failed'"
        ).fetchone()
        self.assertEqual(failed["error_code"], "duplicate_frame")
        self.assertEqual(
            json.loads(failed["error_detail"])["validation"]["duplicate_capture_ids"],
            [row["capture_id"]],
        )

    def test_heartbeat_covers_validation_save_completion_and_saves_capture_time_pose(
        self,
    ):
        from PIL import Image
        import numpy as np

        controller = self.controller()
        place = self.connection.execute(
            "SELECT * FROM places WHERE scope_status='in_scope' LIMIT 1"
        ).fetchone()
        runtime = self.runtime(place)
        controller.runtime = runtime
        tick = threading.Event()
        workers = set()

        def heartbeat(_session):
            if threading.current_thread().name == "world-capture-heartbeat":
                workers.add(threading.current_thread())
                tick.set()

        def wait_for_heartbeat():
            tick.clear()
            self.assertTrue(
                tick.wait(1.5), "heartbeat stopped during active capture work"
            )

        runtime.heartbeat = heartbeat

        def snapshot(**_kwargs):
            event = copy.deepcopy(runtime.event())
            event["actual_pose"]["x"] += 0.1
            event["readiness"]["presented_frame"] = 20
            event["frame"] = 20
            event["timestamp"] = "capture-time"
            event["actual_fov"] = 79
            event["runtime_location"] = {"named_area": "Capture time area"}
            return event

        runtime.capture_evidence = snapshot
        complete = runtime.wait_for_completion
        runtime.wait_for_completion = lambda **kwargs: (
            wait_for_heartbeat(),
            complete(**kwargs),
        )[1]
        controller.window = mock.Mock()
        pixels = np.random.default_rng(12).integers(0, 256, (36, 64, 3), dtype=np.uint8)
        controller.window.capture.return_value = Image.fromarray(pixels)
        validate = capture.validate_image
        save = controller._save_capture

        def slow_validate(*args, **kwargs):
            wait_for_heartbeat()
            return validate(*args, **kwargs)

        def slow_save(**kwargs):
            wait_for_heartbeat()
            return save(**kwargs)

        with (
            mock.patch.object(capture, "validate_image", side_effect=slow_validate),
            mock.patch.object(controller, "_save_capture", side_effect=slow_save),
        ):
            self.assertTrue(controller._capture_place("session-test", place)[0])
        self.assertTrue(workers)
        self.assertTrue(all(not worker.is_alive() for worker in workers))
        row = self.connection.execute("SELECT sidecar_path FROM captures").fetchone()
        sidecar = json.loads(Path(row["sidecar_path"]).read_text(encoding="utf-8"))
        self.assertAlmostEqual(sidecar["actual_pose"]["x"], place["requested_x"] + 0.1)
        self.assertEqual(sidecar["actual_fov"], 79)
        self.assertEqual(sidecar["runtime_location"]["named_area"], "Capture time area")
        self.assertEqual(sidecar["readiness"]["presented_frame"], 20)
        self.assertEqual(
            sidecar["validation"]["initial_ready_event"]["readiness"][
                "presented_frame"
            ],
            10,
        )
        actual = self.connection.execute(
            "SELECT actual_x FROM places WHERE location_id=?", (place["location_id"],)
        ).fetchone()[0]
        self.assertAlmostEqual(actual, place["requested_x"] + 0.1)

    def test_heartbeat_covers_rejected_preview_and_negative_completion(self):
        from PIL import Image

        controller = self.controller()
        place = self.connection.execute(
            "SELECT * FROM places WHERE scope_status='in_scope' LIMIT 1"
        ).fetchone()
        runtime = self.runtime(place)
        controller.runtime = runtime
        tick = threading.Event()
        runtime.heartbeat = lambda _session: tick.set()

        def wait_for_heartbeat():
            tick.clear()
            self.assertTrue(
                tick.wait(1.5), "heartbeat stopped before rejection completed"
            )

        complete = runtime.wait_for_completion
        runtime.wait_for_completion = lambda **kwargs: (
            wait_for_heartbeat(),
            complete(**kwargs),
        )[1]
        save = capture._atomic_save_image

        def slow_preview(*args, **kwargs):
            wait_for_heartbeat()
            return save(*args, **kwargs)

        controller.window = mock.Mock()
        controller.window.capture.return_value = Image.new("RGB", (64, 36), "white")
        with mock.patch.object(capture, "_atomic_save_image", side_effect=slow_preview):
            self.assertFalse(controller._capture_place("session-test", place)[0])
        self.assertIs(runtime.success, False)

    def test_run_filters_validate_before_runtime_and_keep_selected_queue_order(self):
        controller = self.controller()
        controller.runtime = mock.Mock(spec=RuntimeProtocol)
        with self.assertRaisesRegex(ValueError, "unknown capture locations"):
            controller.run(location_ids=["unknown"])
        controller.runtime.assert_runtime_alive.assert_not_called()
        rows = self.connection.execute(
            "SELECT * FROM places WHERE scope_status='in_scope' ORDER BY queue_order,location_id LIMIT 3"
        ).fetchall()
        selected = rows[0]
        controller.runtime.root = self.root / "runtime"
        controller._restore = mock.Mock(return_value=True)
        controller._capture_place = mock.Mock(return_value=(False, "fixture"))
        with mock.patch.object(capture, "refresh_session_publication") as refresh:
            result = controller.run(
                location_ids=[row["location_id"] for row in reversed(rows)],
                categories=[selected["category"]],
                limit=1,
            )
        self.assertEqual(result["selected"], 1)
        self.assertEqual(
            controller._capture_place.call_args.args[1]["location_id"],
            selected["location_id"],
        )
        refresh.assert_called_once()


class CetRuntimeTests(unittest.TestCase):
    @unittest.skipUnless(
        shutil.which("lua"), "Lua is required for isolated CET state-machine checks"
    )
    def test_ui_gate_draw_recheck_and_failed_restore_ack(self):
        script = r"""
local callbacks = {}
registerForEvent = function(name, fn) callbacks[name] = fn end
registerHotkey = function(...) end
dofile(arg[1])
local function up(fn, name, replacement)
    for i=1,100 do
        local key, value = debug.getupvalue(fn, i)
        if not key then break end
        if key == name then
            if replacement ~= nil then debug.setupvalue(fn, i, replacement) end
            return value
        end
    end
    error('missing upvalue '..name)
end
local update, draw = callbacks.onUpdate, callbacks.onDraw
up(update, 'config', {expected_width=1920,expected_height=1080,runtime_directory='test'})
local state = up(update, 'state')
state.command = {session_id='s', command_id='c',pose={},effective_pose={}}
local build = up(update,'buildReadiness')
local player = {IsAttached=function() return true end,GetFPPCameraComponent=function() return {GetFOV=function() return 80 end} end}
Game = {GetPlayer=function() return player end,GetSystemRequestsHandler=function() return {IsPreGame=function() return false end} end}
up(build,'getActualPose',function() return {x=0,y=0,z=0,yaw=0} end)
up(build,'positionIsValid',function() return true,0,0 end)
up(build,'playerPositionIsStable',function() return true,0,10,1 end)
up(build,'runtimeLocation',function() return {} end)
up(build,'groundProbe',function() return true,nil,'Static' end)
up(build,'streamingIsComplete',function() return true,'ground' end)
up(build,'getMenuOpen',function() return false end)
up(build,'getPaused',function() return false end)
up(build,'uiIsSuppressed',function() return false,1920,1080,true end)
local _, ready = build(0.01)
assert(ready == false,'UI-visible state must never arm')
up(build,'uiIsSuppressed',function() return true,1920,1080,true end)
_, ready = build(0.01)
assert(ready == true)
state.stage='armed'; state.readyEvidence={evidence={},actual={}}
up(draw,'buildReadiness',function() return {},false,{} end)
draw()
assert(state.stage=='waiting','draw must recheck readiness')
local ack = up(update,'pollAck')
local restore = up(ack,'restoreCaptureMode')
for _, name in ipairs({'restoreEffects','restoreWeapon','restoreControllers','setPhoneMessageNotificationsHidden','restorePrevention'}) do
    up(restore,name,function() return true end)
end
up(restore,'restoreSettings',function() return false end)
up(restore,'log',function(...) end)
state.active=true;state.snapshot={}
local restored = restore('test failure')
assert(restored==false and state.snapshot~=nil,'failed restore must retain snapshot')
up(restore,'restoreSettings',function() return true end)
restored = restore('test recovery')
assert(restored==true and state.snapshot==nil)
state.command={session_id='s',command_id='c'};state.stage='ready';state.active=true
up(ack,'readJson',function() return {schema_version=1,session_id='other',command_id='c',success=false} end)
ack(); assert(state.stage=='ready','foreign ack must be ignored')
up(ack,'readJson',function() return {schema_version=1,session_id='s',command_id='c',success=false} end)
up(ack,'restoreCaptureMode',function() return false,{settings=false} end)
local completed
up(ack,'writeEvent',function(kind,event) completed=event end)
ack()
assert(completed.restoration_verified==false and completed.restoration.settings==false)
assert(state.stage=='idle' and state.command==nil)
local heartbeat = up(update,'controllerHeartbeatIsAlive')
state.captureSessionId='s';state.lastControllerHeartbeatUnix=nil
up(heartbeat,'readJson',function() return {schema_version=1,session_id='s',unix_seconds=os.time()} end)
assert(heartbeat()==true,'idle capture mode must retain its session heartbeat')
local watchdogRestores=0
up(update,'controllerHeartbeatIsAlive',function() return false end)
up(update,'restoreCaptureMode',function() watchdogRestores=watchdogRestores+1;state.active=false;state.snapshot=nil;return true end)
state.heartbeatElapsed=0
update(0.01)
assert(watchdogRestores==1,'heartbeat loss between destinations must restore capture mode')
state.snapshot={}
update(0.01)
assert(watchdogRestores==2,'heartbeat loss must retry pending restoration snapshots')
print('CET state machine checks passed')
"""
        result = subprocess.run(
            [
                shutil.which("lua"),
                "-",
                str(ROOT / "tools/world_location_capture_cet/init.lua"),
            ],
            input=script,
            text=True,
            capture_output=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
