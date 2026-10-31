# Off the Leash: scene presentation

Journal identity: `quests/side_quest/sq017_02_lounge`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq017_02_lounge.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq017\scenes\sq017_16_phone_call_3.scene`

19 graph nodes, 19 edges; 2 event-bearing sections, 32 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: kerry (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 265.

End nodes: 2: `<omitted>`; 265: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 15 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 10 | 3 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 2

Raw SHA-256: `6a61f8983188cdc22b0964838040c3c0ab5063892160c08242dbe8be9af2b9dd`. Binary SHA-256: `d463e268ac268a1ef04198b6748c735d8f56d6b0f0226f388aea1cf3e0328de3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_16_phone_call_3.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_17_pachinko.scene`

26 graph nodes, 26 edges; 3 event-bearing sections, 23 events; 4 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: doorman (actor 0, community); v (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 4 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 6 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 9 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 1

Raw SHA-256: `6e5080aaa9a0937aa6deb505282095e11e1d1a715fa2b2def49625a901ec347f`. Binary SHA-256: `42f9a337b1edaf3c91b8504d818a0acfadb9e15dd459775a771e9c67abb5699d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_17_pachinko.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_18_premiere.scene`

496 graph nodes, 644 edges; 115 event-bearing sections, 1036 events; 221 screenplay lines, 36 screenplay options, 17 choice nodes.

Actors: kerry (actor 0, spawnSet); purple_force (actor 1, community); blue_moon (actor 2, community); red_menace (actor 3, community); media1 (actor 4, community); media2 (actor 5, community); spector_vendor (actor 6, spawnSet); vip1 (actor 7, community); vip2 (actor 8, community); photo1 (actor 9, community); photo2 (actor 10, community); photo3 (actor 11, community); johnny (actor 12, spawnDespawn); mrsblocker (actor 13, community); mrblocker (actor 14, community); v (actor 15, findInContext).

Entries: `Start 0` → 1; `Elevator` → 1782; `Start 8` → 7115; `Start1` → 3997; `in_rooftop` → 199; `no_us_cracks_in` → 265; `Speech` → 3788; `kiss` → 2406.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 38 | 19 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 171 | 19 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnGameplayTransitionEvent` | 10 | 19 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/42` |
| `scnIKEvent` | 20 | 19 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/28` |
| `scnLookAtEvent` | 353 | 19 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnPlaySkAnimEvent` | 171 | 19 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scnPoseCorrectionEvent` | 2 | 298 / 848 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/6` |
| `scnUnmountEvent` | 10 | 19 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/41` |
| `scneventsCameraParamsEvent` | 12 | 103 / 536 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/30` |
| `scneventsEquipItemToPerformer` | 25 | 19 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 10 | 19 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/38` |
| `scneventsSocket` | 209 | 19 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scneventsVFXEvent` | 5 | 212 / 712 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 21
- gaze: 19
- skeletal_animation, gaze: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, gaze: 6
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, gaze: 4
- speech: 4
- camera: 4
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation: 3
- speech, gaze, socket_signal: 3
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- idle_animation, gaze: 1
- socket_signal, animation_state: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze, props_equipment, socket_signal: 1
- socket_signal: 1
- skeletal_animation: 1
- vfx: 1

Raw SHA-256: `6ff58157add0c453d8ee9f3b3b41d792fe21ebfa0a5fb7835c710227bf9999cc`. Binary SHA-256: `6d8ff01c80f80ba6fa9a4d210a8b88a8458df9ae0a94360cbe68e59fcf0a1caa`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_18_premiere.scene" --events
```

