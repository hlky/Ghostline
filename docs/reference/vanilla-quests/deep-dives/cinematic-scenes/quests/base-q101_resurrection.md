# Playing for Time: scene presentation

Journal identity: `quests/main_quest/act_01/q101_resurrection`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q101_resurrection.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q101\scenes\q101_01_covered_in_trash.scene`

146 graph nodes, 166 edges; 32 event-bearing sections, 183 events; 19 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: takemura (actor 0, spawnSet); dex (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `vista_in` → 15; `Start 2` → 717.

Exits: `vista_out` → 16.

End nodes: 16: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 42 | 17 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnChangeIdleAnimEvent` | 10 | 17 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnGameplayTransitionEvent` | 1 | 686 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/7` |
| `scnIKEvent` | 2 | 686 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/1` |
| `scnLookAtEvent` | 3 | 525 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnPlaySkAnimEvent` | 36 | 17 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 686 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/6` |
| `scneventsCameraParamsEvent` | 5 | 978 / 413 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 1 | 686 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/5` |
| `scneventsSocket` | 64 | 17 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsVFXEvent` | 18 | 17 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, audio, socket_signal: 12
- skeletal_animation, audio, vfx, socket_signal: 5
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation: 2
- camera: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- camera, vfx: 1
- socket_signal: 1
- vfx: 1
- skeletal_animation, idle_animation, camera, socket_signal: 1

Raw SHA-256: `cdc241e2db105d8d93f0557cfc5df4fef050d27269f5bdd8afbf9f563a9d2aa9`. Binary SHA-256: `6fa57cb47ac3dc9b4fdff5d35e3f83e0af763563083353a346a7b26d64296ed2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_01_covered_in_trash.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_02_vision_and_sobchuk.scene`

70 graph nodes, 77 edges; 10 event-bearing sections, 146 events; 14 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Takemura (actor 0, spawnSet); dex (actor 1, spawnSet); johnny (actor 2, spawnDespawn); takemura_car (actor 3, spawner); V (actor 4, findInContext).

Entries: `part1_in` → 1; `q101_08_takemura_hmm_start` → 980; `q101_return_to_landfill_in` → 1077; `new` → 776.

Exits: `q101_08_takemura_hmm_end` → 981; `part1_out` → 284; `q101_return_to_landfill_out` → 1084.

End nodes: 284: `<omitted>`; 981: `<omitted>`; 1084: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 324 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnChangeIdleAnimEvent` | 5 | 324 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 13 | 324 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/20` |
| `scnGameplayTransitionEvent` | 3 | 883 / 270 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/9` |
| `scnIKEvent` | 10 | 334 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scnLookAtEvent` | 21 | 324 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 18 | 324 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 3 | 883 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/8` |
| `scneventsAttachPropToPerformer` | 1 | 324 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/28` |
| `scneventsAttachPropToWorld` | 1 | 324 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/42` |
| `scneventsEquipItemToPerformer` | 1 | 1082 / 462 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 4 | 334 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsSocket` | 30 | 324 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsVFXEvent` | 24 | 324 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `f1532f22df2eb586f82682f4fe5e725966a4d25f8bd6a54164bae9f8026a3cb9`. Binary SHA-256: `4d91adf27036ff4f49a3fe69109487c5928360fe975ff4718a35775b43915685`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_02_vision_and_sobchuk.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_03_car_ride.scene`

414 graph nodes, 507 edges; 38 event-bearing sections, 586 events; 45 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Takemura (actor 0, spawnSet); Johnny (actor 1, spawnSet); troy1 (actor 2, spawnSet); troy2 (actor 3, spawnSet); troy3 (actor 4, spawnSet); cabrio (actor 5, spawnSet); troy_bike1 (actor 6, community); troy_bike2 (actor 7, community); troy_bike3 (actor 8, community); archer_01 (actor 9, community); archer_02 (actor 10, community); archer_03 (actor 11, community); thorton_colby_01 (actor 12, community); thorton_colby_02 (actor 13, community); thorton_colby_03 (actor 14, community); thorton_colby_04 (actor 15, community); villefort_cortes_01 (actor 16, community); villefort_cortes_02 (actor 17, community); thorton_mackinaw_01 (actor 18, community); chevalier_thrax_01 (actor 19, community); chevalier_thrax_02 (actor 20, community); kaukaz_bratsk_01 (actor 21, community); kaukaz_zeya_01 (actor 22, community); kaukaz_zeya_02 (actor 23, community); mahir_supron_01 (actor 24, community); mahir_supron_02 (actor 25, community); kaukaz_zeya_03 (actor 26, community); thorton_galena_01 (actor 27, community); thorton_galena_02 (actor 28, community); villefort_columbus_01 (actor 29, community); quadra_type66_01 (actor 30, community); kaukaz_bratsk_02 (actor 31, community); kaukaz_bratsk_03 (actor 32, community); thorton_mackinaw_02 (actor 33, community); thorton_mackinaw_03 (actor 34, community); villefort_alvarado_01 (actor 35, community); columbus_traffic_1st_pat_01 (actor 36, community); zeya_traffic_1st_part_01 (actor 37, community); V (actor 38, findInContext).

Entries: `main_in` → 1; `Start 22` → 10728; `Start 21` → 9986; `180_turn_in` → 287; `preview_last_seq` → 2264.

Exits: `troy1_jump_out` → 293.

End nodes: 293: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 57 | 3 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnChangeIdleAnimEvent` | 8 | 600 / 617 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/0` |
| `scnDialogLineEvent` | 16 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 12 | 8 / 224 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/133` |
| `scnIKEvent` | 26 | 8 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/107` |
| `scnPlaySkAnimEvent` | 139 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 2 | 1162 / 1197 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/4` |
| `scneventsAttachPropToPerformer` | 10 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsAttachPropToWorld` | 4 | 8 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/47` |
| `scneventsCameraParamsEvent` | 9 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 23 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 97 | 3 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsVFXEvent` | 183 | 8 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- vfx: 15
- skeletal_animation, audio, vfx: 3
- speech: 2
- skeletal_animation, idle_animation, vfx, socket_signal: 2
- speech, skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state: 2
- speech, skeletal_animation, camera, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- speech, vfx: 1
- skeletal_animation, idle_animation, camera, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, camera, audio, socket_signal, animation_state: 1
- skeletal_animation, audio: 1
- audio, vfx, socket_signal: 1

Raw SHA-256: `45cdf25f302f53a1b130c6a71a87d06f8f3c8307e20a9896e04f8c00917e8908`. Binary SHA-256: `059381df301edb93c588bddc312af5670e6bc591d0f14ee6d3d0448721a83872`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_03_car_ride.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_05_after_crash.scene`

