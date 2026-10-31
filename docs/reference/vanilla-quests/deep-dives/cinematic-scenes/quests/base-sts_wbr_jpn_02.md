# Gig: We Have Your Wife: scene presentation

Journal identity: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wbr_jpn_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02.scene`

15 graph nodes, 11 edges; 5 event-bearing sections, 36 events; 35 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Lauren (actor 0, findInWorld); Enemy1 (actor 1, findInWorld); Enemy2 (actor 2, findInWorld); Worker1 (actor 3, findInWorld); Worker2 (actor 4, findInWorld); Worker3Elevator (actor 5, findInWorld); Enemy8 (actor 6, findInWorld); V (actor 7, findInContext).

Entries: `jpn_02_enemy1_enemy2_chat_start` → 24; `jpn_02_workers_chat_children_start` → 144; `jpn_02_scream_elevator_start` → 111; `jpn_02_torturer_start` → 29.

Exits: `jpn_02_scream_elevator_end` → 110; `jpn_02_workers_chat_children_end` → 145; `jpn_02_enemy1_enemy2_chat_end` → 27; `jpn_02_torturer_end` → 32.

End nodes: 27: `NonTerminating`; 32: `NonTerminating`; 110: `NonTerminating`; 145: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 35 | 30 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 1 | 115 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation: 1

Raw SHA-256: `5fe024e0eea1a3371efd55e8eb8b6ed4ac2ab5fc5ac61af0d68bff4aa3f059dd`. Binary SHA-256: `0a94b5623c1d0f100bee8d3c6c5982e6905d21a7bae7359f2b50defa60c44001`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: wakako (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 289.

End nodes: 2: `<omitted>`; 289: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `51465b5996379f73ba618db4dde21d8b235cab1af1eb9e537d374e8ce703a320`. Binary SHA-256: `518e514ce9bdd18a265aac5f3e1a28fc3fc3b4159d2306d17eb404d003449515`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: wakako (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 30 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `26a306dec22bf5d6472dd403930297184e9e28505d627322af8aabfbaa923ac4`. Binary SHA-256: `abda17a0b9d56199597fa0f4ba8bc4afdb853e95c460de8497d883155e2d2dde`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_lauren.scene`

33 graph nodes, 34 edges; 14 event-bearing sections, 70 events; 31 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: Lauren (actor 0, community); V (actor 1, findInContext).

Entries: `jpn_02_lauren_first_start` → 1; `jpn_02_have_to_call_start` → 144; `jpn_02_bill_last_start` → 39; `jpn_02_lauren_head_low_start` → 128.

Exits: `jpn_02_have_to_call_end` → 145; `jpn_02_lauren_first_end` → 124; `jpn_02_lauren_head_low_end` → 127; `jpn_02_bill_last_end` → 48.

End nodes: 48: `NonTerminating`; 124: `NonTerminating`; 127: `NonTerminating`; 145: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 30 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 8 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnIKEvent` | 4 | 8 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnLookAtEvent` | 8 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 14 | 8 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnUnmountEvent` | 2 | 8 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 8 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsSocket` | 8 | 8 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 3
- speech, gaze: 2
- speech, skeletal_animation, socket_signal: 2
- speech: 2
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `fdaa899b94ecca8dd7c0f9a4d125ef9ff8b98b8217b71fc8c3d4ce735b5f55b6`. Binary SHA-256: `86d2caeed68f8cc1d778b38b2f75ad4fedacefdbcc6b34cb99b77bb95af8cf68`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_lauren.scene" --events
```

