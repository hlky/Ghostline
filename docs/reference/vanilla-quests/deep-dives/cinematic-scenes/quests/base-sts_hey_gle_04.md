# Gig: Fifth Column: scene presentation

Journal identity: `quests/street_stories/heywood/glen/sts_hey_gle_04`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_gle_04.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: padre (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 283.

End nodes: 2: `<omitted>`; 283: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 29 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `fc65c77a33bcba921c77873c23e135d64ff04549abec19610a3e838385534fc6`. Binary SHA-256: `7c45ab260fa2ed7d7978780c393b3a6a18a5715a066c609ebc96e799f1ed58b5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: padre (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 254.

End nodes: 2: `<omitted>`; 254: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 30 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `4283b5973539e9f73fceadb11b2bcf378e96279683a81d5ac83307f4152db680`. Binary SHA-256: `eb4cc35ffd4dfa4359dac9c40660ea10c60331842f4783fe04e39e9bf1e8462e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_johnny.scene`

8 graph nodes, 7 edges; 1 event-bearing sections, 10 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 2 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 3 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 2 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `047bcf3bc3807fbe324f3183697aef0c6da809337445cc3456bd4840519956b5`. Binary SHA-256: `07a2435837294b12fb49ab1ed578c9fe287acefb1854f49acd8b6ff54a3e6c52`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_johnny.scene" --events
```

