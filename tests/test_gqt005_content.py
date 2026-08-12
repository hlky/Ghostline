from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import unittest
import zlib
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import braindance_pipeline
import braindance_scene
import quest_compiler

BUILD_PATH = ROOT / "quests/tests/gqt005/implementation/build.py"
BUILD_SPEC = importlib.util.spec_from_file_location(
    "generate_gqt005_content",
    BUILD_PATH,
)
assert BUILD_SPEC is not None and BUILD_SPEC.loader is not None
generate_gqt005_content = importlib.util.module_from_spec(BUILD_SPEC)
sys.modules["generate_gqt005_content"] = generate_gqt005_content
BUILD_SPEC.loader.exec_module(generate_gqt005_content)

SCENE = ROOT / "source/raw/mod/gqt005/scenes/gqt005_braindance_analysis.scene.json"
SCENE_TEMPLATE = ROOT / "braindance/templates/braindance_analysis.scene.json"
WORLD_SPEC = (
    ROOT / "quests/tests/gqt005/implementation/world/braindance-analysis.world.json"
)
LAUNCH_SCENE = ROOT / "source/raw/mod/gqt005/scenes/gqt005_patch_start.scene.json"
SPEC = ROOT / "braindance/tests/gqt005_braindance_analysis.json"
MANIFEST = ROOT / "quests/tests/gqt005_braindance_analysis.quest.json"
JOURNAL = ROOT / "source/raw/mod/gqt005/journal/gqt005.journal.json"
REVIEW_PHASE = (
    ROOT / "source/raw/mod/gqt005/phases/gqt005_review_braindance.questphase.json"
)


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


