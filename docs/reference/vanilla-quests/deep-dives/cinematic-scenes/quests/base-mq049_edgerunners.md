# Over the Edge: scene presentation

Journal identity: `quests/minor_quest/mq049_edgerunners`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq049_edgerunners.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene`

94 graph nodes, 158 edges; 5 event-bearing sections, 30 events; 3 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Player (actor 0, findInContext).

Entries: `mq049_in` → 1; `Start 1` → 46; `Start 2` → 50.

Exits: `mq049_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 11 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 3 | 521 / 546 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 57 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/5` |
| `scnIKEvent` | 2 | 57 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnPlaySkAnimEvent` | 2 | 11 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 1 | 57 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/9` |
| `scneventsAttachPropToNode` | 1 | 57 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsAttachPropToPerformer` | 2 | 11 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsAttachPropToWorld` | 1 | 11 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 1 | 57 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/8` |
| `scneventsSocket` | 8 | 11 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsVFXEvent` | 7 | 11 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `261f31ca3c4b0ed247834339c0ff643251fa73000b88ccfa5f990aed0e63c860`. Binary SHA-256: `5b3edc25afa3bc350bdb71fa5a78d8f84d1d6e4293af8d894bd4b045a88b2387`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq049\scenes\mq049_braindance.scene" --events
```

