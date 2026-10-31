# I've Seen That Face Before: scene presentation

Journal identity: `ep1/quests/main_quest/q304_netrunners`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q304_netrunners.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\main_quests\q304\scenes\q304_02b_car_rental.scene`

392 graph nodes, 495 edges; 75 event-bearing sections, 483 events; 150 screenplay lines, 29 screenplay options, 9 choice nodes.

Actors: AlexHolo (actor 0, spawnSet); Reed (actor 1, spawnSet); Alex (actor 2, spawnSet); crash_chat_driver_01 (actor 3, community); crash_chat_driver_02 (actor 4, community); car_1 (actor 5, spawnSet); Player (actor 6, findInContext).

Entries: `q304_02b_first_tower_call_in` → 1; `q304_scan1` → 1503; `q304_scan2` → 1505; `q304_scan_3` → 1507; `q304_car_crash_chat_in` → 773; `q304_waiting_at_the_border_one_call` → 798; `q304_02b_tower_04_in` → 51; `Start 3` → 440; `old` → 461; `Start 9` → 1964; `q304_02b_intro_in` → 94; `q304_02b_reminder_call_in` → 493; `q304_02b_vantage_point_in` → 974; `q304_to_the_border_reed_in` → 620; `q304_waiting_at_the_border_in` → 253; `Getting up` → 2145.

Exits: `q304_02b_first_tower_call_out` → 2; `q304_car_crash_chat_out` → 774; `q304_02b_intro_out` → 100; `q304_02b_reminder_call_out` → 495; `q304_waiting_at_the_border_intro_out` → 971; `q304_02b_vantage_point_break_out` → 978; `q304_to_the_border_reed_out` → 622; `q304_waiting_at_the_border_out` → 303; `StartCars` → 310.

End nodes: 2: `<omitted>`; 100: `<omitted>`; 303: `<omitted>`; 310: `NonTerminating`; 495: `<omitted>`; 622: `<omitted>`; 774: `<omitted>`; 971: `<omitted>`; 978: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 465 / 526 | `/Data/RootChunk/sceneGraph/Data/graph/94/Data/events/6` |
| `scnChangeIdleAnimEvent` | 6 | 22 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnDialogLineEvent` | 128 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 447 / 489 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/3` |
| `scnIKEvent` | 12 | 447 / 487 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/1` |
| `scnLookAtAdvancedEvent` | 16 | 465 / 525 | `/Data/RootChunk/sceneGraph/Data/graph/94/Data/events/5` |
| `scnLookAtEvent` | 101 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 99 | 22 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnPoseCorrectionEvent` | 15 | 128 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/3` |
| `scnUnmountEvent` | 6 | 447 / 493 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/6` |
| `scneventsAttachPropToPerformer` | 3 | 465 / 528 | `/Data/RootChunk/sceneGraph/Data/graph/94/Data/events/8` |
| `scneventsAttachPropToWorld` | 4 | 465 / 529 | `/Data/RootChunk/sceneGraph/Data/graph/94/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 6 | 447 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/5` |
| `scneventsSocket` | 75 | 128 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/4` |
| `scneventsVFXEvent` | 2 | 1287 / 1393 | `/Data/RootChunk/sceneGraph/Data/graph/214/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 30
- skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal, animation_state: 5
- speech, gaze: 3
- speech, skeletal_animation, idle_animation: 3
- speech, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- gaze, props_equipment: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- idle_animation, gaze: 1

Raw SHA-256: `9de4cd28802135440d26528d109647804f4c67871329267161bf5080eee5227a`. Binary SHA-256: `8a48627d27a585a9e26c353a141860a02fba307c427f2c5eb4dddee3b7cf55ee`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_02b_car_rental.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_04_entering_stadium.scene`

359 graph nodes, 443 edges; 51 event-bearing sections, 332 events; 95 screenplay lines, 9 screenplay options, 5 choice nodes.

Actors: Alex (actor 0, spawnSet); ReedHolo (actor 1, spawnSet); Songbird (actor 2, spawnDespawn); Aurore (actor 3, spawnSet); Aymeric (actor 4, spawnSet); Reed (actor 5, spawnSet); Theo_test (actor 6, spawnSet); Guard (actor 7, findInContext); ReedAudio (actor 8, findInContext); netrunners_car (actor 9, spawnSet); truck_1 (actor 10, spawner); reed_vehicle (actor 11, spawnSet); truck_2 (actor 12, spawner); truck_3 (actor 13, spawner); Player (actor 14, findInContext).

