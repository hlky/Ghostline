# Unfinished Sympathy: scene presentation

Journal identity: `ep1/quests/main_quest/q306_somi_epilogue`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q306_somi_epilogue.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene`

22 graph nodes, 24 edges; 7 event-bearing sections, 26 events; 12 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: Alex (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 14 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 12 | 14 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnLookAtEvent` | 3 | 14 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 33 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsSocket` | 5 | 14 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze: 1

Raw SHA-256: `db202c3c4187a5164ed5867c6334a7bb0ef89ed142b717e6002d038ddc0e8e32`. Binary SHA-256: `d5a73d3395630d22f4630396b30f7d31c24f4bc3618b7a2915deb3d829f9c6cb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene`

83 graph nodes, 95 edges; 19 event-bearing sections, 172 events; 40 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `q306_somi_wrap_in` → 1; `q306_reed_wrap_in` → 93.

Exits: `q306_somi_wrap_out` → 2; `End1` → 453; `End2` → 469; `q306_reed_wrap_out` → 95.

End nodes: 2: `NonTerminating`; 95: `NonTerminating`; 453: `<omitted>`; 469: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 204 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/3` |
| `scnChangeIdleAnimEvent` | 9 | 86 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnDialogLineEvent` | 34 | 56 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 204 / 299 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/7` |
| `scnIKEvent` | 8 | 204 / 292 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/1` |
| `scnLookAtEvent` | 5 | 60 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scnOverridePhantomParamsEvent` | 1 | 60 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnPlaySkAnimEvent` | 51 | 56 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 4 | 204 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/6` |
| `scneventsAttachPropToPerformer` | 2 | 118 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 118 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 4 | 204 / 296 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/5` |
| `scneventsSocket` | 46 | 56 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 4
- speech, skeletal_animation, socket_signal: 2
- speech: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1

Raw SHA-256: `ccb4212e1b844c02c7ded886ac2fd7035c3fa355600a6ef970c2f85cf6400057`. Binary SHA-256: `55db353f47160dfd7ca3646b4dfa046dafb1066bb0d548e82df600fdb4c1f49e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_12b_holo_reed_call.scene`

22 graph nodes, 24 edges; 6 event-bearing sections, 27 events; 11 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: Reed (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 112 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnDialogLineEvent` | 11 | 112 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnLookAtEvent` | 5 | 112 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 114 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scneventsSocket` | 2 | 112 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech: 1

Raw SHA-256: `73aec221016497aa486a08c9a1161f1bedf99ecf95f7374d5ac08266ec639044`. Binary SHA-256: `2eaeffe40ff661e36eb5cb94c8a8b4089c266d0aff798dc5448c631be45ba435`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_12b_holo_reed_call.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene`

207 graph nodes, 250 edges; 68 event-bearing sections, 634 events; 138 screenplay lines, 41 screenplay options, 14 choice nodes.

Actors: Alex (actor 0, spawnSet); TV_PERSON (actor 1, findInContext); Johnny (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `Start0` → 10; `intro_wait` → 1699; `tv_start` → 1663.

Exits: `End 0` → 2; `intro_wait_out` → 1725; `tv_cut` → 1660.

End nodes: 2: `<omitted>`; 1660: `NonTerminating`; 1725: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 1818 / 1703 | `/Data/RootChunk/sceneGraph/Data/graph/189/Data/events/1` |
| `scnChangeIdleAnimEvent` | 15 | 340 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnDialogLineEvent` | 122 | 13 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 423 / 505 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/6` |
| `scnIKEvent` | 6 | 423 / 499 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |
| `scnLookAtAdvancedEvent` | 13 | 403 / 424 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/26` |
| `scnLookAtEvent` | 164 | 13 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 112 | 13 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 5 | 610 / 713 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/7` |
| `scnUnmountEvent` | 3 | 423 / 504 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/5` |
| `scneventsAttachPropToPerformer` | 33 | 361 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |
| `scneventsAttachPropToWorld` | 31 | 361 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/9` |
| `scneventsCameraParamsEvent` | 2 | 1824 / 1716 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 3 | 423 / 502 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/4` |
| `scneventsSocket` | 106 | 13 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXDurationEvent` | 10 | 361 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/14` |
| `scneventsVFXEvent` | 4 | 828 / 1112 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, skeletal_animation, gaze, socket_signal: 9
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 9
- speech, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, camera, audio, vfx: 1
- vfx: 1
- camera: 1

Raw SHA-256: `3dc8df6614734e32a19eea33ecbcf918f0eeb5d155b976ec53a73bbf0e5cab6e`. Binary SHA-256: `cebbb1f5d9eeacc4ab7b0e0098284abfc1695483d27dd75655e2c6a0780916d1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene`

