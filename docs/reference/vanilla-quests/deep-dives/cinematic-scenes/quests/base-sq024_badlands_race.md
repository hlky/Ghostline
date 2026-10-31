# The Beast in Me: Badlands: scene presentation

Journal identity: `quests/side_quest/sq024_badlands_race`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq024_badlands_race.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq024\scenes\sq024_00_claire_hook.scene`

29 graph nodes, 29 edges; 4 event-bearing sections, 20 events; 13 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: claire (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 1` → 249; `sq024_00_hook_in` → 49.

Exits: `call_rejected` → 340; `sq024_00_hook_out` → 50.

End nodes: 50: `<omitted>`; 340: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 69 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnDialogLineEvent` | 13 | 66 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnLookAtEvent` | 2 | 66 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 66 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsSocket` | 1 | 66 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 1
- speech: 1
- speech, skeletal_animation, idle_animation: 1
- idle_animation, gaze: 1

Raw SHA-256: `d15c1cd5b5808e19d8cbbaff92de3719caa189729e2f2711d2098cea26028800`. Binary SHA-256: `be3da8f6631f25506d7d6bf5ddb4cb4a1f20e634a0224ef0c2531c5ffd25a7eb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_00_claire_hook.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_01a_claire_garage.scene`

93 graph nodes, 107 edges; 19 event-bearing sections, 184 events; 57 screenplay lines, 15 screenplay options, 7 choice nodes.

Actors: claire (actor 0, spawnSet); thorton_galena (actor 1, community); claire_truck (actor 2, community); Player (actor 3, findInContext).

Entries: `sq024_01a_garage_in` → 4; `sq024_01_driving_to_pacifica_fluff_in` → 25.

Exits: `kill_afterlife_scene` → 489; `sq024_01_alone_out` → 24; `sq024_01_end_quest_out` → 208; `sq024_01_driving_to_pacifica_fluff_out` → 26; `End 2` → 230; `End1` → 242.

End nodes: 24: `NonTerminating`; 26: `<omitted>`; 208: `NonTerminating`; 230: `<omitted>`; 242: `<omitted>`; 489: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 25 | 7 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 53 | 7 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 7 | 7 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnPlaySkAnimEvent` | 55 | 7 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 4 | 7 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsSocket` | 40 | 7 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- speech: 2
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation: 1
- socket_signal: 1

Raw SHA-256: `fc29cc8f0f2b5a7b4822d92f069cb6fca37fc8f7864f5e0024d869e297107de3`. Binary SHA-256: `81ed037b16b85e4c51adaf7e056241f1a55c0ee860d03b1cbff5b481bf30769b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_01a_claire_garage.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_01b_claire_afterlife.scene`

58 graph nodes, 75 edges; 9 event-bearing sections, 77 events; 23 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: claire (actor 0, spawnSet); client (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `sq024_01b_afterlife_in` → 1.

Exits: `cleanup` → 323; `sq024_01b_to_garage_out` → 109; `sq024_01b_out` → 110.

End nodes: 109: `NonTerminating`; 110: `NonTerminating`; 323: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 101 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnDialogLineEvent` | 23 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 7 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 20 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 167 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |
| `scneventsEquipItemToPerformer` | 2 | 119 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/13` |
| `scneventsSocket` | 20 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `58fbecae9c3f934db541f1db6536a3223201455e1ba19e59190a6bcf3b6292ac`. Binary SHA-256: `06019ddaaf0103ea3dd40507d2a81cd6e412e31cd838b87d02125334b6fed296`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_01b_claire_afterlife.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_02_santo_domingo_race.scene`

146 graph nodes, 152 edges; 27 event-bearing sections, 139 events; 65 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: claire (actor 0, spawnSet); claire_phone (actor 1, spawnSet); racer_1 (actor 2, community); racer_2 (actor 3, community); announcer (actor 4, findInContext); racer_6th_1 (actor 5, community); racer_6th_2 (actor 6, community); crowd_civ_1 (actor 7, community); crowd_civ_2 (actor 8, community); crowd_scv (actor 9, community); crowd_civ_3 (actor 10, community); race_car_01 (actor 11, community); race_car_02 (actor 12, community); race_car_03 (actor 13, community); race_car_04 (actor 14, community); race_car_05 (actor 15, community); race_car_06 (actor 16, community); race_car_07 (actor 17, community); maelstrom_car (actor 18, community); v (actor 19, findInContext).

