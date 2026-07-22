from __future__ import annotations

import copy
import importlib.util
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
        self.assertEqual({outline["height"] for outline in outlines.values()}, {12})

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


if __name__ == "__main__":
    unittest.main()