Entries: `q304_04_in` → 1; `q304_04_from_failsafe_in` → 392; `OLD` → 2195; `car_rotation_reset_in` → 3999; `Start 5` → 3387; `cinematic_in` → 1070.

Exits: `car_rotation_reset_out` → 4000; `ChasersOn` → 2604; `baricadesetup` → 2636; `car_camera_control_off` → 2296; `car_camera_control_on` → 1228; `FailCamerasOff` → 3103; `q304_04_end_non_term` → 1681; `netrunner_hacking_out` → 1331; `CameraHackingEffect` → 3942.

End nodes: 1228: `NonTerminating`; 1331: `NonTerminating`; 1681: `<omitted>`; 2296: `NonTerminating`; 2604: `NonTerminating`; 2636: `NonTerminating`; 3103: `NonTerminating`; 3942: `NonTerminating`; 4000: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 177 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scnChangeIdleAnimEvent` | 25 | 233 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/10` |
| `scnDialogLineEvent` | 82 | 167 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnGameplayActionEvent` | 3 | 2399 / 1318 | `/Data/RootChunk/sceneGraph/Data/graph/176/Data/events/4` |
| `scnGameplayTransitionEvent` | 5 | 592 / 441 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/10` |
| `scnIKEvent` | 14 | 587 / 399 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/3` |
| `scnLookAtEvent` | 70 | 233 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/2` |
| `scnPlaySkAnimEvent` | 53 | 177 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnUnmountEvent` | 4 | 592 / 445 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/13` |
| `scneventsAttachPropToNode` | 1 | 177 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/7` |
| `scneventsAttachPropToPerformer` | 1 | 177 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 14 | 587 / 391 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/1` |
| `scneventsSocket` | 45 | 177 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scneventsVFXEvent` | 5 | 177 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 20
- speech, socket_signal: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, gaze, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation: 2
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, socket_signal, animation_state: 1
- speech, gaze: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, idle_animation, audio, socket_signal, animation_state, gameplay_action: 1
- idle_animation, gameplay_action: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, ik, socket_signal, animation_state: 1

Raw SHA-256: `32e7297ff4954b5744aca13e73d86fff1aebc19c5132d971727332bc1c725290`. Binary SHA-256: `867a643d074be1a73f225b303ac687116b5d96b795222df04223e14dfd68ba9f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_04_entering_stadium.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_05_garage.scene`

388 graph nodes, 473 edges; 54 event-bearing sections, 604 events; 69 screenplay lines, 21 screenplay options, 11 choice nodes.

Actors: Aymeric (actor 0, spawnSet); Aurore (actor 1, spawnSet); Reed (actor 2, spawnSet); Alex_Male_Morphing (actor 3, spawnDespawn); Alex_Male (actor 4, community); Alex_Female (actor 5, spawnSet); Alex_Female_Morphing (actor 6, spawnDespawn); netrunners_car (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `q304_05_garage_start` → 1; `OLD` → 3132; `Start 0` → 4653; `Start 3` → 859; `Start 9` → 4330.

Exits: `q304_05_out` → 15; `End 0` → 4655; `CommunityCleanup` → 3421; `OutfitHandler` → 2054.

End nodes: 15: `<omitted>`; 2054: `NonTerminating`; 3421: `NonTerminating`; 4655: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 51 | 554 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scnChangeIdleAnimEvent` | 49 | 49 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 59 | 17 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 8 | 428 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 4347 / 2631 | `/Data/RootChunk/sceneGraph/Data/graph/323/Data/events/10` |
| `scnIKEvent` | 4 | 3207 / 1512 | `/Data/RootChunk/sceneGraph/Data/graph/156/Data/events/8` |
| `scnLookAtEvent` | 123 | 49 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnPlaySkAnimEvent` | 94 | 49 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scnUnmountEvent` | 1 | 4347 / 2630 | `/Data/RootChunk/sceneGraph/Data/graph/323/Data/events/9` |
| `scneventsAttachPropToNode` | 4 | 2393 / 798 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/67` |
| `scneventsAttachPropToPerformer` | 14 | 554 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/16` |
| `scneventsAttachPropToWorld` | 9 | 2393 / 734 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/25` |
| `scneventsCameraParamsEvent` | 4 | 3900 / 2233 | `/Data/RootChunk/sceneGraph/Data/graph/260/Data/events/0` |
| `scneventsEquipItemToPerformer` | 1 | 4361 / 2667 | `/Data/RootChunk/sceneGraph/Data/graph/327/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 7 | 554 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/13` |
| `scneventsSocket` | 129 | 49 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scneventsVFXEvent` | 46 | 554 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- speech, skeletal_animation, gaze, socket_signal: 10
- speech, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- camera: 4
- skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, audio, socket_signal, gameplay_action: 2
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, gameplay_action: 2
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 2
- speech, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal, gameplay_action: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, vfx: 1
- speech, skeletal_animation, idle_animation, ik, audio, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `0ef91f62fe6e6c94647b4c1adbc5233d2a3ea1319ad6f45b6004fe4360f84d42`. Binary SHA-256: `84d98c42f3fac9ade1437d9472e6541f37077775ae1907f67c87f6a5c611bf97`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_05_garage.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_06_disguise.scene`

622 graph nodes, 774 edges; 125 event-bearing sections, 812 events; 197 screenplay lines, 26 screenplay options, 12 choice nodes.

Actors: Reedholo (actor 0, spawnDespawn); Guard_01_m (actor 1, community); Guard_02_m (actor 2, community); Replacer_Male_Mirror (actor 3, spawnDespawn); Replacer_Female_Mirror (actor 4, spawnDespawn); Alex_Male (actor 5, community); Alex_Female (actor 6, community); Reed (actor 7, spawnSet); Guard_car_checkpoint (actor 8, community); guard_01_chat_01 (actor 9, community); guard_02_chat_01 (actor 10, community); guard_03_chat_02 (actor 11, community); guard_04_chat_02 (actor 12, community); garage_driveout_driver_01 (actor 13, community); guard_05_chat_03 (actor 14, community); guard_06_chat_03 (actor 15, community); Reed_man_01 (actor 16, spawnDespawn); Reed_man_02 (actor 17, spawnDespawn); netrunners_car (actor 18, spawnSet); reeds_car (actor 19, spawnSet); garage_driveout_01 (actor 20, spawner); Replacer_Male (actor 21, findInContext); Replacer_Female (actor 22, findInContext); Player_Original (actor 23, findInContext).

Entries: `q304_06_in` → 1; `Start 6` → 4618; `GarageChatsIn` → 2525.

Exits: `q304_06_out` → 2; `EnableCarFailsafe` → 1788; `DisableCarFailsafe` → 1791; `Dossier` → 933; `failsafeturnoff` → 4395.

End nodes: 2: `NonTerminating`; 933: `NonTerminating`; 1788: `NonTerminating`; 1791: `NonTerminating`; 4395: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 1733 / 1140 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/1` |
| `scnChangeIdleAnimEvent` | 22 | 1068 / 613 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/4` |
| `scnDialogLineEvent` | 164 | 412 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayActionEvent` | 8 | 1068 / 610 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/3` |
| `scnGameplayTransitionEvent` | 11 | 450 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/16` |
| `scnIKEvent` | 22 | 450 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/9` |
| `scnLookAtAdvancedEvent` | 2 | 2251 / 1696 | `/Data/RootChunk/sceneGraph/Data/graph/224/Data/events/6` |
| `scnLookAtEvent` | 216 | 440 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 146 | 412 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 3 | 2271 / 1803 | `/Data/RootChunk/sceneGraph/Data/graph/227/Data/events/25` |
| `scnUnmountEvent` | 9 | 450 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/15` |
| `scneventsCameraParamsEvent` | 5 | 2807 / 2650 | `/Data/RootChunk/sceneGraph/Data/graph/314/Data/events/7` |
| `scneventsEquipItemToPerformer` | 1 | 2743 / 2544 | `/Data/RootChunk/sceneGraph/Data/graph/306/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 39 | 450 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scneventsSocket` | 145 | 450 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scneventsVFXEvent` | 10 | 500 / 209 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 25
- speech, gaze: 13
- skeletal_animation, gaze, socket_signal: 11
- speech, skeletal_animation, gaze: 8
- speech, skeletal_animation, gaze, socket_signal, animation_state: 7
- speech, skeletal_animation: 6
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- skeletal_animation, gaze: 6
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 4
- camera: 4
- gaze: 4
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state, gameplay_action: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- socket_signal, animation_state: 2
- socket_signal: 2
- speech, gaze, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, socket_signal: 1
- speech, audio: 1
- props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, socket_signal: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `5baf6cd350b8f1cd92c95caf9f15985810a7e50d486cdec51dfc1dedb20eb6ea`. Binary SHA-256: `04a49e91389202e69b77736bd7b752a8498c1c4ba3c3bbd6bc2d84f5996fe912`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_06_disguise.scene" --events
```