Entries: `sq024_02_sd_maelstrom_in` → 265; `start_from_race_in` → 802; `sq024_02_racers_talk_6th_start` → 828; `sq024_02_crowd_talk_start` → 831; `sq024_02_crowd_civ_start` → 834; `sq024_02_pacifica_pre_race_separate_in` → 50; `sq024_02_crowd_scv_start` → 837; `sq024_02_call_in` → 347; `sq024_03_random_banter_in` → 357; `sq024_02_announcer_01_in` → 261.

Exits: `sq024_02_announcer_01_out` → 262; `sq024_02_pacifica_pre_race_out` → 2; `sq024_02_sd_maelstrom_out` → 266; `sq024_02_crowd_talk_end` → 833; `sq024_02_crowd_civ_end` → 836; `sq024_02_crowd_scv_end` → 839; `sq024_02_racer_crowd_6th_end` → 842; `sq024_02_announcer_countdown_out` → 453; `sq024_02_spawn_out` → 610; `sq024_02_call_out` → 348; `End 8` → 896; `End 9` → 1163.

End nodes: 2: `<omitted>`; 262: `NonTerminating`; 266: `<omitted>`; 348: `NonTerminating`; 453: `NonTerminating`; 610: `NonTerminating`; 833: `<omitted>`; 836: `<omitted>`; 839: `<omitted>`; 842: `<omitted>`; 896: `<omitted>`; 1163: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 450 / 186 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/3` |
| `scnChangeIdleAnimEvent` | 6 | 322 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnDialogLineEvent` | 61 | 260 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 592 / 237 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/6` |
| `scnIKEvent` | 6 | 592 / 231 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/1` |
| `scnLookAtEvent` | 19 | 260 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 417 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/2` |
| `scnUnmountEvent` | 3 | 592 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 3 | 592 / 234 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/4` |
| `scneventsSocket` | 25 | 322 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, idle_animation, gaze, socket_signal: 4
- speech, gaze: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation: 2
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, audio, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `39f07292ee07cb205b23983f3bff0f2c76db7a493ca9bff1d24b09022fc8b59c`. Binary SHA-256: `ab822d9b16a5a6c5ecd91359eb0541ba5877413e3fcebcc016a837eb97117638`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_02_santo_domingo_race.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_02b_santo_domingo_race_end.scene`

177 graph nodes, 242 edges; 44 event-bearing sections, 285 events; 108 screenplay lines, 27 screenplay options, 14 choice nodes.

Actors: claire (actor 0, spawnSet); racer_1 (actor 1, community); racer_2 (actor 2, community); announcer (actor 3, findInContext); crowd_end_6th (actor 4, community); Player (actor 5, findInContext).

Entries: `sq024_02b_final_end_scene_in` → 1; `badlands_failed` → 986; `sq024_big_race_reuse_in` → 504; `sq024_02b_sit_reminder_start` → 511; `sq024_02b_race_finish_in` → 28; `sq024_02b_custom_reminder_start` → 516; `sq024_02b_end_6th_start` → 529; `sq024_02b_talking_racers_in` → 55; `line_steal_reggie_dd_in` → 748; `Start 5` → 600.

Exits: `claire_leave_out` → 176; `sq024_big_race_reuse_out` → 505; `sq024_02b_race_finish_out` → 29; `sq024_02b_failed_quest_out` → 194; `sq024_02b_end_6th_end` → 531; `sq024_02b_go_to_view_out` → 56; `badlands_failed_out` → 1032; `End 7` → 399; `despawn_stuff_out` → 289; `sq024_02b_end_out` → 134.

End nodes: 29: `<omitted>`; 56: `<omitted>`; 134: `NonTerminating`; 176: `NonTerminating`; 194: `<omitted>`; 289: `NonTerminating`; 399: `<omitted>`; 505: `<omitted>`; 531: `<omitted>`; 1032: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 17 | 156 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/5` |
| `scnDialogLineEvent` | 97 | 31 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 158 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/23` |
| `scnIKEvent` | 4 | 158 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/16` |
| `scnLookAtEvent` | 56 | 155 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scnPlaySkAnimEvent` | 58 | 155 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnPoseCorrectionEvent` | 10 | 158 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/6` |
| `scnUnmountEvent` | 2 | 158 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/22` |
| `scneventsCameraParamsEvent` | 4 | 198 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 158 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/21` |
| `scneventsSocket` | 33 | 156 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 5
- speech, skeletal_animation, gaze: 3
- speech, gaze: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, gaze, socket_signal: 2
- camera: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, idle_animation: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1

Raw SHA-256: `be67236a1e11624f2aa6de2a68e93325064621b62d3fc0dcc0bb83573c6cafbd`. Binary SHA-256: `0945a3264658654e17edeff16a119aec32eeda2f225ec4c95e820d723fce82a0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_02b_santo_domingo_race_end.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_03_badlands_race.scene`

166 graph nodes, 193 edges; 32 event-bearing sections, 140 events; 61 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: claire (actor 0, spawnSet); announcer (actor 1, findInContext); claire_phone (actor 2, spawnSet); Luigi (actor 3, community); racer_2 (actor 4, community); Margo (actor 5, community); racer_wraith_1 (actor 6, community); racer_wraith_2 (actor 7, community); crowd_wrt (actor 8, community); crowd_civ (actor 9, community); race_vehicle_01 (actor 10, community); race_vehicle_02 (actor 11, community); race_vehicle_03 (actor 12, community); race_vehicle_04 (actor 13, community); race_vehicle_05 (actor 14, community); v (actor 15, findInContext).

Entries: `sq024_03_call_in` → 1; `q115_reuse_in` → 935; `sq024_03_racers_talk_ald_start` → 940; `sq024_03_badlands_pre_race_in` → 16; `sq024_03_racers_talk_wrt_start` → 943; `sq024_03_crowd_civ_start` → 946; `sq024_03_random_banter_in` → 178; `sq024_03_crowd_wrt_start` → 949; `sq024_03_announcer_01_in` → 78; `sq024_03_sandstrom_in` → 83; `Start 6` → 753.

Exits: `sq024_03_call_out` → 2; `sq024_03_announcer_countdown_out` → 466; `q115_reuse_out` → 936; `sq024_03_badlands_pre_race_out` → 17; `sq024_03_racers_talk_ald_end` → 942; `sq024_03_racers_talk_wrt_end` → 945; `sq024_03_crowd_civ_end` → 948; `sq024_03_crowd_wrt_end` → 951; `sq024_03_badlands_spawn_stuff_out` → 652; `End 10` → 977; `sq024_03_announcer_01_out` → 79; `sq024_03_sandstrom_out` → 84.

End nodes: 2: `<omitted>`; 17: `<omitted>`; 79: `NonTerminating`; 84: `<omitted>`; 466: `NonTerminating`; 652: `NonTerminating`; 936: `<omitted>`; 942: `<omitted>`; 945: `<omitted>`; 948: `<omitted>`; 951: `<omitted>`; 977: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 462 / 192 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/2` |
| `scnChangeIdleAnimEvent` | 5 | 129 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnDialogLineEvent` | 58 | 80 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 453 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/14` |
| `scnIKEvent` | 4 | 453 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/7` |
| `scnLookAtEvent` | 12 | 129 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPlaySkAnimEvent` | 25 | 129 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scnPoseCorrectionEvent` | 5 | 446 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/7` |
| `scnUnmountEvent` | 2 | 453 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 2 | 453 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/12` |
| `scneventsSocket` | 21 | 135 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, audio, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- gaze: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- speech, socket_signal: 1

Raw SHA-256: `2a9a0f6878b8e02b44ae3bb59bf0fe5c42577c09abf71941f764fefb1da1e234`. Binary SHA-256: `469d1f748ecbd81584edfba3e699b8a95a366a76000b8dbc8e3a6b172ecb591c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_03_badlands_race.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_03b_badlands_race_end.scene`

60 graph nodes, 62 edges; 17 event-bearing sections, 95 events; 39 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: claire (actor 0, spawnSet); racer_1 (actor 1, community); racer_2 (actor 2, community); announcer (actor 3, findInContext); crowd_end_civ (actor 4, community); crowd_end_ald (actor 5, community); crowd_end_wrt (actor 6, community); beast (actor 7, community); Player (actor 8, findInContext).

Entries: `sq024_03b_race_finish_in` → 10; `sq024_03b_talking_racers_in` → 20; `sq024_03b_end_wrt_start` → 191; `sq024_03b_end_ald_start` → 194; `sq024_03b_end_civ_start` → 197.

Exits: `sq024_03b_ride_to_garage_out` → 9; `sq024_03b_race_finish_out` → 11; `sq024_03b_end_wrt_end` → 193; `sq024_03b_end_ald_end` → 196; `sq024_03b_end_civ_end` → 199; `sq024_03b_end_out` → 41; `badlands_fail` → 367.

End nodes: 9: `<omitted>`; 11: `<omitted>`; 41: `<omitted>`; 193: `<omitted>`; 196: `<omitted>`; 199: `<omitted>`; 367: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 22 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnDialogLineEvent` | 36 | 12 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 32 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scnIKEvent` | 4 | 32 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scnLookAtEvent` | 7 | 25 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scnPlaySkAnimEvent` | 22 | 22 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnPoseCorrectionEvent` | 3 | 32 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scnUnmountEvent` | 2 | 32 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 2 | 32 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/8` |
| `scneventsSocket` | 12 | 22 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze: 1
- socket_signal, animation_state: 1

