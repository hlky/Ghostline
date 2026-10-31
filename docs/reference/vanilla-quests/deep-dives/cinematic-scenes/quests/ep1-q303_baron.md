# The Damned: scene presentation

Journal identity: `ep1/quests/main_quest/q303_baron`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q303_baron.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\main_quests\q303\scenes\q303_02_nighthawks.scene`

1300 graph nodes, 1714 edges; 267 event-bearing sections, 3022 events; 508 screenplay lines, 75 screenplay options, 29 choice nodes.

Actors: Alex (actor 0, spawnSet); Reed (actor 1, spawnSet); Reed_Holo (actor 2, spawnSet); Droid (actor 3, community); customer_01 (actor 4, community); customer_02 (actor 5, community); customer_03 (actor 6, community); Johnny (actor 7, spawnDespawn); customer_v_place (actor 8, community); customer_04 (actor 9, community); customer_05 (actor 10, community); customer_06 (actor 11, community); customer_07 (actor 12, community); customer_08 (actor 13, community); sh_050_customer_1_ma (actor 14, spawnDespawn); sh_050_customer_2_wa (actor 15, spawnDespawn); sh_050_customer_3_wa (actor 16, spawnDespawn); sh_050_customer_4_ma (actor 17, spawnDespawn); reed_car (actor 18, spawnSet); Player (actor 19, findInContext).

Entries: `in` → 1; `trailer_sh_0120` → 13867; `trailer_sh_0270` → 13923; `crowd_preview` → 10739; `dbg_going_back_inside` → 7935; `dbg_silverhand` → 7951; `intro_wait` → 7956; `trailer_sh_260` → 14389; `trailer` → 11264; `Start 11` → 12382; `Start 18` → 14613; `dbg_going_outside` → 5185; `intro_wait_pre_quest` → 14815; `alex_idle` → 11638.

Exits: `output` → 6573; `alex_outside_ui_loop` → 14591; `intro_wait_out` → 8317; `intro_wait_pre_quest_out` → 14827; `alex_idle_out` → 11647.

End nodes: 6573: `NonTerminating`; 8317: `<omitted>`; 11647: `<omitted>`; 14591: `NonTerminating`; 14827: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 40 | 1166 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scnChangeIdleAnimEvent` | 96 | 1166 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnDialogLineEvent` | 338 | 1166 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scnGameplayTransitionEvent` | 29 | 1056 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scnIKEvent` | 58 | 1056 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtAdvancedEvent` | 182 | 3294 / 357 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/6` |
| `scnLookAtEvent` | 661 | 598 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 2 | 7126 / 3104 | `/Data/RootChunk/sceneGraph/Data/graph/171/Data/events/20` |
| `scnPlaySkAnimEvent` | 723 | 598 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPoseCorrectionEvent` | 27 | 1166 / 215 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/38` |
| `scnUnmountEvent` | 29 | 1056 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scneventsAttachPropToNode` | 2 | 10165 / 5456 | `/Data/RootChunk/sceneGraph/Data/graph/471/Data/events/0` |
| `scneventsAttachPropToPerformer` | 62 | 1056 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsAttachPropToWorld` | 46 | 598 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/12` |
| `scneventsCameraParamsEvent` | 23 | 4251 / 522 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/2` |
| `scneventsEquipItemToPerformer` | 22 | 2582 / 305 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/3` |
| `scneventsPlayRidCameraAnimEvent` | 2 | 13883 / 10205 | `/Data/RootChunk/sceneGraph/Data/graph/1120/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 29 | 1056 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scneventsSocket` | 557 | 598 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsSpawnEntityEvent` | 11 | 5302 / 1037 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/13` |
| `scneventsUnequipItemFromPerformer` | 18 | 2582 / 313 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/6` |
| `scneventsUnequipItemFromPerformerByItem` | 3 | 598 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scneventsVFXDurationEvent` | 26 | 5268 / 865 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/29` |
| `scneventsVFXEvent` | 36 | 3294 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 23
- gaze: 22
- skeletal_animation, gaze: 14
- camera: 13
- skeletal_animation, socket_signal: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 12
- skeletal_animation: 11
- vfx: 10
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 8
- speech, gaze: 8
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- speech, gaze, socket_signal: 7
- speech: 6
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- skeletal_animation, props_equipment, vfx, socket_signal, entity_lifecycle: 6
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze: 5
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 4
- speech, skeletal_animation, gaze: 4
- skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- gaze, socket_signal: 3
- socket_signal: 3
- skeletal_animation, props_equipment, socket_signal: 3
- skeletal_animation, props_equipment: 3
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, camera, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, vfx, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 2
- props_equipment: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal, entity_lifecycle: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, camera, audio, vfx: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, vfx: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, rid_camera, socket_signal: 1
- props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, rid_camera, props_equipment, audio, vfx, socket_signal: 1

Raw SHA-256: `b8de4a1a51e6e4ddca8b3800fae2c256fa7d39ebd266160022ce78efb5567ac7`. Binary SHA-256: `ef5b0e80d4adc0f53aa1548b737e7fd5f7a963425fbf7aea9ed63a4d3a426c03`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_02_nighthawks.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_03_voodoo_boys.scene`

