# New Dawn Fades: scene presentation

Journal identity: `quests/main_quest/epilogues/q204_reborn`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q204_reborn.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\epilogue\q204\scenes\q204_01_waking_up.scene`

162 graph nodes, 184 edges; 23 event-bearing sections, 106 events; 16 screenplay lines, 11 screenplay options, 9 choice nodes.

Actors: v_tpp_mirror_male (actor 0, spawnDespawn); v_tpp_mirror_female (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `q204_01_waking_in` → 1; `Start 3` → 2174; `in_mirror` → 986.

Exits: `out_clean_up` → 816; `q204_01_waking_out` → 55.

End nodes: 55: `NonTerminating`; 816: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 43 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnChangeIdleAnimEvent` | 2 | 533 / 257 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/3` |
| `scnDialogLineEvent` | 13 | 32 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 497 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/8` |
| `scnIKEvent` | 8 | 497 / 213 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/1` |
| `scnLookAtEvent` | 4 | 765 / 482 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/1` |
| `scnPlaySkAnimEvent` | 15 | 43 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 4 | 497 / 224 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/11` |
| `scneventsAttachPropToNode` | 1 | 2178 / 972 | `/Data/RootChunk/sceneGraph/Data/graph/150/Data/events/0` |
| `scneventsAttachPropToPerformer` | 6 | 43 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsAttachPropToWorld` | 5 | 43 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsCameraParamsEvent` | 9 | 286 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 4 | 497 / 222 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/10` |
| `scneventsSocket` | 17 | 43 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsVFXEvent` | 2 | 286 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation, camera, props_equipment, audio: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, camera: 1
- speech, skeletal_animation, props_equipment, audio: 1
- skeletal_animation, camera, audio, socket_signal: 1
- props_equipment: 1

Raw SHA-256: `fb863bd20cb776e75a2ed47d90f47fbf09b9d590a91cc312f5034b561b9684bc`. Binary SHA-256: `db2c779ab923152ed0e941d8ed02c5f7eb1c1d4d2a0bac52fe4fb6fc9dfe6ebf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q204\scenes\q204_01_waking_up.scene" --events
```

## `base\quest\main_quests\epilogue\q204\scenes\q204_02_at_steves.scene`

61 graph nodes, 74 edges; 24 event-bearing sections, 104 events; 45 screenplay lines, 10 screenplay options, 4 choice nodes.

Actors: Steve (actor 0, spawnSet); Steves_mom (actor 1, community); V (actor 2, findInContext).

Entries: `in_door` → 1; `q204_09_01` → 469; `q204_09_02` → 472; `in_steve` → 329.

Exits: `out_steve` → 2; `out_door` → 323.

End nodes: 2: `NonTerminating`; 323: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 12 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnChangeIdleAnimEvent` | 10 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 42 | 5 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 13 | 5 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 17 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 7 | 5 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsSocket` | 14 | 5 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `14c48e1c46f0ca31ac8a7be323398e34794f584c34c06a06a0fd65b33d0f17a1`. Binary SHA-256: `d86dd4ce135e10728330bacc78d61f666d645b451e4fe81bf8d6e0bd76ce16b4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q204\scenes\q204_02_at_steves.scene" --events
```

## `base\quest\main_quests\epilogue\q204\scenes\q204_03_steves_dad.scene`

111 graph nodes, 150 edges; 26 event-bearing sections, 249 events; 60 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: Steve (actor 0, spawnSet); Steves_dad (actor 1, community); Steves_dad_friend_01 (actor 2, community); Steves_dad_friend_02 (actor 3, community); steves_dad_car (actor 4, spawnSet); V (actor 5, findInContext).

Entries: `q204_03_before_dad_in` → 1; `placeholder` → 507.

Exits: `peace_done` → 122; `reason_done` → 123; `threaten_done` → 40; `steve_stands_up_done` → 152.

End nodes: 40: `NonTerminating`; 122: `NonTerminating`; 123: `NonTerminating`; 152: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 88 / 187 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/32` |
| `scnChangeIdleAnimEvent` | 7 | 27 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 46 | 7 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 6 | 27 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/31` |
| `scnIKEvent` | 12 | 27 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/21` |
| `scnLookAtAdvancedEvent` | 2 | 494 / 839 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/1` |
| `scnLookAtEvent` | 69 | 7 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 44 | 7 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnUnmountEvent` | 6 | 27 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/30` |
| `scneventsSetAnimFeatureEvent` | 6 | 27 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/27` |
| `scneventsSocket` | 40 | 7 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsVFXEvent` | 2 | 265 / 450 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/21` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 6
- skeletal_animation, socket_signal: 5
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze: 1
- socket_signal: 1