Raw SHA-256: `79966981eef4bcb4168e38d557304b4665cb349963965451946a5dcf1ca36aaf`. Binary SHA-256: `9aefdae7407d954f5e4de25296ff7b62d3720d24e2dce0967a7c422a91c26d6e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_03b_badlands_race_end.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_04_city_race.scene`

244 graph nodes, 261 edges; 46 event-bearing sections, 294 events; 100 screenplay lines, 13 screenplay options, 6 choice nodes.

Actors: claire (actor 0, spawnSet); announcer (actor 1, findInContext); claire_phone (actor 2, spawnSet); racer_1 (actor 3, community); racer_corp_1 (actor 4, community); sampson (actor 5, community); racer_mox_2 (actor 6, community); racer_corp_2 (actor 7, community); racer_val_1 (actor 8, community); racer_val_2 (actor 9, community); crowd_civ_1 (actor 10, community); crowd_civ_2 (actor 11, community); crowd_civ_3 (actor 12, community); crowd_civ_4 (actor 13, community); claire_car (actor 14, community); race_vehicle_01 (actor 15, community); race_vehicle_02 (actor 16, community); race_vehicle_03 (actor 17, community); race_vehicle_04 (actor 18, community); race_vehicle_05 (actor 19, community); sampsons_car (actor 20, community); v (actor 21, findInContext).

