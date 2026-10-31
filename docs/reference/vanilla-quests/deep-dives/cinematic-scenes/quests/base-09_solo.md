# (Don't Fear) The Reaper: scene presentation

Journal identity: `quests/meta/09_solo`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-09_solo.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q113\scenes\q113_13_adam_smasher.scene`

190 graph nodes, 198 edges; 29 event-bearing sections, 98 events; 40 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: smasher (actor 0, spawnSet); Takemura (actor 1, spawnSet); Hanako (actor 2, spawnSet); smasher_q116 (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `q113_12_adam_in` → 4; `q113_12_adam_defeated_in` → 9; `q113_13_smasher_reinforcements_01_in` → 292; `q113_13_smasher_reinforcements_02_in` → 296; `q113_13_smasher_come_to_daddy_in` → 307; `q113_13_v_low_health_in` → 311; `q113_13_smasher_low_health_in` → 316; `q113_13_smasher_to_takemura_in` → 320; `q113_13_smasher_about_oda_in` → 324; `q113_13_smasher_about_rogue_in` → 332; `q113_13_takemura_to_smasher_01_in` → 336; `q113_13_takemura_to_smasher_02_in` → 340; `q113_13_takemura_to_smasher_03_in` → 341; `q113_13_takemura_tip_rockets_in` → 344.

Exits: `q113_12_adam_out` → 5; `q113_12_adam_defeated_out` → 10; `End 2` → 253; `q113_13_smasher_reinforcements_02_out` → 297; `q113_13_smasher_come_to_daddy_out` → 309; `End1` → 114; `q113_13_v_low_health_out` → 313; `q113_13_smasher_low_health_out` → 318; `q113_13_smasher_to_takemura_out` → 322; `q113_13_smasher_about_oda_out` → 329; `q113_13_smasher_about_rogue_out` → 334; `q113_13_takemura_to_smasher_01_out` → 338; `q113_13_takemura_to_smasher_02_out` → 352; `q113_13_takemura_to_smasher_03_out` → 353; `q113_13_takemura_tip_rockets_out` → 355.

End nodes: 5: `NonTerminating`; 10: `NonTerminating`; 114: `<omitted>`; 253: `<omitted>`; 297: `<omitted>`; 309: `<omitted>`; 313: `<omitted>`; 318: `<omitted>`; 322: `<omitted>`; 329: `<omitted>`; 334: `<omitted>`; 338: `<omitted>`; 352: `<omitted>`; 353: `<omitted>`; 355: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 24 | 606 / 497 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/3` |
| `scnDialogLineEvent` | 31 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 2315 / 664 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/7` |
| `scnIKEvent` | 4 | 2315 / 658 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/2` |
| `scnLookAtEvent` | 1 | 606 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/13` |
| `scnPlaySkAnimEvent` | 7 | 149 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/0` |
| `scnUnmountEvent` | 2 | 2315 / 663 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 2315 / 661 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/5` |
| `scneventsSocket` | 16 | 149 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/2` |
| `scneventsVFXEvent` | 9 | 149 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 22
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, vfx, socket_signal: 1
- vfx: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- vfx, socket_signal: 1

Raw SHA-256: `79a06e02d780ceeb3389dea5d44442016c565af15ada8dd51fdd7fab71aa6be9`. Binary SHA-256: `81cc5ae2686d708c101567d0eef669184109ca2e9aeb4b83851e713a84fe933d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_13_adam_smasher.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_06_regroup.scene`

369 graph nodes, 379 edges; 69 event-bearing sections, 186 events; 144 screenplay lines, 15 screenplay options, 5 choice nodes.

Actors: rogue (actor 0, spawnSet); weyland (actor 1, spawnSet); guard_1 (actor 2, community); guard_2 (actor 3, community); arasaka_ai (actor 4, spawnDespawn); trying_to_get_inside_av (actor 5, community); q115_crashed_av (actor 6, spawner); V (actor 7, findInContext).

