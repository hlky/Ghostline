# Boat Drinks: scene presentation

Journal identity: `quests/side_quest/sq028_kerry_romance`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq028_kerry_romance.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene`

33 graph nodes, 40 edges; 4 event-bearing sections, 17 events; 9 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: kerry (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `Start_call` → 1; `Start 0` → 56.

Exits: `End_call` → 2; `rejected_out` → 255.

End nodes: 2: `<omitted>`; 255: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 19 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 8 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 2 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 3 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 2 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, gaze: 1

Raw SHA-256: `cef745038a4fcdb0ae646db7c232760c47cd1711fe1002a331da4a2d7415f26e`. Binary SHA-256: `437451c039a47ffa5dea6343c5e7101534b38998b0e1338b21cc4f09ce08c498`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene" --events
```

## `base\quest\side_quests\sq028\scenes\sq028_02_welcome_aboard.scene`

132 graph nodes, 162 edges; 28 event-bearing sections, 173 events; 48 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: kerry (actor 0, spawnSet); johnny (actor 1, spawnDespawn); yacht (actor 2, community); v (actor 3, findInContext).

Entries: `Start 0` → 1; `wait_kerry_in` → 414; `Start 1` → 255.

Exits: `End_cruiser` → 2; `End1` → 2476; `End_no_go` → 20; `wait_kerry_out` → 445.

End nodes: 2: `NonTerminating`; 20: `NonTerminating`; 445: `<omitted>`; 2476: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 13 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnChangeIdleAnimEvent` | 3 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 29 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 2435 / 547 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/3` |
| `scnIKEvent` | 2 | 2435 / 545 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/1` |
| `scnLookAtEvent` | 23 | 9 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 55 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 2435 / 551 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/6` |
| `scneventsAttachPropToPerformer` | 2 | 111 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scneventsAttachPropToWorld` | 3 | 111 / 195 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |
| `scneventsCameraParamsEvent` | 1 | 13 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 4 | 13 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsSocket` | 41 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 2 | 13 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 4
- gaze: 3
- skeletal_animation: 3
- skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 2
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- props_equipment: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- audio, socket_signal: 1

Raw SHA-256: `1827c24350f6b3036da8cafccc76dce29f2a02dbdf71409c0ba52b07a054a4ed`. Binary SHA-256: `3df635307cbb49a552e18366be74bcd7272162f82c898c3b8f7daaafebddc738`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq028\scenes\sq028_02_welcome_aboard.scene" --events
```

## `base\quest\side_quests\sq028\scenes\sq028_03_chilling_out.scene`

75 graph nodes, 88 edges; 22 event-bearing sections, 221 events; 61 screenplay lines, 11 screenplay options, 5 choice nodes.

Actors: kerry (actor 0, spawnSet); johnny (actor 1, spawnDespawn); sq028_com_yacht (actor 2, community); v (actor 3, findInContext).

Entries: `Start 0` → 1; `scene_preview` → 244; `Start 3` → 211.

Exits: `End 0` → 2; `End 3` → 259.

End nodes: 2: `NonTerminating`; 259: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 14 | 343 / 417 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/2` |
| `scnChangeIdleAnimEvent` | 12 | 44 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnDialogLineEvent` | 47 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 255 / 338 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/5` |
| `scnIKEvent` | 2 | 255 / 333 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/1` |
| `scnLookAtEvent` | 58 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 53 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 1 | 255 / 337 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/4` |
| `scneventsAttachPropToPerformer` | 1 | 114 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/4` |
| `scneventsCameraParamsEvent` | 2 | 317 / 377 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 114 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |
| `scneventsSocket` | 25 | 4 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, gaze, socket_signal: 2
- camera: 2
- speech, gaze: 1
- speech, idle_animation, gaze: 1
- props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- socket_signal, animation_state: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1
- gaze: 1
- audio: 1
- idle_animation: 1

Raw SHA-256: `d221b5407343bbdfc13fab51c4eb975f4833d71d9c4ba554848d8f3c7b75e8f4`. Binary SHA-256: `236dabb5175aaa553c0cb8b531daa915ccafbb29b68259dba5f06e40602ab81b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq028\scenes\sq028_03_chilling_out.scene" --events
```

## `base\quest\side_quests\sq028\scenes\sq028_04_destructive_tendencies.scene`

149 graph nodes, 178 edges; 29 event-bearing sections, 177 events; 50 screenplay lines, 10 screenplay options, 7 choice nodes.

Actors: kerry (actor 0, spawnSet); johnny (actor 1, spawnDespawn); sq028_yacht (actor 2, community); spawner_yaccht (actor 3, spawner); v (actor 4, findInContext).

Entries: `Start 0` → 1; `Start 4` → 643; `Start 5` → 645; `Start 6` → 647; `Start 3` → 364; `Start 7` → 824; `seamurai_start` → 89; `animation_stop` → 249; `Start1` → 598.

Exits: `End_break_stuff` → 2; `cleanup` → 680; `seamurai_end` → 114.

End nodes: 2: `NonTerminating`; 114: `NonTerminating`; 680: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 79 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scnChangeIdleAnimEvent` | 21 | 81 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/9` |
| `scnDialogLineEvent` | 25 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 81 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/18` |
| `scnIKEvent` | 6 | 81 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnLookAtEvent` | 17 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 30 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 3 | 81 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/17` |
| `scneventsAttachPropToPerformer` | 3 | 91 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scneventsAttachPropToWorld` | 3 | 79 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scneventsCameraParamsEvent` | 7 | 81 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 10 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 31 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 11 | 4 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, socket_signal: 4
- speech: 2
- speech, gaze: 2
- socket_signal, animation_state: 2
- gaze, socket_signal: 2
- skeletal_animation, idle_animation: 2
- skeletal_animation, idle_animation, camera: 2
- speech, skeletal_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, socket_signal: 1
- props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, camera, audio: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `c37ec3f9e2bad6ba319f7c3c07bd72cb1ff702bbeda4cd1b02863aa8deb49cc6`. Binary SHA-256: `489861d39dce4f8ceb76c27fed2244b55cd3e0995a89d891639144a3e8ca303c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq028\scenes\sq028_04_destructive_tendencies.scene" --events
```

