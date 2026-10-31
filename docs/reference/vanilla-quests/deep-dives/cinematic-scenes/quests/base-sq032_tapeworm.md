# Tapeworm: scene presentation

Journal identity: `quests/side_quest/sq032_tapeworm`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq032_tapeworm.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene`

172 graph nodes, 198 edges; 45 event-bearing sections, 357 events; 90 screenplay lines, 25 screenplay options, 13 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 1` → 773; `in_q105` → 74; `in_q104` → 76; `preview_02` → 742.

Exits: `out_clean_up` → 854; `out` → 104.

End nodes: 104: `NonTerminating`; 854: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 84 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scnChangeIdleAnimEvent` | 18 | 84 / 131 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/10` |
| `scnDialogLineEvent` | 83 | 78 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 327 / 614 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/12` |
| `scnIKEvent` | 4 | 327 / 598 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/1` |
| `scnLookAtAdvancedEvent` | 1 | 84 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scnLookAtEvent` | 44 | 78 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnOverridePhantomParamsEvent` | 5 | 78 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnPlaySkAnimEvent` | 61 | 78 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 2 | 327 / 620 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/17` |
| `scneventsAttachPropToPerformer` | 10 | 84 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/8` |
| `scneventsAttachPropToWorld` | 7 | 84 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/14` |
| `scneventsCameraParamsEvent` | 9 | 78 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 327 / 615 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/13` |
| `scneventsSocket` | 84 | 78 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXEvent` | 13 | 78 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, camera, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, camera, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, camera, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- gaze, socket_signal: 1

Raw SHA-256: `6ce13afd75b8a7005de7113570521f47721907593f628e4fe2656970b1b5bf0f`. Binary SHA-256: `9bc247ae1e1af865767a9f06f1d785ebb8f39f20d8e6853f683098b34da0d4ae`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene" --events
```

## `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene`

248 graph nodes, 322 edges; 70 event-bearing sections, 431 events; 124 screenplay lines, 45 screenplay options, 22 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); johnny_spawnset_cat (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `in_q105` → 1; `in_q110` → 7; `in_q104` → 10; `in_q112` → 13; `q104_end` → 1071; `q003_cat_reaction_in` → 894; `q112_end` → 1135; `Start1` → 1871.

Exits: `out` → 2; `q003_cat_reaction_out` → 895; `out_clean_up` → 1437.

End nodes: 2: `NonTerminating`; 895: `<omitted>`; 1437: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 11 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnChangeIdleAnimEvent` | 4 | 45 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |
| `scnDialogLineEvent` | 117 | 8 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnGameplayTransitionEvent` | 6 | 74 / 317 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/5` |
| `scnIKEvent` | 12 | 74 / 313 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scnLookAtEvent` | 61 | 8 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPlaySkAnimEvent` | 92 | 8 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnUnmountEvent` | 6 | 74 / 323 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/10` |
| `scneventsAttachPropToPerformer` | 4 | 74 / 318 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/6` |
| `scneventsAttachPropToWorld` | 4 | 74 / 335 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/14` |
| `scneventsCameraParamsEvent` | 13 | 74 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 6 | 74 / 319 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/7` |
| `scneventsSocket` | 81 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsVFXEvent` | 23 | 8 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 17
- speech: 16
- speech, skeletal_animation, gaze, vfx, socket_signal: 7
- speech, skeletal_animation: 4
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, camera, vfx, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- speech, gaze: 2
- camera: 2
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- speech, skeletal_animation, props_equipment: 1

