# Spider and the Fly: scene presentation

Journal identity: `ep1/quests/main_quest/q301_q302_rescue_myers`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q301_q302_rescue_myers.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\main_quests\q301\scenes\q301_05b_crashsite_gameplay.scene`

88 graph nodes, 111 edges; 11 event-bearing sections, 51 events; 42 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: songbird_holo (actor 0, findInContext); bottom_enemy_005 (actor 1, community); bottom_enemy_006 (actor 2, community); bottom_enemy_001 (actor 3, community); bottom_enemy_002 (actor 4, community); bottom_enemy_016 (actor 5, community); bottom_enemy_014 (actor 6, community); bottom_enemy_008 (actor 7, community); bottom_enemy_009 (actor 8, community); AV_003 (actor 9, community); AV_004 (actor 10, community); Player (actor 11, findInContext).

Entries: `sb_guidance_01` → 1; `blockade` → 6; `sb_guidance_02` → 9; `nonlin_reinforcements_chat` → 295; `sb_hack_mech` → 304; `sb_hack_av` → 305; `Kurtz_man_chat` → 337; `AVs_start` → 344.

Exits: `sb_guidance_01_done` → 2; `blockade_done` → 8; `sb_guidance_02_done` → 11; `nonlin_reinforcements_chat_done` → 296; `sb_hack_av_done` → 308; `sb_hack_mech_done` → 311; `Kurtz_man_chat_done` → 339; `AVs_start_done` → 345.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 11: `<omitted>`; 296: `<omitted>`; 308: `<omitted>`; 311: `<omitted>`; 339: `<omitted>`; 345: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 380 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |
| `scnChangeIdleAnimEvent` | 2 | 425 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/2` |
| `scnDialogLineEvent` | 39 | 27 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 380 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/1` |
| `scneventsVFXDurationEvent` | 2 | 380 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- skeletal_animation, audio, vfx: 2
- skeletal_animation, idle_animation: 1

Raw SHA-256: `d383504b084bb605921cf5a6651f13ff7d5c405acb1883331c031e2c6535e260`. Binary SHA-256: `f30b5e7cec08266e80b022c79c16aae4750588311e7151887de76f5ca67a9299`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_05b_crashsite_gameplay.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_06a_shuttle_arrival.scene`

176 graph nodes, 220 edges; 35 event-bearing sections, 310 events; 69 screenplay lines, 21 screenplay options, 5 choice nodes.

Actors: myers (actor 0, spawnSet); fss_01 (actor 1, community); songbird (actor 2, spawnDespawn); kurt_m_01 (actor 3, community); kurt_m_02 (actor 4, community); kurt_m_03 (actor 5, community); songbird_holo (actor 6, findInContext); kurt_m_04_trailer (actor 7, community); kurt_m_05_trailer (actor 8, community); Player (actor 9, findInContext).

Entries: `fx_explosion_preview` → 399; `Start 0` → 1; `Start 3` → 439; `Start1` → 1500; `Start 4` → 530; `Start 5` → 1165; `sb_arrival` → 369.

Exits: `End 0` → 2; `clear` → 78; `End1` → 1502; `sb_arrival_done` → 370.

End nodes: 2: `NonTerminating`; 78: `<omitted>`; 370: `<omitted>`; 1502: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 26 | 451 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/4` |
| `scnChangeIdleAnimEvent` | 14 | 514 / 217 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/1` |
| `scnDialogLineEvent` | 38 | 185 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 811 / 482 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/21` |
| `scnIKEvent` | 14 | 811 / 459 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/2` |
| `scnLookAtAdvancedEvent` | 6 | 1196 / 895 | `/Data/RootChunk/sceneGraph/Data/graph/105/Data/events/3` |
| `scnLookAtEvent` | 6 | 568 / 268 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/12` |
| `scnPlaySkAnimEvent` | 72 | 30 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 6 | 811 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/28` |
| `scneventsAttachPropToNode` | 1 | 811 / 481 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/20` |
| `scneventsAttachPropToPerformer` | 1 | 811 / 470 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/9` |
| `scneventsCameraEvent` | 1 | 1196 / 891 | `/Data/RootChunk/sceneGraph/Data/graph/105/Data/events/0` |
| `scneventsCameraParamsEvent` | 17 | 568 / 266 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/10` |
| `scneventsEquipItemToPerformer` | 9 | 451 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 6 | 811 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/23` |
| `scneventsSocket` | 66 | 30 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scneventsVFXDurationEvent` | 5 | 451 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/6` |
| `scneventsVFXEvent` | 16 | 451 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- skeletal_animation, audio, socket_signal: 4
- skeletal_animation: 4
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- speech, audio, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, audio: 1
- speech, skeletal_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, camera, socket_signal: 1

Raw SHA-256: `35f030c088a3d930965700d78156de2c5107def1358e77b3203de4f3b265d46a`. Binary SHA-256: `cef238230e1689c692eb759ddada64b397093fb2c921b4b059702ce02a579ef1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_06a_shuttle_arrival.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_06b_shuttle_combat.scene`