Raw SHA-256: `5bdd98cf07fc2d1ba2f0b5e614b79c3eb6a989f33d569651f1d0c30bab2f54ee`. Binary SHA-256: `c3b1bb73ba95bd92cd3e163a1d0cde500cd5763d1fefca768525416930e20ba9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q204\scenes\q204_03_steves_dad.scene" --events
```

## `base\quest\main_quests\epilogue\q204\scenes\q204_03b_after_dad.scene`

70 graph nodes, 84 edges; 17 event-bearing sections, 100 events; 43 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: Steve (actor 0, spawnSet); Steves_dad (actor 1, community); steve_car (actor 2, spawnSet); Johnny (actor 3, findInContext); Player (actor 4, findInContext).

Entries: `q204_03b_dad_defeated_in` → 1; `steve stood up` → 175; `threaten` → 119; `peace` → 122; `reason` → 123.

Exits: `q204_03b_after_dad_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 344 / 285 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/3` |
| `scnChangeIdleAnimEvent` | 7 | 50 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 30 | 50 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 352 / 312 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/8` |
| `scnIKEvent` | 4 | 344 / 288 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/6` |
| `scnLookAtEvent` | 25 | 50 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 14 | 50 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPoseCorrectionEvent` | 1 | 344 / 287 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/5` |
| `scnUnmountEvent` | 1 | 352 / 311 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 3 | 344 / 274 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |
| `scneventsSocket` | 10 | 66 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze: 2
- speech, gaze: 1
- skeletal_animation, gaze, ik, audio, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal, animation_state: 1

Raw SHA-256: `023f8f867716fefb77576b0b9ac6b9e5dcbeea1ff01d7605bf827fdc0b489e08`. Binary SHA-256: `e1984eb1ccc93c6a59f24b17206d1954ac5d577299143bcf600ef6ec41e60c67`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q204\scenes\q204_03b_after_dad.scene" --events
```

## `base\quest\main_quests\epilogue\q204\scenes\q204_04_to_music_store.scene`

125 graph nodes, 176 edges; 30 event-bearing sections, 209 events; 92 screenplay lines, 25 screenplay options, 9 choice nodes.

Actors: Steve (actor 0, spawnSet); steves_car (actor 1, spawnSet); Johnny (actor 2, findInContext).

Entries: `q204_04_to_music_store_in` → 1; `Start 3` → 776; `Start 1` → 656; `Start 2` → 691.

Exits: `q204_04_to_music_store_out` → 2; `q204_04_to_music_store_out_terminate` → 650.

End nodes: 2: `NonTerminating`; 650: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 281 / 366 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/2` |
| `scnChangeIdleAnimEvent` | 7 | 5 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 91 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 289 / 404 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/12` |
| `scnIKEvent` | 4 | 289 / 390 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/1` |
| `scnLookAtEvent` | 48 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 27 | 13 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnPoseCorrectionEvent` | 1 | 289 / 402 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/10` |
| `scnUnmountEvent` | 1 | 289 / 410 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/17` |
| `scneventsSetAnimFeatureEvent` | 4 | 281 / 358 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/0` |
| `scneventsSocket` | 18 | 5 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 8
- speech, skeletal_animation, gaze: 6
- speech, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation: 1
- skeletal_animation, audio, socket_signal, animation_state: 1
- skeletal_animation: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal, animation_state: 1
- gaze: 1

