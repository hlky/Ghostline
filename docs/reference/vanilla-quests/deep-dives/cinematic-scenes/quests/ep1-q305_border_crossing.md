# Leave in Silence: scene presentation

Journal identity: `ep1/quests/main_quest/q305_border_crossing`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q305_border_crossing.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene`

109 graph nodes, 124 edges; 10 event-bearing sections, 29 events; 13 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Iguana (actor 0, spawner); Johnny (actor 1, spawnDespawn); IguanaQ203 (actor 2, spawner); NibblesPuff (actor 3, community); IguanaPuff (actor 4, spawner); Player (actor 5, findInContext).

Entries: `mws_wat_02_in` → 1; `mws_wat_02_iguana_cat_in` → 560; `johnny_jamming` → 690; `mws_wat_02_q203_in` → 478.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 7 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 382 / 329 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/5` |
| `scnIKEvent` | 2 | 382 / 324 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/1` |
| `scnLookAtEvent` | 1 | 114 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scnPlaySkAnimEvent` | 7 | 114 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scnUnmountEvent` | 1 | 382 / 328 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 1 | 382 / 326 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/3` |
| `scneventsSocket` | 12 | 114 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 3
- idle_animation: 2
- socket_signal: 2
- skeletal_animation, gaze, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `33bb5b12f99603e0e79c811b20b9fef3f6ff13a7caf8a7648e3ac3ff382a84ff`. Binary SHA-256: `1e4a5430ce064434338c0abd2ac2f2b6f742a21ad036cdc209a64074c1f2abf6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_11_border_crossing.scene`

1824 graph nodes, 2668 edges; 349 event-bearing sections, 2775 events; 507 screenplay lines, 71 screenplay options, 27 choice nodes.