19 graph nodes, 15 edges; 4 event-bearing sections, 10 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: myers (actor 0, spawnSet); Mech (actor 1, community); Player (actor 2, findInContext).

Entries: `myers_orders` → 9; `myers_situation` → 70; `Mech Spawn Debug` → 52; `myers_cover` → 75.

Exits: `myers_cover_done` → 76; `myers_orders_done` → 10; `myers_situation_done` → 71; `Mech Spawn Debug End` → 54.

End nodes: 10: `<omitted>`; 54: `<omitted>`; 71: `<omitted>`; 76: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 35 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnDialogLineEvent` | 5 | 72 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 35 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsSocket` | 1 | 35 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scneventsVFXEvent` | 1 | 35 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- skeletal_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `4fbebbca4ecf1c56add31c848f2bc8ccceba1c02c0883f4bde8dff910ee09c41`. Binary SHA-256: `94c98707a68d2289190996cc9d9a72701aae29b08bf4aa5e0615cad57416160b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_06b_shuttle_combat.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_06c_shuttle_escape.scene`

61 graph nodes, 67 edges; 10 event-bearing sections, 30 events; 21 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: myers (actor 0, spawnSet); songbird (actor 1, findInContext); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `End1` → 1078; `End 1` → 141.

End nodes: 141: `NonTerminating`; 1078: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 1115 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/2` |
| `scnDialogLineEvent` | 14 | 219 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnLookAtEvent` | 1 | 1051 / 282 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/3` |
| `scnPlaySkAnimEvent` | 5 | 95 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 1051 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/7` |
| `scneventsAttachPropToPerformer` | 2 | 1051 / 281 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scneventsSocket` | 5 | 95 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, socket_signal: 2
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, animation_state: 1

Raw SHA-256: `04a7e5fad1328bcd43f8f459aae7300d46337f482cf220532e3dd301a775c19b`. Binary SHA-256: `29b7ed0bc428339bf0e29d0e3f71f8c173bfa2bf3b71593ea06105243bbce5b4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_06c_shuttle_escape.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_07_shuttle_myers.scene`

225 graph nodes, 292 edges; 44 event-bearing sections, 309 events; 156 screenplay lines, 25 screenplay options, 5 choice nodes.

Actors: songbird (actor 0, findInContext); myers (actor 1, spawnSet); johnny (actor 2, spawnDespawn); communication_device (actor 3, spawnDespawn); guard_m_search_01 (actor 4, community); guard_m_search_02 (actor 5, community); guard_m_search_03 (actor 6, community); guard_m_search_04 (actor 7, community); drone (actor 8, community); guard_car (actor 9, community); drone_carrier (actor 10, community); Player (actor 11, findInContext).

Entries: `Start 0` → 1; `tracker` → 2824; `break_bottle` → 2972.

Exits: `Drone_fight` → 4990; `End 1` → 440; `q302_elevator_line` → 4474; `q302_dialogue_starts` → 3969; `q301_spot_check_for_reaction` → 3977.

End nodes: 440: `NonTerminating`; 3969: `NonTerminating`; 3977: `NonTerminating`; 4474: `NonTerminating`; 4990: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 21 | 2719 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/2` |
| `scnChangeIdleAnimEvent` | 18 | 1913 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnDialogLineEvent` | 59 | 1319 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 2810 / 358 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/19` |
| `scnIKEvent` | 6 | 2810 / 333 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/1` |
| `scnLookAtEvent` | 62 | 1913 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnPlaySkAnimEvent` | 29 | 1913 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnUnmountEvent` | 3 | 2810 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/23` |
| `scneventsAttachPropToNode` | 7 | 2799 / 317 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/7` |
| `scneventsAttachPropToPerformer` | 9 | 2719 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 2743 / 255 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/18` |
| `scneventsCameraParamsEvent` | 9 | 2719 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/1` |
| `scneventsEquipItemToPerformer` | 6 | 2810 / 335 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 3 | 2810 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/20` |
| `scneventsSocket` | 64 | 1319 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 2897 / 389 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/5` |
| `scneventsVFXDurationEvent` | 1 | 2810 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/14` |
| `scneventsVFXEvent` | 7 | 2799 / 316 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, socket_signal: 5
- skeletal_animation, idle_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, gaze: 2
- speech, gaze, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 2
- skeletal_animation, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, idle_animation: 1
- props_equipment: 1
- skeletal_animation, props_equipment: 1
- gaze: 1
- skeletal_animation: 1

Raw SHA-256: `b87a57ee959081202c5f8a55ce1a70ecb9f906966b9e74c169484bb9ed0eed45`. Binary SHA-256: `21eaf43dd04f2cd256e90a8d58f7a2efeb125dd006e63388bbee68481baac052`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_07_shuttle_myers.scene" --events
```

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

