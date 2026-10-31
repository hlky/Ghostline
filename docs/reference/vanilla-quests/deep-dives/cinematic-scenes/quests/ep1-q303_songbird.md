# You Know My Name: scene presentation

Journal identity: `ep1/quests/main_quest/q303_songbird`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q303_songbird.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

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

## `ep1\quest\main_quests\q303\scenes\q303_05_safehouse.scene`

629 graph nodes, 725 edges; 109 event-bearing sections, 1011 events; 238 screenplay lines, 37 screenplay options, 15 choice nodes.

Actors: Reed (actor 0, spawnSet); Alex (actor 1, spawnSet); Droid (actor 2, community); Player (actor 3, findInContext).

Entries: `preview_full` → 6138; `start` → 3721; `Start 5` → 6201; `Start 6` → 6289; `door_idle` → 8751; `Start 8` → 8173; `Start 11` → 8866; `Start 7` → 6438; `Start1` → 5409; `dbg_safehouse` → 5411; `intro_wait` → 6661.

Exits: `out` → 2; `intro_wait_out` → 6710.

End nodes: 2: `NonTerminating`; 6710: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 67 | 2470 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/8` |
| `scnChangeIdleAnimEvent` | 48 | 2320 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnDialogLineEvent` | 166 | 2320 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnGameplayTransitionEvent` | 11 | 2351 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/15` |
| `scnIKEvent` | 22 | 2351 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/8` |
| `scnLookAtAdvancedEvent` | 8 | 4298 / 848 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/6` |
| `scnLookAtEvent` | 199 | 2320 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPlaySkAnimEvent` | 212 | 2320 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnPoseCorrectionEvent` | 25 | 2351 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/10` |
| `scnUnmountEvent` | 11 | 2351 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/14` |
| `scneventsAttachPropToNode` | 1 | 2470 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/21` |
| `scneventsAttachPropToPerformer` | 2 | 2470 / 156 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/6` |
| `scneventsAttachPropToWorld` | 1 | 2470 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/7` |
| `scneventsCameraParamsEvent` | 4 | 6257 / 2156 | `/Data/RootChunk/sceneGraph/Data/graph/206/Data/events/29` |
| `scneventsEquipItemToPerformer` | 4 | 8849 / 4330 | `/Data/RootChunk/sceneGraph/Data/graph/562/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 11 | 2351 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |
| `scneventsSocket` | 188 | 2320 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 8849 / 4332 | `/Data/RootChunk/sceneGraph/Data/graph/562/Data/events/5` |
| `scneventsVFXDurationEvent` | 7 | 4592 / 1188 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/5` |
| `scneventsVFXEvent` | 23 | 2971 / 307 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 13
- speech, skeletal_animation, gaze, socket_signal: 12
- speech: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech, gaze, socket_signal: 5
- speech, skeletal_animation, gaze: 5
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze, vfx, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- vfx: 3
- gaze: 3
- skeletal_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, gaze: 1
- skeletal_animation, audio, socket_signal: 1
- camera: 1
- skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- socket_signal: 1
- idle_animation: 1
- idle_animation, audio: 1
- skeletal_animation, gaze: 1
- gaze, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `5e9df7088cc1d1b3e4ea59eccd5b108b1a00cd6b52db6310d0adc02515bc0bee`. Binary SHA-256: `6171834570a03bd1f555a8c1227044a9845bc2dcdda1547077bc5f81ea6633cf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_05_safehouse.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_06_paradise.scene`

532 graph nodes, 626 edges; 81 event-bearing sections, 927 events; 167 screenplay lines, 33 screenplay options, 16 choice nodes.

Actors: Lizzy (actor 0, spawnSet); Reed (actor 1, spawnSet); Songbird (actor 2, spawnSet); Theo (actor 3, spawnSet); Bella (actor 4, spawnSet); Songbird_vision (actor 5, spawnDespawn); Kurt (actor 6, spawnSet); Johnny (actor 7, spawnDespawn); Songbird_crowd_01_ma (actor 8, community); Songbird_crowd_02_ma (actor 9, community); Songbird_crowd_01_wa (actor 10, community); braindace_replacer (actor 11, community); V (actor 12, findInContext).

Entries: `Start 0` → 1; `Start 11` → 4451; `cinedebug_reed_meet_somi` → 550; `lizzys_concert_braindance` → 4476; `cinedebug_somi_reed` → 2050; `lizzys_concert` → 2613; `Start 10` → 4095; `songbird_debug` → 2656; `cinedebug_vision` → 1297; `Start 9` → 3796; `Start 8` → 2837; `cinedebug_endreed` → 1404.

Exits: `End 0` → 2; `lizzys_concert_out` → 4103; `lizzy_braindance_restart` → 4595; `End1` → 4285; `lizzy_terminate` → 4776.

End nodes: 2: `NonTerminating`; 4103: `NonTerminating`; 4285: `<omitted>`; 4595: `<omitted>`; 4776: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 30 | 97 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnChangeIdleAnimEvent` | 47 | 97 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 115 | 97 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnGameplayTransitionEvent` | 3 | 629 / 565 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/8` |
| `scnIKEvent` | 6 | 629 / 559 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/3` |
| `scnLookAtAdvancedEvent` | 86 | 97 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/27` |
| `scnLookAtEvent` | 179 | 97 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlayRidAnimEvent` | 12 | 3880 / 2324 | `/Data/RootChunk/sceneGraph/Data/graph/217/Data/events/2` |
| `scnPlaySkAnimEvent` | 228 | 97 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 3 | 629 / 564 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/7` |
| `scneventsAttachPropToPerformer` | 8 | 623 / 394 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/8` |
| `scneventsAttachPropToWorld` | 7 | 1022 / 758 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/42` |
| `scneventsCameraParamsEvent` | 14 | 97 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/25` |
| `scneventsPlayRidCameraAnimEvent` | 6 | 5178 / 3449 | `/Data/RootChunk/sceneGraph/Data/graph/401/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 3 | 629 / 562 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/6` |
| `scneventsSocket` | 150 | 97 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsSpawnEntityEvent` | 1 | 3832 / 2284 | `/Data/RootChunk/sceneGraph/Data/graph/214/Data/events/7` |
| `scneventsUnequipItemFromPerformer` | 1 | 3832 / 2282 | `/Data/RootChunk/sceneGraph/Data/graph/214/Data/events/5` |
| `scneventsVFXDurationEvent` | 3 | 4594 / 2961 | `/Data/RootChunk/sceneGraph/Data/graph/316/Data/events/0` |
| `scneventsVFXEvent` | 25 | 363 / 217 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 12
- speech, skeletal_animation, gaze, socket_signal: 9
- skeletal_animation, socket_signal: 7
- skeletal_animation: 5
- skeletal_animation, camera, socket_signal: 4
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech: 3
- socket_signal: 3
- vfx: 3
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, gaze, audio: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, props_equipment, audio, entity_lifecycle: 1
- skeletal_animation, rid_actor, audio, vfx, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze: 1
- skeletal_animation, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `29252d1893d6141be4f411fc2437241a7e3eabecc871a660d3005c1695bb80b8`. Binary SHA-256: `44c7af770625f4b199885036f76888d06d78f15a67f3ba9e5a524fc6d2db9483`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_06_paradise.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_06a_paradise_roleplay_restaurant_floor.scene`

1262 graph nodes, 1600 edges; 285 event-bearing sections, 1846 events; 375 screenplay lines, 48 screenplay options, 38 choice nodes.

Actors: Reed (actor 0, spawnSet); Lizzy (actor 1, spawnSet); Concierge (actor 2, community); Reed_comms (actor 3, findInContext); 01_arasaka_contact_01 (actor 4, community); 01_arasaka_contact_02 (actor 5, community); 01_holt (actor 6, community); 02_hands_vip (actor 7, community); 03_hands_fixer (actor 8, community); 03_hands_general (actor 9, community); 04_fashion_model_01 (actor 10, community); 04_fashion_model_02 (actor 11, community); 05_iqbal (actor 12, community); 05_jordan (actor 13, community); 06_ncpd_chief (actor 14, community); 06_6th_leader (actor 15, community); 07_ziggyq (actor 16, community); 08_ruth (actor 17, community); 09_stanley (actor 18, community); 10_kavorkin (actor 19, community); 11_boxer (actor 20, community); 11_rapper (actor 21, community); 12_football_01 (actor 22, community); 12_football_02 (actor 23, community); 12_football_03 (actor 24, community); 12_football_04 (actor 25, community); 13_jotaro (actor 26, community); 13_maiko (actor 27, community); 13_tyger_boss_01 (actor 28, community); 13_tyger_boss_02 (actor 29, community); 13_tyger_guard_01 (actor 30, community); 13_tyger_guard_02 (actor 31, community); 13_tzar (actor 32, community); 13_tzar_bodyguard_01 (actor 33, community); 13_tzar_bodyguard_02 (actor 34, community); 17_priest (actor 35, community); 18_hideshi (actor 36, community); 15_barman (actor 37, community); waitress (actor 38, community); Bella (actor 39, spawnSet); 09_stanley_moodscene_guest (actor 40, community); waitress2 (actor 41, community); waitress_tech1 (actor 42, community); waitress_tech2 (actor 43, community); Songbird (actor 44, spawnSet); Theo (actor 45, spawnSet); 07_ziggyq_crowd (actor 46, community); 21_mask_commenter_01 (actor 47, community); 21_mask_commenter_02 (actor 48, community); waitress_routine (actor 49, community); 20_investor_01 (actor 50, community); 20_investor_02 (actor 51, community); waitress6 (actor 52, community); barman_paradise3 (actor 53, community); barman_paradise2 (actor 54, community); barman_paradise1 (actor 55, community); lady_in_red (actor 56, community); entrance_guard_01 (actor 57, community); entrance_guard_02 (actor 58, community); waitress5 (actor 59, community); casino_barman_1 (actor 60, community); casino_barman_2 (actor 61, community); casino_waitress_1 (actor 62, community); casino_waitress_2 (actor 63, community); stage_guard_01 (actor 64, community); stage_guard_02 (actor 65, community); Johnny (actor 66, spawnDespawn); 22_kurt (actor 67, spawnSet); 23_holt_gossip_01 (actor 68, community); 23_holt_gossip_02 (actor 69, community); casino_01_robot_01 (actor 70, community); casino_02_player_01 (actor 71, community); casino_02_player_02 (actor 72, community); casino_02_player_03 (actor 73, community); casino_02_player_04 (actor 74, community); casino_03_player_01 (actor 75, community); casino_03_player_02 (actor 76, community); casino_03_player_03 (actor 77, community); casino_03_player_04 (actor 78, community); casino_03_player_05 (actor 79, community); casino_01_robot_net_dealer (actor 80, community); casino_01_robot_02 (actor 81, community); casino_01_robot_03 (actor 82, community); 26_tech_floor_guard (actor 83, community); paradise_guest_audience_ma_04 (actor 84, community); paradise_guest_audience_ma_01 (actor 85, community); paradise_guest_audience_wa_02 (actor 86, community); paradise_guest_audience_wa_06 (actor 87, community); paradise_guest_audience_wa_08 (actor 88, community); 25_kurts_interlocutor (actor 89, community); 25_kurt_jago (actor 90, community); 13_tyger_boss_03_single (actor 91, community); 13_tyger_boss_04_single (actor 92, community); paradise_guest_audience_ma_02 (actor 93, community); paradise_guest_audience_ma_03 (actor 94, community); paradise_guest_audience_ma_05 (actor 95, community); paradise_guest_audience_ma_06 (actor 96, community); paradise_guest_audience_ma_07 (actor 97, community); paradise_guest_audience_ma_08 (actor 98, community); paradise_guest_audience_wa_01 (actor 99, community); paradise_guest_audience_wa_03 (actor 100, community); paradise_guest_audience_wa_04 (actor 101, community); paradise_guest_audience_wa_05 (actor 102, community); paradise_guest_audience_wa_07 (actor 103, community); paradise_guest_audience_wa_09 (actor 104, community); paradise_guest_audience_wa_10 (actor 105, community); 25_kurt_bennett (actor 106, community); V (actor 107, findInContext).

Entries: `Start 14` → 9439; `Start 9` → 7364; `Start 11` → 8473; `Start 16` → 9624; `01_holt` → 266; `03_hands` → 288; `04_models` → 299; `05_jordan` → 307; `06_ncpd` → 321; `07_ziggyq` → 329; `08_ruth` → 337; `09_stanley` → 345; `10_kavorkin` → 365; `11_boxer_rapper` → 373; `20_hino_first` → 3518; `12_football` → 381; `hansen_conversation_loop` → 6659; `13_tyger_scav_meeting` → 389; `17_priest` → 424; `johnny_welcomes` → 5661; `19_restaurant_waitress` → 1486; `20_investors` → 3619; `golden_path` → 497; `22_interactions` → 4721; `15_bar` → 3675; `johnny_comments_kurt` → 5811; `johnny_comments_reed_alone` → 5828; `johnny_comment_lift_out` → 5898; `23_holt_commenters` → 5941; `casino_01_robot_table_reaction` → 5948; `casino_02_players_chat_01` → 5950; `casino_02_players_chat_02` → 5952; `Start 12` → 9092; `casino_03_game_oneliners` → 5954; `Start 7` → 3902; `casino_01_robot_table_invites_later` → 5998; `casino_01_robot_02_table_reaction` → 6068; `casino_01_robot_03_table_reaction` → 6070; `concert_reaction_audience_ma_01` → 6125; `22_interactions_casino_waitress` → 9264; `concert_reaction_audience_ma_04` → 6127; `concert_reaction_audience_wa_02` → 6129; `concert_reaction_audience_wa_06` → 6131; `concert_reaction_audience_lookats` → 7266; `21_mask_reaction` → 3106.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 3409 / 1708 | `/Data/RootChunk/sceneGraph/Data/graph/253/Data/events/8` |
| `scnChangeIdleAnimEvent` | 23 | 1419 / 1035 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/3` |
| `scnDialogLineEvent` | 244 | 270 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 31 | 2869 / 1407 | `/Data/RootChunk/sceneGraph/Data/graph/196/Data/events/4` |
| `scnIKEvent` | 62 | 2869 / 1404 | `/Data/RootChunk/sceneGraph/Data/graph/196/Data/events/1` |
| `scnLookAtAdvancedEvent` | 12 | 1589 / 1119 | `/Data/RootChunk/sceneGraph/Data/graph/154/Data/events/10` |
| `scnLookAtEvent` | 328 | 292 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 1 | 5582 / 3699 | `/Data/RootChunk/sceneGraph/Data/graph/478/Data/events/13` |
| `scnPlaySkAnimEvent` | 382 | 270 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 16 | 4238 / 2483 | `/Data/RootChunk/sceneGraph/Data/graph/342/Data/events/3` |
| `scnUnmountEvent` | 31 | 2869 / 1411 | `/Data/RootChunk/sceneGraph/Data/graph/196/Data/events/7` |
| `scneventsAttachPropToNode` | 12 | 4301 / 2578 | `/Data/RootChunk/sceneGraph/Data/graph/349/Data/events/20` |
| `scneventsAttachPropToPerformer` | 78 | 1432 / 1059 | `/Data/RootChunk/sceneGraph/Data/graph/147/Data/events/4` |
| `scneventsAttachPropToWorld` | 30 | 1589 / 1109 | `/Data/RootChunk/sceneGraph/Data/graph/154/Data/events/5` |
| `scneventsCameraParamsEvent` | 12 | 2830 / 1384 | `/Data/RootChunk/sceneGraph/Data/graph/192/Data/events/1` |
| `scneventsEquipItemToPerformer` | 33 | 323 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/31` |
| `scneventsSetAnimFeatureEvent` | 31 | 2869 / 1409 | `/Data/RootChunk/sceneGraph/Data/graph/196/Data/events/6` |
| `scneventsSocket` | 407 | 270 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 3 | 323 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/35` |
| `scneventsUnequipItemFromPerformerByItem` | 17 | 367 / 174 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/13` |
| `scneventsVFXDurationEvent` | 9 | 1589 / 1121 | `/Data/RootChunk/sceneGraph/Data/graph/154/Data/events/12` |
| `scneventsVFXEvent` | 83 | 323 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/30` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 54
- gaze: 32
- speech, skeletal_animation, gaze, socket_signal: 18
- skeletal_animation: 16
- skeletal_animation, socket_signal: 10
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 10
- props_equipment, vfx: 10
- speech, skeletal_animation, socket_signal: 8
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 8
- gaze, socket_signal: 7
- speech, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- skeletal_animation, props_equipment, socket_signal: 6
- props_equipment: 6
- speech, gaze: 5
- skeletal_animation, idle_animation, gaze: 5
- speech, socket_signal: 4
- speech, skeletal_animation: 4
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 4
- speech, gaze, vfx: 4
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 3
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, props_equipment, vfx, socket_signal, animation_state: 3
- skeletal_animation, gaze, ik, camera, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, props_equipment, vfx, socket_signal: 3
- socket_signal: 3
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- props_equipment, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze: 2
- speech, props_equipment, socket_signal: 1
- speech, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- gaze, props_equipment, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- props_equipment, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, vfx: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- gaze, animation_state: 1
- idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, props_equipment, vfx: 1
- vfx, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `fb3c328324d8561e839a30c37dc23131647499909d90755924466ef800cdde58`. Binary SHA-256: `c4cf28fd2d442026d83314bc92e8580fed7f30312f44b5e22b11a21c4411f250`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_06a_paradise_roleplay_restaurant_floor.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_06b_paradise_technical.scene`

513 graph nodes, 590 edges; 75 event-bearing sections, 325 events; 127 screenplay lines, 24 screenplay options, 14 choice nodes.

Actors: Reed (actor 0, spawnSet); Guard_tunnels (actor 1, spawnDespawn); Mood_01_01 (actor 2, spawnDespawn); Mood_01_02 (actor 3, spawnDespawn); Mood_02_01 (actor 4, spawnDespawn); Mood_03_01 (actor 5, spawnDespawn); Mood_03_02_jago (actor 6, spawnDespawn); drone (actor 7, spawnDespawn); Warehouse_01 (actor 8, community); Warehouse_02 (actor 9, community); Warehouse_03 (actor 10, community); Warehouse_04 (actor 11, community); v_tpp_mirror_male (actor 12, spawnDespawn); v_tpp_mirror_female (actor 13, spawnDespawn); sniper_nest_interface_voice (actor 14, spawnDespawn); Warehouse_05 (actor 15, community); sniper_nest_guard (actor 16, community); V (actor 17, findInContext).

Entries: `equipment_malfunction` → 511; `opening_gate` → 6; `nest_jack_out` → 4081; `nest_sniper_defeated_idle` → 4600; `Start 7` → 4106; `arrived_at_tech_floor` → 606; `tunnel_headlight` → 3154; `cinedebug_elevatorTop` → 1141; `warehouse_chat` → 2269; `warehouse_empty` → 2271; `warehouse_chat_cont` → 2314; `suit_up` → 310; `tunnel_headlight_weak` → 3903; `tunnel_garage_door_open` → 2955; `after_tech_floor_combat` → 952; `bridge_anim` → 4016.

Exits: `nest_intro_done` → 8; `equipment_malfunction_out` → 544; `nest_sniper_defeated_idle_out` → 4617; `tunel_headlight_out` → 3165; `equipment_malfunction_comment_out` → 4244; `reed_elevator_moving` → 4275; `warehouse_chat_cont_out` → 2285; `warehouse_alerted_out` → 2295; `warehouse_empty_out` → 2308; `warehouse_chat_out` → 2312; `to_restaurant` → 312; `combat_nest_disconnect_out` → 2861; `to_johnny_welcome` → 2942; `tunnel_garage_door_open_out` → 2953; `force_max_visibility_out` → 3966.

End nodes: 8: `<omitted>`; 312: `NonTerminating`; 544: `<omitted>`; 2285: `<omitted>`; 2295: `<omitted>`; 2308: `<omitted>`; 2312: `<omitted>`; 2861: `NonTerminating`; 2942: `NonTerminating`; 2953: `<omitted>`; 3165: `<omitted>`; 3966: `NonTerminating`; 4244: `NonTerminating`; 4275: `NonTerminating`; 4617: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 2236 / 806 | `/Data/RootChunk/sceneGraph/Data/graph/113/Data/events/1` |
| `scnChangeIdleAnimEvent` | 29 | 392 / 252 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/2` |
| `scnDialogLineEvent` | 80 | 128 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 1150 / 401 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/11` |
| `scnIKEvent` | 14 | 1150 / 394 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/5` |
| `scnLookAtAdvancedEvent` | 2 | 458 / 321 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/6` |
| `scnLookAtEvent` | 14 | 314 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnPlaySkAnimEvent` | 80 | 314 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnUnmountEvent` | 7 | 1150 / 400 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/10` |
| `scneventsAttachPropToNode` | 2 | 3162 / 1649 | `/Data/RootChunk/sceneGraph/Data/graph/237/Data/events/0` |
| `scneventsAttachPropToPerformer` | 4 | 1165 / 419 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/7` |
| `scneventsAttachPropToWorld` | 3 | 392 / 255 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/5` |
| `scneventsCameraParamsEvent` | 2 | 2590 / 1157 | `/Data/RootChunk/sceneGraph/Data/graph/168/Data/events/11` |
| `scneventsEquipItemToPerformer` | 3 | 1698 / 596 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/0` |
| `scneventsPlayerLookAtEvent` | 1 | 2785 / 1348 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 7 | 1150 / 398 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/9` |
| `scneventsSocket` | 56 | 314 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |
| `scneventsUnequipItemFromPerformer` | 1 | 1739 / 687 | `/Data/RootChunk/sceneGraph/Data/graph/94/Data/events/7` |
| `scneventsVFXDurationEvent` | 1 | 458 / 320 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/5` |
| `scneventsVFXEvent` | 2 | 4297 / 2469 | `/Data/RootChunk/sceneGraph/Data/graph/377/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- skeletal_animation: 8
- skeletal_animation, idle_animation: 5
- speech, socket_signal: 4
- skeletal_animation, idle_animation, audio: 4
- props_equipment: 4
- speech, skeletal_animation, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze, props_equipment, socket_signal: 2
- gaze: 2
- vfx: 2
- idle_animation: 2
- skeletal_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, vfx: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- gaze, socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, audio: 1

