# Totalimmortal: scene presentation

Journal identity: `quests/main_quest/act_01/q113_corpo`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q113_corpo.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q113\scenes\q113_03a_haru_kasai_drive.scene`

144 graph nodes, 193 edges; 40 event-bearing sections, 305 events; 71 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Anders (actor 0, spawnSet); Yorinobu_Guard (actor 1, community); Takemura (actor 2, spawnSet); q113_03a_thrax (actor 3, spawner); V (actor 4, findInContext).

Entries: `q113_03a_drive_in` → 7; `q113_03a_guard_in` → 20; `q113_03a_guard_dead_in` → 67; `audio_test` → 847.

Exits: `q113_03a_drive_out` → 13; `q113_03a_guard_out` → 150; `End2` → 674; `q113_03a_guard_dead_out` → 88; `End1` → 491.

End nodes: 13: `NonTerminating`; 88: `NonTerminating`; 150: `NonTerminating`; 491: `NonTerminating`; 674: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 152 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scnChangeIdleAnimEvent` | 18 | 9 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 63 | 9 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 749 / 889 | `/Data/RootChunk/sceneGraph/Data/graph/105/Data/events/6` |
| `scnIKEvent` | 6 | 450 / 577 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/7` |
| `scnLookAtEvent` | 87 | 39 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnPlaySkAnimEvent` | 65 | 39 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 1 | 749 / 888 | `/Data/RootChunk/sceneGraph/Data/graph/105/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 14 | 39 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsSocket` | 44 | 39 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scneventsVFXEvent` | 3 | 39 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, gaze: 3
- speech: 3
- skeletal_animation: 3
- speech, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, audio, socket_signal, animation_state: 2
- skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- ik, socket_signal, animation_state: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze: 1
- socket_signal, animation_state: 1

Raw SHA-256: `eab911dbb5272efb392f20de74ff8a5c52a835fa6b6807fff5bd86fd970be354`. Binary SHA-256: `4d8553d1e13f147166189464366bbf9ecb405b1f97aa34db1794f4adbe6d6a57`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_03a_haru_kasai_drive.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_04_hanako_estate.scene`

255 graph nodes, 303 edges; 52 event-bearing sections, 227 events; 96 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Takemura (actor 0, spawnSet); Hanako (actor 1, spawnSet); Arasaka_Estate_Guard_009 (actor 2, community); Arasaka_Estate_Guard_010 (actor 3, community); Netrunner (actor 4, community); Arasaka_Estate_guard_011 (actor 5, community); Arasaka_Estate_Guard_006 (actor 6, community); Arasaka_Estate_guard_007 (actor 7, community); Anders (actor 8, spawnSet); Hanako_holocall (actor 9, spawnSet); av (actor 10, spawnSet); q113_03a_thrax (actor 11, spawner); V (actor 12, findInContext).

Entries: `q113_04_hanako_in` → 1; `av_start_anim` → 1572; `q113_04_guard_fluff_takedown_in` → 559; `q113_04_exterior_in` → 44; `q113_04_inside_in` → 48; `q113_04_takemura_pickup_in` → 574; `q113_04_alert_in` → 323; `q113_04_close_in` → 69; `q113_04_done_in` → 73; `q113_04_before_av_in` → 80; `q113_04_v_leaves_in` → 354; `q113_04_takemura_takedown_in` → 139; `q113_04_takemura_takedown_done_in` → 144; `q113_04_takemura_netrunner_in` → 149; `q113_04_before_av_in_setup` → 686; `q113_04_mech_NEWNEW_in` → 688; `Start 18` → 2017; `q113_04_guard_fluff_in` → 237.

Exits: `takemura_exit` → 1291; `q113_04_hanako_out` → 2; `av_start_anim_end` → 1575; `q113_04_guard_fluff_out` → 1592; `q113_04_exterior_out` → 45; `q113_04_inside_out` → 49; `av_setup` → 572; `q113_04_takemura_pickup_out` → 577; `q113_04_alert_out` → 326; `q113_04_close_end` → 70; `q113_04_done_out` → 78; `q113_04_before_av_out` → 83; `q113_04_v_leaves_out` → 357; `q113_04_takemura_takedown_out` → 142; `q113_04_takemura_takedown_done_out` → 145; `q113_04_takemura_netrunner_out` → 152; `q113_04_mech_NEWNEW_out` → 690.

