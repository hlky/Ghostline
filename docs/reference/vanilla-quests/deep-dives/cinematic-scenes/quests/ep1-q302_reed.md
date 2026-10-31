# Lucretia My Reflection: scene presentation

Journal identity: `ep1/quests/main_quest/q302_reed`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q302_reed.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\main_quests\q302\scenes\q302_01_escape_the_cz.scene`

1231 graph nodes, 1768 edges; 117 event-bearing sections, 393 events; 180 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Myers (actor 0, spawnSet); Drone (actor 1, community); small_drone_1 (actor 2, spawnDespawn); small_drone_2 (actor 3, spawnDespawn); small_drone_3 (actor 4, spawnDespawn); small_drone_4 (actor 5, spawnDespawn); small_drone_5 (actor 6, spawnDespawn); small_drone_6 (actor 7, spawnDespawn); small_drone_7 (actor 8, spawnDespawn); small_drone_8 (actor 9, spawnDespawn); small_drone_9 (actor 10, spawnDespawn); small_drone_10 (actor 11, spawnDespawn); small_drone_11 (actor 12, spawnDespawn); small_drone_12 (actor 13, spawnDespawn); small_drone_13 (actor 14, spawnDespawn); small_drone_14 (actor 15, spawnDespawn); small_drone_15 (actor 16, spawnDespawn); small_drone_16 (actor 17, spawnDespawn); small_drone_17 (actor 18, spawnDespawn); small_drone_18 (actor 19, spawnDespawn); small_drone_19 (actor 20, spawnDespawn); q302_hotel_militia_1 (actor 21, community); q302_hotel_militia_2 (actor 22, community); q302_hotel_militia_5 (actor 23, community); q302_hotel_militia_8 (actor 24, community); q302_hotel_militia_7 (actor 25, community); Songbird_holo (actor 26, findInContext); q302_drone_flyby_1 (actor 27, spawnDespawn); q302_drone_flyby_2 (actor 28, spawnDespawn); q302_hotel_militia_10 (actor 29, community); q302_hotel_militia_4 (actor 30, community); q302_hotel_militia_3 (actor 31, community); q302_escape_car (actor 32, spawner); q302_escape_car_alt (actor 33, spawner); q302_hotel_av_01 (actor 34, community); q302_hotel_av_02 (actor 35, community); q302_hotel_av_03 (actor 36, community); q302_hotel_av_04 (actor 37, community); Player (actor 38, findInContext); Songbird (actor 39, findInContext).

Entries: `q302_01_escape_elevator_line` → 11028; `arrived_at_parking_prev` → 8652; `drone_surveillance_prev` → 2714; `drone_distract_prev` → 10101; `drone_intro_prev` → 1632; `Pre_drone` → 1664; `q302_01_escape_in` → 542; `on foot akebono` → 9385; `elevator_prev` → 8419; `upper_floor_prev` → 2336; `q302_01_escape_chat` → 10924; `get_into_car_prev` → 8521.

Exits: `Militia alerted after skybridge` → 2608; `Escape_chase` → 3231; `q302_01_escape_out` → 873; `patrols_cleanup` → 5778; `Player has entered the lobby` → 2176; `Combat trigerred from the restaurant` → 2195; `Player exit the vent` → 2201; `clear` → 5896.

End nodes: 873: `NonTerminating`; 2176: `NonTerminating`; 2195: `NonTerminating`; 2201: `NonTerminating`; 2608: `NonTerminating`; 3231: `NonTerminating`; 5778: `NonTerminating`; 5896: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 1625 / 288 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/6` |
| `scnChangeIdleAnimEvent` | 12 | 1360 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |
| `scnDialogLineEvent` | 152 | 550 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 1563 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/14` |
| `scnIKEvent` | 6 | 1563 / 212 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/6` |
| `scnLookAtEvent` | 34 | 1360 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/2` |
| `scnPlaySkAnimEvent` | 87 | 1360 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/7` |
| `scnUnmountEvent` | 3 | 1563 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/13` |
| `scneventsAttachPropToPerformer` | 6 | 8643 / 4541 | `/Data/RootChunk/sceneGraph/Data/graph/675/Data/events/4` |
| `scneventsCameraParamsEvent` | 2 | 2475 / 688 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 4 | 1563 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/10` |
| `scneventsSocket` | 41 | 1360 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/3` |
| `scneventsVFXDurationEvent` | 1 | 1625 / 292 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/10` |
| `scneventsVFXEvent` | 35 | 1625 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 79
- gaze: 7
- skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, vfx: 2
- skeletal_animation: 2
- speech, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, camera, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- vfx, socket_signal: 1

