from __future__ import annotations

import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import quest_compiler

BUILD_PATH = ROOT / "quests/tests/gqt006/implementation/build.py"
BUILD_SPEC = importlib.util.spec_from_file_location(
    "generate_gqt006_content",
    BUILD_PATH,
)
assert BUILD_SPEC is not None and BUILD_SPEC.loader is not None
generate_gqt006_content = importlib.util.module_from_spec(BUILD_SPEC)
sys.modules["generate_gqt006_content"] = generate_gqt006_content
BUILD_SPEC.loader.exec_module(generate_gqt006_content)

MANIFEST = ROOT / "quests/tests/gqt006_goth_baddie_cyberpsycho.quest.json"
WORLD_SPEC = (
    ROOT / "quests/tests/gqt006/implementation/world/goth-baddie-cyberpsycho.world.json"
)
JOURNAL = ROOT / "source/raw/mod/gqt006/journal/gqt006.journal.json"
PHASES = ROOT / "source/raw/mod/gqt006/phases"
ARCHIVE_ROOT = ROOT / "source/archive/mod/gqt006"
GOTH_BADDIE_TWEAK = (
    ROOT / "source/resources/r6/tweaks/ghostline/character_goth_baddie.yaml"
)
QUEST_TWEAK = ROOT / "source/resources/r6/tweaks/ghostline/gqt006_goth_baddie.yaml"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def walk(value):
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def journal_entries(document: dict, entry_type: str) -> list[dict]:
    return [
        value["Data"]
        for value in walk(document)
        if isinstance(value, dict)
        and "HandleId" in value
        and isinstance(value.get("Data"), dict)
        and value["Data"].get("$type") == entry_type
    ]


def handle_map(document: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        value["HandleId"]: value
        for value in walk(document)
        if isinstance(value, dict) and "HandleId" in value
    }


