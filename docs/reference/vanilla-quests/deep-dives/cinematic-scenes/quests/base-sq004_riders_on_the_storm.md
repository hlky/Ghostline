# Riders on the Storm: scene presentation

Journal identity: `quests/side_quest/sq004_riders_on_the_storm`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq004_riders_on_the_storm.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq004\scenes\sq004_01_call.scene`

36 graph nodes, 38 edges; 5 event-bearing sections, 48 events; 22 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: Panam (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `sq004_01_call_in` → 1; `call_again` → 44.

Exits: `sq004_01_call_out` → 2; `sq004_01_no_out` → 39.

End nodes: 2: `<omitted>`; 39: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 9 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 22 | 9 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 21 | 9 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 1 | 13 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 3
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation: 1

Raw SHA-256: `036eeae2b95c5662d18c55bd00f83c7fb5f56d3c25ecec8ec258c5794bcdab44`. Binary SHA-256: `2af25de5107e007df5ae6cdbc37eca09049fe2e4f63f346a89502bc1bd15a6ec`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq004\scenes\sq004_01_call.scene" --events
```

## `base\quest\side_quests\sq004\scenes\sq004_02_intro.scene`

606 graph nodes, 749 edges; 109 event-bearing sections, 811 events; 206 screenplay lines, 23 screenplay options, 16 choice nodes.

Actors: Panam (actor 0, spawnSet); Carol (actor 1, spawnSet); Cassidy (actor 2, spawnSet); Bob (actor 3, spawnSet); Mitch (actor 4, spawnSet); Teddy (actor 5, spawnSet); Nomad_01 (actor 6, community); Nomad_02 (actor 7, community); Nomad_03 (actor 8, community); Van (actor 9, spawnSet); Nomad_01_companion (actor 10, community); Nomad_02_companion (actor 11, community); Panam_drone (actor 12, findInContext); panam_vehicle (actor 13, spawnSet); sq004 (actor 14, spawnSet); nomad_deco_car (actor 15, community); V (actor 16, findInContext).

Entries: `Cinedebug_PanamWalk` → 1528; `cinedebug_panamreturn` → 2031; `Start 14` → 2054; `Debug Panams hands` → 3750; `Panam_scenespot` → 3810; `plan_discussion` → 840; `sq004_02_drone_in` → 353; `sq004_02_clear_in` → 400; `cinedebug_Fluff` → 1904.

Exits: `kill_signal_out` → 2160; `plan_discussion_out` → 310; `Kill_signal` → 1818; `sq004_02_drone_out` → 398; `sq004_02_intro_out` → 404; `End 15` → 2452.

End nodes: 310: `NonTerminating`; 398: `NonTerminating`; 404: `NonTerminating`; 1818: `NonTerminating`; 2160: `<omitted>`; 2452: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 934 / 1127 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/6` |
| `scnChangeIdleAnimEvent` | 158 | 104 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnDialogLineEvent` | 141 | 104 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 524 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/16` |
| `scnIKEvent` | 10 | 524 / 348 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/6` |
| `scnLookAtEvent` | 173 | 104 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 131 | 104 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnPoseCorrectionEvent` | 3 | 934 / 1147 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/24` |
| `scnUnmountEvent` | 5 | 524 / 358 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/15` |
| `scneventsAttachPropToNode` | 2 | 934 / 1145 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/22` |
| `scneventsAttachPropToPerformer` | 4 | 934 / 1125 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/4` |
| `scneventsEquipItemToPerformer` | 12 | 829 / 624 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 5 | 524 / 354 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/12` |
| `scneventsSocket` | 146 | 104 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 3 | 1032 / 1317 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/18` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1032 / 1328 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/24` |
| `scneventsVFXEvent` | 7 | 354 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 22
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 16
- skeletal_animation: 15
- speech: 7
- speech, skeletal_animation, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, gaze, socket_signal: 4
- socket_signal: 4
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, idle_animation, gaze, socket_signal: 3
- speech, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, vfx: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, socket_signal: 1
- speech, idle_animation, gaze: 1
- idle_animation, props_equipment, socket_signal: 1

