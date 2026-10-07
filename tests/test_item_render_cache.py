from __future__ import annotations

import contextlib
import io
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import item_catalog
import item_render


@contextlib.contextmanager
def database_connection(path):
    with contextlib.closing(sqlite3.connect(path)) as connection:
        with connection:
            yield connection


class FakeProcess:
    def __init__(self, returncode: int = 0):
        self.returncode = returncode
        self.stdout = io.StringIO("renderer fixture\n")

    def wait(self) -> int:
        return self.returncode


class ItemRenderCacheTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.database = self.root / "items.sqlite"
        with database_connection(self.database) as connection:
            item_catalog.create_schema(connection)
            connection.execute(
                "INSERT INTO items VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    "Items.Test",
                    "Test",
                    "",
                    "",
                    "",
                    "",
                    "feet",
                    "",
                    "",
                    "",
                    "[]",
                    "",
                    "[]",
                ),
            )
            connection.execute(
                "INSERT INTO variants VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    "test_variant",
                    "Items.Test",
                    "w",
                    "item.app",
                    "default",
                    "",
                    "item.mesh",
                    "default",
                    "[]",
                ),
            )
        for name in (
            "index.json",
            "red.exe",
            "schema.json",
            "blender.exe",
            "asset.glb",
        ):
            (self.root / name).write_text("{}")
        self.export = {"fingerprint": "asset-v1", "glb": str(self.root / "asset.glb")}
        fingerprint = item_render.render_fingerprint(
            self.export,
            "default",
            self.root / "blender.exe",
            256,
            1,
            "CYCLES",
            ["hero"],
        )
        self.render_root = self.root / "renders" / fingerprint
        self.report_path = self.render_root / "render-report.json"
        self.parameters = dict(
            database=self.database,
            index_path=self.root / "index.json",
            output=self.root,
            ghostline_red=self.root / "red.exe",
            red_schema=self.root / "schema.json",
            blender=self.root / "blender.exe",
            game=self.root,
            item="",
            frame="",
            slot="",
            limit=1,
            resolution=256,
            samples=1,
            engine="CYCLES",
            views=["hero"],
            batch_size=1,
            workers=1,
            export_workers=1,
            reuse_compatible=False,
        )

    def write_report(
        self, *, root: Path | None = None, image: bool = True, **overrides
    ) -> Path:
        root = root or self.render_root
        root.mkdir(parents=True, exist_ok=True)
        hero = root / "hero.png"
        if image:
            hero.write_bytes(b"nonempty renderer image")
        report = {
            "schema_version": 1,
            "glb": self.export["glb"],
            "appearance": "default",
            "resolution": 256,
            "samples": 1,
            "engine": "CYCLES",
            "images": [str(hero)],
            **overrides,
        }
        path = root / "render-report.json"
        path.write_text(json.dumps(report))
        return path

    def run_render(self, popen):
        with (
            patch.object(
                item_render,
                "prepare_material_exports_bulk",
                return_value=({("item.mesh", "default"): self.export}, {}),
            ),
            patch.object(item_render.subprocess, "Popen", side_effect=popen) as process,
            contextlib.redirect_stdout(io.StringIO()),
        ):
            result = item_render.render_variants(**self.parameters)
        with database_connection(self.database) as connection:
            statuses = connection.execute("SELECT status FROM renders").fetchall()
        return result, statuses, process

    def test_valid_exact_cache_reuses_without_starting_renderer(self) -> None:
        self.write_report()
        result, statuses, process = self.run_render(AssertionError("Unexpected render"))
        self.assertEqual(
            (result["rendered"], result["reused"], result["failures"]), (0, 1, [])
        )
        self.assertEqual(statuses, [("complete",)])
        process.assert_not_called()

    def test_missing_image_attempts_render_and_failure_revokes_old_complete_record(
        self,
    ) -> None:
        self.write_report(image=False)
        with database_connection(self.database) as connection:
            connection.execute(
                "INSERT INTO renders VALUES (?,?,?,?,?,?,?,?)",
                (
                    "old",
                    "test_variant",
                    "missing.png",
                    "[]",
                    "old",
                    "old",
                    "complete",
                    "",
                ),
            )
        result, statuses, process = self.run_render(OSError("Blender could not start"))
        self.assertEqual((result["rendered"], result["reused"]), (0, 0))
        self.assertEqual(len(result["failures"]), 1)
        self.assertIn("could not start", result["failures"][0]["error"])
        self.assertEqual(statuses, [("failed",)])
        process.assert_called_once()

    def test_malformed_or_mismatched_reports_are_rejected_by_both_cache_paths(
        self,
    ) -> None:
        values = [
            "{",
            "[]",
            {"samples": 2},
            {"resolution": 512},
            {"engine": "OTHER"},
            {"images": []},
            {"images": [123]},
            {"appearance": None},
            {"glb": None},
        ]
        for value in values:
            with self.subTest(value=value):
                self.write_report(**(value if isinstance(value, dict) else {}))
                if isinstance(value, str):
                    self.report_path.write_text(value)
                self.assertFalse(
                    item_render.reusable_render_report(
                        self.report_path, 256, 1, "CYCLES", ["hero"]
                    )
                )
                self.assertEqual(
                    item_render.compatible_render_reports(
                        self.root / "renders", 256, 1, "CYCLES", ["hero"]
                    ),
                    {},
                )
        self.write_report(appearance="different")
        self.assertFalse(
            item_render.reusable_render_report(
                self.report_path, 256, 1, "CYCLES", ["hero"], appearance="default"
            )
        )
        self.write_report(glb=str(self.root / "different.glb"))
        self.assertFalse(
            item_render.reusable_render_report(
                self.report_path, 256, 1, "CYCLES", ["hero"], glb=self.export["glb"]
            )
        )

    def test_valid_compatible_cache_uses_the_same_validation(self) -> None:
        self.write_report(image=False)
        compatible = self.write_report(root=self.root / "renders/previous-key")
        self.parameters["reuse_compatible"] = True
        result, statuses, process = self.run_render(AssertionError("Unexpected render"))
        self.assertEqual(
            (result["rendered"], result["reused"], result["failures"]), (0, 1, [])
        )
        self.assertEqual(statuses, [("complete",)])
        with database_connection(self.database) as connection:
            image = connection.execute("SELECT hero_path FROM renders").fetchone()[0]
        self.assertEqual(Path(image).parent, compatible.parent)
        process.assert_not_called()

    def test_fresh_output_is_validated_before_marking_complete(self) -> None:
        def render(command, **kwargs):
            self.write_report()
            return FakeProcess()

        result, statuses, process = self.run_render(render)
        self.assertEqual(
            (result["rendered"], result["reused"], result["failures"]), (1, 0, [])
        )
        self.assertEqual(statuses, [("complete",)])
        process.assert_called_once()

    def test_failed_or_invalid_fresh_render_cannot_publish_complete(self) -> None:
        for mode in (
            "nonzero",
            "explicit-failure",
            "missing-image",
            "wrong-settings",
            "malformed-report",
        ):
            with self.subTest(mode=mode):
                self.report_path.unlink(missing_ok=True)

                def render(command, **kwargs):
                    self.write_report(
                        resolution=512 if mode == "wrong-settings" else 256
                    )
                    if mode == "missing-image":
                        (self.render_root / "hero.png").unlink()
                    elif mode == "malformed-report":
                        self.report_path.write_text("{")
                    elif mode == "explicit-failure":
                        receipt = Path(command[command.index("--batch-report") + 1])
                        receipt.write_text(
                            json.dumps(
                                {
                                    "completed": [],
                                    "failures": [
                                        {
                                            "output": str(self.render_root),
                                            "error": "failed job",
                                        }
                                    ],
                                }
                            )
                        )
                    return FakeProcess(
                        1 if mode in ("nonzero", "explicit-failure") else 0
                    )

                result, statuses, _process = self.run_render(render)
                self.assertEqual((result["rendered"], result["reused"]), (0, 0))
                self.assertEqual(len(result["failures"]), 1)
                self.assertNotIn(("complete",), statuses)
                self.assertFalse(
                    self.report_path.exists(),
                    "A failed renderer must not leave a reusable success receipt",
                )

    def test_completed_job_survives_a_partially_failed_batch(self) -> None:
        def render(command, **kwargs):
            self.write_report()
            receipt = Path(command[command.index("--batch-report") + 1])
            receipt.write_text(
                json.dumps(
                    {
                        "completed": [str(self.render_root)],
                        "failures": [{"output": "unrelated", "error": "other job"}],
                    }
                )
            )
            return FakeProcess(1)

        result, statuses, _process = self.run_render(render)
        self.assertEqual((result["rendered"], result["failures"]), (1, []))
        self.assertEqual(statuses, [("complete",)])


if __name__ == "__main__":
    unittest.main()
