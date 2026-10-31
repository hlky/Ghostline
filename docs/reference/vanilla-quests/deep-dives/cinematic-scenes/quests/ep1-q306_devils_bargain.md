# The Killing Moon: scene presentation

Journal identity: `ep1/quests/main_quest/q306_devils_bargain`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q306_devils_bargain.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\main_quests\q306\scenes\q306_00_holo_reed.scene`

29 graph nodes, 35 edges; 13 event-bearing sections, 93 events; 37 screenplay lines, 10 screenplay options, 3 choice nodes.

Actors: Reed_holo (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `call_in` → 1.

Exits: `call_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 35 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnDialogLineEvent` | 37 | 35 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scnLookAtEvent` | 5 | 35 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |
| `scnPlaySkAnimEvent` | 29 | 35 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsSocket` | 7 | 35 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation: 4
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `e589ba64f0c8bef488a176ce943582cd0591956ac667a82c564ff778903265bc`. Binary SHA-256: `d9a0fe09f2e604865f1b94b5ec90a3249edce1eeb8541ec203f81a9d361c3a2f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_00_holo_reed.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_00_holo_songbird_hook.scene`

18 graph nodes, 18 edges; 4 event-bearing sections, 12 events; 10 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Songbird (actor 0, findInContext); V (actor 1, findInContext).

Entries: `call_in` → 1.

Exits: `call_out` → 2; `coords_out` → 187.

End nodes: 2: `<omitted>`; 187: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 10 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 2 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, socket_signal: 2
- speech: 2

Raw SHA-256: `07f506c7a88351815e2e39bd7fb383e1724b586c507bcea7dfe1e6a51957a75a`. Binary SHA-256: `6e905e6eadf3c43b2d10c0e17ef76232d3e990275372c7176f3846e2c1f80fa7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_00_holo_songbird_hook.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_01_ride_to_spaceport.scene`

413 graph nodes, 540 edges; 109 event-bearing sections, 513 events; 194 screenplay lines, 55 screenplay options, 20 choice nodes.

Actors: Songbird (actor 0, spawnSet); hobo (actor 1, community); Johnny (actor 2, spawnDespawn); Marilyn (actor 3, spawnDespawn); August (actor 4, spawnDespawn); SongbirdCar (actor 5, community); police_car (actor 6, community); road_block (actor 7, spawner); V (actor 8, findInContext).

Entries: `cinematic_preview` → 906; `van_in` → 79; `song_in` → 1450; `spaceport` → 749; `debug_mid_ride` → 5172; `follow_temp_in` → 6062.

Exits: `drive_out` → 2; `alt_ride` → 1380; `in_van_out` → 1478; `leave_guns` → 5898; `left_guns` → 5901; `start_drive_out` → 4162; `spaceport_arrived_out` → 4195; `car_out` → 1188; `leave car` → 783.

End nodes: 2: `NonTerminating`; 783: `NonTerminating`; 1188: `NonTerminating`; 1380: `NonTerminating`; 1478: `NonTerminating`; 4162: `NonTerminating`; 4195: `NonTerminating`; 5898: `NonTerminating`; 5901: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 4415 / 533 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/9` |
| `scnChangeIdleAnimEvent` | 16 | 1359 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnDialogLineEvent` | 153 | 764 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayActionEvent` | 2 | 1359 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 1359 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/9` |
| `scnIKEvent` | 12 | 1359 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/4` |
| `scnLookAtAdvancedEvent` | 1 | 5334 / 1264 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/2` |
| `scnLookAtEvent` | 103 | 764 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 1839 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/19` |
| `scnPlaySkAnimEvent` | 118 | 764 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 3 | 1839 / 160 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/14` |
| `scneventsAttachPropToPerformer` | 1 | 4470 / 609 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 4470 / 612 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 15 | 1359 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/8` |
| `scneventsSocket` | 74 | 1204 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |
| `scneventsVFXEvent` | 6 | 4415 / 526 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 25
- speech, skeletal_animation, gaze, socket_signal: 21
- speech, gaze: 14
- speech, skeletal_animation, gaze: 9
- speech, skeletal_animation, socket_signal: 5
- gaze: 4
- skeletal_animation: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, gaze: 3
- skeletal_animation, idle_animation, socket_signal, animation_state: 2
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- speech, audio, vfx: 1
- socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1

Raw SHA-256: `4fba99e379947eb4230f67b29bec0fe38ae4712d146a8fde8c79241853fac096`. Binary SHA-256: `74782a8950770a4146c0e457ed786e0241c0e2ba4179dba93a64d6dffabd8296`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_01_ride_to_spaceport.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_02_terminal_recon.scene`

310 graph nodes, 410 edges; 51 event-bearing sections, 305 events; 81 screenplay lines, 15 screenplay options, 7 choice nodes.

Actors: Gate_Guard (actor 0, community); Songbird_audio (actor 1, findInContext); Passenger_gate (actor 2, community); Gate_NPC (actor 3, spawnDespawn); V (actor 4, findInContext).

Entries: `gate_in` → 1; `Cinematic_preview` → 77; `failstate_preview` → 1592.

Exits: `gate_out` → 2; `End1` → 103; `inside_out` → 427; `pre_camera_out` → 429; `pre_link_out` → 431; `post_camera_out` → 479; `post_link_out` → 482; `look_camera` → 1066; `looked_too_soon` → 1069; `look_again` → 1072; `fail` → 811.

End nodes: 2: `NonTerminating`; 103: `<omitted>`; 427: `NonTerminating`; 429: `NonTerminating`; 431: `NonTerminating`; 479: `NonTerminating`; 482: `NonTerminating`; 811: `NonTerminating`; 1066: `NonTerminating`; 1069: `NonTerminating`; 1072: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 728 / 580 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/5` |
| `scnChangeIdleAnimEvent` | 22 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 60 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 375 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/10` |
| `scnIKEvent` | 8 | 375 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/3` |
| `scnLookAtAdvancedEvent` | 5 | 692 / 445 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/3` |
| `scnLookAtEvent` | 30 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 46 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 4 | 375 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/9` |
| `scneventsAttachPropToPerformer` | 7 | 689 / 432 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 728 / 586 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 4 | 375 / 231 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/6` |
| `scneventsSocket` | 70 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 38 | 692 / 443 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech: 6
- speech, socket_signal: 4
- skeletal_animation: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, props_equipment, socket_signal: 3
- gaze, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 2
- skeletal_animation, idle_animation, gaze: 2
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1
- idle_animation, gaze: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `d15fcf7521d067c8ebd952ea3517efdda73272d7b70c21485252cfc155ce11e7`. Binary SHA-256: `439ad12a6d65311225b62e8419c1cd211be76155b5aea647a5c7cf77ceee6bd7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_02_terminal_recon.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_02a_holo_songbird_terminal.scene`

101 graph nodes, 142 edges; 19 event-bearing sections, 36 events; 36 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Songbird_audio (actor 0, findInContext); train (actor 1, community); V (actor 2, findInContext).

Entries: `Start_temp` → 1004; `oa_friendly` → 719; `public_area_in` → 115; `restricted_area_in` → 116; `debug_from_gate` → 973.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 32 | 26 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 4 | 380 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, socket_signal: 4

Raw SHA-256: `92b34ab1ea9d97fdb5215e0289a6cc0082376bed512912e0d53e87dc35b2534c`. Binary SHA-256: `4c7af457780b6a64a49b1d10a1fd61b1362861d181c4a396d2157174a00ee858`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_02a_holo_songbird_terminal.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_03_terminal_mood.scene`

