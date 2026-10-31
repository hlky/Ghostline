# Balls to the Wall: scene presentation

Journal identity: `ep1/quests/minor_quest/mq301_bomb`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-mq301_bomb.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_outside_voodoboys_chat.scene`

4 graph nodes, 4 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Voodoboy_2 (actor 0, community); Voodoboy_1 (actor 1, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `614e76e262f2132cb9a562b134b2e7cb778a31e22c1af1f937308f90c0948274`. Binary SHA-256: `8f7fa97b28704d44e41e1f25d4ea623b6a61c9348e5e9268c1fac7584d421a04`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_outside_voodoboys_chat.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_voodoboys_reception_argue_scene.scene`

3 graph nodes, 2 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Voodoboy_upper (actor 0, community); Voodoboy_down (actor 1, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `89a117591dd76882782b60e0170c8ecc76f2d52431e12320b72901fc946ca249`. Binary SHA-256: `4e3954012b0bf1a30c54e2f10518f92883f6e27963dbdaa353f19dd13e7b6dc3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_voodoboys_reception_argue_scene.scene" --events
```

## `ep1\quest\minor_quests\mq301\scenes\mq301_01_fireplace.scene`

269 graph nodes, 307 edges; 55 event-bearing sections, 834 events; 83 screenplay lines, 20 screenplay options, 9 choice nodes.

Actors: Paco (actor 0, spawnSet); Babs (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `potentialreuse` → 1416; `mq301_01_fireplace_in` → 67; `mq301_01_anticipation_chat_in` → 768; `movedline` → 1925; `floating_preview` → 1987.

Exits: `mq301_01_fireplace_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 384 / 621 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/5` |
| `scnChangeIdleAnimEvent` | 36 | 40 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnDialogLineEvent` | 70 | 25 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayTransitionEvent` | 3 | 25 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/29` |
| `scnIKEvent` | 6 | 25 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/24` |
| `scnLookAtEvent` | 221 | 25 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnOverridePhantomParamsEvent` | 2 | 866 / 1434 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/1` |
| `scnPlaySkAnimEvent` | 253 | 25 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 25 | 25 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 3 | 25 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/25` |
| `scneventsAttachPropToNode` | 2 | 384 / 619 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/3` |
| `scneventsAttachPropToPerformer` | 36 | 25 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsAttachPropToWorld` | 28 | 25 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/19` |
| `scneventsCameraParamsEvent` | 2 | 613 / 1028 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 3 | 25 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/23` |
| `scneventsSocket` | 97 | 25 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsVFXDurationEvent` | 9 | 226 / 266 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/18` |
| `scneventsVFXEvent` | 33 | 226 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/17` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- speech: 9
- gaze: 6
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- vfx: 1

Raw SHA-256: `2b6fad74ec65556726301e1833d7c8251560027fdda4bd33bf415608858cb8c4`. Binary SHA-256: `76b1f27586c661e125e6e8a8f611ac9bc131cca2762d2e36ccec7920d75efec3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq301\scenes\mq301_01_fireplace.scene" --events
```

## `ep1\quest\minor_quests\mq301\scenes\mq301_02_initiation.scene`

847 graph nodes, 953 edges; 84 event-bearing sections, 563 events; 90 screenplay lines, 17 screenplay options, 11 choice nodes.

Actors: Paco (actor 0, spawnSet); Babs (actor 1, spawnSet); Jurij (actor 2, spawnSet); Kruger (actor 3, spawnSet); Rinder (actor 4, spawner); Dodger (actor 5, spawner); Johnny (actor 6, spawnDespawn); Bennet (actor 7, spawner); Soldier_29 (actor 8, community); Boulder (actor 9, spawner); Jago (actor 10, spawner); Paco_off (actor 11, findInContext); Babs_off (actor 12, findInContext); Kurt_mirror (actor 13, spawnDespawn); Soldier_32 (actor 14, community); Soldier_01 (actor 15, community); Soldier_02 (actor 16, community); Soldier_03 (actor 17, community); Soldier_04 (actor 18, community); Soldier_05 (actor 19, community); Soldier_06 (actor 20, community); Soldier_07 (actor 21, community); Soldier_08 (actor 22, community); Soldier_09 (actor 23, community); Soldier_10 (actor 24, community); Soldier_11 (actor 25, community); Soldier_12 (actor 26, community); Soldier_13 (actor 27, community); Soldier_14 (actor 28, community); Soldier_16 (actor 29, community); Soldier_17 (actor 30, community); Soldier_18 (actor 31, community); Soldier_19 (actor 32, community); Soldier_20 (actor 33, community); Soldier_21 (actor 34, community); Soldier_22 (actor 35, community); Soldier_24 (actor 36, community); Soldier_26 (actor 37, community); Soldier_31 (actor 38, community); Soldier_33 (actor 39, community); Soldier_34 (actor 40, community); Patrol_1 (actor 41, community); Patrol_2 (actor 42, community); Patrol_3 (actor 43, community); Patrol_4 (actor 44, community); Patrol_5 (actor 45, community); Soldier_36 (actor 46, community); Soldier_37 (actor 47, community); Soldier_39 (actor 48, community); Soldier_43 (actor 49, community); Soldier_44 (actor 50, community); Soldier_46 (actor 51, community); Soldier_48 (actor 52, community); Soldier_49 (actor 53, community); Soldier_50 (actor 54, community); Player (actor 55, findInContext); Kurt (actor 56, findInContext).

Entries: `mq301_02_initiation_in` → 1; `Start 3` → 2166; `pacolinestouse` → 3855.

Exits: `mq301_02_initiation_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 73 / 289 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/5` |
| `scnChangeIdleAnimEvent` | 21 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 79 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 6 | 10 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/20` |
| `scnIKEvent` | 12 | 10 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scnLookAtEvent` | 113 | 10 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnPlaySkAnimEvent` | 132 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 9 | 24 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnUnmountEvent` | 6 | 10 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/19` |
| `scneventsAttachPropToNode` | 2 | 395 / 616 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/0` |
| `scneventsAttachPropToPerformer` | 9 | 414 / 666 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/9` |
| `scneventsAttachPropToWorld` | 1 | 4103 / 4421 | `/Data/RootChunk/sceneGraph/Data/graph/616/Data/events/7` |
| `scneventsCameraParamsEvent` | 9 | 2175 / 2398 | `/Data/RootChunk/sceneGraph/Data/graph/320/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 6 | 10 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsSocket` | 130 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXDurationEvent` | 2 | 3391 / 3913 | `/Data/RootChunk/sceneGraph/Data/graph/537/Data/events/20` |
| `scneventsVFXEvent` | 20 | 73 / 286 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- speech, skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- gaze: 6
- skeletal_animation, socket_signal: 5
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation: 2
- speech, socket_signal: 2
- gaze, socket_signal: 2
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- vfx: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, gaze, audio, vfx, socket_signal, animation_state: 1
- props_equipment, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, gaze: 1
- idle_animation, socket_signal: 1
- idle_animation, gaze, socket_signal, animation_state: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- camera, props_equipment, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, camera, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, camera: 1

Raw SHA-256: `2d9c3f49751d7c0928342cd8ea16ee7c5edfe11f1e75621d53304d648e5c7f5a`. Binary SHA-256: `0a9ca0bb3feb88e2b76e6a9a99c7f5a2b3178ec4d57effa9c2ed082768b9b46e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq301\scenes\mq301_02_initiation.scene" --events
```

## `ep1\quest\minor_quests\mq301\scenes\mq301_03_delivery.scene`

1390 graph nodes, 1600 edges; 72 event-bearing sections, 679 events; 82 screenplay lines, 16 screenplay options, 10 choice nodes.

Actors: Paco (actor 0, spawnSet); Babs (actor 1, spawnSet); Jurij (actor 2, spawnSet); Kruger (actor 3, spawnSet); Johnny (actor 4, spawnDespawn); Captive (actor 5, spawner); Paco_off (actor 6, findInContext); Babs_off (actor 7, findInContext); kurt_car (actor 8, spawner); Player (actor 9, findInContext); Kurt (actor 10, findInContext).

Entries: `mq301_03_delivery_in` → 1; `mq301_03_talk_paco_in` → 5815; `mq301_03_talk_babs_in` → 5817; `mq301_03_onit_in` → 3147; `mq301_03_drink_in` → 3162; `mq301_03_our_contacts_in` → 4657; `Start 11` → 4717; `Start 12` → 4720; `notused` → 8798; `mq301_03_final_shot_in` → 6217; `Back in tent after delivery` → 7686.

Exits: `mq301_03_talk_paco_out` → 5816; `mq301_03_talk_babs_out` → 5819; `mq301_03_onit_out` → 3148; `mq301_03_drink_out` → 3164; `mq301_03_delivery_out` → 742; `mq301_03_final_shot_out` → 6218; `mq301_03_our_contacts_out` → 6229.

End nodes: 742: `NonTerminating`; 3148: `<omitted>`; 3164: `<omitted>`; 5816: `<omitted>`; 5819: `<omitted>`; 6218: `<omitted>`; 6229: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 662 / 545 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/12` |
| `scnChangeIdleAnimEvent` | 33 | 14 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scnDialogLineEvent` | 70 | 14 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 625 / 468 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/6` |
| `scnIKEvent` | 16 | 621 / 427 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/0` |
| `scnLookAtEvent` | 236 | 14 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 191 | 14 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPoseCorrectionEvent` | 14 | 14 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/28` |
| `scnUnmountEvent` | 4 | 4605 / 3218 | `/Data/RootChunk/sceneGraph/Data/graph/411/Data/events/7` |
| `scneventsAttachPropToPerformer` | 6 | 14 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/22` |
| `scneventsAttachPropToWorld` | 4 | 14 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/41` |
| `scneventsCameraParamsEvent` | 1 | 8818 / 6185 | `/Data/RootChunk/sceneGraph/Data/graph/904/Data/events/1` |
| `scneventsEquipItemToPerformer` | 3 | 660 / 486 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 5 | 625 / 463 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |
| `scneventsSocket` | 71 | 14 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/54` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1817 / 1481 | `/Data/RootChunk/sceneGraph/Data/graph/152/Data/events/15` |
| `scneventsVFXDurationEvent` | 4 | 14 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/46` |
| `scneventsVFXEvent` | 11 | 14 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/31` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 22
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- gaze: 6
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 2
- vfx, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, socket_signal, animation_state: 1
- speech, idle_animation, ik, gameplay_transition, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, socket_signal: 1
- gaze, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- vfx: 1
- skeletal_animation, camera, socket_signal: 1
- speech, idle_animation: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- props_equipment: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `fc86292470246d45a2c039865bafa2a72cbb9b3a73b92004ee2d5a0eecf6cc85`. Binary SHA-256: `2b13a188e32120eda5512a04962cc24c619ef94933ba67786062eec0b1dd471b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq301\scenes\mq301_03_delivery.scene" --events
```

## `ep1\quest\minor_quests\mq301\scenes\mq301_04_frame.scene`

222 graph nodes, 244 edges; 27 event-bearing sections, 176 events; 22 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Paco (actor 0, spawnSet); Babs (actor 1, spawnSet); Kurt (actor 2, spawnSet); Jurij (actor 3, spawnSet); Kruger (actor 4, spawnSet); Johnny (actor 5, spawnDespawn); Player (actor 6, findInContext).

Entries: `paco_body_preview` → 3052; `mq301_04_frame_in` → 45.

Exits: `mq301_04_frame_out` → 46; `mq301_04_frame_kill_out` → 2682.

End nodes: 46: `NonTerminating`; 2682: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 47 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scnChangeIdleAnimEvent` | 6 | 1902 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnDialogLineEvent` | 20 | 47 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 47 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scnIKEvent` | 4 | 47 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 32 | 47 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnOverridePhantomParamsEvent` | 6 | 2832 / 715 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/1` |
| `scnPlaySkAnimEvent` | 42 | 47 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 4 | 1945 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/3` |
| `scnUnmountEvent` | 2 | 47 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/17` |
| `scneventsEquipItemToPerformer` | 7 | 1945 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 2 | 47 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsSocket` | 42 | 47 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsUnequipItemFromPerformer` | 3 | 1945 / 198 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scneventsVFXEvent` | 2 | 1837 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- skeletal_animation, gaze, socket_signal, animation_state: 5
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- gaze: 1

Raw SHA-256: `31eb86dcb03c30c8a9d546e783beb78e765cf05b5459b55346a9db244b866d9a`. Binary SHA-256: `0f48ae0630cb9dd06f01a442bacdb0125a758ac80699779d744f89c092de9549`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq301\scenes\mq301_04_frame.scene" --events
```

## `ep1\quest\minor_quests\mq301\scenes\mq301_05_run.scene`

307 graph nodes, 346 edges; 38 event-bearing sections, 274 events; 35 screenplay lines, 8 screenplay options, 6 choice nodes.

Actors: Paco (actor 0, spawnSet); Babs (actor 1, spawnSet); Kurt (actor 2, spawnSet); Jurij (actor 3, spawnSet); Kruger (actor 4, spawnSet); Johnny (actor 5, spawnDespawn); mq301_paco_transport_car (actor 6, spawner); Player (actor 7, findInContext).

Entries: `mq301_05_postrun_in` → 31; `potentialreuse` → 4588; `mq301_05_run_in` → 2059; `for_preview` → 4195; `mq301_05_lay_low_in` → 3080.

Exits: `mq301_05_postrun_out` → 32; `mq301_05_run_out` → 2184; `mq301_05_lay_low_out` → 3081.

End nodes: 32: `NonTerminating`; 2184: `NonTerminating`; 3081: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 2060 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/12` |
| `scnDialogLineEvent` | 34 | 2060 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scnGameplayTransitionEvent` | 4 | 2060 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnIKEvent` | 8 | 2060 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnLookAtEvent` | 71 | 2060 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnOverridePhantomParamsEvent` | 1 | 3477 / 990 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/1` |
| `scnPlaySkAnimEvent` | 64 | 2060 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scnPoseCorrectionEvent` | 4 | 2060 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/17` |
| `scnUnmountEvent` | 4 | 2060 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsEquipItemToPerformer` | 2 | 2178 / 215 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/32` |
| `scneventsSetAnimFeatureEvent` | 7 | 2060 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsSocket` | 58 | 2060 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 2178 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/33` |
| `scneventsVFXDurationEvent` | 1 | 2178 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/7` |
| `scneventsVFXEvent` | 4 | 2318 / 356 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, gaze: 2
- speech, skeletal_animation: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze, socket_signal, animation_state: 1
- socket_signal, animation_state: 1
- gaze: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze: 1
- speech, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `d428d4288d3828b6b1480ca277acf079015f1c3de106f2c5435b2a872d54c696`. Binary SHA-256: `32ebb7245a4549a64c1cd1548da09a42c0353de5c7a13db9fef8b4fecd91a00d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq301\scenes\mq301_05_run.scene" --events
```

## `ep1\quest\minor_quests\mq301\scenes\mq301_06_contacts.scene`

125 graph nodes, 146 edges; 12 event-bearing sections, 110 events; 15 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: Paco (actor 0, spawnSet); Babs (actor 1, spawnSet); Kurt (actor 2, spawnSet); Jurij (actor 3, spawnSet); Kruger (actor 4, spawnSet); Johnny (actor 5, spawnDespawn); Player (actor 6, findInContext).

Entries: `mq301_river_decal_in` → 3357; `Start1` → 3385; `mq301_06_contacts_reward_in` → 3278; `mq301_06_guards_in` → 2324; `mq301_06_contacts_in` → 2244.

Exits: `mq301_06_contacts_reward_kill_out` → 3329; `mq301_river_decal_out` → 3358; `mq301_06_contacts_kill_out` → 3258; `mq301_06_contacts_reward_out` → 3279; `mq301_06_guards_out` → 2325; `mq301_06_contacts_out` → 2245.

End nodes: 2245: `NonTerminating`; 2325: `<omitted>`; 3258: `<omitted>`; 3279: `NonTerminating`; 3329: `<omitted>`; 3358: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 2252 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnDialogLineEvent` | 11 | 2249 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 29 | 2249 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 1 | 3263 / 336 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/1` |
| `scnPlaySkAnimEvent` | 30 | 2252 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnPoseCorrectionEvent` | 3 | 3263 / 338 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/3` |
| `scneventsSocket` | 28 | 2249 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsVFXDurationEvent` | 1 | 3656 / 630 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- gaze: 2
- speech, gaze, socket_signal: 1
- speech: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- animation_state: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1

Raw SHA-256: `4dd37bc442138d4277b12ffc90cf8711f69f45d69657bf84a8fc284edf07f9d6`. Binary SHA-256: `e6b9baecde42b2e15843b86e257eb6efbcb5f78274c8444113b69eba268ebff5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq301\scenes\mq301_06_contacts.scene" --events
```

