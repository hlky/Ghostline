# The Gun: scene presentation

Journal identity: `quests/side_quest/sq_q001_wilson`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq_q001_wilson.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene`

107 graph nodes, 120 edges; 14 event-bearing sections, 42 events; 22 screenplay lines, 9 screenplay options, 5 choice nodes.

Actors: wilson (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `wilson_default_in` → 0; `backup_lines` → 568.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 44 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 22 | 44 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 8 | 44 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 6 | 44 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 5 | 44 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, gaze: 4
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1

Raw SHA-256: `230b4f7f142e3145266591392f5b305e6d0738c1736f652a886102504730a945`. Binary SHA-256: `a8cbd1b193cb051f42c300b28fd2cb6034daded9ba5a769a31563040c2abcd43`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene" --events
```

