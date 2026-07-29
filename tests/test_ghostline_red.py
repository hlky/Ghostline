from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"

sys.path.insert(0, str(TOOLS))

import ghostline_red


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


if __name__ == "__main__":
    unittest.main()
