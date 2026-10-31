# Gig: Dirty Biz: scene presentation

Journal identity: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_nid_04.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gottfrid_fredrik.scene`

140 graph nodes, 189 edges; 30 event-bearing sections, 183 events; 87 screenplay lines, 9 screenplay options, 5 choice nodes.

Actors: Frederik (actor 0, community); Gottfrid (actor 1, community); Johnny (actor 2, spawnSet); Reggie (actor 3, findInContext); V (actor 4, findInContext).

Entries: `Start 9` → 765; `Sleep_start` → 32; `Woke_start` → 503.

Exits: `Woke_end` → 504; `Both_dead` → 34; `Sleep_end` → 501.

End nodes: 34: `<omitted>`; 501: `NonTerminating`; 504: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 579 / 480 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/1` |
| `scnDialogLineEvent` | 74 | 28 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 44 | 28 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnPlaySkAnimEvent` | 26 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/8` |
| `scneventsSocket` | 31 | 28 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/7` |
| `scneventsVFXEvent` | 6 | 149 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze: 3
- speech, gaze: 2
- speech, skeletal_animation: 1
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- vfx: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `01bf094b20713d8257a1ac505fb2d193821523e90943c988fde2ed6458795bdb`. Binary SHA-256: `d5df68feb771759849e686440991ea4db9fdfde1a37c08635d2a112f8eda4e65`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gottfrid_fredrik.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_debriefs.scene`

27 graph nodes, 36 edges; 2 event-bearing sections, 5 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `Start1` → 249.

Exits: `End 0` → 2; `rejected_out` → 296.

End nodes: 2: `<omitted>`; 296: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `ca3fb665e6381db51664295267f71d4030fab982faaaa6b77c96d06cd828345d`. Binary SHA-256: `4662c503f2fa5b05b5682c50c91398943b63bf1b63292eb5ba564f337cdc379d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `ade0081f62e8030a378d271e8412ef618e90598f7058096d2fef52ee0576af4b`. Binary SHA-256: `c6288d488f29c54c674d9ea9f48394c9daea60002e8881fa78d55cb29a15c7d4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_prebrief.scene" --events
```