820 graph nodes, 1088 edges; 166 event-bearing sections, 845 events; 283 screenplay lines, 31 screenplay options, 16 choice nodes.

Actors: Distant_Observer_m001 (actor 0, community); Distant_Observer_m002 (actor 1, community); Distant_Observer_f001 (actor 2, community); Distant_Observer_f002 (actor 3, community); Undercover_Agent_m001 (actor 4, community); Undercover_Agent_m002 (actor 5, community); Undercover_Agent_f001 (actor 6, community); Undercover_Agent_f002 (actor 7, community); reception_f_passenger (actor 8, community); reception_m_passenger (actor 9, community); reception_f_receptionist (actor 10, community); Scene001_Actor_Guard_m001 (actor 11, community); Scene001_Actor_Guard_m002 (actor 12, community); Scene001_Actor_Bum_m001 (actor 13, community); Scene003_Actor_Guard_m001 (actor 14, community); Scene004_Actor_Guard_m001 (actor 15, community); Scene004_Actor_Civ_m001 (actor 16, community); Scene004_Actor_Civ_f001 (actor 17, community); Undercover_Agent_m003 (actor 18, community); Undercover_Agent_f003 (actor 19, community); Public_Announcement_System (actor 20, community); Scene003_spotted_m001 (actor 21, community); Scene005_Actor_Guard_m001 (actor 22, community); Johnny (actor 23, spawnDespawn); Scene002_Actor_Guard_m001 (actor 24, community); Scene001_Actor_Guard_m003 (actor 25, community); Scene004_Actor_Guard_m002 (actor 26, community); Scene003_Actor_Guard_m002 (actor 27, community); Undercover_Agent_m004 (actor 28, community); Songbird (actor 29, findInContext); int_bag_passenger (actor 30, community); non_casa_01 (actor 31, community); non_casa_02 (actor 32, community); non_bye_01 (actor 33, community); non_bye_02 (actor 34, community); non_stud_guard_01 (actor 35, community); non_stud_guard_02 (actor 36, community); non_stud_01 (actor 37, community); non_schedule (actor 38, community); non_toilet_01 (actor 39, community); non_toilet_02 (actor 40, community); non_corpo_01 (actor 41, community); non_corpo_02 (actor 42, community); non_party_01 (actor 43, community); non_party_02 (actor 44, community); non_party_03 (actor 45, community); non_smuggle_01 (actor 46, community); non_smuggle_02 (actor 47, community); non_stew_01 (actor 48, community); non_stew_02 (actor 49, community); non_elevator_01 (actor 50, community); non_elevator_02 (actor 51, community); int_vendor (actor 52, community); int_shop_guard (actor 53, community); int_rock_guard (actor 54, community); int_lawn_01 (actor 55, community); int_lawn_02 (actor 56, community); int_tarp_guard (actor 57, community); non_welcome_01 (actor 58, community); non_welcome_02 (actor 59, community); non_gillean (actor 60, community); non_oa_manager (actor 61, community); non_interview_guard_02 (actor 62, community); mech_001 (actor 63, spawner); mech_002 (actor 64, spawner); non_interview_fan (actor 65, community); non_crystal_stew (actor 66, community); non_crystal_passenger (actor 67, community); non_interview_guard_03 (actor 68, community); non_interview_guard_04 (actor 69, community); non_interview_guard_01 (actor 70, community); V (actor 71, findInContext).

Entries: `distant_observers_in` → 1; `undercover_agents_in` → 28; `general_mood_in` → 52; `reception_preview` → 3748; `thief_preview` → 4492; `q306_loading_screen` → 907; `spotted_preview` → 4025; `johnny_preview` → 4075; `stud_preview` → 4185; `rocket_preview` → 4264; `tarp_guard_restart_in` → 5102; `gillean_preview` → 4377.

Exits: `fail_mood` → 2958.

