from __future__ import annotations

import json
from pathlib import Path
import tempfile
import shutil
import subprocess
import unittest

from tools.gq003_black_lantern_scout import CET_MOD_NAME, import_log, install, validate_log


class BlackLanternScoutTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which('lua'), 'Lua runtime unavailable')
    def test_lua_capture_safety_and_exploration(self) -> None:
        root = Path(__file__).resolve().parents[1]
        for scenario in ('malformed', 'rename_failure', 'save', 'presets'):
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory() as directory:
                result = subprocess.run(
                    ['lua', str(root / 'tests/gq003_scout_runtime.lua'),
                     str(root / 'tools/gq003_black_lantern_scout_cet/init.lua'), scenario],
                    cwd=directory, capture_output=True, text=True,
                )
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_validates_and_imports_capture_log(self) -> None:
        document = {
            "schema_version": 1,
            "quest": "gq003",
            "captures": [
                {
                    "id": "gq003-001",
                    "slot_id": "freight_yard",
                    "target_id": "dispatch_relay",
                    "role_id": "device",
                    "position": {"x": 1.0, "y": 2.0, "z": 3.0},
                }
            ],
        }
        self.assertIs(document, validate_log(document))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.json"
            output = root / "output.json"
            source.write_text(json.dumps(document), encoding="utf-8")
            imported = import_log(source, output)
            self.assertEqual("freight_yard", imported["captures"][0]["slot_id"])
            self.assertEqual("dispatch_relay", imported["captures"][0]["target_id"])
            self.assertEqual("device", imported["captures"][0]["role_id"])
            self.assertEqual(document, json.loads(output.read_text(encoding="utf-8")))

    def test_rejects_invalid_position(self) -> None:
        with self.assertRaisesRegex(ValueError, "numeric XYZ"):
            validate_log(
                {
                    "schema_version": 1,
                    "quest": "gq003",
                    "captures": [{"slot_id": "relay", "target_id": "core", "position": {"x": "bad"}}],
                }
            )

    def test_installs_without_replacing_modified_runtime(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            game = Path(directory)
            cet = game / "bin/x64/plugins/cyber_engine_tweaks"
            cet.mkdir(parents=True)
            destination = install(game)
            target = destination / "init.lua"
            self.assertEqual(CET_MOD_NAME, destination.name)
            self.assertIn("Black Lantern Scout", target.read_text(encoding="utf-8"))
            self.assertIn("cleanup_boundary", target.read_text(encoding="utf-8"))
            self.assertIn("escort_gate_03", target.read_text(encoding="utf-8"))
            target.write_text("locally modified", encoding="utf-8")
            with self.assertRaisesRegex(SystemExit, "refusing to overwrite"):
                install(game)


if __name__ == "__main__":
    unittest.main()
