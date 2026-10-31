# Gig: Serious Side Effects: scene presentation

Journal identity: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_arr_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\new_scenes\sts_std_arr_01_cleaner_new.scene`

62 graph nodes, 68 edges; 11 event-bearing sections, 138 events; 26 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: Cleaner (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `preview solo` → 460.

Exits: `End 0` → 2; `force_end` → 628.

End nodes: 2: `NonTerminating`; 628: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 12 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnDialogLineEvent` | 21 | 12 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 12 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/27` |
| `scnIKEvent` | 6 | 12 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scnLookAtEvent` | 16 | 12 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 33 | 12 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 3 | 12 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/26` |
| `scneventsEquipItemToPerformer` | 3 | 462 / 286 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 3 | 12 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/23` |
| `scneventsSocket` | 34 | 12 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 21 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 12 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |
| `scneventsVFXEvent` | 2 | 12 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `7f622b658e0735d7a217e1615532139e84b4eadf1e405767e030fd673c93fc3a`. Binary SHA-256: `3f7130efb1eee71197275d28bd306eb809b8a475871000273e93fae683d0bef4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\new_scenes\sts_std_arr_01_cleaner_new.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\new_scenes\sts_std_arr_01_recepctionist_new.scene`

78 graph nodes, 103 edges; 13 event-bearing sections, 138 events; 27 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Receptionist (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 5` → 440.

Exits: `End1` → 149.

End nodes: 149: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 20 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 25 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 33 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsEquipItemToPerformer` | 2 | 12 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsSocket` | 37 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 3 | 21 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsVFXEvent` | 2 | 23 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `c2a69380a4bc6c19e91724eb86cca80fa849d9c1d88a9ed8a175838ec59ba1f7`. Binary SHA-256: `3bef46dfa8d8210583367a59d2812a3a1686150df7ce3b8c226970fb2cb0a963`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\new_scenes\sts_std_arr_01_recepctionist_new.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\new_scenes\sts_std_arr_01_room_new.scene`

71 graph nodes, 77 edges; 10 event-bearing sections, 79 events; 19 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `trigger start` → 1; `conclusion start` → 278; `scanning_001_start` → 295; `scanning_002_start` → 296.

Exits: `conclusion end` → 2; `scanning_002_end` → 312; `scanning_001_end` → 276; `trigger_end` → 293.

End nodes: 2: `<omitted>`; 276: `<omitted>`; 293: `<omitted>`; 312: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 12 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 13 | 12 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 21 | 12 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 19 | 12 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 15 | 12 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- gaze: 4

Raw SHA-256: `298e82edbe048a54fa3261b22cc11b63aff8f5e2310741b9977ce270bec5d413`. Binary SHA-256: `bf090547596032f98d65add2ca3e24cd20e62dd89473a1d0782ae1bc16ffb951`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\new_scenes\sts_std_arr_01_room_new.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\sts_std_arr_01_civilians.scene`

12 graph nodes, 12 edges; 3 event-bearing sections, 12 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: man_002 (actor 0, findInWorld); man_004 (actor 1, findInWorld); woman_002 (actor 2, findInWorld); woman_001 (actor 3, findInWorld); Player (actor 4, findInContext).

Entries: `arr_01_civilians_chat_001_start` → 1; `arr_01_civilians_chat_002_start` → 27; `arr_01_civilians_chat_003_start` → 58.

Exits: `arr_01_civilians_chat_001_end` → 2; `arr_01_civilians_chat_002_end` → 19; `arr_01_civilians_chat_003_end` → 59.

End nodes: 2: `NonTerminating`; 19: `NonTerminating`; 59: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 105 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnLookAtEvent` | 6 | 105 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 3

Raw SHA-256: `1591ad9cafbfe14b66749a090aadb3db07966e6fd85552240083f0ee8dede2de`. Binary SHA-256: `8b253d155152b64b286793823379d7c6a4fa9481dc1a656c81690aa1edde86ae`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\sts_std_arr_01_civilians.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\sts_std_arr_01_holocall_debriefs.scene`

29 graph nodes, 39 edges; 2 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: El_Capitan (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `rejected_out` → 290; `optional` → 2; `non_optional` → 63.

End nodes: 2: `<omitted>`; 63: `<omitted>`; 290: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 42 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `6c9fe07d60728afaa65be9d8e6da8537185603cbe7c15d8339c481a263a9906f`. Binary SHA-256: `e7ea5214bb47d5df05f7b706e0f8fa3d5d9e2605dbd1dbb23a51f07098585a72`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\sts_std_arr_01_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\sts_std_arr_01_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: El_Capitan (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `d85aef9996aff0ea9731024fefc4056a8fdd24f993a12ae6aacc3ee1b3e9c703`. Binary SHA-256: `ef9847db90b4b7f34be4d09837870071e16e8f6140c55dfe8c3c46f233c791e8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_01\scenes\sts_std_arr_01_holocall_prebrief.scene" --events
```