Raw SHA-256: `741c9afca4a9bfd7f85b046bb95a55a58f3c8097aaa576df847557bb64192e01`. Binary SHA-256: `96d4c0b4a3c808443ffa337f140bff840293d275ae97115658d190964cdfab10`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene" --events
```

## `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene`

191 graph nodes, 226 edges; 53 event-bearing sections, 422 events; 119 screenplay lines, 36 screenplay options, 12 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); women (actor 1, spawnDespawn); man (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `in_q105` → 1; `in_q110` → 6; `in_q104` → 9; `in_q112` → 12; `Start 1` → 948; `cigarette_prop_removal` → 1197.

Exits: `out` → 2; `out_clean_up` → 734; `cigarette_prop_removal_out` → 1201.

End nodes: 2: `NonTerminating`; 734: `<omitted>`; 1201: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 31 | 15 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scnChangeIdleAnimEvent` | 10 | 15 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnDialogLineEvent` | 107 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 130 / 352 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/12` |
| `scnIKEvent` | 4 | 130 / 343 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/3` |
| `scnLookAtEvent` | 26 | 15 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scnOverridePhantomParamsEvent` | 1 | 15 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |
| `scnPlaySkAnimEvent` | 81 | 15 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnUnmountEvent` | 2 | 130 / 357 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/16` |
| `scneventsAttachPropToNode` | 2 | 130 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/11` |
| `scneventsAttachPropToPerformer` | 6 | 57 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/7` |
| `scneventsAttachPropToWorld` | 2 | 74 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/7` |
| `scneventsCameraParamsEvent` | 5 | 74 / 174 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/2` |
| `scneventsEquipItemToPerformer` | 11 | 75 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 2 | 130 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/13` |
| `scneventsSocket` | 84 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 10 | 130 / 348 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/8` |
| `scneventsUnequipItemFromPerformerByItem` | 5 | 74 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/5` |
| `scneventsVFXEvent` | 31 | 10 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 11
- speech, socket_signal: 4
- speech: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 3
- speech, skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 2
- skeletal_animation, audio, vfx, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- speech, gaze: 1
- speech, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, ik, camera, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, audio, vfx: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, vfx: 1
- skeletal_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, props_equipment: 1

Raw SHA-256: `5809078320a18521ea6cc6a8116a0480613888fb8ccf906bc1a8ba75b8e451e0`. Binary SHA-256: `4b2f63542a6e290967aaa11834025c1c164717c7059b1313c1c601feb5c4d7b4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene" --events
```

## `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene`

70 graph nodes, 89 edges; 15 event-bearing sections, 104 events; 30 screenplay lines, 4 screenplay options, 4 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `in_q110` → 1; `in_q104` → 4; `in_q112` → 5.

Exits: `out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 6 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnChangeIdleAnimEvent` | 4 | 6 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnDialogLineEvent` | 17 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnLookAtEvent` | 9 | 6 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scnPlaySkAnimEvent` | 15 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsCameraParamsEvent` | 10 | 6 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsSocket` | 17 | 6 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scneventsVFXEvent` | 22 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 4
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 2
- speech, socket_signal: 2
- skeletal_animation, gaze, vfx, socket_signal: 2
- vfx: 2
- speech, audio: 1
- speech, gaze: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `dd31db68202838f6d7e38b1ce802a24fd81158327fe2e1edb8751ce2e091880b`. Binary SHA-256: `b896ccbeaddf3f15ba9bfc3965e7e2cc0326fba1ce9da9fe96dc0ddfa6dde9ff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene" --events
```

## `base\quest\side_quests\sq032\scenes\sq032_07_finale.scene`

222 graph nodes, 266 edges; 68 event-bearing sections, 427 events; 159 screenplay lines, 52 screenplay options, 21 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `in` → 1; `Start 1` → 715; `Start 2` → 988; `Start 0` → 1005.

Exits: `out` → 2; `out_clean_up` → 795.

End nodes: 2: `NonTerminating`; 795: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 19 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scnChangeIdleAnimEvent` | 7 | 19 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scnDialogLineEvent` | 147 | 19 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnGameplayTransitionEvent` | 9 | 34 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scnIKEvent` | 18 | 34 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnLookAtEvent` | 27 | 19 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |
| `scnPlaySkAnimEvent` | 95 | 19 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 9 | 34 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/11` |
| `scneventsAttachPropToPerformer` | 4 | 19 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsAttachPropToWorld` | 4 | 34 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |
| `scneventsCameraParamsEvent` | 2 | 137 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 9 | 34 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/8` |
| `scneventsSocket` | 75 | 19 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsVFXEvent` | 17 | 19 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 30
- speech, skeletal_animation, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation: 4
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation: 1
- socket_signal: 1

Raw SHA-256: `e75c2eff211330c977ef38f78a75a88ec2b051e4a50985e7919742a6974c9e43`. Binary SHA-256: `4a7dde35f23955d64da3137474a75d37915c6f5555bed678f16d31fb72a33f2e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq032\scenes\sq032_07_finale.scene" --events
```

