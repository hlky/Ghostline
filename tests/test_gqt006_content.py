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

BUILD_PATH = ROOT / "projects/test-quests/gqt006/implementation/build.py"
BUILD_SPEC = importlib.util.spec_from_file_location(
    "generate_gqt006_content",
    BUILD_PATH,
)
assert BUILD_SPEC is not None and BUILD_SPEC.loader is not None
generate_gqt006_content = importlib.util.module_from_spec(BUILD_SPEC)
sys.modules["generate_gqt006_content"] = generate_gqt006_content
BUILD_SPEC.loader.exec_module(generate_gqt006_content)

MANIFEST = ROOT / "projects/test-quests/gqt006/gqt006_goth_baddie_cyberpsycho.quest.json"
WORLD_SPEC = (
    ROOT / "projects/test-quests/gqt006/implementation/world/goth-baddie-cyberpsycho.world.json"
)
JOURNAL = ROOT / "projects/test-quests/gqt006/source/raw/mod/gqt006/journal/gqt006.journal.json"
PHASES = ROOT / "projects/test-quests/gqt006/source/raw/mod/gqt006/phases"
SCENE = ROOT / "projects/test-quests/gqt006/source/raw/mod/gqt006/scenes/gqt006_goth_baddie.scene.json"
ARCHIVE_ROOT = ROOT / "projects/test-quests/gqt006/source/archive/mod/gqt006"
GOTH_BADDIE_TWEAK = (
    ROOT / "projects/test-quests/gqt006/source/resources/r6/tweaks/ghostline/character_goth_baddie.yaml"
)
QUEST_TWEAK = ROOT / "projects/test-quests/gqt006/source/resources/r6/tweaks/ghostline/gqt006_goth_baddie.yaml"


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
                "meet_contact",
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
            {
                "#gqt006_mp_goth_baddie", "#gqt006_sm_intimacy",
                "#gqt006_sm_lose_goth", "#gqt006_sm_lose_v",
                "#gqt006_sm_aftermath_goth", "#gqt006_sm_aftermath_v",
            },
        )
        self.assertTrue(
            all(
                item["position"]["from"] == "origin"
                for item in [*world["markers"][:2], *world["triggers"]]
            )
        )
        self.assertEqual(
            {trigger["ref"] for trigger in world["triggers"]},
            {
                "#gqt006_tr_dialogue",
                "#gqt006_tr_outer",
                "#gqt006_tr_reveal",
                "#gqt006_tr_arena",
                "#gqt006_tr_cleanup",
            },
        )
        self.assertEqual(
            {marker["position"]["from"] for marker in world["markers"][2:]},
            {"#gqt006_sm_intimacy"},
        )
        community = world["community"]
        self.assertEqual(community["character"], "Character.GhostlineGothBaddie")
        self.assertEqual(community["appearance"], "ghostline_goth_baddie_default")
        self.assertEqual(community["active_on_start"], 0)
        self.assertEqual(community["spot"]["position"], {"from": "origin"})
        dialogue_trigger = next(
            trigger
            for trigger in world["triggers"]
            if trigger["ref"] == "#gqt006_tr_dialogue"
        )
        self.assertEqual(dialogue_trigger["outline"]["radius"], 5)

        sector = load(
            ROOT / "projects/test-quests/gqt006/source/raw/mod/gqt006/world/"
            "gqt006_goth_baddie_cyberpsycho.streamingsector.json"
        )
        root = sector["Data"]["RootChunk"]
        community_index = next(
            index
            for index, node in enumerate(root["nodes"])
            if node["Data"]["$type"]
            == "worldCompiledCommunityAreaNode_Streamable"
        )
        placement = next(
            value
            for value in root["nodeData"]["Data"]
            if value["NodeIndex"] == community_index
        )
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
            ROOT / "projects/test-quests/gqt006/source/raw/mod/gqt006/world/"
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
            [scalar(value) for value in root["nodeRefs"] if scalar(value) in expected_refs],
            expected_refs,
        )
        self.assertEqual(
            [entry["NodeIndex"] for entry in root["nodeData"]["Data"]],
            list(range(len(root["nodes"]))),
        )

        alerted_spots = [
            value
            for value, node_ref_value in zip(
                root["nodes"],
                root["nodeRefs"],
                strict=True,
            )
            if value["Data"]["$type"] == "worldAISpotNode"
            and "#gqt006_ws_goth_baddie_alerted_" in scalar(node_ref_value)
        ]
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

        spline = next(
            value["Data"]
            for value in root["nodes"]
            if value["Data"]["$type"] == "worldPatrolSplineNode"
        )
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

    def test_loss_intimacy_side_camera_has_authored_tpp_transform(self) -> None:
        world = load(WORLD_SPEC)
        camera_spec = next(
            entity
            for entity in world["entities"]
            if entity["ref"] == "#gqt006_sm_intimacy_side_cam"
        )
        self.assertEqual(
            camera_spec["position"],
            {
                "x": -1026.803729,
                "y": 1280.293998,
                "z": 6.4301804,
            },
        )
        expected_orientation = {
            "i": -0.083388629,
            "j": -0.075279092,
            "k": 0.665849862,
            "r": 0.73757939,
        }
        self.assertEqual(
            camera_spec["node_data"]["orientation"], expected_orientation
        )

        sector = load(
            ROOT / "projects/test-quests/gqt006/source/raw/mod/gqt006/world/"
            "gqt006_goth_baddie_cyberpsycho.streamingsector.json"
        )["Data"]["RootChunk"]
        camera_index = next(
            index
            for index, node_ref_value in enumerate(sector["nodeRefs"])
            if scalar(node_ref_value).endswith("/#gqt006_sm_intimacy_side_cam")
        )
        placement = next(
            value
            for value in sector["nodeData"]["Data"]
            if value["NodeIndex"] == camera_index
        )
        self.assertEqual(
            placement["Position"],
            {
                "$type": "Vector4",
                "W": 0,
                "X": -1026.803729,
                "Y": 1280.293998,
                "Z": 6.4301804,
            },
        )
        self.assertEqual(
            placement["Orientation"],
            {"$type": "Quaternion", **expected_orientation},
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
            "baseAttitudeGroup: neutral",
            "tags:",
            "- Cyberpsycho",
            "Character.Cyberpsycho",
            "Ability.HasDodge",
            "Ability.HasMemoryWipeImmunity",
            "Character.AllowTechWeaponDodgeEffector",
            "Character.GhostlineGothBaddie_HealthMultiplier:",
            "value: 3.0",
        ):
            self.assertIn(expected, tweak)
        self.assertNotIn("Character.AllowAnyDirectionDodgeEffector", tweak)
        self.assertNotIn("baseAttitudeGroup: hostile", tweak)
        for removed in (
            "Ability.CanParry",
            "Ability.HasKerenzikov",
            "Ability.IsTier3Archetype",
            "Character.MaxTac_Mantis_ModGroup",
            "Character.Maxtac_miniboss_ModGroup",
        ):
            self.assertNotIn(removed, tweak)
        self.assertIn("Items.Preset_Katana_E3", tweak)
        self.assertIn("statModifiers:", tweak)

    def test_encounter_replicates_mower_combat_handoff(self) -> None:
        phase = load(PHASES / "gqt006_neutralize_goth_baddie.questphase.json")
        handles = handle_map(phase)
        gameplay = next(
            node
            for node in phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if node["Data"].get("$type") == "questPuppetAIManagerNodeDefinition"
            and all("aiTier" not in entry for entry in node["Data"]["entries"])
        )
        mortal = next(
            node
            for node in phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if any(
                isinstance(value, dict)
                and value.get("$type") == "questCharacterManagerParameters_SetMortality"
                and value.get("state") == "Mortal"
                and value.get("isPlayer") == 0
                for value in walk(node)
            )
        )
        player_immortal = next(
            node
            for node in phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if any(
                isinstance(value, dict)
                and value.get("$type") == "questCharacterManagerParameters_SetMortality"
                and value.get("state") == "Immortal"
                and value.get("isPlayer") == 1
                for value in walk(node)
            )
        )
        not_in_combat = next(
            node
            for node in phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if any(
                isinstance(value, dict)
                and value.get("$type") == "questCharacterCombat_ConditionType"
                and value.get("isPlayer") == 0
                for value in walk(node)
            )
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
        delay = next(
            node
            for node in phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if any(
                isinstance(value, dict)
                and value.get("$type") == "questRealtimeDelay_ConditionType"
                for value in walk(node)
            )
            and (
                node["Data"]["id"],
                "Out",
                not_in_combat["Data"]["id"],
                "In",
            )
            in edges
        )
        expected_edges = {
            (gameplay["Data"]["id"], "Out", mortal["Data"]["id"], "In"),
            (gameplay["Data"]["id"], "Out", delay["Data"]["id"], "In"),
            (delay["Data"]["id"], "Out", not_in_combat["Data"]["id"], "In"),
            (delay["Data"]["id"], "Out", target["Data"]["id"], "In"),
            (not_in_combat["Data"]["id"], "Out", assign["Data"]["id"], "In"),
            (
                target["Data"]["id"],
                "Success",
                player_immortal["Data"]["id"],
                "In",
            ),
            (
                player_immortal["Data"]["id"],
                "Out",
                threat["Data"]["id"],
                "In",
            ),
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

    def test_prefight_scene_suppresses_combat_and_reaches_three_real_choices(self) -> None:
        scene = load(SCENE)
        graph = scene["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
        nodes = {
            node["Data"]["nodeId"]["id"]: node["Data"]
            for node in graph
        }

        start_destinations = [
            destination["nodeId"]["id"]
            for socket in nodes[1]["outputSockets"]
            for destination in socket["destinations"]
        ]
        self.assertEqual(start_destinations, [10])
        self.assertEqual(
            [destination["nodeId"]["id"] for socket in nodes[10]["outputSockets"] for destination in socket["destinations"]],
            [2],
        )

        puppet_ai = nodes[10]["questNode"]["Data"]
        self.assertEqual(puppet_ai["$type"], "questPuppetAIManagerNodeDefinition")
        self.assertEqual(puppet_ai["entries"][0]["aiTier"], "Cinematic")
        self.assertEqual(
            puppet_ai["entries"][0]["entityReference"]["reference"]["$value"],
            "#gqt006_com_goth_baddie",
        )

        choice = nodes[3]
        self.assertEqual(choice["$type"], "scnChoiceNode")
        self.assertEqual(len(choice["options"]), 3)
        choice_destinations = [
            destination["nodeId"]["id"]
            for socket in choice["outputSockets"]
            for destination in socket["destinations"]
        ]
        self.assertEqual(choice_destinations, [4, 5, 6])
        self.assertEqual(
            [option["type"]["properties"] for option in choice["options"]],
            [1, 1, 0],
        )

    def test_intimacy_rid_is_a_synchronously_loaded_resource(self) -> None:
        scene_root = load(SCENE)["Data"]["RootChunk"]
        resources = scene_root["ridResources"]

        self.assertEqual(len(resources), 1)
        self.assertEqual(
            resources[0]["ridResource"]["DepotPath"]["$value"],
            (
                "base\\animations\\quest\\lore\\generic_sex\\intercourse\\"
                "sex_06_5s_m.scenerid"
            ),
        )
        self.assertTrue(
            all(resource["ridResource"]["Flags"] == "Default" for resource in resources)
        )

        prop = scene_root["props"][0]
        self.assertEqual(prop["entityAcquisitionPlan"], "findInNode")
        self.assertEqual(
            prop["findEntityInNodeParams"]["nodeRef"]["$value"],
            "#gqt006_sm_intimacy_cam",
        )
        props = scene_root["props"]
        self.assertTrue(all(prop["entityAcquisitionPlan"] == "findInNode" for prop in props))
        self.assertEqual(
            {prop["findEntityInNodeParams"]["nodeRef"]["$value"] for prop in props},
            {"#gqt006_sm_intimacy_cam", "#gqt006_sm_lose_face_cam", "#gqt006_sm_lose_genitals_cam"},
        )

    def test_intimacy_routes_use_distinct_roles_and_real_player_loss(self) -> None:
        main_root = load(SCENE)["Data"]["RootChunk"]
        main_nodes = {node["Data"]["nodeId"]["id"]: node["Data"] for node in main_root["sceneGraph"]["Data"]["graph"]}
        win_refs = [event["Data"]["animResRefId"]["id"] for event in main_nodes[16]["events"] if event["Data"].get("$type") == "scnPlayRidAnimEvent"]
        self.assertEqual(win_refs, [0, 1, 2])

        scene = load(SCENE.with_name("gqt006_goth_baddie_intimacy.scene.json"))["Data"]["RootChunk"]
        nodes = {node["Data"]["nodeId"]["id"]: node["Data"] for node in scene["sceneGraph"]["Data"]["graph"]}
        gender = nodes[18]["questNode"]["Data"]["condition"]["Data"]["type"]["Data"]
        self.assertEqual(gender["$type"], "questCharacterGender_CondtionType")
        self.assertEqual(gender["gender"]["$value"], "Male")
        self.assertEqual([socket["destinations"][0]["nodeId"]["id"] for socket in nodes[18]["outputSockets"]], [20, 19])
        self.assertEqual([resource["ridResource"]["Flags"] for resource in scene["ridResources"]], ["Default"] * 4)
        self.assertEqual([actor["actorName"] for actor in scene["actors"]], ["Goth Baddie"])
        self.assertEqual([actor["playerName"] for actor in scene["playerActors"]], ["V"])

        expected_sections = {
            19: ([0, 1, 2], 2000, 30), 30: ([3, 4, 5], 5000, 31),
            31: ([6, 7, 8], 2000, 33), 33: ([10, 11, 12], 2000, 21),
            20: ([0, 1, 2], 2000, 34), 34: ([3, 4, 5], 5000, 35),
            35: ([6, 7, 9], 2000, 37), 37: ([10, 11, 13], 2000, 21),
        }
        for node_id, (refs, duration, next_id) in expected_sections.items():
            with self.subTest(section=node_id):
                node = nodes[node_id]
                animations = [event["Data"] for event in node["events"] if event["Data"].get("$type") == "scnPlayRidAnimEvent"]
                self.assertEqual([event["animResRefId"]["id"] for event in animations], refs)
                self.assertEqual(sorted(event["performer"]["id"] for event in animations), [1, 1, 257])
                self.assertEqual(sum(event["FPPControlActive"] for event in animations), 1)
                self.assertEqual(node["sectionDuration"]["stu"], duration)
                destinations = [destination["nodeId"]["id"] for socket in node["outputSockets"] for destination in socket["destinations"]]
                self.assertIn(next_id, destinations)
                self.assertIn(21, destinations)  # Cancellation also reaches the fade/exit.
        self.assertEqual(nodes[21]["outputSockets"][0]["destinations"][0]["nodeId"]["id"], 50)

        encounter = load(PHASES / "gqt006_neutralize_goth_baddie.questphase.json")
        handles = handle_map(encounter)
        by_entry = {}
        for wrapper in encounter["Data"]["RootChunk"]["graph"]["Data"]["nodes"]:
            node = wrapper["Data"]
            if node.get("$type") == "questSceneNodeDefinition":
                for value in node["sockets"]:
                    socket = resolve(value, handles)["Data"]
                    if socket["type"] == "Input":
                        by_entry[scalar(socket["name"])] = node["id"]
        edges = graph_edges(encounter)
        self.assertIn((by_entry["goth_wins_debug"], "goth_intimacy_requested", by_entry["start"], "start"), edges)
        self.assertIn((by_entry["start"], "done", by_entry["goth_after"], "goth_after"), edges)

    def test_scene_handoffs_cover_combat_leave_and_both_postfight_routes(self) -> None:
        scene = load(SCENE)
        scene_root = scene["Data"]["RootChunk"]
        scene_nodes = {
            node["Data"]["nodeId"]["id"]: node["Data"]
            for node in scene_root["sceneGraph"]["Data"]["graph"]
        }
        entry_nodes = {
            value["name"]["$value"]: value["nodeId"]["id"]
            for value in scene_root["entryPoints"]
        }
        self.assertEqual(
            entry_nodes,
            {"start": 1, "v_wins": 47, "goth_wins_debug": 48, "goth_after": 78},
        )
        self.assertTrue(
            all(scene_nodes[node_id]["$type"] == "scnStartNode" for node_id in entry_nodes.values())
        )
        self.assertEqual(
            scene_nodes[47]["outputSockets"][0]["destinations"][0]["nodeId"]["id"],
            69,
        )
        self.assertEqual(
            scene_nodes[47]["outputSockets"][0]["destinations"][0]["isockStamp"]["ordinal"],
            1,
        )
        self.assertEqual(
            scene_nodes[48]["outputSockets"][0]["destinations"][0]["nodeId"]["id"],
            70,
        )
        self.assertEqual(
            scene_nodes[48]["outputSockets"][0]["destinations"][0]["isockStamp"]["ordinal"],
            1,
        )

        appearance_ids = {41, 42, 43, 44, 45, 46}
        appearance_destinations = []
        for node in scene_nodes.values():
            for socket in node.get("outputSockets", []):
                for destination in socket.get("destinations", []):
                    if destination["nodeId"]["id"] in appearance_ids:
                        appearance_destinations.append(
                            (
                                node["nodeId"]["id"],
                                destination["nodeId"]["id"],
                                destination["isockStamp"]["ordinal"],
                            )
                        )
        self.assertEqual(
            appearance_destinations,
            [
                (66, 41, 1),
                (13, 43, 1),
                (15, 43, 1),
                (17, 45, 1),
                (14, 45, 1),
                (81, 42, 1),
                (112, 46, 1),
            ],
        )

        challenge = load(PHASES / "gqt006_challenge_goth_baddie.questphase.json")
        challenge_handles = handle_map(challenge)
        challenge_scene = next(
            node
            for node in challenge["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if node["Data"].get("$type") == "questSceneNodeDefinition"
        )
        challenge_sockets = {
            scalar(resolve(value, challenge_handles)["Data"]["name"]):
            resolve(value, challenge_handles)["Data"]["type"]
            for value in challenge_scene["Data"]["sockets"]
        }
        self.assertEqual(challenge_sockets["start_combat"], "Output")
        self.assertEqual(challenge_sockets["end"], "Output")
        self.assertFalse(
            any(
                source_id == challenge_scene["Data"]["id"]
                and source_socket == "end"
                for source_id, source_socket, _, _ in graph_edges(challenge)
            )
        )

        encounter = load(PHASES / "gqt006_neutralize_goth_baddie.questphase.json")
        encounter_handles = handle_map(encounter)
        scene_sockets = []
        for node in encounter["Data"]["RootChunk"]["graph"]["Data"]["nodes"]:
            if node["Data"].get("$type") != "questSceneNodeDefinition":
                continue
            scene_sockets.append(
                {
                    scalar(resolve(value, encounter_handles)["Data"]["name"])
                    for value in node["Data"]["sockets"]
                }
            )
        self.assertIn({"CutDestination", "v_wins", "v_wins_done"}, scene_sockets)
        self.assertIn(
            {"CutDestination", "goth_wins_debug", "goth_intimacy_requested", "goth_truce_done"},
            scene_sockets,
        )
        encoded = json.dumps(encounter)
        self.assertIn("gqt006_debug_goth_wins", encoded)
        self.assertEqual(encoded.count('"type": "IsInside"'), 2)

    def test_player_defeat_is_intercepted_without_the_debug_fact(self) -> None:
        phase = load(PHASES / "gqt006_neutralize_goth_baddie.questphase.json")
        values = list(walk(phase))
        graph_nodes = phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]

        health_conditions = [
            value
            for value in values
            if isinstance(value, dict)
            and value.get("$type") == "questCharacterHealth_ConditionType"
        ]
        self.assertEqual(
            health_conditions,
            [
                {
                    "$type": "questCharacterHealth_ConditionType",
                    "comparisonType": "LessOrEqual",
                    "isPlayer": 1,
                    "objectRef": health_conditions[0]["objectRef"],
                    "percent": 5,
                }
            ],
        )

        player_mortality = [
            value
            for value in values
            if isinstance(value, dict)
            and value.get("$type")
            == "questCharacterManagerParameters_SetMortality"
            and value.get("isPlayer") == 1
        ]
        self.assertEqual(
            [(value["state"], value["resetToDefault"]) for value in player_mortality],
            [("Immortal", 0), ("Mortal", 1), ("Mortal", 1), ("Mortal", 1)],
        )

        player_heals = [
            value
            for value in values
            if isinstance(value, dict)
            and value.get("$type") == "questCharacterManagerCombat_ModifyHealth"
            and value.get("isPlayer") == 1
        ]
        self.assertEqual(len(player_heals), 1)
        self.assertEqual(player_heals[0]["percent"], 100)
        self.assertEqual(player_heals[0]["setExactValue"], 1)
        self.assertIn("gqt006_v_defeated", json.dumps(phase))

        player_immortal_node = next(
            node
            for node in graph_nodes
            if any(
                isinstance(value, dict)
                and value.get("$type")
                == "questCharacterManagerParameters_SetMortality"
                and value.get("isPlayer") == 1
                and value.get("state") == "Immortal"
                for value in walk(node)
            )
        )
        listener_nodes = [
            node
            for node in graph_nodes
            if any(
                isinstance(value, dict)
                and value.get("$type")
                in {
                    "questCharacterKilled_ConditionType",
                    "questCharacterHealth_ConditionType",
                    "questVarComparison_ConditionType",
                }
                and (
                    value.get("$type") != "questVarComparison_ConditionType"
                    or value.get("factName") == "gqt006_debug_goth_wins"
                )
                for value in walk(node)
            )
        ]
        edges = graph_edges(phase)
        for listener in listener_nodes:
            self.assertIn(
                (
                    player_immortal_node["Data"]["id"],
                    "Out",
                    listener["Data"]["id"],
                    "In",
                ),
                edges,
            )

        cinematic_boss = next(
            node
            for node in graph_nodes
            if node["Data"].get("$type") == "questPuppetAIManagerNodeDefinition"
            and any(entry.get("aiTier") == "Cinematic" for entry in node["Data"]["entries"])
        )
        friendly_boss = next(
            node
            for node in graph_nodes
            if any(
                isinstance(value, dict)
                and value.get("$type")
                == "questCharacterManagerParameters_SetAttitudeGroupForPuppet"
                and scalar(value.get("groupName")) == "friendly"
                for value in walk(node)
            )
        )
        clear_boss_role = next(
            node
            for node in graph_nodes
            if node["Data"].get("$type") == "questMiscAICommandNode"
            and any(
                isinstance(value, dict)
                and value.get("$type") == "AIClearRoleCommandParams"
                for value in walk(node)
            )
        )
        self.assertFalse(any(
            isinstance(value, dict)
            and value.get("$type") == "questCharacterCombat_ConditionType"
            and value.get("isPlayer") == 1
            for value in walk(phase)
        ))
        loss_scene = next(
            node
            for node in graph_nodes
            if node["Data"].get("$type") == "questSceneNodeDefinition"
            and any(
                scalar(resolve(socket, handle_map(phase))["Data"]["name"])
                == "goth_wins_debug"
                for socket in node["Data"]["sockets"]
            )
        )
        heal_player = next(
            node
            for node in graph_nodes
            if any(
                isinstance(value, dict)
                and value.get("$type") == "questCharacterManagerCombat_ModifyHealth"
                and value.get("isPlayer") == 1
                for value in walk(node)
            )
        )
        release_delay = next(
            node
            for node in graph_nodes
            if any(
                isinstance(value, dict)
                and value.get("$type") == "questRealtimeDelay_ConditionType"
                and value.get("miliseconds") == 200
                for value in walk(node)
            )
            and (
                node["Data"]["id"],
                "Out",
                heal_player["Data"]["id"],
                "In",
            )
            in edges
        )
        self.assertIn(
            (
                friendly_boss["Data"]["id"],
                "Out",
                clear_boss_role["Data"]["id"],
                "In",
            ),
            edges,
        )
        self.assertIn(
            (
                clear_boss_role["Data"]["id"],
                "Success",
                cinematic_boss["Data"]["id"],
                "In",
            ),
            edges,
        )
        self.assertIn(
            (release_delay["Data"]["id"], "Out", heal_player["Data"]["id"], "In"), edges,
        )
        self.assertIn(
            (
                heal_player["Data"]["id"],
                "Out",
                loss_scene["Data"]["id"],
                "goth_wins_debug",
            ),
            edges,
        )

    def test_scene_changes_postfight_and_intimacy_appearances_then_restores(self) -> None:
        scene = load(SCENE)
        appearance_changes = [
            value["appearanceName"]["$value"]
            for value in walk(scene)
            if isinstance(value, dict)
            and value.get("$type")
            == "questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry"
        ]
        self.assertEqual(
            appearance_changes,
            [
                "ghostline_goth_baddie_postfight",
                "ghostline_goth_baddie_intimacy",
                "ghostline_goth_baddie_default",
                "ghostline_goth_baddie_postfight",
                "ghostline_goth_baddie_default",
                "ghostline_goth_baddie_default",
            ],
        )

    def test_postfight_entries_holster_v_and_loss_entry_knocks_v_down(self) -> None:
        scene = load(SCENE)
        nodes = {
            node["Data"]["nodeId"]["id"]: node["Data"]
            for node in scene["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
        }

        for node_id in (54, 55):
            params = nodes[node_id]["questNode"]["Data"]["params"]["Data"]
            self.assertEqual(params["$type"], "questEquipItemParams")
            self.assertEqual(params["type"], "Unequip")
            self.assertEqual(params["unequipTypes"], "AllWeapons")
            self.assertEqual(params["isPlayer"], 1)
            self.assertEqual(params["instant"], 1)
            self.assertEqual(params["ignoreStateMachine"], 0)

        for node_id in (65, 67, 73):
            quest_node = nodes[node_id]["questNode"]["Data"]
            observable = quest_node["entityReference"]["Data"]
            entity_ref = observable["entityReference"]
            params = quest_node["params"]["Data"]
            self.assertEqual(observable["refLocalPlayer"], 0)
            self.assertEqual(entity_ref["reference"]["$value"], "#gqt006_com_goth_baddie")
            self.assertEqual(
                [name["$value"] for name in entity_ref["names"]],
                ["goth_baddie"],
            )
            self.assertEqual(params["type"], "Unequip")
            self.assertEqual(params["isPlayer"], 0)
            self.assertEqual(params["byItem"], 1)
            self.assertEqual(params["itemId"]["$value"], "Items.Preset_Katana_E3")
            self.assertEqual(
                params["slotId"]["$value"], "AttachmentSlots.WeaponRight"
            )
            self.assertEqual(params["unequipTypes"], "AllItems")
            self.assertEqual(params["instant"], 1)
            self.assertEqual(params["ignoreStateMachine"], 0)

        for node_id in (66, 68):
            delay = nodes[node_id]["questNode"]["Data"]["condition"]["Data"][
                "type"
            ]["Data"]
            self.assertEqual(delay["$type"], "questRealtimeDelay_ConditionType")
            self.assertEqual(delay["miliseconds"], 100)

        for node_id in (69, 70):
            entry = nodes[node_id]["questNode"]["Data"]["entries"][0]
            self.assertEqual(entry["aiTier"], "Cinematic")
            self.assertEqual(
                entry["entityReference"]["reference"]["$value"],
                "#gqt006_com_goth_baddie",
            )

        knockdown = (
            nodes[56]["questNode"]["Data"]["type"]["Data"]["subtype"]["Data"]
        )
        self.assertEqual(
            knockdown["statusEffectID"]["$value"],
            "BaseStatusEffect.Knockdown",
        )
        self.assertEqual(knockdown["isPlayer"], 1)
        self.assertEqual(knockdown["set"], 1)
        self.assertEqual(nodes[57]["sectionDuration"]["stu"], 750)

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
        registration = (ROOT / "projects/test-quests/gqt006/source/resources/Goth_Baddie.archive.xl").read_text(
            encoding="utf-8"
        )
        for expected in (
            r"mod\gqt006\phases\gqt006_goth_baddie_cyberpsycho.questphase",
            r"mod\gqt006\journal\gqt006.journal",
            r"mod\gqt006\localization\en-us\onscreens\gqt006.json",
            r"mod\gqt006\localization\en-us\subtitles\gqt006_10_subtitles_map.json",
            r"mod\gqt006\localization\en-us\vo\gqt006_10.json",
            r"mod\gqt006\world\gqt006_goth_baddie_cyberpsycho.streamingblock",
        ):
            self.assertIn(expected, registration)

    def test_all_authored_cr2w_outputs_have_binary_headers(self) -> None:
        expected = [
            ARCHIVE_ROOT / "journal/gqt006.journal",
            ARCHIVE_ROOT / "localization/en-us/onscreens/gqt006.json",
            ARCHIVE_ROOT / "localization/en-us/subtitles/gqt006_10.json",
            ARCHIVE_ROOT / "localization/en-us/subtitles/gqt006_10_subtitles_map.json",
            ARCHIVE_ROOT / "localization/en-us/vo/gqt006_10.json",
            ARCHIVE_ROOT / "scenes/gqt006_goth_baddie.scene",
            ARCHIVE_ROOT / "world/gqt006_goth_baddie_cyberpsycho.streamingsector",
            ARCHIVE_ROOT / "world/gqt006_always_loaded.streamingsector",
            ARCHIVE_ROOT / "world/gqt006_goth_baddie_cyberpsycho.streamingblock",
            ARCHIVE_ROOT / "phases/gqt006_goth_baddie_cyberpsycho.questphase",
            *[
                ARCHIVE_ROOT / f"phases/gqt006_{name}.questphase"
                for name in (
                    "neutralize_goth_baddie",
                    "challenge_goth_baddie",
                    "recover_goth_baddie_shard",
                    "read_goth_baddie_shard",
                    "leave_goth_baddie_site",
                    "report_goth_baddie_outcome",
                )
            ],
            ROOT
            / "projects/test-quests/gqt006/source/archive/mod/ghostline/characters/goth_baddie/goth_baddie.ent",
            ROOT
            / "projects/test-quests/gqt006/source/archive/mod/ghostline/characters/goth_baddie/goth_baddie.app",
        ]
        for path in expected:
            with self.subTest(path=path):
                self.assertTrue(path.is_file())
                self.assertEqual(path.read_bytes()[:4], b"CR2W")


if __name__ == "__main__":
    unittest.main()
