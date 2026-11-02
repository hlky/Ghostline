from __future__ import annotations

import sys
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"

sys.path.insert(0, str(TOOLS))

import ghostline_red


class GhostlineRedTests(unittest.TestCase):
    def test_cr2w_deserializer_needs_only_json_and_schema(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            raw=root/'resource.json'
            output=root/'empty-output/resource.questphase'
            cli=root/'ghostline-red.exe'
            schema=root/'schema.json'
            raw.write_text('{}')
            with patch('ghostline_red.ensure_schema',return_value=schema), \
                 patch('ghostline_red.subprocess.run') as run:
                ghostline_red.deserialize(raw,output,red_cli=cli,schema=schema)
            run.assert_called_once_with([str(cli),'cr2w-deserialize',str(raw),str(output),
                                         '--schema',str(schema)],check=True)
            self.assertTrue(output.parent.is_dir())

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


class SchemaReuseTests(unittest.TestCase):
    def test_existing_schema_is_reused_without_hashing_or_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            schema = Path(directory) / "schema.json"
            schema.write_text('{"stable": true}', encoding="utf-8")
            with patch("ghostline_red.subprocess.run") as run:
                result = ghostline_red.ensure_schema(Path(directory) / "missing-cli", schema)
            self.assertEqual(result, schema)
            self.assertEqual(schema.read_text(encoding="utf-8"), '{"stable": true}')
            run.assert_not_called()

    def test_missing_schema_is_generated_once(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            schema = root / "schema.json"
            cli = root / "ghostline-red.exe"
            cli.touch()
            def generate(command, **kwargs):
                Path(command[-1]).write_text('{"Example": {}}', encoding="utf-8")
                return subprocess.CompletedProcess(command, 0)
            with patch("ghostline_red.subprocess.run", side_effect=generate) as run:
                ghostline_red.ensure_schema(cli, schema)
                ghostline_red.ensure_schema(cli, schema)
            self.assertEqual(run.call_count, 1)
            self.assertEqual(json.loads(schema.read_text(encoding="utf-8")), {"Example": {}})

    def test_failed_generation_does_not_publish_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            schema = root / "schema.json"
            cli = root / "ghostline-red.exe"
            cli.touch()
            with patch("ghostline_red.subprocess.run", side_effect=subprocess.CalledProcessError(1, "schema-generate")):
                with self.assertRaises(subprocess.CalledProcessError):
                    ghostline_red.ensure_schema(cli, schema)
            self.assertFalse(schema.exists())


if __name__ == "__main__":
    unittest.main()
