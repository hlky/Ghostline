from __future__ import annotations

import copy
import importlib.util
import math
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

SPEC = importlib.util.spec_from_file_location("generate_world", TOOLS / "generate_world.py")
assert SPEC is not None
generate_world = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["generate_world"] = generate_world
SPEC.loader.exec_module(generate_world)


class GenerateWorldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec = generate_world.load_json(TOOLS / "gq000_patch_meet.world.json")

    def build_production_world(self, spec: dict | None = None) -> tuple[dict, dict]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            generated = generate_world.build_world(
                spec or copy.deepcopy(self.spec),
                root / "raw",
                root / "archive",
            )
            paths = {item.kind: item.raw_path for item in generated}
            quest_sector = generate_world.load_json(paths["quest_sector"])
            always_loaded_sector = generate_world.load_json(paths["always_loaded_sector"])
        return quest_sector, always_loaded_sector

    def test_production_trigger_radii_keep_stable_bridge_baseline(self) -> None:
        outlines = {item["ref"]: item["outline"] for item in self.spec["triggers"]}

        self.assertEqual(outlines["#gq000_01_tr_setup"]["radius"], 90)
        self.assertEqual(outlines["#gq000_01_tr_engage"]["radius"], 10)
        self.assertEqual(outlines["#gq000_01_tr_bridge_case_mood"]["radius"], 60)
        self.assertEqual(outlines["#gq000_01_tr_someone_coming"]["radius"], 20)
        meeting_heights = {
            outline["height"] for ref, outline in outlines.items() if ref.startswith("#gq000_01_")
        }
        self.assertEqual(meeting_heights, {12})

    def test_registry_node_has_distinct_global_identity(self) -> None:
        quest_sector, always_loaded_sector = self.build_production_world()
        quest_root = quest_sector["Data"]["RootChunk"]
        always_root = always_loaded_sector["Data"]["RootChunk"]

        area_index = next(
            index
            for index, node in enumerate(quest_root["nodes"])
            if node["Data"]["$type"] == "worldCompiledCommunityAreaNode_Streamable"
        )
        registry_index = next(
            index
            for index, node in enumerate(always_root["nodes"])
            if node["Data"]["$type"] == "worldCommunityRegistryNode"
        )
        area = quest_root["nodes"][area_index]["Data"]
        registry = always_root["nodes"][registry_index]["Data"]
        area_node_id = quest_root["nodeData"]["Data"][area_index]["QuestPrefabRefHash"]["$value"]
        registry_node_ref = always_root["nodeData"]["Data"][registry_index]["QuestPrefabRefHash"]
        source_object_id = area["sourceObjectId"]["hash"]
        community_id = registry["communitiesData"][0]["communityId"]["entityId"]["hash"]
        area_spot_id = area["area"]["Data"]["entriesData"][0]["phasesData"][0]["timePeriodsData"][0]["spotNodeIds"][0]["hash"]
        registry_spot_id = registry["workspotsPersistentData"][0]["globalNodeId"]["hash"]

        self.assertEqual(area_node_id, "$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_com_patch_bridge")
        self.assertEqual(source_object_id, "7897875840529598144")
        self.assertEqual(community_id, source_object_id)
        self.assertEqual(area_spot_id, "3986972213571675071")
        self.assertEqual(registry_spot_id, area_spot_id)
        self.assertEqual(registry_node_ref["$storage"], "uint64")
        self.assertEqual(registry_node_ref["$value"], "7571954536596633334")
        self.assertNotEqual(registry_node_ref["$value"], source_object_id)

    def test_production_registry_spawns_the_custom_patch_record(self) -> None:
        _, always_loaded_sector = self.build_production_world()
        registry = next(
            node["Data"]
            for node in always_loaded_sector["Data"]["RootChunk"]["nodes"]
            if node["Data"]["$type"] == "worldCommunityRegistryNode"
        )
        character_record = registry["communitiesData"][0]["template"]["Data"]["entries"][0][
            "Data"
        ]["characterRecordId"]

        self.assertEqual(self.spec["community"]["character"], "Character.GhostlinePatch")
        self.assertEqual(character_record["$type"], "TweakDBID")
        self.assertEqual(character_record["$storage"], "string")
        self.assertEqual(character_record["$value"], "Character.GhostlinePatch")

        phase = registry["communitiesData"][0]["template"]["Data"]["entries"][0][
            "Data"
        ]["phases"][0]["Data"]
        appearances = [item["$value"] for item in phase["appearances"]]
        self.assertEqual(self.spec["community"]["appearance"], "ghostline_patch_default")
        self.assertEqual(appearances, ["ghostline_patch_default"])

    def test_registry_node_rejects_community_source_id_collision(self) -> None:
        spec = copy.deepcopy(self.spec)
        spec["community"]["registry_node_id"] = "7897875840529598144"

        with self.assertRaisesRegex(SystemExit, "must differ from community.source_object_id"):
            generate_world.build_world(spec, Path("unused-raw"), Path("unused-archive"), dry_run=True)

    def test_cache_access_point_is_a_unique_disabled_native_device(self) -> None:
        quest_sector, _ = self.build_production_world()
        root = quest_sector["Data"]["RootChunk"]
        devices = [
            (index, node["Data"])
            for index, node in enumerate(root["nodes"])
            if node["Data"]["$type"] == "worldDeviceNode"
        ]

        self.assertEqual(len(devices), 1)
        node_index, device = devices[0]
        self.assertEqual(device["appearanceName"]["$value"], "access_point_access_point_socket_f_neomil")
        self.assertEqual(
            device["entityTemplate"]["DepotPath"]["$value"],
            r"base\gameplay\devices\masters\access_points\accesspoint.ent",
        )
        access_point = device["instanceData"]["Data"]["buffer"]["Data"]["Chunks"][0]
        self.assertEqual(access_point["$type"], "AccessPoint")
        self.assertEqual(access_point["contentScale"]["$value"], "DeviceContentAssignment.Autoscaling")
        self.assertEqual(access_point["deviceState"], "OFF")

        placement = next(item for item in root["nodeData"]["Data"] if item["NodeIndex"] == node_index)
        full_ref = "$/mod/gq000/#gq000_pr_patch_meet/#gq000_02_ap_cache"
        self.assertEqual(placement["QuestPrefabRefHash"]["$value"], full_ref)
        self.assertIn(full_ref, [item["$value"] for item in root["nodeRefs"]])
        self.assertAlmostEqual(
            placement["Orientation"]["k"], math.sin(math.radians(178.6) / 2), places=6
        )
        self.assertAlmostEqual(
            placement["Orientation"]["r"], math.cos(math.radians(178.6) / 2), places=6
        )

    def test_cache_access_point_is_registered_for_quest_device_lookup(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            generated = generate_world.build_world(
                copy.deepcopy(self.spec),
                root / "raw",
                root / "archive",
            )
            registry_file = next(item for item in generated if item.kind == "device_registry")
            registry = generate_world.load_json(registry_file.raw_path)

        self.assertEqual(
            registry_file.depot_path,
            r"mod\gq000\world\gq000_custom_devices.devices",
        )
        root_chunk = registry["Data"]["RootChunk"]
        self.assertEqual(root_chunk["$type"], "gameDeviceResource")
        data = root_chunk["data"]
        self.assertNotIn("HandleId", data)
        registry_data = data["Data"]
        self.assertEqual(registry_data["$type"], "gameDeviceResourceData")
        self.assertEqual(registry_data["version"], 2)
        self.assertEqual(len(registry_data["unk1"]), 1)
        entry = registry_data["unk1"][0]
        self.assertEqual(entry["$type"], "gameDeviceResourceData_Cls1")
        self.assertEqual(entry["className"]["$value"], "AccessPointControllerPS")
        self.assertEqual(entry["hash"], "13482927561872837971")
        self.assertEqual(entry["nodePosition"]["X"], -1000.02)
        self.assertEqual(entry["nodePosition"]["Y"], 1497.2208)
        self.assertEqual(entry["nodePosition"]["Z"], 8.3)
        self.assertEqual(entry["parents"], [])
        self.assertEqual(entry["children"], [])

    def test_archive_xl_registration_includes_device_registry_patch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            archive_xl = Path(tmp) / "Ghostline.archive.xl"
            generate_world.register_archive_xl(
                archive_xl,
                r"mod\gq000\world\gq000_patch_meet.streamingblock",
                False,
                r"mod\gq000\world\gq000_custom_devices.devices",
            )
            import yaml

            data = yaml.safe_load(archive_xl.read_text(encoding="utf-8"))

        self.assertEqual(
            data["streaming"]["blocks"],
            [r"mod\gq000\world\gq000_patch_meet.streamingblock"],
        )
        self.assertEqual(
            data["resource"]["patch"][r"mod\gq000\world\gq000_custom_devices.devices"],
            [r"base\worlds\03_night_city\_compiled\default\03_night_city.devices"],
        )

    def test_device_instance_buffer_ids_must_be_nonzero_and_unique(self) -> None:
        zero = copy.deepcopy(self.spec)
        zero["devices"][0]["buffer_id"] = 0
        with self.assertRaisesRegex(SystemExit, "must not reuse sector buffer 0"):
            generate_world.build_world(zero, Path("unused-raw"), Path("unused-archive"), dry_run=True)

        duplicate = copy.deepcopy(self.spec)
        second = copy.deepcopy(duplicate["devices"][0])
        second["ref"] = "#gq000_02_ap_cache_probe"
        duplicate["devices"].append(second)
        with self.assertRaisesRegex(SystemExit, "must be unique within the sector"):
            generate_world.build_world(duplicate, Path("unused-raw"), Path("unused-archive"), dry_run=True)

    def test_cache_guard_registry_contains_three_varied_tyger_claws(self) -> None:
        quest_sector, always_loaded_sector = self.build_production_world()
        quest_root = quest_sector["Data"]["RootChunk"]
        always_root = always_loaded_sector["Data"]["RootChunk"]
        registry = next(
            node["Data"]
            for node in always_root["nodes"]
            if node["Data"]["$type"] == "worldCommunityRegistryNode"
            and node["Data"]["debugName"]["$value"] == "gq000_cache_guards_registry"
        )
        area = next(
            node["Data"]
            for node in quest_root["nodes"]
            if node["Data"]["$type"] == "worldCompiledCommunityAreaNode_Streamable"
            and node["Data"]["debugName"]["$value"] == "{gq000_02_com_cache_guards}"
        )

        item = registry["communitiesData"][0]
        entries = item["template"]["Data"]["entries"]
        characters = [entry["Data"]["characterRecordId"]["$value"] for entry in entries]
        self.assertEqual(
            characters,
            [
                "Character.jpn_tyger_claws_gangster2_ranged2_sidewinder_ma",
                "Character.jpn_tyger_claws_biker2_ranged2_copperhead_wa",
                "Character.jpn_tyger_claws_biker1_melee1_baseball_ma",
            ],
        )
        self.assertEqual(
            [state["entryActiveOnStart"] for state in item["entriesInitialState"]],
            [0, 0, 0],
        )
        self.assertEqual(len(registry["workspotsPersistentData"]), 4)
        self.assertEqual(len(area["area"]["Data"]["entriesData"]), 3)

        registry_periods = [
            entry["Data"]["phases"][0]["Data"]["timePeriods"][0]
            for entry in entries
        ]
        area_periods = [
            entry["phasesData"][0]["timePeriodsData"][0]
            for entry in area["area"]["Data"]["entriesData"]
        ]
        self.assertEqual([period["isSequence"] for period in registry_periods], [1, 0, 0])
        self.assertEqual([period["isSequence"] for period in area_periods], [1, 0, 0])
        self.assertEqual(
            [len(period["spotNodeRefs"]) for period in registry_periods],
            [2, 1, 1],
        )
        self.assertEqual(
            [len(period["spotNodeIds"]) for period in area_periods],
            [2, 1, 1],
        )

        cache_spots = [
            node["Data"]
            for node in quest_root["nodes"]
            if node["Data"]["$type"] == "worldAISpotNode"
            and node["Data"]["debugName"]["$value"].startswith("{gq000_02_spot_guard_")
        ]
        self.assertEqual(len(cache_spots), 4)
        patrol_spots = [
            spot for spot in cache_spots if spot["spot"]["Data"]["resource"]["DepotPath"]["$value"]
            == r"base\workspots\patrolling\guard_stand.workspot"
        ]
        self.assertEqual(len(patrol_spots), 2)
        self.assertEqual([spot["isWorkspotInfinite"] for spot in patrol_spots], [0, 0])

        area_index = next(
            index
            for index, node in enumerate(quest_root["nodes"])
            if node["Data"] is area
        )
        placement = quest_root["nodeData"]["Data"][area_index]
        self.assertAlmostEqual(placement["Position"]["X"], -1000.02, places=3)
        self.assertAlmostEqual(placement["Position"]["Y"], 1497.2208, places=3)
        self.assertAlmostEqual(placement["Position"]["Z"], 6.957, places=3)

        marker_x = -1000.02
        marker_y = 1497.2208
        for spot in self.spec["communities"][0]["entries"]:
            for placement_spec in spot["spots"]:
                position = placement_spec["position"]
                distance = math.hypot(
                    position["x"] - marker_x,
                    position["y"] - marker_y,
                )
                self.assertLessEqual(distance, 7.0)
                self.assertLess(position["x"], marker_x - 1.5)

    def test_cache_arrival_trigger_and_marker_use_cabinet_site(self) -> None:
        marker = next(item for item in self.spec["markers"] if item["ref"] == "#gq000_02_mp_cache")
        trigger = next(item for item in self.spec["triggers"] if item["ref"] == "#gq000_02_tr_cache_arrive")
        cleanup = next(item for item in self.spec["triggers"] if item["ref"] == "#gq000_02_tr_cache_cleanup")

        self.assertEqual(marker["position"], {"x": -1000.02, "y": 1497.2208, "z": 8.3})
        self.assertEqual(trigger["outline"]["radius"], 25)
        self.assertEqual(trigger["outline"]["height"], 12)
        self.assertEqual(cleanup["outline"]["radius"], 75)
        self.assertEqual(cleanup["outline"]["height"], 16)

    def test_delivery_marker_uses_live_confirmed_drop_point_009_site(self) -> None:
        marker = next(
            item
            for item in self.spec["markers"]
            if item["ref"] == "#gq000_03_mp_drop_point"
        )
        self.assertEqual(marker["sector"], "always_loaded")
        self.assertEqual(
            marker["position"],
            {"x": -1168.66333, "y": 1309.51709, "z": 19.9768238},
        )
        self.assertEqual(marker["yaw"], 175)

        _, always_loaded_sector = self.build_production_world()
        root = always_loaded_sector["Data"]["RootChunk"]
        full_ref = "$/mod/gq000/#gq000_pr_patch_meet/#gq000_03_mp_drop_point"
        placement = next(
            item
            for item in root["nodeData"]["Data"]
            if item["QuestPrefabRefHash"]["$value"] == full_ref
        )
        node = root["nodes"][placement["NodeIndex"]]["Data"]

        self.assertEqual(node["$type"], "worldStaticMarkerNode")
        self.assertEqual(placement["Position"]["X"], -1168.66333)
        self.assertEqual(placement["Position"]["Y"], 1309.51709)
        self.assertEqual(placement["Position"]["Z"], 19.9768238)


if __name__ == "__main__":
    unittest.main()
