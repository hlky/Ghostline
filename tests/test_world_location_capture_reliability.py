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
    exclusive_controller,
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
                    "freefly_active",
                    "ui_suppressed",
                    "weapon_suppressed",
                    "player_protected",
                    "combat_clear",
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


class ControllerLockTests(unittest.TestCase):
    def test_collision_is_rejected_and_exception_releases_lock(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "controller.lock"
            with self.assertRaisesRegex(RuntimeError, "fixture abort"):
                with exclusive_controller(path):
                    with self.assertRaisesRegex(ProtocolError, "another capture controller"):
                        with exclusive_controller(path):
                            self.fail("second controller acquired an owned lock")
                    raise RuntimeError("fixture abort")
            with exclusive_controller(path):
                self.assertTrue(path.exists())


class ReadyEvidenceTests(unittest.TestCase):
    def test_airborne_pose_requires_flight_and_preserves_requested_height(self):
        airborne = {**PLACE, "requested_z": 100.0}
        event = ready_event(airborne)
        self.assertNotIn("ground_probe", event["readiness"])
        self.assertTrue(validate_ready_event(event, airborne, {})["valid"])
        event["readiness"]["freefly_active"] = False
        self.assertFalse(validate_ready_event(event, airborne, {})["valid"])
        event["readiness"]["freefly_active"] = True
        event["effective_pose"]["z"] = event["actual_pose"]["z"] = 0.0
        self.assertFalse(validate_ready_event(event, airborne, {})["valid"])

    def test_ui_weapon_display_frame_and_numeric_pose_are_enforced(self):
        for change in (
            "ui",
            "weapon",
            "display",
            "frame",
            "nan",
            "distance",
            "redirected",
            "player_protected",
            "combat_clear",
        ):
            event = ready_event(PLACE)
            if change in ("player_protected", "combat_clear"):
                event["readiness"][change] = False
            elif change == "ui":
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

    def test_setup_failure_restores_and_stops_before_retry_or_queue_exhaustion(self):
        controller = self.controller()
        place = self.connection.execute("SELECT * FROM places LIMIT 1").fetchone()
        controller.runtime = self.runtime(place)
        controller.capture_config["maximum_attempts"] = 3
        controller.runtime.wait_for_event = mock.Mock(
            side_effect=ProtocolError("protection failed", code="capture_mode_failed")
        )
        with self.assertRaisesRegex(SessionProtocolError, "runtime is unhealthy"):
            controller._capture_place("session-test", place)
        self.assertFalse(controller.runtime.success)
        self.assertEqual(controller.runtime.wait_for_event.call_count, 1)
        status = self.connection.execute(
            "SELECT queue_status FROM places WHERE location_id=?", (place["location_id"],)
        ).fetchone()[0]
        self.assertEqual(status, "in_progress")

    def test_busy_or_old_runtime_cannot_clear_protocol_or_recover_queue(self):
        controller = self.controller()
        controller.runtime = mock.Mock(spec=RuntimeProtocol)
        controller.runtime.root = self.root / "runtime"
        controller.runtime.assert_runtime_alive.return_value = {
            "stage": "idle", "capture_mode_active": False,
        }
        with mock.patch.object(capture, "recover_interrupted_queue") as recover:
            with self.assertRaisesRegex(ProtocolError, "current protection runtime"):
                controller.run(limit=1)
        controller.runtime.prepare.assert_not_called()
        recover.assert_not_called()

    def test_consecutive_location_failures_continue_through_remaining_queue(self):
        controller = self.controller()
        row = dict(self.connection.execute("SELECT * FROM places LIMIT 1").fetchone())
        row.pop("place_pk")
        for index in range(6):
            row["location_id"] = f"extra-fixture-{index}"
            with transaction(self.connection):
                self.connection.execute(
                    f"INSERT INTO places({','.join(row)}) VALUES({','.join('?' for _ in row)})",
                    list(row.values()),
                )
        controller.runtime = mock.Mock(spec=RuntimeProtocol)
        controller.runtime.root = self.root / "runtime"
        controller.runtime.assert_runtime_alive.return_value = {
            "stage": "idle", "capture_mode_active": False,
            "restoration_verified": True, "protection_contract_version": 1, "freefly_active": True,
        }
        controller._capture_place = mock.Mock(return_value=(False, "fixture"))
        controller._restore = mock.Mock(return_value=True)
        with mock.patch.object(capture, "refresh_session_publication"):
            result = controller.run()
        self.assertGreater(result["selected"], 5)
        self.assertEqual(controller._capture_place.call_count, result["selected"])
        self.assertEqual(result["failed"], result["selected"])
        self.assertTrue(result["restoration_verified"])
        controller._restore.assert_called_once()

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
        controller.runtime.assert_runtime_alive.return_value = {
            "stage": "idle", "capture_mode_active": False,
            "restoration_verified": True, "protection_contract_version": 1, "freefly_active": True,
        }
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
-- Accepted effect requests may become observable on a later update.
local enter=up(up(update,'beginCaptureWhenGameplayIsReady'),'enterCaptureMode')
local applyEffects=up(enter,'applyCaptureEffects')
up(update,'config').restrictions={'GameplayRestriction.NoCombat'}
TweakDB={GetRecord=function() return {} end}
TweakDBID={new=function(value) return value end}
Vector4={new=function(...) return {...} end}
player.GetEntityID=function() return {hash='player'} end
player.GetRecordID=function() return 'Player.Record' end
local appliedCount=0
local effectPresent=false
local effectSystem={
 HasStatusEffect=function() return effectPresent end,
 ApplyStatusEffect=function(_,id,effect,record,instigator,count,direction,savable)
  assert(effect=='GameplayRestriction.NoCombat','invulnerability must use GodMode only')
  assert(count==1 and record=='Player.Record' and instigator.hash=='player' and savable==false)
  appliedCount=appliedCount+1;return true
 end,
}
Game.GetStatusEffectSystem=function() return effectSystem end
local effects,effectError=applyEffects(player)
assert(effects and not effectError and appliedCount==1,'accepted effect must wait for readiness')
state.snapshot={effects=effects}
local effectsReady=up(up(build,'uiIsSuppressed'),'effectsAreApplied')
assert(not effectsReady(player),'unobserved effects must block readiness')
effectPresent=true;assert(effectsReady(player))
local cleanupEffects=up(up(up(update,'pollAck'),'restoreCaptureMode'),'restoreEffects')
local removalRequests=0
effectSystem.RemoveStatusEffect=function(_,id,effect,count)
 assert(count==1);removalRequests=removalRequests+1;return true
end
assert(not cleanupEffects(player),'cleanup must await native effect disappearance')
effectPresent=false
assert(cleanupEffects(player) and removalRequests==1,'absent owned effects need no repeated removal')

effectPresent=false
effectSystem.ApplyStatusEffect=function() error('native application failure') end
local _,nativeError=applyEffects(player)
assert(nativeError:find('native application failure'),'retain native error diagnostics')
state.snapshot=nil
up(build,'getActualPose',function() return {x=0,y=0,z=0,yaw=0} end)
up(build,'positionIsValid',function() return true,0,0 end)
up(build,'playerPositionIsStable',function() return true,0,10,1 end)
up(build,'runtimeLocation',function() return {} end)
up(build,'getMenuOpen',function() return false end)
up(build,'getPaused',function() return false end)
-- Popup lifecycle flags do not prove pixels are visible.
local realUi=up(build,'uiIsSuppressed')
up(realUi,'settingsAreSuppressed',function() return true end)
up(realUi,'effectsAreApplied',function() return true end)
up(realUi,'hideCurrentWeapon',function() return true end)
GetDisplayResolution=function() return 1920,1080 end
local popupVisible=false
state.popupControllers={test={GetRootWidget=function() return {IsVisible=function() return popupVisible end} end}}
state.phonePresentationActive=true;state.notificationSuppressionActive=true
assert(realUi(player),'hidden popup must not reject a clean frame because of lifecycle state')
popupVisible=true;assert(realUi(player),'visible empty controller container is diagnostic, not proof of phone pixels')
state.popupControllers={};state.phonePresentationActive=false
local phoneMute=up(up(up(update,'pollAck'),'restoreCaptureMode'),'setPhoneMessageNotificationsHidden')
local contactsActive=false
Game.GetAllBlackboardDefs=function() return {UI_ComDevice={ContactsActive='contacts'}} end
Game.GetBlackboardSystem=function() return {Get=function() return {
 GetBool=function() return contactsActive end,
 SetBool=function(_,key,value) contactsActive=value end,
} end} end
state.snapshot={}
assert(phoneMute(true) and contactsActive==false,'suppression must not open contacts')
assert(phoneMute(false) and contactsActive==false)
state.snapshot=nil
-- Flight can hold a pose without any collision/floor probe. It owns its
-- protections; capture must never toggle or remove them.
local flight={runtimeData={active=true,inGame=true,inMenu=false}}
GetMod=function(name) assert(name=='freefly');return flight end
gameGodModeType={Invulnerable='invulnerable'}
local invisible,combat,invulnerable=true,false,true
player.IsInvisible=function() return invisible end
player.IsInCombat=function() return combat end
Game.GetGodModeSystem=function() return {HasGodMode=function() return invulnerable end} end
local maintain=up(build,'maintainProtection')
assert(maintain(player))
flight.runtimeData.active=false
local protected,reason,fatal=maintain(player)
assert(not protected and fatal and reason:find('Activate FreeFly'))
flight.runtimeData.active=true
invisible=false;assert(not maintain(player));invisible=true
invulnerable=false;assert(not maintain(player));invulnerable=true
assert(maintain(player))
local combatClear=up(build,'combatIsClear')
local preventionEnabled,heat=false,0
state.snapshot={prevention={system={
 IsSystemEnabled=function() return preventionEnabled end,
 GetHeatStageAsInt=function() return heat end,
}}}
assert(combatClear(player))
combat=true;assert(not combatClear(player));combat=false
heat=1;assert(not combatClear(player));heat=0
state.snapshot=nil
up(build,'maintainProtection',function() return true end)
up(build,'combatIsClear',function() return true end)
local begin=up(update,'beginCaptureWhenGameplayIsReady')
up(begin,'enterCaptureMode',function() return true end)
up(begin,'effectsAreApplied',function() return true end)
local teleports=0
up(begin,'teleport',function() teleports=teleports+1;return true end)
state.stage='preflight'
up(begin,'maintainProtection',function() return false,'waiting',false end)
begin();assert(teleports==0 and state.stage=='preflight','must wait for protection before teleport')
up(begin,'maintainProtection',function() return true end)
begin();assert(teleports==1 and state.stage=='waiting')
up(build,'uiIsSuppressed',function() return false,1920,1080,true end)
local _, ready = build(0.01)
assert(ready == false,'UI-visible state must never arm')
up(build,'uiIsSuppressed',function() return true,1920,1080,true end)
_, ready = build(0.01)
assert(ready == true)
up(build,'combatIsClear',function() return false end)
_,ready=build(0.01);assert(not ready,'combat must block readiness')
up(build,'combatIsClear',function() return true end)
up(build,'maintainProtection',function() return false end)
_,ready=build(0.01);assert(not ready,'missing protection must block readiness')
up(build,'maintainProtection',function() return true end)
state.stage='armed'; state.readyEvidence={evidence={},actual={}}
up(draw,'buildReadiness',function() return {},false,{} end)
draw()
assert(state.stage=='waiting','draw must recheck readiness')
local ack = up(update,'pollAck')
local restore = up(ack,'restoreCaptureMode')
for _, name in ipairs({'restoreEffects','restoreWeapon','restoreControllers','setPhoneMessageNotificationsHidden','restorePrevention'}) do
    up(restore,name,function() return true end)
end
-- Return to the original point before releasing protection or restoring UI.
local returnPosition={x=100,y=200,z=30}
local currentPosition={x=0,y=0,z=0}
player.GetWorldPosition=function() return currentPosition end
local returnTeleports=0
Game.GetTeleportationFacility=function() return {Teleport=function(_,entity,position,rotation)
 returnTeleports=returnTeleports+1
end} end
state.active=true;state.snapshot={returnPosition=returnPosition,returnRotation={}}
local returned=restore('return test')
assert(not returned and returnTeleports==1)
assert(state.lastRestoration.return_position==false)
currentPosition=returnPosition
returned=restore('return settled')
assert(returned)
up(restore,'restoreSettings',function() return false end)
up(restore,'log',function(...) end)
state.active=true;state.snapshot={}
local restored = restore('test failure')
assert(restored==false and state.snapshot~=nil,'failed restore must retain snapshot')
up(restore,'restoreSettings',function() return true end)
restored = restore('test recovery')
assert(restored==true and state.snapshot==nil)
up(restore,'restoreControllers',function() return false end)
state.active=true;state.snapshot={}
local released,cosmetic=restore('stale popup')
assert(released and cosmetic.controllers==false and state.snapshot==nil,'cosmetic cleanup must not block release')
assert(#state.cleanupWarnings==1)
up(restore,'restoreControllers',function() return true end)

state.command={session_id='s',command_id='c'};state.stage='ready';state.active=false
up(ack,'readJson',function() return {schema_version=1,session_id='other',command_id='c',success=false} end)
ack(); assert(state.stage=='ready','foreign ack must be ignored')
up(ack,'readJson',function() return {schema_version=1,session_id='s',command_id='c',success=false} end)
up(ack,'restoreCaptureMode',function() return false,{settings=false} end)
local completed
up(ack,'writeEvent',function(kind,event) completed=event end)
ack()
assert(completed==nil and state.stage=='ready','pending cleanup must not emit a premature negative completion')
up(ack,'restoreCaptureMode',function() return true,{settings=true,effects=true} end)
ack()
assert(completed.restoration_verified==true and completed.restoration.effects==true)
assert(state.stage=='idle' and state.command==nil)
local heartbeat = up(update,'controllerHeartbeatIsAlive')
state.active=true;state.captureSessionId='s';state.lastControllerHeartbeatUnix=nil
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
-- Final explicit restoration follows the same asynchronous barrier.
up(update,'controllerHeartbeatIsAlive',function() return true end)
up(update,'pollAck',function() end)
up(update,'pollCommand',function() end)
local cleanupComplete=false
up(update,'restoreCaptureMode',function() return cleanupComplete,{return_position=cleanupComplete,effects=cleanupComplete} end)
local restoreEvent=nil
up(update,'writeEvent',function(kind,event) restoreEvent={kind=kind,event=event} end)
state.stage='restoring';state.command={kind='restore',session_id='s',command_id='r'}
state.active=false;state.snapshot=nil;state.heartbeatElapsed=0
update(0.01)
assert(restoreEvent==nil and state.stage=='restoring','final restore must await cleanup')
cleanupComplete=true
update(0.01)
assert(restoreEvent.kind=='restored' and restoreEvent.event.restoration_verified and state.stage=='idle')
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
