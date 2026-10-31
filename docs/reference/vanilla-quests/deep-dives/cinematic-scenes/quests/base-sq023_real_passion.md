# They Won't Go When I Go: scene presentation

Journal identity: `quests/side_quest/sq023_real_passion`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq023_real_passion.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq023\scenes\sq023_01_hook.scene`

231 graph nodes, 283 edges; 41 event-bearing sections, 228 events; 69 screenplay lines, 13 screenplay options, 7 choice nodes.

Actors: Rachel (actor 0, spawnSet); Vasquez (actor 1, spawnSet); Joshua (actor 2, spawnSet); Wakako_fixer (actor 3, findInContext); Bill_jablonsky (actor 4, spawnSet); Truck_driver (actor 5, spawnSet); Johnny (actor 6, spawnDespawn); bills_truck (actor 7, spawnSet); Cargo_truck (actor 8, spawnSet); limo (actor 9, spawnSet); V (actor 10, findInContext).

Entries: `chase_start_in` → 482; `chicken_car_in` → 2590; `at_place_in_2` → 1908; `chase_banter` → 310; `car_fail_in` → 1266; `Start 14` → 2031; `bill_meeting_in` → 4382; `at_place_in` → 1125; `sq023_pedestrians_1` → 4440; `sq023_pedestrians_2` → 4441.

Exits: `chase_start_out` → 483; `at_place_out_2` → 1910; `bill_meeting_out` → 309; `chase_banter_out` → 311; `distance_out` → 1263; `car_fail_out` → 1267; `v_in_car_out` → 1377.

End nodes: 309: `NonTerminating`; 311: `<omitted>`; 483: `<omitted>`; 1263: `NonTerminating`; 1267: `<omitted>`; 1377: `NonTerminating`; 1910: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 1003 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/6` |
| `scnChangeIdleAnimEvent` | 11 | 992 / 163 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/10` |
| `scnDialogLineEvent` | 56 | 316 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnGameplayActionEvent` | 2 | 1989 / 808 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 2202 / 992 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/8` |
| `scnIKEvent` | 4 | 2202 / 987 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/3` |
| `scnLookAtEvent` | 46 | 316 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 37 | 316 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 1 | 2202 / 996 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/11` |
| `scneventsAttachPropToPerformer` | 1 | 1664 / 612 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 1003 / 218 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 16 | 316 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsSocket` | 41 | 316 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsVFXEvent` | 2 | 1127 / 352 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- gaze: 5
- speech, skeletal_animation, gaze, socket_signal, animation_state: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, gaze, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, idle_animation, gaze: 1
- idle_animation, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, audio: 1
- skeletal_animation, vfx, socket_signal: 1
- idle_animation, gameplay_action: 1
- socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, audio, socket_signal, animation_state: 1
- ik, gameplay_transition, socket_signal, animation_state: 1

Raw SHA-256: `2792efb6a7306de4979e64ec37f91e8c1e19e78d7dae58ee56f70a511ef929cf`. Binary SHA-256: `fb150b0b5b0a55522e89c818ffeb7036b886f94e22b0c2f2e1e87afc80921e12`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq023\scenes\sq023_01_hook.scene" --events
```

## `base\quest\side_quests\sq023\scenes\sq023_02_ride_gloria.scene`

228 graph nodes, 310 edges; 40 event-bearing sections, 362 events; 89 screenplay lines, 23 screenplay options, 9 choice nodes.

