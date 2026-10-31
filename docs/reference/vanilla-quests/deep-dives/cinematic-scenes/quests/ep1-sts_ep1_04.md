# Gig: Prototype in the Scraper: scene presentation

Journal identity: `ep1/quests/street_stories/sts_ep1_04`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_04.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan.scene`

203 graph nodes, 219 edges; 52 event-bearing sections, 252 events; 101 screenplay lines, 21 screenplay options, 9 choice nodes.

Actors: hasan (actor 0, community); johnny (actor 1, spawnDespawn); v (actor 2, findInContext).

Entries: `meeting` → 1; `leave` → 376; `on_the_bridge` → 1695; `furnace` → 580; `balcony_scavenger` → 786; `combat_voiceset_start` → 1910; `bodies` → 601; `code_found_earlier` → 1189; `scavengers_takedown` → 266; `bridge` → 839; `hasan_talk_start` → 1788; `by_virus_room` → 298; `gate_opened_combat` → 1061; `gate_opened` → 691; `walkthorugh` → 164; `combat_triggered` → 728; `in_combat` → 732; `combat_by_virus` → 735.

Exits: `meeting_end` → 2; `leave_end` → 378; `on_the_bridge_end` → 1697; `furnace_end` → 582; `bridge_end` → 1713; `combat_voiceset_end` → 1912; `balcony_scavenger_end` → 790; `bodies_end` → 603; `code_found_earlier_end` → 1191; `scavengers_takedown_end` → 270; `hasan_talk_end` → 1792; `by_virus_room_end` → 300; `clear` → 1831; `walkthorugh_end` → 166; `combat_triggered_end` → 737; `combat_by_virus_end` → 741; `in_combat_end` → 367.

End nodes: 2: `NonTerminating`; 166: `NonTerminating`; 270: `<omitted>`; 300: `<omitted>`; 367: `<omitted>`; 378: `<omitted>`; 582: `<omitted>`; 603: `<omitted>`; 737: `<omitted>`; 741: `<omitted>`; 790: `<omitted>`; 1191: `<omitted>`; 1697: `<omitted>`; 1713: `<omitted>`; 1792: `<omitted>`; 1831: `<omitted>`; 1912: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 22 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 94 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 19 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 68 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 47 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXDurationEvent` | 2 | 46 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 22
- speech, skeletal_animation, idle_animation, socket_signal: 8
- speech, skeletal_animation, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, gaze: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `33f5c58dd4a05adf1a290e8b6a40382c08b8380a57dd3944be6eb7a8fe094d96`. Binary SHA-256: `e905e6e57418647e42c540c81aa898ef47e9e4777217587cc1f89df168199653`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan_final.scene`

230 graph nodes, 248 edges; 35 event-bearing sections, 440 events; 76 screenplay lines, 15 screenplay options, 8 choice nodes.

Actors: hasan (actor 0, community); johnny (actor 1, spawnDespawn); hands_man (actor 2, community); fixer (actor 3, spawnSet); extra_hands_merc (actor 4, community); hands_man_car (actor 5, community); V (actor 6, findInContext).

Entries: `Start 0` → 1; `Start 1` → 493.

Exits: `End 0` → 2; `End 3` → 1201; `End 2` → 828.

End nodes: 2: `NonTerminating`; 828: `<omitted>`; 1201: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 28 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnChangeIdleAnimEvent` | 20 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 63 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 11 | 119 / 365 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/7` |
| `scnIKEvent` | 22 | 119 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/3` |
| `scnLookAtAdvancedEvent` | 3 | 327 / 762 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/0` |
| `scnLookAtEvent` | 75 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 101 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnUnmountEvent` | 11 | 119 / 370 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/11` |
| `scneventsAttachPropToPerformer` | 6 | 244 / 549 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/5` |
| `scneventsAttachPropToWorld` | 4 | 244 / 551 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/7` |
| `scneventsCameraParamsEvent` | 4 | 28 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scneventsEquipItemToPerformer` | 3 | 138 / 425 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 15 | 119 / 366 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/8` |
| `scneventsSocket` | 95 | 6 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsUnequipItemFromPerformer` | 2 | 323 / 752 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/43` |
| `scneventsVFXEvent` | 3 | 323 / 701 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, socket_signal: 3
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, camera, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `db5d9f98ac027fb361e78eec4d2143e338aabbe8beee6df5a0dc604049d6b5a2`. Binary SHA-256: `28770b9d6b277adb0f9a6a206c6a05439f9d2aae319ed838acd75d82c70fa97c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan_final.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_holocall_debrief.scene`

37 graph nodes, 43 edges; 4 event-bearing sections, 13 events; 13 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); hands_man (actor 1, community); hasan (actor 2, community); player (actor 3, findInContext).

Entries: `Start 0` → 6; `Start1` → 214; `not_rejectable_q303_start` → 375.

Exits: `End 0` → 8; `rejected_out` → 62; `End1` → 216; `not_rejectable_q303_end` → 376.

End nodes: 8: `<omitted>`; 62: `<omitted>`; 216: `<omitted>`; 376: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 13 | 39 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `4736d2d2b237ffbd6f49b06cc99ab969818e6e5bc9a922066151f248a09c5fc9`. Binary SHA-256: `8b324e165bcb582286afb6b9d0ca6e4129993fb3f0e1093b4ba63194f0b6655e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_holocall_debrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_holocall_gig_failed.scene`

32 graph nodes, 37 edges; 3 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); player (actor 1, findInContext).

Entries: `not_rejectable_q303_start` → 196; `Start 0` → 112.

Exits: `not_rejectable_q303_end` → 197; `rejected_out` → 142; `End 0` → 114.

End nodes: 114: `<omitted>`; 142: `<omitted>`; 197: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 181 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `a1abd2453689da118fcbc134e084749317294b1d6cb83038b47f7eae25248531`. Binary SHA-256: `5a81a0c8dc3c40cabeafe3f6702355cecf13da2db1c33980b6de85be2587c9dd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_holocall_gig_failed.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_holocall_prebrief.scene`

21 graph nodes, 24 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); player (actor 1, findInContext).

Entries: `Start 0` → 35.

Exits: `End 0` → 37; `rejected_out` → 83.

End nodes: 37: `<omitted>`; 83: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 68 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `aa9b67e1fd15b47e06bbc13ee0c5bdea6aaaea4c11d0e4d198d76fb8b27c4ce1`. Binary SHA-256: `fdd8c66af7f5799f742f3e31863305d5d7a8bdc250b90c830a52e8d8590ad36f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_holocall_prebrief.scene" --events
```

