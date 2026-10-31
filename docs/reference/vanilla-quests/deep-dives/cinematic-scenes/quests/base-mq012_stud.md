# Burning Desire: scene presentation

Journal identity: `quests/minor_quest/mq012_stud`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq012_stud.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene`

293 graph nodes, 400 edges; 42 event-bearing sections, 192 events; 92 screenplay lines, 12 screenplay options, 4 choice nodes.

Actors: stud (actor 0, spawner); stud_phone (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `mq012_00_stud_appear_in` → 1; `mq012_00_car_in` → 63; `mq012_00_walking_to_ripper_in` → 1086; `mq012_stud_pose` → 805; `mq012_00_too_long_in` → 175; `mq012_00_at_ripperdoc_in` → 209; `mq012_00_holocall_in` → 217; `chicken_in` → 241.

Exits: `mq012_00_stud_appear_out` → 2; `mq012_00_quest_end_out` → 118; `start_timer` → 773; `mq012_00_too_long_out` → 176; `mq012_00_at_ripperdoc_out` → 210; `mq012_00_holocall_out` → 218; `mq012_00_too_far_out` → 1196; `End 8` → 561; `talk_out` → 242; `holocall_out` → 243.

End nodes: 2: `NonTerminating`; 118: `NonTerminating`; 176: `<omitted>`; 210: `<omitted>`; 218: `<omitted>`; 242: `<omitted>`; 243: `<omitted>`; 561: `<omitted>`; 773: `NonTerminating`; 1196: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 22 | 49 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnChangeIdleAnimEvent` | 4 | 51 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 78 | 49 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnLookAtEvent` | 38 | 51 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 39 | 51 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsSocket` | 4 | 205 / 327 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/3` |
| `scneventsVFXEvent` | 7 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 9
- speech, skeletal_animation, gaze, audio: 7
- speech, audio: 5
- speech, gaze, audio: 4
- speech: 3
- speech, skeletal_animation, gaze: 2
- speech, gaze: 2
- idle_animation, vfx: 2
- vfx: 1
- speech, skeletal_animation, idle_animation, gaze, audio: 1
- speech, gaze, audio, socket_signal: 1
- speech, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze: 1
- gaze: 1

Raw SHA-256: `14f9f8d190769d37143abfdf9f6b7cb8c9077e306ea8a9c14144e3912dd853a6`. Binary SHA-256: `b357e2e0b05566200d338748ec1e943ac81bac937de4f968e6150dbd1c6c1e04`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene" --events
```

