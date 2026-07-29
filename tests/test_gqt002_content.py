from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "quest_compiler", ROOT / "tools/quest_compiler.py"
)
assert SPEC and SPEC.loader
quest_compiler = importlib.util.module_from_spec(SPEC)
sys.modules["quest_compiler"] = quest_compiler
SPEC.loader.exec_module(quest_compiler)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def graph_nodes(document: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        wrapped["Data"]
        for wrapped in document["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
    ]


class QuietInstallTests(unittest.TestCase):
    def test_manifest_exercises_both_remaining_quiet_install_blocks(self) -> None:
        manifest = ROOT / "quests/tests/gqt002_quiet_install.quest.json"
        spec, diagnostics = quest_compiler.load_spec(manifest)
        self.assertFalse([item for item in diagnostics if item.level == "error"])
        assert spec is not None
        self.assertEqual(
            [stage.type for stage in spec.stages],
            ["stealth_monitor", "plant_item"],
        )
        self.assertEqual([stage.status for stage in spec.stages], ["ready", "ready"])
        self.assertEqual(spec.phase_prefabs, ("#gqt002_pr_quiet_install",))
        self.assertEqual(
            spec.stages[1].data["action"], "QuestForceDisconnectPersonalLink"
        )
        self.assertEqual(
            spec.stages[1].data["completion_function"],
            "IsPersonalLinkConnected",
        )
        self.assertEqual(
            spec.stages[1].data["controller_class"],
            "ScriptableDeviceComponentPS",
        )
        self.assertEqual(
            spec.stages[1].data["device"],
            "#gqt002_02_computer_target_r2",
        )

    def test_root_runs_detector_monitor_and_plant_in_parallel(self) -> None:
        phase = load(
            ROOT / "source/raw/mod/gqt002/phases/gqt002_quiet_install.questphase.json"
        )
        nodes = graph_nodes(phase)
        phase_paths = {
            node["phaseResource"]["DepotPath"]["$value"]
            for node in nodes
            if node["$type"] == "questPhaseNodeDefinition"
        }
        self.assertEqual(
            phase_paths,
            {
                r"mod\gqt002\phases\gqt002_detect_guards.questphase",
                r"mod\gqt002\phases\gqt002_remain_undetected.questphase",
                r"mod\gqt002\phases\gqt002_plant_keylogger.questphase",
            },
        )
        joins = [
            node for node in nodes if node["$type"] == "questLogicalAndNodeDefinition"
        ]
        self.assertEqual(len(joins), 1)
        self.assertEqual(joins[0]["inputSocketCount"], 3)
        self.assertEqual(
            phase["Data"]["RootChunk"]["phasePrefabs"][0]["prefabNodeRef"]["$value"],
            "#gqt002_pr_quiet_install",
        )
        attitudes = [
            node["type"]["Data"]["subtype"]["Data"]
            for node in nodes
            if node["$type"] == "questCharacterManagerNodeDefinition"
        ]
        self.assertEqual(
            [attitude["groupName"]["$value"] for attitude in attitudes],
            ["neutral", "hostile"] * 3,
        )
        self.assertEqual(
            [attitude["puppetRef"]["names"][0]["$value"] for attitude in attitudes],
            [
                "guard_ranged_m",
                "guard_ranged_m",
                "guard_ranged_f",
                "guard_ranged_f",
                "guard_melee",
                "guard_melee",
            ],
        )
        self.assertTrue(
            all(
                attitude["puppetRef"]["reference"]["$value"] == "#gqt002_01_com_guards"
                for attitude in attitudes
            )
        )

    def test_detector_uses_connected_security_system_combat_state(self) -> None:
        phase = load(
            ROOT / "source/raw/mod/gqt002/phases/gqt002_detect_guards.questphase.json"
        )
        nodes = graph_nodes(phase)
        conditions = [
            node["condition"]["Data"]["type"]["Data"]
            for node in nodes
            if node["$type"] == "questPauseConditionNodeDefinition"
            and isinstance(node["condition"]["Data"].get("type"), dict)
            and node["condition"]["Data"]["type"]["Data"].get("$type")
            == "questDevice_ConditionType"
        ]
        self.assertEqual(len(conditions), 1)
        self.assertEqual(
            conditions[0]["objectRef"]["$value"],
            "#gqt002_01_dvc_security_system",
        )
        self.assertEqual(
            conditions[0]["deviceControllerClass"]["$value"],
            "SecuritySystemControllerPS",
        )
        self.assertEqual(
            conditions[0]["deviceConditionFunction"]["$value"],
            "IsSystemInCombat",
        )

    def test_guarded_plant_uses_personal_link_and_progress_overlay(self) -> None:
        phase = load(
            ROOT / "source/raw/mod/gqt002/phases/gqt002_plant_keylogger.questphase.json"
        )
        nodes = graph_nodes(phase)
        self.assertFalse(
            [
                node
                for node in nodes
                if node["$type"] == "questPauseConditionNodeDefinition"
                and node["condition"]["Data"]["$type"] == "questTriggerCondition"
            ]
        )
        condition = next(
            node["condition"]["Data"]["type"]["Data"]
            for node in nodes
            if node["$type"] == "questPauseConditionNodeDefinition"
            and isinstance(node["condition"]["Data"].get("type"), dict)
            and node["condition"]["Data"]["type"]["Data"].get("$type")
            == "questDevice_ConditionType"
        )
        self.assertEqual(
            condition["deviceConditionFunction"]["$value"],
            "IsPersonalLinkConnected",
        )
        self.assertEqual(
            condition["deviceControllerClass"]["$value"],
            "ScriptableDeviceComponentPS",
        )
        self.assertEqual(
            condition["objectRef"]["$value"],
            "#gqt002_02_computer_target_r2",
        )
        progress = next(
            node["type"]["Data"]
            for node in nodes
            if node["$type"] == "questUIManagerNodeDefinition"
        )
        self.assertEqual(progress["$type"], "questProgressBar_NodeType")
        self.assertEqual(progress["duration"], 5.0)
        self.assertEqual(progress["text"]["value"], "gl_gqt002_installing_keylogger")
        self.assertEqual(progress["bottomText"]["value"], "gl_gqt002_do_not_disconnect")
        disconnect = next(
            node["type"]["Data"]["params"][0]["Data"]
            for node in nodes
            if node["$type"] == "questInteractiveObjectManagerNodeDefinition"
        )
        self.assertEqual(
            disconnect["deviceAction"]["$value"],
            "QuestForceDisconnectPersonalLink",
        )
        self.assertEqual(
            disconnect["deviceControllerClass"]["$value"],
            "ScriptableDeviceComponentPS",
        )
        serialized = json.dumps(phase)
        self.assertNotIn("InstallKeylogger", serialized)
        self.assertNotIn("IsKeyloggerInstalled", serialized)

    def test_world_uses_user_selected_vertical_layout(self) -> None:
        world = load(
            ROOT / "quests/tests/gqt002/implementation/world/quiet-install.world.json"
        )
        self.assertEqual(
            world["origin"],
            {
                "x": -1052.1395,
                "y": 1283.3362,
                "z": 12.46019,
                "yaw": -48.882914515,
            },
        )
        guards = world["communities"][0]
        self.assertEqual(guards["active_on_start"], 0)
        self.assertEqual(
            guards["position"],
            {"x": -1052.7932, "y": 1283.967, "z": 11.76162},
        )
        self.assertEqual(
            [entry["entry"] for entry in guards["entries"]],
            ["guard_ranged_m", "guard_ranged_f", "guard_melee"],
        )
        self.assertTrue(
            all(
                entry["spots"][0]["position"]["z"] < 5.15 for entry in guards["entries"]
            )
        )
        self.assertEqual(world["triggers"][0]["outline"]["radius"], 2.25)
        security = world["security"]
        self.assertEqual(security["type"], "DANGEROUS")
        self.assertEqual(security["position"], {"x": -1060.0, "y": 1287.0, "z": 5.5})
        self.assertEqual(security["outline"]["height"], 12.0)

    def test_generated_target_resources_share_barrel_placement(self) -> None:
        expected_position = {
            "X": -1052.1395,
            "Y": 1283.3362,
            "Z": 12.46019,
        }
        laptop = load(
            ROOT
            / "source/raw/mod/gqt002/world/gqt002_laptop_instance.streamingsector.json"
        )
        laptop_data = laptop["Data"]["RootChunk"]["nodeData"]["Data"][0]
        self.assertEqual(
            {axis: laptop_data["Position"][axis] for axis in ("X", "Y", "Z")},
            expected_position,
        )
        self.assertEqual(
            laptop_data["Orientation"],
            {
                "$type": "Quaternion",
                "i": 0.0,
                "j": 0.0,
                "k": -0.4137633,
                "r": 0.9103846,
            },
        )

        marker = load(
            ROOT
            / "source/raw/mod/gqt002/world/gqt002_always_loaded.streamingsector.json"
        )
        marker_position = marker["Data"]["RootChunk"]["nodeData"]["Data"][0]["Position"]
        self.assertEqual(
            {axis: marker_position[axis] for axis in ("X", "Y", "Z")},
            expected_position,
        )

        quest_sector = load(
            ROOT
            / "source/raw/mod/gqt002/world/gqt002_quiet_install.streamingsector.json"
        )
        trigger_position = quest_sector["Data"]["RootChunk"]["nodeData"]["Data"][0][
            "Position"
        ]
        self.assertEqual(
            {axis: trigger_position[axis] for axis in ("X", "Y", "Z")},
            {
                "X": expected_position["X"],
                "Y": expected_position["Y"],
                "Z": expected_position["Z"] - 1.5,
            },
        )

        registry = load(
            ROOT / "source/raw/mod/gqt002/world/gqt002_custom_devices.devices.json"
        )
        registry_position = registry["Data"]["RootChunk"]["data"]["Data"]["unk1"][0][
            "nodePosition"
        ]
        self.assertEqual(
            {axis: registry_position[axis] for axis in ("X", "Y", "Z")},
            expected_position,
        )

        controller_states = []
        for chunk in laptop["Data"]["RootChunk"]["nodes"][0]["Data"]["instanceData"][
            "Data"
        ]["buffer"]["Data"]["Chunks"]:
            persistent = chunk.get("persistentState", {}).get("Data", {})
            if persistent.get("$type") == "ComputerControllerPS":
                controller_states.append(persistent)
        self.assertTrue(controller_states)
        self.assertTrue(
            all(state["hasPersonalLinkSlot"] == 0 for state in controller_states)
        )
        self.assertTrue(
            all(
                state["personalLinkCustomInteraction"]["$value"]
                == "Interactions.StealData"
                for state in controller_states
            )
        )
        self.assertTrue(all(state["markAsQuest"] == 1 for state in controller_states))
        self.assertEqual(
            laptop_data["QuestPrefabRefHash"]["$value"],
            "$/mod/gqt002/#gqt002_pr_quiet_install/#gqt002_02_computer_target_r2",
        )

    def test_security_area_is_dangerous_and_connected_to_guard_community(self) -> None:
        sector = load(
            ROOT / "source/raw/mod/gqt002/world/gqt002_security.streamingsector.json"
        )
        root = sector["Data"]["RootChunk"]
        self.assertEqual(
            [node["Data"]["$type"] for node in root["nodes"]],
            ["worldDeviceNode", "worldDeviceNode"],
        )
        system, area = [node["Data"] for node in root["nodes"]]
        self.assertEqual(
            system["deviceConnections"][0]["deviceClassName"]["$value"],
            "SecurityAreaControllerPS",
        )
        self.assertEqual(
            system["deviceConnections"][0]["nodeRefs"][0]["$value"],
            "$/mod/gqt002/#gqt002_pr_quiet_install/#gqt002_01_dvc_security_area",
        )
        self.assertEqual(
            system["deviceConnections"][1]["deviceClassName"]["$value"],
            "CommunityProxyPS",
        )
        self.assertEqual(
            system["deviceConnections"][1]["nodeRefs"][0]["$value"],
            "$/mod/gqt002/#gqt002_pr_quiet_install/#gqt002_01_com_guards",
        )
        self.assertEqual(
            area["deviceConnections"][0]["deviceClassName"]["$value"],
            "CommunityProxyPS",
        )
        self.assertEqual(
            area["deviceConnections"][0]["nodeRefs"][0]["$value"],
            "$/mod/gqt002/#gqt002_pr_quiet_install/#gqt002_01_com_guards",
        )
        chunks = area["instanceData"]["Data"]["buffer"]["Data"]["Chunks"]
        trigger = next(
            chunk
            for chunk in chunks
            if chunk["$type"] == "gameStaticTriggerAreaComponent"
        )
        self.assertEqual(trigger["outline"]["Data"]["height"], 12.0)
        self.assertEqual(len(trigger["outline"]["Data"]["points"]), 4)
        persistent = next(
            chunk["persistentState"]["Data"]
            for chunk in chunks
            if chunk.get("persistentState", {}).get("Data", {}).get("$type")
            == "SecurityAreaControllerPS"
        )
        self.assertEqual(persistent["securityAreaType"], "DANGEROUS")

        block = load(
            ROOT
            / "source/raw/mod/gqt002/world/gqt002_quiet_install.streamingblock.json"
        )
        descriptors = block["Data"]["RootChunk"]["descriptors"]
        security_descriptor = next(
            item
            for item in descriptors
            if item["data"]["DepotPath"].get("$value")
            == r"mod\gqt002\world\gqt002_security.streamingsector"
        )
        self.assertEqual(
            security_descriptor["questPrefabNodeRef"]["$value"],
            "$/mod/gqt002/#gqt002_pr_quiet_install",
        )

        registry = load(
            ROOT / "source/raw/mod/gqt002/world/gqt002_custom_devices.devices.json"
        )
        self.assertEqual(
            {
                entry["className"]["$value"]
                for entry in registry["Data"]["RootChunk"]["data"]["Data"]["unk1"]
            },
            {
                "ComputerControllerPS",
                "SecurityAreaControllerPS",
                "SecuritySystemControllerPS",
            },
        )

    def test_archive_xl_keeps_gqt002_inactive_while_gqt005_is_active(self) -> None:
        config = (ROOT / "source/resources/Ghostline.archive.xl").read_text(
            encoding="utf-8"
        )
        self.assertNotIn(
            r"mod\gqt002\phases\gqt002_quiet_install.questphase",
            config,
        )
        self.assertNotIn(r"mod\gqt002\journal\gqt002.journal", config)
        self.assertNotIn(
            r"mod\gqt002\world\gqt002_quiet_install.streamingblock",
            config,
        )
        self.assertNotIn(
            r"mod\gqt002\world\gqt002_custom_devices.devices:",
            config,
        )
        self.assertIn(
            r"mod\gqt005\phases\gqt005_braindance_analysis.questphase",
            config,
        )
        self.assertIn(
            r"mod\gqt005\world\gqt005_braindance_analysis.streamingblock",
            config,
        )
        self.assertNotIn("gqt003_extract_and_hold", config)


if __name__ == "__main__":
    unittest.main()
