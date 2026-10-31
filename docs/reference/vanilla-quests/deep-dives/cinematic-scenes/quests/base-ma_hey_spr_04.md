# Cyberpsycho Sighting: Seaside Cafe: scene presentation

Journal identity: `quests/minor_quest/ma_hey_spr_04`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_hey_spr_04.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 4 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: regina (actor 0, spawnSet); regina_holo (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `rejected_out` → 176; `End 0` → 2.

End nodes: 2: `<omitted>`; 176: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 29 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 1 | 29 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 1

Raw SHA-256: `0ed1f70c2078b01cda44710ff3a141f3f7a7cee4f97de99004f32a5ab309fc12`. Binary SHA-256: `f83b682f2d1733975cea0703e49b4640bcf6868cd10bdc597716e43047efc4bc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene" --events
```

## `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene`

14 graph nodes, 12 edges; 4 event-bearing sections, 11 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnDespawn); onlooker01 (actor 1, community); onlooker02 (actor 2, community); onlooker03 (actor 3, community); onlooker04 (actor 4, community); onlooker05 (actor 5, community); onlooker06 (actor 6, community); onlooker07 (actor 7, community); onlooker08 (actor 8, community); cyberpsycho (actor 9, community); Player (actor 10, findInContext).

Entries: `knockback` → 45; `spawn_johnny_in` → 1; `lookats_in` → 24.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 50 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnLookAtEvent` | 9 | 20 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 1 | 46 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2
- skeletal_animation: 1
- speech: 1

Raw SHA-256: `accf2103cb015cb5bb39ce9bd80f89aa3d4be71f27eaabbaa2684f2a691a6b9b`. Binary SHA-256: `e6780b02633af2f0d29c3930d0a71537892b04d62164222864b6062b31ef51f5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene" --events
```