Actors: Joshua (actor 0, spawnSet); Vasquez (actor 1, spawnSet); Rachel (actor 2, spawnSet); Emperor (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `cartalk1_in` → 1; `car_talk_2_in` → 193; `Test` → 806.

Exits: `car_talk_2_out` → 194; `cartalk1_out` → 304.

End nodes: 194: `NonTerminating`; 304: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 30 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnDialogLineEvent` | 80 | 3 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnLookAtEvent` | 125 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 769 / 1031 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/2` |
| `scnPlaySkAnimEvent` | 42 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 35 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsSocket` | 48 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 18
- gaze: 7
- speech, gaze: 4
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `15be8d031ed744ccda91311f0d66f97e74d7f6d68910753067a46a2ce5a386c4`. Binary SHA-256: `248067e496d990e3bcc0be1d0a1d600d1daceae51410494cb09847df61f1a497`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq023\scenes\sq023_02_ride_gloria.scene" --events
```

## `base\quest\side_quests\sq023\scenes\sq023_03_call.scene`

188 graph nodes, 207 edges; 24 event-bearing sections, 143 events; 77 screenplay lines, 18 screenplay options, 9 choice nodes.

Actors: Wakako_Okada (actor 0, spawnSet); Rachel (actor 1, spawnSet); Joshua (actor 2, spawnDespawn); wakako_holocall (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `rachel_call` → 194; `fixer_call_in` → 4; `fixer_again_in` → 47; `rachel_after_in` → 252; `fixer_again_in_person` → 1056; `wakako_money_in` → 140.

Exits: `rachel_call_agree` → 223; `rachel_call_disagree` → 229; `fixer_call_ok_out` → 40; `fixer_call_no_out` → 43; `fixer_again_out` → 48; `rejected_out` → 1210; `rachel_after_out` → 269; `r_bd_rejected_out` → 1223; `r_end_rejected_out` → 1236; `wakako_money_out` → 154.

End nodes: 40: `<omitted>`; 43: `<omitted>`; 48: `<omitted>`; 154: `<omitted>`; 223: `<omitted>`; 229: `<omitted>`; 269: `<omitted>`; 1210: `<omitted>`; 1223: `<omitted>`; 1236: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 6. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 24 | 45 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnDialogLineEvent` | 73 | 39 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 6 | 278 / 350 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/2` |
| `scnPlaySkAnimEvent` | 36 | 39 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 4 | 227 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 8
- speech, skeletal_animation, idle_animation: 8
- speech, idle_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech: 1
- speech, socket_signal: 1

Raw SHA-256: `e1ef537d15e0566890bb3ab4e5230e3d9febf7e7778e35d66a4477f870324bce`. Binary SHA-256: `0b25faef10053fb1f070081734d0f5f3f0d7676b09eaaeec6835056c6dbb6d34`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq023\scenes\sq023_03_call.scene" --events
```

## `base\quest\side_quests\sq023\scenes\sq023_04_glorias_house.scene`

535 graph nodes, 742 edges; 95 event-bearing sections, 935 events; 181 screenplay lines, 35 screenplay options, 17 choice nodes.

Actors: Gloria (actor 0, spawnSet); Rachel (actor 1, spawnSet); Joshua (actor 2, spawnSet); Vasquez (actor 3, spawnSet); Zuleikha (actor 4, spawnSet); Johnny (actor 5, spawnDespawn); Emperor (actor 6, spawnSet); V (actor 7, findInContext).

Entries: `porch_in` → 1; `test2` → 4680; `rach_stays_in` → 552; `Start 9` → 5219; `Start 10` → 5223; `Start 11` → 5227; `Start 7` → 1918; `Start 12` → 5231.

Exits: `mariah_talk_out_end` → 415; `quest_failed_out` → 2970; `End 11` → 5062; `End 12` → 5078; `End 13` → 5093; `rach_stays_out` → 553; `End 14` → 5111; `mariah_talk_out` → 381.

End nodes: 381: `NonTerminating`; 415: `NonTerminating`; 553: `<omitted>`; 2970: `<omitted>`; 5062: `NonTerminating`; 5078: `NonTerminating`; 5093: `NonTerminating`; 5111: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 715 / 1125 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/3` |
| `scnChangeIdleAnimEvent` | 78 | 372 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 142 | 372 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnGameplayActionEvent` | 2 | 3447 / 3187 | `/Data/RootChunk/sceneGraph/Data/graph/403/Data/events/2` |
| `scnGameplayTransitionEvent` | 8 | 738 / 1164 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/19` |
| `scnIKEvent` | 20 | 738 / 1135 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/3` |
| `scnLookAtEvent` | 241 | 372 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnPlaySkAnimEvent` | 144 | 372 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPoseCorrectionEvent` | 4 | 372 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/17` |
| `scnUnmountEvent` | 8 | 738 / 1165 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/20` |
| `scneventsAttachPropToPerformer` | 8 | 385 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/22` |
| `scneventsAttachPropToWorld` | 11 | 449 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/6` |
| `scneventsEquipItemToPerformer` | 1 | 3447 / 3191 | `/Data/RootChunk/sceneGraph/Data/graph/403/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 17 | 738 / 1162 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/18` |
| `scneventsSocket` | 236 | 372 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 3455 / 3221 | `/Data/RootChunk/sceneGraph/Data/graph/406/Data/events/5` |
| `scneventsVFXEvent` | 2 | 539 / 924 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 13
- speech: 10
- gaze: 10
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 8
- skeletal_animation, gaze, socket_signal: 7
- speech, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal, animation_state, gameplay_action: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, audio, socket_signal, animation_state: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, audio: 1
- skeletal_animation, socket_signal, animation_state: 1
- speech, idle_animation: 1
- skeletal_animation, props_equipment, socket_signal: 1
- idle_animation, gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, socket_signal, animation_state: 1
- speech, idle_animation, socket_signal: 1

Raw SHA-256: `f59db831a0805dbdbca3112fc7be04a5a6847f84c89476e73bb2e2c627f13dcc`. Binary SHA-256: `d847e40b8967ffc3faaa6d15313999639b93445fada6337e4e51c807b4235127`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq023\scenes\sq023_04_glorias_house.scene" --events
```

## `base\quest\side_quests\sq023\scenes\sq023_07_restaurant.scene`

635 graph nodes, 772 edges; 136 event-bearing sections, 1182 events; 247 screenplay lines, 43 screenplay options, 18 choice nodes.

Actors: Rachel (actor 0, spawnSet); Joshua (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); Vasquez (actor 3, spawnSet); Customer_1 (actor 4, spawnSet); Customer_4 (actor 5, spawnSet); Customer_5 (actor 6, spawnSet); Customer_6 (actor 7, spawnSet); Customer_9 (actor 8, spawnSet); Customer_11 (actor 9, spawnSet); Customer_12 (actor 10, spawnSet); Customer_16 (actor 11, spawnSet); Waitress (actor 12, spawnSet); add_customer_002 (actor 13, spawnSet); add_customer_003 (actor 14, spawnSet); add_customer_007 (actor 15, spawnSet); add_customer_008 (actor 16, spawnSet); add_customer_010 (actor 17, spawnSet); add_customer_013 (actor 18, spawnSet); add_customer_014 (actor 19, spawnSet); add_customer_015 (actor 20, spawnSet); add_customer_017 (actor 21, spawnSet); add_customer_018 (actor 22, spawnSet); add_customer_019 (actor 23, spawnSet); add_customer_020 (actor 24, spawnSet); add_customer_021 (actor 25, spawnSet); add_customer_022 (actor 26, spawnSet); add_customer_023 (actor 27, spawnSet); add_customer_024 (actor 28, spawnSet); add_customer_025 (actor 29, spawnSet); Emperor (actor 30, spawnSet); V (actor 31, findInContext).

Entries: `Start 12` → 5255; `Start 10` → 3193; `Start 13` → 5369; `Start 11` → 4941; `Start 14` → 5374; `cigarette_in` → 644.

Exits: `restaurant_out` → 627; `end_quest` → 665.

End nodes: 627: `NonTerminating`; 665: `Terminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 17 | 1263 / 1670 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/2` |
| `scnChangeIdleAnimEvent` | 54 | 628 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 163 | 628 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayActionEvent` | 2 | 1806 / 1956 | `/Data/RootChunk/sceneGraph/Data/graph/163/Data/events/0` |
| `scnGameplayTransitionEvent` | 25 | 656 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/28` |
| `scnIKEvent` | 52 | 656 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/8` |
| `scnLookAtEvent` | 230 | 628 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 192 | 628 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnPoseCorrectionEvent` | 10 | 656 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/21` |
| `scnUnmountEvent` | 25 | 656 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/27` |
| `scneventsAttachPropToPerformer` | 34 | 1195 / 1581 | `/Data/RootChunk/sceneGraph/Data/graph/121/Data/events/0` |
| `scneventsAttachPropToWorld` | 11 | 1231 / 1608 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/3` |
| `scneventsCameraParamsEvent` | 15 | 656 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/19` |
| `scneventsEquipItemToPerformer` | 9 | 635 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 47 | 654 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/7` |
| `scneventsSocket` | 285 | 628 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 4 | 868 / 1135 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/24` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1231 / 1612 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/7` |
| `scneventsVFXEvent` | 6 | 635 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 34
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- camera: 8
- speech, skeletal_animation, gaze, socket_signal: 7
- speech: 7
- skeletal_animation, props_equipment, socket_signal: 7
- socket_signal: 5
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 4
- speech, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, socket_signal, animation_state: 3
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- props_equipment: 3
- skeletal_animation, audio, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- gaze, props_equipment, socket_signal: 2
- skeletal_animation, camera, audio, socket_signal: 2
- skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, socket_signal, animation_state: 1
- props_equipment, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1

Raw SHA-256: `9ee089d5d29249a682d76761308a484fc76033746d7fc769c212de610d0f350f`. Binary SHA-256: `e660d69d97fc854f93b7326f4b656d6a28f5dd0874f4b63407806f610e5dbd50`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq023\scenes\sq023_07_restaurant.scene" --events
```

## `base\quest\side_quests\sq023\scenes\sq023_10_bd_studio.scene`

572 graph nodes, 712 edges; 128 event-bearing sections, 874 events; 188 screenplay lines, 62 screenplay options, 40 choice nodes.

Actors: Joshua (actor 0, spawnSet); Rachel (actor 1, spawnSet); Vasquez (actor 2, spawnSet); Johnny (actor 3, spawnDespawn); Policewoman (actor 4, spawnSet); director (actor 5, spawnSet); soldat1 (actor 6, spawnSet); nailer (actor 7, spawnSet); operator (actor 8, spawnSet); technician2 (actor 9, spawnSet); V (actor 10, findInContext).

Entries: `in_the_studio` → 15; `joshua_distance_q_end` → 58; `Start 20` → 3114; `Start 21` → 4071; `Start 22` → 4129; `Start 23` → 4155; `Start 18` → 2253.

Exits: `joshua_distance` → 16; `to_joshua_distance2` → 715; `leaving_studio` → 755; `distance_cut` → 2184; `Rachel_reminder` → 2714; `after_crucifixion` → 870; `securing_cut` → 2307; `securing_out_2` → 2314; `cut_control_out` → 2319.

End nodes: 16: `NonTerminating`; 715: `NonTerminating`; 755: `<omitted>`; 870: `<omitted>`; 2184: `NonTerminating`; 2307: `NonTerminating`; 2314: `NonTerminating`; 2319: `NonTerminating`; 2714: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 45 | 261 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnChangeIdleAnimEvent` | 64 | 60 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnDialogLineEvent` | 114 | 60 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnGameplayTransitionEvent` | 11 | 261 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scnIKEvent` | 22 | 261 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scnLookAtEvent` | 136 | 60 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnPlaySkAnimEvent` | 185 | 60 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPoseCorrectionEvent` | 13 | 281 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/9` |
| `scnUnmountEvent` | 11 | 261 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsAttachPropToPerformer` | 14 | 372 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/1` |
| `scneventsAttachPropToWorld` | 16 | 947 / 1474 | `/Data/RootChunk/sceneGraph/Data/graph/158/Data/events/11` |
| `scneventsCameraParamsEvent` | 12 | 353 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/7` |
| `scneventsEquipItemToPerformer` | 6 | 989 / 1601 | `/Data/RootChunk/sceneGraph/Data/graph/167/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 11 | 261 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/10` |
| `scneventsSocket` | 188 | 60 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsUnequipItemFromPerformer` | 3 | 989 / 1605 | `/Data/RootChunk/sceneGraph/Data/graph/167/Data/events/7` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 563 / 868 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/5` |
| `scneventsVFXEvent` | 22 | 372 / 520 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, socket_signal: 20
- skeletal_animation, socket_signal: 9
- gaze: 9
- speech: 7
- skeletal_animation, gaze, socket_signal: 7
- skeletal_animation, idle_animation: 7
- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 6
- camera: 6
- skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal: 5
- speech, skeletal_animation, gaze: 4
- skeletal_animation, props_equipment, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal: 3
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 2
- skeletal_animation: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, camera, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, props_equipment, audio: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `bbabe33f05e348b1f366df61d9ac34b80139b135339d7f6148db784d6d47fd56`. Binary SHA-256: `a6cd77e8f91f3d2cd3aebad35d844e1e46fc61f805a57b40754e07c8122fcaa9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq023\scenes\sq023_10_bd_studio.scene" --events
```

## `base\quest\side_quests\sq023\scenes\sq023_11_01a_after_chase.scene`

405 graph nodes, 596 edges; 65 event-bearing sections, 536 events; 112 screenplay lines, 14 screenplay options, 8 choice nodes.

Actors: Rachel (actor 0, spawnSet); Vasquez (actor 1, spawnSet); Joshua (actor 2, spawnSet); Bill_jablonsky (actor 3, spawnSet); Johnny (actor 4, spawnDespawn); Truck_driver (actor 5, spawnSet); Bills_Truck (actor 6, spawnSet); Cargo_truck (actor 7, spawnSet); Emperor (actor 8, spawnSet); V (actor 9, findInContext).

Entries: `Start 0` → 1; `Start 11` → 4931; `BD_studio_reminder` → 2940; `Start 7` → 2599; `Start 4` → 2002; `Start 10` → 4765.

Exits: `jeremy_intro_out` → 4; `quest_ends` → 14; `combat_out` → 3239; `bill_killed` → 134; `combat_cleanup_out` → 2266; `truck_driver_out` → 2288; `talk_joshua_out` → 968.

End nodes: 4: `NonTerminating`; 14: `NonTerminating`; 134: `NonTerminating`; 968: `NonTerminating`; 2266: `NonTerminating`; 2288: `NonTerminating`; 3239: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 680 / 238 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/20` |
| `scnChangeIdleAnimEvent` | 42 | 680 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/4` |
| `scnDialogLineEvent` | 84 | 363 / 163 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/0` |
| `scnGameplayActionEvent` | 4 | 680 / 226 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/15` |
| `scnGameplayTransitionEvent` | 7 | 708 / 701 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/45` |
| `scnIKEvent` | 16 | 708 / 684 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/35` |
| `scnLookAtAdvancedEvent` | 2 | 716 / 775 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/3` |
| `scnLookAtEvent` | 112 | 679 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 4 | 1056 / 898 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/0` |
| `scnPlaySkAnimEvent` | 94 | 680 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/0` |
| `scnUnmountEvent` | 7 | 708 / 702 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/46` |
| `scneventsAttachPropToPerformer` | 1 | 680 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/18` |
| `scneventsAttachPropToWorld` | 1 | 2714 / 1953 | `/Data/RootChunk/sceneGraph/Data/graph/242/Data/events/0` |
| `scneventsEquipItemToPerformer` | 1 | 680 / 239 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/21` |
| `scneventsSetAnimFeatureEvent` | 38 | 680 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/16` |
| `scneventsSocket` | 110 | 680 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/10` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1376 / 1049 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/16` |
| `scneventsVFXEvent` | 3 | 702 / 539 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 5
- skeletal_animation: 4
- skeletal_animation, socket_signal, animation_state: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- gaze: 3
- speech, skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, idle_animation: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1
- props_equipment, socket_signal, animation_state: 1
- speech, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, audio, socket_signal, animation_state: 1
- skeletal_animation, audio, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `f451a5636a3064f8085a084f12131bb5d49ff34f490fa7873a81bd2eea74563f`. Binary SHA-256: `a40faab05cf8fc9475ad1d37469814a0db1c1f1a063f0bc341b0d94fd633cba0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq023\scenes\sq023_11_01a_after_chase.scene" --events
```

## `base\quest\side_quests\sq023\scenes\sq023_11_protesters_chats.scene`

101 graph nodes, 136 edges; 16 event-bearing sections, 116 events; 28 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: protester_001 (actor 0, spawnSet); protester_002 (actor 1, spawnSet); protester_003 (actor 2, spawnSet); protester_004 (actor 3, spawnSet); protester_005 (actor 4, spawnSet); protester_006 (actor 5, spawnSet); protester_007 (actor 6, spawnSet); protester_008 (actor 7, spawnSet); Vasquez (actor 8, spawnSet); Policewoman (actor 9, spawnSet); V (actor 10, findInContext).

Entries: `random_in` → 10; `chat_in` → 61; `meet_vasq_in` → 160; `to_protest` → 87.

Exits: `to_studio` → 98; `policewoman_distance` → 101.

End nodes: 98: `NonTerminating`; 101: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 40 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 26 | 40 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnLookAtEvent` | 29 | 63 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scnPlaySkAnimEvent` | 25 | 63 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scneventsAttachPropToPerformer` | 12 | 391 / 387 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/1` |
| `scneventsSocket` | 16 | 63 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation: 5
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `5a2c99c95eec8e539466078f7729a1b10ffd4827de390420cc6c5cac1af2a177`. Binary SHA-256: `c48ffb8139566e159e7483843349f9f684183dfa6e98d8a0a74e0f3048fbdf4b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq023\scenes\sq023_11_protesters_chats.scene" --events
```

## `ep1\quest\minor_quests\mq303\scenes\mq303_02_linas_mansion.scene`

572 graph nodes, 707 edges; 68 event-bearing sections, 548 events; 100 screenplay lines, 21 screenplay options, 11 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Ganger_1__female (actor 1, community); Ganger_2__male (actor 2, community); Lina (actor 3, spawnSet); Ganger_4__male (actor 4, community); Ganger_5_male (actor 5, community); Ganger_6_female (actor 6, community); ganger_car (actor 7, community); Player (actor 8, findInContext).

Entries: `Start 0` → 1; `Start 3` → 3002.

Exits: `scene killer` → 2171; `End 0` → 157.

End nodes: 157: `NonTerminating`; 2171: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 37 | 17 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 79 | 17 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 12 | 107 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/6` |
| `scnIKEvent` | 24 | 107 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 116 / 230 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/4` |
| `scnLookAtEvent` | 100 | 17 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 146 | 17 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 12 | 107 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |
| `scneventsEquipItemToPerformer` | 7 | 151 / 550 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/21` |
| `scneventsSetAnimFeatureEvent` | 13 | 107 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scneventsSocket` | 111 | 17 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1195 / 1561 | `/Data/RootChunk/sceneGraph/Data/graph/149/Data/events/27` |
| `scneventsVFXEvent` | 4 | 80 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 15
- speech, skeletal_animation, socket_signal: 6
- skeletal_animation, socket_signal: 6
- speech: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- socket_signal: 2
- props_equipment, socket_signal: 2
- speech, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `390e77d25919721256a5b97b8d18fa947e94a435c1c8471249c3d9a587f5f005`. Binary SHA-256: `1b26c26c9a07185dcee971c44c14b3d251a1f6967811695aa9290a2f5a761eab`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq303\scenes\mq303_02_linas_mansion.scene" --events
```