## `base\quest\side_quests\sq028\scenes\sq028_05_sex.scene`

91 graph nodes, 111 edges; 10 event-bearing sections, 296 events; 25 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: kerry (actor 0, spawnSet); johnny (actor 1, spawnSet); sq028yacht (actor 2, spawner); v (actor 3, findInContext).

Entries: `Start_demolition` → 1; `Start 4` → 198; `Start 5` → 237; `Start 6` → 239; `Start 3` → 165; `rip` → 347; `Start 2` → 83.

Exits: `End 0` → 2; `sex_ending` → 151.

End nodes: 2: `<omitted>`; 151: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 22 | 94 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scnChangeIdleAnimEvent` | 7 | 9 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 7 | 15 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 15 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnIKEvent` | 8 | 15 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnLookAtEvent` | 13 | 9 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlayRidAnimEvent` | 24 | 94 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnPlaySkAnimEvent` | 87 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 4 | 15 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsAttachPropToPerformer` | 1 | 522 / 969 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 9 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsCameraParamsEvent` | 6 | 9 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsPlayRidCameraAnimEvent` | 22 | 94 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 4 | 15 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsSocket` | 55 | 9 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsVFXEvent` | 30 | 94 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 2
- skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1

Raw SHA-256: `d951305ab55db83eae68360281b190e5d66369a8e8ef8a633b39bf93fbc1ab84`. Binary SHA-256: `8ee74e0984e4fc7055a4e60b55c3e82940a9617e018e410de6089815b1bc082d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq028\scenes\sq028_05_sex.scene" --events
```

## `base\quest\side_quests\sq028\scenes\sq028_06_wrap_up.scene`

58 graph nodes, 64 edges; 12 event-bearing sections, 82 events; 21 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: kerry (actor 0, spawnSet); johnny (actor 1, spawnDespawn); spawner (actor 2, spawner); v (actor 3, findInContext).

Entries: `Start 0` → 1; `refuse` → 156; `Start 5` → 171; `Start 2` → 123; `Start 6` → 174; `Start 1` → 87; `Start 3` → 140.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 8 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnChangeIdleAnimEvent` | 1 | 67 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnDialogLineEvent` | 12 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 4 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnIKEvent` | 6 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 8 | 4 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scnPlaySkAnimEvent` | 9 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 3 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsAttachPropToPerformer` | 5 | 8 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsAttachPropToWorld` | 3 | 8 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scneventsCameraParamsEvent` | 2 | 8 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 3 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 19 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXEvent` | 4 | 8 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation: 1
- speech: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `3603060d91cddcf25bb10fec3cb53c21ab5cddc3634ba4a38a1195d4d6d2fc28`. Binary SHA-256: `b8a16ca4046092df5c46a78945be3909e6f56d0f53f47364fad248bb136ee0fd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq028\scenes\sq028_06_wrap_up.scene" --events
```

## `base\quest\side_quests\sq028\scenes\sq028_07_trashy_beach.scene`

103 graph nodes, 145 edges; 26 event-bearing sections, 203 events; 63 screenplay lines, 10 screenplay options, 4 choice nodes.

Actors: kerry (actor 0, spawnSet); sq028_yacht (actor 1, community); sq028_yacht_no_enviro (actor 2, community); v (actor 3, findInContext).

Entries: `beach_in` → 1; `Start 1` → 227; `Start 2` → 230; `mainline` → 252; `Start 4` → 287.

Exits: `back_together_out` → 2; `cleanup` → 429.

End nodes: 2: `NonTerminating`; 429: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 9 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scnChangeIdleAnimEvent` | 15 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 51 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 52 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |
| `scnIKEvent` | 8 | 52 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnLookAtEvent` | 46 | 5 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 26 | 9 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnUnmountEvent` | 4 | 52 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/10` |
| `scneventsCameraParamsEvent` | 4 | 113 / 314 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 4 | 52 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/9` |
| `scneventsSocket` | 34 | 9 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scneventsVFXEvent` | 1 | 52 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- skeletal_animation, socket_signal: 2
- socket_signal: 2
- camera: 2
- speech, idle_animation, gaze: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze: 1
- speech, skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, camera, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio: 1

Raw SHA-256: `5365b4e288c11fcc6c933ff1e7fc695f27803d72056594215c5113a058a26256`. Binary SHA-256: `1bb663aabc3292a2789b1bc6e8c2ce20ff81242a9b2d66c91ecf4a97bd2c2cbe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq028\scenes\sq028_07_trashy_beach.scene" --events
```