Raw SHA-256: `4d1d3a21e6f0aaf3998300bc88e882a4ce5e3df546dea1a3ff1c6fb26474d4ff`. Binary SHA-256: `367734b0408cdb06d2f29b242279b0818994a49bc7ff32d5ee2c843d36eac1e5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_01_escape_the_cz.scene" --events
```

## `ep1\quest\main_quests\q302\scenes\q302_02_spider.scene`

1593 graph nodes, 2013 edges; 207 event-bearing sections, 1410 events; 319 screenplay lines, 19 screenplay options, 14 choice nodes.

Actors: Myers (actor 0, spawnSet); Songbird (actor 1, spawnDespawn); Tank_Pilot (actor 2, spawnSet); Spidertank_actor (actor 3, spawnSet); Johnny (actor 4, spawnDespawn); kurtz_militia_01 (actor 5, community); kurtz_militia_03 (actor 6, community); kurtz_militia_02 (actor 7, community); kurtz_militia_04 (actor 8, community); kurtz_militia_05 (actor 9, community); kurtz_militia_06 (actor 10, community); kurtz_militia_07 (actor 11, community); kurtz_militia_08 (actor 12, community); kurtz_militia_09 (actor 13, community); kurtz_militia_10 (actor 14, community); kurtz_militia_11 (actor 15, community); repair_drone_1 (actor 16, community); repair_drone_2 (actor 17, community); combat_drone_1 (actor 18, community); combat_drone_2 (actor 19, community); combat_drone_3 (actor 20, community); combat_drone_4 (actor 21, community); combat_drone_5 (actor 22, community); combat_drone_6 (actor 23, community); myers_chimera_follower (actor 24, spawnSet); fake_myers (actor 25, spawnDespawn); vehicle_shooting_spot (actor 26, spawner); Player (actor 27, findInContext).

Entries: `q302_02_spider_intro_in` → 1; `elevator_reached` → 6785; `q302_spider_arena` → 177; `tank_movement_prev` → 284; `Section 2 starts` → 1984; `main_hall_prev` → 327; `1st_encounter` → 1993; `tank_plugin` → 374; `Tank defeated` → 2068; `Start 25` → 10423; `tank_escape` → 462; `failstates_prev` → 2142; `balcony_salvo` → 593; `spidertank_fall` → 640; `drone_deployment_prev` → 5634; `Start 23` → 7395; `Start 19` → 4091; `Start 26` → 10816; `glass_floor_failstate` → 10898; `sec_1_tank_rising` → 2680; `corridor_chase_reactions` → 7740; `escalator_prev` → 4418; `tank_crashing_gate_prev` → 3057; `Start 21` → 4856; `after_the_fall_prev` → 1564; `before_connection` → 1637.

Exits: `q302_02_out` → 55; `sec_1_combat` → 1798; `boss_out` → 1806; `Section2_corridor` → 4156; `sec_1_tank_fighting` → 2686.

