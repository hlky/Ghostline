# Following the River: scene presentation

Journal identity: `quests/side_quest/sq029_sobchak_romance`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq029_sobchak_romance.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq029\scenes\sq029_01a_phonecall.scene`

55 graph nodes, 62 edges; 16 event-bearing sections, 77 events; 58 screenplay lines, 10 screenplay options, 4 choice nodes.

Actors: sobchak (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `river_calls_in` → 1; `river_again_in` → 154.

Exits: `accept_invite_out` → 2; `reject_invite_out` → 16; `rejected_out` → 627; `river_again_out` → 155.

End nodes: 2: `<omitted>`; 16: `<omitted>`; 155: `<omitted>`; 627: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 19 | 27 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 58 | 27 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation: 9
- speech: 7

Raw SHA-256: `8a994dc19562487d3cdbd4e402e7e345378b56604e908dd2fe292e30d9a3eaa7`. Binary SHA-256: `548b276929573628b024d3d65508da5c32c3f7ac19dd702ec5596e84afdea615`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq029\scenes\sq029_01a_phonecall.scene" --events
```

## `base\quest\side_quests\sq029\scenes\sq029_02a_arrival.scene`

672 graph nodes, 836 edges; 123 event-bearing sections, 782 events; 206 screenplay lines, 32 screenplay options, 21 choice nodes.

Actors: River (actor 0, spawnSet); joss (actor 1, spawnSet); kid_boy (actor 2, spawnSet); kid_girl (actor 3, spawnSet); johnny (actor 4, spawnSet); V (actor 5, findInContext).

Entries: `cinedebug_start` → 1985; `cinematic_debug_joss` → 1998; `cinedebug_rice` → 2013; `cooking_start_in` → 231; `cinedebug_rivertabletalk` → 2059; `Start 30` → 3878; `cinedebug_Johnny` → 2109; `Start 32` → 5808; `at_place_in` → 523; `cinedebug_table` → 3620.

Exits: `cooking_start_out` → 232; `arivalterminatingoutput` → 1541; `at_place_out` → 524.

End nodes: 232: `NonTerminating`; 524: `<omitted>`; 1541: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 1743 / 1770 | `/Data/RootChunk/sceneGraph/Data/graph/184/Data/events/1` |
| `scnChangeIdleAnimEvent` | 128 | 95 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnDialogLineEvent` | 130 | 95 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnGameplayTransitionEvent` | 9 | 506 / 392 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/18` |
| `scnIKEvent` | 18 | 506 / 381 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/7` |
| `scnLookAtEvent` | 136 | 115 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 166 | 95 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnUnmountEvent` | 9 | 506 / 397 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/22` |
| `scneventsAttachPropToNode` | 3 | 254 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |
| `scneventsAttachPropToPerformer` | 16 | 254 / 155 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scneventsAttachPropToWorld` | 6 | 259 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |
| `scneventsCameraParamsEvent` | 5 | 2320 / 2142 | `/Data/RootChunk/sceneGraph/Data/graph/254/Data/events/4` |
| `scneventsEquipItemToPerformer` | 3 | 3601 / 2760 | `/Data/RootChunk/sceneGraph/Data/graph/378/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 9 | 506 / 393 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/19` |
| `scneventsSocket` | 125 | 95 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 3601 / 2763 | `/Data/RootChunk/sceneGraph/Data/graph/378/Data/events/9` |
| `scneventsUnequipItemFromPerformerByItem` | 3 | 341 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/4` |
| `scneventsVFXEvent` | 11 | 254 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 18
- skeletal_animation: 18
- speech, skeletal_animation, idle_animation, gaze: 12
- gaze: 11
- speech: 9
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 4
- speech, gaze: 4
- skeletal_animation, idle_animation, socket_signal: 4
- speech, idle_animation, gaze: 3
- speech, idle_animation, gaze, socket_signal: 3
- skeletal_animation, props_equipment, socket_signal: 3
- camera: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, socket_signal: 1
- vfx: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, props_equipment: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, audio: 1
- props_equipment: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `d9b794bba57ca0812901722bd1f7ee30781ef8bbc86eddfca19213ab49135a43`. Binary SHA-256: `8e73bc68a37588c055866d9149c9473ae7a3476fd108aad4cab5195b5d4da7bc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq029\scenes\sq029_02a_arrival.scene" --events
```

## `base\quest\side_quests\sq029\scenes\sq029_03_argame.scene`

