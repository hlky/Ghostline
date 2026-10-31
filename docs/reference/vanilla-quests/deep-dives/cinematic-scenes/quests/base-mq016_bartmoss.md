# KOLD MIRAGE: scene presentation

Journal identity: `quests/minor_quest/mq016_bartmoss`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq016_bartmoss.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene`

97 graph nodes, 105 edges; 14 event-bearing sections, 84 events; 27 screenplay lines, 10 screenplay options, 7 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `in` → 1.

Exits: `out` → 2; `End 1` → 426.

End nodes: 2: `NonTerminating`; 426: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 26 | 28 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 646 / 667 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/7` |
| `scnIKEvent` | 2 | 646 / 661 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/2` |
| `scnLookAtEvent` | 7 | 28 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnOverridePhantomParamsEvent` | 1 | 646 / 660 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/1` |
| `scnPlaySkAnimEvent` | 32 | 28 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnUnmountEvent` | 1 | 646 / 666 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/6` |
| `scneventsEquipItemToPerformer` | 1 | 28 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 646 / 664 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/5` |
| `scneventsSocket` | 8 | 28 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsVFXEvent` | 4 | 28 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 7
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `2c4b80ffb716b234e7a72f17a8787e81022c6f863b482b2d14fa6e33e45f39a3`. Binary SHA-256: `e41323c95eaabf32a656384fb6a24717a117116a3326917af04bf97cb0a98268`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene" --events
```

## `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene`

138 graph nodes, 162 edges; 28 event-bearing sections, 144 events; 66 screenplay lines, 13 screenplay options, 7 choice nodes.

Actors: nix (actor 0, spawnSet); johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `in` → 1.

Exits: `out_clean_up` → 574; `out_decrypted` → 102.

End nodes: 102: `NonTerminating`; 574: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 65 | 12 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 15 | 12 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 38 | 12 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsAttachPropToNode` | 3 | 297 / 241 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scneventsAttachPropToPerformer` | 1 | 297 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/2` |
| `scneventsEquipItemToPerformer` | 1 | 747 / 705 | `/Data/RootChunk/sceneGraph/Data/graph/94/Data/events/3` |
| `scneventsSocket` | 11 | 12 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 747 / 716 | `/Data/RootChunk/sceneGraph/Data/graph/94/Data/events/7` |
| `scneventsVFXEvent` | 9 | 23 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, vfx: 1
- speech, vfx: 1
- speech, gaze: 1

Raw SHA-256: `e5a9c9ab3130ca63a58db47c66b938bc5fddfdf3fedb4691f0a1f1cb196bc4de`. Binary SHA-256: `c716dba8fc01aec83978b81528910ec899bc81fca048ce3bb2a39a5cec17609e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene" --events
```

