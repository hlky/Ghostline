# Gig: Eye for an Eye: scene presentation

Journal identity: `quests/street_stories/heywood/glen/sts_hey_gle_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_gle_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene`

30 graph nodes, 40 edges; 4 event-bearing sections, 9 events; 9 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start1` → 105.

Exits: `End1` → 106; `rejected_out` → 289.

End nodes: 106: `<omitted>`; 289: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 9 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `2c7e4f9b5e7d631abfbd6fc339fb534c2a5673b718ed5692884567a31d24816c`. Binary SHA-256: `a9817575e324c61b4b3dc90cf22a3092e4790e55c32fe6061da716922fbd52fa`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 261.

End nodes: 2: `<omitted>`; 261: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e679f7e0f2b83209ae8128bafa21926a5479459c8784ba30f9aeccb12a58a2c7`. Binary SHA-256: `0554e0d1867eddc34857827a31cc604a2a3c537eb34a3d52700787555ebbaaaf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_tucker.scene`

49 graph nodes, 74 edges; 13 event-bearing sections, 80 events; 25 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: tucker (actor 0, community); V (actor 1, findInContext).

Entries: `gle_01_tucker_start` → 1; `gle_01_tucker_stealth_start` → 61; `ungrappled` → 323.

Exits: `gle_01_tucker_killed` → 91; `exit_grappled` → 344; `gle_01_tucker_end` → 28; `finito` → 325.

End nodes: 28: `NonTerminating`; 91: `<omitted>`; 325: `<omitted>`; 344: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 6 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 24 | 2 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnLookAtEvent` | 12 | 2 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 17 | 2 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsSocket` | 14 | 2 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsVFXEvent` | 2 | 24 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `25798a0eea7dc2041a044b6c53171575e6f9274ea20b2fbf5ecc19e41c751e25`. Binary SHA-256: `f73d28766150f9528852400a29001a3d8ab775654f1fc1f1b3714ad3ce85be3a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_tucker.scene" --events
```

