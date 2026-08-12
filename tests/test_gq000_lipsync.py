from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from generate_scene import fnv1a64

SCENE_PATH = "mod\\gq000\\scenes\\gq000_patch_meet.scene"
LOGICAL_ANIMSET = (
    "mod\\gq000\\scenes\\lipsync\\en\\gq000_patch_meet\\"
    "civ_low_m_11_enus_40_fat.anims"
)
LOCALIZED_ANIMSET = (
    "base\\localization\\en-us\\lipsync\\mod\\gq000\\scenes\\"
    "gq000_patch_meet\\civ_low_m_11_enus_40_fat.anims"
)


class Gq000LipsyncTests(unittest.TestCase):
    def test_scene_lipmap_and_archive_xl_use_the_same_binding(self) -> None:
        scene = json.loads(
            (ROOT / "source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json").read_text(
                encoding="utf-8-sig"
            )
        )["Data"]["RootChunk"]
        lipmap = json.loads(
            (ROOT / "source/raw/mod/gq000/localization/en-us/gq000.lipmap.json").read_text(
                encoding="utf-8-sig"
            )
        )["Data"]["RootChunk"]
        voice_tag = scene["actors"][0]["voicetagId"]["id"]
        scene_animset = scene["resouresReferences"]["lipsyncAnimSets"][0][
            "asyncRefLipsyncAnimSet"
        ]["DepotPath"]["$value"]
        entries = dict(zip(lipmap["scenePaths"], lipmap["sceneEntries"]))
        entry = entries[str(fnv1a64(SCENE_PATH))]
        self.assertEqual(scene_animset, LOGICAL_ANIMSET)
        self.assertEqual(
            set(lipmap["scenePaths"]),
            {
                str(fnv1a64(SCENE_PATH)),
                str(fnv1a64(r"mod\gqt005\scenes\gqt005_patch_start.scene")),
            },
        )
        self.assertEqual(entry["actorVoiceTags"], [voice_tag])
        self.assertEqual(entry["animSets"][0]["DepotPath"]["$value"], LOCALIZED_ANIMSET)
        gqt005_entry = entries[
            str(fnv1a64(r"mod\gqt005\scenes\gqt005_patch_start.scene"))
        ]
        self.assertEqual(gqt005_entry["actorVoiceTags"], ["1624173162010260376"])
        self.assertEqual(
            gqt005_entry["animSets"][0]["DepotPath"]["$value"],
            LOCALIZED_ANIMSET,
        )
        archive_xl = (ROOT / "source/resources/Ghostline.archive.xl").read_text(
            encoding="utf-8"
        )
        self.assertIn("mod\\gq000\\localization\\en-us\\gq000.lipmap", archive_xl)

    def test_rebuilt_animset_is_present_as_cr2w(self) -> None:
        path = ROOT / "source/archive" / Path(LOCALIZED_ANIMSET.replace("\\", "/"))
        self.assertTrue(path.is_file())
        self.assertEqual(path.read_bytes()[:4], b"CR2W")


if __name__ == "__main__":
    unittest.main()
