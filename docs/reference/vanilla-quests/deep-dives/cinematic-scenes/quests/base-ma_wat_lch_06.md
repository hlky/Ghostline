# Cyberpsycho Sighting: Ticket to the Major Leagues: scene presentation

Journal identity: `quests/minor_quest/ma_wat_lch_06`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_wat_lch_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_brief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `ma_wat_lch_06_brief_in` → 1.

Exits: `ma_wat_lch_06_brief_out` → 2; `rejected_out` → 399.

End nodes: 2: `<omitted>`; 399: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `bce9b8dcbc941e51f224e392b87680bc1d22ce80dcdce93e8d3cd2f90ea7e3e7`. Binary SHA-256: `f1c5ec47974cd0c5ab100e6bb96104d7ea42dc00fa5ed2fcb8ee2cb656210993`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_brief.scene" --events
```

## `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_clues_n_mood.scene`

10 graph nodes, 9 edges; 1 event-bearing sections, 11 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnDespawn).

Entries: `johnny_gate_in` → 1.

Exits: `johnny_gate_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 12 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnLookAtEvent` | 3 | 12 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 3 | 12 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsSocket` | 4 | 12 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `c47130709963402fbecda87809638c3c1dd0033abf2eca2e1b8e7e04abdd626e`. Binary SHA-256: `242179472cbbeb4bfd9f15870d8f455ae806d56f035175d46cb1bee42021919a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_clues_n_mood.scene" --events
```

