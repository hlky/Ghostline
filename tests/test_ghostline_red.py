from __future__ import annotations

import sys
import json
import subprocess
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"

sys.path.insert(0, str(TOOLS))

import ghostline_red
import artifact_io


class GhostlineRedTests(unittest.TestCase):
    def test_localization_deserializer_uses_typed_writer(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "gqt005.json.json"
            template = root / "template.json"
            output = root / "out" / "gqt005.json"
            cli = root / "ghostline-red.exe"
            raw.write_text("{}", encoding="utf-8")
            template.write_bytes(b"CR2W")

            with patch("ghostline_red.subprocess.run") as run:
                ghostline_red.deserialize_localization(
                    raw,
                    output,
                    template=template,
                    red_cli=cli,
                )

            self.assertTrue(output.parent.is_dir())
            run.assert_called_once_with(
                [
                    str(cli),
                    "cr2w-deserialize-localization",
                    str(raw),
                    str(output),
                    "--template",
                    str(template),
                ],
                check=True,
            )


class SchemaIdentityTests(unittest.TestCase):
    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.root = Path(self.stack.enter_context(tempfile.TemporaryDirectory()))
        self.cli = self.root / "ghostline-red.exe"
        self.cli.write_bytes(b"writer-v1")
        self.schema = self.root / "schema.json"
        self.receipt = self.root / "schema.json.identity.json"
        self.types = self.root / "WolvenKit"
        self.types.mkdir()
        self.revision = b"pin-v1"
        self.diff = b""
        self.untracked = b""
        self.ignored = b""
        self.generated = 0
        self.failure = None
        self.stack.enter_context(patch.object(ghostline_red, "WOLVENKIT_SOURCE", self.types))
        self.stack.enter_context(patch.object(ghostline_red.subprocess, "run", side_effect=self.run_command))

    def run_command(self, command, **kwargs):
        if command[0] == "git":
            operation = command[3]
            if operation == "rev-parse":
                value = self.revision
            elif operation == "diff":
                value = self.diff
            else:
                value = self.ignored if "--ignored" in command else self.untracked
            return subprocess.CompletedProcess(command, 0, stdout=value)
        self.generated += 1
        output = Path(command[-1])
        if self.failure == "process":
            output.write_text('{"partial":')
            raise subprocess.CalledProcessError(1, command)
        document = [] if self.failure == "shape" else {f"Generated{self.generated}": {"base": None, "properties": {}}}
        output.write_text(json.dumps(document))
        return subprocess.CompletedProcess(command, 0)

    def test_writer_pin_schema_and_dirty_type_changes_invalidate_reuse(self):
        ghostline_red.ensure_schema(self.cli, self.schema)
        ghostline_red.ensure_schema(self.cli, self.schema)
        self.assertEqual(self.generated, 1)
        self.cli.write_bytes(b"writer-v2")
        ghostline_red.ensure_schema(self.cli, self.schema)
        self.revision = b"pin-v2"
        ghostline_red.ensure_schema(self.cli, self.schema)
        self.schema.write_text('{"tampered":true}')
        ghostline_red.ensure_schema(self.cli, self.schema)
        self.diff = b"changed tracked RED property"
        ghostline_red.ensure_schema(self.cli, self.schema)
        self.assertEqual(self.generated, 5)

    def test_untracked_and_ignored_csharp_contents_participate_in_identity(self):
        source = self.types / "NewType.cs"
        source.write_text("class NewType {}")
        self.untracked = b"NewType.cs\0"
        ghostline_red.ensure_schema(self.cli, self.schema)
        source.write_text("class NewType { int Value; }")
        ghostline_red.ensure_schema(self.cli, self.schema)
        generated = self.types / "obj/Generated.cs"
        generated.parent.mkdir()
        generated.write_text("class GeneratedType {}")
        self.ignored = b"obj/Generated.cs\0"
        ghostline_red.ensure_schema(self.cli, self.schema)
        self.assertEqual(self.generated, 3)

    def test_failed_or_invalid_regeneration_preserves_schema_and_receipt(self):
        ghostline_red.ensure_schema(self.cli, self.schema)
        previous = (self.schema.read_bytes(), self.receipt.read_bytes())
        self.cli.write_bytes(b"new-writer")
        for failure, error in (("process", subprocess.CalledProcessError), ("shape", ValueError)):
            self.failure = failure
            with self.subTest(failure=failure), self.assertRaises(error):
                ghostline_red.ensure_schema(self.cli, self.schema)
            self.assertEqual((self.schema.read_bytes(), self.receipt.read_bytes()), previous)

    def test_receipt_publication_failure_rolls_back_the_schema(self):
        ghostline_red.ensure_schema(self.cli, self.schema)
        previous = (self.schema.read_bytes(), self.receipt.read_bytes())
        self.cli.write_bytes(b"new-writer")
        replace = artifact_io.os.replace

        def fail_receipt(source, destination):
            if Path(destination) == self.receipt:
                raise PermissionError("identity receipt is locked")
            return replace(source, destination)

        with patch.object(artifact_io.os, "replace", side_effect=fail_receipt), self.assertRaises(PermissionError):
            ghostline_red.ensure_schema(self.cli, self.schema)
        self.assertEqual((self.schema.read_bytes(), self.receipt.read_bytes()), previous)


if __name__ == "__main__":
    unittest.main()