End nodes: 2958: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 2954 / 2744 | `/Data/RootChunk/sceneGraph/Data/graph/382/Data/events/3` |
| `scnChangeIdleAnimEvent` | 43 | 62 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnDialogLineEvent` | 226 | 62 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scnGameplayTransitionEvent` | 11 | 62 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/31` |
| `scnIKEvent` | 22 | 62 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/21` |
| `scnLookAtAdvancedEvent` | 1 | 395 / 425 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/46` |
| `scnLookAtEvent` | 174 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 162 | 62 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/7` |
| `scnUnmountEvent` | 11 | 62 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/30` |
| `scneventsEquipItemToPerformer` | 12 | 62 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/22` |
| `scneventsSetAnimFeatureEvent` | 11 | 62 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/28` |
| `scneventsSocket` | 158 | 62 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/5` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 2831 / 2502 | `/Data/RootChunk/sceneGraph/Data/graph/355/Data/events/28` |
| `scneventsVFXEvent` | 8 | 2954 / 2742 | `/Data/RootChunk/sceneGraph/Data/graph/382/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 40
- gaze: 35
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- speech, skeletal_animation, socket_signal: 10
- speech, gaze: 8
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, idle_animation, socket_signal: 5
- speech, skeletal_animation: 5
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, gaze, socket_signal: 3
- speech, idle_animation, socket_signal: 3
- skeletal_animation, props_equipment, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, idle_animation, gaze, socket_signal: 2
- speech, socket_signal: 2
- speech, idle_animation: 2
- idle_animation: 2
- gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, audio, vfx: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `98095234c47680174abd01a996927769e2e4d2f9572990795dcb28fedb88269b`. Binary SHA-256: `b02ab5270711f666976f76a49cb3e0e5338e10f9bcb0dfb49bd0fc19f673f1d9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_03_terminal_mood.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_03b_oa_staff_reactions.scene`

91 graph nodes, 114 edges; 33 event-bearing sections, 85 events; 33 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: rec (actor 0, community); rec_01 (actor 1, community); rec_02 (actor 2, community); rec_06 (actor 3, community); rec_07 (actor 4, community); rec_08 (actor 5, community); rec_09 (actor 6, community); piano (actor 7, community); fan_01 (actor 8, community); fan_02 (actor 9, community); fan_03 (actor 10, community); v (actor 11, findInContext).

Entries: `Start 0` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnLookAtEvent` | 38 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 41 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 6 | 285 / 433 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze: 21
- gaze: 7
- skeletal_animation, socket_signal: 4
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `17374a63d895f5ead94e058cdf134e80e1cde62c2bd941dbeb1a882c0e1033f8`. Binary SHA-256: `d252d94867c1731a6e543d686130aa35fcb355d5f8c438564858561c7d0c7d89`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_03b_oa_staff_reactions.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_03c_side_terminals.scene`

61 graph nodes, 70 edges; 10 event-bearing sections, 25 events; 14 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: rec_terminal_c (actor 0, community); corpo_01 (actor 1, community); corpo_02 (actor 2, community); corpo_coach (actor 3, community); rec_2_terminal_c (actor 4, community); child_05 (actor 5, community); child_17 (actor 6, community); child_18 (actor 7, community); fiona (actor 8, community); teacher_02 (actor 9, community); katie (actor 10, community); v (actor 11, findInContext).

Entries: `Start 0` → 3.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 11 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 11 | 1 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 9 | 11 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 4 | 26 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, skeletal_animation: 2
- gaze: 2
- speech, idle_animation, gaze: 1
- speech, gaze: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `a2cb319bc20ddbec4b28381b936e9584969c1f097ec2ac495942dd4f1a039dbd`. Binary SHA-256: `167f45d89598fd5d45fb759ac3e4166795e4ec829e93591db7b8ac4e6f5b48c3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_03c_side_terminals.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_04_meeting_contact.scene`

316 graph nodes, 394 edges; 52 event-bearing sections, 219 events; 96 screenplay lines, 18 screenplay options, 9 choice nodes.

Actors: Silverhand (actor 0, spawnDespawn); Songbird_audio (actor 1, findInContext); Guard_cell (actor 2, community); Guard_A (actor 3, community); Guard_B (actor 4, community); Guard_C (actor 5, community); Guard_D (actor 6, community); Guard_E (actor 7, community); V (actor 8, findInContext).

Entries: `failstate_cell` → 400; `explo_fail` → 800; `new_PUC_temp` → 2110.

Exits: `security_out` → 619; `spotted_out` → 673; `jacked_out` → 743; `fail_explo` → 1061; `jack in` → 481; `get out` → 527; `kill` → 1189.

End nodes: 481: `NonTerminating`; 527: `NonTerminating`; 619: `NonTerminating`; 673: `NonTerminating`; 743: `NonTerminating`; 1061: `NonTerminating`; 1189: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 428 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnChangeIdleAnimEvent` | 2 | 730 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/7` |
| `scnDialogLineEvent` | 81 | 405 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 575 / 175 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/4` |
| `scnIKEvent` | 6 | 575 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/1` |
| `scnLookAtEvent` | 14 | 405 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 28 | 428 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnUnmountEvent` | 3 | 575 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/8` |
| `scneventsEquipItemToPerformer` | 10 | 409 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 3 | 575 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/5` |
| `scneventsSocket` | 53 | 405 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsVFXEvent` | 10 | 405 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, socket_signal: 15
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 5
- skeletal_animation: 5
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, gaze, vfx, socket_signal: 1
- gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, audio, vfx: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1

Raw SHA-256: `81167fb11655bb23f09807b800f420037830c311fbcf80eb6e2313c8d9d88efa`. Binary SHA-256: `168680bfed20684c8c767d4c7134a2ac1bb95af01a2cafe06c8bd792ba3120e9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_04_meeting_contact.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_06_exploration_cmnts.scene`

135 graph nodes, 96 edges; 38 event-bearing sections, 66 events; 65 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Songbird (actor 0, spawnSet); mech_001 (actor 1, community); mech_002 (actor 2, community); Songbird_audio (actor 3, findInContext); V (actor 4, findInContext).

Entries: `q306_06_copter_frying_in` → 136; `q306_06_lockdown_reaction_in` → 1; `q306_06_public_area_all_clear_in` → 274; `q306_06_scan_for_friendlies_in` → 282; `q306_06_civilian_evac_in` → 10; `q306_06_gallery_chopper_001_in` → 153; `q306_06_orbital_air_mobilized_in` → 290; `q306_06_goal_rehash_in` → 18; `q306_06_gallery_chopper_002_in` → 161; `q306_06_orbital_air_restricted_entered_in` → 298; `q306_06_songbird_black_ops_arrival_in` → 30; `q306_06_gallery_chopper_003_in` → 169; `q306_06_songbird_hit_reaction_in` → 307; `q306_06_tower_approach_mid_fight_in` → 444; `q306_06_general_foobar_in` → 36; `q306_06_gallery_chopper_004_in` → 175; `q306_06_restricted_all_clear_in` → 315; `q306_06_chopper_fire_in` → 44; `q306_06_gallery_chopper_005_in` → 183; `q306_06_shooting_gallery_passed_in` → 324; `q306_06_gallery_chopper_006_in` → 188; `q306_06_in_the_clear_in` → 52; `q306_06_gallery_chopper_007_in` → 466; `q306_06_station_objective_switch_in` → 332; `q306_06_ambush_reaction_in` → 340; `q306_06_stealth_path_found_in` → 209; `q306_06_control_room_before_clear_in` → 348; `q306_06_all_cleared_in` → 356; `q306_06_techieV_mech_closets_in` → 221; `q306_06_gallery_chopper_in` → 85; `q306_06_genericV_mech_closets_in` → 222; `q306_06_connector_chopper_sighting_in` → 370; `q306_06_gallery_chopper_006_clone` → 510; `q306_06_mech_fall_idle_in` → 238; `q306_06_mech_ready_idle_in` → 241; `q306_06_additional_chat_PU_in` → 382; `q306_06_songbird_frying_in` → 110; `q306_06_calm_before_ambush_in` → 394; `q306_06_exit_nearby_in` → 269.

Exits: `q306_06_copter_frying_out` → 138; `q306_06_lockdown_reaction_out` → 2; `q306_06_public_area_all_clear_out` → 276; `q306_06_scan_for_friendlies_out` → 284; `q306_06_civilian_evac_out` → 12; `q306_06_gallery_chopper_001_out` → 155; `q306_06_orbital_air_mobilized_out` → 292; `q306_06_goal_rehash_out` → 20; `q306_06_gallery_chopper_002_out` → 163; `q306_06_orbital_air_restricted_entered_out` → 300; `q306_06_songbird_black_ops_arrival_out` → 31; `q306_06_gallery_chopper_003_out` → 171; `q306_06_tower_approach_mid_fight_out` → 445; `q306_06_songbird_hit_reaction_out` → 309; `q306_06_general_foobar_out` → 38; `q306_06_gallery_chopper_004_out` → 179; `q306_06_restricted_all_clear_out` → 317; `q306_06_chopper_fire_out` → 46; `q306_06_gallery_chopper_005_out` → 186; `q306_06_gallery_chopper_006_out` → 189; `q306_06_shooting_gallery_passed_out` → 326; `q306_06_in_the_clear_out` → 54; `q306_06_gallery_chopper_007_out` → 468; `q306_06_station_objective_switch_out` → 334; `q306_06_ambush_reaction_out` → 342; `q306_06_stealth_path_found_out` → 211; `q306_06_control_room_before_clear_out` → 350; `q306_06_all_cleared_out` → 358; `q306_06_gallery_chopper_out` → 87; `q306_06_techieV_mech_closets_out` → 224; `q306_06_genericV_mech_closets_out` → 225; `q306_06_connector_chopper_sighting_out` → 372; `q306_06_gallery_chopper_006_clone_out` → 512; `q306_06_additional_chat_PU_out` → 383; `q306_06_mech_ready_idle_out` → 247; `q306_06_songbird_frying_out` → 112; `q306_06_mech_fall_idle_out` → 249; `q306_06_calm_before_ambush_out` → 395; `q306_06_exit_nearby_out` → 270.

End nodes: 2: `<omitted>`; 12: `<omitted>`; 20: `<omitted>`; 31: `<omitted>`; 38: `<omitted>`; 46: `<omitted>`; 54: `<omitted>`; 87: `<omitted>`; 112: `<omitted>`; 138: `<omitted>`; 155: `<omitted>`; 163: `<omitted>`; 171: `<omitted>`; 179: `<omitted>`; 186: `<omitted>`; 189: `<omitted>`; 211: `<omitted>`; 224: `<omitted>`; 225: `<omitted>`; 247: `<omitted>`; 249: `<omitted>`; 270: `<omitted>`; 276: `<omitted>`; 284: `<omitted>`; 292: `<omitted>`; 300: `<omitted>`; 309: `<omitted>`; 317: `<omitted>`; 326: `<omitted>`; 334: `<omitted>`; 342: `<omitted>`; 350: `<omitted>`; 358: `<omitted>`; 372: `<omitted>`; 383: `<omitted>`; 395: `<omitted>`; 445: `<omitted>`; 468: `<omitted>`; 512: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 239 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/0` |
| `scnDialogLineEvent` | 59 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 2 | 28 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 28 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 35
- idle_animation: 2
- speech, skeletal_animation, gaze: 1