148 graph nodes, 209 edges; 47 event-bearing sections, 312 events; 88 screenplay lines, 23 screenplay options, 8 choice nodes.

Actors: Reed (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Reed_Car (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `Start 0` → 1; `intro_wait` → 1566.

Exits: `End 0` → 2; `intro_wait_out` → 1568; `End2` → 1239; `reed_leave_out` → 994.

End nodes: 2: `NonTerminating`; 994: `NonTerminating`; 1239: `<omitted>`; 1568: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1578 / 1048 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/3` |
| `scnChangeIdleAnimEvent` | 22 | 382 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scnDialogLineEvent` | 71 | 19 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnGameplayActionEvent` | 2 | 1276 / 697 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/0` |
| `scnLookAtAdvancedEvent` | 6 | 382 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/11` |
| `scnLookAtEvent` | 70 | 19 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 77 | 19 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsCameraParamsEvent` | 2 | 1578 / 1047 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 1 | 1276 / 720 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/12` |
| `scneventsSocket` | 58 | 382 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/16` |
| `scneventsVFXEvent` | 2 | 1578 / 1042 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation, socket_signal: 4
- gaze: 3
- skeletal_animation: 3
- speech, skeletal_animation, gaze: 2
- speech, gaze: 2
- speech, idle_animation, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- idle_animation, gameplay_action: 1
- skeletal_animation, camera, audio, vfx: 1
- camera: 1
- vfx: 1

Raw SHA-256: `22c182dd9d42d0baf626e75b2be0cdfae9577fca5a10c7a8ede7840460c0eadd`. Binary SHA-256: `a1b52e0acb354776196d3a6f1a46193eeeccadab938849182216eb5bfd0172ae`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_post_spaceport.scene`

58 graph nodes, 58 edges; 3 event-bearing sections, 11 events; 3 screenplay lines, 6 screenplay options, 2 choice nodes.

Actors: pilot (actor 0, community); v (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 12 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 1 | 247 / 389 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/0` |
| `scnLookAtEvent` | 2 | 81 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scnPlaySkAnimEvent` | 6 | 12 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 1 | 12 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze: 1
- speech: 1

Raw SHA-256: `9a5490a8cbd030386f12b3dba5152949f3c508f0ef858d7a79e9c02fb9d14159`. Binary SHA-256: `5c60cf07043d9d375ac1bf5b212cacd5205730e5136cfae35006bee1c7b4f0a7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_post_spaceport.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_postcard_alex.scene`

23 graph nodes, 23 edges; 0 event-bearing sections, 0 events; 0 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: .

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `End1` → 52.

End nodes: 2: `NonTerminating`; 52: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |

Presentation families coexisting in an event section (counts are sections, not durations):


Raw SHA-256: `1f4e8e5fa38fa0c6893d4dd70d48eeebaab431e50bb92d103796fd0a99e9a900`. Binary SHA-256: `137ea99fb3894ef2c965f15e9549ab26b62533370dd0a801bafd7ebab702bf27`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_postcard_alex.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene`

32 graph nodes, 32 edges; 2 event-bearing sections, 15 events; 5 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Songbird (actor 0, findInContext); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 101 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnDialogLineEvent` | 3 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 101 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scnIKEvent` | 2 | 101 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scnPlaySkAnimEvent` | 1 | 101 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 1 | 101 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsEquipItemToPerformer` | 1 | 101 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 1 | 101 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSocket` | 3 | 101 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsVFXEvent` | 1 | 101 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- skeletal_animation, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `dce446754f2d1ad495264db7da706bbf34c17b4930b783a21aa112e92ec45010`. Binary SHA-256: `77e8891edfe4abbabb892825d0959ea87cf3cce7a9be4d03f2581f940fe4292d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_tv_bit.scene`

67 graph nodes, 81 edges; 14 event-bearing sections, 38 events; 26 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Journalist (actor 0, community); Wawuda (actor 1, community); chicken_journalist (actor 2, community); chicken_wawuda (actor 3, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 54 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnDialogLineEvent` | 14 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 12 | 57 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scneventsSocket` | 11 | 54 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation, socket_signal: 3
- speech, idle_animation, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation: 1

Raw SHA-256: `e0f9871702126ac7625679f46061ba5dafea7483943b51b34d426800141754f9`. Binary SHA-256: `8fc2d4fa709fea186efbcf804d8683b28084add6d29c843e880cde84e5116bba`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_tv_bit.scene" --events
```