1033 graph nodes, 1419 edges; 68 event-bearing sections, 370 events; 123 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: Sobchak_VR (actor 0, spawnSet); Boy_VR (actor 1, spawnSet); Girl_VR (actor 2, spawnSet); Boy (actor 3, spawnSet); Girl (actor 4, spawnSet); Bandit_Leader (actor 5, findInContext); Neighbour (actor 6, spawnSet); Joss (actor 7, spawnSet); Sobchak (actor 8, spawnSet); V (actor 9, findInContext).

Entries: `ar_game_in` → 290; `Cinedebug_guy` → 2370; `cinedebug_Joss` → 2582; `Start 12` → 1722; `Start 14` → 1764.

Exits: `ar_game_out` → 207.

End nodes: 207: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 38 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnDialogLineEvent` | 91 | 5 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 195 / 311 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/16` |
| `scnIKEvent` | 12 | 195 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/9` |
| `scnLookAtEvent` | 72 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPlaySkAnimEvent` | 46 | 125 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/6` |
| `scnPoseCorrectionEvent` | 2 | 132 / 187 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/11` |
| `scnUnmountEvent` | 6 | 195 / 310 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/15` |
| `scneventsAttachPropToNode` | 2 | 606 / 735 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/6` |
| `scneventsAttachPropToPerformer` | 4 | 606 / 730 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 6 | 195 / 306 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/12` |
| `scneventsSocket` | 73 | 125 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scneventsVFXEvent` | 12 | 606 / 731 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 24
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, socket_signal: 4
- speech, gaze: 3
- speech, idle_animation: 3
- skeletal_animation, props_equipment, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze, socket_signal: 2
- skeletal_animation, gaze, vfx, socket_signal: 2
- gaze: 2
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- vfx: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `b199c3b997f0220bf82a3824d9ed2554da03e002452b3d530ed97df37702cfbd`. Binary SHA-256: `f8ade2ac4fbb6367768d261329355321f873e4a4b4636eacfb58e0baa388964e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq029\scenes\sq029_03_argame.scene" --events
```

## `base\quest\side_quests\sq029\scenes\sq029_04a_dinner.scene`

593 graph nodes, 743 edges; 124 event-bearing sections, 1030 events; 259 screenplay lines, 48 screenplay options, 20 choice nodes.

Actors: River (actor 0, spawnSet); Joss (actor 1, spawnSet); kid_boy (actor 2, spawnSet); kid_girl (actor 3, spawnSet); Johnny (actor 4, spawnSet); V (actor 5, findInContext).

Entries: `food_ready_in` → 1; `cinedebug_dinner_ct` → 2774; `post_climb` → 1457; `Cinedebug_start` → 5002; `Start 12` → 5040; `cinedebug_towertop` → 5068; `cinedebug_reachtower` → 1982; `Cinedebug_noboost` → 1986; `cinedebug_gate` → 1549; `to_tower_in` → 388; `johhny_sex_comment_in` → 432.

Exits: `begin_sex_out` → 389; `no_sex_out` → 390; `johhny_sex_comment_out` → 435.

End nodes: 389: `NonTerminating`; 390: `<omitted>`; 435: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 2416 / 2079 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/2` |
| `scnChangeIdleAnimEvent` | 195 | 30 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 207 | 30 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 379 / 405 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/22` |
| `scnIKEvent` | 8 | 379 / 382 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/2` |
| `scnLookAtEvent` | 196 | 30 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 192 | 30 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnPoseCorrectionEvent` | 3 | 379 / 389 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/9` |
| `scnUnmountEvent` | 4 | 379 / 404 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/21` |
| `scneventsAttachPropToNode` | 1 | 1459 / 1738 | `/Data/RootChunk/sceneGraph/Data/graph/142/Data/events/6` |
| `scneventsAttachPropToPerformer` | 14 | 32 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |
| `scneventsAttachPropToWorld` | 4 | 379 / 392 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/12` |
| `scneventsCameraParamsEvent` | 6 | 1140 / 1301 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 4 | 379 / 400 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/18` |
| `scneventsSocket` | 187 | 32 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsVFXEvent` | 4 | 1616 / 1784 | `/Data/RootChunk/sceneGraph/Data/graph/147/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 31
- speech: 12
- speech, skeletal_animation, idle_animation, gaze: 10
- speech, skeletal_animation, idle_animation: 8
- skeletal_animation, idle_animation, gaze, socket_signal: 7
- skeletal_animation, props_equipment, socket_signal: 6
- skeletal_animation: 6
- socket_signal: 5
- skeletal_animation, gaze: 4
- speech, idle_animation, gaze: 3
- camera: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- idle_animation, gaze: 2
- speech, props_equipment: 2
- speech, idle_animation, gaze, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1
- speech, skeletal_animation: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, gaze, camera, props_equipment, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio: 1
- skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- vfx: 1