Entries: `q115_solo_ai_in` → 1211; `q115_05_birbs_in` → 1218; `commander_dead_in` → 833; `near_elevator_no_weyland_in` → 850; `used_elevator_no_weyland_in` → 856; `secret_elevator_no_weyland_in` → 868; `targeting_weyland_1` → 467; `secret_elevator_weyland_in` → 874; `secret_elevator_ledge_in` → 886; `secret_elevator_in` → 895; `q115_rogue_weyland_to_elev_in` → 1702; `spotted_first_guards_in` → 928; `rogue_second_td_done` → 558; `after_first_guards_in` → 963; `first_guards_player_left_in` → 973; `takedown_activate_in` → 608; `spotted_combat_in` → 1019; `weyland_second_thanks_in` → 621; `q115_05_stealth_takedown_in` → 1039; `landing_in` → 240; `q115_05_use_terminal_in` → 1050; `rogue_first_guards_in` → 245; `q115_05_play_chippin_in` → 1053; `rogue_first_guards_td_in` → 250; `q115_05_lights_in` → 1060; `weyland_thanks_in` → 255; `q115_05_fog_in` → 1065; `rogue_weyland_in` → 260; `rogue_first_guards_02_in` → 265; `commander_keycard_looted_in` → 1076; `q113_lockdown_start_in` → 1105; `Start 20` → 1130; `q115_06_terminal_in` → 1132; `die` → 1139; `regroup_commander_in` → 336; `elevator_fluff_in` → 380; `Start 25` → 1593; `commander_takedown_ready_in` → 799; `Start 27` → 2011.

Exits: `landing_out` → 411; `q115_05_birbs_out` → 1219; `commander_dead_out` → 834; `near_elevator_no_weyland_out` → 851; `used_elevator_no_weyland_out` → 857; `weyland_imprisoned_out` → 465; `secret_elevator_no_weyland_out` → 869; `secret_elevator_weyland_out` → 875; `secret_elevator_ledge_out` → 887; `secret_elevator_out` → 896; `first_guards_sneak_out` → 929; `q115_rogue_weyland_to_elev_out` → 1736; `first_guards_takedown_out` → 930; `after_first_guards_out` → 964; `first_guards_player_left_out` → 974; `guards_move` → 1011; `takedown_activate_out` → 614; `spotted_combat_out` → 1020; `regroup_commander_walk` → 618; ` weyland_second_thanks_out` → 624; `q115_05_stealth_takedown_out` → 1040; `q115_05_use_terminal_out` → 1051; `rogue_first_guards_out` → 246; `q115_05_play_chippin_out` → 1054; `rogue_first_guards_td_out` → 251; `q115_05_lights_out` → 1061; `weyland_to_commander_out` → 256; `q115_05_fog_out` → 1066; `rogue_first_guards_02_out` → 266; `commander_keycard_looted_out` → 1077; `regroup_commander_out` → 343; `elevator_fluff_out` → 383; `weyland_to_elevator_out` → 786; `commander_takedown_ready_out` → 800; `q115_solo_ai_out` → 1208.