End nodes: 2: `<omitted>`; 45: `<omitted>`; 49: `<omitted>`; 70: `<omitted>`; 78: `<omitted>`; 83: `NonTerminating`; 142: `<omitted>`; 145: `<omitted>`; 152: `<omitted>`; 326: `<omitted>`; 357: `<omitted>`; 572: `NonTerminating`; 577: `<omitted>`; 690: `<omitted>`; 1291: `NonTerminating`; 1575: `NonTerminating`; 1592: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 100 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scnChangeIdleAnimEvent` | 8 | 100 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |
| `scnDialogLineEvent` | 87 | 68 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 100 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/20` |
| `scnIKEvent` | 8 | 100 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |
| `scnLookAtEvent` | 32 | 100 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 1550 / 1101 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/6` |
| `scnPlaySkAnimEvent` | 30 | 75 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnPoseCorrectionEvent` | 1 | 661 / 523 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/8` |
| `scnUnmountEvent` | 4 | 100 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/19` |
| `scneventsAttachPropToPerformer` | 6 | 100 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 100 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/14` |
| `scneventsEquipItemToPerformer` | 1 | 624 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 9 | 100 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/16` |
| `scneventsSocket` | 29 | 100 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/13` |
| `scneventsVFXEvent` | 1 | 266 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, gaze: 3
- speech, skeletal_animation: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, vfx: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- gaze, props_equipment, socket_signal: 1
- gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `862a55f2e479133e1b2c730cc97074915d486d0964ec0adfd85ca6952ad62d43`. Binary SHA-256: `39c61b8b250b99f05c078bda6a1263b44fc7b861f626474ac3baa185199c3519`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_04_hanako_estate.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_05_av_flight.scene`

81 graph nodes, 87 edges; 20 event-bearing sections, 305 events; 46 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: hanako (actor 0, spawnSet); haru (actor 1, spawnSet); Takemura (actor 2, spawnSet); av (actor 3, spawner); Player (actor 4, findInContext).

Entries: `q113_05_flight_in` → 1; `q113_05_near_tower_in` → 7.

Exits: `q113_05_flight_out` → 2; `q113_05_near_tower_out` → 8; `end_spline` → 2297.

