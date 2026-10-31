# Cyberpsycho Sighting: Demons of War: scene presentation

Journal identity: `quests/minor_quest/ma_wat_kab_02`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_wat_kab_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene`

76 graph nodes, 104 edges; 7 event-bearing sections, 21 events; 9 screenplay lines, 4 screenplay options, 4 choice nodes.

Actors: psycho (actor 0, community); ncpd (actor 1, community); droid (actor 2, community); regina (actor 3, spawnSet); car (actor 4, community); Player (actor 5, findInContext).

Entries: `ma_wat_kab_02_in` → 1; `ma_wat_kab_02_holocall_in` → 331; `ma_wat_kab_02_clue_choices_in` → 219.

Exits: `ma_wat_kab_02_out` → 2; `ma_wat_kab-02_holocall_out` → 332; `call_rejected` → 496; `ma_wat_kab_02_clue_choices_out` → 286.

End nodes: 2: `NonTerminating`; 286: `<omitted>`; 332: `<omitted>`; 496: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 10 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 3 | 335 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/0` |
| `scnLookAtAdvancedEvent` | 3 | 95 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 9 | 10 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 2 | 102 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, socket_signal: 2
- gaze, socket_signal: 1
- gaze: 1
- gaze, vfx: 1
- vfx: 1
- speech: 1

Raw SHA-256: `c442a4c5cbf184fc2aea4af5f2485549051eefc2d0fea9511cba5ba9a0bbc6e5`. Binary SHA-256: `98ff323744f6d8c9c23104371de65fe252f9bde3b88fa08d56fee642fa4005a1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene" --events
```