Raw SHA-256: `f21674e38c2b0f56185963a395e28ab91ce37f39aa20c1657c7948a1d3ed6f1d`. Binary SHA-256: `a6c66387357315fb00ff4b265e28180d33a6acaddb0b8fa317fa088fe0c74f50`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_06b_paradise_technical.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_06b_paradise_technical_gameplay.scene`

1945 graph nodes, 2644 edges; 126 event-bearing sections, 217 events; 190 screenplay lines, 13 screenplay options, 11 choice nodes.

Actors: Reed_comms (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); chall_03_guard_01 (actor 2, community); chall_03_guard_02 (actor 3, community); chall_03_guard_03 (actor 4, community); chall_03_sniper (actor 5, community); chall_01_patrol_01 (actor 6, community); chall_01_patrol_02 (actor 7, community); chall_02_guard_01 (actor 8, community); chall_02_guard_02 (actor 9, community); elevator_guard_01 (actor 10, community); elevator_guard_02 (actor 11, community); elevator_guard_03 (actor 12, community); chall_04_guard_01 (actor 13, community); chall_05_guard_01 (actor 14, community); chall_05_guard_02 (actor 15, community); sniper_nest (actor 16, spawnDespawn); extra_guard_01 (actor 17, community); extra_guard_02 (actor 18, community); extra_guard_03 (actor 19, community); reinforcements_zone_02_guard_01 (actor 20, community); reinforcements_zone_02_guard_02 (actor 21, community); reinforcements_zone_02_guard_03 (actor 22, community); reinforcements_zone_02_guard_04 (actor 23, community); reinforcements_zone_02_guard_05 (actor 24, community); reinforcements_zone_02_sniper_01 (actor 25, community); reinforcements_zone_02_sniper_02 (actor 26, community); reinforcements_zone_03_behind_01 (actor 27, community); reinforcements_zone_03_behind_02 (actor 28, community); reinforcements_zone_03_guard_01 (actor 29, community); reinforcements_zone_03_guard_02 (actor 30, community); reinforcements_zone_03_guard_03 (actor 31, community); reinforcements_zone_03_guard_04 (actor 32, community); reinforcements_zone_03_guard_05 (actor 33, community); reinforcements_zone_04_guard_01 (actor 34, community); reinforcements_zone_04_guard_02 (actor 35, community); reinforcements_zone_04_guard_03 (actor 36, community); reinforcements_zone_04_guard_04 (actor 37, community); reinforcements_zone_04_guard_05 (actor 38, community); reinforcements_zone_04_guard_06 (actor 39, community); Reed_holo_intro (actor 40, spawnSet); reinforcements_zone_04_drone_03 (actor 41, community); reinforcements_zone_03_guard_exo (actor 42, community); dispatcher (actor 43, spawner); Player (actor 44, findInContext).

Entries: `tunnel_approach` → 1; `in_water` → 16; `platform_hint` → 31; `comms_back` → 55; `entrance_approached` → 9932; `combat_zone_03_drones_in` → 6151; `combat_take_them` → 21982; `combat_snipers_in` → 2443; `combat_zone_02_done_in` → 2451; `combat_zone_03_behind_in` → 2459; `combat_zone_03_done_in` → 2501; `debug_start_chall_01_patrol` → 20484; `debug_start_chall_02` → 20508; `debug_start_chall_05` → 20546; `force_max_visibility_in` → 20572; `in_water_no_suit` → 6768; `combat_octant` → 6786; `Start 3` → 16745; `scene_trough_ledge` → 16754; `scene_stop_ledge` → 16756; `Start 11` → 20749; `reed_to_cover` → 20805; `nest_intro_done` → 3104; `scene_chall01_patrol` → 19285; `reed_elevator_moving` → 21306; `scene_chall01_mine` → 19350; `tunnel_reed_progress_01` → 15566; `tunnel_reed_progress_02` → 15570; `tunnel_reed_progress_03` → 15574; `combat_start_in` → 1781; `combat_reed_blocked_in` → 25471; `combat_lost_damage_message` → 15665; `chall_04_fall_preview` → 25541; `nest_temp_lookat` → 7789; `debug_start_chall_04` → 13735; `debug_start_chall_01_mine` → 13738; `debug_start_chall_03` → 13748; `nest_temp_lookat_reed` → 13793.

Exits: `in_water_out` → 18; `End1` → 25676; `platform_hint_out` → 33; `comms_back_out` → 57; `entrance_approached_out` → 9934; `stealth_nest_disconnect_out` → 69; `recon_elevator_start_out` → 25721; `combat_zone_03_drones_out` → 6153; `combat_take_them_out` → 21987; `combat_snipers_out` → 2445; `combat_zone_02_done_out` → 2453; `combat_zone_03_behind_out` → 2461; `combat_zone_03_done_out` → 2503; `force_max_visibility_out` → 20573; `in_water_no_suit_out` → 6770; `tunnel_approach_out` → 18610; `combat_octant_out` → 6792; `stealth_out` → 12904; `combat_out` → 1148; `chall3_elevator_spawn_out` → 15327; `chall3_elevator_starts_out` → 15328; `chall3_elevator_hacked` → 15330; `combat_ledge_out` → 17349; `tunnel_reed_progress_01_out` → 15568; `tunnel_reed_progress_02_out` → 15572; `tunnel_reed_progress_03_out` → 15576; `combat_done_out` → 1779; `combat_reed_blocked_out` → 25467; `combat_lost_damage_message_out` → 15667; `nest_temp_lookat_out` → 7791; `nest_temp_lookat_reed_out` → 13795.

End nodes: 18: `<omitted>`; 33: `<omitted>`; 57: `<omitted>`; 69: `NonTerminating`; 1148: `<omitted>`; 1779: `<omitted>`; 2445: `<omitted>`; 2453: `<omitted>`; 2461: `<omitted>`; 2503: `<omitted>`; 6153: `<omitted>`; 6770: `<omitted>`; 6792: `<omitted>`; 7791: `<omitted>`; 9934: `<omitted>`; 12904: `<omitted>`; 13795: `<omitted>`; 15327: `NonTerminating`; 15328: `NonTerminating`; 15330: `NonTerminating`; 15568: `<omitted>`; 15572: `<omitted>`; 15576: `<omitted>`; 15667: `<omitted>`; 17349: `NonTerminating`; 18610: `<omitted>`; 20573: `<omitted>`; 21987: `<omitted>`; 25467: `<omitted>`; 25676: `<omitted>`; 25721: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 3049 / 774 | `/Data/RootChunk/sceneGraph/Data/graph/150/Data/events/1` |
| `scnDialogLineEvent` | 144 | 26 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 10 | 9936 / 2128 | `/Data/RootChunk/sceneGraph/Data/graph/436/Data/events/1` |
| `scnPlaySkAnimEvent` | 19 | 9936 / 2122 | `/Data/RootChunk/sceneGraph/Data/graph/436/Data/events/0` |
| `scneventsEquipItemToPerformer` | 3 | 12259 / 2686 | `/Data/RootChunk/sceneGraph/Data/graph/533/Data/events/0` |
| `scneventsPlayerLookAtEvent` | 3 | 6819 / 1351 | `/Data/RootChunk/sceneGraph/Data/graph/269/Data/events/0` |
| `scneventsSocket` | 34 | 165 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scneventsVFXDurationEvent` | 3 | 15669 / 3959 | `/Data/RootChunk/sceneGraph/Data/graph/800/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 92
- speech, socket_signal: 7
- socket_signal: 5
- gaze: 4
- skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 4
- skeletal_animation: 4
- skeletal_animation, props_equipment, socket_signal: 2
- speech, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, vfx: 1
- skeletal_animation, gaze, vfx, socket_signal: 1

Raw SHA-256: `3735fb88fad4b04b109ddbcb5d28b100af5a2746c06e61ef327478c22de67d05`. Binary SHA-256: `c318282c14857adc6b818dafb9774784b2accc9c5d451b40fa80f1927849caee`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_06b_paradise_technical_gameplay.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_07_finale.scene`

