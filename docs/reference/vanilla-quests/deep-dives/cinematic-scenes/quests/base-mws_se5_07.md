# Shape of a Pony: scene presentation

Journal identity: `quests/minor_quest/mws_se5_07`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mws_se5_07.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene`

10 graph nodes, 9 edges; 2 event-bearing sections, 5 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnSet); player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 44 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnOverridePhantomParamsEvent` | 1 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 2 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal, animation_state: 1
- speech: 1

Raw SHA-256: `ff6d834de1f61a5bf1017f5daa9208a2b91984bc9582f6d0980925fb60dac954`. Binary SHA-256: `95adba7d8171e601a3c8eb99cd70b9ca67edf3b82ad8d792e2b8e8f8681aee41`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene" --events
```

## `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene`

10 graph nodes, 9 edges; 2 event-bearing sections, 5 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnSet); porsche_cabrio (actor 1, spawner); player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 53 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnLookAtEvent` | 1 | 8 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 1 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 2 | 8 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, socket_signal: 1
- speech: 1

Raw SHA-256: `a46329accb118bffa0ebb0bc889848e2119dc293f2a13c5489122db5019a2e6b`. Binary SHA-256: `38026a446d5de1a3e82b94bebb0849c80bf7c13ef2e8a3a877d9cded8ae55fe1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene" --events
```

