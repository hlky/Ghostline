import json
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
JOURNAL = ROOT / "source/raw/mod/gq000/journal/gq000.journal.json"
ONSCREENS = ROOT / "source/raw/mod/gq000/localization/en-us/onscreens/gq000.json.json"
SHARD_TWEAKS = ROOT / "source/resources/r6/tweaks/ghostline/gq000_shards.yaml"
ROOT_PHASE = ROOT / "source/raw/mod/gq000/phases/gq000.questphase.json"


def walk_handles(value):
    if isinstance(value, dict):
        if "HandleId" in value:
            yield value
        for child in value.values():
            yield from walk_handles(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_handles(child)


def walk_journal_entries(value, path=()):
    if not isinstance(value, dict):
        return
    data = value.get("Data")
    if not isinstance(data, dict):
        return
    entry_id = data.get("id")
    next_path = path + ((entry_id,) if entry_id else ())
    yield "/".join(next_path), data
    for child in data.get("entries", []):
        yield from walk_journal_entries(child, next_path)


class QuestContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.journal = json.loads(JOURNAL.read_text(encoding="utf-8"))
        cls.onscreens = json.loads(ONSCREENS.read_text(encoding="utf-8"))
        cls.shard_tweaks = yaml.safe_load(SHARD_TWEAKS.read_text(encoding="utf-8"))
        cls.root_phase = json.loads(ROOT_PHASE.read_text(encoding="utf-8"))

    def test_journal_handle_ids_are_unique(self):
        handles = [item["HandleId"] for item in walk_handles(self.journal)]
        self.assertEqual(len(handles), len(set(handles)))

    def test_root_hands_the_cache_phase_to_the_delivery_phase(self):
        graph = self.root_phase["Data"]["RootChunk"]["graph"]["Data"]
        nodes = graph["nodes"]
        phase_paths = {
            node["Data"]["id"]: node["Data"]["phaseResource"]["DepotPath"]["$value"]
            for node in nodes
            if node["Data"]["$type"] == "questPhaseNodeDefinition"
        }
        self.assertEqual(
            "mod\\gq000\\phases\\gq000_post_accept.questphase", phase_paths[32]
        )
        self.assertEqual(
            "mod\\gq000\\phases\\gq000_delivery.questphase", phase_paths[33]
        )

        handles = {
            str(wrapper["HandleId"]): wrapper["Data"]
            for wrapper in walk_handles(self.root_phase)
        }

        def wrapper_id(wrapper):
            return str(wrapper.get("HandleId", wrapper.get("HandleRefId")))

        socket_owners = {}
        for node in nodes:
            for socket in node["Data"].get("sockets", []):
                socket_id = wrapper_id(socket)
                socket_owners[socket_id] = (
                    node["Data"]["id"],
                    handles[socket_id]["name"]["$value"],
                )

        edges = set()
        for data in handles.values():
            if data.get("$type") != "graphGraphConnectionDefinition":
                continue
            source = socket_owners[wrapper_id(data["source"])]
            destination = socket_owners[wrapper_id(data["destination"])]
            edges.add((*source, *destination))

        self.assertIn((32, "Out1", 33, "In1"), edges)
        self.assertIn((33, "Out1", 1, "In"), edges)

    def test_cache_shards_and_morrow_thread_are_authored(self):
        root = self.journal["Data"]["RootChunk"]["entry"]
        entries = dict(walk_journal_entries(root))
        expected = {
            "quests/minor_quest/gq000/gq000_02/gq000_02_obj_extract_cache",
            "quests/minor_quest/gq000/gq000_02/gq000_02_obj_extract_cache/gq000_02_qmp_extract_cache",
            "quests/minor_quest/gq000/gq000_02/gq000_02_obj_leave_area",
            "quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache",
            "quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache/gq000_03_desc_deliver_cache",
            "quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache/gq000_03_qmp_drop_point",
            "onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_01",
            "onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_02",
            "contacts/morrow/gq000_04_delivery/01_msg_cache_authenticated",
            "contacts/morrow/gq000_04_delivery/02_msg_route_found",
            "contacts/morrow/gq000_04_delivery/03_ch_delivery_response/03a_ch_pay_me",
            "contacts/morrow/gq000_04_delivery/03_ch_delivery_response/03b_ch_what_route",
            "contacts/morrow/gq000_04_delivery/04a_msg_pay_adjusted",
            "contacts/morrow/gq000_04_delivery/04b_msg_route_explained",
            "contacts/morrow/gq000_04_delivery/05_msg_more_work",
        }
        self.assertTrue(expected.issubset(entries))

    def test_extract_mappin_targets_the_access_point_interaction_slot(self):
        root = self.journal["Data"]["RootChunk"]["entry"]
        entries = dict(walk_journal_entries(root))
        path = (
            "quests/minor_quest/gq000/gq000_02/gq000_02_obj_extract_cache/"
            "gq000_02_qmp_extract_cache"
        )
        mappin = entries[path]
        self.assertEqual("gameJournalQuestMapPin", mappin["$type"])
        self.assertEqual("#gq000_02_ap_cache", mappin["reference"]["reference"]["$value"])
        self.assertEqual("UI_Interaction", mappin["slotName"]["$value"])
        self.assertEqual(1, mappin["enableGPS"])
        self.assertEqual(1, mappin["mappinData"]["visibleThroughWalls"])

    def test_delivery_mappin_targets_the_always_loaded_yellow_marker(self):
        root = self.journal["Data"]["RootChunk"]["entry"]
        entries = dict(walk_journal_entries(root))
        path = (
            "quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache/"
            "gq000_03_qmp_drop_point"
        )
        mappin = entries[path]
        self.assertEqual("gameJournalQuestMapPin", mappin["$type"])
        self.assertEqual(
            "#gq000_03_mp_drop_point",
            mappin["reference"]["reference"]["$value"],
        )
        self.assertEqual("UI_Interaction", mappin["slotName"]["$value"])
        self.assertEqual(
            {"$type": "Vector3", "X": 0, "Y": 0, "Z": 1},
            mappin["offset"],
        )
        self.assertEqual(1, mappin["enableGPS"])
        self.assertEqual(1, mappin["mappinData"]["active"])
        self.assertEqual("DefaultQuestVariant", mappin["mappinData"]["variant"])
        self.assertEqual(1, mappin["mappinData"]["visibleThroughWalls"])

    def test_new_journal_localization_keys_exist(self):
        entries = self.onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
        keys = {entry["secondaryKey"] for entry in entries}
        expected = {
            "gl_gq000_02_objective_extract_cache",
            "gl_gq000_02_description_extract_cache",
            "gl_gq000_02_objective_leave_area",
            "gl_gq000_02_description_leave_area",
            "gl_gq000_shard_quiet_spine_01_title",
            "gl_gq000_shard_quiet_spine_01_body",
            "gl_gq000_shard_quiet_spine_02_title",
            "gl_gq000_shard_quiet_spine_02_body",
            "gl_gq000_phone_morrow_name",
            "gl_gq000_phone_delivery_title",
            "gl_gq000_phone_morrow_cache_authenticated",
            "gl_gq000_phone_morrow_route_found",
            "gl_gq000_phone_choice_pay_me",
            "gl_gq000_phone_choice_what_route",
            "gl_gq000_phone_morrow_pay_adjusted",
            "gl_gq000_phone_morrow_route_explained",
            "gl_gq000_phone_morrow_more_work",
            "gl_gq000_03_objective_deliver_cache",
            "gl_gq000_03_description_deliver_cache",
            "gl_gq000_03_mappin_drop_point",
            "gl_gq000_item_datacache_name",
        }
        self.assertTrue(expected.issubset(keys))

    def test_readable_shard_items_point_at_the_journal_entries(self):
        expected = {
            "Items.GhostlineQuietSpine01": (
                "Items.GhostlineQuietSpine01_inline0",
                "onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_01",
            ),
            "Items.GhostlineQuietSpine02": (
                "Items.GhostlineQuietSpine02_inline0",
                "onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_02",
            ),
        }
        for item_id, (action_id, journal_path) in expected.items():
            item = self.shard_tweaks[item_id]
            action = self.shard_tweaks[action_id]
            self.assertEqual("Items.sts_wbr_jpn_01_shard_002", item["$base"])
            self.assertEqual(action_id, item["itemSecondaryAction"])
            self.assertEqual(
                "Items.sts_wbr_jpn_01_shard_002_inline0", action["$base"]
            )
            self.assertEqual(journal_path, action["journalEntry"])

        datacache = self.shard_tweaks["Items.gq000_datacache"]
        self.assertEqual("Items.sts_std_rcr_05_datachip", datacache["$base"])
        self.assertEqual("gq000_datacache", datacache["friendlyName"])
        self.assertEqual("gl_gq000_item_datacache_name", datacache["localizedName"])

        reward = self.shard_tweaks["QuestRewards.gq000_completion"]
        self.assertEqual("QuestRewards.sts_wat_kab_05_completion", reward["$base"])


if __name__ == "__main__":
    unittest.main()
