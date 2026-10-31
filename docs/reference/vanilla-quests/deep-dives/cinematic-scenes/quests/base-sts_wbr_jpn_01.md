# Gig: Olive Branch: scene presentation

Journal identity: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wbr_jpn_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_alex.scene`

104 graph nodes, 119 edges; 18 event-bearing sections, 70 events; 33 screenplay lines, 9 screenplay options, 4 choice nodes.

Actors: alex (actor 0, community); vehicle (actor 1, community); Player (actor 2, findInContext).

Entries: `In1` → 1; `trunk_setup` → 609; `after_fight_with_tygers` → 440; `exit_vehicle` → 543; `no_path_on_distance_in` → 1022.

Exits: `Out1` → 2; `alex_free_idle_end` → 969; `End 7` → 611; `End2` → 613; `exit_on_distance` → 635; `no_path_on_distance_out` → 1024; `alex_free` → 372.

End nodes: 2: `<omitted>`; 372: `<omitted>`; 611: `NonTerminating`; 613: `<omitted>`; 635: `<omitted>`; 969: `NonTerminating`; 1024: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 27 | 20 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnLookAtEvent` | 6 | 20 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 14 | 24 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 6 | 24 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsSocket` | 17 | 20 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation: 1
- speech, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `a00a5abee26f771a566351c231466d4037e288a5870eee8362f273050302fc46`. Binary SHA-256: `55eff83903f95b2ad81d42e0b669d762f5761f177a40dd78ebe86bf98c1f62bd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_alex.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_holocall_debriefs.scene`

28 graph nodes, 37 edges; 3 event-bearing sections, 7 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: wakako (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 289.

End nodes: 2: `<omitted>`; 289: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 68 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `b3259873e4fad25f3de02201ab62f4dc332be28352ae3927bcd785311718092c`. Binary SHA-256: `d1c347676a393fa47896a28b4909531540a7975caec43247a0f124dbcde07e36`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: wakako (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 30 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `b063890cee3dcaa296611dd551ac42958f841380eae60422134448b27e84ca06`. Binary SHA-256: `b5454d6154b44d9f696681efdcc86319a04101d7caa8b6a7c49911d23f3aaeef`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_meeting_sergei.scene`

42 graph nodes, 44 edges; 8 event-bearing sections, 95 events; 29 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: sergei (actor 0, community); gift_car (actor 1, community); siergei_car (actor 2, community); Player (actor 3, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `End 1` → 205.

End nodes: 2: `<omitted>`; 205: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 28 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 20 / 155 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/24` |
| `scnIKEvent` | 2 | 20 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/19` |
| `scnLookAtEvent` | 2 | 20 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/17` |
| `scnPlaySkAnimEvent` | 32 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 1 | 20 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/23` |
| `scneventsSetAnimFeatureEvent` | 1 | 20 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/22` |
| `scneventsSocket` | 21 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 4 | 12 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1

Raw SHA-256: `94cc89a2ee39f226979d59391eb7257087d44e0b7d4c3eb2d8a5b36e06d0e556`. Binary SHA-256: `963e9db898bb31fc6b0f680cac6f117e8e9a788fcf6928ae9bf73a442d824c62`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_meeting_sergei.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_tyger_claws.scene`

24 graph nodes, 24 edges; 5 event-bearing sections, 19 events; 9 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Enemy_01 (actor 0, community); Enemy_02 (actor 1, community); Enemy_03 (actor 2, community); alex (actor 3, community); gift_car (actor 4, community); Player (actor 5, findInContext).

Entries: `Start 0` → 1; `second_phase` → 117.

Exits: `combat` → 121; `end_scene` → 2; `jpn_01_failed` → 78; `greeting_out` → 115.

End nodes: 2: `<omitted>`; 78: `<omitted>`; 115: `NonTerminating`; 121: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 9 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 4 | 20 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnPlaySkAnimEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 2 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- speech: 1
- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `d99c83fa15d916f19e2504f6d4d5e379779530a5b32a37a7c2e5be755fca2016`. Binary SHA-256: `45a494621dc6abf6f18e620b5ae913c033f7e11c6ead81f26c9eaf02d8a50aa7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\scenes\sts_wbr_jpn_01_tyger_claws.scene" --events
```

