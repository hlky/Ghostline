# Motorbreath: scene presentation

Journal identity: `quests/minor_quest/mq057_motorbreath`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq057_motorbreath.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq057\scenes\mq057_afterchase.scene`

10 graph nodes, 7 edges; 1 event-bearing sections, 9 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: semimaru (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnGameplayTransitionEvent` | 1 | 23 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scnIKEvent` | 2 | 23 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnPlaySkAnimEvent` | 2 | 23 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnUnmountEvent` | 1 | 23 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 1 | 23 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scneventsSocket` | 2 | 23 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `89c2a909970a598c26c0e317421028924aff001a9785ac78f97d541f6e72d300`. Binary SHA-256: `e6c2124c90219380b02b9ef08a99649f49da95ae46b660b9f7f4e13d8c18272b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq057\scenes\mq057_afterchase.scene" --events
```

## `base\quest\minor_quests\mq057\scenes\mq057_chase.scene`

40 graph nodes, 23 edges; 2 event-bearing sections, 16 events; 3 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: mq057_Semimaru (actor 0, spawner); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 65 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |
| `scnChangeIdleAnimEvent` | 2 | 65 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 231 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/8` |
| `scnIKEvent` | 2 | 231 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/6` |
| `scnPlaySkAnimEvent` | 2 | 65 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 2 | 65 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scneventsSocket` | 5 | 65 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state: 1

Raw SHA-256: `7a9a8464560a060ccfd27f3356ad8cd40b70aca38326256b9d77ef5961cf2e57`. Binary SHA-256: `125343b9473f729e1c7c70647dbc22a6783cedf89180172d43edafc25e7b6ebe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq057\scenes\mq057_chase.scene" --events
```

## `base\quest\minor_quests\mq057\scenes\mq057_voicelines.scene`

9 graph nodes, 8 edges; 4 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: driver_01 (actor 0, community); driver_02 (actor 1, community); Player (actor 2, findInContext).

Entries: `V_react_Semimaru` → 1; `V_react_end_combat` → 6; `Driver_1_react` → 7; `Driver_2_react` → 8.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 9 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `911104582f2d501ff1434b47841468da3829db1ab2b904feade6e4c05677c7c5`. Binary SHA-256: `f0fa21de3937d3ae84aaa681c70e5bf49635975bab71f141e4e1c9f8d8572a0f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq057\scenes\mq057_voicelines.scene" --events
```

