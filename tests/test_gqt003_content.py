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


def handle_definitions(value: Any) -> dict[str, dict[str, Any]]:
    definitions: dict[str, dict[str, Any]] = {}

    def visit(item: Any) -> None:
        if isinstance(item, dict):
            if "HandleId" in item and "Data" in item:
                definitions[item["HandleId"]] = item["Data"]
            for child in item.values():
                visit(child)
        elif isinstance(item, list):
            for child in item:
                visit(child)

    visit(value)
    return definitions


class ExtractAndHoldTests(unittest.TestCase):
    def test_manifest_has_the_expected_runtime_ready_flow(self) -> None:
        path = ROOT / "quests/tests/gqt003_extract_and_hold.quest.json"
        spec, diagnostics = quest_compiler.load_spec(path)

        self.assertFalse(
            [diagnostic for diagnostic in diagnostics if diagnostic.level == "error"]
        )
        assert spec is not None
        self.assertEqual(
            [stage.type for stage in spec.stages],
            [
                "reach_area",
                "release_or_rescue_npc",
                "escort_npc",
                "defend_target",
            ],
        )
        self.assertEqual([stage.status for stage in spec.stages], ["ready"] * 4)
        self.assertTrue(
            all(stage.data["inherit_phase_prefabs"] is False for stage in spec.stages)
        )
        self.assertEqual(spec.phase_prefabs, ("#gqt003_pr_extract_and_hold",))
        self.assertEqual(spec.debug_fact, "gqt003_debug_step")
        self.assertEqual(
            spec.stages[2].data["route_mappins"],
            [
                "quests/minor_quest/gqt003/gqt003_03/"
                "gqt003_03_obj_escort_patch/gqt003_03_qmp_escort_gate_01",
                "quests/minor_quest/gqt003/gqt003_03/"
                "gqt003_03_obj_escort_patch/gqt003_03_qmp_escort_gate_02",
                "quests/minor_quest/gqt003/gqt003_03/"
                "gqt003_03_obj_escort_patch/gqt003_03_qmp_escort_gate_03",
            ],
        )

    def test_escort_assigns_patch_as_player_follower_through_three_gates(
        self,
    ) -> None:
        phase = load(
            ROOT / "source/raw/mod/gqt003/phases/gqt003_escort_patch.questphase.json"
        )
        nodes = graph_nodes(phase)
        commands = [
            node["params"]["Data"]
            for node in nodes
            if node["$type"] == "questMiscAICommandNode"
        ]
        follower = next(
            command
            for command in commands
            if command["$type"] == "AIAssignRoleCommandParams"
        )
        self.assertEqual(follower["role"]["Data"]["$type"], "AIFollowerRole")
        self.assertEqual(
            follower["role"]["Data"]["followerRef"]["reference"]["$value"],
            "#player",
        )
        self.assertNotIn(
            "AIClearRoleCommandParams",
            {command["$type"] for command in commands},
        )
        gates = [
            node["condition"]["Data"]["triggerAreaRef"]["$value"]
            for node in nodes
            if node["$type"] == "questPauseConditionNodeDefinition"
        ]
        self.assertEqual(
            gates,
            [
                "#gqt003_03_tr_escort_gate_01",
                "#gqt003_03_tr_escort_gate_02",
                "#gqt003_03_tr_escort_gate_03",
            ],
        )
        mappins = [
            node
            for node in nodes
            if node["$type"] == "questMappinManagerNodeDefinition"
        ]
        self.assertEqual(len(mappins), 6)
        self.assertEqual(
            [node["path"]["Data"]["realPath"].rsplit("/", 1)[-1] for node in mappins],
            [
                "gqt003_03_qmp_escort_gate_01",
                "gqt003_03_qmp_escort_gate_01",
                "gqt003_03_qmp_escort_gate_02",
                "gqt003_03_qmp_escort_gate_02",
                "gqt003_03_qmp_escort_gate_03",
                "gqt003_03_qmp_escort_gate_03",
            ],
        )

    def test_timed_defend_has_success_failure_and_twenty_second_race(self) -> None:
        phase = load(
            ROOT / "source/raw/mod/gqt003/phases/gqt003_defend_patch.questphase.json"
        )
        nodes = graph_nodes(phase)
        delays = [
            node["condition"]["Data"]["type"]["Data"]["seconds"]
            for node in nodes
            if node["$type"] == "questPauseConditionNodeDefinition"
            and node["condition"]["Data"]["type"]["Data"]["$type"]
            == "questRealtimeDelay_ConditionType"
        ]
        self.assertEqual(delays, [20])
        facts = {
            node["type"]["Data"]["factName"]
            for node in nodes
            if node["$type"] == "questFactsDBManagerNodeDefinition"
        }
        self.assertEqual(
            facts,
            {"gqt003_hold_complete", "gqt003_completed", "gqt003_patch_lost"},
        )
        clear_roles = [
            node
            for node in nodes
            if node["$type"] == "questMiscAICommandNode"
            and node["params"]["Data"]["$type"] == "AIClearRoleCommandParams"
        ]
        self.assertEqual(len(clear_roles), 1)
        combat_nodes = [
            node for node in nodes if node["$type"] == "questCombatNodeDefinition"
        ]
        self.assertEqual(len(combat_nodes), 3)
        self.assertEqual(
            [node["entityReference"]["names"][0]["$value"] for node in combat_nodes],
            ["attacker_ranged_m", "attacker_ranged_f", "attacker_melee"],
        )
        self.assertEqual(
            [
                node["params"]["Data"]["targetPuppetRef"]["reference"]["$value"]
                for node in combat_nodes
            ],
            ["#gqt003_com_patch", "#gqt003_com_patch", "#player"],
        )
        handles = handle_definitions(phase)
        quest_states = [
            socket_data["name"]["$value"]
            for node in nodes
            if node["$type"] == "questJournalNodeDefinition"
            and node["type"]["Data"]["path"]["Data"]["realPath"]
            == "quests/minor_quest/gqt003"
            for socket in node["sockets"]
            for socket_data in [
                socket.get("Data") or handles.get(socket.get("HandleRefId", ""))
            ]
            if socket_data is not None
            and socket_data["name"]["$value"] in {"Succeeded", "Failed"}
            and socket_data["connections"]
        ]
        self.assertEqual(quest_states.count("Succeeded"), 1)
        self.assertEqual(quest_states.count("Failed"), 1)

    def test_world_keeps_patch_persistent_and_defines_four_authored_triggers(
        self,
    ) -> None:
        world = load(
            ROOT / "quests/tests/gqt003/implementation/world/"
            "extract-and-hold.world.json"
        )
        patch = world["communities"][0]
        self.assertEqual(patch["character"], "Character.GhostlinePatch")
        self.assertEqual(patch["always_spawned"], "true_")
        self.assertEqual(patch["spot"]["is_workspot_infinite"], 1)
        attackers = world["communities"][1]
        self.assertEqual(attackers["ref"], "#gqt003_04_com_attackers")
        self.assertEqual(attackers["active_on_start"], 0)
        self.assertEqual(
            [entry["entry"] for entry in attackers["entries"]],
            ["attacker_ranged_m", "attacker_ranged_f", "attacker_melee"],
        )
        self.assertEqual(len(world["triggers"]), 4)
        self.assertEqual(
            [marker["ref"] for marker in world["markers"]],
            [
                "#gqt003_01_mp_relay",
                "#gqt003_03_mp_gate_01",
                "#gqt003_03_mp_gate_02",
                "#gqt003_03_mp_gate_03",
            ],
        )
        self.assertTrue(
            all(trigger["outline"]["segments"] == 12 for trigger in world["triggers"])
        )
        escort_gates = world["triggers"][1:]
        self.assertEqual(
            [gate["position"]["z"] for gate in escort_gates],
            [1.24, 1.3, 1.433075],
        )
        self.assertTrue(all(gate["outline"]["height"] == 8 for gate in escort_gates))
        self.assertEqual(
            world["devices"][0]["controller_class"], "AccessPointControllerPS"
        )
        self.assertEqual(
            world["devices"][0]["position"],
            {"from": "origin", "right": 4, "up": 1.2},
        )

    def test_archive_xl_keeps_runtime_proven_gqt003_inactive(self) -> None:
        config = (ROOT / "source/resources/Ghostline.archive.xl").read_text(
            encoding="utf-8"
        )
        self.assertNotIn(r"mod\gqt003_extract_and_hold\phases", config)
        self.assertNotIn(r"mod\gqt003\world\gqt003_custom_devices.devices:", config)
        self.assertIn(
            r"mod\gqt005\phases\gqt005_braindance_analysis.questphase",
            config,
        )
        self.assertNotIn("gqt004", config)


if __name__ == "__main__":
    unittest.main()
