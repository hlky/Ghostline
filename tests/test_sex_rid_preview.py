from __future__ import annotations

import base64
import struct
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import sex_rid_preview  # noqa: E402


def simple_simd_buffer() -> dict:
    values: list[float] = []
    for _frame in range(2):
        values.extend([0.0, 0.0, 0.0, 0.0])
        values.extend([0.0, 0.0, 0.0, 0.0])
        values.extend([0.0, 0.0, 0.0, 0.0])
        values.extend([1.0, 1.0, 1.0, 1.0])
    values.extend([1.0, 1.0, 1.0, 1.0])
    payload = struct.pack(f"<{len(values)}f", *values)
    payload += struct.pack("<fffh", 1.0, 2.0, 3.0, 0)
    return {
        "$type": "animAnimationBufferSimd",
        "duration": 1.0,
        "numFrames": 2,
        "numJoints": 1,
        "numExtraJoints": 0,
        "numTracks": 0,
        "numExtraTracks": 0,
        "numTranslationsToCopy": 1,
        "numTranslationsToEvalAlignedToSimd": 0,
        "quantizationBits": 0,
        "isScaleConstant": 1,
        "isTrackConstant": 0,
        "defferedBuffer": {"Bytes": base64.b64encode(payload).decode("ascii")},
    }


def simple_compressed_buffer() -> dict:
    payload = struct.pack("<HHfff", 0, 0, 0.0, 0.0, 0.0)
    payload += struct.pack("<HHfff", 65535, 0, 2.0, 0.0, 0.0)
    payload += struct.pack("<HHfff", 1 << 13, 0, 0.0, 0.0, 0.0)
    return {
        "$type": "animAnimationBufferCompressed",
        "duration": 2.0,
        "numFrames": 3,
        "numJoints": 1,
        "numTracks": 0,
        "numAnimKeys": 0,
        "numAnimKeysRaw": 2,
        "numConstAnimKeys": 1,
        "numTrackKeys": 0,
        "numConstTrackKeys": 0,
        "defferedBuffer": {"Bytes": base64.b64encode(payload).decode("ascii")},
    }


class SexRidPreviewTests(unittest.TestCase):
    def test_decodes_unquantized_simd_copy_translation(self) -> None:
        decoded = sex_rid_preview.decode_simd_buffer(simple_simd_buffer())
        self.assertEqual(2, decoded.frame_count)
        self.assertEqual([1.0, 2.0, 3.0], decoded.translations[0][0])
        self.assertEqual([0.0, 0.0, 0.0, 1.0], decoded.rotations[1][0])
        self.assertEqual(decoded.payload_bytes, decoded.bytes_consumed)

    def test_decodes_and_interpolates_compressed_keys(self) -> None:
        decoded = sex_rid_preview.decode_compressed_buffer(simple_compressed_buffer())
        self.assertEqual([0.0, 0.0, 0.0], decoded.translations[0][0])
        self.assertEqual([1.0, 0.0, 0.0], decoded.translations[1][0])
        self.assertEqual([2.0, 0.0, 0.0], decoded.translations[2][0])
        self.assertEqual([0.0, 0.0, 0.0, 1.0], decoded.rotations[1][0])
        self.assertEqual(decoded.payload_bytes, decoded.bytes_consumed)

    def test_parent_transform_and_rid_offset_are_applied(self) -> None:
        decoded = sex_rid_preview.SimdAnimation(
            duration=1.0,
            frame_count=1,
            translations=[[[1.0, 0.0, 0.0], [0.0, 2.0, 0.0]]],
            rotations=[[[0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0]]],
            scales=[[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]],
            tracks=[[]],
            bytes_consumed=0,
            payload_bytes=0,
        )
        positions = sex_rid_preview._model_positions(
            decoded,
            [-1, 0],
            [10.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        )
        self.assertEqual([11.0, 0.0, 0.0], positions[0][0])
        self.assertEqual([11.0, 2.0, 0.0], positions[0][1])

    def test_preview_slug_matches_catalog_contract(self) -> None:
        self.assertEqual(
            "base-x-scenerid",
            sex_rid_preview.preview_slug(r"base\x.scenerid"),
        )

    def test_preview_colors_follow_roles_not_source_order(self) -> None:
        self.assertEqual(
            list(sex_rid_preview.PLAYER_COLOR),
            sex_rid_preview.actor_preview_color("player", 0),
        )
        self.assertEqual(
            list(sex_rid_preview.OTHER_COLOR),
            sex_rid_preview.actor_preview_color("woman_average_1", 1),
        )

    def test_selects_uncluttered_generic_human_pair(self) -> None:
        actors = []
        for signature in (
            "female_average",
            "male_average",
            "int_item_templates_001__generic_lighter",
            "player",
        ):
            actors.append(
                {
                    "tag": {"signature": {"$value": signature}},
                    "animations": [{}],
                }
            )
        document = {
            "Data": {
                "RootChunk": {
                    "$type": "scnRidResource",
                    "actors": actors,
                }
            }
        }
        selected = sex_rid_preview.select_human_actor_signatures(
            document, r"base\sex_01_5s_f.scenerid"
        )
        self.assertEqual(["female_average", "player"], selected)

        document["Data"]["RootChunk"]["actors"] = [
            actor
            for actor in actors
            if actor["tag"]["signature"]["$value"] != "female_average"
        ]
        selected = sex_rid_preview.select_human_actor_signatures(
            document, r"base\sex_02_5s_f.scenerid"
        )
        self.assertEqual(["male_average", "player"], selected)


if __name__ == "__main__":
    unittest.main()
