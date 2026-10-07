from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

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
                    [values["voice_tag"]],
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


if __name__ == "__main__":
    unittest.main()
