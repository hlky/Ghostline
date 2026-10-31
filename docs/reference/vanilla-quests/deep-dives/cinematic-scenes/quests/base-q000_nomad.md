# The Nomad: scene presentation

Journal identity: `quests/main_quest/prologue/q000_nomad`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q000_nomad.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_01_garage.scene`

308 graph nodes, 387 edges; 51 event-bearing sections, 453 events; 89 screenplay lines, 25 screenplay options, 18 choice nodes.

Actors: Mechanic (actor 0, spawnSet); Sheriff (actor 1, spawnSet); player_tpp_female (actor 2, spawnDespawn); player_tpp_male (actor 3, spawnDespawn); player_galena (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `q000_kid_01_garage_in` → 1; `Start 4` → 2440.

Exits: `q000_kid_01_garage_out` → 2; `FT _Terminating_End` → 867.

End nodes: 2: `NonTerminating`; 867: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 23 | 27 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnChangeIdleAnimEvent` | 37 | 21 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 76 | 21 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayActionEvent` | 2 | 27 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnGameplayTransitionEvent` | 4 | 217 / 497 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/26` |
| `scnIKEvent` | 12 | 36 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnLookAtEvent` | 53 | 36 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/9` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 698 / 1026 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/10` |
| `scnPlaySkAnimEvent` | 79 | 27 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 36 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scnUnmountEvent` | 4 | 217 / 509 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/35` |
| `scneventsAttachPropToNode` | 7 | 217 / 495 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/24` |
| `scneventsAttachPropToPerformer` | 3 | 36 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scneventsAttachPropToWorld` | 6 | 36 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsCameraParamsEvent` | 7 | 217 / 473 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 8 | 27 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsSocket` | 110 | 21 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsVFXEvent` | 19 | 27 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, gaze: 5
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- speech: 4
- gaze: 3
- camera: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- skeletal_animation, idle_animation, gaze, camera, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, ik, camera, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1
- speech, audio, vfx: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, idle_animation, ik, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- props_equipment: 1

Raw SHA-256: `71b794d483c71a81aaec848de3dcfb34824a1b69e6341f1cc8d6119ad780e43f`. Binary SHA-256: `4c801543f476b59f22861afc67c20b4a5e7560860c422841c623508069669dcd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_01_garage.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_02_fixer.scene`

87 graph nodes, 123 edges; 15 event-bearing sections, 116 events; 34 screenplay lines, 9 screenplay options, 7 choice nodes.

Actors: Fixer (actor 0, spawnDespawn); background_car_driver (actor 1, spawner); nomad_car_01 (actor 2, spawner); Player (actor 3, findInContext).

Entries: `q000_nomad_02_fixer_in` → 1; `SceneSkippedIdleOnly` → 335; `q000_nomad_Gate_in` → 362; `Start 3` → 394; `q000_nomad_02_fixer_gate_in` → 192.

Exits: `q000_nomad_02_fixer_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 28 | 11 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnChangeIdleAnimEvent` | 11 | 29 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnDialogLineEvent` | 23 | 11 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 48 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/8` |
| `scnIKEvent` | 4 | 29 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |
| `scnPlaySkAnimEvent` | 11 | 29 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnUnmountEvent` | 1 | 48 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/12` |
| `scneventsAttachPropToPerformer` | 1 | 29 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 48 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 1 | 48 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/11` |
| `scneventsSocket` | 32 | 11 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 2 | 153 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, audio, socket_signal: 6
- idle_animation: 2
- skeletal_animation, idle_animation, ik, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, vfx: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `9a987b271b70eaae3aafdd09d9cef4307e048454ddad8419979081d4fd68f161`. Binary SHA-256: `11c2e70f04f2b58e3d49df8f5f062b8a2d9d186e2dcec36ed9c69ba5dc420da2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_02_fixer.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_03_jackie.scene`

138 graph nodes, 168 edges; 22 event-bearing sections, 221 events; 77 screenplay lines, 14 screenplay options, 5 choice nodes.