End nodes: 55: `NonTerminating`; 1798: `NonTerminating`; 1806: `NonTerminating`; 2686: `NonTerminating`; 4156: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 68 | 388 / 311 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/2` |
| `scnChangeIdleAnimEvent` | 98 | 241 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scnDialogLineEvent` | 195 | 241 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnGameplayTransitionEvent` | 9 | 258 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/14` |
| `scnIKEvent` | 18 | 258 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/7` |
| `scnLookAtEvent` | 90 | 241 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnPlaySkAnimEvent` | 345 | 241 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnUnmountEvent` | 9 | 258 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/13` |
| `scneventsAttachPropToPerformer` | 10 | 1562 / 1014 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/10` |
| `scneventsAttachPropToWorld` | 6 | 3262 / 2037 | `/Data/RootChunk/sceneGraph/Data/graph/190/Data/events/18` |
| `scneventsCameraParamsEvent` | 33 | 388 / 417 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/58` |
| `scneventsEquipItemToPerformer` | 1 | 399 / 606 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 9 | 258 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/10` |
| `scneventsSocket` | 323 | 241 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scneventsVFXDurationEvent` | 5 | 285 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scneventsVFXEvent` | 191 | 285 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 81
- skeletal_animation, socket_signal: 13
- speech, skeletal_animation, camera, audio, vfx, socket_signal: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- idle_animation: 5
- skeletal_animation, idle_animation: 5
- vfx: 5
- socket_signal: 4
- skeletal_animation, gaze, socket_signal: 4
- skeletal_animation: 4
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 2
- skeletal_animation, idle_animation, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, idle_animation, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, camera, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation: 2
- idle_animation, gaze: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, audio, vfx, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 2
- skeletal_animation, vfx: 2
- skeletal_animation, gaze, props_equipment: 2
- gaze: 2
- camera: 2
- vfx, socket_signal: 2
- idle_animation, vfx: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, vfx, socket_signal: 1
- speech, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, audio, socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, audio, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment: 1

Raw SHA-256: `c6dd4e63edf1bad91dd0b2a227bb014d7784d3bcdacf9a174658117acc3d1c0b`. Binary SHA-256: `f2b9ec38101c39ece4d8e45e5f59a8f622106c0b3be022b2325bae824bdf7b06`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_02_spider.scene" --events
```

## `ep1\quest\main_quests\q302\scenes\q302_03_subway.scene`

580 graph nodes, 825 edges; 82 event-bearing sections, 615 events; 176 screenplay lines, 24 screenplay options, 14 choice nodes.