665 graph nodes, 827 edges; 97 event-bearing sections, 503 events; 138 screenplay lines, 23 screenplay options, 8 choice nodes.

Actors: Reed (actor 0, spawnSet); q303_voodoo_boy_guard_wa (actor 1, community); q303_voodoo_boy_guard_ma_01 (actor 2, community); q303_voodoo_trap (actor 3, community); vdb_comm_1_male (actor 4, community); vdb_comm_1_female (actor 5, community); vdb_comm_2_male (actor 6, community); vdb_comm_2_female (actor 7, community); Johnny (actor 8, spawnDespawn); mood_vdb1_wa (actor 9, community); chat_vdb1_ma (actor 10, community); chat_vdb2_wa (actor 11, community); chat_vdb3_ma (actor 12, community); chat_vdb4_ma (actor 13, community); Player (actor 14, findInContext).

Entries: `trap_fallen` → 1; `server_glitch` → 1262; `server_destroyed` → 1288; `Start 0` → 3801; `Start 5` → 2578; `EntranceDoor_CineDebug` → 97; `intro` → 760; `server_netrunner_tip` → 2701; `server_tech_weapon_tip` → 2710; `server_melee_tip` → 2714; `server_advice` → 880; `trap_hunch` → 1516; `Start1` → 5319; `camera_kick_effect` → 5960; `server_glitch_damage` → 3460; `server_glitch_stop` → 4771; `server_advice_trap` → 2274; `server_open_shout2` → 1046; `server_open_shout3` → 1050; `server_hack_done` → 1701; `defeat_enemies` → 1074; `trap_scanned` → 3033; `peaceful_entry` → 4309; `server_moodscene` → 1824.

Exits: `server_destroyed_out` → 1292; `intro_done` → 752; `trap_hunch_cut` → 1402; `trap_secured_out` → 1439; `server_netrunner_tip_out` → 2703; `server_tech_weapon_tip_out` → 2712; `server_melee_tip_out` → 2719; `trap_disabled_out` → 1495; `server_advice_out` → 884; `server_advice_trap_out` → 2277; `server_open_shout2_out` → 1048; `exploration_start_out` → 4188; `server_open_shout3_out` → 1052; `server_hack_done_out` → 1703; `defeat_enemies_out` → 1078; `trap_out` → 1085; `peaceful_entry_out` → 4310; `server_moodscene_out` → 1826; `restore_reactions_out` → 4975; `intro_vent_guidance` → 1250.

