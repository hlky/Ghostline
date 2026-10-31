# Killing In The Name: scene presentation

Journal identity: `quests/minor_quest/mq018_writer`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq018_writer.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq018\scenes\mq018_01_call.scene`

31 graph nodes, 32 edges; 7 event-bearing sections, 26 events; 26 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Nancy (actor 0, spawnSet); Bes_Isis (actor 1, findInContext); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `blocked_in` → 134.

Exits: `End 0` → 2; `teleport_out` → 96; `blocked_out` → 40.

End nodes: 2: `<omitted>`; 40: `<omitted>`; 96: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 26 | 17 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7

Raw SHA-256: `05baf5f5908f682480c5bec39aa405385b8f6684635b864356619a334b58df2a`. Binary SHA-256: `a2bddd8300283489b2d0e7788d19ea7a75c835083bd554d3a2df1301d4d07ce3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq018\scenes\mq018_01_call.scene" --events
```

## `base\quest\minor_quests\mq018\scenes\mq018_02_fortuneteller.scene`

234 graph nodes, 262 edges; 22 event-bearing sections, 116 events; 50 screenplay lines, 9 screenplay options, 6 choice nodes.

Actors: Fortuneteller (actor 0, community); Johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `setup_in` → 162.

Exits: `End 0` → 2; `persistent_exit` → 527.

End nodes: 2: `NonTerminating`; 527: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 39 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |
| `scnDialogLineEvent` | 45 | 13 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 18 | 39 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlaySkAnimEvent` | 30 | 39 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scneventsSocket` | 17 | 39 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `3ca9141b16a4cc032f9188dd2dca4543753cfb9e55288c82571d87daa8aa3671`. Binary SHA-256: `34e2a97e11d2bb0f2d9a64d633c2d5b2ba6ca1a7e102a040fe0c6cbb058d1c32`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq018\scenes\mq018_02_fortuneteller.scene" --events
```

## `base\quest\minor_quests\mq018\scenes\mq018_03_call02.scene`

39 graph nodes, 45 edges; 5 event-bearing sections, 16 events; 13 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Nancy (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `chicken_in` → 90.

Exits: `exit` → 88.

End nodes: 88: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 22 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 13 | 20 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 1 | 20 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, socket_signal: 1
- speech, idle_animation: 1

Raw SHA-256: `24e73937b59da7ad334e957b45dba9ea8d4f5b50136ae2a1ebc8bffb0f5aa0ad`. Binary SHA-256: `5ae72bc3e9a13049888cb893c4ed207d3c170d438d215781e297bfececae3223`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq018\scenes\mq018_03_call02.scene" --events
```

## `base\quest\minor_quests\mq018\scenes\mq018_05_brooklyn.scene`

87 graph nodes, 119 edges; 9 event-bearing sections, 37 events; 21 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Nancy (actor 1, findInContext); Player (actor 2, findInContext).

Entries: `Start 0` → 4; `Start 2` → 274.

Exits: `continue` → 5; `interrupt` → 144; `exit` → 169.

End nodes: 5: `NonTerminating`; 144: `<omitted>`; 169: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 20 | 18 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnLookAtEvent` | 3 | 19 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnPlaySkAnimEvent` | 7 | 18 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scneventsSocket` | 7 | 18 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 2
- speech: 2
- speech, skeletal_animation, gaze: 1

Raw SHA-256: `b30937104a67ba596804cd453708307527afdb4d55052509b42c4359156791ad`. Binary SHA-256: `c21a66dc75879e2d19cdd4d7321da4ee09f6b7697b23e28d74a63ab60ccc59eb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq018\scenes\mq018_05_brooklyn.scene" --events
```

## `base\quest\minor_quests\mq018\scenes\mq018_06_solar.scene`

77 graph nodes, 103 edges; 8 event-bearing sections, 35 events; 16 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 4.

Exits: `continue` → 5; `exit` → 161; `interrupt` → 179.

End nodes: 5: `NonTerminating`; 161: `<omitted>`; 179: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 14 | 24 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnLookAtEvent` | 7 | 24 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scnPlaySkAnimEvent` | 9 | 24 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scneventsSocket` | 5 | 25 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `e9df536e7cc4fddc5ffeb15893ead931175cd25f6a549ee89951716c6ecfad44`. Binary SHA-256: `f5daec2aa74c274160ab72def974728fcc0afa392b0f6cd6000e95d62da71f58`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq018\scenes\mq018_06_solar.scene" --events
```

## `base\quest\minor_quests\mq018\scenes\mq018_07_protein.scene`

91 graph nodes, 128 edges; 7 event-bearing sections, 28 events; 15 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 4.

Exits: `continue` → 5; `interrupt` → 197.

End nodes: 5: `NonTerminating`; 197: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 15 | 24 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scnLookAtEvent` | 5 | 24 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnPlaySkAnimEvent` | 6 | 24 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/4` |
| `scneventsSocket` | 2 | 24 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 3
- speech: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1

Raw SHA-256: `5a42e08b2f24b503969fa6f336f11e29f29de40941641ebd350dcbe5f702c0e2`. Binary SHA-256: `e7c74e98ae129feaeaece52efd0ce392fa8c37ab2e05111f1e8c5864dcaad751`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq018\scenes\mq018_07_protein.scene" --events
```

