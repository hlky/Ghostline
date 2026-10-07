from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

SPEC = importlib.util.spec_from_file_location(
    "generate_scene", TOOLS / "generate_scene.py"
)
assert SPEC is not None
generate_scene = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["generate_scene"] = generate_scene
SPEC.loader.exec_module(generate_scene)


class GenerateSceneTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec = generate_scene.load_json(
            ROOT / "projects/ghostline/quests/gq000/implementation/scenes/"
            "patch-meet.scene-spec.json"
        )
        cls.scene = generate_scene.build_scene(cls.spec)
        cls.raw_scene = generate_scene.load_json(ROOT / cls.spec["raw_path"])
        cls.root = cls.scene["Data"]["RootChunk"]

    def test_checked_in_raw_scene_matches_generator(self) -> None:
        self.assertEqual(self.raw_scene, self.scene)
        self.assertEqual(generate_scene.validate_scene(self.raw_scene, self.spec), [])

    def test_fixture_shape(self) -> None:
        self.assertEqual(
            self.scene["Header"]["ExportedDateTime"], self.spec["exported_datetime"]
        )
        self.assertEqual(len(self.root["actors"]), 1)
        self.assertEqual(len(self.root["playerActors"]), 1)
        self.assertEqual(len(self.root["sceneGraph"]["Data"]["graph"]), 15)
        edge_count = sum(
            len(socket.get("destinations", []))
            for node in self.root["sceneGraph"]["Data"]["graph"]
            for socket in node["Data"].get("outputSockets", [])
        )
        self.assertEqual(edge_count, 16)
        self.assertEqual(len(self.root["screenplayStore"]["lines"]), 13)
        self.assertEqual(len(self.root["screenplayStore"]["options"]), 5)
        self.assertTrue(
            any(
                point["name"]["$value"] == "start" for point in self.root["entryPoints"]
            )
        )
        self.assertTrue(
            any(
                point["name"]["$value"] == "job_accept"
                for point in self.root["exitPoints"]
            )
        )

    def test_patch_looks_at_v_throughout_each_dialogue_section(self) -> None:
        sections = [node["Data"] for node in self.root["sceneGraph"]["Data"]["graph"]
                    if node["Data"]["$type"] == "scnSectionNode"]
        self.assertEqual(len(sections), len(self.spec["sections"]))
        for section in sections:
            events = [event["Data"] for event in section["events"]
                      if event["Data"]["$type"] == "scnLookAtEvent"]
            self.assertEqual(len(events), 1)
            event = events[0]
            self.assertEqual(event["duration"], section["sectionDuration"]["stu"])
            self.assertEqual(event["startTime"], 0)
            basic = event["basicData"]["basic"]
            self.assertEqual(basic["performerId"]["id"], 1)
            self.assertEqual(basic["targetPerformerId"]["id"], 257)
            self.assertEqual(basic["targetSlot"]["$value"], "camera")

    def test_fixture_uses_one_shared_lipsync_slot_for_crash_isolation(self) -> None:
        patch_lipsync = self.root["actors"][0]["lipsyncAnimSet"]["id"]
        player_lipsync = self.root["playerActors"][0]["lipsyncAnimSet"]["id"]
        lipsync_refs = self.root["resouresReferences"]["lipsyncAnimSets"]

        self.assertEqual((patch_lipsync, player_lipsync), (0, 0))
        self.assertEqual(len(lipsync_refs), 1)

    def test_validation_rejects_lost_actor_voice_tags(self) -> None:
        for group in ("actors", "playerActors"):
            with self.subTest(group=group):
                scene = copy.deepcopy(self.scene)
                scene["Data"]["RootChunk"][group][0]["voicetagId"]["id"] = "0"
                self.assertTrue(any("voicetag mismatch" in error for error in generate_scene.validate_scene(scene, self.spec)))

    def test_failed_scene_readback_preserves_the_previous_packed_resource(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw, binary = root / "probe.scene.json", root / "probe.scene"
            raw.write_text("{}", encoding="utf-8")
            binary.write_bytes(b"CR2Wprevious")
            with mock.patch("quest_build.convert_resource", side_effect=RuntimeError("voice tag lost")):
                with self.assertRaisesRegex(generate_scene.SceneBuildError, "voice tag lost"):
                    generate_scene.deserialize({"raw_path": str(raw), "archive_path": str(binary)}, root / "red", root / "schema")
            self.assertEqual(binary.read_bytes(), b"CR2Wprevious")

    def test_fixture_graph_matches_mq003_shaped_scene_order(self) -> None:
        node_ids = [
            node["Data"]["nodeId"]["id"]
            for node in self.root["sceneGraph"]["Data"]["graph"]
        ]
        self.assertEqual(node_ids, [1, 10, 11, 13, 2, 22, 8, 3, 4, 5, 9, 6, 7, 18, 19])

    def test_fixture_dialogue_flow_edges(self) -> None:
        edges = []
        for node in self.root["sceneGraph"]["Data"]["graph"]:
            source = node["Data"]["nodeId"]["id"]
            for socket in node["Data"].get("outputSockets", []):
                for destination in socket.get("destinations", []):
                    edges.append(
                        (
                            source,
                            destination["nodeId"]["id"],
                            destination["isockStamp"]["ordinal"],
                        )
                    )
        self.assertEqual(
            edges,
            [
                (1, 10, 1),
                (1, 11, 1),
                (11, 13, 1),
                (13, 2, 0),
                (2, 22, 1),
                (22, 8, 0),
                (8, 3, 0),
                (8, 4, 0),
                (8, 5, 0),
                (3, 8, 0),
                (4, 8, 0),
                (5, 9, 0),
                (9, 6, 0),
                (9, 7, 0),
                (6, 9, 0),
                (7, 19, 0),
            ],
        )

    def test_fixture_keeps_engage_as_scene_local_final_gate(self) -> None:
        engage = next(
            node["Data"]
            for node in self.root["sceneGraph"]["Data"]["graph"]
            if node["Data"]["nodeId"]["id"] == 22
        )
        quest_node = engage["questNode"]["Data"]
        condition = quest_node["condition"]["Data"]

        self.assertEqual(quest_node["$type"], "questPauseConditionNodeDefinition")
        self.assertEqual(condition["$type"], "questTriggerCondition")
        self.assertEqual(condition["triggerAreaRef"]["$value"], "#gq000_01_tr_engage")

    def test_screenplay_ids_use_vanilla_pattern(self) -> None:
        line_ids = [
            line["itemId"]["id"] for line in self.root["screenplayStore"]["lines"]
        ]
        option_ids = [
            option["itemId"]["id"] for option in self.root["screenplayStore"]["options"]
        ]
        self.assertEqual(
            line_ids,
            [1, 257, 513, 769, 1025, 1281, 1537, 1793, 2049, 2305, 2561, 2817, 3073],
        )
        self.assertEqual(option_ids, [2, 258, 514, 770, 1026])

    def test_spoken_line_can_select_an_explicit_lipsync_animation(self) -> None:
        spec = copy.deepcopy(self.spec)
        manifest = generate_scene.load_json(ROOT / spec["manifest"])
        line = manifest["spoken_lines"][0]
        line["female_lipsync_animation"] = "gqt007_modified"
        line["male_lipsync_animation"] = "gqt007_modified"

        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = Path(tmp) / "manifest.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            spec["manifest"] = str(manifest_path)
            scene = generate_scene.build_scene(spec)

        screenplay_line = scene["Data"]["RootChunk"]["screenplayStore"]["lines"][0]
        self.assertEqual(
            screenplay_line["femaleLipsyncAnimationName"]["$value"],
            "gqt007_modified",
        )
        self.assertEqual(
            screenplay_line["maleLipsyncAnimationName"]["$value"],
            "gqt007_modified",
        )

    def test_fixture_choice_node_has_padded_sockets_and_locstore_entries(self) -> None:
        choices = [
            node["Data"]
            for node in self.root["sceneGraph"]["Data"]["graph"]
            if node["Data"]["$type"] == "scnChoiceNode"
        ]
        self.assertEqual(len(choices), 2)
        self.assertEqual(
            [socket["stamp"]["name"] for socket in choices[0]["outputSockets"]],
            [0, 0, 0, 1, 2, 3, 4, 5, 6],
        )
        self.assertEqual(
            [socket["stamp"]["name"] for socket in choices[1]["outputSockets"]],
            [0, 0, 1, 2, 3, 4, 5, 6],
        )
        self.assertEqual(
            [option["isSingleChoice"] for option in choices[0]["options"]], [0, 0, 0]
        )
        self.assertEqual(
            [option["isSingleChoice"] for option in choices[1]["options"]], [0, 0]
        )
        self.assertEqual(
            [option["type"]["properties"] for option in choices[0]["options"]],
            [0, 0, 1],
        )
        self.assertEqual(
            [option["type"]["properties"] for option in choices[1]["options"]], [0, 1]
        )
        self.assertEqual(len(self.root["locStore"]["vdEntries"]), 20)
        self.assertEqual(len(self.root["locStore"]["vpEntries"]), 20)
        first_choice_locstring = self.root["screenplayStore"]["options"][0][
            "locstringId"
        ]["ruid"]
        first_choice_rows = [
            entry
            for entry in self.root["locStore"]["vdEntries"]
            if entry["locstringId"]["ruid"] == first_choice_locstring
        ]
        self.assertEqual(
            [entry["localeId"] for entry in first_choice_rows],
            ["db_db", "db_db", "pl_pl", "en_us"],
        )
        self.assertEqual(
            self.root["locStore"]["vpEntries"][first_choice_rows[0]["vpeIndex"]][
                "content"
            ],
            "",
        )

    def test_choice_option_supports_vanilla_icon_tags(self) -> None:
        option = generate_scene.build_choice_option(
            {
                "caption": "Play braindance",
                "icon_tags": ["ChoiceCaptionParts.BraindanceIcon"],
            },
            2,
        )
        self.assertEqual(
            option["iconTagIds"],
            [
                {
                    "$type": "TweakDBID",
                    "$storage": "string",
                    "$value": "ChoiceCaptionParts.BraindanceIcon",
                }
            ],
        )

    def test_fixture_choice_locstore_ids_are_sorted_within_locale_blocks(self) -> None:
        descriptors = self.root["locStore"]["vdEntries"]

        for locale in self.spec["choice_locales"]:
            locstring_ids = [
                int(entry["locstringId"]["ruid"])
                for entry in descriptors
                if entry["localeId"] == locale
            ]
            self.assertEqual(locstring_ids, sorted(locstring_ids), locale)

    def test_validation_passes_and_event_ids_are_not_placeholders(self) -> None:
        self.assertEqual(generate_scene.validate_scene(self.scene, self.spec), [])
        event_ids = []
        for node in self.root["sceneGraph"]["Data"]["graph"]:
            for event in node["Data"].get("events", []):
                event_ids.append(event["Data"]["id"]["id"])
        self.assertEqual(len(event_ids), len(set(event_ids)))
        self.assertNotIn(generate_scene.MAX_INT64, event_ids)

    def test_rid_resources_use_synchronous_default_references(self) -> None:
        spec = copy.deepcopy(self.spec)
        spec["rid_resources"] = [
            {
                "resource_id": 123,
                "path": (
                    "base\\animations\\quest\\lore\\generic_sex\\intercourse\\"
                    "sex_06_5s_m.scenerid"
                ),
            }
        ]
        scene = generate_scene.build_scene(spec)
        rid_resource = scene["Data"]["RootChunk"]["ridResources"][0][
            "ridResource"
        ]

        self.assertEqual(rid_resource["Flags"], "Default")
        self.assertEqual(generate_scene.validate_scene(scene, spec), [])

        rid_resource["Flags"] = "Soft"
        errors = generate_scene.validate_scene(scene, spec)
        self.assertTrue(
            any("synchronous Default reference" in error for error in errors),
            errors,
        )

    def test_scene_can_acquire_a_world_camera_prop(self) -> None:
        spec = copy.deepcopy(self.spec)
        spec["props"] = [
            {
                "id": 0,
                "name": "test_camera",
                "node_ref": "#test_scene_camera",
            }
        ]

        scene = generate_scene.build_scene(spec)
        root = scene["Data"]["RootChunk"]
        prop = root["props"][0]
        performer = root["debugSymbols"]["performersDebugSymbols"][-1]

        self.assertEqual(prop["$type"], "scnPropDef")
        self.assertEqual(prop["entityAcquisitionPlan"], "findInNode")
        self.assertEqual(
            prop["findEntityInNodeParams"]["nodeRef"]["$value"],
            "#test_scene_camera",
        )
        self.assertEqual(performer["performerId"]["id"], 2)
        self.assertEqual(
            performer["entityRef"]["reference"]["$value"],
            "#test_scene_camera",
        )
        self.assertEqual(generate_scene.validate_scene(scene, spec), [])

    def test_fpp_rid_event_supports_gender_specific_transition_angles(self) -> None:
        event = generate_scene.rid_anim_event(
            "test_scene",
            "test_section",
            0,
            {
                "actor": "v",
                "component": "body",
                "anim_ref_id": 0,
                "origin": "#test_origin",
                "duration_ms": 5000,
                "fpp": True,
                "fpp_gender_params": {
                    "gender_masks": [2, 1],
                    "transition_blend_in_trajectory_space_angles": [
                        {"pitch": 1, "roll": 2, "yaw": 3}
                    ],
                    "transition_end_input_angles": [
                        {"pitch": 4, "roll": 5, "yaw": 6}
                    ],
                },
            },
            generate_scene.actor_lookup(self.spec),
            generate_scene.HandleAllocator(),
        )["Data"]

        self.assertEqual(
            [value["genderMask"]["mask"] for value in event["genderSpecificParams"]],
            [2, 1],
        )
        self.assertEqual(
            event["genderSpecificParams"][0][
                "transitionBlendInTrajectorySpaceAngles"
            ][0]["Yaw"],
            3.0,
        )

    def test_section_supports_a_regular_world_camera_event(self) -> None:
        event = generate_scene.camera_event(
            "test_scene",
            "test_section",
            {
                "camera_ref": "#test_side_camera",
                "duration_ms": 2000,
                "start_time_ms": 100,
                "blend_time_seconds": 0.25,
            },
            generate_scene.HandleAllocator(),
        )["Data"]

        self.assertEqual(event["$type"], "scneventsCameraEvent")
        self.assertEqual(event["cameraRef"]["$value"], "#test_side_camera")
        self.assertEqual(event["duration"], 2000)
        self.assertEqual(event["startTime"], 100)
        self.assertEqual(event["isBlendIn"], 1)
        self.assertEqual(event["blendTime"], 0.25)

    def test_world_camera_hard_cut_uses_vanilla_blend_in_event(self) -> None:
        event = generate_scene.camera_event(
            "test_scene",
            "test_section",
            {
                "camera_ref": "#test_side_camera",
                "duration_ms": 2000,
            },
            generate_scene.HandleAllocator(),
        )["Data"]

        self.assertEqual(event["isBlendIn"], 1)
        self.assertEqual(event["blendTime"], 0.0)

    def test_world_camera_can_be_explicitly_released(self) -> None:
        event = generate_scene.camera_event(
            "test_scene",
            "test_section",
            {
                "camera_ref": "#test_side_camera",
                "duration_ms": 50,
                "blend_in": False,
            },
            generate_scene.HandleAllocator(),
        )["Data"]

        self.assertEqual(event["isBlendIn"], 0)
        self.assertEqual(event["blendTime"], 0.0)

    def test_world_camera_rejects_invalid_timing(self) -> None:
        for timing, message in (
            ({"duration_ms": 0}, "duration_ms must be positive"),
            (
                {"duration_ms": 2000, "blend_time_seconds": -0.1},
                "blend_time_seconds cannot be negative",
            ),
        ):
            with self.subTest(timing=timing):
                with self.assertRaisesRegex(generate_scene.SceneBuildError, message):
                    generate_scene.camera_event(
                        "test_scene",
                        "test_section",
                        {"camera_ref": "#test_side_camera", **timing},
                        generate_scene.HandleAllocator(),
                    )

    def test_section_rejects_competing_rid_and_world_cameras(self) -> None:
        spec = copy.deepcopy(self.spec)
        section = spec["sections"][0]
        section["rid_camera"] = {
            "camera_ref_id": 0,
            "origin": "#test_origin",
            "camera_ref": "#test_camera",
            "duration_ms": 2000,
        }
        section["camera_event"] = {
            "camera_ref": "#test_side_camera",
            "duration_ms": 2000,
        }

        with self.assertRaisesRegex(
            generate_scene.SceneBuildError,
            "cannot declare both rid_camera and camera_event",
        ):
            generate_scene.build_scene(spec)

    def test_character_gender_node_matches_vanilla_condition_branch(self) -> None:
        node = generate_scene.build_quest_node(
            {
                "kind": "character_gender",
                "node_id": 62,
                "gender": "Male",
                "on_true": [{"node_id": 64}],
                "on_false": [{"node_id": 63}],
            },
            generate_scene.HandleAllocator(),
        )["Data"]
        quest = node["questNode"]["Data"]
        condition = quest["condition"]["Data"]
        gender = condition["type"]["Data"]

        self.assertEqual(node["$type"], "scnQuestNode")
        self.assertEqual(
            [mapping["$value"] for mapping in node["osockMappings"]],
            ["True", "False"],
        )
        self.assertEqual(
            [
                socket["destinations"][0]["nodeId"]["id"]
                for socket in node["outputSockets"]
            ],
            [64, 63],
        )
        self.assertEqual(
            [
                (
                    socket["destinations"][0]["isockStamp"]["name"],
                    socket["destinations"][0]["isockStamp"]["ordinal"],
                )
                for socket in node["outputSockets"]
            ],
            [(0, 0), (0, 0)],
        )
        self.assertEqual(quest["$type"], "questConditionNodeDefinition")
        self.assertEqual(condition["$type"], "questCharacterCondition")
        self.assertEqual(gender["$type"], "questCharacterGender_CondtionType")
        self.assertEqual(gender["gender"]["$value"], "Male")
        self.assertEqual(gender["isPlayer"], 1)
        self.assertEqual(gender["objectRef"]["reference"]["$value"], "0")
        self.assertEqual(
            [socket["Data"]["name"]["$value"] for socket in quest["sockets"]],
            ["CutDestination", "In", "True", "False"],
        )

    def test_scene_quest_nodes_support_vanilla_sex_handoff_controls(self) -> None:
        alloc = generate_scene.HandleAllocator()
        tier = generate_scene.build_quest_node(
            {
                "kind": "scene_tier",
                "node_id": 100,
                "tier": "Tier4_FPPCinematic",
                "force_empty_hands": True,
            },
            alloc,
        )["Data"]["questNode"]["Data"]
        unequip = generate_scene.build_quest_node(
            {"kind": "unequip_player", "node_id": 101},
            alloc,
        )["Data"]["questNode"]["Data"]
        actor_unequip = generate_scene.build_quest_node(
            {
                "kind": "unequip_actor",
                "node_id": 103,
                "entity_ref": "#test_community",
                "entry": "test_actor",
                "by_item": True,
                "item_id": "Items.Preset_Katana_E3",
                "slot_id": "AttachmentSlots.WeaponRight",
                "unequip_types": "AllItems",
                "instant": True,
            },
            alloc,
        )["Data"]["questNode"]["Data"]
        delay = generate_scene.build_quest_node(
            {
                "kind": "realtime_delay",
                "node_id": 104,
                "milliseconds": 100,
            },
            alloc,
        )["Data"]["questNode"]["Data"]
        fade = generate_scene.build_quest_node(
            {
                "kind": "render_fade",
                "node_id": 105,
                "fade_in": False,
                "duration_seconds": 0.25,
            },
            alloc,
        )["Data"]["questNode"]["Data"]
        knockdown = generate_scene.build_quest_node(
            {
                "kind": "player_status_effect",
                "node_id": 102,
                "status_effect": "BaseStatusEffect.Knockdown",
            },
            alloc,
        )["Data"]["questNode"]["Data"]

        self.assertEqual(tier["type"]["Data"]["tier"], "Tier4_FPPCinematic")
        self.assertEqual(tier["type"]["Data"]["forceEmptyHands"], 1)
        self.assertEqual(unequip["params"]["Data"]["unequipTypes"], "AllWeapons")
        self.assertEqual(unequip["params"]["Data"]["isPlayer"], 1)
        actor_ref = actor_unequip["entityReference"]["Data"]
        actor_params = actor_unequip["params"]["Data"]
        self.assertEqual(actor_ref["refLocalPlayer"], 0)
        self.assertEqual(
            actor_ref["entityReference"]["reference"]["$value"],
            "#test_community",
        )
        self.assertEqual(
            [value["$value"] for value in actor_ref["entityReference"]["names"]],
            ["test_actor"],
        )
        self.assertEqual(actor_params["isPlayer"], 0)
        self.assertEqual(actor_params["byItem"], 1)
        self.assertEqual(actor_params["itemId"]["$value"], "Items.Preset_Katana_E3")
        self.assertEqual(
            actor_params["slotId"]["$value"], "AttachmentSlots.WeaponRight"
        )
        self.assertEqual(actor_params["unequipTypes"], "AllItems")
        self.assertEqual(actor_params["instant"], 1)
        delay_type = delay["condition"]["Data"]["type"]["Data"]
        self.assertEqual(delay_type["$type"], "questRealtimeDelay_ConditionType")
        self.assertEqual(delay_type["miliseconds"], 100)
        fade_type = fade["type"]["Data"]
        self.assertEqual(fade["$type"], "questRenderFxManagerNodeDefinition")
        self.assertEqual(fade_type["$type"], "questSetFadeInOut_NodeType")
        self.assertEqual(fade_type["fadeIn"], 0)
        self.assertEqual(fade_type["duration"], 0.25)
        self.assertEqual(
            fade_type["fadeColor"],
            {"$type": "Color", "Alpha": 0, "Blue": 0, "Green": 0, "Red": 0},
        )
        self.assertEqual(
            knockdown["type"]["Data"]["subtype"]["Data"]["statusEffectID"][
                "$value"
            ],
            "BaseStatusEffect.Knockdown",
        )

    def test_spawn_actor_uses_vanilla_cutscene_replica_shape(self) -> None:
        spec = copy.deepcopy(self.spec)
        spec["actors"].append(
            {
                "key": "v_tpp_female",
                "name": "V TPP Female",
                "kind": "spawn",
                "id": 2,
                "record": "Character.TPP_Player_Cutscene_Female",
                "dynamic_name": "a_test_v_tpp_female",
                "spawn_marker": "#test_scene_marker",
                "rid_anim_sets": [0],
                "rid_facial_anim_sets": [0],
            }
        )
        spec["rid_anim_sets"] = [{"animations": [0, 2]}]
        spec["rid_facial_anim_sets"] = [{"animations": [1]}]

        scene = generate_scene.build_scene(spec)
        root = scene["Data"]["RootChunk"]
        actor = root["actors"][-1]
        performer = root["debugSymbols"]["performersDebugSymbols"][2]

        self.assertEqual(actor["acquisitionPlan"], "spawnDespawn")
        self.assertEqual(
            actor["spawnDespawnParams"]["specRecordId"]["$value"],
            "Character.TPP_Player_Cutscene_Female",
        )
        self.assertEqual(actor["spawnDespawnParams"]["spawnOnStart"], 1)
        self.assertEqual(actor["spawnDespawnParams"]["alwaysSpawned"], 0)
        self.assertEqual(actor["spawnDespawnParams"]["forceMaxVisibility"], 0)
        self.assertEqual(
            actor["communityParams"],
            {
                "$type": "scnCommunityParams",
                "entryName": {"$type": "CName", "$storage": "string", "$value": "None"},
                "forceMaxVisibility": 0,
                "reference": {"$type": "NodeRef", "$storage": "uint64", "$value": "0"},
            },
        )
        self.assertEqual(
            actor["spawnDespawnParams"]["dynamicEntityUniqueName"]["$value"],
            "a_test_v_tpp_female",
        )
        self.assertEqual(actor["animSets"], [{"$type": "scnSRRefId", "id": 0}])
        self.assertEqual(
            actor["facialAnimSets"],
            [{"$type": "scnRidFacialAnimSetSRRefId", "id": 0}],
        )
        self.assertEqual(
            performer["entityRef"]["dynamicEntityUniqueName"]["$value"],
            "a_test_v_tpp_female",
        )
        self.assertEqual(
            root["resouresReferences"]["ridAnimSets"][0]["animations"],
            [
                {"$type": "scnSRRefId", "id": 0},
                {"$type": "scnSRRefId", "id": 2},
            ],
        )
        self.assertEqual(
            root["resouresReferences"]["ridFacialAnimSets"][0]["animations"],
            [{"$type": "scnSRRefId", "id": 1}],
        )
        self.assertEqual(generate_scene.validate_scene(scene, spec), [])

    def test_spawn_wait_and_player_visibility_nodes_match_vanilla(self) -> None:
        alloc = generate_scene.HandleAllocator()
        activate = generate_scene.build_quest_node(
            {
                "kind": "spawn_actor",
                "node_id": 103,
                "dynamic_name": "a_test_v_tpp_female",
                "action": "Activate",
            },
            alloc,
        )["Data"]["questNode"]["Data"]
        wait = generate_scene.build_quest_node(
            {
                "kind": "wait_actor_spawned",
                "node_id": 104,
                "dynamic_name": "a_test_v_tpp_female",
            },
            alloc,
        )["Data"]["questNode"]["Data"]
        hide = generate_scene.build_quest_node(
            {"kind": "show_player", "node_id": 105, "show": False},
            alloc,
        )["Data"]["questNode"]["Data"]

        action = activate["actions"][0]["type"]["Data"]
        self.assertEqual(activate["$type"], "questSpawnManagerNodeDefinition")
        self.assertEqual(action["$type"], "questScene_NodeType")
        self.assertEqual(action["action"], "Activate")
        self.assertEqual(
            action["entityReference"]["dynamicEntityUniqueName"]["$value"],
            "a_test_v_tpp_female",
        )

        condition = wait["condition"]["Data"]["type"]["Data"]
        self.assertEqual(condition["$type"], "questCharacterSpawned_ConditionType")
        self.assertEqual(
            condition["comparisonParams"]["Data"]["comparisonType"], "Greater"
        )
        self.assertEqual(condition["comparisonParams"]["Data"]["count"], 0)

        visibility = hide["type"]["Data"]
        self.assertEqual(hide["$type"], "questWorldDataManagerNodeDefinition")
        self.assertEqual(visibility["$type"], "questShowWorldNode_NodeType")
        self.assertEqual(visibility["isPlayer"], 1)
        self.assertEqual(visibility["show"], 0)
        self.assertEqual(visibility["objectRef"]["$value"], "0")

    def test_multiple_entry_points_each_target_a_start_node(self) -> None:
        spec = copy.deepcopy(self.spec)
        spec["entry_points"] = [
            {"name": "start", "node_id": 1},
            {"name": "alternate", "node_id": 99},
        ]
        spec["start_nodes"] = [
            spec["start_node"],
            {"node_id": 99, "on_start": [{"node_id": 18}]},
        ]
        spec.pop("graph_order", None)

        scene = generate_scene.build_scene(spec)
        graph = {
            node["Data"]["nodeId"]["id"]: node["Data"]
            for node in scene["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
        }

        self.assertEqual(graph[1]["$type"], "scnStartNode")
        self.assertEqual(graph[99]["$type"], "scnStartNode")
        self.assertEqual(
            {
                entry["name"]["$value"]: entry["nodeId"]["id"]
                for entry in scene["Data"]["RootChunk"]["entryPoints"]
            },
            {"start": 1, "alternate": 99},
        )
        self.assertEqual(generate_scene.validate_scene(scene, spec), [])

    def test_validation_rejects_entry_point_that_bypasses_start_node(self) -> None:
        scene = copy.deepcopy(self.scene)
        scene["Data"]["RootChunk"]["entryPoints"][0]["nodeId"]["id"] = 2

        errors = generate_scene.validate_scene(scene, self.spec)

        self.assertTrue(
            any("must target a scnStartNode" in error for error in errors),
            errors,
        )

    def test_validation_rejects_regular_flow_into_quest_cut_destination(self) -> None:
        scene = copy.deepcopy(self.scene)
        start = next(
            node["Data"]
            for node in scene["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
            if node["Data"]["nodeId"]["id"] == 1
        )
        start["outputSockets"][0]["destinations"][0]["isockStamp"]["ordinal"] = 0

        errors = generate_scene.validate_scene(scene, self.spec)

        self.assertTrue(
            any("targets CutDestination on quest node 10" in error for error in errors),
            errors,
        )

    def test_validation_rejects_non_executable_section_destination(self) -> None:
        scene = copy.deepcopy(self.scene)
        transition = next(
            node["Data"]
            for node in scene["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
            if node["Data"]["nodeId"]["id"] == 13
        )
        destination = transition["outputSockets"][0]["destinations"][0]
        self.assertEqual(destination["nodeId"]["id"], 2)
        destination["isockStamp"]["ordinal"] = 1

        errors = generate_scene.validate_scene(scene, self.spec)

        self.assertTrue(
            any("section flow must use socket 0:0" in error for error in errors),
            errors,
        )

    def test_spoken_only_scene_does_not_require_choice_lines(self) -> None:
        spec = copy.deepcopy(self.spec)
        spec["name"] = "test_spoken_only"
        spec["spoken_line_order"] = ["line_a"]
        spec["choice_line_order"] = []
        spec["sections"] = [
            {
                "key": "opening_line",
                "node_id": 2,
                "lines": ["line_a"],
                "on_end": [{"node_id": 18}],
            }
        ]
        spec["choices"] = []
        spec["quest_nodes"] = []
        spec["xor_nodes"] = []
        spec["start_node"] = {"node_id": 1, "on_start": [{"node_id": 2}]}
        spec["end_node"] = {"node_id": 18}
        spec["entry_point"] = {"name": "start", "node_id": 1}
        spec["exit_points"] = [{"name": "job_accept", "node_id": 18}]
        spec.pop("graph_order", None)

        manifest = {
            "spoken_lines": [
                {
                    "key": "line_a",
                    "string_id": "1000",
                    "speaker": "Patch",
                    "addressee": "V",
                    "text": "You made it.",
                    "duration_ms": 1000,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as tmp:
            manifest_path = Path(tmp) / "manifest.json"
            base_path = Path(tmp) / "base.scene.json"
            base = generate_scene.load_json(ROOT / spec["base_scene"])
            base["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"] = [
                wrapper
                for wrapper in base["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
                if wrapper.get("Data", {}).get("$type") != "scnChoiceNode"
            ]
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            base_path.write_text(json.dumps(base), encoding="utf-8")
            spec["manifest"] = str(manifest_path)
            spec["base_scene"] = str(base_path)
            scene = generate_scene.build_scene(spec)

        root = scene["Data"]["RootChunk"]
        self.assertEqual(root["screenplayStore"]["options"], [])
        self.assertEqual(root["locStore"]["vdEntries"], [])
        self.assertEqual(root["locStore"]["vpEntries"], [])
        self.assertEqual(generate_scene.validate_scene(scene, spec), [])

    def test_locstore_variant_ids_are_reserved_and_unique(self) -> None:
        spec = {
            "name": "test_locstore",
            "choice_line_order": ["choice_a", "choice_b"],
            "choice_locales": ["db_db", "en_us"],
        }
        choice_manifest = {
            "choice_a": {"key": "choice_a", "string_id": "1000", "text": "A"},
            "choice_b": {"key": "choice_b", "string_id": "1004", "text": "B"},
        }
        spoken_manifest = {
            "line_a": {"key": "line_a", "string_id": "1008", "text": "Line"},
        }

        loc_store = generate_scene.build_loc_store(
            spec, choice_manifest, spoken_manifest
        )
        variant_ids = [entry["variantId"]["ruid"] for entry in loc_store["vpEntries"]]

        self.assertEqual(len(variant_ids), len(set(variant_ids)))
        self.assertTrue(set(variant_ids).isdisjoint({"1000", "1004", "1008"}))

    def test_validation_rejects_locstore_variant_locstring_collision(self) -> None:
        scene = copy.deepcopy(self.scene)
        root = scene["Data"]["RootChunk"]
        collision = root["screenplayStore"]["lines"][0]["locstringId"]["ruid"]
        root["locStore"]["vpEntries"].append({"variantId": {"ruid": collision}})

        errors = generate_scene.validate_scene(scene, self.spec)

        self.assertTrue(
            any(
                "locStore variant ids collide with screenplay locstrings" in error
                for error in errors
            )
        )

    def test_validation_rejects_unsorted_choice_locstore_descriptors(self) -> None:
        scene = copy.deepcopy(self.scene)
        descriptors = scene["Data"]["RootChunk"]["locStore"]["vdEntries"]
        en_us_indexes = [
            index
            for index, entry in enumerate(descriptors)
            if entry["localeId"] == "en_us"
        ]
        descriptors[en_us_indexes[0]], descriptors[en_us_indexes[-1]] = (
            descriptors[en_us_indexes[-1]],
            descriptors[en_us_indexes[0]],
        )

        errors = generate_scene.validate_scene(scene, self.spec)

        self.assertTrue(
            any(
                "en_us choice locStore descriptors must be sorted" in error
                for error in errors
            )
        )

    def test_fixture_keeps_spawn_and_journal_flow_in_questphase(self) -> None:
        serialized = json.dumps(self.root)

        self.assertNotIn("questSpawnManagerNodeDefinition", serialized)
        self.assertNotIn("questCharacterSpawned_ConditionType", serialized)
        self.assertEqual(list(generate_scene.iter_journal_paths(self.root)), [])

    def test_validation_rejects_graph_order_drift(self) -> None:
        scene = copy.deepcopy(self.scene)
        graph = scene["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]
        graph[8], graph[9] = graph[9], graph[8]

        errors = generate_scene.validate_scene(scene, self.spec)

        self.assertTrue(any("Scene graph order mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