def resolve(
    value: dict[str, Any],
    handles: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    if "HandleRefId" in value:
        return handles[value["HandleRefId"]]
    return value


def scalar(value: Any) -> Any:
    if isinstance(value, dict) and "$value" in value:
        return value["$value"]
    return value


def graph_edges(
    phase: dict[str, Any],
) -> set[tuple[int, str, int, str]]:
    handles = handle_map(phase)
    nodes = phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
    socket_owner: dict[str, tuple[int, str]] = {}
    for node in nodes:
        quest_id = node["Data"]["id"]
        for socket_value in node["Data"]["sockets"]:
            socket_handle = resolve(socket_value, handles)
            socket_owner[socket_handle["HandleId"]] = (
                quest_id,
                scalar(socket_handle["Data"]["name"]),
            )

    edges: set[tuple[int, str, int, str]] = set()
    for handle in handles.values():
        data = handle.get("Data", {})
        if data.get("$type") != "graphGraphConnectionDefinition":
            continue
        source = resolve(data["source"], handles)["HandleId"]
        destination = resolve(data["destination"], handles)["HandleId"]
        edges.add((*socket_owner[source], *socket_owner[destination]))
    return edges


def graph_node_with_type(
    phase: dict[str, Any],
    type_name: str,
) -> dict[str, Any]:
    matches = [
        node
        for node in phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
        if any(
            isinstance(value, dict) and value.get("$type") == type_name
            for value in walk(node)
        )
    ]
    if len(matches) != 1:
        raise AssertionError(
            f"Expected one graph node containing {type_name}, found {len(matches)}"
        )
    return matches[0]


class GothBaddieCyberpsychoContentTests(unittest.TestCase):
    def test_manifest_is_complete_and_ready(self) -> None:
        spec, diagnostics = quest_compiler.load_spec(MANIFEST)
        self.assertIsNotNone(
            spec,
            [diagnostic.as_dict() for diagnostic in diagnostics],
        )
        assert spec is not None
        self.assertEqual(
            [stage.type for stage in spec.stages],
            [
                "cyberpsycho_encounter",
                "acquire_item",
                "read_shard",
                "leave_area",
                "phone_conversation",
            ],
        )
        self.assertTrue(all(stage.status == "ready" for stage in spec.stages))
        self.assertFalse(
            [
                item
                for item in quest_compiler.audit_resources(spec)
                if item.level == "error"
            ]
        )

    def test_world_uses_selected_origin_and_inactive_community(self) -> None:
        world = load(WORLD_SPEC)
        self.assertEqual(
            world["origin"],
            {
                "x": -1026.8678,
                "y": 1279.5898,
                "z": 5.1301804,
                "yaw": 2.931411456,
            },
        )
        self.assertIn("origin selected", world["_note"])
        self.assertEqual(
            {marker["ref"] for marker in world["markers"]},
            {"#gqt006_mp_goth_baddie"},
        )
        self.assertTrue(
            all(
                item["position"]["from"] == "origin"
                for item in [*world["markers"], *world["triggers"]]
            )
        )
        self.assertEqual(
            {trigger["ref"] for trigger in world["triggers"]},
            {
                "#gqt006_tr_outer",
                "#gqt006_tr_reveal",
                "#gqt006_tr_arena",
                "#gqt006_tr_cleanup",
            },
        )
        community = world["community"]
        self.assertEqual(community["character"], "Character.GhostlineGothBaddie")
        self.assertEqual(community["appearance"], "ghostline_goth_baddie_default")
        self.assertEqual(community["active_on_start"], 0)
        self.assertEqual(community["spot"]["position"], {"from": "origin"})

        sector = load(
            ROOT / "source/raw/mod/gqt006/world/"
            "gqt006_goth_baddie_cyberpsycho.streamingsector.json"
        )
        placement = sector["Data"]["RootChunk"]["nodeData"]["Data"][4]
        self.assertEqual(
            placement["Position"],
            {
                "$type": "Vector4",
                "W": 0,
                "X": -1026.8678,
                "Y": 1279.5898,
                "Z": 5.1301804,
            },
        )
        orientation = placement["Orientation"]
        supplied = (0.0, 0.0, -0.025578603, -0.9996729)
        generated = (
            orientation["i"],
            orientation["j"],
            orientation["k"],
            orientation["r"],
        )
        dot = sum(
            left * right
            for left, right in zip(
                supplied,
                generated,
                strict=True,
            )
        )
        self.assertTrue(math.isclose(abs(dot), 1.0, abs_tol=1e-6))

    def test_world_contains_selected_location_alerted_patrol_route(self) -> None:
        sector = load(
            ROOT / "source/raw/mod/gqt006/world/"
            "gqt006_goth_baddie_cyberpsycho.streamingsector.json"
        )
        root = sector["Data"]["RootChunk"]
        expected_refs = [
            (
                "$/mod/gqt006/#gqt006_pr_goth_baddie_cyberpsycho/"
                "#gqt006_ws_goth_baddie_alerted_001"
            ),
            (
                "$/mod/gqt006/#gqt006_pr_goth_baddie_cyberpsycho/"
                "#gqt006_ws_goth_baddie_alerted_002"
            ),
            (
                "$/mod/gqt006/#gqt006_pr_goth_baddie_cyberpsycho/"
                "#gqt006_spl_goth_baddie_alerted"
            ),
        ]
        self.assertEqual(
            [scalar(value) for value in root["nodeRefs"][-3:]],
            expected_refs,
        )
        self.assertEqual(
            [entry["NodeIndex"] for entry in root["nodeData"]["Data"]],
            list(range(len(root["nodes"]))),
        )

        alerted_spots = root["nodes"][6:8]
        self.assertEqual(
            [value["Data"]["$type"] for value in alerted_spots],
            ["worldAISpotNode", "worldAISpotNode"],
        )
        for spot in alerted_spots:
            data = spot["Data"]
            self.assertEqual(data["isWorkspotInfinite"], 0)
            self.assertEqual(data["isWorkspotStatic"], 0)
            self.assertEqual(data["useCrowdBlacklist"], 0)
            self.assertEqual(data["useCrowdWhitelist"], 0)
            self.assertEqual(
                data["spot"]["Data"]["resource"]["DepotPath"]["$value"],
                (
                    "base\\workspots\\patrolling\\cyberpsycho\\"
                    "wa_unarmed_agitated_shuffle.workspot"
                ),
            )

        spline = root["nodes"][8]["Data"]
        self.assertEqual(spline["$type"], "worldPatrolSplineNode")
        self.assertEqual(spline["splineData"]["Data"]["looped"], 1)
        self.assertEqual(len(spline["splineData"]["Data"]["points"]), 4)
        self.assertEqual(
            [value["Data"]["node"]["$value"] for value in spline["patrolPointDefs"]],
            [
                "#gqt006_ws_goth_baddie_alerted_001",
                "#gqt006_ws_goth_baddie_alerted_002",
            ],
        )
        self.assertTrue(
            all(
                value["Data"]["pointType"] == "Workspot"
                for value in spline["patrolPointDefs"]
            )
        )

    def test_goth_baddie_owns_boss_hud_and_cyberpsycho_contract(self) -> None:
        tweak = GOTH_BADDIE_TWEAK.read_text(encoding="utf-8")
        for expected in (
            "Character.GhostlineGothBaddie:",
            "$base: Character.Quest_Combat_NPC_Base",
            "actionMap: MaxTacNetrunner.Map",
            "archetypeData: ArchetypeData.NetrunnerT3",
            "rarity: NPCRarity.Boss",
            "threatTrackingPreset: TargetTracking.DefaultPreset",
            "tags:",
            "- Cyberpsycho",
            "Character.Cyberpsycho",
            "Ability.HasDodge",
            "Ability.CanParry",
            "Ability.HasKerenzikov",
            "Ability.IsTier3Archetype",
            "Ability.HasMemoryWipeImmunity",
            "Character.AllowTechWeaponDodgeEffector",
            "Character.MaxTac_Mantis_ModGroup",
            "Character.Maxtac_miniboss_ModGroup",
        ):
            self.assertIn(expected, tweak)
        self.assertNotIn("Character.AllowAnyDirectionDodgeEffector", tweak)
        self.assertIn("Items.Preset_Katana_E3", tweak)
        self.assertIn("statModifiers:", tweak)

    def test_encounter_replicates_mower_combat_handoff(self) -> None:
        phase = load(PHASES / "gqt006_neutralize_goth_baddie.questphase.json")
        handles = handle_map(phase)
        gameplay = graph_node_with_type(
            phase,
            "questPuppetAIManagerNodeDefinition",
        )
        mortal = next(
            node
            for node in phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if any(
                isinstance(value, dict)
                and value.get("$type") == "questCharacterManagerParameters_SetMortality"
                and value.get("state") == "Mortal"
                for value in walk(node)
            )
        )
        delay = graph_node_with_type(
            phase,
            "questRealtimeDelay_ConditionType",
        )
        not_in_combat = graph_node_with_type(
            phase,
            "questCharacterCombat_ConditionType",
        )
        assign = graph_node_with_type(
            phase,
            "AIAssignRoleCommandParams",
        )
        target = graph_node_with_type(
            phase,
            "questCombatNodeParams_CombatTarget",
        )
        threat = graph_node_with_type(
            phase,
            "AIInjectCombatThreatCommandParams",
        )

        edges = graph_edges(phase)
        expected_edges = {
            (gameplay["Data"]["id"], "Out", mortal["Data"]["id"], "In"),
            (gameplay["Data"]["id"], "Out", delay["Data"]["id"], "In"),
            (delay["Data"]["id"], "Out", not_in_combat["Data"]["id"], "In"),
            (delay["Data"]["id"], "Out", target["Data"]["id"], "In"),
            (not_in_combat["Data"]["id"], "Out", assign["Data"]["id"], "In"),
            (target["Data"]["id"], "Success", threat["Data"]["id"], "In"),
        }
        self.assertTrue(expected_edges.issubset(edges))

        delay_condition = resolve(delay["Data"]["condition"], handles)["Data"]
        delay_type = resolve(delay_condition["type"], handles)["Data"]
        self.assertEqual(delay_type["miliseconds"], 200)

        combat_condition = resolve(
            not_in_combat["Data"]["condition"],
            handles,
        )["Data"]
        combat_type = resolve(combat_condition["type"], handles)["Data"]
        self.assertTrue(combat_type["inverted"])
        self.assertFalse(combat_type["isPlayer"])

        params = resolve(assign["Data"]["params"], handles)["Data"]
        self.assertEqual(params["$type"], "AIAssignRoleCommandParams")
        role = resolve(params["role"], handles)["Data"]
        self.assertEqual(role["$type"], "AIPatrolRole")
        self.assertTrue(role["forceAlerted"])
        path_params = resolve(role["pathParams"], handles)["Data"]
        alerted_path = resolve(role["alertedPathParams"], handles)["Data"]
        for value in (path_params, alerted_path):
            self.assertEqual(value["movementType"], "Sprint")
            self.assertTrue(value["patrolWithWeapon"])
        self.assertEqual(
            alerted_path["path"]["$value"],
            "#gqt006_spl_goth_baddie_alerted",
        )
        alerted_spots = resolve(role["alertedSpots"], handles)["Data"]
        self.assertEqual(
            [value["$value"] for value in alerted_spots["spots"]],
            [
                "#gqt006_ws_goth_baddie_alerted_001",
                "#gqt006_ws_goth_baddie_alerted_002",
            ],
        )

        target_params = resolve(target["Data"]["params"], handles)["Data"]
        threat_params = resolve(threat["Data"]["params"], handles)["Data"]
        self.assertEqual(target_params["duration"], 0.01)
        self.assertEqual(threat_params["duration"], 0.5)
        self.assertEqual(
            target_params["targetPuppet"]["reference"]["$value"],
            "#player",
        )
        self.assertEqual(
            threat_params["targetPuppetRef"]["reference"]["$value"],
            "#player",
        )

    def test_encounter_records_distinct_lethal_and_nonlethal_outcomes(self) -> None:
        phase = load(PHASES / "gqt006_neutralize_goth_baddie.questphase.json")
        encoded = json.dumps(phase)
        self.assertEqual(encoded.count("questCharacterKilled_ConditionType"), 2)
        self.assertIn("gqt006_goth_baddie_killed", encoded)
        self.assertIn("gqt006_goth_baddie_spared", encoded)
        self.assertIn("questCharacterManagerParameters_SetMortality", encoded)
        self.assertIn("questCombatNodeParams_CombatTarget", encoded)
        self.assertIn("AIInjectCombatThreatCommandParams", encoded)
        self.assertIn("questTriggerCondition", encoded)

    def test_journal_is_cyberpsycho_with_evidence_and_patch_debrief(self) -> None:
        journal = load(JOURNAL)
        quests = journal_entries(journal, "gameJournalQuest")
        self.assertEqual(len(quests), 1)
        self.assertEqual(quests[0]["id"], "gqt006")
        self.assertEqual(quests[0]["type"], "CyberPsycho")
        self.assertEqual(
            [
                entry["id"]
                for entry in journal_entries(
                    journal,
                    "gameJournalQuestPhase",
                )
            ],
            ["gqt006_01", "gqt006_02", "gqt006_03", "gqt006_04"],
        )
        conversations = journal_entries(
            journal,
            "gameJournalPhoneConversation",
        )
        self.assertEqual(
            [entry["id"] for entry in conversations],
            ["gqt006_04_report"],
        )
        self.assertEqual(
            [
                entry["id"]
                for entry in journal_entries(
                    journal,
                    "gameJournalOnscreen",
                )
            ],
            ["goth_baddie_datashard"],
        )

    def test_datashard_and_reward_records_are_quest_owned(self) -> None:
        tweak = QUEST_TWEAK.read_text(encoding="utf-8")
        self.assertIn("Items.GhostlineGothBaddieDatashard:", tweak)
        self.assertIn(
            "onscreens/emails/quests/minor_quest/gqt006/shards/goth_baddie_datashard",
            tweak,
        )
        self.assertIn("QuestRewards.gqt006_completion:", tweak)

    def test_generator_outputs_are_deterministic(self) -> None:
        self.assertEqual(
            generate_gqt006_content.generate_journal(),
            load(JOURNAL),
        )
        self.assertEqual(
            generate_gqt006_content.generate_onscreens(),
            load(generate_gqt006_content.ONSCREEN_RAW),
        )

    def test_selected_location_package_is_registered(self) -> None:
        registration = (ROOT / "source/resources/Ghostline.archive.xl").read_text(
            encoding="utf-8"
        )
        for expected in (
            r"mod\gqt006\phases\gqt006_goth_baddie_cyberpsycho.questphase",
            r"mod\gqt006\journal\gqt006.journal",
            r"mod\gqt006\localization\en-us\onscreens\gqt006.json",
            r"mod\gqt006\world\gqt006_goth_baddie_cyberpsycho.streamingblock",
        ):
            self.assertIn(expected, registration)

    def test_all_authored_cr2w_outputs_have_binary_headers(self) -> None:
        expected = [
            ARCHIVE_ROOT / "journal/gqt006.journal",
            ARCHIVE_ROOT / "localization/en-us/onscreens/gqt006.json",
            ARCHIVE_ROOT / "world/gqt006_goth_baddie_cyberpsycho.streamingsector",
            ARCHIVE_ROOT / "world/gqt006_always_loaded.streamingsector",
            ARCHIVE_ROOT / "world/gqt006_goth_baddie_cyberpsycho.streamingblock",
            ARCHIVE_ROOT / "phases/gqt006_goth_baddie_cyberpsycho.questphase",
            *[
                ARCHIVE_ROOT / f"phases/gqt006_{name}.questphase"
                for name in (
                    "neutralize_goth_baddie",
                    "recover_goth_baddie_shard",
                    "read_goth_baddie_shard",
                    "leave_goth_baddie_site",
                    "report_goth_baddie_outcome",
                )
            ],
            ROOT
            / "source/archive/mod/ghostline/characters/goth_baddie/goth_baddie.ent",
            ROOT
            / "source/archive/mod/ghostline/characters/goth_baddie/goth_baddie.app",
        ]
        for path in expected:
            with self.subTest(path=path):
                self.assertTrue(path.is_file())
                self.assertEqual(path.read_bytes()[:4], b"CR2W")


if __name__ == "__main__":
    unittest.main()
