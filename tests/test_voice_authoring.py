from __future__ import annotations

import contextlib
import csv
import hashlib
import io
import json
import sys
import tempfile
import unittest
import wave
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import build_voice_selection_csv as review
import promote_voice_selections as promotion


def wav(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as stream:
        stream.setnchannels(1)
        stream.setsampwidth(2)
        stream.setframerate(24000)
        stream.writeframes(b"\0\0" * 240)


class VoiceAuthoringTests(unittest.TestCase):
    def test_report_review_selection_and_promotion_for_two_designed_speakers(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            lines, candidates = [], []
            for speaker in ("Iris", "Patch"):
                key = speaker.lower()
                path = root / "dialogue" / f"{key}-version00.wav"
                wav(path)
                lines.append(
                    {
                        "key": key,
                        "speaker": speaker,
                        "text": "Hello",
                        "audio_path": f"mod\\q\\{key}.wem",
                    }
                )
                candidates.append(
                    {
                        "line_key": key,
                        "speaker": speaker,
                        "version": 0,
                        "design": f"{key}-design",
                        "wav": path.relative_to(root).as_posix(),
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    }
                )
            manifest = {"spoken_lines": lines}
            report = root / "render-report.json"
            report.write_text(
                json.dumps({"schema_version": 1, "candidates": candidates})
            )
            rows = review.report_rows(manifest, report)
            for row in rows:
                row["selected"] = "x"
            csv_path = root / "selected.csv"
            with csv_path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)
            manifest_path = root / "manifest.json"
            manifest_path.write_text(json.dumps(manifest))
            output = root / "source"
            with (
                patch.object(
                    sys,
                    "argv",
                    [
                        "promote",
                        "--csv",
                        str(csv_path),
                        "--manifest",
                        str(manifest_path),
                        "--output-dir",
                        str(output),
                    ],
                ),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                promotion.main()
            receipt = json.loads((output / "selection-receipt.json").read_text())
            self.assertEqual(
                receipt["voice_designs"],
                {"iris": "iris-design", "patch": "patch-design"},
            )
            self.assertEqual(
                {path.name for path in output.glob("*.wav")}, {"iris.wav", "patch.wav"}
            )
            self.assertEqual(len(rows), 2)
            self.assertEqual(
                (output / "iris.wav").read_bytes(),
                (root / "dialogue/iris-version00.wav").read_bytes(),
            )
            (root / "dialogue/iris-version00.wav").write_bytes(b"modified")
            with self.assertRaisesRegex(ValueError, "changed after rendering"):
                review.report_rows(manifest, report)

    def test_empty_inventory_is_an_error_and_legacy_reference_is_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = {
                "spoken_lines": [{"key": "hello", "speaker": "Iris", "text": "Hi"}]
            }
            report = root / "report.json"
            report.write_text('{"schema_version":1,"candidates":[]}')
            with self.assertRaisesRegex(ValueError, "no candidates"):
                review.report_rows(manifest, report)
            wav(root / "design/reference.wav")
            wav(root / "design/hello/take-1.wav")
            with self.assertRaisesRegex(ValueError, "reference-speaker"):
                review.legacy_rows(manifest, root)
            rows = review.legacy_rows(manifest, root, "Iris", "Reference text")
            self.assertEqual(rows[0]["speaker"], "Iris")
            self.assertEqual(rows[1]["line_key"], "hello")

    def test_per_speaker_configuration_rejects_a_mixed_design(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "voice.wav"
            wav(path)
            manifest = {
                "voice_designs": {"Iris": "approved"},
                "spoken_lines": [{"key": "hello", "speaker": "Iris"}],
            }
            rows = [
                {
                    "selected": "x",
                    "line_key": "hello",
                    "speaker": "Iris",
                    "design": "other",
                    "file": str(path),
                }
            ]
            with self.assertRaisesRegex(ValueError, "not selected design"):
                promotion.validate(manifest, rows)


if __name__ == "__main__":
    unittest.main()