1655 graph nodes, 2134 edges; 459 event-bearing sections, 4121 events; 655 screenplay lines, 88 screenplay options, 39 choice nodes.

Actors: Reed (actor 0, spawnSet); Bella (actor 1, spawnSet); Theo (actor 2, spawnSet); Kurt (actor 3, spawnSet); Barwoman (actor 4, community); Reed_comms (actor 5, findInContext); Dealer (actor 6, community); Alex_comms (actor 7, findInContext); Waitress_one (actor 8, community); Waitress_two (actor 9, community); Onlooker_1 (actor 10, spawnDespawn); Onlooker_2 (actor 11, spawnDespawn); Onlooker_3 (actor 12, spawnDespawn); Chips_Clerk (actor 13, community); Chips_Clerk_02 (actor 14, community); casino_crowd_01 (actor 15, community); casino_crowd_02 (actor 16, community); V (actor 17, findInContext).

Entries: `Start 0` → 1; `Start 31` → 14069; `Start 32` → 14176; `Start 24` → 12755; `Start 33` → 14393; `Start 25` → 12843; `Start 26` → 12987; `Start 27` → 13003; `Start 14` → 8407; `whispering_lipsync` → 11704; `roulette_debug` → 1168; `Start 18` → 10522; `waitress_preview` → 7426; `cinedebug_kurt` → 7542.