Raw SHA-256: `6da1a0a687f8f52bf7b7a1eebd1f47ac532d1eac72a87b204954a2d7c2da60c0`. Binary SHA-256: `cd2fce13a70ba3214595404f5051f7cf608c6538057747943f2e6e7c147ac224`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq004\scenes\sq004_02_intro.scene" --events
```

## `base\quest\side_quests\sq004\scenes\sq004_04_drive.scene`

76 graph nodes, 70 edges; 21 event-bearing sections, 222 events; 51 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: Panam (actor 0, spawnSet); Mitch (actor 1, spawnSet); Panam_Veh (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `sq004_04_start_in` → 1; `sq004_04_hide_the_scope` → 795; `sq004_04_lookout` → 503; `sq004_04_arrived_in` → 332; `sq004_04_distance_warning` → 516; `sq004_04_arrived_alone_in` → 520; `sq004_scope_prop_in` → 775; `sq004_04_accompany_panam` → 533; `sq004_04_start_rejoin_in` → 540; `panam_exit_van_driver_in` → 850; `panam_exit_van_pass_in` → 852; `sq004_04_skip_lookout` → 547.

Exits: `sq004_04_scope_is_hidden` → 793; `sq004_04_lookout_out` → 506; `kicked_out_kill_signal` → 763; `sq004_04_arrived_alone_out` → 521; `End 18` → 716; `sq004_04_accompany_panam_out` → 535; `sq004_04_arrived_out` → 353; `sq004_04_distance_warning_out` → 542; `panam_exit_van_driver_out` → 851; `panam_exit_van_pass_out` → 853; `sq004_04_skip_lookout_out` → 548.

End nodes: 353: `NonTerminating`; 506: `<omitted>`; 521: `<omitted>`; 535: `<omitted>`; 542: `<omitted>`; 548: `<omitted>`; 716: `<omitted>`; 763: `<omitted>`; 793: `<omitted>`; 851: `<omitted>`; 853: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 785 / 388 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/9` |
| `scnChangeIdleAnimEvent` | 44 | 234 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnDialogLineEvent` | 45 | 234 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnGameplayTransitionEvent` | 5 | 522 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/13` |
| `scnIKEvent` | 10 | 522 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/6` |
| `scnLookAtEvent` | 25 | 234 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnPlaySkAnimEvent` | 43 | 234 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 5 | 522 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/12` |
| `scneventsAttachPropToPerformer` | 1 | 234 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsAttachPropToWorld` | 3 | 785 / 376 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 9 | 234 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsSocket` | 26 | 234 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1
- idle_animation, gaze: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `2c49a4a6601237377cc5b5f4d01f40d0efbbc6359051851c2f847b002b07908a`. Binary SHA-256: `86ea191321e31349bf3150444efcb581f5e29ccf508f9df8012fa852ebf154d8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq004\scenes\sq004_04_drive.scene" --events
```

## `base\quest\side_quests\sq004\scenes\sq004_05_infiltration.scene`

103 graph nodes, 127 edges; 25 event-bearing sections, 90 events; 51 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Panam (actor 0, findInContext); Ganger_outside_01 (actor 1, community); Ganger_outside_02 (actor 2, community); Ganger_main_01 (actor 3, community); Ganger_gate_02 (actor 4, community); Ganger_main_02 (actor 5, community); Ganger_gate_01 (actor 6, community); V (actor 7, findInContext).

Entries: `nomad_girl_in` → 729; `sauls_position_chat_main_hall` → 438; `sauls_position_chat_outdoor` → 454; `ganger_gate_mood_scene` → 498; `sq004_05_panam_back_in` → 399; `lookout_skipped_waiting` → 608; `camera_comment_in` → 829.

Exits: `camera_comment_out` → 834; `End 16` → 733; `sauls_position_chat_out` → 440; `sq004_05_alarm_tripped_out` → 563; `sq004_05_panam_back_in_end` → 477; `lookout_skipped_waiting_out` → 609.

End nodes: 440: `<omitted>`; 477: `<omitted>`; 563: `<omitted>`; 609: `<omitted>`; 733: `<omitted>`; 834: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 446 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |
| `scnDialogLineEvent` | 48 | 389 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnLookAtEvent` | 19 | 389 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 18 | 439 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scneventsSocket` | 2 | 439 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21
- speech, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1

