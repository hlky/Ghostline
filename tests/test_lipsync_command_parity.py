from __future__ import annotations
import contextlib
import io
import json
import struct
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import compile_lipsync_line as single
import compile_lipsync_manifest as batch
from build_lipsync_dataset import PhoneAlignment
from lipsync_glb import write_glb


class LipsyncCommandParityTests(unittest.TestCase):
    def test_single_and_manifest_compile_identical_clips_and_options(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            donor, model_path = root / "donor.glb", root / "model.json"
            audio = root / "historical_audio.wav"
            audio.write_bytes(b"mock aligner input")
            document = {
                "skins": [{"extras": {"trackNames": ["jaw"]}}],
                "animations": [
                    {
                        "name": "source",
                        "samplers": [{"input": 0}],
                        "extras": {"trackKeys": []},
                    }
                ],
                "accessors": [{"bufferView": 0}],
                "bufferViews": [{"buffer": 0, "byteLength": 4, "byteOffset": 0}],
                "buffers": [{"byteLength": 4}],
            }
            write_glb(donor, document, [(single.BIN_CHUNK, struct.pack("<f", 1.0))])
            model = {
                "tracks": ["jaw"],
                "phase": [0.0, 0.5, 1.0],
                "silence": {"median": [0.0]},
                "phones": {"AA": {"curves": {"median": [[0.0], [0.5], [1.0]]}}},
                "contexts": {"previous": [], "next": []},
                "boundaries": {
                    "AA": {
                        "anticipation_ms": 0,
                        "anticipation_censored": False,
                        "release_ms": 0,
                        "release_censored": False,
                    }
                },
            }
            model_path.write_text(json.dumps(model))
            manifest = root / "manifest.json"
            manifest.write_text(
                json.dumps(
                    {
                        "spoken_lines": [
                            {
                                "key": "hello",
                                "string_id": "42",
                                "text": "Hello",
                                "audio_path": "mod\\q\\historical_audio.wem",
                                "phones": ["AA"],
                            }
                        ]
                    }
                )
            )
            alignment = ([PhoneAlignment("AA", 0.0, 1.0, 0.9, 0.0, 1.0)], 1.0, "cpu")
            settings = [
                "--source",
                "source",
                "--model",
                str(model_path),
                "--fps",
                "20",
                "--clear-donor-controls",
                "--zero-track-prefix",
                "jaw",
            ]
            output_single, output_batch = root / "single.glb", root / "batch.glb"
            with (
                patch.object(single, "CTCPhoneAligner") as aligner,
                contextlib.redirect_stdout(io.StringIO()),
                patch.object(
                    sys,
                    "argv",
                    [
                        "single",
                        str(audio),
                        str(donor),
                        str(output_single),
                        "--text",
                        "Hello",
                        "--phones",
                        "AA",
                        "--locstring",
                        "42",
                        *settings,
                    ],
                ),
            ):
                aligner.return_value.align.return_value = alignment
                single.main()
            with patch.object(batch, "CTCPhoneAligner") as aligner:
                aligner.return_value.align.return_value = alignment
                args = batch.build_parser().parse_args(
                    [
                        str(manifest),
                        str(root),
                        str(donor),
                        str(output_batch),
                        "--reports",
                        str(root / "reports"),
                        *settings,
                    ]
                )
                batch.compile_manifest(args)
            self.assertEqual(output_single.read_bytes(), output_batch.read_bytes())
            report_single = json.loads(
                output_single.with_suffix(".alignment.json").read_text()
            )
            report_batch = json.loads(
                (root / "reports/hello.alignment.json").read_text()
            )
            for report in [report_single, report_batch]:
                report.pop("output_glb")
            self.assertEqual(report_single, report_batch)
            self.assertEqual(report_batch["zeroed_tracks"], ["jaw"])


if __name__ == "__main__":
    unittest.main()
