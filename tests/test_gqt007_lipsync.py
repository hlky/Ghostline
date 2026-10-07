from __future__ import annotations

import importlib.util
import copy
import json
import sys
import unittest
from unittest import mock
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

SPEC = importlib.util.spec_from_file_location(
    "gqt007_build",
    ROOT / "projects/test-quests/gqt007/implementation/build.py",
)
assert SPEC is not None
gqt007 = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["gqt007_build"] = gqt007
SPEC.loader.exec_module(gqt007)


class Gqt007LipsyncTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec = gqt007.load(gqt007.SCENE_SPEC)
        cls.scene = gqt007.scene_builder.build_scene(cls.spec)
        cls.root = cls.scene["Data"]["RootChunk"]

    def test_scene_is_two_option_repeatable_ab_comparison(self) -> None:
        self.assertEqual(
            [
                option["locstringId"]["ruid"]
                for option in self.root["screenplayStore"]["options"]
            ],
            ["17000000000000000001", "17000000000000000002"],
        )
        choices = [
            node["Data"]
            for node in self.root["sceneGraph"]["Data"]["graph"]
            if node["Data"]["$type"] == "scnChoiceNode"
        ]
        self.assertEqual(len(choices), 1)
        self.assertEqual(len(choices[0]["options"]), 2)
        section_targets = {
            destination["nodeId"]["id"]
            for node in self.root["sceneGraph"]["Data"]["graph"]
            if node["Data"]["$type"] == "scnSectionNode"
            for socket in node["Data"]["outputSockets"][:1]
            for destination in socket["destinations"]
        }
        self.assertEqual(section_targets, {2})

    def test_both_lines_share_audio_but_select_different_clips(self) -> None:
        lines = self.root["screenplayStore"]["lines"]
        self.assertEqual(
            {line["locstringId"]["ruid"] for line in lines},
            {"9041139144898214479", "14094805234786396679"},
        )
        self.assertEqual(
            [line["femaleLipsyncAnimationName"]["$value"] for line in lines],
            ["f_7D78942678897A4F", "f_C39ACEAEFDC26A07"],
        )

    def test_scene_uses_custom_localized_animset_without_vanilla_override(self) -> None:
        reference = self.root["resouresReferences"]["lipsyncAnimSets"][0]
        self.assertEqual(
            reference["asyncRefLipsyncAnimSet"]["DepotPath"]["$value"],
            r"mod\gqt007\scenes\lipsync\en\gqt007_barry_lipsync\civ_low_m_11_enus_40_fat.anims",
        )
        self.assertTrue(gqt007.CUSTOM_ANIMSET.is_file())
        self.assertEqual(gqt007.CUSTOM_ANIMSET.read_bytes()[:4], b"CR2W")

    def test_world_spawns_vanilla_barry_with_his_voice_identity(self) -> None:
        world = gqt007.load(gqt007.WORLD_SPEC)
        self.assertEqual(
            world["community"]["character"],
            "Character.mq010_barry",
        )
        self.assertEqual(
            world["community"]["voice_tag"],
            "civ_low_m_11_enus_40_fat",
        )

    def test_lipmap_binds_mod_scene_to_localized_barry_animset(self) -> None:
        lipmap = gqt007.generate_lipmap()["Data"]["RootChunk"]
        self.assertEqual(
            lipmap["scenePaths"],
            [
                str(
                    gqt007.scene_builder.fnv1a64(
                        r"mod\gqt007\scenes\gqt007_barry_lipsync.scene"
                    )
                )
            ],
        )
        self.assertEqual(
            lipmap["sceneEntries"][0]["actorVoiceTags"],
            ["1624173162010260376"],
        )
        self.assertEqual(
            lipmap["sceneEntries"][0]["animSets"][0]["DepotPath"]["$value"],
            gqt007.CUSTOM_ANIMSET_DEPOT_PATH,
        )

    def test_audio_and_subtitles_are_self_contained(self) -> None:
        subtitles = gqt007.generate_subtitles()["Data"]["RootChunk"]["root"]["Data"][
            "entries"
        ]
        vomap = gqt007.generate_vomap()["Data"]["RootChunk"]["root"]["Data"]["entries"]
        line_ids = ["9041139144898214479", "14094805234786396679"]
        self.assertEqual([entry["stringId"] for entry in subtitles], line_ids)
        self.assertEqual([entry["stringId"] for entry in vomap], line_ids)
        self.assertEqual(
            [entry["femaleResPath"]["DepotPath"]["$value"] for entry in vomap],
            [r"mod\gqt007\localization\en-us\vo\barry_who_is_it.wem"] * 2,
        )
        self.assertTrue(all(path.is_file() for path in gqt007.wem_archive_paths()))

    def test_subtitles_and_audio_follow_authored_dialogue_changes(self) -> None:
        spoken, choices = gqt007.scene_builder.load_manifest(self.spec)
        changed = copy.deepcopy(spoken)
        line = changed["barry_vanilla"]
        line.update(
            text="A revised line.",
            string_id="123456789",
            audio_path=r"mod\test\revised.wem",
            male_audio_path=r"mod\test\revised_male.wem",
        )
        with mock.patch.object(
            gqt007.scene_builder, "load_manifest", return_value=(changed, choices)
        ):
            subtitles = gqt007.generate_subtitles()["Data"]["RootChunk"]["root"][
                "Data"
            ]["entries"]
            audio = gqt007.generate_vomap()["Data"]["RootChunk"]["root"]["Data"][
                "entries"
            ]
        self.assertEqual(subtitles[0]["stringId"], "123456789")
        self.assertEqual(subtitles[0]["femaleVariant"], "A revised line.")
        self.assertEqual(subtitles[0]["maleVariant"], "A revised line.")
        self.assertEqual(audio[0]["stringId"], "123456789")
        self.assertEqual(
            audio[0]["femaleResPath"]["DepotPath"]["$value"], r"mod\test\revised.wem"
        )
        self.assertEqual(
            audio[0]["maleResPath"]["DepotPath"]["$value"], r"mod\test\revised_male.wem"
        )
        self.assertEqual(
            subtitles[1]["stringId"], spoken["barry_modified"]["string_id"]
        )

    def test_lipmap_follows_authored_scene_and_actor_identity(self) -> None:
        changed = copy.deepcopy(self.spec)
        changed["archive_path"] = "projects/test-quests/gqt007/source/archive/mod/gqt007/scenes/revised.scene"
        next(actor for actor in changed["actors"] if actor["key"] == "barry")[
            "voicetag"
        ] = "987654321"
        with mock.patch.object(gqt007, "load", return_value=changed):
            lipmap = gqt007.generate_lipmap()["Data"]["RootChunk"]
        self.assertEqual(
            lipmap["scenePaths"],
            [str(gqt007.scene_builder.fnv1a64(r"mod\gqt007\scenes\revised.scene"))],
        )
        self.assertEqual(lipmap["sceneEntries"][0]["actorVoiceTags"], ["987654321"])

    def test_checked_in_raw_scene_matches_generator(self) -> None:
        raw = json.loads(
            (
                ROOT / "projects/test-quests/gqt007/source/raw/mod/gqt007/scenes/gqt007_barry_lipsync.scene.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(raw, self.scene)
        self.assertEqual(
            gqt007.scene_builder.validate_scene(raw, self.spec),
            [],
        )

    def test_archive_xl_registers_all_runtime_roots(self) -> None:
        config = yaml.safe_load(
            (ROOT / "projects/test-quests/gqt007/source/resources/Ghostline_GQT007.archive.xl").read_text(encoding="utf-8")
        )
        self.assertIn(
            {
                "path": r"mod\gqt007\phases\gqt007_barry_lipsync.questphase",
                "parent": r"base\quest\cyberpunk2077.quest",
            },
            config["quest"]["phases"],
        )
        self.assertIn(r"mod\gqt007\journal\gqt007.journal", config["journal"])
        self.assertIn(
            r"mod\gqt007\localization\en-us\onscreens\gqt007.json",
            config["localization"]["onscreens"]["en-us"],
        )
        self.assertIn(
            r"mod\gqt007\localization\en-us\gqt007.lipmap",
            config["localization"]["lipmaps"]["en-us"],
        )
        self.assertIn(
            r"mod\gqt007\localization\en-us\subtitles\gqt007_subtitles_map.json",
            config["localization"]["subtitles"]["en-us"],
        )
        self.assertIn(
            r"mod\gqt007\localization\en-us\vo\gqt007.json",
            config["localization"]["vomaps"]["en-us"],
        )
        self.assertIn(
            r"mod\gqt007\world\gqt007_barry_lipsync.streamingblock",
            config["streaming"]["blocks"],
        )


if __name__ == "__main__":
    unittest.main()
