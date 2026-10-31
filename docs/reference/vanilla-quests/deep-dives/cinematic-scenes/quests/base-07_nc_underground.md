# The Beast In Me: scene presentation

Journal identity: `quests/meta/07_nc_underground`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-07_nc_underground.md) · [All cinematic studies](../README.md)

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

