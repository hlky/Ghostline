# Career Opportunities: scene presentation

Journal identity: `quests/minor_quest/mws_wat_08_trauma_drama`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mws_wat_08_trauma_drama.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene`

85 graph nodes, 85 edges; 4 event-bearing sections, 28 events; 4 screenplay lines, 8 screenplay options, 5 choice nodes.

Actors: trauma_team_01 (actor 0, community); trauma_team_02 (actor 1, community); johnny (actor 2, spawnDespawn); player (actor 3, findInContext).

Entries: `in_trauma_team` → 1; `debug_teleport_in` → 258; `in_av_toy_interaction` → 6; `chicken_in` → 234.

Exits: `out_trauma_team` → 2; `out_av_toy_interaction` → 8; `End1` → 128; `test_toy_av_out` → 330; `chicken_out` → 246.

End nodes: 2: `NonTerminating`; 8: `<omitted>`; 128: `<omitted>`; 246: `<omitted>`; 330: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 70 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scnLookAtEvent` | 2 | 179 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/1` |
| `scnPlaySkAnimEvent` | 11 | 70 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/0` |
| `scneventsEquipItemToPerformer` | 1 | 70 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scneventsSocket` | 13 | 70 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 2
- skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `3b46379d669dc81c28cf72ac0557ef6bc2d588b71f93d5418768724d721b149f`. Binary SHA-256: `62acb4a2722e778694e0b6b64cddb9a2b11aa6d94fc49458725a03454e58f3da`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene" --events
```

