# Gig: Last Login: scene presentation

Journal identity: `quests/street_stories/watson/kabuki/sts_wat_kab_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_kab_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\scenes\sts_wat_kab_05_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start1` → 57.

Exits: `rejected_out` → 285; `End1` → 58.

End nodes: 58: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `27ec88e96ca00fb80b3710117c8d8e4918070de41dc2bc6c0f6e181553a4a81f`. Binary SHA-256: `bd7274c089cfd3b8fac88755359dc67e612ee979032fcf965660f87d29c71fdc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\scenes\sts_wat_kab_05_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\scenes\sts_wat_kab_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start1` → 56.

Exits: `End1` → 57; `rejected_out` → 260.

End nodes: 57: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e013a5f270a54a5c00f3cd8bdba661716363ed9a3aa889f4962db9e6e958ef56`. Binary SHA-256: `ded4ff26eb0589209b447ce92e50020305affe880381f4596f76f352f01a8546`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\scenes\sts_wat_kab_05_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\scenes\sts_wat_kab_05_johnny.scene`

13 graph nodes, 12 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: johnny (actor 0, spawnDespawn).

Entries: `victim` → 27.

Exits: `victim_end` → 28.

End nodes: 28: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 29 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `8f0a1f888ae6c76407eecb4670acd5d42287b9a0a43488fb313a3505c76b6fc1`. Binary SHA-256: `ab6c940820ca20090a6cf11ca6cff91c36f37ed21f5f9416a9337fca9c8c260e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\scenes\sts_wat_kab_05_johnny.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\scenes\sts_wat_kab_05_ripperdoc.scene`

45 graph nodes, 47 edges; 7 event-bearing sections, 104 events; 25 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: ripperdoc (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `surprised` → 103; `exposed` → 172.

Exits: `escape` → 130; `spared` → 168; `bribed` → 170; `Killed` → 180.

End nodes: 130: `<omitted>`; 168: `<omitted>`; 170: `NonTerminating`; 180: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 104 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 24 | 104 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 121 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/20` |
| `scnIKEvent` | 2 | 121 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/13` |
| `scnLookAtEvent` | 13 | 104 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 32 | 104 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnUnmountEvent` | 1 | 121 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/19` |
| `scneventsSetAnimFeatureEvent` | 1 | 121 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/16` |
| `scneventsSocket` | 19 | 104 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `e043afef9ed7be6a1a30d80bee9b06065ccb6082152c96bdc550b06c433773d2`. Binary SHA-256: `ff27a4989de14011667b405c60a13c9a45b5c9e2912baa2660102551941907a1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\scenes\sts_wat_kab_05_ripperdoc.scene" --events
```