Actors: reed (actor 0, spawnSet); myers (actor 1, spawnSet); songbird (actor 2, spawnSet); helicopter_crew1 (actor 3, community); helicopter_crew_2 (actor 4, community); secret_service_main (actor 5, community); secret_service_reward (actor 6, community); ripperdoc (actor 7, community); background_agent_01 (actor 8, community); background_agent_02 (actor 9, community); background_agent_03 (actor 10, community); nusa_soldier_01 (actor 11, community); nusa_soldier_03 (actor 12, community); nusa_soldier_04 (actor 13, community); nusa_soldier_05 (actor 14, community); sniper1 (actor 15, community); sniper2 (actor 16, community); nusa_soldier_06 (actor 17, community); nusa_soldier_07 (actor 18, community); nusa_soldier_08 (actor 19, community); foreground_lane_soldier_1 (actor 20, community); foreground_lane_soldier_2 (actor 21, community); foreground_lane_soldier_3 (actor 22, community); foreground_lane_soldier_4 (actor 23, community); foreground_lane_soldier_5 (actor 24, community); foreground_lane_soldier_6 (actor 25, community); foreground_lane_soldier_7 (actor 26, community); foreground_lane_soldier_8 (actor 27, community); nusa_soldier_02 (actor 28, community); soldier_passage_001 (actor 29, community); soldier_passage_002 (actor 30, community); soldier_passage_003 (actor 31, community); soldier_passage_004 (actor 32, community); soldier_passage_005 (actor 33, community); socal_border_guard_passage_001 (actor 34, community); convoy_agent_01 (actor 35, community); convoy_agent_02 (actor 36, community); foreground_lane_soldier_9 (actor 37, community); foregound_lane_soldier_10 (actor 38, community); foreground_agent_001 (actor 39, community); convoy_agent_03 (actor 40, community); convoy_agent_04 (actor 41, community); socal_bg_lane (actor 42, community); socal_bg_lane_02 (actor 43, community); socal_bg_lane_03 (actor 44, community); agent_bg_lane (actor 45, community); mech_patrolling_bg_lane_001 (actor 46, community); soldier_patrolling_bg_lane_001 (actor 47, community); soldier_patrolling_bg_lane_002 (actor 48, community); agent_blockade (actor 49, spawnSet); policeman_1 (actor 50, spawnSet); driver_1 (actor 51, spawnSet); driver_2 (actor 52, spawnSet); traffic_droid_1 (actor 53, community); traffic_droid_2 (actor 54, community); traffic_droid_3 (actor 55, community); traffic_droid_4 (actor 56, community); traffic_droid_5 (actor 57, community); traffic_droid_6 (actor 58, community); traffic_droid_7 (actor 59, community); traffic_droid_8 (actor 60, community); traffic_socal_1 (actor 61, community); traffic_socal_2 (actor 62, community); traffic_socal_3 (actor 63, community); traffic_socal_4 (actor 64, community); traffic_socal_5 (actor 65, community); traffic_socal_6 (actor 66, community); traffic_socal_7 (actor 67, community); traffic_socal_8 (actor 68, community); traffic_socal_9 (actor 69, community); traffic_socal_10 (actor 70, community); traffic_socal_11 (actor 71, community); traffic_socal_12 (actor 72, community); traffic_civ_out_01 (actor 73, community); traffic_civ_out_02 (actor 74, community); traffic_civ_out_03 (actor 75, community); traffic_civ_out_04 (actor 76, community); traffic_civ_out_05 (actor 77, community); traffic_civ_out_06 (actor 78, community); traffic_civ_out_07 (actor 79, community); traffic_civ_out_08 (actor 80, community); traffic_civ_out_09 (actor 81, community); traffic_civ_out_10 (actor 82, community); traffic_civ_out_11 (actor 83, community); traffic_civ_out_12 (actor 84, community); traffic_civ_out_13 (actor 85, community); traffic_civ_out_14 (actor 86, community); traffic_civ_out_15 (actor 87, community); traffic_civ_out_16 (actor 88, community); traffic_socal_commander (actor 89, community); reed_car (actor 90, spawnSet); sbhelicopter (actor 91, community); myers_av (actor 92, community); nusa_av1 (actor 93, community); stretchers (actor 94, community); nusa_av2 (actor 95, community); nusa_car3 (actor 96, community); nusa_car4 (actor 97, community); nusa_car1 (actor 98, community); nusa_suv5 (actor 99, community); nusa_av3 (actor 100, community); nusa_av4 (actor 101, community); convoy_suv_01 (actor 102, community); av_bg_lane (actor 103, community); nusa_av_6 (actor 104, community); nusa_av_7 (actor 105, community); nusa_av_8 (actor 106, community); traffic_car_1 (actor 107, community); traffic_car_2 (actor 108, community); traffic_car_3 (actor 109, community); traffic_car_4 (actor 110, community); traffic_car_5 (actor 111, community); traffic_car_6 (actor 112, community); traffic_car_7 (actor 113, community); traffic_car_8 (actor 114, community); traffic_car_9 (actor 115, community); traffic_car_10 (actor 116, community); traffic_car_11 (actor 117, community); traffic_car_12 (actor 118, community); traffic_car_13 (actor 119, community); traffic_car_14 (actor 120, community); traffic_car_15 (actor 121, community); traffic_car_16 (actor 122, community); traffic_car_17 (actor 123, community); traffic_car_18 (actor 124, community); traffic_car_19 (actor 125, community); traffic_car_20 (actor 126, community); traffic_car_21 (actor 127, community); traffic_car_22 (actor 128, community); traffic_car_23 (actor 129, community); traffic_car_24 (actor 130, community); traffic_car_25 (actor 131, community); traffic_car_26 (actor 132, community); traffic_car_27 (actor 133, community); traffic_car_28 (actor 134, community); traffic_car_29 (actor 135, community); traffic_car_30 (actor 136, community); traffic_car_31 (actor 137, community); traffic_car_32 (actor 138, community); traffic_car_33 (actor 139, community); traffic_car_34 (actor 140, community); traffic_car_35 (actor 141, community); traffic_car_36 (actor 142, community); traffic_car_37 (actor 143, community); traffic_car_38 (actor 144, community); traffic_car_39 (actor 145, community); traffic_car_40 (actor 146, community); traffic_car_41 (actor 147, community); traffic_car_42 (actor 148, community); traffic_car_43 (actor 149, community); traffic_car_44 (actor 150, community); traffic_car_45 (actor 151, community); traffic_car_46 (actor 152, community); traffic_retreating_car (actor 153, community); traffic_overtaking_car (actor 154, community); reed_car_test (actor 155, spawnSet); V (actor 156, findInContext).