End nodes: 246: `<omitted>`; 251: `<omitted>`; 256: `<omitted>`; 266: `<omitted>`; 343: `<omitted>`; 383: `<omitted>`; 411: `NonTerminating`; 465: `<omitted>`; 614: `<omitted>`; 618: `NonTerminating`; 624: `<omitted>`; 786: `<omitted>`; 800: `<omitted>`; 834: `<omitted>`; 851: `<omitted>`; 857: `<omitted>`; 869: `<omitted>`; 875: `<omitted>`; 887: `<omitted>`; 896: `<omitted>`; 929: `<omitted>`; 930: `<omitted>`; 964: `<omitted>`; 974: `<omitted>`; 1011: `NonTerminating`; 1020: `<omitted>`; 1040: `<omitted>`; 1051: `<omitted>`; 1054: `<omitted>`; 1061: `<omitted>`; 1066: `<omitted>`; 1077: `<omitted>`; 1208: `<omitted>`; 1219: `<omitted>`; 1736: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 1138 / 924 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/2` |
| `scnDialogLineEvent` | 103 | 247 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 1138 / 921 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 1535 / 1094 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/7` |
| `scnIKEvent` | 4 | 1535 / 1088 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/1` |
| `scnLookAtEvent` | 17 | 257 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPlaySkAnimEvent` | 19 | 257 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnUnmountEvent` | 2 | 1535 / 1100 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/12` |
| `scneventsCameraParamsEvent` | 3 | 692 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 1535 / 1096 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/9` |
| `scneventsSocket` | 29 | 257 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scneventsVFXEvent` | 3 | 692 / 316 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 43
- speech, socket_signal: 4
- skeletal_animation: 4
- speech, skeletal_animation, gaze: 3
- speech, gaze: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, camera, vfx, socket_signal: 1
- speech, vfx: 1
- skeletal_animation, idle_animation, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `439164211270e7a09bf3d34c248f79f97055262f5551da39bfd332d5d9234796`. Binary SHA-256: `f8604d4eb3e3b20d5cc7d504d6534e7c5b52eea08eee7cd545822dfa5a8e9020`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_06_regroup.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_11_netrunners_nest.scene`

138 graph nodes, 128 edges; 21 event-bearing sections, 65 events; 79 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: Rogue (actor 0, spawnSet); Weyland (actor 1, spawnSet); guard_008 (actor 2, community); operator (actor 3, community); alt (actor 4, spawnDespawn); netrunner_01 (actor 5, community); netrunner_02 (actor 6, community); netrunner_03 (actor 7, community); guard_009 (actor 8, community); arasaka_elevator_ai (actor 9, spawner); guard_shot (actor 10, spawner); V_POSESSED (actor 11, findInContext).

Entries: `q115_elevator_ai_in` → 589; `q115_01_af_nest_in` → 1; `q115_11_spooky_moment_01_in` → 600; `q115_11_spooky_moment_02_in` → 605; `q115_11_spooky_moment_03_in` → 607; `q115_11_spooky_moment_04_in` → 609; `q115_connect_alt_in` → 415; `q115_01_af_kill_in` → 220; `q115_solo_in` → 1204; `q115_01_rogue_start_brief` → 424; `q115_01_af_nest_brief_control_room` → 430; `q115_11_guard_shot_in` → 627; `q115_01_af_nest_brief_alt` → 437; `q115_01_af_nest_access_granted` → 443; `q115_rogue_nest_start_warning` → 448; `q115_get_to_nest_floor_in` → 454; `q115_nest_banter_walkway_in` → 459; `q115_nest_banter_room_in` → 465; `q115_nest_banter_turret_in` → 470; `q115_nest_banter_engineers_in` → 475; `q115_nest_banter_patrols_in` → 480; `q115_11_alt_in_elevator_in` → 687; `q115_nest_overheat_in` → 495; `q114_11_alt_reminder_in` → 897; `spotted_combat_in` → 507; `q115_11_riding_down_long_elevator_in` → 518; `q115_01_af_see_nest_in` → 136; `q115_nest_defeated_everyone_in` → 531; `q115_01_af_glass_in` → 164; `q115_11_NPC_to_gate_in` → 957; `q115_11_netrunners_in` → 568.

Exits: `q115_elevator_ai_out` → 590; `q115_11_spooky_moment_01_out` → 601; `q115_11_spooky_moment_02_out` → 606; `q115_11_spooky_moment_03_out` → 608; `q115_11_spooky_moment_04_out` → 610; `q115_solo_out` → 1205; `q115_11_guard_shot_out` → 631; `q115_rogue_nest_start_warning_end` → 452; `q115_get_to_nest_floor_out` → 455; `q115_nest_banter_walkway_out` → 460; `q115_11_alt_in_elevator_out` → 688; `q114_11_alt_reminder_out` → 898; `spotted_combat_out` → 508; `q115_11_riding_down_long_elevator_out` → 519; `solo_open_door` → 759; `q115_11_NPC_elevator_out` → 958.

End nodes: 452: `<omitted>`; 455: `<omitted>`; 460: `<omitted>`; 508: `<omitted>`; 519: `<omitted>`; 590: `NonTerminating`; 601: `<omitted>`; 606: `<omitted>`; 608: `<omitted>`; 610: `<omitted>`; 631: `<omitted>`; 688: `<omitted>`; 759: `NonTerminating`; 898: `<omitted>`; 958: `<omitted>`; 1205: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 43 | 450 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnLookAtEvent` | 7 | 522 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 522 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |
| `scneventsSocket` | 4 | 588 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/7` |
| `scneventsVFXEvent` | 2 | 588 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, skeletal_animation, gaze: 2
- speech, socket_signal: 2
- skeletal_animation: 2
- speech, gaze, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `3c95461441f6d97125fefa9442df054dcdc65eb9324f40382f5f64d44b30e43a`. Binary SHA-256: `d3f08ebe4b0138497a0f47c02719f45934fc494ee3efef21b986a784d2138b63`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_11_netrunners_nest.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_12b_tower_lobby.scene`