81 graph nodes, 88 edges; 20 event-bearing sections, 129 events; 33 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: takemura (actor 0, spawnSet); delamain (actor 1, spawnSet); troy (actor 2, spawnSet); cabrio (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `blackout_in` → 234; `aft_crash_in` → 245.

Exits: `blackout_out` → 235; `aft_crash_out` → 247.

End nodes: 235: `<omitted>`; 247: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 13 | 418 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/9` |
| `scnChangeIdleAnimEvent` | 4 | 418 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/3` |
| `scnDialogLineEvent` | 25 | 236 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 17 | 290 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnPlaySkAnimEvent` | 18 | 290 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsAttachPropToPerformer` | 3 | 418 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/11` |
| `scneventsCameraParamsEvent` | 3 | 418 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/5` |
| `scneventsSocket` | 28 | 290 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsVFXEvent` | 18 | 290 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, vfx: 1
- vfx: 1
- skeletal_animation, gaze: 1
- skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1

Raw SHA-256: `37b4549af1431aefa8f392ebf982393fe0e69c23d2323cce7a6cac09765fec5d`. Binary SHA-256: `125e3606377d569d6e88f784c544d62b45f2574469d685a30d9167f3f7eadd84`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_05_after_crash.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_06_delamain_ride.scene`

33 graph nodes, 34 edges; 2 event-bearing sections, 39 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: delamain (actor 0, spawnSet); takemura (actor 1, spawnSet); delamain_wheels (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 4 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/19` |
| `scnChangeIdleAnimEvent` | 1 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnDialogLineEvent` | 11 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 3 | 4 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/16` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 5 | 4 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsAttachPropToPerformer` | 1 | 4 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsCameraParamsEvent` | 2 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 3 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 4 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 5 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal, animation_state, mount_workspot: 1
- speech: 1

Raw SHA-256: `37e8b81705df71764cc678b903fd0b83ed26825c84aa522c77d812fad669c589`. Binary SHA-256: `df50b74652957d1c558f56b0e88149fa56fd962f1bc949cf463e78743bc689ea`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_06_delamain_ride.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_07_ripperdoc.scene`

236 graph nodes, 257 edges; 39 event-bearing sections, 502 events; 98 screenplay lines, 18 screenplay options, 8 choice nodes.

Actors: Viktor (actor 0, spawnSet); Takemura (actor 1, spawnSet); Delamain (actor 2, findInContext); misty (actor 3, spawnSet); delamain_cab (actor 4, spawnSet); wheelchair (actor 5, community); V (actor 6, findInContext).

Entries: `garage_decision_in` → 508; `Start 12` → 1901; `Start 11` → 1608; `garage2_in` → 490; `garage1_in` → 497.

Exits: `garage_decision_out` → 509; `garage2_out` → 488; `garage1_out` → 498.

End nodes: 488: `<omitted>`; 498: `<omitted>`; 509: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 22 | 499 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnChangeIdleAnimEvent` | 15 | 499 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 92 | 499 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnGameplayTransitionEvent` | 3 | 1245 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |
| `scnIKEvent` | 6 | 1245 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnLookAtEvent` | 103 | 507 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/13` |
| `scnPlaySkAnimEvent` | 111 | 499 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnPoseCorrectionEvent` | 1 | 1388 / 880 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/4` |
| `scnUnmountEvent` | 3 | 1245 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/9` |
| `scneventsCameraParamsEvent` | 11 | 499 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 3 | 1245 / 198 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/8` |
| `scneventsSocket` | 95 | 499 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsVFXEvent` | 37 | 499 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 12
- speech: 6
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, camera, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- gaze, socket_signal: 1
- socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, camera, audio, vfx, socket_signal: 1

Raw SHA-256: `a3feef79b24a63bd1ed327fe54ac29b367b7dc23ab6c9407a82f7227f3b185da`. Binary SHA-256: `69eec42d39613aef3dd949c3c853e45f280c20ffbc42cd87c603ab1a334ea59f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_07_ripperdoc.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_07b_whiteroom.scene`

77 graph nodes, 92 edges; 8 event-bearing sections, 46 events; 8 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `whiteroom` → 7; `Start 1` → 115.

Exits: `whiteroom_out` → 8.

End nodes: 8: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 9 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnChangeIdleAnimEvent` | 1 | 9 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 1 | 9 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnLookAtEvent` | 7 | 9 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 13 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 14 | 9 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsVFXEvent` | 4 | 9 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, audio, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- gaze, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- vfx: 1

Raw SHA-256: `401bb95fc4ab620a3113c4ca0ead6927f4c89cfbd28c3d9e152f2f54de288918`. Binary SHA-256: `140f4614d37e57eba1c87868f2e73982cb7c95052461c613ee270ac1bb00d741`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_07b_whiteroom.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_07c_johnny_triggers.scene`

299 graph nodes, 357 edges; 46 event-bearing sections, 502 events; 118 screenplay lines, 17 screenplay options, 10 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); misty (actor 1, spawnSet); stanley_media (actor 2, findInContext); V_tpp_male (actor 3, spawnDespawn); V_tpp_female (actor 4, spawnDespawn); wheelchair (actor 5, community); Player (actor 6, findInContext).

Entries: `johnny_triggers` → 1; `misty_goto_sleep_in` → 598; `q101_stanley_lines_in` → 2487; `Start 4` → 2742.

Exits: `johnny_triggers_out` → 2; `misty_goto_sleep_out` → 599; `q101_stanley_lines_out` → 2497.

End nodes: 2: `<omitted>`; 599: `NonTerminating`; 2497: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 61 | 68 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scnChangeIdleAnimEvent` | 37 | 20 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnDialogLineEvent` | 99 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 1261 / 654 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/23` |
| `scnIKEvent` | 6 | 1261 / 651 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/20` |
| `scnLookAtEvent` | 43 | 7 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scnPlaySkAnimEvent` | 97 | 7 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |
| `scnUnmountEvent` | 3 | 1261 / 653 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/22` |
| `scneventsAttachPropToNode` | 2 | 68 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/19` |
| `scneventsAttachPropToPerformer` | 6 | 68 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scneventsAttachPropToWorld` | 8 | 68 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/20` |
| `scneventsCameraParamsEvent` | 6 | 600 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 4 | 1261 / 648 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/18` |
| `scneventsSocket` | 97 | 7 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsVFXDurationEvent` | 2 | 2734 / 1849 | `/Data/RootChunk/sceneGraph/Data/graph/212/Data/events/5` |
| `scneventsVFXEvent` | 28 | 7 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech: 3
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- skeletal_animation: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1
- props_equipment, vfx: 1
- skeletal_animation, props_equipment, audio, vfx: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, socket_signal: 1
- camera, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1

Raw SHA-256: `35d7a0d0d2a14a6727bc025965839cee5d8cd10c414b837988b3dede9a2b398d`. Binary SHA-256: `9f9ced6db8100f5949220eb3b20b374d68766df396aed05b2c4cbf5eed88cc30`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_07c_johnny_triggers.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_08_takemura_v_room.scene`

325 graph nodes, 381 edges; 84 event-bearing sections, 801 events; 243 screenplay lines, 49 screenplay options, 16 choice nodes.

Actors: takemura (actor 0, spawnSet); takemura_phone (actor 1, spawnSet); Tom (actor 2, community); Johnny (actor 3, spawnDespawn); toms_client6 (actor 4, community); suit1 (actor 5, community); suit2 (actor 6, community); client1 (actor 7, community); client2 (actor 8, community); client3 (actor 9, community); client4 (actor 10, community); client5 (actor 11, community); lady (actor 12, community); customer7 (actor 13, community); waitress (actor 14, community); v (actor 15, findInContext).

Entries: `v_flat_in` → 1; `call_in` → 45; `cup_in` → 2031; `Start 4` → 758; `q112_takemura_clone` → 1462.

Exits: `v_flat_out` → 2; `call_out` → 46; `End 4` → 1464.

End nodes: 2: `NonTerminating`; 46: `<omitted>`; 1464: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 18 | 69 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scnChangeIdleAnimEvent` | 31 | 69 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnDialogLineEvent` | 158 | 47 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnGameplayTransitionEvent` | 11 | 105 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/20` |
| `scnIKEvent` | 22 | 105 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/13` |
| `scnLookAtAdvancedEvent` | 1 | 202 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scnLookAtEvent` | 156 | 47 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 188 | 66 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnPoseCorrectionEvent` | 10 | 105 / 203 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/22` |
| `scnUnmountEvent` | 11 | 105 / 195 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/19` |
| `scneventsAttachPropToPerformer` | 7 | 69 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsAttachPropToWorld` | 3 | 173 / 267 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/6` |
| `scneventsCameraParamsEvent` | 3 | 69 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 11 | 105 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/16` |
| `scneventsSocket` | 170 | 66 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1337 / 2272 | `/Data/RootChunk/sceneGraph/Data/graph/201/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 15
- skeletal_animation, gaze: 11
- skeletal_animation: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- skeletal_animation, gaze, socket_signal: 4
- speech: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation: 2
- speech, gaze, socket_signal: 2
- idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `319646b526930fecabfd3ac649c1272da642c5e0eaea6af9745144f189e363d4`. Binary SHA-256: `56b99f3de7037c8bf46a0c76b2233fb932fd0463575c604e457e90401b8e4750`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_08_takemura_v_room.scene" --events
```

