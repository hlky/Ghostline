from __future__ import annotations

import json
import io
import struct
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import explore_lipsync  # noqa: E402


def fixture_document() -> dict:
    return {
        "accessors": [{"max": [1.5]}],
        "skins": [
            {
                "extras": {
                    "rigPath": r"base\characters\test.rig",
                    "boneNames": ["Root", "Head"],
                    "trackNames": ["lipSyncEnvelope", "jaw_mid_openLipsyncPoseOutput"],
                }
            }
        ],
        "animations": [
            {
                "name": "f_000000000000002A",
                "samplers": [{"input": 0}],
                "extras": {
                    "trackKeys": [
                        {"trackIndex": 1, "time": 0.0, "value": 0.0},
                        {"trackIndex": 1, "time": 1.0, "value": 0.8},
                    ],
                    "constTrackKeys": [{"trackIndex": 0, "time": 1.25, "value": 1.0}],
                },
            }
        ],
    }


class LipsyncExplorerTests(unittest.TestCase):
    def test_reads_glb_json_chunk(self) -> None:
        payload = json.dumps(fixture_document(), separators=(",", ":")).encode("utf-8")
        payload += b" " * (-len(payload) % 4)
        total = 12 + 8 + len(payload)
        blob = struct.pack("<4sII", b"glTF", 2, total)
        blob += struct.pack("<II", len(payload), explore_lipsync.GLB_JSON_CHUNK) + payload
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "sample.glb"
            path.write_bytes(blob)
            self.assertEqual(explore_lipsync.read_glb_json(path), fixture_document())

    def test_indexes_locstring_duration_and_curve_counts(self) -> None:
        explorer = explore_lipsync.LipsyncExplorer(fixture_document())
        self.assertEqual(explorer.rig_path, r"base\characters\test.rig")
        self.assertEqual(
            explorer.lines(),
            [
                explore_lipsync.LineInfo(
                    index=0,
                    name="f_000000000000002A",
                    locstring_id="42",
                    duration=1.5,
                    dynamic_tracks=1,
                    dynamic_keys=2,
                    const_tracks=1,
                )
            ],
        )

    def test_selects_lines_and_filters_named_tracks(self) -> None:
        explorer = explore_lipsync.LipsyncExplorer(fixture_document())
        rows = explorer.tracks("42", "jaw")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].name, "jaw_mid_openLipsyncPoseOutput")
        self.assertEqual((rows[0].keys, rows[0].minimum, rows[0].maximum), (2, 0.0, 0.8))
        self.assertEqual(explorer.select_line("0x2a")[0].locstring_id, "42")

    def test_returns_timed_samples_by_track_name(self) -> None:
        explorer = explore_lipsync.LipsyncExplorer(fixture_document())
        rows = explorer.samples("0", "jaw_mid_open")
        self.assertEqual([(row.time, row.value) for row in rows], [(0.0, 0.0), (1.0, 0.8)])
        self.assertTrue(all(row.track_index == 1 for row in rows))

    def test_csv_writer_uses_single_newlines(self) -> None:
        output = io.StringIO()
        explore_lipsync.write_csv([{"time": 0.0, "value": 0.8}], output)
        self.assertEqual(output.getvalue(), "time,value\n0.0,0.8\n")


if __name__ == "__main__":
    unittest.main()