266 graph nodes, 271 edges; 31 event-bearing sections, 106 events; 38 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnDespawn); guard_1 (actor 1, community); arasaka_ai (actor 2, findInContext); minotaur_1 (actor 3, community); minotaur_2 (actor 4, community); minotaur_3 (actor 5, community); guard_voiceover_1 (actor 6, community); guard_voiceover_2 (actor 7, community); guard_voiceover_3 (actor 8, community); guard_voiceover_4 (actor 9, community); Player (actor 10, findInContext).

Entries: `q115_12b_arrive_tower_in` → 4; `q115_12b_many_guards_in` → 9; `Start 0` → 803; `q115_12b_elevator_in` → 29; `q115_12b_loot_in` → 40; `q115_12b_combat_fluff_2_in` → 568; `q115_12b_combat_fluff_3_in` → 573; `q115_12b_elevator_access_in` → 51; `q115_12b_got_loot_in` → 62; `q115_12b_in_elevator_in` → 73; `q115_12b_combat_fluff_1_in` → 84; `q115_12b_heads_up_in` → 897; `Start 5` → 396; `q115_12b_final_mech_in` → 413; `q115_12b_tower_ai_in` → 159; `q115_12b_guard_afam_1_in` → 462; `q115_12b_guard_afam_2_in` → 463; `q115_12b_guard_enus_1_in` → 464; `q115_12b_guard_enus_4_in` → 465; `q115_12b_secret_ending_in` → 1002; `ded_in` → 1010; `in_got_it` → 1023.

Exits: `q115_12b_arrive_tower_out` → 5; `q115_12b_many_guards_out` → 10; `out_got_it` → 1069; `q115_12b_elevator_out` → 30; `q115_12b_loot_out` → 41; `combat_fluff_3_non_terminating_out` → 1103; `q115_12b_elevator_access_out` → 52; `q115_12b_combat_fluff_3_out` → 581; `q115_12b_got_loot_out` → 63; `q115_12b_combat_fluff_out` → 85; `q115_12b_taking_elev_down_out` → 107; `q115_12b_heads_up_out` → 898; `q115_12b_final_mech_out` → 414; `q115_12b_tower_ai_out` → 160; `johnny_mech_reaction` → 435; `End1` → 1224; `End2` → 1228; `q115_12b_guard_afam_1_out` → 466; `q115_12b_guard_afam_2_out` → 467; `q115_12b_guard_enus_1_out` → 468; `q115_12b_guard_enus_4_out` → 469; `despawn_enemies` → 999; `ded_out` → 1011.

End nodes: 5: `NonTerminating`; 10: `<omitted>`; 30: `<omitted>`; 41: `<omitted>`; 52: `<omitted>`; 63: `NonTerminating`; 85: `<omitted>`; 107: `<omitted>`; 160: `NonTerminating`; 414: `NonTerminating`; 435: `NonTerminating`; 466: `<omitted>`; 467: `<omitted>`; 468: `<omitted>`; 469: `<omitted>`; 581: `<omitted>`; 898: `<omitted>`; 999: `NonTerminating`; 1011: `<omitted>`; 1069: `NonTerminating`; 1103: `NonTerminating`; 1224: `<omitted>`; 1228: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 131 / 169 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/7` |
| `scnDialogLineEvent` | 22 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 14 | 11 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 21 | 75 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 131 / 170 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/8` |
| `scneventsEquipItemToPerformer` | 6 | 31 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsSocket` | 28 | 11 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsVFXEvent` | 8 | 108 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- skeletal_animation: 6
- speech, gaze, socket_signal: 3
- speech, gaze, props_equipment, socket_signal: 3
- speech, props_equipment, socket_signal: 3
- skeletal_animation, audio, vfx, socket_signal: 3
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, vfx: 1
- skeletal_animation, camera, audio, vfx, socket_signal: 1
- speech, vfx: 1
- skeletal_animation, socket_signal: 1
- gaze: 1
- vfx: 1