Raw SHA-256: `f621b2e0ca9a7ef161b92ad46cbf1a7b6eadb9191655f5914a626dd2bb80c51d`. Binary SHA-256: `db8be6a62bf5ee67636c8c6421aa429774c65ae75820d45d0de9b991bea6b59a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_06_exploration_cmnts.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_06_myers_intro.scene`

1081 graph nodes, 1270 edges; 168 event-bearing sections, 1219 events; 260 screenplay lines, 30 screenplay options, 23 choice nodes.

Actors: Myers (actor 0, spawnSet); Songbird (actor 1, spawnSet); Reed (actor 2, spawnSet); Reed_Escort_001 (actor 3, community); Reed_Escort_002 (actor 4, community); Soldier_001 (actor 5, community); Soldier_002 (actor 6, community); Soldier_003 (actor 7, community); Soldier_004 (actor 8, community); Soldier_005 (actor 9, community); Myers_Escort_001 (actor 10, community); Myers_Escort_002 (actor 11, community); Myers_Escort_003 (actor 12, community); black_ops_crew_001 (actor 13, spawnDespawn); black_ops_crew_002 (actor 14, spawnDespawn); black_ops_crew_003 (actor 15, spawnDespawn); black_ops_crew_004 (actor 16, spawnDespawn); black_ops_crew_005 (actor 17, spawnDespawn); black_ops_crew_006 (actor 18, spawnDespawn); black_ops_crew_007 (actor 19, spawnDespawn); black_ops_crew_008 (actor 20, spawnDespawn); black_ops_crew_009 (actor 21, spawnDespawn); black_ops_crew_010 (actor 22, spawnDespawn); Johnny (actor 23, spawnDespawn); Flyer_001 (actor 24, spawner); Flyer_002 (actor 25, spawner); Flyer_003 (actor 26, spawner); Flyer_004 (actor 27, spawner); Flyer_005 (actor 28, spawner); V (actor 29, findInContext).

Entries: `Start0` → 1; `entering_tunnel_preview` → 4147; `walk_to_roof_preview` → 8068; `entering_landing_area` → 1573; `Start 3` → 8430; `firehose_pulling_preview` → 9406; `last_spot_preview` → 9458; `lift_in` → 5567.

Exits: `myers_intro_cleanup` → 9814; `End 1` → 284; `lift_out` → 5568; `lift_presetup` → 5679; `lift_arrived` → 5696.