End nodes: 2: `NonTerminating`; 8: `NonTerminating`; 2297: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 13 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/38` |
| `scnChangeIdleAnimEvent` | 15 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 42 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnLookAtEvent` | 92 | 10 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 64 | 10 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPoseCorrectionEvent` | 1 | 2315 / 765 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/2` |
| `scneventsAttachPropToPerformer` | 10 | 13 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/19` |
| `scneventsSetAnimFeatureEvent` | 20 | 10 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scneventsSocket` | 45 | 10 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/13` |
| `scneventsVFXEvent` | 13 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- socket_signal, animation_state: 1
- skeletal_animation, gaze: 1
- idle_animation, gaze, socket_signal, animation_state: 1

Raw SHA-256: `bea4a468ded256e1c6f2a43a1875963cd27267a49e5ffa16d1c0cd5751dab60b`. Binary SHA-256: `3dc9f3037c749ce68d5d142fb25d432524592e9efd099d7d6e16011cfe9ad95a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_05_av_flight.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_06_saburo_office.scene`

351 graph nodes, 503 edges; 74 event-bearing sections, 513 events; 88 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: hanako (actor 0, spawnSet); michiko (actor 1, findInContext); Takemura (actor 2, spawnSet); Anders (actor 3, spawnSet); av (actor 4, spawner); av_chicken_test (actor 5, spawner); V (actor 6, findInContext).

Entries: `q113_06_office_start_in` → 1; `preview_takemura_helps` → 1886; `preview_input` → 1653; `q113_06_av_landing` → 1439.

Exits: `q113_06_michiko_or_takemura_out` → 19; `End1` → 1899; `q113_06_av_landing_out` → 1441.

End nodes: 19: `NonTerminating`; 1441: `NonTerminating`; 1899: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 158 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scnChangeIdleAnimEvent` | 22 | 35 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnDialogLineEvent` | 67 | 14 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 20 | 35 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/27` |
| `scnIKEvent` | 40 | 35 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scnLookAtEvent` | 100 | 14 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 1463 / 1711 | `/Data/RootChunk/sceneGraph/Data/graph/218/Data/events/2` |
| `scnPlaySkAnimEvent` | 80 | 35 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 229 / 296 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/19` |
| `scnUnmountEvent` | 20 | 35 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/26` |
| `scneventsSetAnimFeatureEvent` | 30 | 35 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/23` |
| `scneventsSocket` | 117 | 35 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/21` |
| `scneventsVFXEvent` | 10 | 158 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- skeletal_animation, gaze, socket_signal: 7
- speech, gaze: 6
- skeletal_animation, socket_signal: 6
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- gaze, socket_signal: 2
- skeletal_animation: 2
- socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation: 2
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- vfx: 1
- skeletal_animation, idle_animation, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- socket_signal, animation_state: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `32ed4c67da53696cba8a4d14525d5b6bb9feae6268a7246257611b1bd3313062`. Binary SHA-256: `08d7b700d381570fc5da53c7eec023ac3244fe6fc8b6bc0957227c45a6760a2d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_06_saburo_office.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_07_mikoshi.scene`

248 graph nodes, 310 edges; 48 event-bearing sections, 441 events; 115 screenplay lines, 20 screenplay options, 9 choice nodes.

Actors: hanako (actor 0, spawnSet); Saburo (actor 1, spawnDespawn); Anders (actor 2, spawnSet); Jackie (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `q113_07_walk_in` → 1; `Mikoshi` → 201.

Exits: `prefetch` → 2; `q113_07_panel_out` → 8.

End nodes: 2: `NonTerminating`; 8: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 10 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnChangeIdleAnimEvent` | 11 | 67 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/19` |
| `scnDialogLineEvent` | 104 | 10 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnGameplayTransitionEvent` | 7 | 142 / 327 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/11` |
| `scnIKEvent` | 14 | 142 / 319 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/4` |
| `scnLookAtEvent` | 80 | 10 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scnPlaySkAnimEvent` | 84 | 10 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 7 | 142 / 326 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/10` |
| `scneventsAttachPropToPerformer` | 6 | 446 / 803 | `/Data/RootChunk/sceneGraph/Data/graph/74/Data/events/9` |
| `scneventsCameraParamsEvent` | 3 | 249 / 472 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 7 | 142 / 322 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/7` |
| `scneventsSocket` | 103 | 10 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsVFXEvent` | 5 | 14 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 13
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, gaze, camera, audio, socket_signal: 1
- skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- speech: 1
- speech, gaze, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- skeletal_animation, gaze, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `9185e546b998f6d721808b1f621a7ce39f73563be9d97cafbde34933e8980306`. Binary SHA-256: `d75912d5facbdaef86273d5e38a4a2bcbb965cee33a1887e7dc7b58a71fc163e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_07_mikoshi.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_09_jungle_start.scene`

558 graph nodes, 766 edges; 103 event-bearing sections, 1738 events; 182 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: Hanako (actor 0, spawnSet); Takemura (actor 1, spawnSet); saburo (actor 2, spawnDespawn); faction_01 (actor 3, community); faction_02 (actor 4, community); Oda (actor 5, spawnSet); Michiko (actor 6, spawnSet); Civilian (actor 7, community); Officer (actor 8, community); faction_03 (actor 9, community); faction_04 (actor 10, community); faction_05 (actor 11, community); Takemura_Loyalist_01 (actor 12, community); Takemura_Loyalist_02 (actor 13, community); Takemura_Loyalist_03 (actor 14, community); Takemura_Loyalist_04 (actor 15, community); Soldier_14 (actor 16, community); Soldier_15 (actor 17, community); Soldier_16 (actor 18, community); Soldier_17 (actor 19, community); Soldier_18 (actor 20, community); faction_06 (actor 21, community); faction_07 (actor 22, community); faction_08 (actor 23, community); faction_09 (actor 24, community); guard_01 (actor 25, community); guard_02 (actor 26, community); guard_03 (actor 27, community); guard_04 (actor 28, community); guard_kiji_01 (actor 29, community); guard_kiji_02 (actor 30, community); guard_kiji_03 (actor 31, community); guard_kiji_04 (actor 32, community); V (actor 33, findInContext).