Raw SHA-256: `e3c4c43e1da6971b54e11fc45da8da0292894796f16ce593a5aa2997c3c9b987`. Binary SHA-256: `a5bb878604b7deb878141220a84496ca82cdd6085a7420e73aed3f9f24222a85`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq004\scenes\sq004_05_infiltration.scene" --events
```

## `base\quest\side_quests\sq004\scenes\sq004_06_prison_escape.scene`

229 graph nodes, 286 edges; 46 event-bearing sections, 213 events; 75 screenplay lines, 10 screenplay options, 6 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); sq004_panam_van (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `sq004_06_start_in` → 1; `sq004_06_panam_comes_in` → 473; `debug_stimpack` → 2243; `cinedebug_v_in_first` → 1586; `Cinedebug_SaulEnter` → 953; `sq004_06_stealth_to_jammer` → 520; `cineamtic_debug_van` → 1633; `sq004_06_enter_van_drive_in` → 1636; `sq004_06_basement_entrance` → 542; `Start 19` → 2311; `Start 20` → 2326; `cinedebug_saulenter` → 1058.

Exits: `sq004_06_stealth_to_jammer_out` → 726; `sq004_06_start_stealth_out` → 513; `sq004_06_enter_van_drive_out` → 1637; `sq004_06_panam_comes_in_out` → 603; `sq004_06_start_out` → 391.

End nodes: 391: `NonTerminating`; 513: `NonTerminating`; 603: `NonTerminating`; 726: `NonTerminating`; 1637: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 797 / 386 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/4` |
| `scnChangeIdleAnimEvent` | 25 | 389 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnDialogLineEvent` | 53 | 389 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayActionEvent` | 1 | 907 / 493 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 609 / 274 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/12` |
| `scnIKEvent` | 6 | 609 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/4` |
| `scnLookAtEvent` | 32 | 389 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 40 | 389 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnUnmountEvent` | 1 | 609 / 273 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/11` |
| `scneventsAttachPropToPerformer` | 3 | 756 / 336 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 11 | 609 / 271 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/10` |
| `scneventsSocket` | 37 | 389 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- gaze: 6
- skeletal_animation: 6
- speech, idle_animation: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, ik, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, idle_animation: 1
- ik, socket_signal, animation_state: 1

Raw SHA-256: `df2dde0075eda684c777da793266395fa90e7aa6a3728c187224adf4715a1fcd`. Binary SHA-256: `07ff64bcb282c8a87c9d6bd7819a46ae0f83dde5e1c658b82ac2eb5199681e98`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq004\scenes\sq004_06_prison_escape.scene" --events
```

## `base\quest\side_quests\sq004\scenes\sq004_07_chase.scene`

422 graph nodes, 505 edges; 36 event-bearing sections, 325 events; 68 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); sq004_vehicle (actor 2, spawnSet); Ramming_Car (actor 3, community); Side_road_car (actor 4, community); Jump_over_car (actor 5, community); V (actor 6, findInContext).

Entries: `sq004_07_chase_in` → 1; `jump_over_preview` → 1676; `sq004_07_no_chase_in` → 515; `Cinedebug_chase_car_anim` → 977; `Start 26` → 2638; `Start 17` → 568; `Start1` → 2303; `Start 27` → 2808; `cinedebug_stealth` → 1152; `side_road_preview` → 1624; `Cinedebug_chaseend` → 1215.

Exits: `sq004_07_no_chase_out` → 521; `sq004_07_chase_out` → 610; `sq004_07_chase_failed_out` → 762.

End nodes: 521: `<omitted>`; 610: `NonTerminating`; 762: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 527 / 199 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/9` |
| `scnChangeIdleAnimEvent` | 61 | 496 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 52 | 496 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayActionEvent` | 1 | 553 / 311 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 2469 / 2378 | `/Data/RootChunk/sceneGraph/Data/graph/356/Data/events/4` |
| `scnIKEvent` | 10 | 982 / 877 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/5` |
| `scnLookAtEvent` | 56 | 496 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 81 | 496 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 18 | 514 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/28` |
| `scneventsSocket` | 37 | 514 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/29` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 6
- skeletal_animation: 5
- speech: 3
- gaze, ik, socket_signal, animation_state: 3
- gaze: 3
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- gaze, socket_signal, animation_state: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, audio: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state: 1
- idle_animation, gaze: 1
- ik, socket_signal, animation_state: 1

Raw SHA-256: `f63819f48a3f6a8ac912cd27d3efef77f0201b8226332a35d8d588599cbf070c`. Binary SHA-256: `f96da881cce9e961f7a7d91e89cb96ea1bac563d0474564d91d45e64651ec342`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq004\scenes\sq004_07_chase.scene" --events
```

## `base\quest\side_quests\sq004\scenes\sq004_08_farm.scene`

605 graph nodes, 738 edges; 119 event-bearing sections, 1069 events; 230 screenplay lines, 35 screenplay options, 18 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Johnny (actor 2, spawnSet); sq004van (actor 3, spawnSet); sq004_nomad_bike_02 (actor 4, community); sq004_nomad_bike_01 (actor 5, community); V (actor 6, findInContext).

