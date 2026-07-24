import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def strings(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from strings(child)
    elif isinstance(value, str):
        yield value


class Gq002ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quest = load("source/quests/gq002.quest.json")
        cls.dialogue = load("source/raw/gq002_01_manifest.json")
        cls.selection = load("source/raw/gq002_01_voice_selection.json")
        cls.world = load("tools/gq002_machine_stops.world.json")

    def test_typed_stage_sequence_is_shipping_ready(self):
        self.assertEqual("The Machine Stops", self.quest["title"])
        self.assertEqual(
            [
                "phone_job_offer",
                "meet_contact",
                "reach_area",
                "investigate_clues",
                "read_shard",
                "reach_area",
                "combat_encounter",
                "phone_conversation",
                "choice_gate",
                "interact_device",
                "leave_area",
                "phone_conversation",
            ],
            [stage["type"] for stage in self.quest["stages"]],
        )
        self.assertTrue(all(stage["status"] == "ready" for stage in self.quest["stages"]))

    def test_shard_handoff_routes_back_to_relay_before_combat(self):
        return_stage = next(
            stage for stage in self.quest["stages"]
            if stage["id"] == "return_to_relay"
        )
        combat_stage = next(
            stage for stage in self.quest["stages"]
            if stage["id"] == "relay_security"
        )
        self.assertEqual("#gq002_05_tr_security", return_stage["trigger"])
        self.assertEqual(
            "quests/minor_quest/gq002/gq002_04b/"
            "gq002_04b_obj_return_relay/gq002_04b_qmp_relay",
            return_stage["mappin"],
        )
        self.assertNotIn("trigger", combat_stage)

    def test_final_relay_observes_native_hack_without_retriggering_device(self):
        operate = next(
            stage for stage in self.quest["stages"]
            if stage["id"] == "operate_relay"
        )
        self.assertFalse(operate["send_action"])
        phase = load(
            "source/raw/mod/gq002/phases/gq002_operate_relay.questphase.json"
        )
        encoded = json.dumps(phase)
        self.assertIn("WasHackingMinigameSucceeded", encoded)
        self.assertNotIn("questDeviceManagerNodeDefinition", encoded)
        self.assertNotIn("ToggleON", encoded)

    def test_debrief_tracks_response_and_grants_completion_reward(self):
        debrief = next(
            stage for stage in self.quest["stages"]
            if stage["id"] == "cinder_debrief"
        )
        self.assertEqual(
            "quests/minor_quest/gq002/gq002_08/gq002_08_obj_respond_cinder",
            debrief["objective"],
        )
        self.assertEqual("QuestRewards.gq002_completion", debrief["reward"])
        phase = load(
            "source/raw/mod/gq002/phases/gq002_cinder_debrief.questphase.json"
        )
        encoded = json.dumps(phase)
        self.assertIn("questRewardManagerNodeDefinition", encoded)
        self.assertIn("QuestRewards.gq002_completion", encoded)
        tweaks = (
            ROOT / "source/resources/r6/tweaks/ghostline/gq000_shards.yaml"
        ).read_text(encoding="utf-8")
        self.assertIn("QuestRewards.gq002_completion:", tweaks)

    def test_investigation_has_three_distinct_required_clues(self):
        stage = next(stage for stage in self.quest["stages"] if stage["id"] == "investigate_relay")
        self.assertEqual(3, stage["required_count"])
        self.assertEqual(3, len(stage["clues"]))
        self.assertEqual(3, len({clue["object_ref"] for clue in stage["clues"]}))
        self.assertTrue(all(clue.get("completion_fact") for clue in stage["clues"]))
        self.assertTrue(all("journal_entry" not in clue for clue in stage["clues"]))

    def test_shard_notification_and_quest_completion_are_explicit(self):
        shard = next(
            stage for stage in self.quest["stages"]
            if stage["id"] == "read_hostage_circuit"
        )
        debrief = next(
            stage for stage in self.quest["stages"]
            if stage["id"] == "cinder_debrief"
        )
        self.assertEqual("Items.GhostlineHostageCircuit", shard["item"])
        self.assertEqual(1, shard["file_entry_index"])
        self.assertTrue(all(clue.get("mappin") for clue in next(
            stage for stage in self.quest["stages"]
            if stage["id"] == "investigate_relay"
        )["clues"]))
        final_clue = next(
            stage for stage in self.quest["stages"]
            if stage["id"] == "investigate_relay"
        )["clues"][-1]
        self.assertEqual(
            "Items.GhostlineHostageCircuit", final_clue["grant_item"]
        )
        self.assertEqual("quests/minor_quest/gq002", debrief["complete_quest"])

        read_phase = load(
            "source/raw/mod/gq002/phases/"
            "gq002_read_hostage_circuit.questphase.json"
        )
        encoded = json.dumps(read_phase)
        self.assertIn("questFactsDBCondition", encoded)
        self.assertIn("gq002_clue_invoice_scanned", encoded)
        self.assertIn("questRealtimeDelay_ConditionType", encoded)
        self.assertNotIn("questInventory_ConditionType", encoded)
        self.assertNotIn("questJournalEntryVisited_ConditionType", encoded)

    def test_medical_relay_pin_uses_the_native_device_reference(self):
        journal = load("source/raw/mod/gq002/journal/gq002.journal.json")
        encoded = json.dumps(journal)
        self.assertIn(
            "$/03_night_city/c_watson/kabuki/"
            "loc_ma_wat_kab_15_prefab7XOZ7NY/"
            "loc_ma_wat_kab_15_gameplay_prefabLA72KZQ/"
            "loc_ma_wat_kab_15_devices_prefabLCOBNEQ/"
            "ma_wat_kab_15_access_point_001",
            encoded,
        )
        medical = next(
            entry["Data"]
            for entry in journal["Data"]["RootChunk"]["entry"]["Data"]["entries"][0]["Data"]["entries"][0]["Data"]["entries"][0]["Data"]["entries"][2]["Data"]["entries"][0]["Data"]["entries"]
            if entry["Data"].get("id") == "gq002_03_qmp_medical"
        )
        self.assertEqual(0, medical["enableGPS"])

    def test_destroy_and_spoof_facts_reach_outcome_debrief(self):
        decision = next(stage for stage in self.quest["stages"] if stage["id"] == "relay_decision")
        gate = next(stage for stage in self.quest["stages"] if stage["id"] == "relay_choice")
        debrief = next(stage for stage in self.quest["stages"] if stage["id"] == "cinder_debrief")
        decision_facts = {choice["set_fact"] for choice in decision["choices"]}
        self.assertEqual(
            {"gq002_scene_choice_destroy", "gq002_scene_choice_spoof"},
            decision_facts,
        )
        self.assertEqual(decision_facts, {branch["condition"] for branch in gate["branches"]})
        outcome_facts = {branch["set_fact"] for branch in gate["branches"]}
        self.assertEqual(outcome_facts, {branch["condition"] for branch in debrief["opening_branches"]})
        self.assertEqual("gq002_completed", debrief["completion_fact"])

    def test_selected_audio_exactly_covers_spoken_manifest(self):
        manifest = {line["key"]: line for line in self.dialogue["spoken_lines"]}
        receipt = {line["key"]: line for line in self.selection["lines"]}
        self.assertEqual(set(manifest), set(receipt))
        self.assertEqual(11, len(manifest))
        self.assertEqual("cinder-a-grounded-medic", self.selection["voice_design"])
        for key, line in manifest.items():
            selected = receipt[key]
            self.assertEqual(line["speaker"], selected["speaker"])
            self.assertEqual(line["duration_ms"], selected["duration_ms"])
            if line["speaker"] == "Cinder":
                self.assertEqual(self.selection["voice_design"], selected["design"])
            else:
                self.assertEqual("v-original-embed", selected["design"])

    def test_every_spoken_line_has_nonempty_wem(self):
        for line in self.dialogue["spoken_lines"]:
            relative = line["audio_path"].replace("\\", "/")
            wem = ROOT / "source/archive" / relative
            self.assertTrue(wem.is_file(), line["key"])
            self.assertGreater(wem.stat().st_size, 0, line["key"])

    def test_journal_gq002_loc_keys_are_covered(self):
        journal = load("source/raw/mod/gq002/journal/gq002.journal.json")
        onscreen = load(
            "source/raw/mod/gq002/localization/en-us/onscreens/gq002.json.json"
        )
        required = {value for value in strings(journal) if value.startswith("gl_gq002_")}
        available = {
            entry["secondaryKey"]
            for entry in onscreen["Data"]["RootChunk"]["root"]["Data"]["entries"]
        }
        self.assertTrue(required)
        self.assertEqual(set(), required - available)

    def test_archive_xl_registers_every_gq002_root_resource(self):
        archive_xl = (ROOT / "source/resources/Ghostline.archive.xl").read_text(
            encoding="utf-8"
        )
        for depot_path in (
            r"mod\gq002\phases\gq002.questphase",
            r"mod\gq002\journal\gq002.journal",
            r"mod\gq002\localization\en-us\onscreens\gq002.json",
            r"mod\gq002\localization\en-us\subtitles\gq002_01_subtitles_map.json",
            r"mod\gq002\localization\en-us\vo\gq002_01.json",
            r"mod\gq002\world\gq002_machine_stops.streamingblock",
        ):
            self.assertIn(depot_path, archive_xl)
            self.assertTrue((ROOT / "source/archive" / depot_path).exists())

    def test_cinder_resources_and_trigger_radius_are_authored(self):
        for relative in (
            "source/characters/cinder.character.json",
            "source/archive/mod/ghostline/characters/cinder/cinder.ent",
            "source/resources/r6/tweaks/ghostline/character_cinder.yaml",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)
        engage = next(
            trigger
            for trigger in self.world["triggers"]
            if trigger["ref"] == "#gq002_01_tr_engage"
        )
        self.assertEqual(3, engage["outline"]["radius"])

    def test_security_trigger_is_centered_on_relay_walking_plane(self):
        security_trigger = next(
            trigger
            for trigger in self.world["triggers"]
            if trigger["ref"] == "#gq002_05_tr_security"
        )
        self.assertEqual(
            {"from": "#gq002_02_mp_relay"},
            security_trigger["position"],
        )
        self.assertGreaterEqual(security_trigger["outline"]["height"], 10)

    def test_melee_security_spot_is_moved_onto_open_relay_floor(self):
        community = self.world["communities"][0]
        melee = next(
            entry for entry in community["entries"]
            if entry["entry"] == "security_melee"
        )
        self.assertEqual(
            {"x": -1108.2, "y": 1453.6, "z": 16.36},
            melee["spots"][0]["position"],
        )


if __name__ == "__main__":
    unittest.main()