Entries: `at_table` → 1749; `q113_09_elevator_in` → 41; `guards_test_prev` → 1797; `saburo_preview` → 1918; `Start 11` → 3024.

Exits: `hanako_arrives_conference_save` → 447; `q113_09_meeting_out` → 34; `lockdown` → 130; `squad_arrives` → 296.

End nodes: 34: `<omitted>`; 130: `NonTerminating`; 296: `NonTerminating`; 447: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 12 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/133` |
| `scnChangeIdleAnimEvent` | 71 | 12 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnDialogLineEvent` | 136 | 2 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 28 | 358 / 1733 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/10` |
| `scnIKEvent` | 56 | 358 / 1719 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/1` |
| `scnLookAtAdvancedEvent` | 8 | 23 / 407 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/47` |
| `scnLookAtEvent` | 866 | 12 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 248 | 7 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 28 | 358 / 1732 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/9` |
| `scneventsAttachPropToPerformer` | 6 | 31 / 510 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/16` |
| `scneventsAttachPropToWorld` | 2 | 12 / 207 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/140` |
| `scneventsSetAnimFeatureEvent` | 28 | 358 / 1728 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/6` |
| `scneventsSocket` | 211 | 2 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scneventsVFXEvent` | 34 | 31 / 531 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/29` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 16
- skeletal_animation, socket_signal: 14
- speech: 9
- speech, gaze: 7
- speech, skeletal_animation, gaze, socket_signal: 7
- skeletal_animation, gaze, socket_signal: 6
- socket_signal: 6
- gaze: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, socket_signal: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, audio, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, socket_signal: 2
- gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `9727b5950d3bc952ee74048dc873e7a71010683eb4d0a08497481777d125cd20`. Binary SHA-256: `62269b35d494f3a6fab45c58a4a35a7e9da4be310ca8f77015a1ddfb54e48c30`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_09_jungle_start.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_10_jungle_combat.scene`

62 graph nodes, 68 edges; 12 event-bearing sections, 137 events; 28 screenplay lines, 2 screenplay options, 0 choice nodes.

Actors: Hanako (actor 0, spawnSet); Takemura (actor 1, spawnSet); saburo (actor 2, findInContext); faction_01 (actor 3, community); faction_02 (actor 4, community); Oda (actor 5, spawnSet); Michiko (actor 6, spawnSet); Civilian (actor 7, community); Officer (actor 8, community); V (actor 9, findInContext).

Entries: `q113_10_hanako_to_loyalists_in` → 300; `q113_10_after_fight_in` → 203; `q113_10_hanako_fluff_in` → 324; `q113_michiko_fluff_in` → 281.

Exits: `q113_10_hanako_to_loyalists_out` → 302; `q113_10_after_fight_out` → 268; `q113_10_hanako_fluff_out` → 328; `q113_michiko_fluff_out` → 283.

End nodes: 268: `NonTerminating`; 283: `<omitted>`; 302: `<omitted>`; 328: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 202 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 25 | 202 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnGameplayTransitionEvent` | 2 | 202 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/22` |
| `scnIKEvent` | 4 | 202 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scnLookAtEvent` | 56 | 202 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPlaySkAnimEvent` | 19 | 202 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnUnmountEvent` | 2 | 202 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/21` |
| `scneventsAttachPropToPerformer` | 1 | 202 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 2 | 202 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/18` |
| `scneventsSocket` | 19 | 202 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scneventsVFXEvent` | 4 | 263 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `dfe3be387a5000b1caeea9a13f7adfd8a295490e033a15bb07b3bdb983593fa2`. Binary SHA-256: `b917736c697154cb9680ea4dc852eef0f7710af23771bbda0c89c4fa2828ec6c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_10_jungle_combat.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_11_top_atrium.scene`