Entries: `sq004_08_main_in` → 1; `Cinedebug_PanamSaul` → 2066; `Cinedebug_PanamHeater` → 2085; `Cinedebug_PanamBeer` → 2121; `sq004_08_distance_warning` → 639; `sq004_player_exitvan_in` → 4801; `retrofix_in` → 4813; `Start 53` → 4826; `Start 54` → 4831; `Start 55` → 4834; `Start 31` → 4356; `cinedebug_sandgetseverywhere` → 2355; `Cinedebug_heaterchat` → 2875; `Start 46` → 4426; `cinedebug_Fusebox` → 2375; `sq004_farmhouse_chickentest_in` → 3425; `Start 47` → 4465; `Start 48` → 4469; `Start 49` → 4471; `Start 50` → 4520; `Start 0` → 4532; `Start 56` → 5049; `Start 57` → 5053; `cinedebug_panamlegs` → 4030; `cinedebug_Inside` → 2063.

Exits: `sq004_08_distance_warning_out` → 640; `sq004_player_exitvan_out` → 4802; `retrofix_out` → 4821; `sq004_08_main_out` → 901.

End nodes: 640: `<omitted>`; 901: `NonTerminating`; 4802: `<omitted>`; 4821: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 13 | 520 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scnChangeIdleAnimEvent` | 223 | 490 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 168 | 490 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayActionEvent` | 1 | 2738 / 2667 | `/Data/RootChunk/sceneGraph/Data/graph/262/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 1291 / 1480 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/38` |
| `scnIKEvent` | 10 | 1291 / 1435 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/1` |
| `scnLookAtEvent` | 170 | 520 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 259 | 520 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 5 | 1291 / 1479 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/37` |
| `scneventsCameraParamsEvent` | 4 | 1980 / 2052 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 9 | 1291 / 1475 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/34` |
| `scneventsSocket` | 198 | 520 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 4 | 2623 / 2497 | `/Data/RootChunk/sceneGraph/Data/graph/239/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 34
- speech: 9
- skeletal_animation: 9
- gaze: 7
- skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze: 4
- socket_signal: 4
- speech, idle_animation: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation, audio, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation: 2
- skeletal_animation, socket_signal, animation_state: 2
- camera: 2
- speech, idle_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- speech, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- idle_animation, gameplay_action: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- idle_animation: 1

Raw SHA-256: `9af5c29c1b8295cc6863732c547f332c38964d81bb84f83d03ca5226bf29447e`. Binary SHA-256: `43d1fee3a3403be89874e7e6ba69cc087387b7a555f56fc3ff67c8f4a20a71ef`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq004\scenes\sq004_08_farm.scene" --events
```

## `base\quest\side_quests\sq004\scenes\sq004_09_morning_after.scene`

251 graph nodes, 306 edges; 54 event-bearing sections, 359 events; 96 screenplay lines, 14 screenplay options, 6 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Johnny (actor 2, spawnSet); Carol (actor 3, spawnSet); Cassidy (actor 4, spawnSet); Bob (actor 5, spawnSet); Teddy (actor 6, spawnSet); Mitch (actor 7, spawnSet); bikepanam (actor 8, community); bike_player (actor 9, community); PanamVan (actor 10, community); V (actor 11, findInContext).

Entries: `sq004_09_morning_after_in` → 4; `Cinedebug_Dooropen` → 520; `Cinedebug_saul` → 639; `Start 11` → 1601; `Start 13` → 1607; `Start1` → 1381; `sq004_09_mq025_keep_it_clone_in` → 442; `cinedebug_johnny` → 939.

Exits: `sq004_09_morning_after_out` → 7; `sq004_09_mq025_keep_it_clone_out` → 446.

End nodes: 7: `NonTerminating`; 446: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 19 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scnChangeIdleAnimEvent` | 78 | 14 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 61 | 14 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 236 / 469 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/39` |
| `scnIKEvent` | 6 | 236 / 441 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/21` |
| `scnLookAtEvent` | 63 | 14 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 76 | 14 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 3 | 236 / 468 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/38` |
| `scneventsCameraParamsEvent` | 5 | 236 / 411 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 4 | 19 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scneventsSocket` | 46 | 17 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsVFXEvent` | 6 | 236 / 456 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/29` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 9
- skeletal_animation: 9
- gaze: 8
- speech, skeletal_animation, idle_animation, gaze: 4
- speech, idle_animation: 4
- speech, idle_animation, gaze, socket_signal: 2
- speech: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- vfx: 2
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- idle_animation, gaze, camera, vfx, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- idle_animation: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `0f8b44fb84713147c0d1e4841110e48b70fcd5a80db8f5d3bd96df7d9ebbb3df`. Binary SHA-256: `6b7503a542074111df160306ab9cf006d154424d13907fcfb36df57043e9f283`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq004\scenes\sq004_09_morning_after.scene" --events
```

