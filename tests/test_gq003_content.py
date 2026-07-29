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
SCRIPT = ROOT / "quests/story/ghostline/gq003/script"
LOCALIZATION = ROOT / "source/raw/mod/gq003/localization/en-us"
VOICE_PRODUCTION = SCRIPT / "voice-production.json"
ARCHIVE_XL = ROOT / "source/resources/Ghostline.archive.xl"


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


def fnv1a64(value: str) -> int:
    result = 14695981039346656037
    for byte in value.encode("utf-8"):
        result ^= byte
        result = (result * 1099511628211) & 0xFFFFFFFFFFFFFFFF
    return result


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

    def test_dialogue_assets_cover_every_spoken_line(self) -> None:
        production = load(VOICE_PRODUCTION)
        indexed_files = {entry["file"] for entry in production["manifests"]}
        manifest_files = {path.name for path in SCRIPT.glob("gq003_*_manifest.json")}
        self.assertEqual(indexed_files, manifest_files)

        total = 0
        all_keys: set[str] = set()
        all_ids: set[str] = set()
        all_audio_paths: set[str] = set()
        for entry in production["manifests"]:
            dialogue_id = entry["id"]
            with self.subTest(dialogue=dialogue_id):
                manifest = load(SCRIPT / entry["file"])
                spoken = manifest["spoken_lines"]
                subtitle = load(
                    LOCALIZATION / f"subtitles/{dialogue_id}.json.json"
                )
                voice = load(
                    LOCALIZATION / f"vo/{dialogue_id}.json.json"
                )
                subtitle_map = load(
                    LOCALIZATION / f"subtitles/{dialogue_id}_subtitles_map.json.json"
                )
                self.assertEqual(len(spoken), entry["line_count"])
                self.assertEqual(
                    len(subtitle["Data"]["RootChunk"]["root"]["Data"]["entries"]),
                    len(spoken),
                )
                self.assertEqual(
                    len(voice["Data"]["RootChunk"]["root"]["Data"]["entries"]),
                    len(spoken),
                )
                self.assertEqual(
                    len(subtitle_map["Data"]["RootChunk"]["root"]["Data"]["entries"]),
                    1,
                )
                subtitle_entries = subtitle["Data"]["RootChunk"]["root"]["Data"]["entries"]
                voice_entries = voice["Data"]["RootChunk"]["root"]["Data"]["entries"]
                self.assertEqual(
                    [item["stringId"] for item in subtitle_entries],
                    [line["string_id"] for line in spoken],
                )
                self.assertEqual(
                    [item["femaleVariant"] for item in subtitle_entries],
                    [line["text"] for line in spoken],
                )
                self.assertEqual(
                    [
                        item["femaleResPath"]["DepotPath"]["$value"]
                        for item in voice_entries
                    ],
                    [line["audio_path"] for line in spoken],
                )
                self.assertEqual(
                    sorted({line["speaker"] for line in spoken}),
                    entry["speakers"],
                )
                for line in spoken:
                    self.assertEqual(line["string_id"], str(fnv1a64(line["key"])))
                    self.assertLessEqual(line["duration_ms"], 20_000)
                    self.assertTrue(line["audio_path"].endswith(f"{line['key']}.wem"))
                    self.assertNotIn(line["key"], all_keys)
                    self.assertNotIn(line["string_id"], all_ids)
                    self.assertNotIn(line["audio_path"], all_audio_paths)
                    all_keys.add(line["key"])
                    all_ids.add(line["string_id"])
                    all_audio_paths.add(line["audio_path"])
                total += len(spoken)

        self.assertEqual(total, production["spoken_line_count"])

    def test_dialogue_maps_are_registered_with_archivexl(self) -> None:
        production = load(VOICE_PRODUCTION)
        registration = ARCHIVE_XL.read_text(encoding="utf-8")
        for dialogue in production["manifests"]:
            dialogue_id = dialogue["id"]
            with self.subTest(dialogue=dialogue_id):
                self.assertIn(
                    rf"mod\gq003\localization\en-us\subtitles\{dialogue_id}_subtitles_map.json",
                    registration,
                )
                self.assertIn(
                    rf"mod\gq003\localization\en-us\vo\{dialogue_id}.json",
                    registration,
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