129 graph nodes, 144 edges; 29 event-bearing sections, 111 events; 48 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: hanako (actor 0, findInContext); takemura (actor 1, spawnSet); Takemura_Loyalist_00 (actor 2, community); Takemura_Loyalist_02 (actor 3, community); Yorinobu_Soldier_01 (actor 4, community); Victim_02 (actor 5, community); Executioner (actor 6, community); Victim_01 (actor 7, community); V (actor 8, findInContext).

Entries: `q113_11_atrium_start_in` → 1; `q113_11_elevators_broken_in` → 7; `q113_11_in_elevator_in` → 13; `q113_11_fall_guy_in` → 41; `q113_11_takemura_elevator_mount` → 529; `q113_11_elevator_start_in` → 49; `q113_11_2nd_floor_in` → 63; `q113_11_takemura_loyal_in` → 78; `q113_11_takemura_dead_in` → 93; `q113_11_takemura_top_elevator_mount` → 594.

Exits: `q113_11_atrium_start_out` → 2; `q113_11_elevators_broken_out` → 8; `q113_11_in_elevator_out` → 14; `q113_11_fall_guy_out` → 44; `q113_11_elevator_start_out` → 54; `q113_11_takemura_elevator_mount_out` → 546; `q113_11_2nd_floor_out` → 66; `q113_11_takemura_dead_victim_01_dead` → 212; `End1` → 581; `q113_11_takemura_top_elevator_mount_out` → 595.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 14: `<omitted>`; 44: `<omitted>`; 54: `NonTerminating`; 66: `<omitted>`; 212: `NonTerminating`; 546: `NonTerminating`; 581: `<omitted>`; 595: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 50 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scnDialogLineEvent` | 44 | 16 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 296 / 330 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/14` |
| `scnIKEvent` | 4 | 296 / 323 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/8` |
| `scnLookAtEvent` | 15 | 16 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnPlaySkAnimEvent` | 17 | 16 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnPoseCorrectionEvent` | 2 | 533 / 600 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/1` |
| `scnUnmountEvent` | 2 | 296 / 329 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 2 | 296 / 327 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/12` |
| `scneventsSocket` | 18 | 16 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze: 2
- skeletal_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- speech, socket_signal: 1
- socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `65502072a80a0a2f03f44a5797443942fe0ad706c6db30ed0e11ce8ad67d3e54`. Binary SHA-256: `94149a5c78c920b506ebc25a9ba41a30b16167adcf074e8e35800042a0dbcd4e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_11_top_atrium.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_12_ceo_floor.scene`

41 graph nodes, 44 edges; 9 event-bearing sections, 16 events; 13 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: hanako (actor 0, findInContext); takemura (actor 1, spawnSet); smasher (actor 2, spawnSet); Officer (actor 3, community); V (actor 4, findInContext).

Entries: `q113_12_ceo_floor_start_in` → 1; `q113_officer_reinforcements_in` → 46; `q113_12_first_guards_in` → 7.

Exits: `q113_12_ceo_floor_start_out` → 2; `q113_officer_reinforcements_out` → 49; `q113_12_first_guards_out` → 8.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 49: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 13 | 10 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsSocket` | 3 | 10 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, socket_signal: 2

Raw SHA-256: `11d5436470661d186161fede3836a2db5c3b195a4413c8d1a5cfbd9c5c9a15f0`. Binary SHA-256: `54b24b6fc807716c930ffe0a65deeaa6dffc8b3ea4407178e9ff53e3ae3c56cb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_12_ceo_floor.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_13_adam_smasher.scene`