Entries: `q305_11_border_crossing_in` → 1; `Start 36` → 8901; `Start 37` → 8913; `Start 40` → 8923; `Start 41` → 8925; `Start 44` → 8936; `Start 45` → 8942; `Start3` → 7479; `Start 46` → 8972; `Start 135` → 16347; `Start 49` → 9075; `Start 51` → 9087; `Start 136` → 16467; `Start 53` → 9117; `preview` → 274; `Start 137` → 16492; `Start 138` → 16498; `Start 116` → 15038; `Start 117` → 15058; `Start 58` → 9243; `helicopter_leaving` → 3352; `Start 120` → 15147; `Start 59` → 9252; `Start 60` → 9254; `Start 64` → 9277; `Start 16` → 7803; `Start 90` → 12231; `Start 65` → 9309; `Start 139` → 16702; `Start 92` → 12282; `Start 17` → 7871; `Start 18` → 7882; `Start 19` → 7887; `Start 20` → 7900; `Start 21` → 7911; `Start 22` → 7915; `Start 67` → 9397; `Start 68` → 9404; `Start 141` → 16790; `Start 23` → 7996; `reed_sit` → 15368; `Start 71` → 9478; `Start 73` → 9540; `Start 79` → 11071; `Start 80` → 11073; `Start 105` → 14050; `Start 81` → 11104; `Start 82` → 11114; `Start 74` → 9657; `Start 143` → 17052; `Start 98` → 12639; `Start 109` → 14248; `Start 126` → 15742; `Start 75` → 9868; `Start 127` → 15811; `Start 27` → 8441; `Start 28` → 8505; `Start 112` → 14442; `Start 7` → 7091; `Start 5` → 4152; `Start 113` → 14486; `Start 76` → 10092; `Start 145` → 17483; `Start 32` → 8691; `Start 129` → 16112; `Start 130` → 16114; `Start 131` → 16122; `Start 132` → 16126; `Start 133` → 16128; `farewell_with_myers` → 4369; `car_stop_units_placement` → 7321; `Start 33` → 8803; `Start 34` → 8805; `Start 134` → 16188; `Start 35` → 8829.

Exits: `End 6` → 8903; `Prefetch_out` → 15100; `q305_11_border_crossing_end` → 4276.