Raw SHA-256: `6004eced5f7dc3de436a1961dfd2895b75188e401e896a0c5c306af0f386511f`. Binary SHA-256: `099f958ffcb76aa963188b6204054c2689ad904f810b318f8ee33d7af2664f5f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_12b_tower_lobby.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_12c_tower_nest.scene`

144 graph nodes, 125 edges; 27 event-bearing sections, 86 events; 36 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: johnny (actor 0, spawnDespawn); alt (actor 1, spawnDespawn); guard_voiceover_1 (actor 2, community); guard_voiceover_2 (actor 3, community); guard_voiceover_3 (actor 4, community); guard_voiceover_4 (actor 5, community); guard_voiceover_5 (actor 6, community); guard_voiceover_6 (actor 7, community); guard_voiceover_7 (actor 8, community); guard_voiceover_8 (actor 9, community); guard_voiceover_9 (actor 10, community); guard_voiceover_10 (actor 11, community); guard_voiceover_11 (actor 12, community); guard_voiceover_12 (actor 13, community); mech (actor 14, community); Player (actor 15, findInContext).

Entries: `q115_12c_arrive_nest_in` → 4; `q115_12c_first_security_in` → 21; `q115_12c_security_booth_in` → 34; `q115_12c_mainframe_in` → 47; `q115_12c_connecting_alt_in` → 60; `q115_12c_alt_connected_in` → 73; `fluff_004` → 344; `fluff_006` → 345; `fluff_008` → 346; `fluff_010` → 347; `fluff_012` → 348; `fluff_011` → 349; `fluff_control_room_1` → 350; `fluff_control_room_2` → 351; `fluff_022` → 352; `fluff_002` → 217; `fluff_023` → 353; `fluff_025` → 354; `q115_12c_see_mainframe_booth_in` → 117; `q115_12c_nest_room_in` → 132.

Exits: `q115_12c_arrive_nest_out` → 5; `q115_12c_first_security_out` → 22; `q115_12c_security_booth_out` → 35; `q115_12c_mainframe_out` → 48; `johnny_can_tp` → 196; `door` → 340; `q115_12c_alt_connected_out` → 74; `End 5` → 366; `End 6` → 367; `End 7` → 368; `End 8` → 369; `End 9` → 370; `End 10` → 371; `End 11` → 372; `End 12` → 373; `End 13` → 374; `End 14` → 375; `End 15` → 376; `killing_monsters` → 106; `End 16` → 377; `q115_12c_see_mainframe_booth_out` → 118; `q115_12c_nest_room_out` → 133.

End nodes: 5: `<omitted>`; 22: `NonTerminating`; 35: `<omitted>`; 48: `<omitted>`; 74: `<omitted>`; 106: `NonTerminating`; 118: `<omitted>`; 133: `NonTerminating`; 196: `NonTerminating`; 340: `NonTerminating`; 366: `<omitted>`; 367: `<omitted>`; 368: `<omitted>`; 369: `<omitted>`; 370: `<omitted>`; 371: `<omitted>`; 372: `<omitted>`; 373: `<omitted>`; 374: `<omitted>`; 375: `<omitted>`; 376: `<omitted>`; 377: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 32 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 36 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/15` |
| `scnIKEvent` | 2 | 36 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scnLookAtEvent` | 12 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 12 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 36 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/14` |
| `scneventsAttachPropToNode` | 1 | 76 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/5` |
| `scneventsAttachPropToPerformer` | 1 | 76 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/2` |
| `scneventsCameraParamsEvent` | 2 | 76 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scneventsEquipItemToPerformer` | 3 | 138 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 36 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsSocket` | 16 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 2 | 36 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- skeletal_animation: 2
- props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation: 1
- speech, gaze, props_equipment, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `69d2c8f3d8ccf8f0e903b749bb70536d19044d8a8c782accb9e6cdd1ebca0157`. Binary SHA-256: `5a3d551637ee8211e89cb62bf2b0aaede0493c7a52b9c8026ea5835579a5f079`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_12c_tower_nest.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_12d_mikoshi.scene`