class BraindanceAnalysisContentTests(unittest.TestCase):
    def test_braindance_spec_uses_checked_full_body_rig(self) -> None:
        spec = load(SPEC)
        contract_path = ROOT / "braindance/rigs/man_base.skeleton.json"
        contract_bytes = contract_path.read_bytes()
        contract = json.loads(contract_bytes)
        bone_order = [bone["name"] for bone in contract["bones"]]

        self.assertEqual(contract["kind"], "ghostline_braindance_skeleton")
        self.assertEqual(contract["name"], "man_base")
        self.assertEqual(contract["bone_count"], 71)
        self.assertEqual(contract["trajectory_joint_index"], 1)
        self.assertEqual(
            [bone["index"] for bone in contract["bones"]],
            list(range(71)),
        )
        self.assertEqual(len(set(bone_order)), 71)
        self.assertEqual(
            bone_order[0:7],
            [
                "Root",
                "Trajectory",
                "Hips",
                "reference_joint",
                "Spine",
                "LeftUpLeg",
                "RightUpLeg",
            ],
        )
        self.assertEqual(bone_order[1], "Trajectory")

        handoff = braindance_scene.build_handoff_manifest(spec, SPEC)
        expected_hash = hashlib.sha256(contract_bytes).hexdigest()
        for actor, actor_handoff in zip(
            spec["actors"],
            handoff["actors"],
            strict=True,
        ):
            self.assertEqual(
                actor["asset"]["path"],
                "braindance/rigs/man_base.glb",
            )
            self.assertEqual(
                actor["rig"]["contract"],
                "braindance/rigs/man_base.skeleton.json",
            )
            self.assertEqual(
                actor["body_animation"]["type"],
                "walk_from_root_motion",
            )
            self.assertGreater(actor["body_animation"]["stride_length"], 0)
            self.assertGreater(
                actor["body_animation"]["leg_swing_degrees"],
                0,
            )
            self.assertEqual(actor_handoff["rig"]["bone_order"], bone_order)
            self.assertEqual(actor_handoff["rig"]["bone_count"], 71)
            self.assertEqual(
                actor_handoff["rig"]["contract_sha256"],
                expected_hash,
            )
            self.assertEqual(
                actor_handoff["body_animation"],
                actor["body_animation"],
            )

    def test_typed_manifest_is_ready_and_resolves_builtin_template(self) -> None:
        spec, diagnostics = quest_compiler.load_spec(MANIFEST)
        self.assertIsNotNone(
            spec,
            [diagnostic.as_dict() for diagnostic in diagnostics],
        )
        assert spec is not None
        self.assertEqual(
            [stage.type for stage in spec.stages],
            ["reach_area", "meet_contact", "braindance_analysis"],
        )
        stage = spec.stages[2]
        self.assertEqual(stage.type, "braindance_analysis")
        self.assertEqual(stage.status, "ready")
        self.assertEqual(
            stage.data["objective"],
            ("quests/minor_quest/gqt005/gqt005_01/gqt005_01_obj_review_braindance"),
        )
        self.assertEqual(
            stage.data["clue_facts"],
            [
                "gqt005_bd_encrypted_shard_found",
                "gqt005_bd_guard_warning_found",
                "gqt005_bd_guard_implant_heat_found",
            ],
        )
        self.assertEqual(
            quest_compiler.stage_template_resource(stage),
            (
                r"mod\ghostline\quest_blocks\templates"
                r"\braindance_analysis.questphase"
            ),
        )
        self.assertFalse(
            [
                item
                for item in quest_compiler.audit_resources(spec)
                if item.level == "error"
            ]
        )

    def test_review_objective_has_vanilla_three_clue_counter(self) -> None:
        journal = load(JOURNAL)
        objective = next(
            item
            for item in walk(journal)
            if isinstance(item, dict)
            and item.get("$type") == "gameJournalQuestObjective"
            and item.get("id") == "gqt005_01_obj_review_braindance"
        )
        self.assertEqual(objective["counter"], 3)

        review = load(REVIEW_PHASE)
        counters = [
            item
            for item in review["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if any(
                isinstance(child, dict)
                and child.get("$type") == "questJournalQuestObjectiveCounter_NodeType"
                for child in walk(item)
            )
        ]
        self.assertEqual(
            [item["Data"]["id"] for item in counters],
            [26, 27, 28],
        )
        for counter in counters:
            counter_type = next(
                child
                for child in walk(counter)
                if isinstance(child, dict)
                and child.get("$type") == "questJournalQuestObjectiveCounter_NodeType"
            )
            self.assertEqual(
                counter_type["path"]["Data"]["realPath"],
                ("quests/minor_quest/gqt005/gqt005_01/gqt005_01_obj_review_braindance"),
            )
            self.assertEqual(
                counter_type["path"]["Data"]["className"]["$value"],
                "gameJournalQuestObjective",
            )
            self.assertEqual(
                counter_type["path"]["Data"]["fileEntryIndex"],
                2,
            )
        quest_compiler.validate_handle_graph(
            review,
            context="gqt005 review clue counters",
        )
        quest_compiler.validate_no_forward_handle_refs(
            review,
            context="gqt005 review clue counters",
        )

    def test_scene_has_functional_editor_graph_and_three_layers(self) -> None:
        handoff = braindance_scene.build_handoff_manifest(
            load(SPEC),
            SPEC,
        )
        report = braindance_pipeline.audit_scene_document(
            load(SCENE),
            handoff=handoff,
        )
        self.assertTrue(report["ok"], report["errors"])
        self.assertEqual(
            report["clue_layers"],
            ["Audio", "Thermal", "Visual"],
        )
        self.assertTrue(report["finish_action_enabled"])
        self.assertTrue(report["exit_action_consumed"])
        self.assertTrue(report["rewind_loop_present"])
        self.assertTrue(report["normal_exit_cleanup"])
        self.assertEqual(report["functional_clue_count"], 3)
        scene = load(SCENE)["Data"]["RootChunk"]
        graph = scene["sceneGraph"]["Data"]["graph"]
        self.assertEqual(len(graph), 58)
        by_id = {node["Data"]["nodeId"]["id"]: node["Data"] for node in graph}
        self.assertEqual(
            [
                destination["nodeId"]["id"]
                for destination in by_id[1]["outputSockets"][0]["destinations"]
            ],
            [31, 168, 6091, 6092, 6505, 6515, 6525],
        )
        self.assertEqual(
            by_id[6091]["questNode"]["Data"]["type"]["Data"],
            {
                "$type": "questSetVar_NodeType",
                "factName": "braindaneAudioLayerAvailable",
                "setExactValue": 1,
                "value": 1,
            },
        )
        self.assertEqual(
            by_id[6092]["questNode"]["Data"]["type"]["Data"],
            {
                "$type": "questSetVar_NodeType",
                "factName": "braindaneThermalLayerAvailable",
                "setExactValue": 1,
                "value": 1,
            },
        )
        self.assertEqual(
            [
                destination["nodeId"]["id"]
                for destination in by_id[31]["outputSockets"][0]["destinations"]
            ],
            [20],
        )
        tier2 = by_id[31]["questNode"]["Data"]["type"]["Data"]
        self.assertEqual(tier2["tier"], "Tier2_StagedGameplay")
        self.assertEqual(tier2["forceEmptyHands"], 1)
        self.assertEqual(
            by_id[28]["questNode"]["Data"]["type"]["Data"]["factName"],
            "bd_stop",
        )
        self.assertEqual(
            by_id[34]["questNode"]["Data"]["type"]["Data"]["tier"],
            "Tier1_FullGameplay",
        )
        self.assertEqual(
            [
                destination["nodeId"]["id"]
                for node_id in (4576, 527, 28, 34)
                for destination in by_id[node_id]["outputSockets"][0]["destinations"]
            ],
            [527, 28, 34, 2],
        )
        self.assertEqual(
            [option["itemId"]["id"] for option in scene["screenplayStore"]["options"]],
            [2, 258, 514],
        )
        self.assertEqual(len(scene["locStore"]["vdEntries"]), 12)
        self.assertEqual(len(scene["locStore"]["vpEntries"]), 12)
        self.assertEqual(
            {entry["content"] for entry in scene["locStore"]["vpEntries"]},
            {"", "Inspect clue"},
        )
        self.assertEqual(
            [
                symbol["performerId"]["id"]
                for symbol in scene["debugSymbols"]["performersDebugSymbols"]
            ],
            [1, 257, 513, 2, 258, 514, 770, 1026],
        )
        editor_event_ids = {
            str(symbol["editorEventId"])
            for symbol in scene["debugSymbols"]["sceneEventsDebugSymbols"]
        }
        self.assertTrue({"268435782", "268435791"}.issubset(editor_event_ids))
        self.assertEqual(
            scene["playerActors"][0]["actorId"]["id"],
            2,
        )
        self.assertEqual(report["camera_refs"], ["#gqt005_bd_camera"])
        self.assertEqual(len(scene["props"]), 7)
        self.assertEqual(
            [prop["propName"] for prop in scene["props"]],
            [
                "gqt005_bd_camera",
                "gqt005_bdview",
                "gqt005_bdfog",
                "gqt005_bdsetup",
                "gqt005_encrypted_shard",
                "gqt005_bd_clue_audio",
                "gqt005_bd_clue_thermal",
            ],
        )
        self.assertEqual(
            [prop["propId"]["id"] for prop in scene["props"]],
            [0, 1, 2, 3, 4, 5, 6],
        )
        infrastructure_props = {
            prop["propName"]: prop["spawnDespawnParams"]["spawnMarkerNodeRef"]["$value"]
            for prop in scene["props"]
            if prop["propName"] in {"gqt005_bdview", "gqt005_bdfog", "gqt005_bdsetup"}
        }
        self.assertEqual(
            infrastructure_props,
            {
                "gqt005_bdview": "#gqt005_bdview_spawner",
                "gqt005_bdfog": "#gqt005_bdview_spawner",
                "gqt005_bdsetup": "#gqt005_bdview_spawner",
            },
        )
        infrastructure_records = {
            prop["propName"]: (
                prop["specPropRecordId"]["$value"],
                prop["spawnDespawnParams"]["specRecordId"]["$value"],
            )
            for prop in scene["props"]
            if prop["propName"] in {"gqt005_bdview", "gqt005_bdfog", "gqt005_bdsetup"}
        }
        self.assertEqual(
            infrastructure_records,
            {
                "gqt005_bdview": (
                    "Props.GhostlineGQT005BDView",
                    "Props.GhostlineGQT005BDView",
                ),
                "gqt005_bdfog": (
                    "Props.GhostlineGQT005BDFog",
                    "Props.GhostlineGQT005BDFog",
                ),
                "gqt005_bdsetup": (
                    "Props.GhostlineGQT005BDSetup",
                    "Props.GhostlineGQT005BDSetup",
                ),
            },
        )
        tweaks = (
            ROOT / "source/resources/r6/tweaks/ghostline/gqt005_braindance.yaml"
        ).read_text(encoding="utf-8")
        self.assertNotIn("Props.q004", tweaks)
        self.assertEqual(tweaks.count("$type: gamedataProp_Record"), 6)
        for record, entity in (
            ("Props.GhostlineGQT005BDView", "gqt005_bdview.ent"),
            ("Props.GhostlineGQT005BDFog", "gqt005_bdfog.ent"),
            ("Props.GhostlineGQT005BDSetup", "gqt005_bdsetup.ent"),
        ):
            self.assertIn(record, tweaks)
            self.assertIn(entity, tweaks)
        shard = next(
            prop
            for prop in scene["props"]
            if prop["propName"] == "gqt005_encrypted_shard"
        )
        self.assertEqual(
            shard["spawnDespawnParams"]["spawnMarkerNodeRef"]["$value"],
            "#gqt005_bd_origin",
        )
        self.assertEqual(
            shard["spawnDespawnParams"]["spawnOffset"]["position"],
            {
                "$type": "Vector4",
                "W": 0,
                "X": 0.0,
                "Y": 0.0,
                "Z": 0.92,
            },
        )
        self.assertEqual(
            shard["spawnDespawnParams"]["specRecordId"]["$value"],
            "Props.GhostlineGQT005BDEncryptedShardClue",
        )
        self.assertEqual(
            shard["specPropRecordId"]["$value"],
            "Props.GhostlineGQT005BDEncryptedShardClue",
        )
        guard = next(
            actor for actor in scene["actors"] if actor["actorName"] == "Guard"
        )
        self.assertEqual(
            guard["spawnDespawnParams"]["spawnMarkerNodeRef"]["$value"],
            "#gqt005_bd_origin",
        )
        self.assertEqual(
            guard["spawnDespawnParams"]["appearance"]["$value"],
            "gang__tyger_ma_gangster__lvl2_01",
        )
        self.assertEqual(
            guard["specAppearance"]["$value"],
            "gang__tyger_ma_gangster__lvl2_01",
        )
        self.assertEqual(
            report["visibility_targets"],
            ["gqt005_bdfog", "gqt005_bdview"],
        )
        self.assertEqual(
            report["clue_entities"],
            {
                "encrypted_shard": ("p_gqt005_braindance_analysis_encrypted_shard"),
                "guard_warning": ("p_gqt005_braindance_analysis_clue_audio"),
                "guard_implant_heat": ("p_gqt005_braindance_analysis_clue_thermal"),
            },
        )
        self.assertEqual(
            report["clue_availability_facts"],
            {
                "encrypted_shard": "gqt005_bd_encrypted_shard_clue_on",
                "guard_warning": "gqt005_bd_guard_warning_clue_on",
                "guard_implant_heat": "gqt005_bd_guard_implant_heat_clue_on",
            },
        )
        for (
            base,
            auxiliary_base,
            prop_id,
            target_dynamic_name,
            availability_fact,
            layer,
            completion_fact,
        ) in (
            (
                6000,
                6500,
                4,
                "p_gqt005_braindance_analysis_encrypted_shard",
                "gqt005_bd_encrypted_shard_clue_on",
                "Visual",
                "gqt005_bd_encrypted_shard_found",
            ),
            (
                6010,
                6510,
                5,
                "p_gqt005_braindance_analysis_clue_audio",
                "gqt005_bd_guard_warning_clue_on",
                "Audio",
                "gqt005_bd_guard_warning_found",
            ),
            (
                6020,
                6520,
                6,
                "p_gqt005_braindance_analysis_clue_thermal",
                "gqt005_bd_guard_implant_heat_clue_on",
                "Thermal",
                "gqt005_bd_guard_implant_heat_found",
            ),
        ):
            scan = by_id[base + 1]
            valid = by_id[base + 2]
            choice = by_id[base + 3]
            invalid = by_id[base + 4]
            cut = by_id[base + 5]
            inspected = by_id[base + 6]
            discovered = by_id[base + 7]
            completion = by_id[base + 8]
            reactivate = by_id[base + 9]
            success_cut = by_id[auxiliary_base + 1]
            reactivation_section = by_id[auxiliary_base + 2]
            enable_scanning = by_id[auxiliary_base + 3]
            disable_scanning = by_id[auxiliary_base + 4]
            bootstrap_scanning = by_id[auxiliary_base + 5]
            seed_focus = by_id[auxiliary_base + 6]
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in bootstrap_scanning["outputSockets"][0][
                        "destinations"
                    ]
                ],
                [
                    (base + 1, 0, 1),
                    (auxiliary_base + 6, 0, 1),
                ],
            )
            bootstrap_type = bootstrap_scanning["questNode"]["Data"]["type"]["Data"]
            self.assertEqual(
                bootstrap_type["$type"],
                "questEnableScanning_NodeType",
            )
            self.assertEqual(bootstrap_type["enable"], 1)
            self.assertEqual(
                bootstrap_type["objectRef"]["dynamicEntityUniqueName"]["$value"],
                target_dynamic_name,
            )
            self.assertEqual(
                seed_focus["questNode"]["Data"]["event"]["Data"]["investigationState"],
                "NOT_INSPECTED",
            )
            self.assertIn(target_dynamic_name, json.dumps(seed_focus))
            self.assertEqual(
                [
                    destination["nodeId"]["id"]
                    for destination in scan["outputSockets"][0]["destinations"]
                ],
                [base + 2],
            )
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in valid["outputSockets"][0]["destinations"]
                ],
                [
                    (auxiliary_base + 3, 0, 1),
                    (base + 4, 0, 1),
                ],
            )
            self.assertEqual(choice["choiceFlags"], "IsFocusClue")
            self.assertEqual(choice["mode"], "attachToProp")
            self.assertEqual(choice["atpParams"]["propId"]["id"], prop_id)
            self.assertEqual(
                scene["props"][prop_id]["spawnDespawnParams"][
                    "dynamicEntityUniqueName"
                ]["$value"],
                target_dynamic_name,
            )
            self.assertIn(target_dynamic_name, json.dumps(scan))
            self.assertIn(target_dynamic_name, json.dumps(inspected))
            self.assertEqual(
                choice["atpParams"]["visualizerStyle"],
                "onScreen",
            )
            self.assertEqual(
                choice["shapeParams"]["Data"]["customActivationRange"],
                3,
            )
            self.assertEqual(
                choice["shapeParams"]["Data"]["customIndicationRange"],
                20,
            )
            self.assertEqual(
                choice["shapeParams"]["Data"]["preset"],
                "normal",
            )
            self.assertEqual(
                choice["mappinParams"]["Data"]["locationType"],
                "None",
            )
            self.assertEqual(
                choice["choiceGroup"]["$value"],
                "ghostline_bd_clues",
            )
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in choice["outputSockets"][0]["destinations"]
                ],
                [(auxiliary_base + 1, 0, 0)],
            )
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in invalid["outputSockets"][0]["destinations"]
                ],
                [(auxiliary_base + 4, 0, 1)],
            )
            for scanning_node, enabled in (
                (enable_scanning, 1),
                (disable_scanning, 0),
            ):
                scanning_type = scanning_node["questNode"]["Data"]["type"]["Data"]
                self.assertEqual(
                    scanning_type["$type"],
                    "questEnableScanning_NodeType",
                )
                self.assertEqual(scanning_type["enable"], enabled)
                self.assertEqual(
                    scanning_type["objectRef"]["dynamicEntityUniqueName"]["$value"],
                    target_dynamic_name,
                )
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in enable_scanning["outputSockets"][0][
                        "destinations"
                    ]
                ],
                [(base + 3, 0, 0)],
            )
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in disable_scanning["outputSockets"][0][
                        "destinations"
                    ]
                ],
                [(base + 5, 0, 0)],
            )
            self.assertEqual(cut["$type"], "scnCutControlNode")
            self.assertEqual(
                [
                    (
                        socket["stamp"]["name"],
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for socket in cut["outputSockets"]
                    for destination in socket["destinations"]
                ],
                [
                    (0, base + 2, 0, 1),
                    (1, base + 3, 1, 0),
                ],
            )
            self.assertEqual(success_cut["$type"], "scnCutControlNode")
            self.assertEqual(
                [
                    (
                        socket["stamp"]["name"],
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for socket in success_cut["outputSockets"]
                    for destination in socket["destinations"]
                ],
                [
                    (0, base + 6, 0, 1),
                    (1, base + 4, 0, 0),
                    (1, base + 4, 1026, 0),
                ],
            )
            valid_values = list(walk(valid))
            self.assertTrue(
                any(
                    item.get("$type") == "questLogicalCondition"
                    and item.get("operation") == "AND"
                    for item in valid_values
                    if isinstance(item, dict)
                )
            )
            self.assertTrue(
                any(
                    item.get("$type") == "questVarComparison_ConditionType"
                    and item.get("comparisonType") == "Greater"
                    and item.get("factName") == availability_fact
                    for item in valid_values
                    if isinstance(item, dict)
                )
            )
            self.assertTrue(
                any(
                    item.get("$type") == "scnBraindanceLayer_ConditionType"
                    and item.get("layer") == layer
                    for item in valid_values
                    if isinstance(item, dict)
                )
            )
            invalid_values = list(walk(invalid))
            self.assertTrue(
                any(
                    item.get("$type") == "questLogicalCondition"
                    and item.get("operation") == "OR"
                    for item in invalid_values
                    if isinstance(item, dict)
                )
            )
            self.assertTrue(
                any(
                    item.get("$type") == "questVarComparison_ConditionType"
                    and item.get("comparisonType") == "LessOrEqual"
                    and item.get("factName") == availability_fact
                    for item in invalid_values
                    if isinstance(item, dict)
                )
            )
            self.assertIn(
                "ToggleFocusClueEvent",
                json.dumps(inspected),
            )
            inspected_data = inspected["questNode"]["Data"]
            self.assertEqual(
                inspected_data["event"]["Data"]["investigationState"],
                "INSPECTED",
            )
            self.assertEqual(
                inspected_data["objectRef"]["dynamicEntityUniqueName"]["$value"],
                target_dynamic_name,
            )
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in inspected["outputSockets"][0]["destinations"]
                ],
                [(base + 7, 0, 1)],
            )
            self.assertIn(
                "questDiscoverBraindanceClue_NodeType",
                json.dumps(discovered),
            )
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in discovered["outputSockets"][0]["destinations"]
                ],
                [(base + 8, 0, 1)],
            )
            completion_type = next(
                item
                for item in walk(completion)
                if isinstance(item, dict)
                and item.get("$type") == "questSetVar_NodeType"
            )
            self.assertEqual(completion_type["factName"], completion_fact)
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in completion["outputSockets"][0]["destinations"]
                ],
                [(auxiliary_base + 2, 0, 0)],
            )
            self.assertEqual(
                reactivation_section["$type"],
                "scnSectionNode",
            )
            self.assertEqual(reactivation_section["isFocusClue"], 1)
            self.assertEqual(
                reactivation_section["sectionDuration"]["stu"],
                100,
            )
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in reactivation_section["outputSockets"][0][
                        "destinations"
                    ]
                ],
                [(base + 9, 0, 0)],
            )
            self.assertEqual(reactivate["$type"], "scnHubNode")
            self.assertEqual(
                [
                    (
                        destination["nodeId"]["id"],
                        destination["isockStamp"]["name"],
                        destination["isockStamp"]["ordinal"],
                    )
                    for destination in reactivate["outputSockets"][0]["destinations"]
                ],
                [(base + 3, 2, 0)],
            )
            self.assertTrue(
                any(
                    point["nodeId"]["id"] == base + 3
                    for point in scene["notablePoints"]
                )
            )
        encoded_graph = json.dumps(graph)
        self.assertEqual(encoded_graph.count("questScan_ConditionType"), 3)
        self.assertEqual(encoded_graph.count("ToggleFocusClueEvent"), 6)
        self.assertEqual(
            encoded_graph.count("questEnableScanning_NodeType"),
            9,
        )
        self.assertEqual(
            encoded_graph.count("questDiscoverBraindanceClue_NodeType"),
            3,
        )
        self.assertEqual(encoded_graph.count('"choiceFlags": "IsFocusClue"'), 3)
        self.assertEqual(encoded_graph.count('"$type": "scnCutControlNode"'), 6)
        self.assertEqual(encoded_graph.count('"$type": "scnHubNode"'), 3)
        self.assertEqual(encoded_graph.count('"operation": "AND"'), 3)
        self.assertEqual(encoded_graph.count('"operation": "OR"'), 3)
        self.assertEqual(
            [actor["animSets"] for actor in scene["actors"]],
            [
                [{"$type": "scnSRRefId", "id": 0}],
                [{"$type": "scnSRRefId", "id": 1}],
            ],
        )
        self.assertEqual(
            [actor["lipsyncAnimSet"]["id"] for actor in scene["actors"]],
            [0xFFFFFFFF, 0xFFFFFFFF],
        )
        self.assertEqual(
            scene["playerActors"][0]["lipsyncAnimSet"]["id"],
            0xFFFFFFFF,
        )
        self.assertEqual(
            scene["props"][0]["findEntityInNodeParams"]["nodeRef"]["$value"],
            "#gqt005_bd_camera",
        )
        rewindable = next(
            node["Data"]
            for node in graph
            if node["Data"]["$type"] == "scnRewindableSectionNode"
        )
        self.assertEqual(
            [behavior["actorId"]["id"] for behavior in rewindable["actorBehaviors"]],
            [0, 1, 2],
        )
        self.assertEqual(len(rewindable["events"]), 13)
        attachments = [
            event["Data"]
            for event in rewindable["events"]
            if event["Data"].get("$type") == "scneventsAttachPropToPerformer"
        ]
        self.assertEqual(
            [
                (
                    attachment["propId"]["id"],
                    attachment["performerId"]["id"],
                    attachment["slot"]["$value"],
                    attachment["startTime"],
                    attachment["offsetMode"],
                    (
                        attachment["customOffsetPos"]["X"],
                        attachment["customOffsetPos"]["Y"],
                        attachment["customOffsetPos"]["Z"],
                    ),
                )
                for attachment in attachments
            ],
            [
                (
                    4,
                    1,
                    "WeaponLeft",
                    0,
                    "useCustomOffset",
                    (0.0, 0.0, 0.0),
                ),
                (
                    5,
                    257,
                    "(Root)",
                    0,
                    "useCustomOffset",
                    (0.0, 0.0, 1.55),
                ),
                (
                    6,
                    257,
                    "(Root)",
                    0,
                    "useCustomOffset",
                    (0.0, 0.0, 1.2),
                ),
            ],
        )
        clue_events = [
            event["Data"]
            for event in rewindable["events"]
            if event["Data"].get("$type") == "scneventsClueEvent"
        ]
        self.assertEqual(
            {
                event["clueName"]["$value"]: event["factName"]["$value"]
                for event in clue_events
            },
            {
                "encrypted_shard": "gqt005_bd_encrypted_shard_clue_on",
                "guard_warning": "gqt005_bd_guard_warning_clue_on",
                "guard_implant_heat": "gqt005_bd_guard_implant_heat_clue_on",
            },
        )
        self.assertEqual(
            {
                event["clueName"]["$value"]: event["clueEntity"][
                    "dynamicEntityUniqueName"
                ]["$value"]
                for event in clue_events
            },
            {
                "encrypted_shard": "p_gqt005_braindance_analysis_encrypted_shard",
                "guard_warning": "p_gqt005_braindance_analysis_clue_audio",
                "guard_implant_heat": "p_gqt005_braindance_analysis_clue_thermal",
            },
        )
        clue_events_by_name = {
            event["clueName"]["$value"]: event for event in clue_events
        }
        self.assertEqual(
            clue_events_by_name["guard_implant_heat"]["executionTagFlags"],
            16,
        )
        self.assertEqual(
            clue_events_by_name["guard_warning"]["executionTagFlags"],
            0,
        )
        audio_events = [
            event["Data"]
            for event in rewindable["events"]
            if event["Data"].get("$type") == "scnAudioDurationEvent"
        ]
        self.assertEqual(
            [
                (
                    event["audioEventName"]["$value"],
                    event["performer"]["id"],
                    event["startTime"],
                    event["duration"],
                    event["playbackDirectionSupport"],
                    event["type"],
                )
                for event in audio_events
            ],
            [
                (
                    "q004_sc_04a_thug_breath_long",
                    257,
                    2400,
                    3133,
                    "Forward",
                    "0",
                ),
                (
                    "q004_sc_04a_thug_breath_long_rev",
                    257,
                    2400,
                    3133,
                    "Backward",
                    "0",
                ),
            ],
        )
        event_index_by_id = {
            event["Data"]["id"]["id"]: index
            for index, event in enumerate(rewindable["events"])
        }
        self.assertLess(
            event_index_by_id[attachments[0]["id"]["id"]],
            event_index_by_id[clue_events_by_name["encrypted_shard"]["id"]["id"]],
        )
        audio_clue_index = event_index_by_id[
            clue_events_by_name["guard_warning"]["id"]["id"]
        ]
        self.assertTrue(
            all(
                event_index_by_id[event["id"]["id"]] < audio_clue_index
                for event in audio_events
            )
        )
        clue_positions = {
            prop["propId"]["id"]: (
                prop["spawnDespawnParams"]["spawnOffset"]["position"]["X"],
                prop["spawnDespawnParams"]["spawnOffset"]["position"]["Y"],
                prop["spawnDespawnParams"]["spawnOffset"]["position"]["Z"],
            )
            for prop in scene["props"]
            if prop["propId"]["id"] in {4, 5, 6}
        }
        self.assertEqual(
            clue_positions,
            {
                4: (0.0, 0.0, 0.92),
                5: (-1.64, -0.28, 1.55),
                6: (-1.25, -0.25, 1.2),
            },
        )
        bdview = next(
            event["Data"]
            for event in rewindable["events"]
            if event["Data"].get("$type") == "scneventsBraindanceVisibilityEvent"
            and event["Data"]["performerId"]["id"] == 258
        )
        self.assertEqual(bdview["override"], 1)
        expected_render_types = [
            "BloomAreaSettings",
            "ChromaticAberrationAreaSettings",
            "ColorGradingAreaSettings",
            "ImageBasedFlareAreaSettings",
            "VolumetricFogAreaSettings",
        ]
        for field in ("renderSettingsFPP", "renderSettingsTPP"):
            self.assertEqual(
                [item["Data"]["$type"] for item in bdview[field]["areaParameters"]],
                expected_render_types,
            )
        self.assertEqual(scene["exitPoints"][0]["name"]["$value"], "complete")

    def test_bd_capture_rig_is_gqt005_owned_and_stage_authored(self) -> None:
        helper_root = ROOT / "source/raw/mod/gqt005/braindance"
        helper_paths = [
            helper_root / "gqt005_bdview.ent.json",
            helper_root / "gqt005_bdfog.ent.json",
            helper_root / "gqt005_bdsetup.ent.json",
            helper_root / "gqt005_bdview.mesh.json",
            helper_root / "gqt005_bdview.mi.json",
            helper_root / "gqt005_bdfog.mesh.json",
            helper_root / "gqt005_reveal_mask.xbm.json",
            helper_root / "gqt005_clues_data.xbm.json",
        ]
        helpers = [load(path) for path in helper_paths]
        encoded = json.dumps(helpers)
        strings = {
            item
            for document in helpers
            for item in walk(document)
            if isinstance(item, str)
        }
        self.assertNotIn("q004_04a_bd_tutorial", encoded)
        for depot_path in (
            r"mod\gqt005\braindance\gqt005_bdview.mesh",
            r"mod\gqt005\braindance\gqt005_bdview.mi",
            r"mod\gqt005\braindance\gqt005_bdfog.mesh",
            r"mod\gqt005\braindance\gqt005_reveal_mask.xbm",
            r"mod\gqt005\braindance\gqt005_clues_data.xbm",
        ):
            self.assertIn(depot_path, strings)

        setup = load(helper_root / "gqt005_bdsetup.ent.json")
        cameras = {}
        for item in walk(setup):
            if (
                isinstance(item, dict)
                and item.get("$type") == "entRenderToTextureCameraComponent"
            ):
                name = item["virtualCameraName"]["$value"]
                cameras.setdefault(name, item)
        self.assertEqual(set(cameras), {"MapCamera00", "MapCamera01", "MapCamera02"})
        expected = {
            "MapCamera00": ((-983040, -851968, 655360), 100),
            "MapCamera01": ((-65536, -983040, 589824), 95),
            "MapCamera02": ((851968, -786432, 720896), 100),
        }
        for name, (position, fov) in expected.items():
            camera = cameras[name]
            actual = camera["localTransform"]["Position"]
            self.assertEqual(
                (
                    actual["x"]["Bits"],
                    actual["y"]["Bits"],
                    actual["z"]["Bits"],
                ),
                position,
            )
            self.assertEqual(camera["fov"], fov)
            self.assertEqual(camera["nearPlaneOverride"], 1)
            self.assertEqual(camera["farPlaneOverride"], 25)

        material = load(helper_root / "gqt005_bdview.mi.json")["Data"]["RootChunk"]
        parameters = {
            key: value
            for value in material["values"]
            for key in value
            if key != "$type"
        }
        self.assertEqual(
            parameters["RevealMaskBoundsMin"]["RevealMaskBoundsMin"],
            {
                "$type": "Vector4",
                "X": -1088.8691,
                "Y": 1303.3234,
                "Z": 3.674843,
                "W": 0,
            },
        )
        self.assertEqual(
            parameters["RevealMaskBoundsMax"]["RevealMaskBoundsMax"],
            {
                "$type": "Vector4",
                "X": -1067.6435,
                "Y": 1324.549,
                "Z": 13.174843,
                "W": 0,
            },
        )

    def test_bd_clue_targets_own_the_vanilla_scanning_contract(self) -> None:
        helper_root = ROOT / "source/raw/mod/gqt005/braindance"
        targets = {
            "gqt005_encrypted_shard_clue.ent.json": (
                "Props.GhostlineGQT005BDEncryptedShardClue",
                r"mod\gqt005\braindance\gqt005_encrypted_shard_clue.ent",
                "Default",
                (
                    "scanning.gqt005_encrypted_shard_01",
                    "scanning.gqt005_encrypted_shard_02",
                ),
                "gl_gqt005_bd_clue_encrypted_shard_name",
                1.0,
                (
                    "base\\environment\\decoration\\electronics\\devices\\"
                    "tablet\\tablet_b_kitsch.mesh"
                ),
                None,
            ),
            "gqt005_guard_warning_clue.ent.json": (
                "Props.GhostlineGQT005BDGuardWarningClue",
                r"mod\gqt005\braindance\gqt005_guard_warning_clue.ent",
                "Audio",
                (
                    "scanning.gqt005_guard_warning_01",
                    "scanning.gqt005_guard_warning_02",
                ),
                "gl_gqt005_bd_clue_guard_warning_name",
                2.0,
                None,
                None,
            ),
            "gqt005_guard_implant_heat_clue.ent.json": (
                "Props.GhostlineGQT005BDGuardImplantHeatClue",
                r"mod\gqt005\braindance\gqt005_guard_implant_heat_clue.ent",
                "Thermal",
                (
                    "scanning.gqt005_guard_implant_heat_01",
                    "scanning.gqt005_guard_implant_heat_02",
                ),
                "gl_gqt005_bd_clue_guard_implant_heat_name",
                2.0,
                "base\\items\\quest\\q003__splinter_case\\q003__splinter.mesh",
                (
                    (
                        "thermal_cold",
                        "base\\quest\\main_quests\\prologue\\q004\\entities\\"
                        "temp\\cold_effect.effect",
                        2,
                    ),
                    (
                        "braindanceClueEffect",
                        "base\\quest\\main_quests\\prologue\\q004\\entities\\"
                        "temp\\cold_effect.effect",
                        2,
                    ),
                    (
                        "thermal_hot",
                        "base\\quest\\main_quests\\prologue\\q004\\entities\\"
                        "temp\\hot_effect.effect",
                        1,
                    ),
                ),
            ),
        }
        tweaks = (
            ROOT / "source/resources/r6/tweaks/ghostline/gqt005_braindance.yaml"
        ).read_text(encoding="utf-8")
        generator = (ROOT / "quests/tests/gqt005/implementation/build.py").read_text(
            encoding="utf-8"
        )
        onscreens = load(
            ROOT / "source/raw/mod/gqt005/localization/en-us/onscreens/gqt005.json.json"
        )
        localized = {
            entry["secondaryKey"]: entry["femaleVariant"]
            for entry in onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
        }
        encoded_targets: list[str] = []
        for filename, (
            record,
            depot_path,
            layer,
            clue_records,
            localized_name,
            expected_radius,
            expected_mesh,
            expected_effects,
        ) in targets.items():
            document = load(helper_root / filename)
            encoded_targets.append(json.dumps(document))
            package = document["Data"]["RootChunk"]["compiledData"]["Data"]
            chunks = package["Chunks"]
            types = [chunk["$type"] for chunk in chunks]
            self.assertEqual(types.count("gameScanningComponent"), 1)
            self.assertEqual(types.count("gameVisionModeComponent"), 1)
            self.assertEqual(types.count("gameTargetingComponent"), 1)
            self.assertEqual(types.count("entColliderComponent"), 1)
            self.assertEqual(package["Sections"], len(chunks))
            self.assertEqual(
                list(package["CruidDict"].values()),
                [str(chunk.get("id", "0")) for chunk in chunks],
            )
            mesh_paths = [
                chunk["mesh"]["DepotPath"]["$value"]
                for chunk in chunks
                if "MeshComponent" in chunk["$type"]
            ]
            if expected_mesh is None:
                self.assertEqual(mesh_paths, [])
            else:
                self.assertEqual(mesh_paths, [expected_mesh])

            scanner = next(
                chunk for chunk in chunks if chunk["$type"] == "gameScanningComponent"
            )
            self.assertEqual(
                scanner["persistentState"]["Data"]["$type"],
                "gameScanningComponentPS",
            )
            self.assertEqual(scanner["isBraindanceClue"], 1)
            self.assertEqual(scanner["BraindanceLayer"], layer)
            self.assertEqual(scanner["timeNeeded"], 1.5)
            self.assertEqual(
                scanner["boundingSphere"]["CenterRadius2"]["W"],
                expected_radius,
            )
            self.assertEqual(len(scanner["clues"]), 1)
            clue = scanner["clues"][0]
            self.assertEqual(clue["$type"], "FocusClueDefinition")
            self.assertEqual(clue["isEnabled"], 1)
            self.assertEqual(
                [item["clueRecord"]["$value"] for item in clue["extendedClueRecords"]],
                [
                    str((len(name) << 32) | zlib.crc32(name.encode("utf-8")))
                    for name in clue_records
                ],
            )
            self.assertEqual(
                [item["percentage"] for item in clue["extendedClueRecords"]],
                [0.30000001192092896, 0.699999988079071],
            )

            targeting = next(
                chunk for chunk in chunks if chunk["$type"] == "gameTargetingComponent"
            )
            ui_slots = next(
                chunk for chunk in chunks if chunk["$type"] == "entSlotComponent"
            )
            collider = next(
                chunk for chunk in chunks if chunk["$type"] == "entColliderComponent"
            )
            if layer == "Default":
                self.assertIsNotNone(targeting.get("parentTransform"))
            else:
                self.assertIsNone(targeting.get("parentTransform"))
                self.assertIsNone(ui_slots.get("parentTransform"))
            self.assertEqual(
                collider["colliders"][0]["Data"]["$type"],
                "physicsColliderSphere",
            )
            if layer == "Default":
                self.assertEqual(chunks[0]["$type"], "gameObject")
            elif layer == "Audio":
                self.assertEqual(
                    collider["filterData"]["Data"]["queryFilter"]["mask2"],
                    "2097152",
                )
                self.assertEqual(
                    collider["filterData"]["Data"]["preset"]["$value"],
                    "Interaction Object",
                )
                self.assertEqual(
                    collider["colliders"][0]["Data"]["radius"],
                    0.3,
                )
            else:
                self.assertEqual(
                    collider["filterData"]["Data"]["queryFilter"]["mask2"],
                    "2097152",
                )
                self.assertEqual(
                    collider["filterData"]["Data"]["preset"]["$value"],
                    "Interaction Object",
                )
                self.assertEqual(
                    collider["colliders"][0]["Data"]["radius"],
                    0.5,
                )
            if layer == "Audio":
                self.assertEqual(chunks[0]["$type"], "gameAudioClueObject")
            effect_spawners = [
                chunk
                for chunk in chunks
                if chunk["$type"] == "entEffectSpawnerComponent"
            ]
            if expected_effects is None:
                self.assertEqual(effect_spawners, [])
            else:
                self.assertEqual(len(effect_spawners), 1)
                effects = effect_spawners[0]["effectDescs"]
                self.assertEqual(
                    [
                        (
                            effect["Data"]["effectName"]["$value"],
                            effect["Data"]["effect"]["DepotPath"]["$value"],
                            len(
                                effect["Data"]["compiledEffectInfo"][
                                    "eventsSortedByRUID"
                                ]
                            ),
                        )
                        for effect in effects
                    ],
                    list(expected_effects),
                )
            self.assertIn(record, tweaks)
            self.assertIn(depot_path, tweaks)
            self.assertIn(filename, generator)
            for clue_record in clue_records:
                self.assertIn(
                    f"{clue_record}:\n  $type: gamedataFocusClue_Record",
                    tweaks,
                )
            self.assertIn(localized_name, localized)
            self.assertIn(localized_name, tweaks)
            self.assertIn(localized_name, generator)
        encoded = "\n".join(encoded_targets)
        self.assertNotIn("124162930667", encoded)
        self.assertNotIn("122165831249", encoded)
        self.assertEqual(
            tweaks.count("$type: gamedataFocusClue_Record"),
            6,
        )

    def test_launch_scene_has_repeatable_patch_lipsync_and_braindance_choices(self) -> None:
        scene = load(LAUNCH_SCENE)["Data"]["RootChunk"]
        graph = scene["sceneGraph"]["Data"]["graph"]
        self.assertEqual(
            [node["Data"]["$type"] for node in graph],
            [
                "scnStartNode",
                "scnSectionNode",
                "scnChoiceNode",
                "scnSectionNode",
                "scnSectionNode",
                "scnSectionNode",
                "scnSectionNode",
                "scnEndNode",
            ],
        )
        self.assertEqual(len(scene["actors"]), 1)
        self.assertEqual(scene["actors"][0]["actorName"], "patch")
        self.assertEqual(
            scene["actors"][0]["communityParams"]["forceMaxVisibility"],
            0,
        )
        choice = graph[2]["Data"]
        self.assertEqual(choice["mode"], "attachToActor")
        self.assertEqual(choice["ataParams"]["actorId"]["id"], 0)
        self.assertEqual(len(choice["options"]), 5)
        self.assertEqual(
            [option["caption"]["$value"] for option in choice["options"]],
            [
                "Replay: You made it",
                "Replay: Knew you would",
                "Replay: Pull the cache",
                "Replay: That's the point",
                "Play braindance",
            ],
        )
        self.assertEqual(
            choice["options"][4]["iconTagIds"][0]["$value"],
            "ChoiceCaptionParts.BraindanceIcon",
        )
        self.assertTrue(all(option["isSingleChoice"] == 0 for option in choice["options"][:4]))
        self.assertEqual(choice["options"][4]["isSingleChoice"], 1)
        lines = scene["screenplayStore"]["lines"]
        expected_locstrings = [
            "3552541838326363267",
            "1728179479238269697",
            "1563333104533324901",
            "1855362652331361983",
        ]
        self.assertEqual(
            [line["locstringId"]["ruid"] for line in lines],
            expected_locstrings,
        )
        self.assertEqual(
            [line["itemId"]["id"] for line in lines],
            [1, 257, 513, 769],
        )
        self.assertEqual(
            [
                node["Data"]["events"][0]["Data"]["screenplayLineId"]["id"]
                for node in graph[3:7]
            ],
            [1, 257, 513, 769],
        )
        for node in graph[3:7]:
            events = node["Data"]["events"]
            self.assertEqual(
                [event["Data"]["$type"] for event in events],
                ["scnDialogLineEvent", "scnLookAtEvent"],
            )
            lookat = events[1]["Data"]["basicData"]["basic"]
            self.assertEqual(lookat["performerId"]["id"], 1)
            self.assertEqual(lookat["targetPerformerId"]["id"], 257)
            self.assertEqual(lookat["targetSlot"]["$value"], "pla_default_tgt")
        self.assertEqual(
            [line["femaleLipsyncAnimationName"]["$value"] for line in lines],
            [f"f_{int(locstring):016X}" for locstring in expected_locstrings],
        )
        self.assertEqual(
            [line["maleLipsyncAnimationName"]["$value"] for line in lines],
            [f"f_{int(locstring):016X}" for locstring in expected_locstrings],
        )
        self.assertEqual(len(scene["screenplayStore"]["options"]), 5)
        self.assertEqual(len(scene["locStore"]["vdEntries"]), 20)
        self.assertEqual(scene["actors"][0]["voicetagId"]["id"], "1624173162010260376")
        self.assertEqual(choice["options"][4]["screenplayOptionId"]["id"], 1026)
        self.assertEqual(
            scene["resouresReferences"]["lipsyncAnimSets"][0][
                "asyncRefLipsyncAnimSet"
            ]["DepotPath"]["$value"],
            r"base\localization\en-us\lipsync\mod\gq000\scenes\gq000_patch_meet\civ_low_m_11_enus_40_fat.anims",
        )
        self.assertEqual(
            scene["exitPoints"][0]["name"]["$value"],
            "play_braindance",
        )
        performers = scene["debugSymbols"]["performersDebugSymbols"]
        self.assertEqual(
            [item["performerId"]["id"] for item in performers],
            [1, 257],
        )
        self.assertEqual(
            performers[0]["entityRef"]["reference"]["$value"],
            "#gqt005_com_contact",
        )
        self.assertEqual(
            performers[0]["entityRef"]["dynamicEntityUniqueName"],
            {
                "$type": "CName",
                "$storage": "string",
                "$value": "None",
            },
        )
        self.assertTrue(scene["interruptionScenarios"])
        self.assertTrue(
            all(scenario["enabled"] == 0 for scenario in scene["interruptionScenarios"])
        )

        world_spec = load(
            ROOT
            / "quests/tests/gqt005/implementation/world/braindance-analysis.world.json"
        )
        self.assertEqual(
            world_spec["community"]["spot"]["workspot"],
            r"base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot",
        )

    def test_meet_contact_owns_patch_and_bd_phase_owns_player_handoff(self) -> None:
        meet = load(
            ROOT / "source/raw/mod/gqt005/phases/gqt005_meet_patch.questphase.json"
        )
        review = load(
            ROOT / "source/raw/mod/gqt005/phases/"
            "gqt005_review_braindance.questphase.json"
        )
        meet_encoded = json.dumps(meet)
        review_encoded = json.dumps(review)
        types = {
            item["$type"]
            for item in walk(meet)
            if isinstance(item, dict) and isinstance(item.get("$type"), str)
        }
        self.assertEqual(meet_encoded.count("questSceneNodeDefinition"), 1)
        self.assertIn("questCharacterSpawned_ConditionType", types)
        self.assertIn("questTriggerCondition", types)
        spawned = next(
            item
            for item in walk(meet)
            if isinstance(item, dict)
            and item.get("$type") == "questCharacterSpawned_ConditionType"
        )
        self.assertEqual(
            spawned["comparisonParams"]["Data"]["entireCommunity"],
            1,
        )
        self.assertEqual(spawned["objectRef"]["names"], [])
        self.assertIn("#gqt005_tr_setup", meet_encoded)
        self.assertIn("#gqt005_com_contact", meet_encoded)
        self.assertIn(
            r"mod\\gqt005\\scenes\\gqt005_patch_start.scene",
            meet_encoded,
        )
        self.assertIn('"$value": "play_braindance"', meet_encoded)
        handle_definitions = {
            str(item["HandleId"]): item
            for item in walk(meet)
            if isinstance(item, dict)
            and "HandleId" in item
            and isinstance(item.get("Data"), dict)
        }

        def resolve(wrapper):
            handle_id = wrapper.get(
                "HandleId",
                wrapper.get("HandleRefId"),
            )
            return handle_definitions[str(handle_id)]

        def socket(node, name):
            return next(
                resolve(wrapper)
                for wrapper in node["Data"]["sockets"]
                if (resolve(wrapper)["Data"].get("name", {}).get("$value") == name)
            )

        meet_scene = next(
            item
            for item in meet["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if item["Data"]["$type"] == "questSceneNodeDefinition"
        )
        journal = next(
            item
            for item in meet["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if item["Data"]["$type"] == "questJournalNodeDefinition"
        )
        mappin = next(
            item
            for item in meet["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
            if item["Data"]["$type"] == "questMappinManagerNodeDefinition"
        )
        play = socket(meet_scene, "play_braindance")
        self.assertEqual(len(play["Data"]["connections"]), 1)
        play_connection = resolve(play["Data"]["connections"][0])
        destination = play_connection["Data"]["destination"]
        mappin_inactive = socket(mappin, "Inactive")
        self.assertEqual(
            destination.get(
                "HandleId",
                destination.get("HandleRefId"),
            ),
            mappin_inactive.get(
                "HandleId",
                mappin_inactive.get("HandleRefId"),
            ),
        )
        self.assertEqual(
            socket(journal, "Succeeded")["Data"]["connections"],
            [],
        )
        self.assertEqual(
            socket(journal, "Out")["Data"]["connections"],
            [],
        )
        self.assertEqual(review_encoded.count("questSceneNodeDefinition"), 1)
        self.assertEqual(
            review_encoded.count("questJournalNodeDefinition"),
            5,
        )
        self.assertEqual(
            review_encoded.count("questJournalQuestObjectiveCounter_NodeType"),
            3,
        )
        self.assertEqual(
            review_encoded.count("questFactsDBCondition"),
            3,
        )
        self.assertEqual(
            review_encoded.count("questLogicalAndNodeDefinition"),
            1,
        )
        for fact in (
            "gqt005_bd_encrypted_shard_found",
            "gqt005_bd_guard_warning_found",
            "gqt005_bd_guard_implant_heat_found",
        ):
            self.assertIn(fact, review_encoded)
        self.assertIn("gqt005_completed", review_encoded)
        self.assertNotIn("questCharacterSpawned_ConditionType", review_encoded)
        self.assertNotIn("questSpawnManagerNodeDefinition", review_encoded)
        self.assertNotIn("questReplacer_NodeType", review_encoded)
        self.assertNotIn("questSpawnSet_NodeType", review_encoded)
        self.assertEqual(
            review_encoded.count("questTeleportPuppetNodeDefinition"),
            2,
        )
        self.assertEqual(
            review_encoded.count("questShowWorldNode_NodeType"),
            2,
        )
        self.assertIn("#gqt005_bd_player_hold", review_encoded)
        self.assertNotIn("#gqt005_bd_replacer", review_encoded)
        self.assertIn("#gqt005_bd_player_return", review_encoded)
        self.assertIn("#gqt005_bd_origin", review_encoded)
        self.assertIn(
            r"mod\\gqt005\\scenes\\gqt005_braindance_analysis.scene",
            review_encoded,
        )

    def test_normal_generation_uses_owned_scene_template(self) -> None:
        generator = (ROOT / "quests/tests/gqt005/implementation/build.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("SCENE_TEMPLATE", generator)
        self.assertNotIn("reduce_scene_donor", generator)
        self.assertNotIn("--scene-donor", generator)
        template = load(SCENE_TEMPLATE)["Data"]["RootChunk"]
        self.assertEqual(
            [
                node["Data"]["nodeId"]["id"]
                for node in template["sceneGraph"]["Data"]["graph"]
            ],
            [1, 31, 20, 163, 168, 166, 4576, 527, 28, 34, 2],
        )

    def test_scene_generation_uses_context_player_without_replacer_actor(
        self,
    ) -> None:
        template = load(SCENE_TEMPLATE)
        with (
            mock.patch.object(
                generate_gqt005_content,
                "link_scene_document",
                return_value=(template, {"ok": True}),
            ) as linker,
            mock.patch.object(generate_gqt005_content, "write"),
        ):
            report = generate_gqt005_content.generate_scene(
                SCENE_TEMPLATE,
                SCENE_TEMPLATE,
                SCENE_TEMPLATE,
                wolvenkit=None,
                deserialize_scene=False,
            )

        self.assertEqual(report, {"ok": True})
        self.assertEqual(
            linker.call_args.kwargs["scene_spawn_set_actors"],
            [],
        )

    def test_player_handoff_markers_match_working_bd_layout(self) -> None:
        spec = load(WORLD_SPEC)
        hold = next(
            item for item in spec["markers"] if item["ref"] == "#gqt005_bd_player_hold"
        )
        self.assertEqual(
            hold["position"],
            {"from": "origin"},
        )
        returned = next(
            item
            for item in spec["markers"]
            if item["ref"] == "#gqt005_bd_player_return"
        )
        self.assertEqual(
            returned["position"],
            {"from": "origin", "forward": -3},
        )

    def test_quest_scene_sockets_match_scene_entry_points(self) -> None:
        phases = [
            load(
                ROOT / "source/raw/mod/gqt005/phases/gqt005_meet_patch.questphase.json"
            ),
            load(
                ROOT / "source/raw/mod/gqt005/phases/"
                "gqt005_review_braindance.questphase.json"
            ),
        ]
        scene_nodes = [
            (
                item,
                {
                    wrapper["HandleId"]: wrapper["Data"]
                    for wrapper in walk(phase)
                    if isinstance(wrapper, dict)
                    and "HandleId" in wrapper
                    and isinstance(wrapper.get("Data"), dict)
                },
            )
            for phase in phases
            for item in walk(phase)
            if isinstance(item, dict)
            and item.get("$type") == "questSceneNodeDefinition"
        ]
        scenes = {
            r"mod\gqt005\scenes\gqt005_patch_start.scene": load(LAUNCH_SCENE),
            r"mod\gqt005\scenes\gqt005_braindance_analysis.scene": load(SCENE),
        }
        for scene_node, handles in scene_nodes:
            depot = scene_node["sceneFile"]["DepotPath"]["$value"]
            sockets = [
                socket.get("Data") or handles[socket["HandleRefId"]]
                for socket in scene_node["sockets"]
            ]
            input_sockets = {
                socket["name"]["$value"]
                for socket in sockets
                if socket.get("type") == "Input"
            }
            entry_points = {
                entry["name"]["$value"]
                for entry in scenes[depot]["Data"]["RootChunk"]["entryPoints"]
            }
            self.assertEqual(input_sockets, {"start"})
            self.assertEqual(entry_points, input_sockets)

    def test_all_registered_gqt005_binaries_are_cr2w(self) -> None:
        expected = [
            ROOT / "source/archive/mod/gqt005/braindance/"
            "gqt005_braindance_analysis.scenerid",
            ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdview.ent",
            ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdfog.ent",
            ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdsetup.ent",
            ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdview.mesh",
            ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdview.mi",
            ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdfog.mesh",
            ROOT / "source/archive/mod/gqt005/braindance/gqt005_reveal_mask.xbm",
            ROOT / "source/archive/mod/gqt005/braindance/gqt005_clues_data.xbm",
            ROOT / "source/archive/mod/gqt005/scenes/gqt005_braindance_analysis.scene",
            ROOT / "source/archive/mod/gqt005/scenes/gqt005_patch_start.scene",
            ROOT / "source/archive/mod/gqt005/phases/"
            "gqt005_braindance_analysis.questphase",
            ROOT / "source/archive/mod/gqt005/phases/gqt005_approach_patch.questphase",
            ROOT / "source/archive/mod/gqt005/phases/gqt005_meet_patch.questphase",
            ROOT / "source/archive/mod/gqt005/phases/"
            "gqt005_review_braindance.questphase",
            ROOT / "source/archive/mod/gqt005/journal/gqt005.journal",
            ROOT / "source/archive/mod/gqt005/localization/en-us/onscreens/gqt005.json",
            ROOT / "source/archive/mod/gqt005/world/"
            "gqt005_braindance_analysis.streamingblock",
            ROOT / "source/archive/mod/gqt005/world/"
            "gqt005_braindance_analysis.streamingsector",
            ROOT / "source/archive/mod/gqt005/world/"
            "gqt005_always_loaded.streamingsector",
        ]
        for path in expected:
            with self.subTest(path=path):
                self.assertEqual(path.read_bytes()[:4], b"CR2W")

    def test_world_owns_origin_patch_and_player_handoff_markers(self) -> None:
        always = load(
            ROOT / "source/raw/mod/gqt005/world/"
            "gqt005_always_loaded.streamingsector.json"
        )["Data"]["RootChunk"]
        sector = load(
            ROOT / "source/raw/mod/gqt005/world/"
            "gqt005_braindance_analysis.streamingsector.json"
        )["Data"]["RootChunk"]
        self.assertEqual(len(always["nodes"]), 5)
        self.assertEqual(len(always["nodeData"]["Data"]), 5)
        self.assertEqual(len(always["nodeRefs"]), 4)
        registries = [
            node["Data"]
            for node in always["nodes"]
            if node["Data"]["$type"] == "worldCommunityRegistryNode"
        ]
        self.assertEqual(len(registries), 1)
        for registry in registries:
            states = registry["communitiesData"][0]["entriesInitialState"]
            self.assertEqual(
                [state["entryActiveOnStart"] for state in states],
                [0],
            )
        self.assertEqual(len(sector["nodes"]), 5)
        self.assertEqual(len(sector["nodeData"]["Data"]), 5)
        self.assertEqual(len(sector["nodeRefs"]), 5)
        encoded = json.dumps([always, sector])
        self.assertIn("#gqt005_pr_braindance_analysis", encoded)
        self.assertIn("#gqt005_bd_origin", encoded)
        self.assertIn("#gqt005_bdview_spawner", encoded)
        self.assertIn("#gqt005_bd_player_hold", encoded)
        self.assertIn("#gqt005_bd_player_return", encoded)
        self.assertNotIn("#gqt005_bd_replacer", encoded)
        self.assertNotIn("#gqt005_com_bd_replacer", encoded)
        self.assertNotIn("#gqt005_ws_bd_replacer", encoded)
        self.assertIn("#gqt005_com_contact", encoded)
        self.assertIn("Character.GhostlinePatchLipsyncTest", encoded)
        tweak = (
            ROOT / "source/resources/r6/tweaks/ghostline/gqt005_lipsync.yaml"
        ).read_text(encoding="utf-8")
        self.assertIn("$base: Character.GhostlinePatch", tweak)
        self.assertIn("voiceTag: civ_low_m_11_enus_40_fat", tweak)
        self.assertIn("#gqt005_tr_wake", encoded)
        self.assertIn("#gqt005_tr_setup", encoded)
        self.assertIn("#gqt005_bd_camera", encoded)
        camera = next(
            node["Data"]
            for node in sector["nodes"]
            if node["Data"].get("debugName", {}).get("$value") == "{gqt005_bd_camera}"
        )
        self.assertEqual(camera["$type"], "worldEntityNode")
        self.assertEqual(
            camera["entityTemplate"]["DepotPath"]["$value"],
            r"engine\scenesystem\camera.ent",
        )
        origin_index = next(
            index
            for index, node in enumerate(always["nodes"])
            if node["Data"].get("debugName", {}).get("$value") == "{gqt005_bd_origin}"
        )
        origin = always["nodes"][origin_index]["Data"]
        self.assertEqual(origin["data"]["Data"]["$type"], "scnSceneMarker")
        self.assertEqual(
            [
                entry["startName"]["$value"]
                for entry in origin["data"]["Data"]["markers"]
            ],
            ["268435782_start", "268435791_start"],
        )
        spawner_index = next(
            index
            for index, node in enumerate(always["nodes"])
            if node["Data"].get("debugName", {}).get("$value")
            == "{gqt005_bdview_spawner}"
        )
        spawner = always["nodes"][spawner_index]["Data"]
        self.assertEqual(spawner["$type"], "worldStaticMarkerNode")
        self.assertEqual(
            spawner["data"]["Data"],
            {
                "$type": "scnSceneMarker",
                "markers": [],
                "workspotMarkers": [],
            },
        )
        placement = next(
            item
            for item in always["nodeData"]["Data"]
            if item["NodeIndex"] == spawner_index
        )
        origin_placement = next(
            item
            for item in always["nodeData"]["Data"]
            if item["NodeIndex"] == origin_index
        )
        self.assertEqual(
            placement["QuestPrefabRefHash"]["$value"],
            "$/mod/gqt005/#gqt005_pr_braindance_analysis/#gqt005_bdview_spawner",
        )
        self.assertEqual(
            placement["Orientation"],
            origin_placement["Orientation"],
        )
        self.assertEqual(placement["MaxStreamingDistance"], 3856.41016)
        self.assertEqual(placement["UkFloat1"], 512.0)
        self.assertEqual(placement["Uk10"], 1056)
        self.assertEqual(placement["Uk11"], 512)
        self.assertAlmostEqual(placement["Position"]["X"], -1078.2563, places=5)
        self.assertAlmostEqual(placement["Position"]["Y"], 1313.9362, places=5)
        self.assertAlmostEqual(placement["Position"]["Z"], 5.174843, places=5)
        marker_types = {
            node["Data"].get("debugName", {}).get("$value"): node["Data"]
            .get("data", {})
            .get("Data", {})
            .get("$type")
            for node in always["nodes"]
        }
        self.assertEqual(
            marker_types["{gqt005_bd_player_hold}"],
            None,
        )
        self.assertEqual(
            marker_types["{gqt005_bd_player_return}"],
            None,
        )
        self.assertNotIn("GQT004", encoded)
        self.assertNotIn("vehicle_lab", encoded)

    def test_archive_xl_activates_gqt005_and_not_older_test_quests(self) -> None:
        config = (ROOT / "source/resources/Ghostline.archive.xl").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            r"mod\gqt005\phases\gqt005_braindance_analysis.questphase",
            config,
        )
        self.assertIn(
            r"mod\gqt005\world\gqt005_braindance_analysis.streamingblock",
            config,
        )
        for old in ("gqt001", "gqt002", "gqt003", "gqt004"):
            self.assertNotIn(old, config)


if __name__ == "__main__":
    unittest.main()
