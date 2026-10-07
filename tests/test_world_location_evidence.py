from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from world_locations.capture_evidence import (
    assess_capture,
    capture_rows,
    hash_file,
    refresh_session_publication,
)
from world_locations.cli import CliError, command_export, command_retry, create_parser
from world_locations.database import connect, connect_readonly, requeue_places


class CaptureEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.path = self.root / "locations.sqlite3"
        self.connection = connect(self.path)
        self.addCleanup(self.connection.close)
        self.connection.execute(
            """INSERT INTO places(location_id,category,requested_x,requested_y,requested_z,
                   requested_yaw,forward_x,forward_y,forward_z,resource_path,
                   extraction_rule_version,placement_rule_version,queue_order,
                   queue_status,review_status,publishable,created_at,updated_at)
               VALUES('place_test','terminal',1,2,3,90,1,0,0,'test.ent',
                      '1','1',1,'captured','resolved',1,'now','now')"""
        )
        self.connection.commit()

    def add_capture(self, identifier="one", *, restored=True, valid=True):
        session, attempt = f"session_{identifier}", f"attempt_{identifier}"
        self.connection.execute(
            """INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,
                   runtime_path,started_at,status,restoration_verified)
               VALUES(?,'test','{}','runtime','now','completed',?)""",
            (session, int(restored)),
        )
        self.connection.execute(
            """INSERT INTO capture_attempts(attempt_id,session_id,location_id,command_id,
                   attempt_number,status) VALUES(?,?,'place_test',?,1,'captured')""",
            (attempt, session, f"command_{identifier}"),
        )
        png = self.root / f"{identifier}.png"
        thumbnail = self.root / f"{identifier}.webp"
        from PIL import Image

        color = (sum(map(ord, identifier)) % 256, 40, 50)
        Image.new("RGB", (16, 16), color).save(png)
        Image.new("RGB", (8, 8), color).save(thumbnail, lossless=True)
        validation = {
            "valid": True,
            "publication_ready": valid,
            "errors": [],
            "warnings": [],
        }
        sidecar = {
            "capture_id": identifier,
            "attempt_id": attempt,
            "session_id": session,
            "location_id": "place_test",
            "planned_pose": {"x": 1, "y": 2, "z": 3, "yaw": 90, "pitch": 0, "roll": 0},
            "anchor": {
                "category": "terminal",
                "direction": "outward",
                "resource": "test.ent",
            },
            "readiness": {"ui_suppressed": True, "weapon_suppressed": True},
            "actual_pose": {
                "x": 1.1,
                "y": 2.1,
                "z": 3.1,
                "yaw": 90,
                "pitch": 0,
                "roll": 0,
            },
            "actual_fov": 70,
            "effective_pose": {"x": 1, "y": 2, "z": 3.1},
            "capture_profile": {"time": "10:00"},
            "validation": validation,
            "files": {
                "png": str(png),
                "thumbnail": str(thumbnail),
                "png_sha256": hash_file(png),
                "thumbnail_sha256": hash_file(thumbnail),
            },
        }
        sidecar_path = self.root / f"{identifier}.json"
        sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
        self.connection.execute(
            """INSERT INTO captures(capture_id,attempt_id,location_id,png_path,sidecar_path,
                   thumbnail_path,width,height,image_sha256,metadata_sha256,thumbnail_sha256,
                   captured_at,validation_status,validation_json)
               VALUES(?,?,'place_test',?,?,?,16,16,?,?,?,?,?,?)""",
            (
                identifier,
                attempt,
                str(png),
                str(sidecar_path),
                str(thumbnail),
                hash_file(png),
                hash_file(sidecar_path),
                hash_file(thumbnail),
                identifier,
                "valid" if valid else "needs_ui_review",
                json.dumps(validation),
            ),
        )
        self.connection.commit()
        return capture_rows(self.connection, session)[0]

    def test_capture_specific_validation_and_session_restore_control_export(self):
        good = self.add_capture()
        self.assertTrue(assess_capture(good)["publishable"])
        bad = self.add_capture("two", restored=False, valid=False)
        bad["publishable"] = 1
        self.assertFalse(assess_capture(bad)["publishable"])
        blockers = assess_capture(bad)["blockers"]
        self.assertTrue(any("session" in value for value in blockers))
        self.assertTrue(any("validation" in value for value in blockers))

    def test_changed_pose_or_anchor_cannot_borrow_historical_capture(self):
        row = self.add_capture()
        for field, value in (
            ("requested_x", 11),
            ("requested_yaw", 0),
            ("resource_path", "other.ent"),
            ("category", "door"),
            ("source_sector", "other.streamingsector.json"),
            ("road_id", "other-road"),
        ):
            with self.subTest(field=field):
                changed = {**row, field: value}
                result = assess_capture(changed)
                self.assertFalse(result["current"])
                self.assertFalse(result["publishable"])
        self.assertTrue(assess_capture({**row, "requested_yaw": 450})["current"])

    def test_hash_identity_and_suppression_evidence_fail_closed(self):
        row = self.add_capture()
        self.assertFalse(assess_capture(row, verify_files=False)["publishable"])
        self.assertFalse(assess_capture({**row, "session_id": "other"})["publishable"])
        sidecar_path = Path(row["sidecar_path"])
        sidecar = json.loads(sidecar_path.read_text())
        sidecar["readiness"]["ui_suppressed"] = False
        sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
        row["metadata_sha256"] = hash_file(sidecar_path)
        self.assertTrue(
            any("ui suppressed" in value for value in assess_capture(row)["blockers"])
        )
        Path(row["png_path"]).write_bytes(b"tampered")
        self.assertTrue(assess_capture(row)["integrity_errors"])

    def test_session_publication_does_not_reenable_stale_or_disabled_places(self):
        self.add_capture()
        for updates in (
            "queue_status='pending'",
            "queue_status='disabled'",
            "queue_status='captured',requested_z=99",
        ):
            self.connection.execute(f"UPDATE places SET publishable=1,{updates}")
            self.connection.commit()
            self.assertEqual(
                refresh_session_publication(self.connection, "session_one"), 0
            )
            self.assertEqual(
                self.connection.execute("SELECT publishable FROM places").fetchone()[0],
                0,
            )

    def test_export_uses_evidence_instead_of_cached_place_flag_and_is_readonly(self):
        self.add_capture()
        self.connection.execute("UPDATE places SET publishable=0")
        self.connection.commit()
        before = list(self.connection.iterdump())
        paths = {
            "database": self.path,
            "root": self.root,
            "exports": self.root / "exports",
            "reports": self.root / "reports",
        }
        args = argparse.Namespace(name="checked", include_unpublishable=False)
        result = command_export(args, {}, paths)
        self.assertEqual(result["exported"], 1)
        exported = json.loads(Path(result["json"]).read_text())["places"][0]
        self.assertEqual(exported["publishable"], 1)
        self.assertTrue(exported["current_capture"])
        self.assertEqual(before, list(self.connection.iterdump()))
        self.assertFalse((self.root / "capture-config.json").exists())
        args.name = "../outside"
        with self.assertRaisesRegex(ValueError, "Report name"):
            command_export(args, {}, paths)

    def test_review_export_keeps_blockers_and_never_claims_unverified_capture_valid(
        self,
    ):
        self.add_capture(restored=False, valid=False)
        paths = {
            "database": self.path,
            "exports": self.root / "exports",
            "reports": self.root / "reports",
        }
        args = argparse.Namespace(name="review", include_unpublishable=True)
        result = command_export(args, {}, paths)
        exported = json.loads(Path(result["json"]).read_text())["places"][0]
        self.assertEqual(exported["publishable"], 0)
        self.assertTrue(exported["publication_blockers"])

    def test_export_keeps_each_capture_pose_and_filters_its_own_validation(self):
        self.add_capture()
        self.add_capture("two", restored=False, valid=False)
        self.connection.execute(
            "UPDATE places SET actual_x=999,actual_fov=100,publishable=1"
        )
        self.connection.commit()
        paths = {
            "database": self.path,
            "exports": self.root / "exports",
            "reports": self.root / "reports",
        }
        result = command_export(
            argparse.Namespace(name="poses", include_unpublishable=False), {}, paths
        )
        records = json.loads(Path(result["json"]).read_text())["places"]
        self.assertEqual([item["capture_id"] for item in records], ["one"])
        self.assertEqual(records[0]["actual_x"], 1.1)
        self.assertEqual(records[0]["actual_fov"], 70)
        self.assertEqual(records[0]["capture_profile"], {"time": "10:00"})

    def test_export_cannot_overwrite_capture_sidecar_in_custom_directory(self):
        row = self.add_capture()
        before = Path(row["sidecar_path"]).read_bytes()
        paths = {
            "database": self.path,
            "exports": self.root,
            "reports": self.root / "reports",
        }
        with self.assertRaisesRegex(ValueError, "overwrite capture evidence"):
            command_export(
                argparse.Namespace(name="one", include_unpublishable=False), {}, paths
            )
        self.assertEqual(Path(row["sidecar_path"]).read_bytes(), before)

    def test_retry_only_recaptures_explicit_ids_and_retains_history(self):
        self.add_capture()
        with self.assertRaisesRegex(ValueError, "explicit"):
            requeue_places(self.connection, recapture=True)
        with self.assertRaisesRegex(ValueError, "recapture"):
            requeue_places(self.connection, location_ids=["place_test"])
        self.assertEqual(
            requeue_places(
                self.connection, location_ids=["place_test"], recapture=True
            ),
            1,
        )
        self.assertEqual(len(capture_rows(self.connection)), 1)
        self.assertEqual(
            self.connection.execute(
                "SELECT queue_status,publishable FROM places"
            ).fetchone()[:],
            ("pending", 0),
        )

    def test_retry_rejects_active_unknown_disabled_or_interrupted_selections(self):
        self.add_capture()
        with self.assertRaisesRegex(ValueError, "Unknown"):
            requeue_places(self.connection, location_ids=["missing"])
        for status in ("disabled", "in_progress"):
            self.connection.execute("UPDATE places SET queue_status=?", (status,))
            self.connection.commit()
            self.assertEqual(
                requeue_places(self.connection, categories=["terminal"]), 0
            )
            with self.assertRaisesRegex(ValueError, "not eligible"):
                requeue_places(
                    self.connection, location_ids=["place_test"], recapture=True
                )
        self.connection.execute("UPDATE capture_sessions SET status='running'")
        self.connection.commit()
        with self.assertRaisesRegex(ValueError, "Stop the capture"):
            requeue_places(self.connection)

    def test_retry_can_find_real_reason_in_latest_legacy_attempt(self):
        self.add_capture()
        self.connection.execute(
            "UPDATE places SET queue_status='failed',failure_code='attempts_exhausted'"
        )
        self.connection.execute(
            "UPDATE capture_attempts SET error_code='blurred_frame'"
        )
        self.connection.commit()
        self.assertEqual(
            requeue_places(self.connection, failure_codes=["frame_timeout"]), 0
        )
        self.assertEqual(
            requeue_places(self.connection, failure_codes=["blurred_frame"]), 1
        )

    def test_readonly_connection_cannot_create_or_modify_database(self):
        with self.assertRaises(FileNotFoundError):
            connect_readonly(self.root / "missing.sqlite3")
        with self.assertRaises(CliError):
            command_retry(
                argparse.Namespace(), {}, {"database": self.root / "missing.sqlite3"}
            )
        self.assertFalse((self.root / "missing.sqlite3").exists())
        connection = connect_readonly(self.path)
        self.addCleanup(connection.close)
        import sqlite3

        with self.assertRaises(sqlite3.OperationalError):
            connection.execute("DELETE FROM places")

    def test_cli_requires_positive_capture_limit_and_supports_targeted_review(self):
        parser = create_parser()
        args = parser.parse_args(["review", "--limit", "0", "--category", "terminal"])
        self.assertEqual(args.limit, 0)
        self.assertEqual(args.category, ["terminal"])
        capture = parser.parse_args(
            ["capture", "--location-id", "place_test", "--limit", "2"]
        )
        self.assertEqual(capture.location_id, ["place_test"])
        with self.assertRaises(SystemExit):
            parser.parse_args(["capture", "--limit", "0"])