Entries: `sq024_03_city_call_in` → 1; `chicken_in` → 860; `sq024_04_city_pre_race_in` → 16; `sq024_03_random_banter_in` → 244; `Start 13` → 684; `sq024_04_talk_racers_in` → 286; `sq024_04_announcer_01_in` → 94; `sq024_city_together_in` → 306; `sq024_04_racers_talk_corp_start` → 945; `sq024_04_racers_talk_val_start` → 950; `sq024_04_crowd_civ_4_start` → 955; `sq024_04_crowd_civ_3_start` → 960; `sq024_04_crowd_civ_2_start` → 965; `sq024_04_crowd_civ_1_start` → 970; `sharp_turn_in` → 978; `too_far_1_in` → 611; `too_far_2_in` → 612; `too_far_3_in` → 613; `get_out_1_in` → 628; `get_out_2_in` → 629; `let_me_out_1_in` → 630; `let_me_out_2_in` → 631.

Exits: `sq024_03_city_call_out` → 2; `get_out_1_out` → 636; `get_out_2_out` → 637; `let_me_out_1_out` → 638; `let_me_out_2_out` → 639; `End 18` → 1279; `sq024_04_city_pre_race_out` → 17; `sq024_announcer_start_countdown_out` → 445; `sq024_04_announcer_01_out` → 95; `sq024_city_together_out` → 307; `sq024_04_racers_talk_corp_end` → 947; `sq024_04_racers_talk_val_end` → 952; `sq024_04_crowd_civ_4_end` → 957; `sq024_04_crowd_civ_3_end` → 962; `sq024_04_crowd_civ_2_end` → 967; `sq024_04_crowd_civ_1_end` → 972; `sharp_turn_out` → 979; `fade_out` → 395; `too_far_1_out` → 614; `too_far_2_out` → 615; `too_far_3_out` → 616; `End 16` → 1041; `End 17` → 1261.

