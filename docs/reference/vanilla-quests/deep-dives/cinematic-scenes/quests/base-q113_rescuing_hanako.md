# Last Caress: scene presentation

Journal identity: `quests/main_quest/act_01/q113_rescuing_hanako`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q113_rescuing_hanako.md) · [All cinematic studies](../README.md)

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

