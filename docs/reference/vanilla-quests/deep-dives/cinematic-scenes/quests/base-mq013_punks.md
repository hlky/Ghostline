# A Day In The Life: scene presentation

Journal identity: `quests/minor_quest/mq013_punks`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq013_punks.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene`

304 graph nodes, 386 edges; 51 event-bearing sections, 395 events; 112 screenplay lines, 17 screenplay options, 7 choice nodes.

Actors: shopkeep (actor 0, spawnSet); punk_01 (actor 1, community); punk_02 (actor 2, community); customer (actor 3, community); bike (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `mq013_00_in` → 1; `mq013_00_punk_off_bike` → 935; `stop_lookats` → 2120; `combat_shop` → 2188; `Start 3` → 756; `chicken_in` → 484; `mq013_00_combat_in` → 1386; `Start 9` → 1996; `Start 7` → 1147.

Exits: `mq013_00_shopkeep_alive_out` → 2; `mq013_00_shopkeep_dead_out` → 7; `combat` → 1273; `End 8` → 1876; `goto_combat_shop` → 2186; `chicken_out` → 485; `mq013_00_to_combat_scene_out` → 1387.

End nodes: 2: `<omitted>`; 7: `NonTerminating`; 485: `<omitted>`; 1273: `NonTerminating`; 1387: `<omitted>`; 1876: `<omitted>`; 2186: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 206 / 389 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/2` |
| `scnDialogLineEvent` | 87 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 19 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/18` |
| `scnIKEvent` | 16 | 19 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/8` |
| `scnLookAtEvent` | 74 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 137 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 4 | 19 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/17` |
| `scneventsSetAnimFeatureEvent` | 4 | 19 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/14` |
| `scneventsSocket` | 62 | 4 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 11
- speech, skeletal_animation, socket_signal: 7
- skeletal_animation, socket_signal: 7
- speech, skeletal_animation: 4
- ik: 4
- speech, skeletal_animation, gaze: 3
- gaze: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, audio: 1
- speech, gaze: 1
- skeletal_animation: 1

Raw SHA-256: `390a3d3a958b9c756529b45cdaf7f7576f7e137a93448a7bd1e29731ad0bc733`. Binary SHA-256: `51b5204cf85b416c59c372fd4309e8a924092e5fa1fed412e82a19584bf83df1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene" --events
```

