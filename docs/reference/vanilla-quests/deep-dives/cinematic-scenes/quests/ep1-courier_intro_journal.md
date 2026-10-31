# Push It to the Limit: scene presentation

Journal identity: `ep1/quests/sandbox_activities/courier_intro_journal`. Stored type: **CourierSideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-courier_intro_journal.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\sandbox_activities\courier_spot\introduction_quest\scene\sa_ep1_introduction_scene_muamar.scene`

244 graph nodes, 290 edges; 49 event-bearing sections, 391 events; 74 screenplay lines, 14 screenplay options, 7 choice nodes.

Actors: Muamar (actor 0, spawnSet); Daniels (actor 1, community); driver (actor 2, community); buyer_car (actor 3, community); garage_car (actor 4, community); nice_car (actor 5, community); Player (actor 6, findInContext).

Entries: `Start 0` → 1; `cine_debug` → 1382.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 26 | 12 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/27` |
| `scnChangeIdleAnimEvent` | 21 | 12 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnDialogLineEvent` | 49 | 12 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 5 | 480 / 375 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/10` |
| `scnIKEvent` | 10 | 480 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/1` |
| `scnLookAtEvent` | 73 | 12 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 108 | 12 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 5 | 480 / 374 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/9` |
| `scneventsAttachPropToPerformer` | 4 | 470 / 347 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/4` |
| `scneventsAttachPropToWorld` | 2 | 12 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsCameraParamsEvent` | 3 | 429 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/5` |
| `scneventsEquipItemToPerformer` | 1 | 1434 / 1170 | `/Data/RootChunk/sceneGraph/Data/graph/110/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 13 | 12 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/20` |
| `scneventsSocket` | 64 | 12 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXDurationEvent` | 1 | 947 / 682 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/17` |
| `scneventsVFXEvent` | 6 | 12 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 5
- skeletal_animation: 5
- speech, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal, animation_state: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, gaze, socket_signal: 2
- skeletal_animation, audio, socket_signal, animation_state: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1
- socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- vfx, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `efb0b035e089502160cf7c3c6043e6beba8f5599784f4bdff1e3358e9f933165`. Binary SHA-256: `2ad515b54782e97eac63e722063df82ce235bde8c2603985af3503524fa360c4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\sandbox_activities\courier_spot\introduction_quest\scene\sa_ep1_introduction_scene_muamar.scene" --events
```

## `ep1\openworld\sandbox_activities\courier_spot\scenes\courier_sandbox_holocall_prebrief.scene`

57 graph nodes, 62 edges; 6 event-bearing sections, 12 events; 12 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 152.

Exits: `intro_success` → 400; `intro_failed` → 381; `audio_call` → 211.

End nodes: 211: `NonTerminating`; 381: `<omitted>`; 400: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 12 | 163 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6

Raw SHA-256: `25b54bfb796ecf8493a464dfcaee51104b6c0f39c888dfe36707114089528153`. Binary SHA-256: `3cab70bcf96e01c279947caa395268adabfef37f384910f8c2948b8e9eec1eb1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\sandbox_activities\courier_spot\scenes\courier_sandbox_holocall_prebrief.scene" --events
```

## `ep1\openworld\sandbox_activities\courier_spot\scenes_loop\sa_ep1_courier_loop_all_holocalls.scene`

472 graph nodes, 696 edges; 52 event-bearing sections, 68 events; 68 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer_voice (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Mission_starting` → 1.

Exits: `holo_closed` → 1997; `courier_succes` → 246; `courier_failed` → 371.

End nodes: 246: `<omitted>`; 371: `<omitted>`; 1997: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 68 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 52

Raw SHA-256: `5d02a1dfc933d9aa32ed0cb1b27bbe1436b6d93cb41e8dcf160900d5c77f0ec7`. Binary SHA-256: `2f41eaeabd0842c2b584224e4528667ddb09947515dcb5a9c0a711e709da09a7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\sandbox_activities\courier_spot\scenes_loop\sa_ep1_courier_loop_all_holocalls.scene" --events
```