End nodes: 2: `NonTerminating`; 17: `NonTerminating`; 95: `NonTerminating`; 307: `<omitted>`; 395: `NonTerminating`; 445: `NonTerminating`; 614: `<omitted>`; 615: `<omitted>`; 616: `<omitted>`; 636: `<omitted>`; 637: `<omitted>`; 638: `<omitted>`; 639: `<omitted>`; 947: `<omitted>`; 952: `<omitted>`; 957: `<omitted>`; 962: `<omitted>`; 967: `<omitted>`; 972: `<omitted>`; 979: `<omitted>`; 1041: `<omitted>`; 1261: `<omitted>`; 1279: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 428 / 357 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scnChangeIdleAnimEvent` | 13 | 20 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnDialogLineEvent` | 86 | 20 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnGameplayTransitionEvent` | 6 | 341 / 189 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/29` |
| `scnIKEvent` | 12 | 341 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/21` |
| `scnLookAtEvent` | 42 | 20 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 53 | 20 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnUnmountEvent` | 6 | 341 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/28` |
| `scneventsAttachPropToPerformer` | 2 | 341 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/3` |
| `scneventsAttachPropToWorld` | 2 | 341 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/7` |
| `scneventsCameraParamsEvent` | 3 | 400 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 6 | 341 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/25` |
| `scneventsSocket` | 58 | 20 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsVFXEvent` | 1 | 341 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, audio, socket_signal: 1
- gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1
- gaze: 1

Raw SHA-256: `b164b74049bd06a2cc276927177b2fed20d8596ed26e59604c2e97486704c989`. Binary SHA-256: `7b749b7704a8e5eef1a7cfd9b33e2030ba1db7575ec1d88e5896d1a50b107e6b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_04_city_race.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_04b_docks_scene.scene`

96 graph nodes, 106 edges; 24 event-bearing sections, 173 events; 64 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: claire (actor 0, spawnSet); racer_1 (actor 1, community); racer_2 (actor 2, community); announcer (actor 3, findInContext); crowd_end_civ_1 (actor 4, community); crowd_end_civ_2 (actor 5, community); crowd_end_civ_3 (actor 6, community); claire_truck (actor 7, community); Player (actor 8, findInContext).

Entries: `sq024_03b_ride_to_garage_in` → 104; `sq024_03b_race_finish_in` → 106; `sq024_reuse_big_race_won` → 425; `sq024_04b_end_civ_3_start` → 269; `sq024_04b_end_civ_2_start` → 272; `sq024_03b_talking_racers_in` → 116; `sq024_04b_end_civ_1_start` → 275.

Exits: `sq024_03b_ride_to_garage_out` → 105; `sq024_03b_race_finish_out` → 107; `End 2` → 427; `sq024_04b_end_civ_3_end` → 271; `sq024_04b_end_civ_2_end` → 274; `sq024_04b_end_civ_1_end` → 277; `sq024_03b_first_race_out` → 125; `sq024_03b_end_out` → 137; `End1` → 308.

End nodes: 105: `<omitted>`; 107: `<omitted>`; 125: `NonTerminating`; 137: `<omitted>`; 271: `<omitted>`; 274: `<omitted>`; 277: `<omitted>`; 308: `<omitted>`; 427: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 108 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 53 | 108 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 129 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/12` |
| `scnIKEvent` | 12 | 129 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scnLookAtEvent` | 23 | 108 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 23 | 111 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scnPoseCorrectionEvent` | 5 | 129 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/6` |
| `scnUnmountEvent` | 4 | 129 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 4 | 129 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/8` |
| `scneventsSocket` | 35 | 118 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- gaze: 3
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- ik: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, idle_animation: 1
- speech: 1
- socket_signal, animation_state: 1
- speech, socket_signal: 1

