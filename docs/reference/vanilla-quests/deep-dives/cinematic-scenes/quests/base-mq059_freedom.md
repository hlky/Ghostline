# Freedom: scene presentation

Journal identity: `quests/minor_quest/mq059_freedom`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq059_freedom.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq059\scenes\mq059_play_vos.scene`

89 graph nodes, 68 edges; 10 event-bearing sections, 32 events; 15 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: Johnny_voice (actor 0, findInContext); Johnny_scan (actor 1, spawnDespawn); Johnny_corpses (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `V_read_file` → 1; `Tablet` → 400; `Mordred_flee` → 418; `react_corpses` → 39; `scan_engineer` → 47; `Shard_read` → 50; `Work_station` → 52; `Laptop_react` → 54; `Street_kid_react` → 72; `Alarm_trigger` → 74.

Exits: `End4` → 95; `End6` → 98; `End7` → 101; `End8` → 104; `End 9` → 405; `End10` → 413; `End1` → 44; `End2` → 88; `End3` → 92.

End nodes: 44: `<omitted>`; 88: `<omitted>`; 92: `<omitted>`; 95: `<omitted>`; 98: `<omitted>`; 101: `<omitted>`; 104: `<omitted>`; 405: `<omitted>`; 413: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 365 / 302 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/1` |
| `scnDialogLineEvent` | 14 | 6 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 365 / 327 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/15` |
| `scnIKEvent` | 2 | 365 / 324 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/12` |
| `scnPlaySkAnimEvent` | 3 | 365 / 296 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/0` |
| `scnUnmountEvent` | 1 | 365 / 326 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 1 | 365 / 321 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/10` |
| `scneventsSocket` | 9 | 23 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `2f4b649c8bf4168358745c465129c593d92f2696178434e33f0d7808f1231d5b`. Binary SHA-256: `c2255ab2837ed64713774a58f03b8225b0b9e024195652ab75f797162cdbe3fe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq059\scenes\mq059_play_vos.scene" --events
```