End nodes: 752: `<omitted>`; 884: `<omitted>`; 1048: `<omitted>`; 1052: `<omitted>`; 1078: `<omitted>`; 1085: `<omitted>`; 1250: `NonTerminating`; 1292: `<omitted>`; 1402: `<omitted>`; 1439: `<omitted>`; 1495: `NonTerminating`; 1703: `<omitted>`; 1826: `<omitted>`; 2277: `<omitted>`; 2703: `<omitted>`; 2712: `<omitted>`; 2719: `<omitted>`; 4188: `NonTerminating`; 4310: `<omitted>`; 4975: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 21 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnDialogLineEvent` | 91 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnGameplayTransitionEvent` | 5 | 70 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/10` |
| `scnIKEvent` | 10 | 70 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |
| `scnLookAtEvent` | 98 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 120 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 5 | 70 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/9` |
| `scneventsCameraParamsEvent` | 2 | 740 / 436 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/1` |
| `scneventsEquipItemToPerformer` | 6 | 661 / 348 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/0` |
| `scneventsPlayerLookAtEvent` | 1 | 5077 / 3325 | `/Data/RootChunk/sceneGraph/Data/graph/518/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 70 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/6` |
| `scneventsSocket` | 105 | 5 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scneventsUnequipItemFromPerformer` | 1 | 661 / 368 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/11` |
| `scneventsVFXDurationEvent` | 41 | 1175 / 765 | `/Data/RootChunk/sceneGraph/Data/graph/101/Data/events/0` |
| `scneventsVFXEvent` | 8 | 12 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 20
- vfx: 14
- speech, skeletal_animation, gaze, socket_signal: 12
- skeletal_animation, socket_signal: 8
- skeletal_animation, gaze: 8
- gaze: 6
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- camera: 1
- speech, skeletal_animation, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `4f7584726fb5754f8e9091d8f501bb665967ad982261bb80c3c651f4c866ac21`. Binary SHA-256: `10d5226ab197e45079dfdf94f9ab183820c80a098fb444cb36711a9eef6426a0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_03_voodoo_boys.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_03a_voodoo_baron.scene`

832 graph nodes, 1064 edges; 121 event-bearing sections, 1943 events; 270 screenplay lines, 41 screenplay options, 23 choice nodes.

Actors: Reed (actor 0, spawnDespawn); Songbird (actor 1, spawnDespawn); Baron (actor 2, spawnSet); Johnny (actor 3, spawnDespawn); q303_voodoo_boy_after_guard_02 (actor 4, community); q303_voodoo_boy_after_guard_01 (actor 5, community); Reed_real_npc (actor 6, spawnSet); reed_vehicle (actor 7, spawner); Player (actor 8, findInContext).

Entries: `preview_start_reed_baron_death` → 4916; `Start 18` → 6377; `start_baron` → 4422; `exit_patrol_incoming` → 4430; `blackwall_baron` → 5161; `exit_sequence` → 5164; `Start 15` → 5900; `dbg_exit` → 2558.

Exits: `baron_done_out` → 4466; `exit_patrol_incoming_done` → 5948; `exit_done` → 1334.

End nodes: 1334: `NonTerminating`; 4466: `NonTerminating`; 5948: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 81 | 1188 / 313 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/18` |
| `scnChangeIdleAnimEvent` | 114 | 1106 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 204 | 1106 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 10 | 1423 / 1460 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/12` |
| `scnIKEvent` | 20 | 1423 / 1444 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/1` |
| `scnLookAtAdvancedEvent` | 39 | 1195 / 395 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/24` |
| `scnLookAtEvent` | 282 | 1106 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnOverridePhantomParamsEvent` | 2 | 1198 / 545 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/62` |
| `scnPlaySkAnimEvent` | 598 | 1106 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPoseCorrectionEvent` | 2 | 1437 / 1500 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/17` |
| `scnUnmountEvent` | 10 | 1423 / 1465 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/16` |
| `scneventsCameraParamsEvent` | 14 | 1198 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/43` |
| `scneventsSetAnimFeatureEvent` | 10 | 1423 / 1461 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/13` |
| `scneventsSocket` | 364 | 1118 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsVFXDurationEvent` | 85 | 1195 / 390 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/21` |
| `scneventsVFXEvent` | 108 | 1106 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 21
- skeletal_animation, gaze, socket_signal: 11
- speech, skeletal_animation, gaze, socket_signal: 10
- skeletal_animation, socket_signal: 10
- skeletal_animation: 9
- speech: 5
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 3
- speech, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- vfx: 3
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- skeletal_animation, gaze: 3
- skeletal_animation, gaze, audio, vfx: 3
- speech, skeletal_animation, idle_animation, gaze, vfx: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `f39ce422379d74d84a3e98289619164d2c3e46537ddc34a8c9b0d0575d3e790f`. Binary SHA-256: `4c1def6cb22db9483517532c8c0b341e0393abb94935c8cf9c2b261a589b60e1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_03a_voodoo_baron.scene" --events
```

