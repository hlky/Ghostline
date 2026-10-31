# Knockin' on Heaven's Door: scene presentation

Journal identity: `quests/main_quest/act_01/q115_rogues_last_flight`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q115_rogues_last_flight.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q115\scenes\q115_05_halo_jump.scene`

130 graph nodes, 177 edges; 28 event-bearing sections, 291 events; 62 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: rogue (actor 0, spawnSet); weyland (actor 1, spawnSet); q115_av (actor 2, community); Player (actor 3, findInContext); V_POSESSED (actor 4, findInContext).

Entries: `Start 8` → 393; `Start 5` → 283; `halo_jump` → 326; `RID` → 334; `q115_flight_in` → 80; `Start 10` → 471.

Exits: `q115_shot_out` → 83; `everyone_mounted` → 231.

End nodes: 83: `<omitted>`; 231: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 17 | 131 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnChangeIdleAnimEvent` | 6 | 92 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 44 | 87 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 409 / 623 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/0` |
| `scnLookAtEvent` | 19 | 92 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPlayRidAnimEvent` | 4 | 332 / 314 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/4` |
| `scnPlaySkAnimEvent` | 65 | 92 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 6 | 224 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |
| `scneventsSocket` | 50 | 92 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsVFXDurationEvent` | 2 | 161 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/8` |
| `scneventsVFXEvent` | 76 | 161 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, gaze: 2
- vfx: 2
- idle_animation, gameplay_action: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- socket_signal, animation_state: 1
- skeletal_animation, rid_actor, audio, vfx, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, audio, vfx, socket_signal, animation_state: 1

Raw SHA-256: `018847f4a0252025741189f7f0ddb008dd35184c19a06969e14808d4bded4012`. Binary SHA-256: `0e38117864e01bbc845f37495ea5b39c3efecbd7e2e77202626f8d5eefd2834c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_05_halo_jump.scene" --events
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

## `base\quest\main_quests\part1\q115\scenes\q115_08b_garden_guards.scene`

20 graph nodes, 15 edges; 7 event-bearing sections, 17 events; 17 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: guard_01 (actor 0, community); guard_04 (actor 1, community); guard_12 (actor 2, findInWorld); guard_elev (actor 3, community); guard_06 (actor 4, community).

Entries: `chippin_in_commander_in` → 40; `first_in` → 1; `weyland_in` → 8; `commander_in` → 13; `chippin_in_av_in` → 35; `elevator_in` → 18.

Exits: `chippin_in_commander_out` → 41; `first_out` → 2; `weyland_out` → 9; `commander_out` → 14; `chippin_in_av_out` → 36; `elevator_out` → 19.

End nodes: 2: `<omitted>`; 9: `<omitted>`; 14: `<omitted>`; 19: `<omitted>`; 36: `<omitted>`; 41: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 17 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7

Raw SHA-256: `a1c8cab5898c1b58a9d8b3f7f101546251e014077ffbe167d72c3ee9ed0af5b4`. Binary SHA-256: `2e7fcf1c9ac3dc5225857a9e2300c6845d5ecea56c59c4a9a7e74ea9ae312008`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_08b_garden_guards.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_09_security_level.scene`

207 graph nodes, 229 edges; 29 event-bearing sections, 95 events; 57 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: rogue (actor 0, spawnSet); weyland (actor 1, spawnSet); alt (actor 2, spawnDespawn); player (actor 3, findInContext).

Entries: `q115_09_alt_connected_in` → 414; `q115_09_av_in` → 425; `q115_09_atrium_top_in` → 298; `q115_09_atrium_bottom_in` → 300; `q115_09_security_room_in` → 302; `q115_09_fluff_banter_02_in` → 329; `q115_09_fluff_banter_03_in` → 334; `fluff_banter_04_in` → 339; `q115_09_spotted_combat_in` → 373.

Exits: `q115_09_av_out` → 426; `q115_09_in_elevator_out` → 431; `alt_connected` → 1280; `q115_09_atrium_top_out` → 299; `q115_09_atrium_bottom_out` → 301; `q115_09_security_room_out` → 303; `q115_09_fluff_banter_02_out` → 330; `q115_09_fluff_banter_03_out` → 335; `fluff_banter_04_out` → 340; `secret_elevator` → 991; `q115_09_spotted_combat_out` → 374.

End nodes: 299: `<omitted>`; 301: `<omitted>`; 303: `<omitted>`; 330: `<omitted>`; 335: `<omitted>`; 340: `<omitted>`; 374: `<omitted>`; 426: `<omitted>`; 431: `NonTerminating`; 991: `NonTerminating`; 1280: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 44 | 304 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 477 / 211 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/10` |
| `scnIKEvent` | 4 | 477 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/4` |
| `scnLookAtEvent` | 10 | 307 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 437 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/0` |
| `scnUnmountEvent` | 2 | 477 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/9` |
| `scneventsAttachPropToNode` | 1 | 437 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/4` |
| `scneventsAttachPropToPerformer` | 1 | 437 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/2` |
| `scneventsCameraParamsEvent` | 2 | 437 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 477 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/8` |
| `scneventsSocket` | 18 | 394 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- speech, gaze: 2
- skeletal_animation, socket_signal: 2
- socket_signal: 2
- skeletal_animation, gaze: 2
- speech, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, camera, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `7f87cbc4428b36133cae797f9fbc0bb4db4578ce990c8a60a111e94092536cb6`. Binary SHA-256: `4bb5aee6e07eaf8877cc7d3ac2744ab949d0ba37f5d9494cd574038c19985992`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_09_security_level.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_09b_atrium_guards.scene`

20 graph nodes, 19 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: boss (actor 0, community); guard_01 (actor 1, community); burn_1 (actor 2, community); burn_2 (actor 3, community); burn_3 (actor 4, community); burn_lobby_1 (actor 5, community); burn_lobby_2 (actor 6, community); burn_lobby_3 (actor 7, community); burn_lobby_4 (actor 8, community); burn_elev_1 (actor 9, community); burn_elev_2 (actor 10, community); burn_elev_3 (actor 11, community); walkway_2 (actor 12, community); walkway_2_2 (actor 13, community).

Entries: `q115_09b_boss_in` → 1; `q115_09b_guard_in` → 7; `q115_09b_walkway_guard_in` → 71; `q115_09b_burnout_lobby_in` → 37.

Exits: `q115_09b_burnout_lobby_out` → 42; `q115_09b_boss_out` → 2; `q115_09b_guard_out` → 8.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 42: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `49866528f85da68d444bd308a401bde410efa6555bda094cfcd9ae98849b92c9`. Binary SHA-256: `300f8a89dc003a82e43da38a3e4ee000185c6a765c6944b4260b2cc34b171ec2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_09b_atrium_guards.scene" --events
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