Raw SHA-256: `6bf7a40541087fcee9c8e7447b3cab17f67d948e903e9d4f25130f9acdf86e56`. Binary SHA-256: `7842282f825dc0449783de6111bd9e5ca03bc65dfd17c1bdcdca8855c219cc7f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_04b_docks_scene.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_05_big_race.scene`

209 graph nodes, 214 edges; 52 event-bearing sections, 317 events; 123 screenplay lines, 12 screenplay options, 7 choice nodes.

Actors: claire (actor 0, spawnSet); announcer (actor 1, findInContext); sampson (actor 2, spawnSet); claire_phone (actor 3, spawnSet); sampson_gunner (actor 4, spawnSet); prost (actor 5, community); racer_scv_1 (actor 6, community); racer_scv_2 (actor 7, community); crowd_civ_1 (actor 8, community); crowd_civ_2 (actor 9, community); crowd_civ_3 (actor 10, community); crowd_6th (actor 11, community); end_civ_1 (actor 12, community); end_scv (actor 13, community); end_civ_2 (actor 14, community); sq024_dominic_car (actor 15, spawnSet); big_race_car_001 (actor 16, spawner); big_race_car_002 (actor 17, spawner); big_race_car_003 (actor 18, spawner); big_race_car_005 (actor 19, spawner); big_race_car_004 (actor 20, spawner); big_race_car_006 (actor 21, spawner); v (actor 22, findInContext).

Entries: `sq024_05_call_in` → 1; `sq024_05_big_pre_race_in` → 17; `sq024_05_continue_race_2_in` → 220; `sq024_05_follow_dominic_2_in` → 226; `sq024_05_dominic_injured_in` → 58; `sq024_05_end_civs_in` → 772; `sq024_05_dominic_beat_race_in` → 84; `sq024_05_after_race_dominic_alive_in` → 93; `sq024_05_after_him_v_in` → 1336; `sq024_05_butt_in` → 1342; `sq024_05_announcer_01_in` → 104; `timelapse_preview` → 838; `sq024_05_follow_dominic_1_in` → 139; `sq024_05_continue_race_1_in` → 140; `sq024_05_race_start_fluff_in` → 865; `Start 4` → 517.

Exits: `texting` → 532; `sq024_05_call_out` → 2; `sq024_05_big_pre_race_out` → 18; `sq024_05_continue_race_2_out` → 221; `End 9` → 934; `sq024_05_follow_dominic_2_out` → 227; `sq024_05_end_civ_1_end` → 774; `sq024_05_spawn_race_out` → 428; `End 10` → 1146; `sq024_05_dominic_beat_race_out` → 87; `sq024_05_after_race_out` → 90; `sq024_05_after_him_v_out` → 1337; `sq024_05_butt_out` → 1343; `sq024_05_announcer_01_out` → 106; `sq024_05_dominic_or_win` → 137; `sq024_05_follow_dominic_1_out` → 141; `sq024_05_continue_race_1_out` → 142; `sq024_05_race_start_fluff_out` → 873; `countdown_out` → 346.

End nodes: 2: `<omitted>`; 18: `NonTerminating`; 87: `<omitted>`; 90: `<omitted>`; 106: `NonTerminating`; 137: `<omitted>`; 141: `<omitted>`; 142: `<omitted>`; 221: `NonTerminating`; 227: `<omitted>`; 346: `NonTerminating`; 428: `NonTerminating`; 532: `NonTerminating`; 774: `<omitted>`; 873: `<omitted>`; 934: `<omitted>`; 1146: `<omitted>`; 1337: `<omitted>`; 1343: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 340 / 499 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/1` |
| `scnChangeIdleAnimEvent` | 17 | 202 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/2` |
| `scnDialogLineEvent` | 100 | 8 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayActionEvent` | 2 | 310 / 380 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/10` |
| `scnGameplayTransitionEvent` | 4 | 133 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/10` |
| `scnIKEvent` | 8 | 133 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |
| `scnLookAtEvent` | 61 | 8 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 53 | 8 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnUnmountEvent` | 3 | 133 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 7 | 133 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/6` |
| `scneventsSocket` | 58 | 8 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, gaze: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, ik, gameplay_transition, socket_signal, animation_state: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, audio, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- gaze: 1
- idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, idle_animation, gaze: 1
- skeletal_animation: 1
- speech, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `a9b61d379ba8bd978728f62ac2f385955b6ffd0367fb7e0146ba45526d4b8971`. Binary SHA-256: `f54645eec5195b18ed98e029f0fe5174f647a65b0b93bfb9563416d1a2dbb575`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_05_big_race.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_05b_trauma_team.scene`