190 graph nodes, 198 edges; 29 event-bearing sections, 98 events; 40 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: smasher (actor 0, spawnSet); Takemura (actor 1, spawnSet); Hanako (actor 2, spawnSet); smasher_q116 (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `q113_12_adam_in` → 4; `q113_12_adam_defeated_in` → 9; `q113_13_smasher_reinforcements_01_in` → 292; `q113_13_smasher_reinforcements_02_in` → 296; `q113_13_smasher_come_to_daddy_in` → 307; `q113_13_v_low_health_in` → 311; `q113_13_smasher_low_health_in` → 316; `q113_13_smasher_to_takemura_in` → 320; `q113_13_smasher_about_oda_in` → 324; `q113_13_smasher_about_rogue_in` → 332; `q113_13_takemura_to_smasher_01_in` → 336; `q113_13_takemura_to_smasher_02_in` → 340; `q113_13_takemura_to_smasher_03_in` → 341; `q113_13_takemura_tip_rockets_in` → 344.

Exits: `q113_12_adam_out` → 5; `q113_12_adam_defeated_out` → 10; `End 2` → 253; `q113_13_smasher_reinforcements_02_out` → 297; `q113_13_smasher_come_to_daddy_out` → 309; `End1` → 114; `q113_13_v_low_health_out` → 313; `q113_13_smasher_low_health_out` → 318; `q113_13_smasher_to_takemura_out` → 322; `q113_13_smasher_about_oda_out` → 329; `q113_13_smasher_about_rogue_out` → 334; `q113_13_takemura_to_smasher_01_out` → 338; `q113_13_takemura_to_smasher_02_out` → 352; `q113_13_takemura_to_smasher_03_out` → 353; `q113_13_takemura_tip_rockets_out` → 355.

End nodes: 5: `NonTerminating`; 10: `NonTerminating`; 114: `<omitted>`; 253: `<omitted>`; 297: `<omitted>`; 309: `<omitted>`; 313: `<omitted>`; 318: `<omitted>`; 322: `<omitted>`; 329: `<omitted>`; 334: `<omitted>`; 338: `<omitted>`; 352: `<omitted>`; 353: `<omitted>`; 355: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 24 | 606 / 497 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/3` |
| `scnDialogLineEvent` | 31 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 2315 / 664 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/7` |
| `scnIKEvent` | 4 | 2315 / 658 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/2` |
| `scnLookAtEvent` | 1 | 606 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/13` |
| `scnPlaySkAnimEvent` | 7 | 149 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/0` |
| `scnUnmountEvent` | 2 | 2315 / 663 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 2315 / 661 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/5` |
| `scneventsSocket` | 16 | 149 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/2` |
| `scneventsVFXEvent` | 9 | 149 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 22
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, vfx, socket_signal: 1
- vfx: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- vfx, socket_signal: 1

Raw SHA-256: `79a06e02d780ceeb3389dea5d44442016c565af15ada8dd51fdd7fab71aa6be9`. Binary SHA-256: `81cc5ae2686d708c101567d0eef669184109ca2e9aeb4b83851e713a84fe933d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_13_adam_smasher.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_14_yorinobu.scene`

310 graph nodes, 382 edges; 62 event-bearing sections, 388 events; 122 screenplay lines, 19 screenplay options, 10 choice nodes.

Actors: hanako (actor 0, spawnSet); takemura (actor 1, spawnSet); yorinobu (actor 2, spawnSet); hanako_phone (actor 3, findInContext); Anders (actor 4, spawnSet); V (actor 5, findInContext).

Entries: `q113_14_go_to_office_in` → 7; `q113_14_confront_in` → 13; `q113_14_embrace_in` → 95; `q113_14_elevator_in` → 112.

Exits: `q113_14_go_to_office_out` → 8; `q113_14_confront_out` → 14; `cut_embrace` → 597; `open_doors` → 605; `unseal_elevator` → 637; `q113_14_embrace_out` → 110; `q113_14_elevator_out` → 120; `End 7` → 1189.

End nodes: 8: `NonTerminating`; 14: `NonTerminating`; 110: `NonTerminating`; 120: `<omitted>`; 597: `NonTerminating`; 605: `NonTerminating`; 637: `NonTerminating`; 1189: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 170 / 266 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/3` |
| `scnChangeIdleAnimEvent` | 12 | 41 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnDialogLineEvent` | 112 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 356 / 555 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/4` |
| `scnIKEvent` | 10 | 356 / 552 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/1` |
| `scnLookAtEvent` | 58 | 41 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |
| `scnPlaySkAnimEvent` | 74 | 41 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scnUnmountEvent` | 5 | 356 / 560 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/8` |
| `scneventsAttachPropToPerformer` | 2 | 857 / 1046 | `/Data/RootChunk/sceneGraph/Data/graph/134/Data/events/0` |
| `scneventsAttachPropToWorld` | 1 | 266 / 447 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/5` |
| `scneventsCameraParamsEvent` | 7 | 212 / 344 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 5 | 356 / 556 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/5` |
| `scneventsSocket` | 86 | 10 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 5 | 531 / 707 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- skeletal_animation, gaze, socket_signal: 7
- speech: 6
- speech, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, gaze: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze: 2
- skeletal_animation, audio, socket_signal: 2
- skeletal_animation, gaze: 2
- camera: 2
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- props_equipment: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1

Raw SHA-256: `f1ae493f431bc21038237d230f5892303675cd08cdf862937344acff2a07e255`. Binary SHA-256: `eeb1d730498bedacd32f79bd9342d0ff0d4a6c3f57bb182f66e648d8daa18d39`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_14_yorinobu.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_06_regroup.scene`

369 graph nodes, 379 edges; 69 event-bearing sections, 186 events; 144 screenplay lines, 15 screenplay options, 5 choice nodes.

Actors: rogue (actor 0, spawnSet); weyland (actor 1, spawnSet); guard_1 (actor 2, community); guard_2 (actor 3, community); arasaka_ai (actor 4, spawnDespawn); trying_to_get_inside_av (actor 5, community); q115_crashed_av (actor 6, spawner); V (actor 7, findInContext).

Entries: `q115_solo_ai_in` → 1211; `q115_05_birbs_in` → 1218; `commander_dead_in` → 833; `near_elevator_no_weyland_in` → 850; `used_elevator_no_weyland_in` → 856; `secret_elevator_no_weyland_in` → 868; `targeting_weyland_1` → 467; `secret_elevator_weyland_in` → 874; `secret_elevator_ledge_in` → 886; `secret_elevator_in` → 895; `q115_rogue_weyland_to_elev_in` → 1702; `spotted_first_guards_in` → 928; `rogue_second_td_done` → 558; `after_first_guards_in` → 963; `first_guards_player_left_in` → 973; `takedown_activate_in` → 608; `spotted_combat_in` → 1019; `weyland_second_thanks_in` → 621; `q115_05_stealth_takedown_in` → 1039; `landing_in` → 240; `q115_05_use_terminal_in` → 1050; `rogue_first_guards_in` → 245; `q115_05_play_chippin_in` → 1053; `rogue_first_guards_td_in` → 250; `q115_05_lights_in` → 1060; `weyland_thanks_in` → 255; `q115_05_fog_in` → 1065; `rogue_weyland_in` → 260; `rogue_first_guards_02_in` → 265; `commander_keycard_looted_in` → 1076; `q113_lockdown_start_in` → 1105; `Start 20` → 1130; `q115_06_terminal_in` → 1132; `die` → 1139; `regroup_commander_in` → 336; `elevator_fluff_in` → 380; `Start 25` → 1593; `commander_takedown_ready_in` → 799; `Start 27` → 2011.

Exits: `landing_out` → 411; `q115_05_birbs_out` → 1219; `commander_dead_out` → 834; `near_elevator_no_weyland_out` → 851; `used_elevator_no_weyland_out` → 857; `weyland_imprisoned_out` → 465; `secret_elevator_no_weyland_out` → 869; `secret_elevator_weyland_out` → 875; `secret_elevator_ledge_out` → 887; `secret_elevator_out` → 896; `first_guards_sneak_out` → 929; `q115_rogue_weyland_to_elev_out` → 1736; `first_guards_takedown_out` → 930; `after_first_guards_out` → 964; `first_guards_player_left_out` → 974; `guards_move` → 1011; `takedown_activate_out` → 614; `spotted_combat_out` → 1020; `regroup_commander_walk` → 618; ` weyland_second_thanks_out` → 624; `q115_05_stealth_takedown_out` → 1040; `q115_05_use_terminal_out` → 1051; `rogue_first_guards_out` → 246; `q115_05_play_chippin_out` → 1054; `rogue_first_guards_td_out` → 251; `q115_05_lights_out` → 1061; `weyland_to_commander_out` → 256; `q115_05_fog_out` → 1066; `rogue_first_guards_02_out` → 266; `commander_keycard_looted_out` → 1077; `regroup_commander_out` → 343; `elevator_fluff_out` → 383; `weyland_to_elevator_out` → 786; `commander_takedown_ready_out` → 800; `q115_solo_ai_out` → 1208.

End nodes: 246: `<omitted>`; 251: `<omitted>`; 256: `<omitted>`; 266: `<omitted>`; 343: `<omitted>`; 383: `<omitted>`; 411: `NonTerminating`; 465: `<omitted>`; 614: `<omitted>`; 618: `NonTerminating`; 624: `<omitted>`; 786: `<omitted>`; 800: `<omitted>`; 834: `<omitted>`; 851: `<omitted>`; 857: `<omitted>`; 869: `<omitted>`; 875: `<omitted>`; 887: `<omitted>`; 896: `<omitted>`; 929: `<omitted>`; 930: `<omitted>`; 964: `<omitted>`; 974: `<omitted>`; 1011: `NonTerminating`; 1020: `<omitted>`; 1040: `<omitted>`; 1051: `<omitted>`; 1054: `<omitted>`; 1061: `<omitted>`; 1066: `<omitted>`; 1077: `<omitted>`; 1208: `<omitted>`; 1219: `<omitted>`; 1736: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 1138 / 924 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/2` |
| `scnDialogLineEvent` | 103 | 247 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 1138 / 921 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 1535 / 1094 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/7` |
| `scnIKEvent` | 4 | 1535 / 1088 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/1` |
| `scnLookAtEvent` | 17 | 257 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPlaySkAnimEvent` | 19 | 257 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnUnmountEvent` | 2 | 1535 / 1100 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/12` |
| `scneventsCameraParamsEvent` | 3 | 692 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 1535 / 1096 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/9` |
| `scneventsSocket` | 29 | 257 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scneventsVFXEvent` | 3 | 692 / 316 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 43
- speech, socket_signal: 4
- skeletal_animation: 4
- speech, skeletal_animation, gaze: 3
- speech, gaze: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, camera, vfx, socket_signal: 1
- speech, vfx: 1
- skeletal_animation, idle_animation, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `439164211270e7a09bf3d34c248f79f97055262f5551da39bfd332d5d9234796`. Binary SHA-256: `f8604d4eb3e3b20d5cc7d504d6534e7c5b52eea08eee7cd545822dfa5a8e9020`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_06_regroup.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_corpo_02_to_elevators.scene`

263 graph nodes, 323 edges; 39 event-bearing sections, 169 events; 71 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: corpo_friend (actor 0, community); agent_jenkins (actor 1, spawnSet); arasaka_ai (actor 2, community); corpo_01_elevator (actor 3, community); corpo_02_elevator (actor 4, community); corpo_03_elevator (actor 5, community); corpo_04_elevator (actor 6, community); arasaka_ai_2 (actor 7, community); arasaka_ai_voice (actor 8, findInContext); Player (actor 9, findInContext).

Entries: `in` → 1; `q000_corpo_02_arasaka_propaganda_in` → 1067; `q113_q115_elevator_in` → 377; `Start 3` → 666; `Start 5` → 687; `q000_corpo_02_frank_in` → 1239; `Start 8` → 1294.

Exits: `out` → 2; `q000_corpo_02_arasaka_propaganda_out` → 1069; `q113_q115_elevator_out` → 1420; `PrepareJenkinsFloor` → 683; `ad_over_out` → 437.

End nodes: 2: `NonTerminating`; 437: `NonTerminating`; 683: `NonTerminating`; 1069: `<omitted>`; 1420: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 59 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnDialogLineEvent` | 41 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 541 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/13` |
| `scnIKEvent` | 2 | 541 / 347 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/4` |
| `scnLookAtEvent` | 34 | 57 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 31 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 541 / 366 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 1 | 541 / 362 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/9` |
| `scneventsSocket` | 53 | 3 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- gaze: 8
- skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- socket_signal: 3
- skeletal_animation, socket_signal: 3
- gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation: 1

Raw SHA-256: `75394ac2bbf2bb2f829819facc7bb0a3778932cfdcc50cc6f44722b312e01a01`. Binary SHA-256: `adad2c0437680fc474d1e648844f569a210d0866597fb82b82085a1e28a7e8d7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_corpo_02_to_elevators.scene" --events
```