158 graph nodes, 171 edges; 29 event-bearing sections, 138 events; 45 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: johnny (actor 0, spawnSet); alt (actor 1, spawnDespawn); smasher (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `q115_12d_after_bossfight_in` → 1; `Start 5` → 3765; `q115_12d_bossfight_in` → 7; `Start 4` → 373; `Start 2` → 256; `Start 3` → 271; `q115_12d_to_mikoshi_in` → 150; `q115_12d_mikoshi_room_in` → 155; `q115_12d_mikoshi_access_in` → 160.

Exits: `q115_12d_after_bossfight_out` → 2; `q115_12d_bossfight_out` → 8; `johnny_comment` → 3799; `q115_12d_to_mikoshi_out` → 151; `q115_12d_mikoshi_room_out` → 156; `q115_12d_mikoshi_access_out` → 161.

End nodes: 2: `NonTerminating`; 8: `NonTerminating`; 151: `NonTerminating`; 156: `NonTerminating`; 161: `<omitted>`; 3799: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 234 / 146 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/4` |
| `scnChangeIdleAnimEvent` | 3 | 152 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnDialogLineEvent` | 21 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 10 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 31 | 157 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scneventsCameraParamsEvent` | 5 | 341 / 266 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/2` |
| `scneventsSocket` | 41 | 9 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsVFXEvent` | 22 | 234 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- socket_signal: 3
- skeletal_animation, camera, socket_signal: 3
- speech, gaze: 2
- speech, socket_signal: 2
- gaze, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 2
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- idle_animation: 1
- speech, skeletal_animation, camera, audio, vfx, socket_signal: 1
- gaze: 1

Raw SHA-256: `6f32b9b2d338452e40281c47596193d55cbadd7c69550e47d07754fd2a9cd306`. Binary SHA-256: `9bc34491bc5326ca0938ece59def75b42fee11e7a872064ef33cc4aefb0f7078`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_12d_mikoshi.scene" --events
```

## `base\quest\main_quests\part1\q116\scenes\q116_01_adam_smasher.scene`

170 graph nodes, 221 edges; 34 event-bearing sections, 193 events; 46 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: smasher (actor 0, spawnSet); rogue (actor 1, spawnSet); panam (actor 2, spawnSet); weyland (actor 3, spawnSet); saul (actor 4, spawnSet); alt (actor 5, findInContext); minotaur_1 (actor 6, community); minotaur_2 (actor 7, community); V (actor 8, findInContext); V_possessed (actor 9, findInContext).

Entries: `q116_bossfight_in` → 1; `q116_start_in` → 188; `Start 0` → 907; `q114` → 551; `mech1` → 1222; `mech2` → 1223; `q115` → 520.

Exits: `q116_bossfight_out` → 2; `q116_start_out` → 189.

End nodes: 2: `NonTerminating`; 189: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 515 / 175 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/9` |
| `scnChangeIdleAnimEvent` | 8 | 515 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/10` |
| `scnDialogLineEvent` | 17 | 190 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnLookAtEvent` | 23 | 190 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 44 | 515 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/2` |
| `scneventsAttachPropToNode` | 1 | 515 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/1` |
| `scneventsAttachPropToPerformer` | 3 | 515 / 226 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/37` |
| `scneventsAttachPropToWorld` | 1 | 515 / 234 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/43` |
| `scneventsSocket` | 50 | 190 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsVFXEvent` | 44 | 515 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/20` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- skeletal_animation: 10
- gaze: 4
- skeletal_animation, socket_signal: 3
- speech, gaze, socket_signal: 2
- vfx: 2
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1

Raw SHA-256: `2386c5a14c94c99ba7ed38d1fdcd2ca7e4a6bac3b4b2b67290e4e58a8ceefc36`. Binary SHA-256: `7642406d5e724bfd0fa1c662a7934507d68364a022157291aa9492c92f751eb1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q116\scenes\q116_01_adam_smasher.scene" --events
```

## `base\quest\main_quests\part1\q116\scenes\q116_03b_after_bossfight.scene`

128 graph nodes, 176 edges; 24 event-bearing sections, 106 events; 73 screenplay lines, 15 screenplay options, 7 choice nodes.

Actors: Panam (actor 0, spawnSet); Alt (actor 1, spawnDespawn); rogue (actor 2, spawnSet); weyland (actor 3, spawnSet); smasher (actor 4, spawnSet); saul (actor 5, spawnSet); V (actor 6, findInContext); V_possessed (actor 7, findInContext).

Entries: `q116_03b_after_bossfight_in` → 1; `Start 2` → 345; `panam_to_finale` → 532; `Start 4` → 538; `Start 5` → 572; `Start 8` → 922; `q116_03b_player_dies` → 598; `Start 9` → 959; `panam` → 814.

Exits: `q116_03b_after_bossfight_out` → 16; `q116_03b_player_dies_out` → 752.

End nodes: 16: `NonTerminating`; 752: `Terminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 364 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/2` |
| `scnDialogLineEvent` | 47 | 135 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 382 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/7` |
| `scnIKEvent` | 2 | 382 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |
| `scnLookAtEvent` | 7 | 188 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnPlaySkAnimEvent` | 13 | 183 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnUnmountEvent` | 1 | 382 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/6` |
| `scneventsAttachPropToPerformer` | 4 | 183 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 1 | 382 / 218 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/5` |
| `scneventsSocket` | 25 | 135 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, skeletal_animation, props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- socket_signal: 2
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze: 1
- idle_animation: 1

Raw SHA-256: `80a9c15ecf241698bdd440c7654667a8a1353d1e3a67347760746ba342f3a90f`. Binary SHA-256: `ab7fd4a0d8dd6e6223df7db328daeb4dd0a7820e6b331f6db173023fbcee05c7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q116\scenes\q116_03b_after_bossfight.scene" --events
```

## `base\quest\main_quests\part1\q116\scenes\q116_04_mikoshi_intro.scene`

234 graph nodes, 281 edges; 33 event-bearing sections, 173 events; 52 screenplay lines, 5 screenplay options, 4 choice nodes.

Actors: Panam (actor 0, spawnSet); Alt (actor 1, spawnDespawn); weyland (actor 2, spawnSet); V (actor 3, findInContext); V_possessed (actor 4, findInContext).

Entries: `Start 16` → 747; `Start 12` → 574; `Start 13` → 584; `Start 20` → 1093; `Start 26` → 3596; `Start 22` → 1129; `weyland` → 1377; `Start 24` → 1380; `Start 25` → 1385; `q116_05_jack_in` → 402; `Start 0` → 1150; `Start 17` → 927; `Start 18` → 929; `Start 19` → 931; `falling` → 693; `Start1` → 1225.

Exits: `q116_05_jack_in_out` → 407.

End nodes: 407: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 572 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scnChangeIdleAnimEvent` | 1 | 1135 / 794 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/1` |
| `scnDialogLineEvent` | 22 | 338 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 8 | 370 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnPlaySkAnimEvent` | 59 | 370 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsSocket` | 48 | 370 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsVFXEvent` | 29 | 572 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 7
- skeletal_animation: 7
- skeletal_animation, audio, vfx, socket_signal: 5
- gaze: 4
- speech: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation: 1
- vfx: 1
- socket_signal: 1

Raw SHA-256: `2224624ba09eb1cd45c6c807fa42f04a39de29d6ded3b375ddbb28a1a00f7e74`. Binary SHA-256: `6db44c7d668b4ce00e4aba54c2571ec16e19859895e5e4204acf8d3901a8cd61`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q116\scenes\q116_04_mikoshi_intro.scene" --events
```