Actors: Jackie (actor 0, spawnSet); nomad_car (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `q000_nomad_03_jackie_in` → 1; `q000_nomad_03_jackie_from_failsafe` → 478; `q000_nomad_jackie_startsetu` → 990.

Exits: `q000_nomad_03_jackie_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 24 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scnChangeIdleAnimEvent` | 23 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 52 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtAdvancedEvent` | 4 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 32 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 37 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scnPlaySkAnimEvent` | 49 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPoseCorrectionEvent` | 6 | 3 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsAttachPropToNode` | 3 | 31 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/11` |
| `scneventsAttachPropToPerformer` | 4 | 31 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 1 | 37 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scneventsSocket` | 41 | 3 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `3979007b6969e43808d461f58d4a23a26d9ed03ea9135a3ff699309eb5d611f7`. Binary SHA-256: `c8502fc9aca6346bfa035c4193b66120022b874d7c8930102ac3e1071549b591`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_03_jackie.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_04_drive_to_border.scene`

28 graph nodes, 36 edges; 9 event-bearing sections, 49 events; 19 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Jackie (actor 0, spawnSet); vs_car (actor 1, spawnSet); helicopter (actor 2, spawner); Player (actor 3, findInContext).

Entries: `q000_nomad_04_drive_to_border_in` → 1; `HelicopterIdleIn` → 138; `Start 1` → 89.

Exits: `q000_nomad_04_drive_to_border_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 9 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 17 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 139 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/0` |
| `scnLookAtEvent` | 20 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 80 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |
| `scnPlaySkAnimEvent` | 3 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 2 | 80 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scneventsSocket` | 2 | 45 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 4
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze, socket_signal: 1
- socket_signal, animation_state, mount_workspot: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `a45bde14fd905e80f00353f416ee26e9808e73853bd57ad339bbfeb70fa08ccf`. Binary SHA-256: `36e085db05ca7cd2a2c82b865997e8941dcd4f22b1dacf5283b86714e63d64f8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_04_drive_to_border.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_05_border_crossing.scene`

329 graph nodes, 393 edges; 60 event-bearing sections, 309 events; 87 screenplay lines, 17 screenplay options, 12 choice nodes.

Actors: Jackie (actor 0, spawnSet); Border_Loadspeaker (actor 1, spawnDespawn); Officer (actor 2, community); Guard (actor 3, community); guard_interior_walking (actor 4, community); guard_guide (actor 5, community); vs_car (actor 6, spawnSet); vs_car_chase (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `q000_nomad_05_border_crossing_in` → 1; `Start 11` → 1927; `IllegalCrossingWarningIn` → 370; `IllegalCrossingWithJackieIn` → 371; `IllegalCrossingAffterInterrogation` → 379; `q000_questioning_start` → 396; `q000_walk_out` → 518; `Start 8` → 1175; `Start 10` → 1203; `leaning_at_car` → 1904.

Exits: `q000_nomad_05_border_crossing_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 82 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnChangeIdleAnimEvent` | 18 | 7 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 65 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 511 / 1017 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 249 / 506 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/9` |
| `scnIKEvent` | 8 | 249 / 497 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/1` |
| `scnLookAtEvent` | 46 | 7 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 515 / 1046 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/8` |
| `scnPlaySkAnimEvent` | 48 | 19 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnUnmountEvent` | 2 | 249 / 505 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/8` |
| `scneventsAttachPropToNode` | 2 | 539 / 1106 | `/Data/RootChunk/sceneGraph/Data/graph/134/Data/events/9` |
| `scneventsAttachPropToPerformer` | 9 | 21 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/7` |
| `scneventsAttachPropToWorld` | 5 | 82 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/6` |
| `scneventsCameraParamsEvent` | 2 | 94 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 11 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 74 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 1 | 102 / 263 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- gaze: 6
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- idle_animation, socket_signal: 2
- socket_signal: 2
- speech, socket_signal, animation_state: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal, gameplay_action: 1
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, props_equipment, audio: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- animation_state, mount_workspot: 1
- speech, gaze: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `696c9b4920183220e91659ce27afe9604d375a4d98a673053b874474624f49c1`. Binary SHA-256: `e5851647338dfa4de9c55aef7606535e8a52bf9a0e6123968419b2f2e597c132`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_05_border_crossing.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_05b_border_chats.scene`

66 graph nodes, 78 edges; 5 event-bearing sections, 37 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: traveller_female (actor 0, community); traveller_male (actor 1, community); inspection_guard_01 (actor 2, community); guards_chat_01 (actor 3, community); inspection_guard_02 (actor 4, community); travellers_car (actor 5, spawner); player (actor 6, findInContext).

Entries: `q000_nomad_05b_chats_in` → 1; `ArrestScenePreview` → 222.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 28 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnLookAtEvent` | 7 | 28 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlaySkAnimEvent` | 10 | 45 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsSocket` | 14 | 45 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2
- speech, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `d08c4952618f71f043e7fb76e1232680b8d8186b5a37f0927e6009aa09268f32`. Binary SHA-256: `fe2ee0eb061a70a4dfa58c42498bbc3923d522723b6bf824e4ce64feac66312f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_05b_border_chats.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_06_chase.scene`

344 graph nodes, 369 edges; 28 event-bearing sections, 108 events; 42 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Jackie (actor 0, spawnSet); Arasaka_Security (actor 1, community); vs_car (actor 2, spawnSet); ArasakaCar01 (actor 3, spawner); ArasakaCar02 (actor 4, spawner); ArasakaCar03 (actor 5, spawner); Player (actor 6, findInContext).

Entries: `q000_nomad_06_chase_in` → 1; `old_lines` → 567; `Start 2` → 1269; `Start 3` → 1296.

Exits: `q000_nomad_06_chase_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 695 / 456 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/6` |
| `scnChangeIdleAnimEvent` | 6 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 37 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 28 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 3 | 1280 / 1323 | `/Data/RootChunk/sceneGraph/Data/graph/219/Data/events/7` |
| `scnPlaySkAnimEvent` | 8 | 291 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 695 / 438 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/0` |
| `scneventsSocket` | 20 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, socket_signal: 4
- speech, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, gaze, socket_signal: 2
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, animation_state, mount_workspot: 1
- animation_state, mount_workspot: 1

Raw SHA-256: `6cff847dd6ff27709a74fbde2da4422e3ad7b59c7f1b32fae53273b671e62bf3`. Binary SHA-256: `9577de8413fde4f3c5d06e0e26d874de291440efaa8422cf0695faf4a70d8a04`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_06_chase.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_07_hideout.scene`

183 graph nodes, 230 edges; 40 event-bearing sections, 362 events; 82 screenplay lines, 18 screenplay options, 12 choice nodes.

Actors: Jackie (actor 0, spawnSet); galena (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `q000_nomad_07_hideout_in` → 1; `Start 5` → 888; `Start 3` → 762; `FAKE INPUT LOCO` → 1062; `q000_nomad_07_hideout_test_only_in` → 627; `Start 4` → 780; `Start 6` → 931; `Start 7` → 936; `Start 1` → 543; `Start 2` → 561.

Exits: `q000_nomad_07_hideout_out` → 2; `MontagePreloadOut` → 1159.

End nodes: 2: `<omitted>`; 1159: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 10 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnChangeIdleAnimEvent` | 40 | 10 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnDialogLineEvent` | 68 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 3 | 276 / 418 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/5` |
| `scnGameplayTransitionEvent` | 1 | 692 / 866 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/6` |
| `scnIKEvent` | 4 | 301 / 489 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/5` |
| `scnLookAtEvent` | 70 | 10 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 483 / 665 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/0` |
| `scnPlaySkAnimEvent` | 78 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPoseCorrectionEvent` | 1 | 281 / 457 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/5` |
| `scnUnmountEvent` | 1 | 692 / 870 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 4 | 483 / 666 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/1` |
| `scneventsSocket` | 78 | 10 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsVFXEvent` | 3 | 10 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal: 6
- gaze: 4
- speech: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, ik, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation: 1
- animation_state, mount_workspot: 1
- idle_animation: 1
- skeletal_animation, idle_animation, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `cc6b544241043c5175c8c7a816dd9a317ed08ac57c0d6103ddcc497497781f07`. Binary SHA-256: `51bdf2c489882a73ecaac4066b8a91cb113b19c36e2936af5b25db8a16e89011`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_07_hideout.scene" --events
```

