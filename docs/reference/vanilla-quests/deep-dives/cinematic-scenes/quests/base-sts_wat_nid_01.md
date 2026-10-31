# Gig: Occupational Hazard: scene presentation

Journal identity: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_nid_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_hal.scene`

97 graph nodes, 106 edges; 23 event-bearing sections, 165 events; 43 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: hal (actor 0, community); player (actor 1, findInContext).

Entries: `hal` → 6.

Exits: `after sts end` → 132.

End nodes: 132: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 36 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnDialogLineEvent` | 34 | 11 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 304 / 410 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/7` |
| `scnIKEvent` | 4 | 304 / 403 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/1` |
| `scnLookAtEvent` | 17 | 21 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnPlaySkAnimEvent` | 42 | 11 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 2 | 304 / 409 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/6` |
| `scneventsAttachPropToPerformer` | 1 | 93 / 203 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/5` |
| `scneventsAttachPropToWorld` | 1 | 93 / 247 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/28` |
| `scneventsEquipItemToPerformer` | 3 | 93 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 304 / 407 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/5` |
| `scneventsSocket` | 44 | 11 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 93 / 260 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/36` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech: 2
- speech, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `5d3fd4f7dc09c577f6e9e6326cf3a6a804ad99a4fe63503459e462f77cb63fac`. Binary SHA-256: `c1c606ca64d9b5570e430bdf9668eb11b7714977020df226e10d4f46cd3d4f3a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_hal.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_debrief.scene`

29 graph nodes, 39 edges; 3 event-bearing sections, 6 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 101.

Exits: `rejected_out` → 294; `End 0` → 102.

End nodes: 102: `<omitted>`; 294: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `a62afc3aca69fe901f56cdc2b5aae1c4e099855d4851f6c912e03c3383b0ad6a`. Binary SHA-256: `069e7b65c8fe3e3afa4aa79da52257b73cd35c977a736f4df0263a4f4cd41764`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_debrief.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start1` → 56.

Exits: `End1` → 57; `rejected_out` → 260.

End nodes: 57: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 29 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `8fb967e8034d5d2ac85553941b439abcec6e79cb2c3c71c6965de4d511d6d4cb`. Binary SHA-256: `06126d3e0b23be3c32739d7c4dcfc551501a7965ad9fe8a4b9508dc9bb98b8c3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_lizzie.scene`

31 graph nodes, 44 edges; 7 event-bearing sections, 58 events; 16 screenplay lines, 4 screenplay options, 1 choice nodes.

Actors: lizzie (actor 0, community); psycho (actor 1, community); player (actor 2, findInContext).

Entries: `lizzie` → 90.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 91 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 14 | 91 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnLookAtEvent` | 19 | 91 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 10 | 91 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsSocket` | 13 | 91 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, gaze: 1
- gaze: 1

Raw SHA-256: `257cc2015a58cbb3d14359c2310cbab5ee20ecc55fde28f5c5ab18b4e9c7a21a`. Binary SHA-256: `7aed6d3db0c8e371d563891e9935fad9b10f92e01f50af3093a6426e3a30886d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_lizzie.scene" --events
```

