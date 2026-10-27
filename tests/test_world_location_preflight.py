"""Unattended readiness checks must report blockers without changing the queue."""

import contextlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from world_locations import cli, preflight
from world_locations.config import load_config, output_paths
from world_locations.database import connect
from world_locations.protocol import atomic_write_json


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.config = load_config()
        self.config["output_root"] = str(self.root)
        self.paths = output_paths(self.config)
        connect(self.paths["database"]).close()
        self.mod = self.root / "mod"
        self.mod.mkdir()
        (self.mod / "init.lua").write_text("fixture", encoding="utf-8")
        atomic_write_json(self.paths["runtime"] / "cet-runtime.json", {
            "runtime_path": str(self.paths["runtime"]), "cet_mod_path": str(self.mod),
        })
        atomic_write_json(self.paths["runtime"] / "cet-heartbeat.json", {
            "schema_version": 1, "stage": "idle", "capture_mode_active": False,
            "restoration_verified": True, "protection_contract_version": 1, "freefly_active": True,
        })

    def check(self):
        with (
            mock.patch.object(preflight.importlib, "import_module"),
            mock.patch.object(preflight, "GameWindow") as window,
            mock.patch.object(preflight.shutil, "disk_usage", return_value=mock.Mock(free=100 * 1024**3)),
        ):
            window.return_value.client_rectangle.return_value = (0, 0, 1920, 1080)
            return preflight.check_preflight(self.config, self.paths, self.paths["runtime"])

    def test_ready_checks_leave_database_and_queue_unchanged(self):
        before = self.paths["database"].read_bytes()
        report = self.check()
        self.assertTrue(report["ready"], report)
        self.assertEqual(before, self.paths["database"].read_bytes())
        self.assertEqual(next(c for c in report["checks"] if c["name"] == "hud_templates")["status"], "warning")

    def test_disabled_bridge_and_stale_heartbeat_block_readiness(self):
        (self.mod / "init.lua").rename(self.mod / "init.lua.disabled")
        with mock.patch.object(preflight.RuntimeProtocol, "assert_runtime_alive", side_effect=RuntimeError("stale heartbeat")):
            report = self.check()
        self.assertFalse(report["ready"])
        blocked = {c["name"] for c in report["checks"] if c["status"] == "blocked"}
        self.assertTrue({"installed_bridge", "cet_heartbeat"} <= blocked)

    def test_idle_with_capture_mode_still_active_is_not_ready(self):
        atomic_write_json(self.paths["runtime"] / "cet-heartbeat.json", {
            "schema_version": 1, "stage": "idle", "capture_mode_active": True,
        })
        self.assertFalse(self.check()["ready"])

    def test_preflight_exit_code_reports_blocked_run(self):
        with mock.patch.object(preflight, "check_preflight", return_value={"ready": False}), mock.patch.object(cli, "_print"):
            self.assertEqual(cli.main(["preflight"]), 1)

    def test_final_cleanup_failure_is_a_warning(self):
        args = cli.create_parser().parse_args(["capture"])
        with (
            mock.patch.object(cli, "CaptureController") as controller,
            mock.patch.object(preflight, "keep_awake", contextlib.nullcontext),
        ):
            controller.return_value.run.return_value = {"restoration_verified": False}
            with mock.patch("sys.stderr"):
                result = cli.command_capture(args, self.config, self.paths)
            self.assertFalse(result["restoration_verified"])

    def test_power_request_is_released_after_exception(self):
        request = mock.Mock(return_value=0x80000000)
        with mock.patch.object(preflight.sys, "platform", "win32"), mock.patch.object(preflight.ctypes, "windll", create=True) as dll:
            dll.kernel32.SetThreadExecutionState = request
            with self.assertRaisesRegex(RuntimeError, "interrupted"):
                with preflight.keep_awake():
                    raise RuntimeError("interrupted")
        self.assertEqual(request.call_args_list, [mock.call(0x80000003), mock.call(0x80000000)])


if __name__ == "__main__":
    unittest.main()
