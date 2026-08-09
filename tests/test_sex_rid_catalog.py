from __future__ import annotations

import base64
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import sex_rid_catalog  # noqa: E402


def tag(signature: str, serial: int) -> dict:
    return {
        "$type": "scnRidTag",
        "serialNumber": {"serialNumber": serial},
        "signature": {"$value": signature},
    }


def buffer(duration: float = 2.0, joints: int = 71) -> dict:
    return {
        "$type": "animAnimationBufferSimd",
        "duration": duration,
        "numFrames": 61,
        "numJoints": joints,
        "numTracks": 4,
        "defferedBuffer": {"Bytes": base64.b64encode(b"pose").decode("ascii")},
    }


def body_clip(name: str, serial: int) -> dict:
    return {
        "animation": {
            "Data": {
                "$type": "animAnimation",
                "name": {"$value": name},
                "animBuffer": {"Data": buffer()},
            }
        },
        "bonesCount": 71,
        "motionExtracted": 1,
        "trajectoryBoneIndex": 1,
        "events": {"Data": {"events": [{"$type": "animAnimEvent"}]}},
        "offset": {
            "position": {"X": 1, "Y": 2, "Z": 3},
            "orientation": {"i": 0, "j": 0, "k": 0, "r": 1},
        },
        "tag": tag(name + "_tag", serial),
    }


def rid_document() -> dict:
    return {
        "Data": {
            "RootChunk": {
                "$type": "scnRidResource",
                "actors": [
                    {
                        "tag": tag("female_average", 0),
                        "animations": [body_clip("first", 1), body_clip("second", 2)],
                        "facialAnimations": [],
                        "cyberwareAnimations": [],
                    }
                ],
                "cameras": [
                    {
                        "tag": tag("Camera", 3),
                        "animations": [
                            {
                                "tag": tag("Camera_anim_0", 4),
                                "animation": {"Data": buffer(2.0, 1)},
                            }
                        ],
                    }
                ],
                "nextSerialNumber": 5,
                "version": 2,
            }
        }
    }


class SexRidCatalogTests(unittest.TestCase):
    def test_detects_opaque_reflection_payloads(self) -> None:
        self.assertTrue(
            sex_rid_catalog._contains_raw_data(
                {"x": [{"$type": "animAnimationBufferCompressed", "$rawData": "AA=="}]}
            )
        )
        self.assertFalse(
            sex_rid_catalog._contains_raw_data({"x": [{"$rawData": "AA=="}]})
        )
        self.assertFalse(sex_rid_catalog._contains_raw_data({"x": [{"Bytes": "AA=="}]}))

    def test_inspect_supports_multiple_clips_per_actor(self) -> None:
        entry = sex_rid_catalog.inspect_rid(
            rid_document(),
            r"base\animations\quest\lore\generic_sex\intercourse\sex_09_2s_f.scenerid",
        )
        self.assertEqual(2, len(entry["actors"][0]["body"]))
        self.assertEqual("generic_intercourse", entry["inferred"]["family"])
        self.assertEqual("female", entry["inferred"]["player_frame_hint"])
        self.assertEqual(2, entry["inferred"]["nominal_duration_seconds"])
        self.assertEqual(2.0, entry["duration_seconds"])
        self.assertEqual(30.0, entry["actors"][0]["body"][0]["buffer"]["fps"])

    def test_scene_usage_counts_duplicate_resource_rows(self) -> None:
        scene = {
            "Header": {"ArchiveFileName": r"x\q003.scene"},
            "Data": {
                "RootChunk": {
                    "$type": "scnSceneResource",
                    "ridResources": [
                        {
                            "id": {"id": 10},
                            "ridResource": {
                                "DepotPath": {"$value": r"base\x.scenerid"}
                            },
                        },
                        {
                            "id": {"id": 10},
                            "ridResource": {
                                "DepotPath": {"$value": r"base\x.scenerid"}
                            },
                        },
                    ],
                }
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "q003.scene.json"
            path.write_text(json.dumps(scene), encoding="utf-8")
            usage = sex_rid_catalog.scene_usage([path])
        self.assertEqual(2, usage[r"base\x.scenerid"][0]["references"])

    def test_annotation_refresh_preserves_reviews_and_adds_rows(self) -> None:
        catalog = {
            "entries": [
                {"id": "a", "inferred": {"phase_hint": "intro"}},
                {"id": "b", "inferred": {}},
            ]
        }
        existing = {
            "entries": {
                "a": {
                    "label": "Standing kiss",
                    "compatibility": "reusable",
                    "tags": ["kiss"],
                },
                "removed": {"label": "old"},
            }
        }
        value = sex_rid_catalog.starter_annotations(catalog, existing)
        self.assertEqual("Standing kiss", value["entries"]["a"]["label"])
        self.assertEqual("intro", value["entries"]["a"]["phase"])
        self.assertEqual("unreviewed", value["entries"]["b"]["compatibility"])
        self.assertNotIn("removed", value["entries"])

    def test_bespoke_annotation_seed_is_human_readable(self) -> None:
        rid_id = r"base\x\sex_judy_layout.scenerid"
        value = sex_rid_catalog.starter_annotations(
            {"entries": [{"id": rid_id, "inferred": {}}]}
        )
        row = value["entries"][rid_id]
        self.assertEqual("Judy — apartment sex sequence", row["label"])
        self.assertEqual("female V", row["player_role"])
        self.assertEqual("bespoke-only", row["compatibility"])

    def test_preview_manifest_has_stable_expected_paths(self) -> None:
        entry = sex_rid_catalog.inspect_rid(rid_document(), r"base\x.scenerid")
        manifest = sex_rid_catalog.preview_manifest({"entries": [entry]})
        self.assertEqual(
            "previews/base-x-scenerid.mp4", manifest["jobs"][0]["expected_video"]
        )
        self.assertEqual("decoder_required", manifest["jobs"][0]["status"])

    def test_resolve_preview_artifacts_marks_complete_media_ready(self) -> None:
        manifest = {
            "jobs": [
                {
                    "id": "base\\x.scenerid",
                    "expected_video": "previews/base-x-scenerid.mp4",
                    "expected_contact_sheet": "previews/base-x-scenerid.jpg",
                    "status": "decoder_required",
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            review_directory = Path(directory)
            preview_directory = review_directory / "previews"
            preview_directory.mkdir()
            (preview_directory / "base-x-scenerid.mp4").write_bytes(b"video")
            (preview_directory / "base-x-scenerid.jpg").write_bytes(b"image")
            (preview_directory / "base-x-scenerid.preview.json").write_text(
                json.dumps(
                    {
                        "actors": [
                            {"signature": "female_average"},
                            {"signature": "player"},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            resolved = sex_rid_catalog.resolve_preview_artifacts(
                manifest, review_directory
            )

        job = resolved["jobs"][0]
        self.assertEqual("ready", job["status"])
        self.assertEqual("previews/base-x-scenerid.mp4", job["video_url"])
        self.assertEqual(["female_average", "player"], job["rendered_actors"])
        self.assertEqual("decoder_required", manifest["jobs"][0]["status"])


if __name__ == "__main__":
    unittest.main()
