from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import toolchain


class ToolchainTests(unittest.TestCase):
    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.root = Path(self.stack.enter_context(tempfile.TemporaryDirectory()))
        self.config = self.root / "toolchain.local.json"
        self.stack.enter_context(mock.patch.object(toolchain, "ROOT", self.root))
        self.stack.enter_context(mock.patch.object(toolchain, "CONFIG_PATH", self.config))
        self.stack.enter_context(mock.patch.dict(os.environ, {}, clear=True))
        self.paths = {name: self.root / f"{name}.exe" for name in ("explicit", "environment", "config", "path", "installed")}
        for path in self.paths.values():
            path.write_bytes(b"tool")
        self.which = self.stack.enter_context(mock.patch.object(toolchain.shutil, "which", return_value=str(self.paths["path"])))
        self.stack.enter_context(mock.patch.object(toolchain, "_installed_candidates", return_value=[self.paths["installed"]]))

    def test_explicit_environment_config_path_installed_precedence(self):
        self.config.write_text(json.dumps({"blender": self.paths["config"].name}))
        os.environ["GHOSTLINE_BLENDER"] = str(self.paths["environment"])
        self.assertEqual(toolchain.resolve_tool("blender", self.paths["explicit"]), self.paths["explicit"])
        self.assertEqual(toolchain.resolve_tool("blender"), self.paths["environment"])
        del os.environ["GHOSTLINE_BLENDER"]
        self.assertEqual(toolchain.resolve_tool("blender"), self.paths["config"])
        self.config.unlink()
        self.assertEqual(toolchain.resolve_tool("blender"), self.paths["path"])
        self.which.return_value = None
        self.assertEqual(toolchain.resolve_tool("blender"), self.paths["installed"])

    def test_invalid_overrides_never_fall_back_to_an_installed_tool(self):
        missing = self.root / "missing.exe"
        for source in ("explicit", "environment", "config"):
            with self.subTest(source=source):
                explicit = missing if source == "explicit" else None
                if source == "environment":
                    os.environ["GHOSTLINE_BLENDER"] = str(missing)
                if source == "config":
                    self.config.write_text(json.dumps({"blender": str(missing)}))
                with self.assertRaises(FileNotFoundError):
                    toolchain.resolve_tool("blender", explicit)
                self.assertEqual(toolchain.resolve_tool("blender", explicit, required=False), missing)
                os.environ.pop("GHOSTLINE_BLENDER", None)
                self.config.unlink(missing_ok=True)

    def test_snapshot_is_immutable_and_environment_changes_do_not_retarget_it(self):
        os.environ["GHOSTLINE_RED"] = str(self.paths["environment"])
        snapshot = toolchain.Toolchain.resolve(ghostline_red=None)
        os.environ["GHOSTLINE_RED"] = str(self.paths["explicit"])
        self.assertEqual(snapshot["ghostline_red"], self.paths["environment"])
        with self.assertRaises(TypeError):
            snapshot.paths["ghostline_red"] = self.paths["explicit"]

    def test_game_override_requires_its_executable(self):
        game = self.root / "game"
        game.mkdir()
        with self.assertRaises(FileNotFoundError):
            toolchain.resolve_tool("game", game)
        executable = game / "bin/x64/Cyberpunk2077.exe"
        executable.parent.mkdir(parents=True)
        executable.write_bytes(b"game")
        self.assertEqual(toolchain.resolve_tool("game", game), game)

    def test_invalid_configuration_and_unknown_names_fail_clearly(self):
        self.config.write_text('{"blender": null}')
        with self.assertRaisesRegex(ValueError, "known tool names"):
            toolchain.resolve_tool("blender")
        with self.assertRaisesRegex(ValueError, "Unknown tool"):
            toolchain.resolve_tool("unsupported")


if __name__ == "__main__":
    unittest.main()
