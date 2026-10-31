# Gig: Playing for Keeps: scene presentation

Journal identity: `quests/street_stories/watson/little_china/sts_wat_lch_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_lch_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start1` → 69.

Exits: `rejected_out` → 288; `End1` → 70.

End nodes: 70: `<omitted>`; 288: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `2b8c5962e4847e7ccd46dcb325d97d0db114c2504d4c3f51e6b84d1fc1882892`. Binary SHA-256: `b9eb1b4cdc5ad5588941574da829b74d70b401648cc3fee775903005a44c9e80`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene" --events
```

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start1` → 56.

Exits: `End1` → 57; `rejected_out` → 260.

End nodes: 57: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `5031c7f56999946f4ae468b33861a87f817db040c4d7632d9288f8aedfb66d45`. Binary SHA-256: `02e7f5efa2ff2bb0345e0abd2a8f03c1ac70ed82a34aaac45e26e0cb8661965e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_johnny.scene`

21 graph nodes, 18 edges; 5 event-bearing sections, 25 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnDespawn); bartender (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `Start 1` → 7; `Start 2` → 16.

Exits: `End 2` → 19; `End 0` → 2; `End 1` → 10.

End nodes: 2: `NonTerminating`; 10: `<omitted>`; 19: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 42 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/5` |
| `scnIKEvent` | 4 | 42 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnLookAtEvent` | 4 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 2 | 42 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 2 | 42 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |
| `scneventsSocket` | 6 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze, socket_signal: 2
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech: 1

Raw SHA-256: `150b039f527f1b68b3337aae865878c1f9bac6cad2ac40a542217ed86819ed17`. Binary SHA-256: `952ba6efc5e6de491d6140a65258e8ec8ccce81524c7f16ad712d6cef30f08bd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_johnny.scene" --events
```

## `base\open_world\vendors\watson\little_china\wat_lch_foodshop_02\wat_lch_foodshop_02.scene`

86 graph nodes, 101 edges; 16 event-bearing sections, 110 events; 26 screenplay lines, 11 screenplay options, 3 choice nodes.

Actors: vendor (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `start` → 4; `Start 1` → 401.

Exits: `end` → 12.

End nodes: 12: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 36 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnDialogLineEvent` | 14 | 35 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 219 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/7` |
| `scnIKEvent` | 8 | 219 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scnLookAtEvent` | 12 | 37 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnPlaySkAnimEvent` | 21 | 35 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnUnmountEvent` | 4 | 219 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/6` |
| `scneventsAttachPropToNode` | 3 | 691 / 422 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/12` |
| `scneventsAttachPropToPerformer` | 5 | 247 / 218 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/2` |
| `scneventsAttachPropToWorld` | 3 | 247 / 222 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 4 | 219 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/5` |
| `scneventsSocket` | 27 | 36 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- gaze: 2
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech: 1
- socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `b260085779159c367c89dda3b6f27f4aca5115b992901839af4d19f4ea5ad3a7`. Binary SHA-256: `7ef9d2a6345fb7bc607b228df05998938f2f9198515b2fdaa90a0c0ce54e9536`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\vendors\watson\little_china\wat_lch_foodshop_02\wat_lch_foodshop_02.scene" --events
```

