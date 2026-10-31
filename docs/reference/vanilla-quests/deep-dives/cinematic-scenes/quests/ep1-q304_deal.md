# Firestarter: scene presentation

Journal identity: `ep1/quests/main_quest/q304_deal`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q304_deal.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\main_quests\q304\scenes\q304_00_callin.scene`

14 graph nodes, 13 edges; 2 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: reed (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `q304_00_in` → 1.

Exits: `q304_00_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 37 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `ce67f86e5e759087c80a81cc086943fe46ed6897257909ce7ba44fc0a5ca67f7`. Binary SHA-256: `b59e510901e6228aff2fcbb145464ebb76317236d883e64a6491fa0be3526b7c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_00_callin.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_01_briefing.scene`

317 graph nodes, 468 edges; 81 event-bearing sections, 962 events; 202 screenplay lines, 36 screenplay options, 19 choice nodes.

Actors: Reed (actor 0, spawnSet); Alex (actor 1, spawnSet); Songbird (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `q304_01_in` → 1; `after_feedback` → 3778; `Sitting TEST` → 4685; `Getting up downstairs` → 3256; `Reaching briefing table` → 734; `End of briefing` → 3970; `Connect Later` → 3691; `FluffInspectablesIn` → 4023.

Exits: `q304_01_out` → 2; `FluffInspectablesOut` → 4062; `EnablePostBriefingFluffs` → 4067; `PrepAlexScene` → 2745; `q304_01_kill` → 3456.

End nodes: 2: `NonTerminating`; 2745: `NonTerminating`; 3456: `<omitted>`; 4062: `NonTerminating`; 4067: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 38 | 3700 / 1285 | `/Data/RootChunk/sceneGraph/Data/graph/133/Data/events/16` |
| `scnChangeIdleAnimEvent` | 34 | 11 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 163 | 11 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnGameplayTransitionEvent` | 7 | 11 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/19` |
| `scnIKEvent` | 14 | 11 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtAdvancedEvent` | 16 | 347 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/33` |
| `scnLookAtEvent` | 256 | 11 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 281 | 11 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 8 | 309 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/27` |
| `scnUnmountEvent` | 7 | 11 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsAttachPropToPerformer` | 6 | 309 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/10` |
| `scneventsAttachPropToWorld` | 6 | 309 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/17` |
| `scneventsSetAnimFeatureEvent` | 7 | 11 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scneventsSocket` | 117 | 11 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsUnequipItemFromPerformer` | 2 | 362 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, skeletal_animation, gaze, socket_signal: 7
- skeletal_animation, gaze, socket_signal: 6
- speech, gaze, socket_signal: 5
- speech, skeletal_animation, gaze: 5
- skeletal_animation, socket_signal: 5
- speech, skeletal_animation, gaze, audio, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, gaze: 3
- skeletal_animation, idle_animation: 3
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- gaze, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze, audio: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `7268795b2f398905ae2ed11100716cbbc3ee5227a04dca7202e4c670e45722f6`. Binary SHA-256: `96364ce83e6ce77399ea978f110ff1490fb4c1d4819235da5c574cbe474037ff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_01_briefing.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_02_songbird_calls.scene`

71 graph nodes, 70 edges; 12 event-bearing sections, 61 events; 22 screenplay lines, 5 screenplay options, 4 choice nodes.

Actors: Songbird (actor 0, findInContext); Songbird_Holo (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `q304_02_in` → 1; `WaitingForSomiIn` → 83; `Start 2` → 230; `Old` → 185.

Exits: `q304_02_out` → 2; `TimelapseActivated` → 152; `WaitingForSomiOut` → 115; `Restrictions on` → 425.

End nodes: 2: `<omitted>`; 115: `<omitted>`; 152: `NonTerminating`; 425: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 15 | 30 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 109 / 163 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/3` |
| `scnIKEvent` | 6 | 109 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/1` |
| `scnLookAtEvent` | 1 | 231 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/2` |
| `scnPlaySkAnimEvent` | 8 | 87 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/0` |
| `scnUnmountEvent` | 3 | 109 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 3 | 109 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/4` |
| `scneventsSocket` | 19 | 34 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scneventsVFXEvent` | 3 | 36 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, vfx, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `3bc811292d1e3548db6979f9c9cd6ae8dfe7835a0a2f15ef83577513d1c3ea40`. Binary SHA-256: `7dce831b34ea787bf0b2e1ca6ad74fefe546ca071fb9964b374d8ae1cd206a25`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_02_songbird_calls.scene" --events
```

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

## `ep1\quest\main_quests\q304\scenes\q304_02c_car_rental_kids.scene`

205 graph nodes, 246 edges; 34 event-bearing sections, 208 events; 55 screenplay lines, 16 screenplay options, 9 choice nodes.

Actors: Doris (actor 0, community); resident (actor 1, spawnDespawn); johnny (actor 2, spawnDespawn); kid_01 (actor 3, community); kid_02_speaker (actor 4, community); Player (actor 5, findInContext).

Entries: `q304_02c_car_rental_kids_in` → 1; `bd_guy_comment_in` → 1710; `OLD` → 1170; `PowerRestartIn` → 806; `WarmerIn` → 71; `ColderIn` → 85; `TestJohnny` → 501; `HotIn` → 360; `test johnny` → 925.

Exits: `q304_02c_car_rental_kids_out` → 2; `bd_guy_comment_out` → 1712; `PowerRestartOut` → 807; `StartColdWarm` → 103; `DownloadData` → 111; `q304_02b_tower_04_out` → 1477; `q304_02b_tower_04_download_out` → 1487; `HotOut` → 369.

End nodes: 2: `<omitted>`; 103: `NonTerminating`; 111: `NonTerminating`; 369: `<omitted>`; 807: `<omitted>`; 1477: `NonTerminating`; 1487: `<omitted>`; 1712: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 553 / 429 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/4` |
| `scnChangeIdleAnimEvent` | 11 | 305 / 251 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/1` |
| `scnDialogLineEvent` | 48 | 32 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 553 / 431 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/6` |
| `scnIKEvent` | 4 | 553 / 426 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/1` |
| `scnLookAtAdvancedEvent` | 1 | 626 / 565 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/6` |
| `scnLookAtEvent` | 37 | 305 / 252 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/2` |
| `scnPlaySkAnimEvent` | 54 | 225 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |
| `scnUnmountEvent` | 2 | 553 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/9` |
| `scneventsEquipItemToPerformer` | 1 | 626 / 568 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 2 | 553 / 433 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/8` |
| `scneventsSocket` | 40 | 225 / 206 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/1` |
| `scneventsVFXEvent` | 4 | 546 / 411 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 2
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `9c3b7457c05a2e9f2eaecc6a6e96868a03fc34ca3e5b72cc19a02a129fcd61e0`. Binary SHA-256: `79404ce00081f9da94cc630e5ca674f25518c6317417e56614bfd520c01f57a9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_02c_car_rental_kids.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_03_songbird_meeting.scene`

527 graph nodes, 704 edges; 121 event-bearing sections, 982 events; 245 screenplay lines, 46 screenplay options, 20 choice nodes.

Actors: Songbird (actor 0, spawnDespawn); Johnny (actor 1, spawnDespawn); reed_holo (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `q304_03_in` → 1; `Trailer shot 2` → 7112; `Mural` → 3386; `Songbird sits sofa2` → 3882; `q304_03_interrupted_2nd` → 7198; `After sofa` → 4845; `Start 0` → 6806; `Old` → 4941; `q304_03_reed_phonecall_straight_to_farida_in` → 4944; `q304_03_reed_phonecall_in` → 270; `Going to view` → 5511; `Sofa2 Fluffs` → 5985; `Trailer shot 1` → 6989; `Sofa test` → 4699.

Exits: `q304_03_out` → 2; `End 0` → 6808; `player_breaks_2nd` → 6335; `q304_03_reed_phonecall_loop_out` → 305; `q304_03_reed_phonecall_progress_out` → 1784; `CarRentalDone` → 1795; `q304_songbird_green_light_done` → 1802; `kill_songbird_meeting_scene` → 1808.

End nodes: 2: `NonTerminating`; 305: `<omitted>`; 1784: `<omitted>`; 1795: `NonTerminating`; 1802: `NonTerminating`; 1808: `<omitted>`; 6335: `<omitted>`; 6808: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 82 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/12` |
| `scnChangeIdleAnimEvent` | 20 | 64 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/32` |
| `scnDialogLineEvent` | 190 | 9 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 6 | 9 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scnIKEvent` | 12 | 9 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtAdvancedEvent` | 39 | 18 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnLookAtEvent` | 285 | 9 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayRidAnimEvent` | 1 | 7010 / 3647 | `/Data/RootChunk/sceneGraph/Data/graph/464/Data/events/1` |
| `scnPlaySkAnimEvent` | 236 | 9 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 9 | 64 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/11` |
| `scnUnmountEvent` | 6 | 9 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scneventsCameraParamsEvent` | 17 | 780 / 489 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/2` |
| `scneventsPlayRidCameraAnimEvent` | 2 | 6990 / 3615 | `/Data/RootChunk/sceneGraph/Data/graph/459/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 6 | 9 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsSocket` | 137 | 9 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsVFXEvent` | 15 | 82 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 18
- speech, skeletal_animation, gaze, socket_signal: 17
- camera: 9
- skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze: 7
- speech, socket_signal: 6
- skeletal_animation, socket_signal: 6
- gaze: 6
- speech, skeletal_animation, gaze, camera, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, vfx, socket_signal: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation: 2
- socket_signal: 2
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, camera, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal, animation_state: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- idle_animation, camera, socket_signal: 1
- skeletal_animation: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, camera, rid_camera, socket_signal: 1
- skeletal_animation, gaze, rid_actor, camera, rid_camera: 1
- vfx: 1

Raw SHA-256: `1909c3e6567b5a17291bde1130e2896c006849e0287f12872a87c9c8a602b167`. Binary SHA-256: `7d54a93cde2d1b8ba95a67fee111277e9b532ab7f9f71b4cf23291e0ee2c4464`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_03_songbird_meeting.scene" --events
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

## `ep1\quest\main_quests\q304\scenes\q304_04d_shard_pickup.scene`

765 graph nodes, 1024 edges; 171 event-bearing sections, 1233 events; 271 screenplay lines, 46 screenplay options, 18 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Farida (actor 1, spawnSet); Reed (actor 2, spawnSet); head_in_jar_male (actor 3, spawnDespawn); head_in_jar_female (actor 4, spawnDespawn); Player (actor 5, findInContext).

Entries: `q304_04d_in` → 1; `farida` → 3202; `Jar` → 3420; `icebreaker` → 4128; `reed` → 3677.

Exits: `q304_04d_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 43 | 1420 / 343 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/0` |
| `scnChangeIdleAnimEvent` | 68 | 1270 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnDialogLineEvent` | 186 | 1217 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 1270 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/16` |
| `scnIKEvent` | 14 | 1270 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |
| `scnLookAtEvent` | 301 | 1270 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scnPlaySkAnimEvent` | 229 | 1270 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnPoseCorrectionEvent` | 11 | 1331 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/4` |
| `scnUnmountEvent` | 7 | 1270 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/15` |
| `scneventsAttachPropToPerformer` | 30 | 1324 / 203 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scneventsAttachPropToWorld` | 24 | 1270 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/5` |
| `scneventsCameraParamsEvent` | 23 | 1420 / 344 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |
| `scneventsEquipItemToPerformer` | 4 | 2073 / 1314 | `/Data/RootChunk/sceneGraph/Data/graph/108/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 7 | 1270 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/14` |
| `scneventsSocket` | 244 | 1217 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsVFXEvent` | 35 | 1331 / 234 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 32
- skeletal_animation: 28
- skeletal_animation, socket_signal: 16
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 14
- speech: 9
- speech, gaze: 9
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 5
- skeletal_animation, props_equipment, socket_signal: 4
- speech, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- camera: 3
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, props_equipment, socket_signal: 1

Raw SHA-256: `5add514f37ab753ad4f1e43b2312b413ddad9e43200cc8d168f001676b692098`. Binary SHA-256: `782689ff3a0f2c29cbcdf9391fc040c60994fa51f57b7a79017dda3dbb61ec40`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_04d_shard_pickup.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_04e_alex_heart_to_heart.scene`

381 graph nodes, 564 edges; 91 event-bearing sections, 815 events; 172 screenplay lines, 47 screenplay options, 16 choice nodes.

Actors: Alex (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `q304_04e_in` → 1; `Start 5` → 3085; `Tests scene` → 833; `Start 2` → 467; `FOR NICO` → 1381.

Exits: `q304_04e_out` → 2; `TerminateOut` → 235; `HeartToHeartLeft` → 245.

End nodes: 2: `NonTerminating`; 235: `<omitted>`; 245: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 105 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 5 | 902 / 1227 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/3` |
| `scnIKEvent` | 10 | 902 / 1225 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/1` |
| `scnLookAtAdvancedEvent` | 63 | 12 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scnLookAtEvent` | 192 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 199 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 4 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnUnmountEvent` | 5 | 902 / 1232 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/7` |
| `scneventsAttachPropToPerformer` | 34 | 12 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsAttachPropToWorld` | 35 | 12 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scneventsCameraParamsEvent` | 18 | 767 / 1075 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/16` |
| `scneventsEquipItemToPerformer` | 2 | 1091 / 1275 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 902 / 1228 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/4` |
| `scneventsSocket` | 110 | 4 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsVFXDurationEvent` | 25 | 298 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, props_equipment, socket_signal: 13
- gaze: 13
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 10
- camera: 6
- speech, skeletal_animation, gaze: 5
- speech, gaze: 5
- skeletal_animation, gaze, socket_signal: 5
- skeletal_animation, gaze: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- gaze, props_equipment, socket_signal: 1
- props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze: 1
- speech: 1

Raw SHA-256: `8ab1430acf9dd845483d68f7cd8ef0d925fcfa20596a70d2ce3a6bdbcb050a4b`. Binary SHA-256: `ae7c2c93cfb9cdb2ae22fc30992a3626c9193c1a918d4ef46d76c39233ad5dd8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_04e_alex_heart_to_heart.scene" --events
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

## `ep1\quest\main_quests\q304\scenes\q304_07_deal.scene`

1552 graph nodes, 1851 edges; 340 event-bearing sections, 3983 events; 617 screenplay lines, 95 screenplay options, 42 choice nodes.

Actors: Songbird (actor 0, spawnSet); Alex_Male (actor 1, community); Alex_Female (actor 2, community); CoreGuard1_m (actor 3, community); CoreGuard2_m (actor 4, community); Kurt (actor 5, spawnSet); ReedHolo (actor 6, spawnDespawn); CoreGuard3_f (actor 7, community); CoreGuard4_f (actor 8, community); EscortBGSoldier_01_m (actor 9, community); EscortBGSoldier_02_m (actor 10, community); EscortBGSoldier_03_f (actor 11, community); EscortBGSoldier_04_m (actor 12, community); EscortBGSoldier_05_m (actor 13, community); GuardMeetingRoom_01_m (actor 14, community); GuardMeetingRoom_02_m (actor 15, community); Murphy (actor 16, spawnSet); tour_guide (actor 17, community); Guard_Graber (actor 18, spawnDespawn); Jago (actor 19, spawnDespawn); Guard_Gorzala (actor 20, spawnDespawn); Barmaid (actor 21, spawnDespawn); barman_chatter (actor 22, spawnDespawn); bennet (actor 23, spawnDespawn); worker_003 (actor 24, spawnDespawn); core_transport (actor 25, spawner); Replacer_Male (actor 26, findInContext); Replacer_Female (actor 27, findInContext); player_test (actor 28, findInContext).

Entries: `q304_07_in` → 1; `mocap` → 2985; `OLD` → 6149; `DealRoomTestIn` → 1214; `Start 8` → 6223; `Start 9` → 6226; `Start 10` → 6228; `Start 11` → 6230; `Start 19` → 12185; `Start 17` → 10281; `vodka` → 6377; `Start 14` → 9486; `Start1` → 9488; `Start 16` → 9719.

Exits: `q304_07_out` → 2; `TerminateOut` → 389; `SoldierDespawn` → 12512; `SpawnDealInsideSoldiers` → 12515.

End nodes: 2: `NonTerminating`; 389: `<omitted>`; 12512: `NonTerminating`; 12515: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 41 | 2164 / 2578 | `/Data/RootChunk/sceneGraph/Data/graph/180/Data/events/3` |
| `scnChangeIdleAnimEvent` | 269 | 236 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |
| `scnDialogLineEvent` | 588 | 144 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 27 | 1310 / 1752 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/17` |
| `scnIKEvent` | 54 | 1310 / 1744 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/10` |
| `scnLookAtEvent` | 1260 | 236 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnPlaySkAnimEvent` | 680 | 205 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnPoseCorrectionEvent` | 9 | 964 / 1443 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/4` |
| `scnUnmountEvent` | 27 | 1310 / 1751 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/16` |
| `scneventsAttachPropToPerformer` | 37 | 236 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/30` |
| `scneventsAttachPropToWorld` | 47 | 236 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/35` |
| `scneventsCameraParamsEvent` | 4 | 2263 / 3198 | `/Data/RootChunk/sceneGraph/Data/graph/205/Data/events/9` |
| `scneventsEquipItemToPerformer` | 30 | 279 / 322 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 27 | 1310 / 1749 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/15` |
| `scneventsSocket` | 825 | 144 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 2 | 2687 / 3821 | `/Data/RootChunk/sceneGraph/Data/graph/236/Data/events/7` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 2773 / 3985 | `/Data/RootChunk/sceneGraph/Data/graph/248/Data/events/3` |
| `scneventsVFXDurationEvent` | 2 | 286 / 343 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/9` |
| `scneventsVFXEvent` | 52 | 286 / 344 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 113
- speech: 62
- speech, skeletal_animation, gaze, socket_signal: 27
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 26
- skeletal_animation, gaze, socket_signal: 17
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 14
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 10
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 8
- speech, skeletal_animation, gaze: 7
- skeletal_animation, socket_signal: 6
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech, gaze: 4
- skeletal_animation, audio, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- gaze: 3
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 2
- skeletal_animation, gaze: 2
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx: 1
- gaze, socket_signal: 1
- socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `439a66ced2714f88fe9aa625411733b6d9e72e13e1668000012e51dcef8ecbf8`. Binary SHA-256: `232be831957af06131fc2882689cf7d466be070430b18600b140c228ee572ed8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_07_deal.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_07b_lab.scene`

845 graph nodes, 1009 edges; 99 event-bearing sections, 1765 events; 195 screenplay lines, 30 screenplay options, 21 choice nodes.

Actors: Songbird (actor 0, spawnSet); Songbird_vision (actor 1, spawnDespawn); Guard_01_m (actor 2, community); Guard_02_m (actor 3, community); GuardOutside_01_m (actor 4, community); GuardOutside_02_f (actor 5, community); Reed (actor 6, findInContext); Alex_Male (actor 7, community); Alex_Female (actor 8, community); Kurt (actor 9, spawnSet); Player_Voice (actor 10, findInContext); Alex_Voice (actor 11, findInContext); Guard_03_m (actor 12, community); Guard_04_m (actor 13, community); Guard_05_m (actor 14, community); Guard_06_m (actor 15, community); Replacer_Male (actor 16, findInContext); Replacer_Female (actor 17, findInContext); Player_Original (actor 18, findInContext).

Entries: `q304_07b_lab_in` → 1; `Start 5` → 4401; `SoldierRunInTest` → 4609; `ReplacerSwitchEndMaleReed` → 1832; `ReplacerSwitchEndFemaleReed` → 1837; `Start 7` → 4673.

Exits: `q304_07b_out_reed` → 2; `Blackwall` → 2327; `ReplacerSwitchPrepReed` → 3937; `ReedReplacerSwitchStart` → 1831; `ReplacerSwitchPrepSongbird` → 3960; `q304_07b_out_somi` → 1941.

End nodes: 2: `<omitted>`; 1831: `<omitted>`; 1941: `NonTerminating`; 2327: `NonTerminating`; 3937: `NonTerminating`; 3960: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 143 | 40 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/9` |
| `scnChangeIdleAnimEvent` | 132 | 25 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scnDialogLineEvent` | 175 | 9 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 452 / 1072 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/24` |
| `scnIKEvent` | 18 | 40 / 145 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/11` |
| `scnLookAtAdvancedEvent` | 6 | 62 / 329 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/22` |
| `scnLookAtEvent` | 289 | 9 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 191 | 21 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/8` |
| `scnUnmountEvent` | 5 | 452 / 1071 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/23` |
| `scneventsAttachPropToPerformer` | 6 | 69 / 360 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/8` |
| `scneventsAttachPropToWorld` | 4 | 69 / 384 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/32` |
| `scneventsCameraParamsEvent` | 9 | 2849 / 2892 | `/Data/RootChunk/sceneGraph/Data/graph/240/Data/events/16` |
| `scneventsSetAnimFeatureEvent` | 5 | 452 / 1067 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/20` |
| `scneventsSocket` | 321 | 21 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scneventsVFXEvent` | 456 | 25 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 22
- speech: 12
- speech, skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 8
- skeletal_animation: 6
- gaze: 6
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, socket_signal: 2
- skeletal_animation, gaze, audio, vfx, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `80a0860b8d2bb92e08405016643da4110db62796b38a93058da5511b8239a723`. Binary SHA-256: `569c9a4e1c394030b5a6591608eec2285378eb2332c1e6209b2e0a8ee594c509`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_07b_lab.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_08a_reed_wake_up.scene`

130 graph nodes, 134 edges; 19 event-bearing sections, 244 events; 34 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Reed (actor 0, findInContext); Johnny (actor 1, spawnDespawn); Kurt (actor 2, spawnSet); guard1 (actor 3, community); guard2 (actor 4, community); Alex_Female (actor 5, community); Alex_Male (actor 6, community); Player (actor 7, findInContext).

Entries: `q304_08a_in` → 1; `KurtInDealRoomIn` → 674; `backup` → 1136.

Exits: `StartKurtScene` → 744; `KurtInDealRoomOut` → 683; `EnableCombatPhase` → 800; `q304_08a_out` → 290; `Terminate` → 196; `StartOpeningDoor` → 727.

End nodes: 196: `<omitted>`; 290: `NonTerminating`; 683: `<omitted>`; 727: `NonTerminating`; 744: `NonTerminating`; 800: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 6 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnDialogLineEvent` | 34 | 6 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnGameplayTransitionEvent` | 9 | 241 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |
| `scnIKEvent` | 18 | 241 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnLookAtEvent` | 44 | 6 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scnPlaySkAnimEvent` | 45 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 9 | 241 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/8` |
| `scneventsCameraParamsEvent` | 2 | 310 / 231 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scneventsEquipItemToPerformer` | 2 | 540 / 398 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 9 | 241 / 173 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/5` |
| `scneventsSocket` | 60 | 6 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scneventsUnequipItemFromPerformer` | 1 | 540 / 421 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/22` |
| `scneventsVFXEvent` | 4 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation: 2
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, camera, vfx, socket_signal: 1
- camera: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `a020ea2a5b54c552f2def157ce4dbce5e23fcc4c8ac2a91e09e920f60964a98e`. Binary SHA-256: `1109d8a45850d907e41d15a79f9ed82c0c2e9206888a4dc54e6ea335ef9693e0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_08a_reed_wake_up.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_08b_songbird_wake_up.scene`

90 graph nodes, 97 edges; 3 event-bearing sections, 147 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Songbird (actor 0, spawnSet); Kurt (actor 1, spawnSet); Alex_Voice (actor 2, findInContext); Alex_Female (actor 3, community); Alex_Male (actor 4, community); Player (actor 5, findInContext).

Entries: `q304_08b_in` → 542.

Exits: `q304_08b_out` → 2; `Terminate` → 947; `AboutBlackwall` → 957.

End nodes: 2: `NonTerminating`; 947: `<omitted>`; 957: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 637 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnChangeIdleAnimEvent` | 17 | 637 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 14 | 637 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/17` |
| `scnLookAtEvent` | 16 | 637 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |
| `scnPlaySkAnimEvent` | 10 | 637 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsAttachPropToPerformer` | 2 | 637 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/35` |
| `scneventsEquipItemToPerformer` | 2 | 637 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/33` |
| `scneventsSocket` | 36 | 637 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsVFXEvent` | 44 | 637 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 2
- idle_animation: 1

Raw SHA-256: `575472759cdf149cde08b617beb9c2aca8fa992909ad503d7c6bf357d5945bbf`. Binary SHA-256: `f28997f67acca94edbcd1dfa39347b811d41533f61a16628203b910378ac3750`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_08b_songbird_wake_up.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_09a_reed_escape.scene`

413 graph nodes, 458 edges; 67 event-bearing sections, 428 events; 110 screenplay lines, 11 screenplay options, 7 choice nodes.

Actors: Reed (actor 0, spawnSet); radio_voice (actor 1, findInContext); Myers (actor 2, findInContext); Reed_Audio (actor 3, findInContext); Kurt_Audio (actor 4, findInContext); Songbird (actor 5, spawnDespawn); maxtac (actor 6, community); maxtac_1 (actor 7, community); maxtac_2 (actor 8, community); maxtac_3 (actor 9, community); DriveOutSoldier07 (actor 10, community); DriveOutSoldier01 (actor 11, community); DriveOutSoldier02 (actor 12, community); DriveOutSoldier03 (actor 13, community); DriveOutSoldier04 (actor 14, community); DriveOutSoldier05 (actor 15, community); DriveOutSoldier06 (actor 16, community); DriveOutSoldier08 (actor 17, community); DriveOutSoldier09 (actor 18, community); Barghest_Soldier_01 (actor 19, community); Barghest_Soldier_02 (actor 20, community); Barghest_Soldier_03 (actor 21, community); Barghest_Soldier_04 (actor 22, community); Barghest_Soldier_05 (actor 23, community); Barghest_Soldier_06 (actor 24, community); barghest_dispatch (actor 25, findInContext); get_away_car (actor 26, spawnSet); maxtac_av (actor 27, community); maxtac_av_2 (actor 28, community); maxtac_av_3 (actor 29, community); kurt_army (actor 30, spawner); kurt_army_01 (actor 31, spawner); kurt_army_02 (actor 32, spawner); kurt_army_03 (actor 33, spawner); kurt_army_04 (actor 34, spawner); kurt_army_05 (actor 35, spawner); kurt_army_06 (actor 36, spawner); kurt_army_07 (actor 37, spawner); kurt_army_08 (actor 38, spawner); Player (actor 39, findInContext).

Entries: `market_before_arena_in` → 3099; `av_landing_scene_test` → 1837; `Reed go back in` → 2286; `near_pz_exit_in` → 181; `market_mid_way_in` → 188; `market_crossed_in` → 198; `elevator_corridor_in` → 206; `elevator_arriving_in` → 214; `Test car impact` → 2344; `Start1` → 271; `av_landing_view_test` → 1161; `av_cavalry` → 1181; `spot_songbird` → 1204.

Exits: `market_before_arena_out` → 3101; `DespawnSoldiers` → 1830; `near_pz_exit_out` → 186; `market_mid_way_out` → 195; `market_crossed_out` → 203; `elevator_corridor_out` → 211; `elevator_arriving_out` → 218; `End1` → 273.

End nodes: 186: `<omitted>`; 195: `<omitted>`; 203: `<omitted>`; 211: `<omitted>`; 218: `<omitted>`; 273: `<omitted>`; 1830: `NonTerminating`; 3101: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 275 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/5` |
| `scnChangeIdleAnimEvent` | 24 | 275 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |
| `scnDialogLineEvent` | 73 | 182 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayActionEvent` | 10 | 275 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 309 / 237 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/14` |
| `scnIKEvent` | 16 | 309 / 222 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/2` |
| `scnLookAtAdvancedEvent` | 1 | 305 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/3` |
| `scnLookAtEvent` | 89 | 275 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |
| `scnPlaySkAnimEvent` | 90 | 275 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/3` |
| `scnUnmountEvent` | 2 | 309 / 245 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/21` |
| `scneventsCameraParamsEvent` | 2 | 2205 / 1541 | `/Data/RootChunk/sceneGraph/Data/graph/222/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 16 | 309 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/10` |
| `scneventsSocket` | 64 | 182 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 2 | 1388 / 892 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/21` |
| `scneventsVFXEvent` | 19 | 281 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- skeletal_animation: 6
- skeletal_animation, socket_signal, animation_state: 5
- speech, gaze: 5
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, idle_animation: 3
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 2
- skeletal_animation, audio, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- camera: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, audio, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, audio: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal, animation_state, gameplay_action: 1
- ik, socket_signal, animation_state: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, gaze, ik, audio, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, ik, socket_signal, gameplay_action: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, vfx: 1
- skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1

Raw SHA-256: `dcae8edc20d5e304a0e37b187bc41f42d4e3f4b436975a4dbb2a4a6bc977b42e`. Binary SHA-256: `703ee2236e248b5d4d886eb585b98342e8ac630b64bd8f12680f23b789e51eb7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_09a_reed_escape.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_09b_songbird_escape.scene`

327 graph nodes, 402 edges; 68 event-bearing sections, 315 events; 108 screenplay lines, 10 screenplay options, 7 choice nodes.

Actors: Songbird (actor 0, spawnSet); KurtAudio (actor 1, findInContext); HoboScared (actor 2, community); Cab_Driver (actor 3, spawner); Reed (actor 4, spawnSet); SongbirdHolocall (actor 5, findInContext); homeless_chat_01_speaker_02 (actor 6, community); homeless_chat_01_speaker_01 (actor 7, community); homeless_chat_02_speaker_01 (actor 8, community); homeless_chat_02_speaker_02 (actor 9, community); homeless_chat_03_speaker_01 (actor 10, community); homeless_chat_03_speaker_02 (actor 11, community); q304_spwn_songbird_escape_car_002 (actor 12, spawner); q304_spwn_songbird_escape_car_player (actor 13, spawner); Player (actor 14, findInContext).

Entries: `Start2` → 348; `escape_corridor_elevator_reed_kill` → 2629; `Start 15` → 4290; `Songbird jumps` → 3661; `escape_corridor_door_locked_in` → 128; `Start 5` → 1112; `Start 13` → 4030; `FailsafeHolocallStartIn` → 3797; `SBLockerRoomIn` → 2190; `q304_09b_v2_in` → 262.

Exits: `StartCarCleaup` → 1382; `escape_corridor_door_locked_out` → 130; `End 4` → 2758; `KillDoorScene` → 4704; `FailsafeOut` → 3795; `FailsafeHolocallStartOut` → 3828; `SBLockerRoomOut` → 2222; `Continue` → 3849.

End nodes: 130: `<omitted>`; 1382: `<omitted>`; 2222: `<omitted>`; 2758: `<omitted>`; 3795: `NonTerminating`; 3828: `<omitted>`; 3849: `NonTerminating`; 4704: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 1100 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/3` |
| `scnChangeIdleAnimEvent` | 12 | 1221 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/2` |
| `scnDialogLineEvent` | 79 | 133 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 1221 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 519 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |
| `scnIKEvent` | 10 | 519 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |
| `scnLookAtAdvancedEvent` | 1 | 2812 / 816 | `/Data/RootChunk/sceneGraph/Data/graph/120/Data/events/2` |
| `scnLookAtEvent` | 65 | 133 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 56 | 292 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnUnmountEvent` | 5 | 519 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/9` |
| `scneventsEquipItemToPerformer` | 5 | 2812 / 809 | `/Data/RootChunk/sceneGraph/Data/graph/120/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 7 | 519 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/6` |
| `scneventsSocket` | 56 | 292 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 24
- speech, gaze: 4
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze: 3
- skeletal_animation, audio, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, gameplay_action: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- props_equipment, socket_signal: 1
- gaze: 1

Raw SHA-256: `37945aabf0bcb9922a5a4fde8afa184d09a6d38bdba79a0c2dc17205063df9c9`. Binary SHA-256: `ac32112dafdb45ee59bf8ec7e2de21ab0f093fa7ab98428fb0e693fc177278eb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_09b_songbird_escape.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_09c_songbird_escape_combat.scene`

364 graph nodes, 409 edges; 44 event-bearing sections, 108 events; 77 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Songbird (actor 0, spawnSet); warehouse_chat_guard_001 (actor 1, community); warehouse_chat_guard_002 (actor 2, community); vehicle_area_chat_guard_001 (actor 3, community); KrugerVoice (actor 4, findInContext); Kruger (actor 5, spawnSet); miniboss_area_guard_001 (actor 6, community); miniboss_area_guard_002 (actor 7, community); tunnel_utility_worker_001 (actor 8, community); tunnel_utility_worker_002 (actor 9, community); tunnel_utility_worker_003 (actor 10, community); drone_02 (actor 11, community); drone_04 (actor 12, community); Player (actor 13, findInContext).

Entries: `KrugerChatsOld` → 1101; `warehouse_in` → 1; `near_pz_exit_in` → 374; `blocked_elevator_in` → 380; `entering_market_in` → 386; `MarketMechTurrets` → 757; `market_mid_way_in` → 392; `market_crossed_in` → 400; `escape_corridor_entered_in` → 406; `tech_corridor_in` → 412; `utility_room_in` → 418; `entering_sewers_in` → 424; `reaching_drain_tunnel_in` → 430; `CarRoomIn` → 146; `TunnelsChat01In` → 582; `TunnelsChat02In` → 583; `escape_start_in` → 677; `RadioSoldierIn` → 1432; `KrugerKilledIn` → 1453; `songbird_short_tired_in` → 1459.

Exits: `warehouse_out` → 2; `near_pz_exit_out` → 378; `blocked_elevator_out` → 384; `entering_market_out` → 388; `market_mid_way_out` → 394; `market_crossed_out` → 402; `escape_corridor_entered_out` → 410; `tech_corridor_out` → 414; `utility_room_out` → 420; `entering_sewers_out` → 426; `reaching_drain_tunnel_out` → 432; `MinibossRoomPatrols` → 528; `CarRoomOut` → 222; `TunnelsChat01Out` → 599; `TunnelsChat02Out` → 603; `WarehousePatrols` → 293; `escape_start_out` → 679; `TunnelsChat01Cut` → 1425; `RadioSoldierOut` → 330; `songbird_short_tired_out` → 1462.

End nodes: 2: `NonTerminating`; 222: `<omitted>`; 293: `NonTerminating`; 330: `NonTerminating`; 378: `<omitted>`; 384: `<omitted>`; 388: `<omitted>`; 394: `<omitted>`; 402: `<omitted>`; 410: `<omitted>`; 414: `<omitted>`; 420: `<omitted>`; 426: `<omitted>`; 432: `<omitted>`; 528: `NonTerminating`; 599: `NonTerminating`; 603: `<omitted>`; 679: `<omitted>`; 1425: `<omitted>`; 1462: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 1362 / 1260 | `/Data/RootChunk/sceneGraph/Data/graph/258/Data/events/2` |
| `scnDialogLineEvent` | 63 | 270 / 267 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 438 / 402 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/9` |
| `scnIKEvent` | 2 | 438 / 399 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/6` |
| `scnLookAtEvent` | 6 | 597 / 493 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 326 / 322 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/0` |
| `scnUnmountEvent` | 1 | 438 / 401 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 1 | 438 / 396 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/4` |
| `scneventsSocket` | 23 | 438 / 392 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- speech, socket_signal: 13
- skeletal_animation, gaze: 2
- speech, skeletal_animation: 1
- speech, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `56d3b84cae3a962b31b0e41f4be40b994d40b2362bf5fd910d0e78d5ec0a4545`. Binary SHA-256: `415279c50ae60ae4b63a997ffc15bd5041ef458b89cdc5ccbe4ae2722ae02a4d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_09c_songbird_escape_combat.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_09d_reed_escape_combat.scene`

259 graph nodes, 284 edges; 61 event-bearing sections, 128 events; 102 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: vip_area_rotor_chat_soldier_01 (actor 0, community); vehicle_area_chat_soldier_01 (actor 1, community); vehicle_area_chat_soldier_02 (actor 2, community); market_chat_soldier_01 (actor 3, community); market_chat_soldier_02 (actor 4, community); delivery_area_worker_01_chat_01 (actor 5, community); delivery_area_soldier_05_chat_02 (actor 6, community); delivery_area_soldier_04_chat_03 (actor 7, community); delivery_area_soldier_07_chat_03 (actor 8, community); Kurt (actor 9, spawnSet); miniboss_soldier_01_chat_01 (actor 10, community); miniboss_soldier_02_chat_01 (actor 11, community); ReedRadio (actor 12, findInContext); market_chat_soldier_03_chat_02 (actor 13, community); statue_chat_01 (actor 14, community); statue_chat_02 (actor 15, community); KurtVoice (actor 16, findInContext); miniboss_soldier_kurt_escort_01 (actor 17, community); miniboss_soldier_kurt_escort_02 (actor 18, community); Player (actor 19, findInContext).

Entries: `helicopter_rotor_chat_in` → 1; `kurt_bossfight_strong_arms_in` → 531; `vehicle_room_chat_in` → 20; `kurt_bossfight_knife_thrown_in` → 544; `kurt_bossfight_kurt_defeated_in` → 284; `kurt_bossfight_stealth_detect_in` → 1070; `kurt_glitched_announcement_in` → 559; `kurt_bossfight_stage_switch_in` → 578; `q304_09d_market_reaction_02_in` → 318; `market_chat_01_in` → 63; `delivery_area_chat_01_in` → 113; `kurt_bossfight_stealth_phonecall_in` → 380; `delivery_area_chat_02_in` → 130; `q304_reed_escape_civilian_bodies_comment_01_in` → 392; `q304_reed_escape_civilian_bodies_comment_02_in` → 393; `q304_reed_escape_civilian_bodies_comment_03_in` → 395; `q304_reed_escape_civilian_bodies_comment_04_in` → 397; `delivery_area_chat_03_in` → 147; `kurt_finish_off_in` → 676; `statue_chat_in` → 420; `kurt_bossfight_kurt_uses_knife_fist_time_in` → 428; `kurt_bossfight_ambush_in` → 167; `kurt_bossfight_kurt_prepares_to_use_knife_in` → 431; `kurt_bossfight_half_men_dead_in` → 172; `kurt_bossfight_all_men_dead_in` → 179; `kurt_bossfight_lmg_switching_position_in` → 443; `kurt_bossfight_custom_taunts_in` → 187; `kurt_bossfight_about_attempt_on_kurts_life_in` → 456; `kurt_bossfight_about_myers_in` → 459; `kurt_bossfight_taunt_about_alex_in` → 464; `kurt_bossfight_kurt_defeated_v2_in` → 492; `kurt_bossfight_stealth_chat_in` → 245; `kurt_bossfight_stealth_in` → 258; `kurt_bossfight_burst_taunt_in` → 521.

Exits: `kurt_bossfight_stealth_out` → 262; `helicopter_rotor_chat_out` → 2; `vehicle_room_chat_out` → 22; `SwitchObjectives` → 814; `kurt_glitched_announcement_out` → 561; `kurt_bossfight_kurt_defeated_out` → 304; `vehicle_room_chat_patrols_on` → 60; `market_chat_01_out` → 65; `q304_09d_market_reaction_02_out` → 334; `market_chat_01_patrols_on` → 89; `kurt_ambush_lights_off` → 370; `kurt_ambush_open_gate` → 373; `delivery_area_chat_01_out` → 121; `kurt_bossfight_stealth_phonecall_out` → 383; `kurt_ambush_grenade_bounce` → 389; `delivery_area_chat_02_out` → 138; `delivery_area_chat_03_out` → 149; `statue_chat_out` → 423; `kurt_bossfight_ambush_out` → 170; `kurt_bossfight_half_men_dead_out` → 174; `kurt_bossfight_all_men_dead_out` → 181; `kurt_bossfight_kurt_defeated_v2_out` → 508; `kurt_bossfight_stealth_chat_out` → 255.

End nodes: 2: `<omitted>`; 22: `<omitted>`; 60: `NonTerminating`; 65: `<omitted>`; 89: `NonTerminating`; 121: `<omitted>`; 138: `<omitted>`; 149: `<omitted>`; 170: `<omitted>`; 174: `<omitted>`; 181: `<omitted>`; 255: `NonTerminating`; 262: `<omitted>`; 304: `NonTerminating`; 334: `<omitted>`; 370: `NonTerminating`; 373: `NonTerminating`; 383: `<omitted>`; 389: `NonTerminating`; 423: `<omitted>`; 508: `NonTerminating`; 561: `<omitted>`; 814: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 168 / 306 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/2` |
| `scnChangeIdleAnimEvent` | 3 | 496 / 621 | `/Data/RootChunk/sceneGraph/Data/graph/147/Data/events/0` |
| `scnDialogLineEvent` | 97 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 247 / 396 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/2` |
| `scneventsAttachPropToPerformer` | 1 | 680 / 843 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/6` |
| `scneventsAttachPropToWorld` | 1 | 680 / 844 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/7` |
| `scneventsCameraParamsEvent` | 2 | 680 / 840 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/3` |
| `scneventsSocket` | 12 | 168 / 304 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/0` |
| `scneventsVFXEvent` | 2 | 1068 / 1121 | `/Data/RootChunk/sceneGraph/Data/graph/240/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 51
- speech, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, idle_animation, socket_signal: 1
- speech, socket_signal: 1
- speech, idle_animation: 1
- skeletal_animation, camera, props_equipment, socket_signal: 1
- idle_animation: 1
- skeletal_animation: 1
- speech, vfx: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `fcf1273404edb209b86fd0d9ee800508f46a2fd99fa65b6a406f73c1f6255d32`. Binary SHA-256: `10680cfea41103c5db9895758446fa7369b7830d1e9092dd89d51849cdb19e8d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_09d_reed_escape_combat.scene" --events
```

## `ep1\quest\main_quests\q304\scenes\q304_car_rental_voodooboys.scene`

5 graph nodes, 5 edges; 1 event-bearing sections, 10 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: car_rental_voodooboys_1 (actor 0, community); car_rental_voodooboys_2 (actor 1, community); Player (actor 2, findInContext).

Entries: `car_rental_voodooboys_chat_start` → 30.

Exits: `End` → 32.

End nodes: 32: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 40 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 40 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 1

Raw SHA-256: `48d1e033caecd293c6a48e229e59b2e70a241cf2f761fdcda91e0b857a6d335d`. Binary SHA-256: `a468bd2d5469d7f2a491a7731187a14cb6dea1888d3e9a6f17431ddd97f3ab13`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q304\scenes\q304_car_rental_voodooboys.scene" --events
```