Exits: `End 0` → 2; `End1` → 4363.

End nodes: 2: `NonTerminating`; 4363: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 23 | 3236 / 871 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/29` |
| `scnChangeIdleAnimEvent` | 133 | 1735 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnDialogLineEvent` | 440 | 1735 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scnGameplayTransitionEvent` | 13 | 2135 / 316 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/15` |
| `scnIKEvent` | 26 | 2135 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |
| `scnLookAtAdvancedEvent` | 216 | 1744 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/6` |
| `scnLookAtEvent` | 786 | 1735 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 642 | 1735 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPoseCorrectionEvent` | 14 | 2135 / 305 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/8` |
| `scnUnmountEvent` | 13 | 2135 / 321 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/19` |
| `scneventsAttachPropToNode` | 2 | 14221 / 12497 | `/Data/RootChunk/sceneGraph/Data/graph/1577/Data/events/2` |
| `scneventsAttachPropToPerformer` | 81 | 2086 / 283 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/3` |
| `scneventsAttachPropToWorld` | 113 | 2135 / 314 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/13` |
| `scneventsCameraParamsEvent` | 11 | 2086 / 281 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/1` |
| `scneventsEquipItemToPerformer` | 6 | 2086 / 284 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 13 | 2135 / 319 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/18` |
| `scneventsSocket` | 719 | 1735 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scneventsSpawnEntityEvent` | 11 | 5369 / 3086 | `/Data/RootChunk/sceneGraph/Data/graph/255/Data/events/6` |
| `scneventsUnequipItemFromPerformer` | 12 | 4038 / 1655 | `/Data/RootChunk/sceneGraph/Data/graph/126/Data/events/15` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 7223 / 4722 | `/Data/RootChunk/sceneGraph/Data/graph/424/Data/events/2` |
| `scneventsVFXDurationEvent` | 2 | 3786 / 1177 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/13` |
| `scneventsVFXEvent` | 844 | 2175 / 342 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- vfx, socket_signal: 51
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 44
- speech, vfx: 43
- speech, vfx, socket_signal: 31
- speech, skeletal_animation, gaze, socket_signal: 30
- speech: 27
- gaze: 14
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 13
- speech, socket_signal: 12
- gaze, vfx: 10
- skeletal_animation, socket_signal: 9
- skeletal_animation, gaze, vfx, socket_signal: 8
- speech, gaze, vfx, socket_signal: 7
- props_equipment, vfx, socket_signal: 7
- skeletal_animation, gaze, props_equipment, socket_signal: 6
- speech, skeletal_animation, socket_signal: 6
- speech, skeletal_animation: 6
- props_equipment, vfx: 6
- audio, vfx: 6
- skeletal_animation, gaze, props_equipment, vfx, socket_signal, entity_lifecycle: 6
- speech, skeletal_animation, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 5
- speech, skeletal_animation, gaze, vfx, socket_signal: 5
- socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 4
- skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze: 4
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, gaze: 4
- skeletal_animation, gaze: 4
- skeletal_animation, props_equipment, vfx, socket_signal: 4
- idle_animation, gaze: 4
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal, entity_lifecycle: 3
- skeletal_animation, idle_animation, gaze: 3
- skeletal_animation, gaze, props_equipment, vfx: 3
- gaze, audio, vfx: 3
- vfx: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- gaze, socket_signal: 2
- skeletal_animation, camera, socket_signal: 2
- camera: 2
- speech, gaze, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- skeletal_animation, gaze, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- idle_animation, socket_signal, animation_state: 1
- skeletal_animation, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, props_equipment, vfx, socket_signal, entity_lifecycle: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, props_equipment: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- socket_signal, animation_state: 1
- skeletal_animation, props_equipment, socket_signal, entity_lifecycle: 1
- props_equipment: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1