250 graph nodes, 295 edges; 35 event-bearing sections, 365 events; 77 screenplay lines, 7 screenplay options, 5 choice nodes.

Actors: claire (actor 0, spawnSet); sampson (actor 1, spawnSet); sampson_gunner (actor 2, spawnSet); crash_car_driver (actor 3, spawner); crowd_driver_front (actor 4, spawner); crowd_driver_right_0 (actor 5, spawner); crowd_driver_right_1 (actor 6, spawner); crowd_driver_back (actor 7, spawner); crowd_driver_left_0 (actor 8, spawner); crowd_driver_left_1 (actor 9, spawner); crowd_helper_0 (actor 10, spawner); crowd_helper_1 (actor 11, spawner); crowd_bystander_0 (actor 12, spawner); crowd_bystander_1 (actor 13, spawner); crowd_bystander_2 (actor 14, spawner); crowd_bystander_3 (actor 15, spawner); crowd_bystander_4 (actor 16, spawner); crowd_bystander_5 (actor 17, spawner); sq024_05b_sampson_car (actor 18, spawnSet); sq024_05b_crash_car (actor 19, spawner); crowd_car_front (actor 20, spawner); crowd_car_right_0 (actor 21, spawner); crowd_car_right_1 (actor 22, spawner); crowd_car_back (actor 23, spawner); crowd_car_left_0 (actor 24, spawner); crowd_car_left_1 (actor 25, spawner); claire_car (actor 26, community); v (actor 27, findInContext).

Entries: `sq024_05b_tt_in` → 1; `q000_car_reuse` → 1233; `claire_kills` → 1161; `scene_pass_claire_spares` → 1170; `claire_kills_no_choice` → 1193.

Exits: `sq024_05b_sampson_dead_out` → 2; `q000_hijack_end` → 1236; `check_player_left` → 553.

End nodes: 2: `<omitted>`; 553: `NonTerminating`; 1236: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 506 / 514 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/5` |
| `scnChangeIdleAnimEvent` | 14 | 140 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 60 | 116 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 9 | 212 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/24` |
| `scnIKEvent` | 18 | 212 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnLookAtEvent` | 76 | 206 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 70 | 206 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnUnmountEvent` | 9 | 212 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/23` |
| `scneventsSetAnimFeatureEvent` | 9 | 212 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/19` |
| `scneventsSocket` | 94 | 140 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsVFXEvent` | 4 | 212 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 8
- speech: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `565881eae525b90a9ec57983daf0ccc7135128f47a598b8c9685ab4484a601da`. Binary SHA-256: `9b5a455f8025a4bed7df122e700efe45c430ffef5562b39771acc8a568f11dd4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_05b_trauma_team.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_06_bar_ending.scene`

66 graph nodes, 92 edges; 9 event-bearing sections, 85 events; 29 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: claire (actor 0, spawnSet); claire_truck (actor 1, community); Player (actor 2, findInContext).

Entries: `sq024_06_ending_on_foot_in` → 176; `sq024_06_drive_in` → 119.

Exits: `leave` → 606; `sq024_06_drive_out` → 120.

End nodes: 120: `<omitted>`; 606: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 122 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 24 | 122 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 483 / 273 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/16` |
| `scnIKEvent` | 5 | 122 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 14 | 160 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 20 | 122 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPoseCorrectionEvent` | 3 | 122 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 1 | 483 / 272 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 5 | 122 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 8 | 122 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, socket_signal, animation_state: 1

Raw SHA-256: `c6498ee4f9ed0ffeb9a68254ee25cc0a9d7fff9fccaf04e2643a795eb48617d9`. Binary SHA-256: `cdc49d87d637588b4d23ea7399b8780036076d3acaafd46c5c43859fa530ef85`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_06_bar_ending.scene" --events
```

