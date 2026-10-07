from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from generate_scene import fnv1a64
PLAYER_VOICETAG = "1103967280742240864"

QUESTS = {
    "gq001": {
        "scene": "gq001_iris_meet",
        "voice_tag": "13635884494759391413",
        "scene_hash": "17290731643441409860",
    },
    "gq002": {
        "scene": "gq002_cinder_meet",
        "voice_tag": "4805841566478315727",
        "scene_hash": "12748148790176160796",
    },
}


class StoryLipsyncTests(unittest.TestCase):
    def test_scene_voice_tags_match_the_installed_character_records(self) -> None:
        for quest, character, scene_name, owner in [
            ("gq000", "patch", "gq000_patch_meet", "projects/shared/ghostline-runtime"),
            ("gq001", "iris", "gq001_iris_meet", "projects/ghostline"),
            ("gq002", "cinder", "gq002_cinder_meet", "projects/ghostline"),
        ]:
            with self.subTest(character=character):
                records = yaml.safe_load((ROOT / owner / f"source/resources/r6/tweaks/ghostline/character_{character}.yaml").read_text(encoding="utf-8"))
                tag = records[f"Character.Ghostline{character.title()}"]["voiceTag"]
                scene = json.loads((ROOT / owner / f"source/raw/mod/{quest}/scenes/{scene_name}.scene.json").read_text(encoding="utf-8-sig"))["Data"]["RootChunk"]
                self.assertEqual(scene["actors"][0]["voicetagId"]["id"], str(fnv1a64(tag)))

    def test_scene_lipmap_and_archive_xl_bindings_match(self) -> None:
        archive_xl = (ROOT / "projects/ghostline/source/resources/Ghostline.archive.xl").read_text(
            encoding="utf-8"
        )
        for quest, values in QUESTS.items():
            with self.subTest(quest=quest):
                scene_name = values["scene"]
                basename = "civ_low_f_45_afam_30.anims"
                logical = (
                    f"mod\\{quest}\\scenes\\lipsync\\en\\{scene_name}\\{basename}"
                )
                localized = (
                    f"base\\localization\\en-us\\lipsync\\mod\\{quest}\\scenes\\"
                    f"{scene_name}\\{basename}"
                )
                scene = json.loads(
                    (ROOT / f"projects/ghostline/source/raw/mod/{quest}/scenes/{scene_name}.scene.json").read_text(
                        encoding="utf-8-sig"
                    )
                )["Data"]["RootChunk"]
                lipmap = json.loads(
                    (ROOT / f"projects/ghostline/source/raw/mod/{quest}/localization/en-us/{quest}.lipmap.json").read_text(
                        encoding="utf-8-sig"
                    )
                )["Data"]["RootChunk"]
                self.assertEqual(
                    scene["resouresReferences"]["lipsyncAnimSets"][0][
                        "asyncRefLipsyncAnimSet"
                    ]["DepotPath"]["$value"],
                    logical,
                )
                self.assertEqual(lipmap["scenePaths"], [values["scene_hash"]])
                self.assertEqual(
                    lipmap["sceneEntries"][0]["actorVoiceTags"],
                    [values["voice_tag"], PLAYER_VOICETAG],
                )
                self.assertEqual(
                    [item["DepotPath"]["$value"] for item in lipmap["sceneEntries"][0]["animSets"]],
                    [localized, localized],
                )
                self.assertEqual(
                    lipmap["sceneEntries"][0]["animSets"][0]["DepotPath"]["$value"],
                    localized,
                )
                self.assertIn(
                    f"mod\\{quest}\\localization\\en-us\\{quest}.lipmap", archive_xl
                )

    def test_localized_animsets_are_cr2w(self) -> None:
        for quest, values in QUESTS.items():
            with self.subTest(quest=quest):
                path = (
                    ROOT
                    / "projects/ghostline/source/archive/base/localization/en-us/lipsync/mod"
                    / quest
                    / "scenes"
                    / values["scene"]
                    / "civ_low_f_45_afam_30.anims"
                )
                self.assertTrue(path.is_file())
                self.assertEqual(path.read_bytes()[:4], b"CR2W")

    def test_every_spoken_line_selects_a_present_clip_for_both_voice_variants(self) -> None:
        cases = [
            ("gq000", "projects/shared/ghostline-runtime", "gq000_patch_meet", "gq000_01", "civ_low_m_11_enus_40_fat.anims"),
            ("gq001", "projects/ghostline", "gq001_iris_meet", "gq001_03", "civ_low_f_45_afam_30.anims"),
            ("gq002", "projects/ghostline", "gq002_cinder_meet", "gq002_01", "civ_low_f_45_afam_30.anims"),
        ]
        for quest, owner, scene_name, dialogue, basename in cases:
            with self.subTest(quest=quest):
                manifest = json.loads((ROOT / f"projects/ghostline/quests/{quest}/script/{dialogue}_manifest.json").read_text(encoding="utf-8"))
                scene = json.loads((ROOT / owner / f"source/raw/mod/{quest}/scenes/{scene_name}.scene.json").read_text(encoding="utf-8-sig"))["Data"]["RootChunk"]
                binary = (ROOT / owner / f"source/archive/base/localization/en-us/lipsync/mod/{quest}/scenes/{scene_name}/{basename}").read_bytes()
                scene_lines = {line["locstringId"]["ruid"]: line for line in scene["screenplayStore"]["lines"]}
                for line in manifest["spoken_lines"]:
                    clip = f"f_{int(line['string_id']):016X}"
                    self.assertIn(clip.encode("ascii") + b"\0", binary, line["key"])
                    for gender in ("female", "male"):
                        self.assertEqual(line[f"{gender}_lipsync_animation"], clip)
                        self.assertEqual(scene_lines[line["string_id"]][f"{gender}LipsyncAnimationName"]["$value"], clip)


if __name__ == "__main__":
    unittest.main()
