# Every Breath You Take: scene presentation

Journal identity: `quests/minor_quest/mq028_stalker`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq028_stalker.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq028\scenes\mq028_01_holocall.scene`

64 graph nodes, 68 edges; 9 event-bearing sections, 43 events; 31 screenplay lines, 6 screenplay options, 2 choice nodes.

Actors: Blue_Moon (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `skip_call` → 400; `refused_in` → 48.

Exits: `continue` → 2; `prefetch_out` → 3995; `exit` → 156; `refused` → 35.

End nodes: 2: `NonTerminating`; 35: `<omitted>`; 156: `<omitted>`; 3995: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 5 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 29 | 5 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 306 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/3` |
| `scnIKEvent` | 2 | 306 / 186 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/1` |
| `scnPlaySkAnimEvent` | 2 | 298 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/0` |
| `scnUnmountEvent` | 1 | 306 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 1 | 306 / 189 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/4` |
| `scneventsSocket` | 5 | 298 / 170 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, idle_animation: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `8778ef866f345b0815457ee836d8164e911156e6a45241b03dc19175ec737427`. Binary SHA-256: `14ee2712af744b03551416abf18353ae115fdbd4026fddb1579bdde7bd68ca4e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq028\scenes\mq028_01_holocall.scene" --events
```

## `base\quest\minor_quests\mq028\scenes\mq028_02_park.scene`

555 graph nodes, 627 edges; 95 event-bearing sections, 458 events; 149 screenplay lines, 21 screenplay options, 10 choice nodes.

Actors: Blue_Moon (actor 0, community); Kid (actor 1, community); Ganger01 (actor 2, community); Ganger02 (actor 3, community); Stalker (actor 4, community); Jogger (actor 5, community); Weird (actor 6, community); Ganger03 (actor 7, community); Ganger04 (actor 8, community); Ganger05 (actor 9, community); Old01 (actor 10, community); Old02 (actor 11, community); Blue_Moon_voice (actor 12, findInContext); Red_menace (actor 13, community); Player (actor 14, findInContext).

Entries: `main_in` → 1; `Start 8` → 4452; `scene_preview` → 4072; `kill_in` → 363; `exposed_in` → 2044.

Exits: `continue_out` → 2; `exposed_out` → 2043; `aborted_out` → 1041.

End nodes: 2: `<omitted>`; 1041: `<omitted>`; 2043: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 38 | 85 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |
| `scnDialogLineEvent` | 92 | 85 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnGameplayTransitionEvent` | 18 | 85 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/20` |
| `scnIKEvent` | 36 | 85 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/14` |
| `scnLookAtEvent` | 44 | 118 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |
| `scnPlaySkAnimEvent` | 85 | 85 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnUnmountEvent` | 18 | 85 / 170 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/19` |
| `scneventsAttachPropToNode` | 1 | 118 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/27` |
| `scneventsAttachPropToPerformer` | 1 | 118 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 18 | 85 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/16` |
| `scneventsSocket` | 106 | 85 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/17` |
| `scneventsUnequipItemFromPerformer` | 1 | 286 / 424 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 28
- skeletal_animation, socket_signal: 15
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 9
- speech, idle_animation: 5
- socket_signal: 4
- speech, skeletal_animation: 3
- speech, gaze, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, gaze: 2
- skeletal_animation, gaze, socket_signal: 2
- idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `098945eeefddefc53173cf92b708763b73bb268323985db1cd7259f05a526ced`. Binary SHA-256: `39eef1db6bdcb81edbca3a6ee954e550f64147f0dedfa70b2d5fa6f17c322b7e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq028\scenes\mq028_02_park.scene" --events
```

## `base\quest\minor_quests\mq028\scenes\mq028_03_resolution.scene`

172 graph nodes, 225 edges; 22 event-bearing sections, 100 events; 37 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Blue_Moon (actor 0, community); Stalker (actor 1, community); Agent_Orange (actor 2, community); Red_Menace (actor 3, community); Kid (actor 4, community); Blue_Moon_Voice (actor 5, findInContext); Ganger01 (actor 6, community); Ganger02 (actor 7, community); Ganger03 (actor 8, community); Player (actor 9, findInContext).

Entries: `main_in` → 1.

Exits: `continue_out` → 2; `exit_out` → 481.

End nodes: 2: `NonTerminating`; 481: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 51 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnDialogLineEvent` | 31 | 51 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnLookAtEvent` | 18 | 51 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnPlaySkAnimEvent` | 29 | 51 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scneventsSocket` | 16 | 51 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech: 5
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `d0cf7d6e633fe7bf2dd0e5762eaaec0f7d9e83fadd01f8260ae8672f0c5c63cd`. Binary SHA-256: `d14373cf1fca388f3958d6f3457164c9907ee6fe92f1f19488cb2974e8eafa00`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq028\scenes\mq028_03_resolution.scene" --events
```

## `base\quest\minor_quests\mq028\scenes\mq028_04_idle.scene`

55 graph nodes, 61 edges; 12 event-bearing sections, 25 events; 13 screenplay lines, 6 screenplay options, 6 choice nodes.

Actors: Blue_moon (actor 0, community); Kid (actor 1, community); Stalker (actor 2, community); Jogger (actor 3, community); Weird (actor 4, community); Red_menace (actor 5, community); Player (actor 6, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 108 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnDialogLineEvent` | 9 | 23 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnLookAtEvent` | 8 | 65 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 264 / 211 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/0` |
| `scneventsSocket` | 3 | 211 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, gaze: 2
- speech, idle_animation, gaze: 1
- socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- idle_animation, gaze: 1

Raw SHA-256: `064d0c7856c928e4bada65fc708d69469510501e8c053ee8e7d5b8a97b37b34a`. Binary SHA-256: `77a7aa5fe7d933bc5717714f2a4d7f277eb30a12bdeaa8de44935037c279ef6f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq028\scenes\mq028_04_idle.scene" --events
```