Raw SHA-256: `239cd422410bf2bb9aee7ba218a42d340bdb1d071686457a88c3421c492f6757`. Binary SHA-256: `508b2e56398f74397197ab579f08190649dd5d8349c39585612cb41f7242cdc6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq029\scenes\sq029_04a_dinner.scene" --events
```

## `base\quest\side_quests\sq029\scenes\sq029_05_morning_after.scene`

318 graph nodes, 370 edges; 66 event-bearing sections, 537 events; 138 screenplay lines, 24 screenplay options, 12 choice nodes.

Actors: River (actor 0, spawnSet); joss (actor 1, spawnSet); Johnny (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `breakfast` → 4; `river_safehouse_interaction_in` → 1699; `cinedebug_romancestart` → 1152; `cinedebug_RiverEnter` → 887; `hangover` → 94; `wake_up` → 102.

Exits: `breakfast_out` → 5; `quest_rewards` → 1118; `hangover_out` → 95; `wake_up_out` → 103; `sq029_Johnny_sex_comment_start` → 1332.

End nodes: 5: `<omitted>`; 95: `<omitted>`; 103: `<omitted>`; 1118: `NonTerminating`; 1332: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 104 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/12` |
| `scnChangeIdleAnimEvent` | 100 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 105 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 8 | 314 / 597 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/8` |
| `scnIKEvent` | 16 | 314 / 589 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/1` |
| `scnLookAtAdvancedEvent` | 4 | 154 / 378 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/3` |
| `scnLookAtEvent` | 70 | 23 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 80 | 8 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPoseCorrectionEvent` | 1 | 1355 / 1376 | `/Data/RootChunk/sceneGraph/Data/graph/177/Data/events/3` |
| `scnUnmountEvent` | 8 | 314 / 596 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/7` |
| `scneventsAttachPropToNode` | 2 | 26 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scneventsAttachPropToPerformer` | 3 | 812 / 931 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/5` |
| `scneventsAttachPropToWorld` | 1 | 1258 / 1227 | `/Data/RootChunk/sceneGraph/Data/graph/151/Data/events/2` |
| `scneventsCameraParamsEvent` | 8 | 104 / 345 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/3` |
| `scneventsEquipItemToPerformer` | 4 | 2055 / 2148 | `/Data/RootChunk/sceneGraph/Data/graph/307/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 8 | 314 / 594 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/6` |
| `scneventsSocket` | 99 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 2 | 2055 / 2150 | `/Data/RootChunk/sceneGraph/Data/graph/307/Data/events/7` |
| `scneventsVFXEvent` | 11 | 8 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 9
- speech, idle_animation, gaze: 5
- skeletal_animation: 5
- speech, idle_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- speech: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- audio: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- camera, vfx: 1
- camera, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- idle_animation, gaze, vfx, socket_signal: 1
- idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- audio, socket_signal: 1

Raw SHA-256: `5675e3a9b2ddf520b268c43b91ccbf1a41dab2e24e1d9d8603eb76d9284a2661`. Binary SHA-256: `5000f6f173b9284043830e51e12a8ca8891129b6d29545138754861574e87e1b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq029\scenes\sq029_05_morning_after.scene" --events
```

## `base\quest\side_quests\sq029\scenes\sq029_06a_sex.scene`

82 graph nodes, 88 edges; 6 event-bearing sections, 261 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: river (actor 0, spawnSet); playerTPP (actor 1, spawnDespawn); Girl (actor 2, spawnSet); Boy (actor 3, spawnSet); BoringGuy (actor 4, spawnDespawn); SmokingLady (actor 5, spawnDespawn); V_Impostor (actor 6, spawnDespawn); V (actor 7, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 29 | 13 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scnChangeIdleAnimEvent` | 5 | 13 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scnLookAtEvent` | 7 | 13 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/19` |
| `scnPlayRidAnimEvent` | 25 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 136 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraParamsEvent` | 2 | 353 / 921 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/4` |
| `scneventsPlayRidCameraAnimEvent` | 25 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 17 | 13 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsVFXEvent` | 15 | 4 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, gaze, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 2
- skeletal_animation, rid_actor, camera, rid_camera, vfx: 1
- skeletal_animation, gaze, camera, audio, vfx, socket_signal: 1
- idle_animation, camera: 1
- audio, vfx: 1

Raw SHA-256: `56b86b589767d366466326ef35d92aba5d77dcaec22c27e140be1371117ac190`. Binary SHA-256: `0bad68fc103aeebcb3e81964e9fd3d838e96cb1990c1375c0a056f55ee925535`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq029\scenes\sq029_06a_sex.scene" --events
```

