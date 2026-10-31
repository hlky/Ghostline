"""Camera surveys preserve source evidence and wait through transient loading."""
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from world_locations.capture import validate_ready_event
from world_locations.config import load_config
from world_locations.database import connect
from world_locations.survey import expanded_views, prepare_survey, recovery_candidates
from world_locations.visual_readiness import FrameReadiness


class SurveyTests(unittest.TestCase):
    def place(self, category="road", role="along", status="pending"):
        with tempfile.TemporaryDirectory() as folder:
            db = connect(Path(folder) / "seed.sqlite3")
            db.execute("""INSERT INTO places(location_id,category,direction,requested_x,requested_y,requested_z,
                requested_yaw,requested_pitch,forward_x,forward_y,forward_z,extraction_rule_version,
                placement_rule_version,queue_order,created_at,updated_at,queue_status,provenance_json)
                VALUES('p',?,?,10,20,5,30,0,-0.5,0.866,0,'e','p',0,'old','old',?,'{}')""", (category,role,status))
            db.commit()
            row = dict(db.execute("SELECT * FROM places").fetchone())
            db.close()
            return row

    def test_context_sweep_preserves_center_identity_and_creates_independent_angles(self):
        row = self.place(status="captured")
        views = expanded_views(row)
        self.assertEqual(views[0]["location_id"], "p")
        self.assertEqual(views[0]["queue_status"], "pending")
        self.assertEqual([r["requested_yaw"] for r in views], [30,345,75])
        self.assertEqual(len({r["location_id"] for r in views}), 3)
        self.assertTrue(all(r["requested_x"] == 10 and r["requested_z"] == 5 for r in views))
        self.assertEqual(len(expanded_views(self.place("fast_travel", "terminal"))), 1)

    def test_parking_is_raised_and_pitched_at_four_bearings(self):
        views = expanded_views(self.place("parking_space", "parking_context"))
        self.assertEqual([r["requested_yaw"] for r in views], [30,120,210,300])
        self.assertTrue(all(r["requested_pitch"] == -20 and r["requested_z"] == 7 for r in views))
        self.assertTrue(all(r["forward_z"] < 0 for r in views))
        self.assertNotIn("p", {r["location_id"] for r in views})

    def test_snapshot_keeps_historical_capture_and_source_database_unchanged(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "source.sqlite3"
            db = connect(source)
            row = self.place(status="failed")
            columns = list(row)
            db.execute(f"INSERT INTO places({','.join(columns)}) VALUES({','.join('?' for _ in columns)})", list(row.values()))
            db.execute("INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,runtime_path,started_at,status) VALUES('s','p','{}','runtime','old','completed')")
            db.execute("INSERT INTO capture_attempts(attempt_id,session_id,location_id,command_id,attempt_number,status) VALUES('a','s','p','c',1,'captured')")
            db.execute("""INSERT INTO captures(capture_id,attempt_id,location_id,png_path,sidecar_path,thumbnail_path,
                width,height,image_sha256,metadata_sha256,captured_at,validation_status,validation_json)
                VALUES('image','a','p','original.png','original.json','thumb.webp',1920,1080,'hash','meta','old','valid','{}')""")
            db.commit(); db.close()
            result = prepare_survey(Path(folder) / "survey.sqlite3", [source])
            self.assertEqual(result["preserved_captures"], 1)
            copied = sqlite3.connect(Path(folder) / "survey.sqlite3")
            self.assertEqual(copied.execute("SELECT png_path FROM captures").fetchone()[0], "original.png")
            self.assertEqual(copied.execute("SELECT count(*) FROM places WHERE queue_status='pending'").fetchone()[0], 3)
            copied.close()
            check = sqlite3.connect(source)
            self.assertEqual(check.execute("SELECT queue_status FROM places").fetchone()[0], "failed")
            self.assertEqual(check.execute("SELECT count(*) FROM captures").fetchone()[0], 1)
            check.close()

    def test_camera_readback_rejects_fabricated_or_incorrect_pitch(self):
        from tests.test_world_location_capture_reliability import ready_event
        # Use a known valid protocol fixture, then require the camera contract.
        row = self.place()
        event = ready_event(row)
        config = load_config()["capture"]
        config.update(survey_runtime_required=True, angle_tolerance_degrees=2)
        actual = event["actual_pose"]
        actual.update(camera_verified=True, pitch=0, roll=0)
        actual["camera_pose"] = {k:actual[k] for k in ("x","y","z","yaw","pitch","roll")}
        self.assertTrue(validate_ready_event(event,row,config)["valid"])
        actual["pitch"] = -20
        self.assertFalse(validate_ready_event(event,row,config)["valid"])
        actual["pitch"]=0; actual["camera_verified"]=False
        self.assertFalse(validate_ready_event(event,row,config)["valid"])

    def test_snapshot_merges_sources_with_colliding_local_primary_keys(self):
        with tempfile.TemporaryDirectory() as folder:
            sources = []
            for number in range(2):
                source = Path(folder) / f"source-{number}.sqlite3"
                db = connect(source)
                row = self.place(status="captured")
                row["location_id"] = f"source-{number}"
                db.execute(f"INSERT INTO places({','.join(row)}) VALUES({','.join('?' for _ in row)})", list(row.values()))
                db.commit()
                db.close()
                sources.append(source)
            result = prepare_survey(Path(folder) / "survey.sqlite3", sources)
            self.assertEqual(result["pending_by_category"], {"road": 6})

    def test_recovery_candidates_cannot_cross_scope_boundary(self):
        row = self.place()
        row["requested_yaw"] = 0
        config = {"scope_rules": [{"id":"test", "type":"exclude_negative_half_plane",
            "boundary_origin":{"x":10,"y":0}, "boundary_tangent":{"x":0,"y":1},
            "in_scope_reference":{"x":20,"y":0}}]}
        candidates = recovery_candidates(row, config)
        self.assertEqual([p["x"] for p in candidates], [11.5,12])

    def test_loading_templates_are_labelled_and_scene_changes_reset_settling(self):
        image = np.repeat(np.arange(64,dtype=np.uint8)[None,:,None]*4,36,axis=0)
        image = np.repeat(image,3,axis=2)
        checker = FrameReadiness()
        self.assertEqual(checker.observe(image,loading_confirmed=True)[1], "engine_loading")
        self.assertEqual(checker.observe(image)[1], "known_loading_screen")
        blank = np.zeros_like(image)
        checker.observe(blank,loading_confirmed=True)
        self.assertEqual(len(checker.templates), 1, "blank loading fades must not poison dark-room detection")
        other = 255-image
        self.assertEqual(checker.observe(other)[1], "first_frame")
        self.assertTrue(checker.observe(other)[0])
        self.assertEqual(checker.observe(np.full_like(other,127))[1], "scene_changing")

    def test_transient_loading_waits_for_a_new_frame_without_failing_capture(self):
        from tests.test_world_location_capture_reliability import WindowCaptureTests
        from world_locations.capture import GameWindow
        from world_locations.protocol import ReadinessPending
        fixture = WindowCaptureTests()
        window = object.__new__(GameWindow)
        window.find = lambda: 42
        window.scene_stability_threshold = 0.04
        started = time.monotonic()
        def readiness():
            if time.monotonic()-started < 0.06:
                raise ReadinessPending("loading", event={"loading_sources":["test_loader"]})
        with mock.patch.dict(sys.modules, {"windows_capture":fixture.backend(range(100))}):
            try:
                image = window.capture(8,8,visual_settle_seconds=0.01,visual_timeout_seconds=0.3,readiness_check=readiness)
                self.assertGreaterEqual(image.info["capture_frame"]["visual_wait_seconds"], 0.06)
            finally:
                fixture.instance.worker.join(1)

    @unittest.skipUnless(shutil.which("lua"), "Lua is required")
    def test_camera_loading_and_obstruction_runtime(self):
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run([shutil.which("lua"),str(root/'tests/world_location_survey_harness.lua'),str(root/'tools/world_location_capture_cet/survey_runtime.lua')],capture_output=True,text=True,timeout=10)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)


if __name__ == "__main__":
    unittest.main()