Raw SHA-256: `40e9a069b484586d57d789ab411b77ec2b1ec258e51ab1834c0fd6fbe2b82fa6`. Binary SHA-256: `e732aac6e4249657b0d478b290c651ac9955de1b6e32b838434868541b9e2297`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q204\scenes\q204_04_to_music_store.scene" --events
```

## `base\quest\main_quests\epilogue\q204\scenes\q204_05_buying_guitar.scene`

331 graph nodes, 421 edges; 75 event-bearing sections, 517 events; 192 screenplay lines, 49 screenplay options, 23 choice nodes.

Actors: StoreOwner (actor 0, community); Steve (actor 1, spawnSet); steve_car (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `q204_05_in` → 1; `Start 4` → 2100; `Start 5` → 2109; `in_vendor` → 1258; `Start 6` → 2146; `Start 0` → 2161.

Exits: `q204_05_out` → 2; `q204_05_clear` → 2054.

End nodes: 2: `NonTerminating`; 2054: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 26 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnChangeIdleAnimEvent` | 27 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 121 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 11 | 601 / 795 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/12` |
| `scnIKEvent` | 22 | 601 / 789 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/6` |
| `scnLookAtEvent` | 86 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 110 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 11 | 601 / 807 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/19` |
| `scneventsAttachPropToPerformer` | 6 | 26 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scneventsCameraParamsEvent` | 4 | 601 / 791 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 11 | 601 / 803 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/16` |
| `scneventsSocket` | 89 | 11 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsVFXDurationEvent` | 1 | 525 / 699 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/2` |
| `scneventsVFXEvent` | 2 | 521 / 689 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, idle_animation, gaze: 5
- speech, skeletal_animation, gaze, socket_signal: 5
- gaze: 5
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation: 3
- speech, idle_animation, gaze: 3
- skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, audio, socket_signal: 3
- socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation: 1
- speech, gaze: 1
- speech, skeletal_animation, vfx: 1
- speech, gaze, vfx: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `acbfa641e9811e9f06e86954cb881fec13dfebdfeca6f168b19b886e7ceee572`. Binary SHA-256: `0916efc9891d24d98c30f9b837f4790be3a63c98bb7e24758842a41d10978931`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q204\scenes\q204_05_buying_guitar.scene" --events
```

## `base\quest\main_quests\epilogue\q204\scenes\q204_06_to_columbarium.scene`

119 graph nodes, 153 edges; 26 event-bearing sections, 164 events; 82 screenplay lines, 11 screenplay options, 7 choice nodes.