End nodes: 4276: `<omitted>`; 8903: `<omitted>`; 15100: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 33 | 399 / 370 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/17` |
| `scnChangeIdleAnimEvent` | 162 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 319 | 97 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/13` |
| `scnGameplayActionEvent` | 9 | 97 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/31` |
| `scnGameplayTransitionEvent` | 23 | 97 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/26` |
| `scnIKEvent` | 70 | 97 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scnLookAtAdvancedEvent` | 50 | 3187 / 1760 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/122` |
| `scnLookAtEvent` | 706 | 97 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 385 / 338 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/0` |
| `scnPlaySkAnimEvent` | 565 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPoseCorrectionEvent` | 24 | 399 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/10` |
| `scnUnmountEvent` | 23 | 97 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/27` |
| `scneventsAttachPropToPerformer` | 10 | 500 / 408 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/3` |
| `scneventsAttachPropToWorld` | 4 | 3 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsCameraParamsEvent` | 25 | 399 / 368 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/15` |
| `scneventsEquipItemToPerformer` | 43 | 2180 / 820 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/13` |
| `scneventsMountEvent` | 2 | 97 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/32` |
| `scneventsRagdollEvent` | 2 | 3187 / 1583 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/36` |
| `scneventsSetAnimFeatureEvent` | 61 | 97 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/21` |
| `scneventsSetAnimsetWeight` | 20 | 97 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsSocket` | 609 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 8840 / 5171 | `/Data/RootChunk/sceneGraph/Data/graph/510/Data/events/10` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 5144 / 2354 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/8` |
| `scneventsVFXEvent` | 11 | 399 / 376 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/23` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 68
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 44
- gaze: 42
- speech, skeletal_animation, gaze, socket_signal: 15
- skeletal_animation, gaze, socket_signal: 13
- skeletal_animation, socket_signal: 10
- speech, socket_signal: 9
- speech, skeletal_animation, socket_signal: 9
- socket_signal: 8
- props_equipment, socket_signal: 8
- skeletal_animation, gaze: 7
- speech, gaze: 6
- speech, skeletal_animation, gaze, socket_signal, animation_state: 5
- speech, skeletal_animation, gaze: 5
- skeletal_animation, idle_animation, socket_signal: 5
- skeletal_animation: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 3
- idle_animation, gameplay_action: 3
- skeletal_animation, idle_animation: 3
- gaze, socket_signal: 3
- skeletal_animation, props_equipment, socket_signal: 3
- camera: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- ik, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 2
- skeletal_animation, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- socket_signal, animation_state: 2
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, camera, socket_signal, animation_state: 2
- props_equipment: 2
- animation_state: 2
- props_equipment, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, camera, socket_signal, animation_state: 1
- idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, animation_state: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, camera, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- idle_animation: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- idle_animation, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, ik, camera, socket_signal, animation_state: 1

Raw SHA-256: `97cce75b54a372db889c2c478fe565820738824d1c54265eec356b53019a23b6`. Binary SHA-256: `ae78f8c943ef2bb20442666533c899ce2b8e8ef75f2ba6d595e07b9783f342f8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_11_border_crossing.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_12_johnny.scene`

260 graph nodes, 298 edges; 73 event-bearing sections, 792 events; 239 screenplay lines, 53 screenplay options, 9 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); v_mirror_tpp_female (actor 1, spawnDespawn); v_mirror_tpp_male (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `Start 0` → 1; `Start 2` → 612; `Start2` → 956; `Start 4` → 1591; `Start1` → 754.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 28 | 770 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/10` |
| `scnChangeIdleAnimEvent` | 16 | 886 / 432 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/1` |
| `scnDialogLineEvent` | 89 | 770 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnGameplayTransitionEvent` | 21 | 832 / 241 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/9` |
| `scnIKEvent` | 42 | 832 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/2` |
| `scnLookAtAdvancedEvent` | 5 | 916 / 719 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/11` |
| `scnLookAtEvent` | 125 | 770 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/5` |
| `scnOverridePhantomParamsEvent` | 10 | 832 / 248 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/11` |
| `scnPlaySkAnimEvent` | 210 | 606 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 14 | 770 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/9` |
| `scnUnmountEvent` | 21 | 832 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/8` |
| `scneventsAttachPropToPerformer` | 2 | 1590 / 1422 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 1590 / 1436 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/8` |
| `scneventsCameraParamsEvent` | 8 | 832 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |
| `scneventsEquipItemToPerformer` | 15 | 770 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 21 | 832 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/5` |
| `scneventsSocket` | 152 | 606 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsSpawnEntityEvent` | 1 | 1590 / 1437 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/9` |
| `scneventsUnequipItemFromPerformer` | 7 | 770 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/12` |
| `scneventsVFXEvent` | 4 | 850 / 318 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 14
- skeletal_animation, gaze, socket_signal: 10
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal, animation_state: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, socket_signal: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, props_equipment, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, audio, vfx: 1
- skeletal_animation, camera, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 1
- speech: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, entity_lifecycle: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `2450446cbee67b1f42090e36cfa0c2a4bec378fd2bbefcb805b7e88cd0bd3564`. Binary SHA-256: `2389f1f738efe13a68cf953415343b7d3956a4efeb74098b3c4c1392b4345fde`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_12_johnny.scene" --events
```