End nodes: 284: `NonTerminating`; 5568: `<omitted>`; 5679: `NonTerminating`; 5696: `NonTerminating`; 9814: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 526 / 430 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/1` |
| `scnChangeIdleAnimEvent` | 46 | 23 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 157 | 6 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 47 | 213 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/13` |
| `scnIKEvent` | 94 | 213 / 175 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/5` |
| `scnLookAtAdvancedEvent` | 15 | 1838 / 1506 | `/Data/RootChunk/sceneGraph/Data/graph/152/Data/events/0` |
| `scnLookAtEvent` | 124 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 225 | 62 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 759 / 953 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/17` |
| `scnUnmountEvent` | 47 | 213 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/12` |
| `scneventsAttachPropToNode` | 1 | 7967 / 5314 | `/Data/RootChunk/sceneGraph/Data/graph/666/Data/events/0` |
| `scneventsCameraParamsEvent` | 6 | 3663 / 2458 | `/Data/RootChunk/sceneGraph/Data/graph/266/Data/events/0` |
| `scneventsEquipItemToPerformer` | 45 | 1658 / 1456 | `/Data/RootChunk/sceneGraph/Data/graph/148/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 63 | 213 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/9` |
| `scneventsSocket` | 289 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsVFXEvent` | 38 | 72 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- skeletal_animation, socket_signal: 12
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 11
- skeletal_animation, props_equipment, socket_signal: 9
- skeletal_animation, gaze, socket_signal: 8
- speech, gaze: 7
- speech, skeletal_animation, socket_signal: 6
- speech, skeletal_animation, gaze, socket_signal: 6
- gaze: 6
- speech, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, socket_signal: 5
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, gaze, socket_signal: 3
- skeletal_animation, gaze, props_equipment, socket_signal: 3
- socket_signal: 3
- speech, skeletal_animation: 3
- skeletal_animation: 3
- props_equipment, socket_signal: 3
- speech, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, camera, socket_signal: 2
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze, vfx, socket_signal: 2
- camera: 2
- gaze, socket_signal: 2
- skeletal_animation, idle_animation, vfx, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, audio: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- props_equipment: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `05b955d619ec1304519be08f68897621b0f3c5c6d8dcdc63293fb6a81b546548`. Binary SHA-256: `adfa5258cd62577ddc439c5796162a7978894260d799cfa92c54212d295f1e82`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_06_myers_intro.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_06a_blackops_intro.scene`

140 graph nodes, 161 edges; 13 event-bearing sections, 79 events; 22 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Songbird (actor 0, spawnSet); Black_Ops_001 (actor 1, community); Orbital_Air_001 (actor 2, community); Black_Ops_002 (actor 3, community); Black_Ops_003 (actor 4, community); Civ_001 (actor 5, community); Civ_002 (actor 6, community); Civ_003 (actor 7, community); Orbital_Air_002 (actor 8, community); Civ_004 (actor 9, community); Civ_005 (actor 10, community); Civ_006 (actor 11, community); Civ_007 (actor 12, community); Civ_008 (actor 13, community); Civ_009 (actor 14, spawnDespawn); Orbital_Air_003 (actor 15, community); Orbital_Air_004 (actor 16, community); Black_Ops_005 (actor 17, community); Black_Ops_006 (actor 18, community); Black_Ops_004 (actor 19, community); V (actor 20, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `q306_06a_player_combat` → 166; `q306_06a_somi_exit` → 1041.

End nodes: 2: `<omitted>`; 166: `<omitted>`; 1041: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 187 / 293 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/7` |
| `scnIKEvent` | 10 | 187 / 287 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/2` |
| `scnLookAtEvent` | 4 | 437 / 582 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/3` |
| `scnPlaySkAnimEvent` | 10 | 187 / 282 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/1` |
| `scnUnmountEvent` | 5 | 187 / 292 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/6` |
| `scneventsEquipItemToPerformer` | 2 | 257 / 390 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 187 / 290 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/5` |
| `scneventsSocket` | 19 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 14 | 785 / 676 | `/Data/RootChunk/sceneGraph/Data/graph/101/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `1096cbe10b66d6a532e4d72bfb7b9c0805e5d8a0db16e113ad9cccf0b4fb2b8b`. Binary SHA-256: `43dc6c50f935a873d9baf73ef1717cc353dd07014d95d0708cf7f2e3a9ff748f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_06a_blackops_intro.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_07_somi_duty_free.scene`

292 graph nodes, 369 edges; 56 event-bearing sections, 262 events; 83 screenplay lines, 17 screenplay options, 12 choice nodes.

Actors: Songbird (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); ChopperNPCHack (actor 2, community); Chopper (actor 3, community); ChopperDrone (actor 4, community); V (actor 5, findInContext).

Entries: `Start 0` → 1; `move_on_preview` → 2150; `in_shop_preview` → 2245.

Exits: `End 0` → 2; `kill_signal` → 1212; `chopper_intro_output` → 1928; `Pre-Load_Out` → 224.

End nodes: 2: `NonTerminating`; 224: `NonTerminating`; 1212: `<omitted>`; 1928: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1415 / 762 | `/Data/RootChunk/sceneGraph/Data/graph/114/Data/events/4` |
| `scnChangeIdleAnimEvent` | 8 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 53 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 198 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/7` |
| `scnIKEvent` | 10 | 198 / 199 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |
| `scnLookAtEvent` | 58 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 44 | 33 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scnUnmountEvent` | 5 | 198 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/6` |
| `scneventsAttachPropToPerformer` | 2 | 76 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 1811 / 1157 | `/Data/RootChunk/sceneGraph/Data/graph/171/Data/events/4` |
| `scneventsEquipItemToPerformer` | 1 | 2152 / 1487 | `/Data/RootChunk/sceneGraph/Data/graph/221/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 198 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/2` |
| `scneventsSocket` | 50 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 18 | 1217 / 518 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, gaze: 7
- speech, skeletal_animation, gaze, socket_signal: 6
- skeletal_animation, gaze, socket_signal: 4
- gaze: 4
- skeletal_animation, socket_signal: 3
- speech, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- idle_animation, gaze: 2
- skeletal_animation: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- speech, vfx, socket_signal: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `91301afa69aaef6c0c1d6fcb4b45c88076717a9e560ee128d03a330a3be605db`. Binary SHA-256: `69c64eeb80e1c0e42f3faf44d9baec1d8887d3d34a1bb6bc0d529eaf3abfec7a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_07_somi_duty_free.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_08_control_tower.scene`

525 graph nodes, 641 edges; 57 event-bearing sections, 597 events; 92 screenplay lines, 11 screenplay options, 7 choice nodes.

Actors: Songbird (actor 0, spawnSet); Johnny (actor 1, community); Reed (actor 2, spawnSet); Myers (actor 3, findInContext); Songbird_Voice (actor 4, findInContext); Soldier_001_overpower_cinematic (actor 5, community); Soldier_002_overpower_cinematic (actor 6, community); Soldier_004_overpower_cinematic (actor 7, community); Soldier_003_overpower_cinematic (actor 8, community); Chopper_Health (actor 9, community); Soldier_005_defense_cinematic (actor 10, community); Soldier_006_defense_cinematic (actor 11, community); Soldier_005_overpower_cinematic (actor 12, community); Soldier_006_overpower_cinematic (actor 13, spawnDespawn); Chopper (actor 14, community); Train (actor 15, community); V (actor 16, findInContext).

Entries: `q306_control_tower_defense_in` → 1; `q306_08_ambush_in` → 2774; `q306_08_soldiers_chat_in` → 2779; `q306_08_ctrl_tower_scene` → 1793; `q306_08_songbird_channeling_in` → 280.

Exits: `q306_08_ambush_out` → 2775; `q306_08_soldiers_chat_out` → 2780; `q306_control_tower_defense_enemies_out` → 305; `q306_control_tower_defense_interrput_out` → 2927; `q306_control_tower_defense_enc_start_out` → 5024; `q306_08_clear_npcs` → 2520; `To_maglev_phase` → 2552.

End nodes: 305: `NonTerminating`; 2520: `NonTerminating`; 2552: `NonTerminating`; 2775: `<omitted>`; 2780: `<omitted>`; 2927: `NonTerminating`; 5024: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 67 | 1357 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/5` |
| `scnChangeIdleAnimEvent` | 19 | 1357 / 261 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/2` |
| `scnDialogLineEvent` | 55 | 6 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnIKEvent` | 3 | 1357 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/18` |
| `scnLookAtAdvancedEvent` | 2 | 2290 / 549 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/1` |
| `scnLookAtEvent` | 13 | 1357 / 274 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/13` |
| `scnPlaySkAnimEvent` | 71 | 1357 / 250 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/0` |
| `scneventsAttachPropToPerformer` | 2 | 2298 / 607 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/37` |
| `scneventsCameraParamsEvent` | 4 | 2298 / 576 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/6` |
| `scneventsEquipItemToPerformer` | 9 | 2298 / 579 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/9` |
| `scneventsMountEvent` | 1 | 1443 / 365 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 2 | 1443 / 360 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/14` |
| `scneventsSetAnimsetWeight` | 8 | 1443 / 340 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/1` |
| `scneventsSocket` | 118 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsVFXEvent` | 223 | 43 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21
- skeletal_animation: 7
- socket_signal: 6
- skeletal_animation, socket_signal: 3
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal: 2
- speech, vfx: 1
- speech, skeletal_animation, audio, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, vfx: 1
- vfx, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `901ecc1cc943f85d1bf89e7b5caa1bdab7189fe5b60202b436083cee73d473dd`. Binary SHA-256: `0f28e3d93dc58c600e5aace012f5ec7ec8adb7f4cd141f8da17e5d36ec9ac5e6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_08_control_tower.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_09_monorail.scene`