Actors: Myers (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Songbird (actor 2, findInContext); Player (actor 3, findInContext).

Entries: `q302_02_subway_in` → 1; `in_elevator_prev` → 1608; `jump_out_cart_prev` → 3224; `Start 11` → 4926; `push_cart_prev` → 1760; `holo` → 2454; `dark_tunnel` → 3038; `sickness_prev` → 1516; `crossroads_prev` → 1557; `light_tunnel` → 3701; `kress_street_chat_prev` → 3709.

Exits: `q302_02_subway_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 1695 / 742 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/3` |
| `scnChangeIdleAnimEvent` | 56 | 18 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 143 | 15 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 1039 / 522 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/20` |
| `scnIKEvent` | 8 | 1039 / 514 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/13` |
| `scnLookAtEvent` | 92 | 18 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 148 | 15 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 4 | 1039 / 521 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/19` |
| `scneventsAttachPropToPerformer` | 6 | 2050 / 1265 | `/Data/RootChunk/sceneGraph/Data/graph/142/Data/events/5` |
| `scneventsAttachPropToWorld` | 1 | 4747 / 3307 | `/Data/RootChunk/sceneGraph/Data/graph/470/Data/events/1` |
| `scneventsCameraParamsEvent` | 2 | 2712 / 1471 | `/Data/RootChunk/sceneGraph/Data/graph/174/Data/events/16` |
| `scneventsSetAnimFeatureEvent` | 4 | 1039 / 517 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/16` |
| `scneventsSocket` | 123 | 50 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsVFXEvent` | 17 | 2712 / 1453 | `/Data/RootChunk/sceneGraph/Data/graph/174/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 15
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 4
- vfx: 4
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- idle_animation: 2
- skeletal_animation, gaze: 2
- gaze: 2
- idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1

Raw SHA-256: `294090e9fc38ea81ff5de6696ee6eb28562d1e602da2eae36ea2e3558ef743cf`. Binary SHA-256: `a917996569bd083c85e8bed080b224e586bc1bdc1d796df576ed4e9ad8b9cd43`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_03_subway.scene" --events
```

## `ep1\quest\main_quests\q302\scenes\q302_04_squot.scene`

1552 graph nodes, 2091 edges; 216 event-bearing sections, 2497 events; 512 screenplay lines, 93 screenplay options, 44 choice nodes.

Actors: Myers (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Taylor (actor 2, community); Jacob (actor 3, community); Lloyd (actor 4, spawnSet); KURT_VOICE (actor 5, findInContext); radio_journalist (actor 6, findInContext); kurtz_av_squot_01 (actor 7, community); kurtz_av_squot_02 (actor 8, community); kurtz_av_squot_03 (actor 9, community); Player (actor 10, findInContext).

Entries: `q302_04_squot_in` → 1; `removing_batteries_from_drone` → 3941; `prev_misfits_come` → 4024; `radio_propaganda` → 6720; `jacob_dispose_prev` → 4133; `morning_after_prev` → 4253; `myers_and_misfits_prev` → 4286; `opening_door` → 1736; `beer_break` → 1747; `going_to_sleep_prev` → 2007; `balcony_prev` → 2027; `oath_prev` → 11251; `taylor_talk_prev` → 9956; `misfits_optional_dialogue` → 9959; `post_combat_in` → 6066; `prev_johnny_ele` → 4913; `airdrop_prev` → 4919; `jacob_test_fight` → 5058; `power_generator` → 2482.

Exits: `q302_04_squot_out` → 2; `clear_scene` → 5682; `misfits_combat_out` → 6064; `misfits_combat_scene_cleared` → 6192.

End nodes: 2: `NonTerminating`; 5682: `<omitted>`; 6064: `NonTerminating`; 6192: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 648 / 1112 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/6` |
| `scnChangeIdleAnimEvent` | 241 | 41 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scnDialogLineEvent` | 433 | 26 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 24 | 41 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scnIKEvent` | 48 | 41 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnLookAtAdvancedEvent` | 4 | 393 / 469 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/12` |
| `scnLookAtEvent` | 415 | 41 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 1 | 399 / 584 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/7` |
| `scnPlaySkAnimEvent` | 693 | 41 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPoseCorrectionEvent` | 1 | 1995 / 2120 | `/Data/RootChunk/sceneGraph/Data/graph/146/Data/events/2` |
| `scnUnmountEvent` | 24 | 41 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scneventsAttachPropToNode` | 3 | 3484 / 2763 | `/Data/RootChunk/sceneGraph/Data/graph/218/Data/events/15` |
| `scneventsAttachPropToPerformer` | 21 | 187 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scneventsAttachPropToWorld` | 15 | 373 / 302 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/8` |
| `scneventsCameraParamsEvent` | 19 | 410 / 688 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/7` |
| `scneventsEquipItemToPerformer` | 7 | 3946 / 3019 | `/Data/RootChunk/sceneGraph/Data/graph/233/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 24 | 41 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsSocket` | 461 | 41 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scneventsUnequipItemFromPerformerByItem` | 3 | 5920 / 5726 | `/Data/RootChunk/sceneGraph/Data/graph/434/Data/events/19` |
| `scneventsVFXEvent` | 53 | 41 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 60
- speech: 20
- gaze: 14
- speech, skeletal_animation, socket_signal: 6
- speech, socket_signal: 6
- speech, skeletal_animation, gaze, socket_signal: 6
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, idle_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 5
- socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, gaze: 3
- skeletal_animation, idle_animation, socket_signal: 3
- speech, idle_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- idle_animation: 3
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze, props_equipment, vfx, socket_signal: 2
- skeletal_animation, camera, socket_signal: 2
- speech, idle_animation, gaze: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, idle_animation: 1
- speech, skeletal_animation, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, audio, vfx: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- props_equipment: 1
- skeletal_animation, idle_animation, vfx: 1
- camera, vfx: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `e3d1b683a07fd8cf11635aeab1403b335e96e4a70f2daf76e1461105a96c3b04`. Binary SHA-256: `061806e4195600bc2724330b3626033870fa48fdcc173eaab9345950757fad73`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_04_squot.scene" --events
```

## `ep1\quest\main_quests\q302\scenes\q302_05_bar.scene`

633 graph nodes, 857 edges; 115 event-bearing sections, 1006 events; 180 screenplay lines, 38 screenplay options, 16 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Reed (actor 1, findInContext); Voice (actor 2, findInContext); Scavenger_01 (actor 3, community); Scavenger_02 (actor 4, community); Ronald (actor 5, community); Protester_01 (actor 6, spawnSet); Protester_02 (actor 7, community); Guard_01 (actor 8, community); Guard_02 (actor 9, community); Protester_03 (actor 10, community); Protester_Vset_USA (actor 11, community); Protester_Vset_terrorists (actor 12, community); Protester_Vset_powerful (actor 13, community); Protester_Vset_damn_u_all (actor 14, community); Player (actor 15, findInContext).

Entries: `q302_05_bar_in` → 1; `phonecall` → 1219; `persistent_content_phone` → 2339; `protester_in` → 1415; `q302_05_ronald_in` → 920; `ronald_dialogue_prev` → 3754; `easter_eggs_prev` → 2707.

Exits: `q302_05_bar_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 13 | 18 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnChangeIdleAnimEvent` | 138 | 18 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnDialogLineEvent` | 136 | 13 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 8 | 405 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/5` |
| `scnIKEvent` | 16 | 405 / 274 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/1` |
| `scnLookAtEvent` | 102 | 18 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 1 | 2647 / 2955 | `/Data/RootChunk/sceneGraph/Data/graph/328/Data/events/2` |
| `scnPlaySkAnimEvent` | 398 | 18 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 8 | 405 / 278 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/4` |
| `scneventsAttachPropToNode` | 3 | 235 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 1261 / 796 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/6` |
| `scneventsCameraParamsEvent` | 18 | 18 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 8 | 405 / 276 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/3` |
| `scneventsSocket` | 152 | 13 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 4 | 876 / 618 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 20
- skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 7
- speech, skeletal_animation, idle_animation, socket_signal: 7
- skeletal_animation, idle_animation, gaze, socket_signal: 6
- gaze: 6
- skeletal_animation, idle_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze: 4
- skeletal_animation, idle_animation: 4
- camera: 4
- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze: 2
- skeletal_animation, idle_animation, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, camera, socket_signal: 2
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, socket_signal: 1
- speech, skeletal_animation, audio: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, audio, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, gaze: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `74513a4330c74de6d03e0044fb3de54b10cd89c0f680cb70cf1f18b61b8a532b`. Binary SHA-256: `27df897f6351b9ddd75874eb660ac02728d9aea808954fad17571b386a3fde26`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_05_bar.scene" --events
```

## `ep1\quest\main_quests\q302\scenes\q302_06_basketball.scene`

584 graph nodes, 719 edges; 119 event-bearing sections, 1030 events; 243 screenplay lines, 39 screenplay options, 17 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Reed (actor 1, spawnSet); Songbird (actor 2, spawnSet); bb_player1 (actor 3, community); bb_player2 (actor 4, community); bb_player3 (actor 5, community); bb_player4 (actor 6, community); bb_player5 (actor 7, community); bb_player6 (actor 8, community); bb_crowd_male_01 (actor 9, community); bb_crowd_male_02 (actor 10, community); bb_crowd_male_03 (actor 11, community); bb_crowd_male_04 (actor 12, community); bb_crowd_male_05 (actor 13, community); bb_crowd_male_06 (actor 14, community); bb_crowd_male_07 (actor 15, community); bb_crowd_male_08 (actor 16, community); bb_crowd_male_09 (actor 17, community); bb_group_1_male1 (actor 18, community); bb_group_1_female1 (actor 19, community); bb_group_1_male2 (actor 20, community); bb_group_2_female2 (actor 21, community); bb_crowd_male_10 (actor 22, community); bb_crowd_male_11 (actor 23, community); bb_crowd_female_12 (actor 24, community); bb_group_2_male2 (actor 25, community); bb_crowd_female_01 (actor 26, community); bb_crowd_female_02 (actor 27, community); bb_player7 (actor 28, community); bb_player8 (actor 29, community); bb_player9 (actor 30, community); bb_crowd_female_03 (actor 31, community); bb_crowd_female_04 (actor 32, community); reed_car (actor 33, spawnSet); Player (actor 34, findInContext).

Entries: `Start 12` → 6360; `q302_06_basketball_in` → 574; `dunk it babe` → 3381; `universal` → 6969; `Start 15` → 7472; `interrogation_continued_prev` → 2113; `Start 13` → 6681.

Exits: `q302_06_basketball_out` → 572; `prefetch_nt_out` → 5288; `End 5` → 5290.

End nodes: 572: `<omitted>`; 5288: `NonTerminating`; 5290: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 48 | 1964 / 735 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/2` |
| `scnDialogLineEvent` | 200 | 47 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 7 | 51 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnIKEvent` | 14 | 51 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnLookAtEvent` | 214 | 47 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPlaySkAnimEvent` | 247 | 47 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnPoseCorrectionEvent` | 6 | 47 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scnUnmountEvent` | 7 | 51 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/12` |
| `scneventsAttachPropToPerformer` | 12 | 2985 / 1892 | `/Data/RootChunk/sceneGraph/Data/graph/157/Data/events/4` |
| `scneventsAttachPropToWorld` | 5 | 51 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsCameraParamsEvent` | 5 | 47 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scneventsEquipItemToPerformer` | 21 | 1964 / 740 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 7 | 51 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsSocket` | 232 | 47 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 3 | 2188 / 1573 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/7` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 2181 / 1538 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/11` |
| `scneventsVFXEvent` | 1 | 6561 / 3306 | `/Data/RootChunk/sceneGraph/Data/graph/410/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21
- speech, skeletal_animation, socket_signal: 18
- speech, skeletal_animation, gaze, socket_signal: 11
- skeletal_animation, props_equipment, socket_signal: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 5
- skeletal_animation, gaze: 5
- skeletal_animation, socket_signal: 4
- speech, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, props_equipment, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze, camera, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- gaze: 2
- camera: 2
- speech, skeletal_animation, gaze, camera, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `a78c4631e9a0f5e767ce27f8fc2a13b5193ae1d41c351f8cc99b71495f689a8a`. Binary SHA-256: `9d92dae98548f2bc0aed6b6030521f2ffbea54c39b5eeddb1937016c128cec58`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_06_basketball.scene" --events
```

## `ep1\quest\main_quests\q302\scenes\q302_06a_ride.scene`

564 graph nodes, 708 edges; 92 event-bearing sections, 716 events; 163 screenplay lines, 33 screenplay options, 16 choice nodes.

Actors: Reed (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Witness (actor 2, spawnDespawn); reed_car (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `next phase of talk` → 3338; `HANDCUFFS (1A)` → 2336; `knockout next phase` → 3428; `Start 8` → 5539; `aft_ambush_dbg` → 5567; `drive` → 3510; `q302_06a_ride_in` → 951; `ambush` → 3566; `q302_06a_1A` → 2082.

Exits: `q302_06a_ride_out` → 53; `barghest_road_ambush_out` → 3218; `spawn_oath` → 3644.

End nodes: 53: `<omitted>`; 3218: `NonTerminating`; 3644: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 17 | 147 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnChangeIdleAnimEvent` | 11 | 738 / 226 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |
| `scnDialogLineEvent` | 128 | 147 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnGameplayTransitionEvent` | 8 | 147 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/16` |
| `scnIKEvent` | 26 | 147 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 160 | 147 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 149 | 147 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 8 | 147 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scneventsAttachPropToPerformer` | 5 | 2741 / 939 | `/Data/RootChunk/sceneGraph/Data/graph/113/Data/events/1` |
| `scneventsAttachPropToWorld` | 3 | 2813 / 1154 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/5` |
| `scneventsCameraParamsEvent` | 11 | 150 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsEquipItemToPerformer` | 2 | 2632 / 761 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 38 | 147 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsSocket` | 135 | 147 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsUnequipItemFromPerformer` | 1 | 2632 / 780 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/14` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 4825 / 2869 | `/Data/RootChunk/sceneGraph/Data/graph/376/Data/events/3` |
| `scneventsVFXDurationEvent` | 7 | 2791 / 1026 | `/Data/RootChunk/sceneGraph/Data/graph/118/Data/events/2` |
| `scneventsVFXEvent` | 5 | 2741 / 953 | `/Data/RootChunk/sceneGraph/Data/graph/113/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 14
- speech, skeletal_animation, gaze, socket_signal, animation_state: 8
- speech: 7
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, gaze, audio, socket_signal: 4
- gaze, socket_signal, animation_state: 4
- speech, skeletal_animation, socket_signal: 3
- speech, socket_signal: 3
- speech, skeletal_animation, gaze, ik, props_equipment, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, audio, vfx: 3
- camera: 3
- speech, gaze, socket_signal: 2
- skeletal_animation, camera, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, vfx: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- socket_signal, animation_state: 2
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze: 2
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, idle_animation: 1
- speech, skeletal_animation: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, vfx: 1
- skeletal_animation, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, ik, camera, socket_signal, animation_state: 1
- props_equipment, socket_signal: 1
- camera, vfx: 1
- vfx: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `3cd2622f6c676e9cc6066b432bc01b7a88ea9e1aadececf5e7d2a9dcc17dd72f`. Binary SHA-256: `b91f94b635f1e5119a4b6ece7df476b1fcb6e326740fc7237371fda589f33736`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_06a_ride.scene" --events
```

## `ep1\quest\main_quests\q302\scenes\q302_07_oath.scene`

919 graph nodes, 1130 edges; 138 event-bearing sections, 1643 events; 325 screenplay lines, 34 screenplay options, 17 choice nodes.

Actors: Myers (actor 0, spawnSet); Reed (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); Jacob (actor 3, community); Taylor (actor 4, community); q302_hobo_m_1 (actor 5, community); q302_hobo_m_2 (actor 6, community); q302_hobo_f_1 (actor 7, community); q302_hobo_f_2 (actor 8, community); q302_hobo_m1_talking (actor 9, community); q302_hobo_f1_talking (actor 10, community); q302_hobo_m2_talking (actor 11, community); q302_hobo_m_3 (actor 12, community); q302_hobo_m_4 (actor 13, community); q302_hobo_f_3 (actor 14, community); q302_hobo_f_4 (actor 15, community); q302_hobo_m_5 (actor 16, community); q302_hobo_f_5 (actor 17, community); Militia_sergeant (actor 18, community); Militia_soldier (actor 19, community); Player (actor 20, findInContext).

Entries: `q302_07_oath_peaceful_in` → 1; `peaceful_return` → 9833; `Reed question hobo` → 8238; `elev combat` → 8247; `elev peace` → 8294; `q302_07_oath_hostile_in` → 9120; `Reed ground floor` → 8303; `hand shake` → 8369; `hostile_return` → 10025; `Start 24` → 8419; `q302_07_oath_1_a` → 1999; `q302_07_oath_1_b` → 2005; `________TEST` → 6092; `q302_07_oath_1_c` → 2007; `q302_07_oath_1_d` → 2010; `q302_07_oath_1_e` → 2012; `q302_07_oath_1_g` → 2912; `oath_main_part_misfits_live` → 7874; `oval_office_talk_preview` → 7919; `elev out reed` → 12823; `Start 29` → 12090; `oath_main_part_myers_alone` → 8027; `entering_squot_prev` → 8042; `q302_oath_1_H` → 4782; `q302_07_oath_1_f` → 2347.

Exits: `q302_07_oath_out` → 2; `peaceful_run_off` → 9834; `Refused_Job` → 137; `hostile_run_off` → 10027; `clear_scene` → 9591.

End nodes: 2: `NonTerminating`; 137: `NonTerminating`; 9591: `<omitted>`; 9834: `<omitted>`; 10027: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 6932 / 2516 | `/Data/RootChunk/sceneGraph/Data/graph/196/Data/events/0` |
| `scnChangeIdleAnimEvent` | 72 | 755 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnDialogLineEvent` | 252 | 578 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnGameplayTransitionEvent` | 13 | 2324 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/12` |
| `scnIKEvent` | 26 | 2324 / 281 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/3` |
| `scnLookAtEvent` | 537 | 578 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 416 | 755 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scnPoseCorrectionEvent` | 6 | 2675 / 453 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/14` |
| `scnUnmountEvent` | 13 | 2324 / 290 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/11` |
| `scneventsAttachPropToPerformer` | 3 | 3669 / 931 | `/Data/RootChunk/sceneGraph/Data/graph/74/Data/events/13` |
| `scneventsAttachPropToWorld` | 2 | 3669 / 933 | `/Data/RootChunk/sceneGraph/Data/graph/74/Data/events/15` |
| `scneventsEquipItemToPerformer` | 20 | 2478 / 311 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 13 | 2324 / 286 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/8` |
| `scneventsSocket` | 264 | 755 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/10` |
| `scneventsUnequipItemFromPerformer` | 3 | 3581 / 900 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/23` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 8325 / 3416 | `/Data/RootChunk/sceneGraph/Data/graph/305/Data/events/25` |
| `scneventsVFXEvent` | 1 | 12018 / 6041 | `/Data/RootChunk/sceneGraph/Data/graph/704/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 26
- speech, skeletal_animation, gaze, socket_signal: 22
- speech, skeletal_animation, gaze: 10
- skeletal_animation, gaze, socket_signal: 8
- speech, idle_animation, gaze, socket_signal: 6
- speech: 6
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 5
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 5
- skeletal_animation, socket_signal: 5
- speech, gaze: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- socket_signal: 2
- gaze, socket_signal: 1
- idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, idle_animation, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, audio: 1
- speech, gaze, socket_signal: 1
- gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1
- skeletal_animation: 1
- props_equipment: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `26488429706739b480892a82d125a46e70dca6a14d354ce8612f279f3dcb8972`. Binary SHA-256: `811e1eadc7dc7906b1771b88a42f267a0472cbee214885cb8234809bb536c9f7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_07_oath.scene" --events
```

## `ep1\quest\main_quests\q302\scenes\q302_08_call.scene`

31 graph nodes, 34 edges; 11 event-bearing sections, 50 events; 22 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: Reed (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `q302_08_call_in` → 6.

Exits: `q302_08_call_out` → 8.

End nodes: 8: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 254 / 222 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/0` |
| `scnDialogLineEvent` | 21 | 71 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnPlaySkAnimEvent` | 22 | 71 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scneventsSocket` | 6 | 71 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation: 3
- speech: 2
- idle_animation: 1

Raw SHA-256: `a84e21e3f2bec73c95aa995488d10288b1205fcd3fd4f8315d9180c636a26452`. Binary SHA-256: `ae4d95d75d305bd7f2854ab57f1a1cf2bc813ac52419315b55f86af5602f1ecf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_08_call.scene" --events
```

## `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene`

294 graph nodes, 347 edges; 42 event-bearing sections, 223 events; 45 screenplay lines, 30 screenplay options, 21 choice nodes.

Actors: johnny_mirror (actor 0, spawnDespawn); v_male_tpp (actor 1, spawnDespawn); v_female_tpp (actor 2, spawnDespawn); Johnny (actor 3, spawnDespawn); idris_shot_myers (actor 4, spawnDespawn); idris_shot_reed (actor 5, spawnDespawn); idris_shot_kurt (actor 6, spawnDespawn); idris_shot_songbird (actor 7, spawnDespawn); idris_shot_johnny (actor 8, spawnDespawn); idris_shot_additional_npc (actor 9, spawnDespawn); Player (actor 10, findInContext).

Entries: `Start 0` → 1; `idris_shot` → 1463.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 15 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnChangeIdleAnimEvent` | 3 | 649 / 994 | `/Data/RootChunk/sceneGraph/Data/graph/149/Data/events/1` |
| `scnDialogLineEvent` | 5 | 696 / 1119 | `/Data/RootChunk/sceneGraph/Data/graph/164/Data/events/0` |
| `scnGameplayTransitionEvent` | 11 | 68 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/6` |
| `scnIKEvent` | 22 | 68 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scnLookAtEvent` | 11 | 616 / 978 | `/Data/RootChunk/sceneGraph/Data/graph/147/Data/events/2` |
| `scnPlayRidAnimEvent` | 1 | 1420 / 1754 | `/Data/RootChunk/sceneGraph/Data/graph/268/Data/events/1` |
| `scnPlaySkAnimEvent` | 58 | 15 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 11 | 68 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/10` |
| `scneventsAttachPropToNode` | 3 | 429 / 660 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/4` |
| `scneventsAttachPropToPerformer` | 3 | 429 / 657 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/1` |
| `scneventsCameraParamsEvent` | 2 | 60 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |
| `scneventsPlayRidCameraAnimEvent` | 1 | 1420 / 1784 | `/Data/RootChunk/sceneGraph/Data/graph/268/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 11 | 68 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/7` |
| `scneventsSocket` | 55 | 15 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsVFXEvent` | 16 | 15 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 8
- skeletal_animation: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech: 4
- skeletal_animation, props_equipment, vfx, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, audio, vfx, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, audio, vfx: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, rid_actor, camera, rid_camera, socket_signal: 1

Raw SHA-256: `27e6e4b6a030cdff28e562bceb0fa7961671ea5e5e272b341366f47e4d4bf8fc`. Binary SHA-256: `5c5ec1d51b2c9df31dcb626e0d715d4a4ce1a057b103dab24c04e7903e303090`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene" --events
```