Raw SHA-256: `9acf17520ec18839770a04b7c9b59151de5af1dda0f1583131dbf67b447a595b`. Binary SHA-256: `4481904081d3b12ad88087e2dee0ef0ed6e8174d90600b49fbad1f9f07045561`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_07_finale.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_08_reed_conversation.scene`

651 graph nodes, 734 edges; 116 event-bearing sections, 662 events; 214 screenplay lines, 19 screenplay options, 9 choice nodes.

Actors: Reed (actor 0, spawnSet); Jago (actor 1, community); Kurt_guard_02_top_lift (actor 2, community); Concierge (actor 3, community); Lizzy (actor 4, spawnSet); Alex (actor 5, findInContext); Checkpoint_guard (actor 6, community); Tech_floor_soldier (actor 7, community); Boulder (actor 8, community); Party_guest_01 (actor 9, spawnDespawn); Party_guest_02 (actor 10, spawnDespawn); Bennet (actor 11, community); Kurt_guard_07 (actor 12, community); ElevatorGuard_01 (actor 13, community); ElevatorGuard_02 (actor 14, community); ElevatorGuard_03 (actor 15, community); drone_1 (actor 16, spawnDespawn); drone_2 (actor 17, spawnDespawn); Ziggy (actor 18, community); Lizzys_fan (actor 19, community); Lobby_Mech_01 (actor 20, community); Lobby_Mech_02 (actor 21, community); tapes_guard (actor 22, spawnDespawn); Alex_holo (actor 23, spawnSet); Reed_holo (actor 24, spawnSet); drone_01_carrier (actor 25, spawner); drone_02_carrier (actor 26, spawner); alex_car (actor 27, spawner); V (actor 28, findInContext).

Entries: `Start 0` → 1; `combat_version` → 3598; `previe_provoke` → 4824; `lizzy_dlg` → 763; `Start 15` → 5438; `reed_preview` → 4854; `cinedebug_security` → 1949; `combat_debug` → 3241; `combat_version_outside` → 3853; `combat_version_mechs_idle` → 4442; `combat_version_mechs_ready` → 4443; `combat_version_exit` → 5047; `combat_version_left` → 3882; `combat_version_right` → 3884; `combat_version_center` → 3885; `combat_version_snipers` → 3900; `combat_version_push` → 3909; `combat_version_turrets` → 3930; `combat_version_mechs` → 3934; `combat_version_abandon` → 3953.

Exits: `End_peaceful_version` → 649; `Out_scene_done` → 3652; `End_combat_version` → 3657; `combat_version_outside_out` → 3855; `combat_version_mechs_idle_out` → 4446; `combat_version_mech_02_ready` → 4447; `combat_version_mech_01_ready` → 4458; `combat_version_exit_out` → 5049; `combat_version_center_out` → 3890; `combat_version_left_out` → 3893; `combat_version_right_out` → 3898; `combat_version_snipers_out` → 3902; `combat_version_push_out` → 3911; `combat_version_turrets_out` → 3936; `combat_version_mechs_out` → 3940; `combat_version_abandon_out` → 3956; `Out_combat` → 6349.

End nodes: 649: `NonTerminating`; 3652: `<omitted>`; 3657: `<omitted>`; 3855: `<omitted>`; 3890: `<omitted>`; 3893: `<omitted>`; 3898: `<omitted>`; 3902: `<omitted>`; 3911: `<omitted>`; 3936: `<omitted>`; 3940: `<omitted>`; 3956: `<omitted>`; 4446: `<omitted>`; 4447: `<omitted>`; 4458: `NonTerminating`; 5049: `<omitted>`; 6349: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 3376 / 760 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/4` |
| `scnDialogLineEvent` | 156 | 415 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnGameplayTransitionEvent` | 14 | 1069 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/7` |
| `scnIKEvent` | 28 | 1069 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/1` |
| `scnLookAtAdvancedEvent` | 5 | 770 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/4` |
| `scnLookAtEvent` | 159 | 770 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/2` |
| `scnPlaySkAnimEvent` | 123 | 770 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |
| `scnPoseCorrectionEvent` | 4 | 3381 / 784 | `/Data/RootChunk/sceneGraph/Data/graph/126/Data/events/0` |
| `scnUnmountEvent` | 14 | 1069 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/6` |
| `scneventsEquipItemToPerformer` | 14 | 2396 / 402 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 14 | 1069 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/5` |
| `scneventsSocket` | 114 | 415 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 4539 / 1843 | `/Data/RootChunk/sceneGraph/Data/graph/268/Data/events/47` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 27
- skeletal_animation, socket_signal: 10
- speech, skeletal_animation, gaze, socket_signal: 9
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 8
- gaze: 8
- skeletal_animation, gaze, socket_signal: 7
- speech, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- socket_signal: 4
- skeletal_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, props_equipment, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- speech, gaze, socket_signal: 3
- skeletal_animation: 3
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze: 2
- props_equipment, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- idle_animation: 1
- idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- gaze, socket_signal: 1

Raw SHA-256: `795d4cd8071a6b3cc21e61863d254aaaf7b201cb44dce3e0b2b35d84d6a59373`. Binary SHA-256: `8caffd852fbb96f71c645abcd5aedb34151a0b2a1a7fcc65980c5ec3531fb77b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_08_reed_conversation.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_09_reed_summary.scene`

17 graph nodes, 17 edges; 3 event-bearing sections, 12 events; 12 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Reed (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 12 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `8c993b45add6894c285ab8cf5e88a51a9bef68b05b514194460a5b4f8b5449f3`. Binary SHA-256: `02d93ec1789d8185eda1ed8116eec372236ff6ca3f496f6f18e3ba1510be75d2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_09_reed_summary.scene" --events
```