240 graph nodes, 286 edges; 65 event-bearing sections, 533 events; 130 screenplay lines, 37 screenplay options, 14 choice nodes.

Actors: Songbird (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Reed_Holo (actor 2, spawnSet); mr_x (actor 3, community); Train (actor 4, community); V (actor 5, findInContext).

Entries: `q306_08_enter_train_in` → 456; `preview_anim` → 2358; `ride_in` → 1908; `preview` → 1038; `Start 2` → 1318.

Exits: `ride_out` → 48.

End nodes: 48: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 45 | 710 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnDialogLineEvent` | 114 | 94 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 893 / 527 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/19` |
| `scnIKEvent` | 15 | 893 / 518 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/11` |
| `scnLookAtAdvancedEvent` | 22 | 711 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |
| `scnLookAtEvent` | 46 | 474 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 1 | 852 / 454 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/7` |
| `scnPlaySkAnimEvent` | 101 | 94 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 1 | 852 / 459 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/10` |
| `scnUnmountEvent` | 7 | 893 / 526 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/18` |
| `scneventsAttachPropToPerformer` | 1 | 2506 / 1903 | `/Data/RootChunk/sceneGraph/Data/graph/233/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 2506 / 1902 | `/Data/RootChunk/sceneGraph/Data/graph/233/Data/events/1` |
| `scneventsCameraParamsEvent` | 15 | 717 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |
| `scneventsMountEvent` | 4 | 897 / 558 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/21` |
| `scneventsRagdollEvent` | 2 | 1099 / 633 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/21` |
| `scneventsSetAnimFeatureEvent` | 35 | 717 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |
| `scneventsSetAnimsetWeight` | 36 | 897 / 534 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/1` |
| `scneventsSocket` | 78 | 94 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 2 | 1099 / 620 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 17
- speech: 16
- camera: 5
- speech, skeletal_animation, socket_signal: 3
- speech, gaze: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, camera, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, ik, camera, vfx, socket_signal, animation_state, gameplay_action: 1
- socket_signal: 1
- skeletal_animation, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, socket_signal, animation_state, gameplay_action: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `18bc6a46789bbdc435596b7871005c43ba4729238374b905392e275023eed03b`. Binary SHA-256: `bc43e54835be540919274a78bf6aff9e3639bb4b5e610315d57275f6c433d5db`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_09_monorail.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_10_finale.scene`

474 graph nodes, 735 edges; 134 event-bearing sections, 807 events; 244 screenplay lines, 75 screenplay options, 25 choice nodes.

Actors: Songbird (actor 0, spawnSet); Reed (actor 1, spawnSet); Myers (actor 2, spawnSet); capsule (actor 3, spawner); V (actor 4, findInContext).

Entries: `somi_chater` → 4533; `countdown` → 4535; `deal` → 4538; `iscussion_03` → 4541; `reed_dead_preview` → 4226; `Start 2` → 198; `v_death_setup` → 5608; `retreated_comment_start` → 4283; `sold_preview` → 5231; `standoff_start` → 3122.

Exits: `Reed_Takes_SB_Out` → 469; `Reed_Dead_Out` → 472; `failstate_kill` → 5997; `retreated_end` → 4256; `retreated_comment_end` → 4277; `v_kill_standby` → 5724; `v_shot_dead` → 5730; `End2` → 4459; `End1` → 2663; `draw_weapon` → 3119.

End nodes: 469: `NonTerminating`; 472: `NonTerminating`; 2663: `Terminating`; 3119: `NonTerminating`; 4256: `Terminating`; 4277: `Terminating`; 4459: `Terminating`; 5724: `NonTerminating`; 5730: `NonTerminating`; 5997: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 25 | 1068 / 211 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/7` |
| `scnChangeIdleAnimEvent` | 27 | 286 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnDialogLineEvent` | 193 | 200 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtAdvancedEvent` | 60 | 286 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnLookAtEvent` | 99 | 229 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlaySkAnimEvent` | 204 | 286 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scneventsAttachPropToPerformer` | 2 | 820 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/3` |
| `scneventsAttachPropToWorld` | 12 | 3576 / 1234 | `/Data/RootChunk/sceneGraph/Data/graph/177/Data/events/2` |
| `scneventsEquipItemToPerformer` | 1 | 3125 / 1031 | `/Data/RootChunk/sceneGraph/Data/graph/149/Data/events/4` |
| `scneventsMountEvent` | 1 | 4899 / 2022 | `/Data/RootChunk/sceneGraph/Data/graph/299/Data/events/12` |
| `scneventsPlayRidCameraAnimEvent` | 1 | 5550 / 2607 | `/Data/RootChunk/sceneGraph/Data/graph/385/Data/events/0` |
| `scneventsRagdollEvent` | 3 | 1068 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/25` |
| `scneventsSetAnimFeatureEvent` | 14 | 1068 / 206 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/3` |
| `scneventsSetAnimsetWeight` | 14 | 1068 / 234 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/23` |
| `scneventsSocket` | 126 | 229 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scneventsVFXEvent` | 25 | 2211 / 509 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 29
- speech, skeletal_animation, socket_signal: 18
- speech, skeletal_animation, gaze, socket_signal: 18
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- skeletal_animation, gaze, socket_signal: 6
- speech, gaze, socket_signal: 4
- skeletal_animation, audio, vfx, socket_signal: 4
- speech, props_equipment, audio, socket_signal: 4
- skeletal_animation: 4
- speech, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- speech, gaze: 3
- speech, skeletal_animation: 2
- speech, props_equipment, socket_signal: 2
- socket_signal: 2
- skeletal_animation, idle_animation: 2
- gaze: 2
- skeletal_animation, socket_signal: 2
- idle_animation, props_equipment, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- camera, rid_camera: 1
- skeletal_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, audio: 1

Raw SHA-256: `0078d53a52361b450d695dbdab7fda107d546df725bc6ca397c6da4c2217f89d`. Binary SHA-256: `8f71a737b13daefc8b6ebf0f9ff3e4584c1c684d37106ea7b8965f81d2ee0dda`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_10_finale.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_11_resolution.scene`

499 graph nodes, 577 edges; 93 event-bearing sections, 652 events; 167 screenplay lines, 24 screenplay options, 9 choice nodes.

Actors: Songbird (actor 0, spawnSet); Reed (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); MRBE (actor 3, findInContext); Rocket_Voice (actor 4, findInContext); Soldier_001 (actor 5, community); Soldier_002 (actor 6, community); Soldier_003 (actor 7, community); AV_speaker (actor 8, findInContext); soldier_004_av02 (actor 9, community); soldier_005_av02 (actor 10, community); soldier_006_av02 (actor 11, community); soldier_007_av02 (actor 12, community); AV (actor 13, community); AV_02 (actor 14, community); capsule (actor 15, spawner); V (actor 16, findInContext).

Entries: `q306_11_reed_dead_in` → 1; `prev_dead` → 2291; `retreated_in` → 1975; `q306_11_reed_left_with_somi_in` → 225; `Start 3` → 2592.

Exits: `Prefetch_Aftermath` → 1920; `q306_11_reed_left_with_somi_out` → 227; `q306_11_reed_left_with_somi_destro_out` → 2092; `q306_11_songbird_rocket_ending_out` → 408.

End nodes: 227: `<omitted>`; 408: `<omitted>`; 1920: `NonTerminating`; 2092: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 23 | 823 / 524 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/3` |
| `scnChangeIdleAnimEvent` | 58 | 309 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scnDialogLineEvent` | 106 | 218 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayActionEvent` | 8 | 1343 / 928 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/5` |
| `scnGameplayTransitionEvent` | 7 | 239 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/17` |
| `scnIKEvent` | 14 | 239 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/14` |
| `scnLookAtAdvancedEvent` | 5 | 781 / 481 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/18` |
| `scnLookAtEvent` | 87 | 218 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnOverridePhantomParamsEvent` | 4 | 1022 / 737 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/6` |
| `scnPlaySkAnimEvent` | 110 | 218 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnUnmountEvent` | 7 | 239 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/16` |
| `scneventsAttachPropToNode` | 1 | 3619 / 3631 | `/Data/RootChunk/sceneGraph/Data/graph/479/Data/events/0` |
| `scneventsAttachPropToWorld` | 2 | 1290 / 845 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/5` |
| `scneventsCameraParamsEvent` | 4 | 3589 / 3587 | `/Data/RootChunk/sceneGraph/Data/graph/471/Data/events/0` |
| `scneventsEquipItemToPerformer` | 8 | 781 / 464 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/5` |
| `scneventsMountEvent` | 2 | 239 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/22` |
| `scneventsRagdollEvent` | 2 | 1349 / 979 | `/Data/RootChunk/sceneGraph/Data/graph/105/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 44 | 239 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/12` |
| `scneventsSetAnimsetWeight` | 20 | 239 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scneventsSocket` | 130 | 218 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 1290 / 844 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/4` |
| `scneventsVFXEvent` | 8 | 823 / 539 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, socket_signal: 7
- speech, skeletal_animation, gaze, socket_signal: 6
- gaze: 5
- idle_animation, gameplay_action: 4
- camera: 4
- speech, gaze: 3
- speech, idle_animation: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- socket_signal: 3
- skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, socket_signal, gameplay_action: 2
- speech, skeletal_animation, socket_signal, animation_state, gameplay_action: 2
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, vfx: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, audio, vfx: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal, animation_state: 1
- props_equipment: 1

Raw SHA-256: `955d4bace50ab3a5a3ad705caf8addb28de4dda7041023c6b18b6e5c5594fe5b`. Binary SHA-256: `44c6bf2eb9eb3ac16b94704286c187ddc1c5ea26df2d16bc90f22b3094e92516`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_11_resolution.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene`

22 graph nodes, 24 edges; 7 event-bearing sections, 26 events; 12 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: Alex (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 14 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 12 | 14 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnLookAtEvent` | 3 | 14 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 33 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsSocket` | 5 | 14 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze: 1

Raw SHA-256: `db202c3c4187a5164ed5867c6334a7bb0ef89ed142b717e6002d038ddc0e8e32`. Binary SHA-256: `d5a73d3395630d22f4630396b30f7d31c24f4bc3618b7a2915deb3d829f9c6cb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_12_holo_alex_call.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene`

83 graph nodes, 95 edges; 19 event-bearing sections, 172 events; 40 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `q306_somi_wrap_in` → 1; `q306_reed_wrap_in` → 93.

Exits: `q306_somi_wrap_out` → 2; `End1` → 453; `End2` → 469; `q306_reed_wrap_out` → 95.

End nodes: 2: `NonTerminating`; 95: `NonTerminating`; 453: `<omitted>`; 469: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 204 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/3` |
| `scnChangeIdleAnimEvent` | 9 | 86 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnDialogLineEvent` | 34 | 56 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 204 / 299 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/7` |
| `scnIKEvent` | 8 | 204 / 292 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/1` |
| `scnLookAtEvent` | 5 | 60 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scnOverridePhantomParamsEvent` | 1 | 60 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnPlaySkAnimEvent` | 51 | 56 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 4 | 204 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/6` |
| `scneventsAttachPropToPerformer` | 2 | 118 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 118 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 4 | 204 / 296 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/5` |
| `scneventsSocket` | 46 | 56 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 4
- speech, skeletal_animation, socket_signal: 2
- speech: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1

Raw SHA-256: `ccb4212e1b844c02c7ded886ac2fd7035c3fa355600a6ef970c2f85cf6400057`. Binary SHA-256: `55db353f47160dfd7ca3646b4dfa046dafb1066bb0d548e82df600fdb4c1f49e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_12a_mission_aftermath.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_12b_holo_reed_call.scene`

22 graph nodes, 24 edges; 6 event-bearing sections, 27 events; 11 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: Reed (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 112 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnDialogLineEvent` | 11 | 112 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnLookAtEvent` | 5 | 112 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 114 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scneventsSocket` | 2 | 112 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech: 1

Raw SHA-256: `73aec221016497aa486a08c9a1161f1bedf99ecf95f7374d5ac08266ec639044`. Binary SHA-256: `2eaeffe40ff661e36eb5cb94c8a8b4089c266d0aff798dc5448c631be45ba435`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_12b_holo_reed_call.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene`

207 graph nodes, 250 edges; 68 event-bearing sections, 634 events; 138 screenplay lines, 41 screenplay options, 14 choice nodes.

Actors: Alex (actor 0, spawnSet); TV_PERSON (actor 1, findInContext); Johnny (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `Start0` → 10; `intro_wait` → 1699; `tv_start` → 1663.

Exits: `End 0` → 2; `intro_wait_out` → 1725; `tv_cut` → 1660.

End nodes: 2: `<omitted>`; 1660: `NonTerminating`; 1725: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 1818 / 1703 | `/Data/RootChunk/sceneGraph/Data/graph/189/Data/events/1` |
| `scnChangeIdleAnimEvent` | 15 | 340 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnDialogLineEvent` | 122 | 13 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 423 / 505 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/6` |
| `scnIKEvent` | 6 | 423 / 499 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |
| `scnLookAtAdvancedEvent` | 13 | 403 / 424 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/26` |
| `scnLookAtEvent` | 164 | 13 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 112 | 13 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 5 | 610 / 713 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/7` |
| `scnUnmountEvent` | 3 | 423 / 504 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/5` |
| `scneventsAttachPropToPerformer` | 33 | 361 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |
| `scneventsAttachPropToWorld` | 31 | 361 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/9` |
| `scneventsCameraParamsEvent` | 2 | 1824 / 1716 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 3 | 423 / 502 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/4` |
| `scneventsSocket` | 106 | 13 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXDurationEvent` | 10 | 361 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/14` |
| `scneventsVFXEvent` | 4 | 828 / 1112 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, skeletal_animation, gaze, socket_signal: 9
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 9
- speech, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, camera, audio, vfx: 1
- vfx: 1
- camera: 1

Raw SHA-256: `3dc8df6614734e32a19eea33ecbcf918f0eeb5d155b976ec53a73bbf0e5cab6e`. Binary SHA-256: `cebbb1f5d9eeacc4ab7b0e0098284abfc1695483d27dd75655e2c6a0780916d1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_13_epilogue.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene`

148 graph nodes, 209 edges; 47 event-bearing sections, 312 events; 88 screenplay lines, 23 screenplay options, 8 choice nodes.

Actors: Reed (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Reed_Car (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `Start 0` → 1; `intro_wait` → 1566.

Exits: `End 0` → 2; `intro_wait_out` → 1568; `End2` → 1239; `reed_leave_out` → 994.

End nodes: 2: `NonTerminating`; 994: `NonTerminating`; 1239: `<omitted>`; 1568: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1578 / 1048 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/3` |
| `scnChangeIdleAnimEvent` | 22 | 382 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scnDialogLineEvent` | 71 | 19 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnGameplayActionEvent` | 2 | 1276 / 697 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/0` |
| `scnLookAtAdvancedEvent` | 6 | 382 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/11` |
| `scnLookAtEvent` | 70 | 19 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 77 | 19 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsCameraParamsEvent` | 2 | 1578 / 1047 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 1 | 1276 / 720 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/12` |
| `scneventsSocket` | 58 | 382 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/16` |
| `scneventsVFXEvent` | 2 | 1578 / 1042 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation, socket_signal: 4
- gaze: 3
- skeletal_animation: 3
- speech, skeletal_animation, gaze: 2
- speech, gaze: 2
- speech, idle_animation, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- idle_animation, gameplay_action: 1
- skeletal_animation, camera, audio, vfx: 1
- camera: 1
- vfx: 1

Raw SHA-256: `22c182dd9d42d0baf626e75b2be0cdfae9577fca5a10c7a8ede7840460c0eadd`. Binary SHA-256: `a1b52e0acb354776196d3a6f1a46193eeeccadab938849182216eb5bfd0172ae`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_13b_epilogue_reed.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_post_spaceport.scene`

58 graph nodes, 58 edges; 3 event-bearing sections, 11 events; 3 screenplay lines, 6 screenplay options, 2 choice nodes.

Actors: pilot (actor 0, community); v (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 12 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 1 | 247 / 389 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/0` |
| `scnLookAtEvent` | 2 | 81 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scnPlaySkAnimEvent` | 6 | 12 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 1 | 12 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze: 1
- speech: 1

Raw SHA-256: `9a5490a8cbd030386f12b3dba5152949f3c508f0ef858d7a79e9c02fb9d14159`. Binary SHA-256: `5c60cf07043d9d375ac1bf5b212cacd5205730e5136cfae35006bee1c7b4f0a7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_post_spaceport.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_postcard_alex.scene`

23 graph nodes, 23 edges; 0 event-bearing sections, 0 events; 0 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: .

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `End1` → 52.

End nodes: 2: `NonTerminating`; 52: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |

Presentation families coexisting in an event section (counts are sections, not durations):


Raw SHA-256: `1f4e8e5fa38fa0c6893d4dd70d48eeebaab431e50bb92d103796fd0a99e9a900`. Binary SHA-256: `137ea99fb3894ef2c965f15e9549ab26b62533370dd0a801bafd7ebab702bf27`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_postcard_alex.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene`

32 graph nodes, 32 edges; 2 event-bearing sections, 15 events; 5 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Songbird (actor 0, findInContext); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 101 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnDialogLineEvent` | 3 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 101 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scnIKEvent` | 2 | 101 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scnPlaySkAnimEvent` | 1 | 101 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 1 | 101 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsEquipItemToPerformer` | 1 | 101 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 1 | 101 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSocket` | 3 | 101 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsVFXEvent` | 1 | 101 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- skeletal_animation, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `dce446754f2d1ad495264db7da706bbf34c17b4930b783a21aa112e92ec45010`. Binary SHA-256: `77e8891edfe4abbabb892825d0959ea87cf3cce7a9be4d03f2581f940fe4292d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene" --events
```

## `ep1\quest\main_quests\q306\scenes\q306_tv_bit.scene`

67 graph nodes, 81 edges; 14 event-bearing sections, 38 events; 26 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Journalist (actor 0, community); Wawuda (actor 1, community); chicken_journalist (actor 2, community); chicken_wawuda (actor 3, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 54 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnDialogLineEvent` | 14 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 12 | 57 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scneventsSocket` | 11 | 54 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation, socket_signal: 3
- speech, idle_animation, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation: 1

Raw SHA-256: `e0f9871702126ac7625679f46061ba5dafea7483943b51b34d426800141754f9`. Binary SHA-256: `8fc2d4fa709fea186efbcf804d8683b28084add6d29c843e880cde84e5116bba`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q306\scenes\q306_tv_bit.scene" --events
```

