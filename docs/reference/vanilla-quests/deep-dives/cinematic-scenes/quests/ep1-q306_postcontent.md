# From Her to Eternity: scene presentation

Journal identity: `ep1/quests/main_quest/q306_postcontent`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q306_postcontent.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene`

32 graph nodes, 32 edges; 2 event-bearing sections, 15 events; 5 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Songbird (actor 0, findInContext); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 101 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnDialogLineEvent` | 3 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 101 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scnIKEvent` | 2 | 101 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scnPlaySkAnimEvent` | 1 | 101 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 1 | 101 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsEquipItemToPerformer` | 1 | 101 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 1 | 101 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSocket` | 3 | 101 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsVFXEvent` | 1 | 101 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- skeletal_animation, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `dce446754f2d1ad495264db7da706bbf34c17b4930b783a21aa112e92ec45010`. Binary SHA-256: `77e8891edfe4abbabb892825d0959ea87cf3cce7a9be4d03f2581f940fe4292d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene" --events
```

