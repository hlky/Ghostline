from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import build_lipsync_corpus as corpus


def path(value: str) -> dict:
    return {"DepotPath": {"$value": value}}


class LipsyncCorpusTests(unittest.TestCase):
    def test_groups_extractions_by_command_length_and_item_limit(self) -> None:
        paths = ["a" * 8, "b" * 8, "c" * 8, "d" * 8]

        by_length = corpus.extraction_chunks(paths, maximum_pattern_chars=25)
        by_count = corpus.extraction_chunks(paths, maximum_pattern_chars=1000, maximum_paths=3)

        self.assertEqual(by_length, [paths[:2], paths[2:]])
        self.assertEqual(by_count, [paths[:3], paths[3:]])

    def test_caches_unique_resources_with_parallel_workers(self) -> None:
        calls: list[str] = []

        def operation(value: str) -> Path:
            calls.append(value)
            return Path(value + ".cached")

        result = corpus.cache_resources(["a", "b", "a"], operation, 2, "test")

        self.assertEqual(sorted(calls), ["a", "b"])
        self.assertEqual(result, {"a": Path("a.cached"), "b": Path("b.cached")})

    def test_retries_transient_parallel_cache_failure_serially(self) -> None:
        attempts: dict[str, int] = {}

        def operation(value: str) -> Path:
            attempts[value] = attempts.get(value, 0) + 1
            if value == "flaky" and attempts[value] == 1:
                raise RuntimeError("transient")
            return Path(value + ".cached")

        result = corpus.cache_resources(["stable", "flaky"], operation, 2, "test")

        self.assertEqual(attempts, {"stable": 1, "flaky": 2})
        self.assertEqual(result["flaky"], Path("flaky.cached"))

    def test_expands_parallel_lipmap_rows(self) -> None:
        document = {
            "Data": {
                "RootChunk": {
                    "scenePaths": ["123"],
                    "sceneEntries": [
                        {
                            "actorVoiceTags": ["10", "20"],
                            "animSets": [path(r"base\a.anims"), path(r"base\b.anims")],
                        }
                    ],
                }
            }
        }
        self.assertEqual(
            corpus.lipmap_rows(document),
            [
                {"scene_hash": "123", "actor_voice_tag": "10", "animset_depot_path": r"base\a.anims"},
                {"scene_hash": "123", "actor_voice_tag": "20", "animset_depot_path": r"base\b.anims"},
            ],
        )

    def test_indexes_wrapped_subtitles_and_voiceovers(self) -> None:
        subtitle = {
            "Data": {
                "RootChunk": {
                    "root": {
                        "Data": {
                            "entries": [
                                {
                                    "stringId": "42",
                                    "femaleVariant": "Who is it?",
                                    "maleVariant": "",
                                }
                            ]
                        }
                    }
                }
            }
        }
        voiceover = {
            "Data": {
                "RootChunk": {
                    "root": {
                        "Data": {
                            "entries": [
                                {
                                    "stringId": "42",
                                    "femaleResPath": path(r"base\voice.wem"),
                                    "maleResPath": path(r"base\voice.wem"),
                                }
                            ]
                        }
                    }
                }
            }
        }
        subtitles = corpus.subtitle_index([(r"base\subtitles\scene.json", subtitle)])
        voices = corpus.voiceover_index([voiceover])
        self.assertEqual(subtitles["42"]["text"], "Who is it?")
        self.assertEqual(voices["42"]["audio_depot_path"], r"base\voice.wem")

    def test_prefers_quest_subtitle_when_scene_stems_collide(self) -> None:
        candidates = corpus.subtitle_candidates(
            r"base\lipsync\quest\mq010\scenes\mq010_02_barry_talk\barry.anims",
            [
                r"base\localization\en-us\subtitles\open_world\mq010_02_barry_talk.json",
                r"base\localization\en-us\subtitles\quest\mq010\mq010_02_barry_talk.json",
            ],
        )
        self.assertIn("\\subtitles\\quest\\", candidates[0])

    def test_clean_line_rejects_placeholders_and_duration_outliers(self) -> None:
        self.assertTrue(corpus.clean_line("Who is it?", 1.0, 0.35, 15.0))
        self.assertFalse(corpus.clean_line("LocKey#123", 1.0, 0.35, 15.0))
        self.assertFalse(corpus.clean_line('<mothertongue l="mex"/>', 1.0, 0.35, 15.0))
        self.assertFalse(corpus.clean_line("Hello", 20.0, 0.35, 15.0))


if __name__ == "__main__":
    unittest.main()
