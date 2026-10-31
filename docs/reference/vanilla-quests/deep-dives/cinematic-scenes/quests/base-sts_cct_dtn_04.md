# Gig: Guinea Pigs: scene presentation

Journal identity: `quests/street_stories/city_center/downtown/sts_cct_dtn_04`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_cct_dtn_04.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_holocall_debriefs.scene`

51 graph nodes, 66 edges; 3 event-bearing sections, 6 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `fail start holocall` → 256; `Start 0` → 1.

Exits: `End 0` → 2; `End1` → 366; `End 1` → 274; `rejected_out` → 353.

End nodes: 2: `<omitted>`; 274: `<omitted>`; 353: `<omitted>`; 366: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 91 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `fac818e44f54cb893453557e80270f8a9daa53299729f11ccdd352b71abfee5f`. Binary SHA-256: `781d423a1d25cd390d142a424dba786e70a4265df5c211c31969a470479e80dd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `f957195096b505931517b0c49c965f1fbb59ce414eccdab7e442d32e82d21f9f`. Binary SHA-256: `1d6652813bae8e22426d8b1437d59b92e193fa3c0a1289fd0763713929a16665`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_misc_interactions.scene`

10 graph nodes, 9 edges; 3 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Corporate (actor 0, findInWorld); V (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 1` → 74.

Exits: `End 0` → 2; `End 1` → 75.

End nodes: 2: `<omitted>`; 75: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 63 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `b161161ba12180793edf326fa4b852d72a9dcecb5d15d08b0bbad1956a8df1c5`. Binary SHA-256: `a0c7fabdc0a285921b36e1a2045b5cc5446e1a3f9a9ec37c1b34c490f36cf210`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_misc_interactions.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_receptionist.scene`

31 graph nodes, 43 edges; 8 event-bearing sections, 32 events; 14 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Receptionist (actor 0, community); V (actor 1, findInContext).

Entries: `HackedAfterNotAdded` → 82; `Start 0` → 1.

Exits: `NotAdded` → 30.

End nodes: 30: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 8 | 5 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 8 | 5 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 4 | 5 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 10 | 5 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scneventsVFXEvent` | 2 | 5 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `7bf4fa6054e7bbab5cc2cc1221faa04445e2191e1520a25730d0ddda06df9c76`. Binary SHA-256: `80daf9efc6bb67083aa175f497efb36dd16851136bf4979e88babef62f58e8f9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_receptionist.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_target_elimination.scene`

65 graph nodes, 78 edges; 12 event-bearing sections, 100 events; 20 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: G1 (actor 0, community); G2 (actor 1, community); Joanne_Koch (actor 2, community); Johnny (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `Start 0` → 1; `player_failed_choked_target` → 419; `Player start combat` → 329.

Exits: `SilentKill` → 2; `LoudKill4` → 91.

End nodes: 2: `<omitted>`; 91: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 15 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 15 | 15 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 40 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/13` |
| `scnIKEvent` | 10 | 40 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/7` |
| `scnLookAtEvent` | 10 | 15 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnPlaySkAnimEvent` | 16 | 15 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnUnmountEvent` | 5 | 40 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scneventsAttachPropToPerformer` | 2 | 15 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsAttachPropToWorld` | 1 | 15 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 5 | 40 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/11` |
| `scneventsSocket` | 25 | 15 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 294 / 277 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `407f0bc160dae712fbbbb10138003cc5cd07e3925fd2b2501e58be16ed4a9431`. Binary SHA-256: `bc7b03564838eb5daedb90b91fa834b9033f1a438d0e6642d88851f68bf9adb9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_04\scenes\sts_cct_dtn_04_target_elimination.scene" --events
```

