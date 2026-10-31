# Nitro (Youth Energy): scene presentation

Journal identity: `quests/minor_quest/mq060_nitro`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq060_nitro.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq060\scenes\mq060_android.scene`

19 graph nodes, 17 edges; 2 event-bearing sections, 23 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Player (actor 0, findInContext); Player_1 (actor 1, findInContext).

Entries: `animation_disconection` → 1; `animation_android` → 6.

Exits: `End 0` → 2; `End1` → 226.

End nodes: 2: `<omitted>`; 226: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 8 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 8 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |
| `scnIKEvent` | 4 | 8 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnPlaySkAnimEvent` | 3 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 2 | 8 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 2 | 8 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scneventsSocket` | 8 | 8 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `a01e776fc5127b5c46f9f8dd9e08826ef25ee68fc3e7f217c8ac12a4d3869321`. Binary SHA-256: `c30743323826f936bdc3d7070ab8dc73d2e4483b38680a7d6a8dd43e6b92a4ce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq060\scenes\mq060_android.scene" --events
```

## `base\quest\minor_quests\mq060\scenes\mq060_connecttoterminal.scene`

104 graph nodes, 130 edges; 9 event-bearing sections, 48 events; 9 screenplay lines, 8 screenplay options, 2 choice nodes.

Actors: android_replacer (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `disconnect` → 22; `Start 3` → 337.

Exits: `End 0` → 2; `End 3` → 336; `End 1` → 53; `End 4` → 472.

End nodes: 2: `<omitted>`; 53: `<omitted>`; 336: `<omitted>`; 472: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 389 / 473 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/1` |
| `scnChangeIdleAnimEvent` | 6 | 10 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 51 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scnIKEvent` | 4 | 51 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnPlaySkAnimEvent` | 10 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 2 | 51 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 2 | 51 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scneventsSocket` | 19 | 10 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, socket_signal: 6
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `640dd38407554ab095bf9fd88f2021d888dcf4f078a75350dbf3a95d25c11732`. Binary SHA-256: `ef6b75ecc88cf350bdf1ef70c5baf9f937e1934f5c46814fb178e82f91c67363`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq060\scenes\mq060_connecttoterminal.scene" --events
```

## `base\quest\minor_quests\mq060\scenes\mq060_identify.scene`

16 graph nodes, 15 edges; 3 event-bearing sections, 26 events; 5 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: android_01 (actor 0, community); android_02 (actor 1, community); android_03 (actor 2, community); android_04 (actor 3, community); android_05 (actor 4, community); android_06 (actor 5, community); Player (actor 6, findInContext).

Entries: `Start 0` → 1; `robot` → 33.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 38 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 38 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/15` |
| `scnIKEvent` | 2 | 38 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/12` |
| `scnLookAtEvent` | 3 | 17 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 34 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnUnmountEvent` | 1 | 38 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 1 | 38 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/10` |
| `scneventsSocket` | 8 | 38 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 1
- skeletal_animation: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `9c5bd1b42d8521423885cad339e1fdea6faea5e3a093ca2c668b2ce9cf837420`. Binary SHA-256: `f7df244ad282aaf34859679eac0bd8939d9c0677438022243b59205878f1c036`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq060\scenes\mq060_identify.scene" --events
```

## `base\quest\minor_quests\mq060\scenes\mq060_voicelines.scene`

15 graph nodes, 14 edges; 7 event-bearing sections, 7 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: androids (actor 0, community); Player (actor 1, findInContext).

Entries: `billboard` → 1; `mail` → 4; `scan` → 5; `robot_warning` → 6; `robot_calm` → 7; `robot_warning_2` → 8; `container` → 9.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 11 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7

Raw SHA-256: `89dfdb2ce69333ee0b7e1068c1c379b2273feab6deeba52a93d1ed86e6098d2f`. Binary SHA-256: `04ccab173b21a2ccda676d8934b917c7d1d916eacaec17375bd98af4d9b2ede8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq060\scenes\mq060_voicelines.scene" --events
```

