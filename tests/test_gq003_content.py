from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BUILD_PATH = ROOT / "quests/story/ghostline/gq003/implementation/build.py"
BUILD_SPEC = importlib.util.spec_from_file_location("generate_gq003_content", BUILD_PATH)
assert BUILD_SPEC and BUILD_SPEC.loader
generate_gq003_content = importlib.util.module_from_spec(BUILD_SPEC)
sys.modules["generate_gq003_content"] = generate_gq003_content
BUILD_SPEC.loader.exec_module(generate_gq003_content)

MANIFEST = ROOT / "quests/story/ghostline/gq003/implementation/quest.json"
JOURNAL = ROOT / "source/raw/mod/gq003/journal/gq003.journal.json"
ONSCREENS = ROOT / "source/raw/mod/gq003/localization/en-us/onscreens/gq003.json.json"
TWEAK = ROOT / "source/resources/r6/tweaks/ghostline/gq003_black_lantern.yaml"
MARA = ROOT / "characters/mara.character.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def walk(value: Any):
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def journal_entries(document: dict[str, Any], entry_type: str) -> list[dict[str, Any]]:
    return [
        value["Data"]
        for value in walk(document)
        if isinstance(value, dict)
        and "HandleId" in value
        and isinstance(value.get("Data"), dict)
        and value["Data"].get("$type") == entry_type
    ]


class Gq003ContentTests(unittest.TestCase):
    def test_generator_outputs_are_deterministic(self) -> None:
        self.assertEqual(generate_gq003_content.generate_journal(), load(JOURNAL))
        self.assertEqual(generate_gq003_content.generate_onscreens(), load(ONSCREENS))

    def test_manifest_objectives_and_mappins_exist_in_journal(self) -> None:
        manifest = load(MANIFEST)
        journal = load(JOURNAL)
        ids = {
            entry["id"]
            for entry in journal_entries(journal, "gameJournalQuestObjective")
        }
        mappin_ids = {
            entry["id"]
            for entry in journal_entries(journal, "gameJournalQuestMapPin")
        }
        for stage in manifest["stages"]:
            if stage.get("objective"):
                self.assertIn(stage["objective"].rsplit("/", 1)[-1], ids)
            paths = [stage.get("mappin"), *stage.get("route_mappins", [])]
            paths.extend(clue.get("mappin") for clue in stage.get("clues", []))
            for path in filter(None, paths):
                self.assertIn(path.rsplit("/", 1)[-1], mappin_ids)

    def test_phone_and_readable_content_is_authored(self) -> None:
        journal = load(JOURNAL)
        onscreens = load(ONSCREENS)
        keys = {
            entry["secondaryKey"]
            for entry in onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
        }
        conversations = journal_entries(journal, "gameJournalPhoneConversation")
        self.assertGreaterEqual(len(conversations), 6)
        onscreen_ids = {
            entry["id"] for entry in journal_entries(journal, "gameJournalOnscreen")
        }
        self.assertEqual(
            onscreen_ids,
            {
                "reconstruction_report",
                "expedited_handoff",
                "clinic_intake",
                "mara_maintenance_ticket",
                "courier_ledger",
            },
        )
        for key in generate_gq003_content.ITEM_COPY:
            self.assertIn(key, keys)

    def test_scene_dialogue_assets_cover_every_spoken_line(self) -> None:
        cases = (("gq003_02", 17), ("gq003_20", 14))
        for scene_id, expected in cases:
            with self.subTest(scene=scene_id):
                manifest = load(
                    ROOT / f"quests/story/ghostline/gq003/script/{scene_id}_manifest.json"
                )
                spoken = manifest["spoken_lines"]
                subtitle = load(
                    ROOT
                    / f"source/raw/mod/gq003/localization/en-us/subtitles/{scene_id}.json.json"
                )
                voice = load(
                    ROOT / f"source/raw/mod/gq003/localization/en-us/vo/{scene_id}.json.json"
                )
                self.assertEqual(len(spoken), expected)
                self.assertEqual(
                    len(subtitle["Data"]["RootChunk"]["root"]["Data"]["entries"]),
                    expected,
                )
                self.assertEqual(
                    len(voice["Data"]["RootChunk"]["root"]["Data"]["entries"]),
                    expected,
                )

    def test_item_and_reward_records_match_delivery_contract(self) -> None:
        tweak = TWEAK.read_text(encoding="utf-8")
        for record in (
            "Items.GhostlineBlackLanternRouteAuth:",
            "Items.GhostlineBlackLanternRouteBeacon:",
            "Items.GhostlineExpeditedHandoff:",
            "Items.GhostlineBlackLanternCipher:",
            "Items.GhostlineBlackLanternReceipt:",
            "QuestRewards.gq003_completion:",
            "Vehicle.GhostlineBlackLanternPatchVan:",
        ):
            self.assertIn(record, tweak)
        self.assertEqual(tweak.count("friendlyName: gq003_cipher_delivered"), 2)
        self.assertNotIn("Items.GhostlineBlackLanternPackage", tweak)

    def test_mara_manifest_matches_reviewed_concept_pass(self) -> None:
        mara = load(MARA)
        appearance = mara["appearance"]
        self.assertEqual(
            appearance["selections"],
            {
                "hair": "tutorial_judy_variant",
                "inner_torso": "tutorial_casual_tank",
                "outer_torso": "tutorial_business_outer",
                "business_extras": "none",
                "legs": "tutorial_casual_pants",
                "feet": "tutorial_casual_boots",
            },
        )
        self.assertEqual(
            {
                slot: override["mesh_appearance"]
                for slot, override in appearance["indexed_overrides"].items()
            },
            {
                "inner_torso": "white_black_dirt",
                "outer_torso": "leather",
                "legs": "military_dirty",
                "feet": "gray",
            },
        )


if __name__ == "__main__":
    unittest.main()
