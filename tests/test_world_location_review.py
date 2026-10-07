from __future__ import annotations

import json
import os
from pathlib import Path
import re
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from world_locations.capture_evidence import hash_file
from world_locations.database import connect, connect_readonly
from world_locations.review import build_review


class WorldLocationReviewTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.database = self.root / "capture's database.sqlite3"
        self.connection = connect(self.database)
        self.addCleanup(self.connection.close)
        self.output = self.root / "review" / "index.html"
        self.connection.execute(
            """INSERT INTO capture_sessions(session_id,game_profile,capture_profile_json,
                   runtime_path,started_at,status,restoration_verified)
               VALUES('session','test','{}','runtime','2026-09-05','completed',1)"""
        )
        self.connection.commit()

    def place(
        self,
        identifier="place_one",
        *,
        status="captured",
        category="terminal",
        area="Kabuki",
        review="resolved",
    ):
        self.connection.execute(
            """INSERT INTO places(location_id,category,requested_x,requested_y,requested_z,
                   requested_yaw,forward_x,forward_y,forward_z,resource_path,named_area,
                   extraction_rule_version,placement_rule_version,queue_order,
                   queue_status,review_status,created_at,updated_at)
               VALUES(?,?,1,2,3,90,1,0,0,'test.ent',?,'1','1',1,?,?,
                      '2026-09-01','2026-09-01')""",
            (identifier, category, area, status, review),
        )
        self.connection.commit()
        return identifier

    def capture(
        self,
        location="place_one",
        *,
        identifier="capture_one",
        at="2026-09-05T10:00:00Z",
        validation=None,
    ):
        from PIL import Image

        self.connection.execute(
            """INSERT INTO capture_attempts(attempt_id,session_id,location_id,command_id,
                   attempt_number,status,captured_at,finished_at)
               VALUES(?,'session',?,?,1,'captured',?,?)""",
            (identifier, location, identifier, at, at),
        )
        png = self.root / (identifier + " # image.png")
        thumbnail = self.root / (identifier + ".webp")
        # Distinct recaptures require distinct hashes under the real schema.
        shade = sum(identifier.encode()) % 255
        Image.new("RGB", (16, 9), (shade, 40, 50)).save(png)
        Image.new("RGB", (8, 5), (shade, 40, 50)).save(thumbnail, lossless=True)
        validation = (
            validation
            if validation is not None
            else {
                "valid": True,
                "publication_ready": True,
                "warnings": [],
                "errors": [],
                "sharpness_laplacian_variance": 50,
                "luminance_mean": 30,
                "black_fraction": 0.01,
            }
        )
        place = self.connection.execute(
            "SELECT * FROM places WHERE location_id=?", (location,)
        ).fetchone()
        sidecar = {
            "capture_id": identifier,
            "attempt_id": identifier,
            "session_id": "session",
            "location_id": location,
            "planned_pose": {
                axis: place[f"requested_{axis}"]
                for axis in ("x", "y", "z", "yaw", "pitch", "roll")
            },
            "anchor": {
                "category": place["category"],
                "direction": "outward",
                "resource": "test.ent",
                "source_sector": None,
                "road_id": None,
            },
            "readiness": {"ui_suppressed": True, "weapon_suppressed": True},
            "validation": validation,
            "files": {
                "png": str(png),
                "thumbnail": str(thumbnail),
                "png_sha256": hash_file(png),
                "thumbnail_sha256": hash_file(thumbnail),
            },
        }
        sidecar_path = self.root / (identifier + ".json")
        sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
        self.connection.execute(
            """INSERT INTO captures(capture_id,attempt_id,location_id,png_path,sidecar_path,
                   thumbnail_path,width,height,image_sha256,metadata_sha256,thumbnail_sha256,
                   captured_at,validation_status,validation_json)
               VALUES(?,?,?,?,?,?,16,9,?,?,?,?,'valid',?)""",
            (
                identifier,
                identifier,
                location,
                str(png),
                str(sidecar_path),
                str(thumbnail),
                hash_file(png),
                hash_file(sidecar_path),
                hash_file(thumbnail),
                at,
                json.dumps(validation),
            ),
        )
        self.connection.commit()
        return {"png": png, "sidecar": sidecar_path, "thumbnail": thumbnail}

    def failure(
        self,
        location,
        *,
        identifier="failure",
        at="2026-09-05T11:00:00Z",
        code="readiness_lost",
        detail="Overlay opened",
    ):
        self.connection.execute(
            """INSERT INTO capture_attempts(attempt_id,session_id,location_id,command_id,
                   attempt_number,status,finished_at,error_code,error_detail)
               VALUES(?,'session',?,?,2,'failed',?,?,?)""",
            (identifier, location, identifier, at, code, detail),
        )
        self.connection.commit()

    def report(self, **options):
        connection = connect_readonly(self.database)
        try:
            result = build_review(connection, self.output, **options)
        finally:
            connection.close()
        return result, json.loads(Path(result["data"]).read_text(encoding="utf-8"))

    def test_readonly_gallery_preserves_database_and_distinguishes_unchecked_hashes(
        self,
    ):
        self.place()
        files = self.capture()
        before = list(self.connection.iterdump())
        with patch(
            "world_locations.capture_evidence.hash_file",
            side_effect=AssertionError("Fast review must not hash files"),
        ):
            summary, report = self.report()
        self.assertEqual(before, list(self.connection.iterdump()))
        self.assertEqual(summary["captures"], 1)
        row = report["rows"][0]
        self.assertEqual(row["publication"], "Ready for hash verification")
        self.assertEqual(row["blockers"], [])
        self.assertFalse(row["hashes_verified"])
        self.assertEqual(row["quality"], "Checks passed")
        self.assertIn("%20%23%20", row["links"]["image"])
        self.assertEqual(
            (self.output.parent / unquote(row["links"]["image"])).resolve(),
            files["png"],
        )
        self.assertEqual(
            (self.output.parent / unquote(row["links"]["sidecar"])).resolve(),
            files["sidecar"],
        )
        _, checked = self.report(verify_files=True)
        self.assertEqual(checked["rows"][0]["publication"], "Evidence checks passed")
        self.assertTrue(checked["rows"][0]["hashes_verified"])

    def test_latest_capture_is_selected_before_limits_and_failed_attempt_is_retained(
        self,
    ):
        self.place()
        self.capture(identifier="older", at="2026-09-04T10:00:00Z")
        self.capture(identifier="newer", at="2026-09-05T10:00:00Z")
        self.connection.execute(
            "UPDATE places SET queue_status='failed' WHERE location_id='place_one'"
        )
        self.failure(
            "place_one",
            identifier="old_failure",
            at="2026-09-05T09:00:00Z",
            detail="Old error",
        )
        self.failure("place_one", identifier="latest_failure", detail="Latest error")
        self.place("second", category="door", status="failed")
        summary, report = self.report(limit=1)
        self.assertEqual(summary["omitted"], 1)
        row = report["rows"][0]
        self.assertEqual(row["capture_id"], "newer")
        self.assertEqual(row["failure_detail"], "Latest error")
        self.assertIn("Location is failed", row["blockers"])
        self.assertTrue(row["retry_command"])
        _, filtered = self.report(limit=0, categories=["door"])
        self.assertEqual([item["id"] for item in filtered["rows"]], ["second"])
        self.assertEqual(filtered["rows"][0]["quality"], "No image")
        _, selected = self.report(location_ids=["place_one"])
        self.assertEqual(len(selected["rows"]), 1)

    def test_rejected_preview_and_metrics_are_distinct_from_capture_evidence(self):
        location = self.place(status="failed")
        preview = self.root / "rejected.webp"
        preview.write_bytes(b"fixture preview")
        self.failure(
            location,
            code="blurred_frame",
            detail=json.dumps(
                {
                    "message": "Rejected blurry frame",
                    "rejected_image": {"path": str(preview)},
                    "validation": {
                        "valid": False,
                        "error_codes": ["blurred_frame"],
                        "sharpness_laplacian_variance": 1.25,
                    },
                }
            ),
        )
        _, report = self.report()
        row = report["rows"][0]
        self.assertFalse(row["has_capture"])
        self.assertEqual(row["quality"], "Blurred")
        self.assertEqual(row["validation_source"], "rejected_attempt")
        self.assertEqual(row["validation"]["sharpness_laplacian_variance"], 1.25)
        self.assertEqual(row["failure_detail"], "Rejected blurry frame")
        self.assertEqual(
            (self.output.parent / unquote(row["links"]["rejected_preview"])).resolve(),
            preview,
        )
        self.assertEqual(row["publication"], "Publication blocked")

    def test_missing_files_and_changed_pose_remain_visible_with_specific_blockers(self):
        self.place()
        files = self.capture()
        files["thumbnail"].unlink()
        self.connection.execute("UPDATE places SET requested_x=8")
        self.connection.commit()
        _, report = self.report()
        row = report["rows"][0]
        self.assertEqual(row["quality"], "File problem")
        self.assertIsNone(row["links"]["thumbnail"])
        self.assertTrue(
            any("Missing thumbnail" in reason for reason in row["blockers"])
        )
        self.assertIn("Capture belongs to an older pose or anchor", row["blockers"])

    def test_untrusted_text_is_escaped_and_retry_commands_preserve_literal_ids(self):
        hostile = "</script><script>alert('oops')</script>"
        location = self.place("place'$(Get-Process)", status="failed", area=hostile)
        self.failure(location, detail=hostile)
        _, report = self.report()
        content = self.output.read_text(encoding="utf-8")
        self.assertNotIn(hostile, content)
        embedded = re.search(
            r'<script id="review-data" type="application/json">(.*?)</script>',
            content,
            re.S,
        )
        self.assertIsNotNone(embedded)
        self.assertEqual(json.loads(embedded.group(1)), report)
        row = report["rows"][0]
        self.assertEqual(row["area"], hostile)
        self.assertIn(
            "--database '" + str(self.database).replace("'", "''") + "' retry",
            row["retry_command"],
        )
        self.assertTrue(
            row["retry_command"].endswith(
                "--recapture --location-id 'place''$(Get-Process)'"
            )
        )

    def test_rejected_and_out_of_scope_places_cannot_be_selected_for_retry(self):
        self.place("rejected", status="failed", review="rejected")
        self.place("outside", status="failed")
        self.connection.execute(
            "UPDATE places SET scope_status='out_of_scope' WHERE location_id='outside'"
        )
        self.connection.commit()
        _, report = self.report()
        self.assertEqual(len(report["rows"]), 2)
        self.assertTrue(all(row["retry_command"] is None for row in report["rows"]))

    def test_report_destinations_cannot_replace_capture_evidence_or_rejected_previews(
        self,
    ):
        self.place()
        files = self.capture()
        captured_bytes = files["sidecar"].read_bytes()
        self.output = files["sidecar"].with_suffix(".html")
        with self.assertRaisesRegex(ValueError, "capture|evidence|input"):
            self.report()
        self.assertEqual(files["sidecar"].read_bytes(), captured_bytes)
        # Protect rejected previews from every attempt, including historical ones.
        self.failure(
            "place_one",
            detail=json.dumps(
                {"rejected_image": {"path": str(self.root / "rejected.json")}}
            ),
        )
        self.output = self.root / "rejected.html"
        with self.assertRaises(ValueError):
            self.report()

    def test_report_pair_rolls_back_if_html_publication_fails(self):
        self.place()
        self.capture()
        self.report()
        before = {
            path: path.read_bytes()
            for path in (self.output, self.output.with_suffix(".json"))
        }
        self.connection.execute("UPDATE places SET named_area='Different area'")
        self.connection.commit()
        replace = os.replace

        def fail_html(source, destination):
            if Path(destination) == self.output:
                raise OSError("simulated HTML write failure")
            return replace(source, destination)

        with patch("artifact_io.os.replace", side_effect=fail_html):
            with self.assertRaisesRegex(OSError, "simulated"):
                self.report()
        for path, content in before.items():
            self.assertEqual(path.read_bytes(), content)

    def test_invalid_inputs_fail_without_writing_and_empty_report_is_valid(self):
        for value in (-1, True, 1.2):
            with self.subTest(limit=value), self.assertRaises(ValueError):
                self.report(limit=value)
        self.assertFalse(self.output.exists())
        self.output = self.output.with_suffix(".json")
        with self.assertRaises(ValueError):
            self.report()
        self.output = self.output.with_suffix(".html")
        _, report = self.report(limit=0)
        self.assertEqual(report["rows"], [])
        with self.assertRaises(sqlite3.OperationalError):
            readonly = connect_readonly(self.database)
            try:
                readonly.execute("DELETE FROM places")
            finally:
                readonly.close()


if __name__ == "__main__":
    unittest.main()