Actors: steve (actor 0, spawnSet); Radio (actor 1, findInContext); steve_car (actor 2, spawnSet); get_out_at_columbarium (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `q000_06_to_columbarium_in` → 2; `in_radio` → 572; `columbarium` → 663.

Exits: `q000_06_to_columbarium_out` → 1.

End nodes: 1: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 205 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/3` |
| `scnDialogLineEvent` | 76 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 300 / 371 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/6` |
| `scnIKEvent` | 6 | 300 / 364 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/1` |
| `scnLookAtEvent` | 28 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 20 | 11 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnPoseCorrectionEvent` | 2 | 300 / 378 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/12` |
| `scnUnmountEvent` | 2 | 300 / 376 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/10` |
| `scneventsAttachPropToPerformer` | 6 | 82 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scneventsDespawnEntityEvent` | 2 | 82 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 5 | 205 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/1` |
| `scneventsSocket` | 12 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 5
- speech: 5
- speech, gaze: 5
- speech, gaze, socket_signal: 2
- skeletal_animation, props_equipment, audio, socket_signal, animation_state: 2
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, props_equipment, entity_lifecycle: 1
- speech, skeletal_animation, props_equipment, entity_lifecycle: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, socket_signal, animation_state: 1
- gaze: 1

Raw SHA-256: `8199fdff54c51380762c70d46fe0325109011f6bcd6542648763d52e989ee555`. Binary SHA-256: `567a1415541042691f9d51c91c2475b100900f81eb373efce23db9a3e5b62b5b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q204\scenes\q204_06_to_columbarium.scene" --events
```

## `base\quest\main_quests\epilogue\q204\scenes\q204_08_farewell.scene`

107 graph nodes, 117 edges; 16 event-bearing sections, 53 events; 18 screenplay lines, 9 screenplay options, 6 choice nodes.

Actors: Steve (actor 0, spawnSet); steve_car (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `q204_farewell_in` → 1; `in_map` → 526.

Exits: `q204_farewell_out` → 2; `out_map` → 531.

End nodes: 2: `NonTerminating`; 531: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 236 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/4` |
| `scnDialogLineEvent` | 13 | 217 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 236 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/11` |
| `scnIKEvent` | 4 | 236 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnLookAtEvent` | 1 | 823 / 599 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/0` |
| `scnPlaySkAnimEvent` | 10 | 236 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scnUnmountEvent` | 2 | 236 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |
| `scneventsAttachPropToPerformer` | 6 | 236 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 2 | 236 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/9` |
| `scneventsSocket` | 6 | 236 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/8` |
| `scneventsVFXEvent` | 1 | 308 / 205 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, skeletal_animation, idle_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- skeletal_animation: 2
- props_equipment: 2
- vfx: 1
- gaze: 1

Raw SHA-256: `e8adad89c4de1ea2e159673f6b217afd3edb58b737240baec2899f92a0409c7d`. Binary SHA-256: `5cd50675f98a9340a2175566c21aa82eef157bd18b39fc1532bbfe8e472ac46f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q204\scenes\q204_08_farewell.scene" --events
```

## `base\quest\main_quests\epilogue\q204\scenes\q204_09_bus_station.scene`

128 graph nodes, 164 edges; 20 event-bearing sections, 603 events; 57 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Steve (actor 0, spawnSet); male_tpp_v (actor 1, spawnDespawn); female_tpp_v (actor 2, spawnDespawn); passenger_fa_01 (actor 3, spawnDespawn); passenger_ma_01 (actor 4, spawnDespawn); steves_dad_car (actor 5, spawnSet); autobus (actor 6, spawner); V (actor 7, findInContext).

Entries: `Start 1` → 600; `q204_09_bus_station_in` → 1; `Start 2` → 603; `Start 4` → 944.

Exits: `q204_09_bus_station_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 8 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnChangeIdleAnimEvent` | 4 | 137 / 450 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |
| `scnDialogLineEvent` | 50 | 8 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scnGameplayActionEvent` | 2 | 223 / 535 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/4` |
| `scnGameplayTransitionEvent` | 3 | 146 / 479 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/12` |
| `scnIKEvent` | 6 | 146 / 469 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scnLookAtEvent` | 12 | 136 / 439 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 413 / 742 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/7` |
| `scnPlayRidAnimEvent` | 144 | 8 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 278 | 8 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 3 | 146 / 478 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/11` |
| `scneventsAttachPropToNode` | 1 | 226 / 555 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/7` |
| `scneventsAttachPropToPerformer` | 20 | 8 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scneventsAttachPropToWorld` | 4 | 180 / 496 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/5` |
| `scneventsPlayRidCameraAnimEvent` | 36 | 8 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 4 | 146 / 474 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/8` |
| `scneventsSocket` | 21 | 8 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/70` |
| `scneventsVFXEvent` | 3 | 418 / 746 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, rid_actor, camera, rid_camera, props_equipment, audio, socket_signal: 4
- gaze: 2
- skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, gameplay_action: 1
- skeletal_animation, idle_animation, props_equipment, audio, gameplay_action: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, audio, animation_state, mount_workspot: 1
- props_equipment, vfx, socket_signal: 1
- speech: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `03f0f0cab9146a35d572d1c9b9496a2019eaf0ca209c08e86588e376af7a6e8c`. Binary SHA-256: `6a1cefd51ddd134248c0bbf6cc3f28176b1c179284cb73f61684b3cb96ab843d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q204\scenes\q204_09_bus_station.scene" --events
```

