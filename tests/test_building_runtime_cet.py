"""Execute CET callback regressions without a running game when Lua is available."""
import os
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
LUA = shutil.which("lua")
if not LUA:
    candidate = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs/Lua/bin/lua.exe"
    LUA = str(candidate) if candidate.is_file() else None


class RuntimeCETTests(unittest.TestCase):
    @unittest.skipUnless(LUA, "Lua interpreter is unavailable")
    def test_shutter_saved_state_migration(self):
        result = subprocess.run([LUA, "tests/fixtures/building_shutter_cet.lua"], cwd=ROOT,
                                capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Shutter migration passed", result.stdout)

    @unittest.skipUnless(LUA, "Lua interpreter is unavailable")
    def test_failed_queries_block_walks_and_teleport_jumps_cannot_pass(self):
        result = subprocess.run([LUA, "tests/fixtures/building_runtime_cet.lua"], cwd=ROOT,
                                capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Synchronous engine jump detected", result.stdout)


if __name__ == "__main__":
    unittest.main()
