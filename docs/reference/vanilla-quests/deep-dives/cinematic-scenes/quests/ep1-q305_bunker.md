# Somewhat Damaged: scene presentation

Journal identity: `ep1/quests/main_quest/q305_bunker`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q305_bunker.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\main_quests\q305\scenes\q305_05_ambush_scenes.scene`

713 graph nodes, 861 edges; 57 event-bearing sections, 618 events; 88 screenplay lines, 11 screenplay options, 6 choice nodes.

Actors: reed_holo (actor 0, spawnSet); songbird (actor 1, findInContext); maxtac_01 (actor 2, community); maxtac_02 (actor 3, community); maxtac_03 (actor 4, community); maxtac_04 (actor 5, community); maxtac_05 (actor 6, community); maxtac_06 (actor 7, community); maxtac_07 (actor 8, community); maxtac_08 (actor 9, community); maxtac_09 (actor 10, community); maxtac_av_01 (actor 11, community); maxtac_av_02 (actor 12, community); maxtac_av_03 (actor 13, community); maxtac_av_04 (actor 14, community); miniboss_1 (actor 15, community); miniboss_2 (actor 16, community); reed_sniper (actor 17, spawnSet); songbird_prison (actor 18, spawnDespawn); reed_gp (actor 19, community); apc_fake_driver (actor 20, spawnDespawn); 6th_explosive_car_majster_woman (actor 21, community); 6th_explosive_car_majster_man_01 (actor 22, community); 6th_explosive_car_majster_man_02 (actor 23, community); 6th_street_demolition_man (actor 24, community); veh_maxtac_01 (actor 25, community); veh_maxtac_02 (actor 26, community); veh_maxtac_apc (actor 27, community); veh_maxtac_destro_1 (actor 28, community); veh_maxtac_destro_2 (actor 29, community); add_car002 (actor 30, spawner); boom_car1 (actor 31, community); veh_blockade (actor 32, community); V (actor 33, findInContext).

Entries: `Start 0` → 1; `Start 46` → 6536; `Start 21` → 2963; `q305_05_av_drop_start` → 815; `Start 40` → 5160; `Start 32` → 4457; `Start 41` → 5952; `Start 25` → 3825; `Start 43` → 6053; `check_truck_in` → 1013; `Start 27` → 3921; `Start 34` → 4644; `Start 35` → 4654; `Start 22` → 3252; `Start 44` → 6137; `q305_05_maxtac_from_apc` → 1832; `Start 23` → 3344; `Ambush_end_in` → 460; `Start 24` → 3365; `Q305_combat_midway_in` → 506; `Start 45` → 6298; `Q305_combat_reminder_1_in` → 1296; `q305_05_somi_drive_away_in` → 612; `q305_05_v_escape_in` → 638; `q305_05_quest_failed_in` → 654; `Start 31` → 4275.

Exits: `End 0` → 2; `Ambush_end_out` → 2209; `Ambush_hacks` → 812; `q305_05_av_drop_end` → 910; `av_01_out` → 914; `av_02_out` → 915; `av_03_out` → 917; `av_04_out` → 919; `check_truck_out` → 1014; `q305_05_maxtac_out_apc` → 1868; `Q305_combat_midway_out` → 507; `q305_05_v_escape_out` → 640; `q305_05_quest_failed_out` → 660.

End nodes: 2: `NonTerminating`; 507: `NonTerminating`; 640: `NonTerminating`; 660: `NonTerminating`; 812: `NonTerminating`; 910: `<omitted>`; 914: `NonTerminating`; 915: `NonTerminating`; 917: `NonTerminating`; 919: `NonTerminating`; 1014: `NonTerminating`; 1868: `<omitted>`; 2209: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 23 | 185 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scnChangeIdleAnimEvent` | 19 | 462 / 224 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/2` |
| `scnDialogLineEvent` | 48 | 177 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 462 / 237 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/11` |
| `scnGameplayTransitionEvent` | 23 | 462 / 287 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/56` |
| `scnIKEvent` | 46 | 462 / 283 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/52` |
| `scnLookAtEvent` | 28 | 1021 / 582 | `/Data/RootChunk/sceneGraph/Data/graph/95/Data/events/14` |
| `scnPlaySkAnimEvent` | 98 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 6046 / 3394 | `/Data/RootChunk/sceneGraph/Data/graph/491/Data/events/4` |
| `scnUnmountEvent` | 23 | 462 / 286 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/55` |
| `scneventsAttachPropToPerformer` | 1 | 1021 / 567 | `/Data/RootChunk/sceneGraph/Data/graph/95/Data/events/7` |
| `scneventsAttachPropToWorld` | 1 | 972 / 502 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/0` |
| `scneventsCameraParamsEvent` | 25 | 462 / 226 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/4` |
| `scneventsEquipItemToPerformer` | 7 | 3518 / 1923 | `/Data/RootChunk/sceneGraph/Data/graph/278/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 23 | 462 / 280 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/50` |
| `scneventsSocket` | 161 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 6071 / 3442 | `/Data/RootChunk/sceneGraph/Data/graph/499/Data/events/4` |
| `scneventsVFXEvent` | 87 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- skeletal_animation, camera, vfx, socket_signal: 9
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 8
- speech, audio, socket_signal: 4
- skeletal_animation, vfx, socket_signal: 3
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- socket_signal: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, vfx, socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, idle_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1
- props_equipment, socket_signal, animation_state: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1

Raw SHA-256: `d51172abdf6315c86b2442639e1975419832c449f5b78bbd5804258706c368b9`. Binary SHA-256: `0293f55018c27805cc1f2971d394617950541e7229eadd3e8afa12870d21456f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_05_ambush_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_05a_maxtac_commands.scene`

229 graph nodes, 278 edges; 44 event-bearing sections, 48 events; 54 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: maxtac (actor 0, community); droid_maxtac (actor 1, community); maxtac_netrunner (actor 2, community); reed_holo (actor 3, spawnSet); droid_maxtac_backup (actor 4, community); Player (actor 5, findInContext).

Entries: `q305_05a_droid_commands_first_in` → 1; `q305_05a_maxtac_killed_in` → 244; `q305_05_coop_lines1_in` → 950; `q305_05_out_of_range_in` → 958; `q305_05_plan_reminder_in` → 962; `q305_05_fight_reminder1_in` → 968; `q305_05a_additional_comments1_in` → 280; `q305_05a_maxtac_commands_mines2_in` → 1688; `q305_05a_maxtac_commands_sniper2_in` → 1696; `q305_05a_vulgar_comments1_in` → 300; `q305_05a_additional_comments2_in` → 1703; `q305_05a_additional_comments3_in` → 1709; `q305_05a_maxtac_hit_reaction2_in` → 1717; `q305_05a_maxtac_taunt2_in` → 1726; `q305_05a_maxtac_taunt3_in` → 1731; `q305_05a_vulgar_comments2_in` → 1740; `q305_05_coop_lines2_in` → 1752; `q305_05_targeting02_in` → 1761; `q305_05_maxtac_shot2_in` → 1771; `q305_05a_maxtac_commands_mines1_in` → 147; `q305_05_maxtac_shot3_in` → 1781; `q305_05_maxtac_shot4_in` → 1787; `q305_05a_maxtac_commands_sniper1_in` → 160; `q305_05_trashtalk2_in` → 1801; `q305_05_reed_kill_comment2_in` → 1811; `q305_05_targeting01_in` → 880; `q305_05_fight_reminder2_in` → 1820; `q305_05_maxtac_shot1_in` → 892; `q305_05a_maxtac_taunt1_in` → 193; `q305_05_V_killing_comment2_in` → 1828; `q305_05_comment_hotel_in` → 904; `q305_05_trashtalk1_in` → 910; `q305_05_V_killing_comment1_in` → 920; `q305_05a_maxtac_distance_in` → 225; `q305_05a_maxtac_hit_reaction1_in` → 230; `q305_05_reed_kill_comment1_in` → 930.

Exits: `q305_05_reed_kill_comment_out` → 932; `q305_05a_droid_commands_first_out` → 2; `q305_05a_maxtac_killed_out` → 245; `q305_05_coop_lines_out` → 952; `q305_05_out_of_range_out` → 960; `q305_05_plan_reminder_out` → 964; `End1` → 1676; `q305_05_fight_reminder_out` → 978; `q305_05a_additional_comments_out` → 281; `q305_05a_vulgar_comments_out` → 301; `q305_05a_maxtac_commands_mines_out` → 154; `q305_05a_maxtac_commands_sniper_out` → 165; `q305_05_targeting_out` → 882; `q305_05a_maxtac_taunt_out` → 194; `q305_05_maxtac_shot_out` → 894; `q305_05_comment_hotel_out` → 908; `q305_05_trashtalk_out` → 912; `q305_05_V_killing_comment_out` → 922; `q305_05a_maxtac_distance_out` → 226; `q305_05a_maxtac_hit_reaction_out` → 231.

End nodes: 2: `NonTerminating`; 154: `NonTerminating`; 165: `NonTerminating`; 194: `NonTerminating`; 226: `NonTerminating`; 231: `NonTerminating`; 245: `NonTerminating`; 281: `NonTerminating`; 301: `NonTerminating`; 882: `NonTerminating`; 894: `NonTerminating`; 908: `NonTerminating`; 912: `NonTerminating`; 922: `NonTerminating`; 932: `NonTerminating`; 952: `NonTerminating`; 960: `NonTerminating`; 964: `NonTerminating`; 978: `NonTerminating`; 1676: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 48 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 44

Raw SHA-256: `5a3f669998c6f1a172468df69265c78707d4e3a3353852c14d6e0debfe23ea40`. Binary SHA-256: `18618d471f51676564d563e82d5560dda644425923795739e2cae696fc54009b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_05a_maxtac_commands.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_06_chase_scenes.scene`

395 graph nodes, 535 edges; 52 event-bearing sections, 231 events; 121 screenplay lines, 13 screenplay options, 10 choice nodes.

Actors: reed_holo (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); argue_01_ma (actor 2, community); argue_02_wa (actor 3, community); comment_01_ma (actor 4, community); comment_02_ma (actor 5, community); comment_03_ma (actor 6, community); comment_04_wa (actor 7, community); argue_03_ma (actor 8, community); argue_04_ma (actor 9, community); comment_hole_01 (actor 10, community); comment_hole_02 (actor 11, community); dead_max_tac (actor 12, community); scene1_corpo1 (actor 13, community); scene1_looker_2 (actor 14, community); V (actor 15, findInContext).

Entries: `Start 12` → 2636; `Start 5` → 961; `Reed_holo_start_in` → 120; `headlamp_retrofix_in` → 2756; `car_delivery_in` → 1515; `q305_06_chase_comments_in` → 1092; `q305_chase_reed_distance_comment_in` → 731; `headlamp_in` → 2479; `Start 9` → 1652.

Exits: `q305_Johny_about_leap_of_faith_out` → 10; `q305_chase_quest_fail_out` → 874; `headlamp_retrofix` → 2751; `q305_chase_reed_distance_comment_out` → 733; `headlamp_unequip` → 2518; `headlamp_end` → 2564.

End nodes: 10: `NonTerminating`; 733: `NonTerminating`; 874: `<omitted>`; 2518: `NonTerminating`; 2564: `NonTerminating`; 2751: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 53 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 78 | 53 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 1114 / 717 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/35` |
| `scnIKEvent` | 2 | 1114 / 701 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/25` |
| `scnLookAtEvent` | 28 | 53 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 3 | 55 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/29` |
| `scnPlaySkAnimEvent` | 52 | 53 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 1 | 1114 / 716 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/34` |
| `scneventsAttachPropToNode` | 1 | 2480 / 1774 | `/Data/RootChunk/sceneGraph/Data/graph/264/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 2494 / 1793 | `/Data/RootChunk/sceneGraph/Data/graph/268/Data/events/0` |
| `scneventsEquipItemToPerformer` | 2 | 2734 / 2114 | `/Data/RootChunk/sceneGraph/Data/graph/322/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 1 | 1114 / 712 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/31` |
| `scneventsSocket` | 47 | 53 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsUnequipItemFromPerformer` | 1 | 2734 / 2116 | `/Data/RootChunk/sceneGraph/Data/graph/322/Data/events/5` |
| `scneventsVFXEvent` | 6 | 174 / 237 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 34
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, socket_signal: 2
- skeletal_animation, gaze: 2
- props_equipment: 2
- skeletal_animation, vfx, socket_signal: 1
- gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1
- vfx, socket_signal: 1
- speech, vfx: 1
- skeletal_animation, props_equipment, socket_signal: 1
- gaze: 1

Raw SHA-256: `e30b7da07268f053054ca66d4375e97866a7433c6da063898aba93460fac1286`. Binary SHA-256: `4e2080b37718e619606ba71fa5cfbb359e1044cea6deb2554eed42fe5f368121`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_06_chase_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_06b_bunker_intro.scene`

720 graph nodes, 941 edges; 98 event-bearing sections, 750 events; 179 screenplay lines, 20 screenplay options, 8 choice nodes.

Actors: Reed_holo (actor 0, spawnSet); Songbird_holo (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); Security (actor 3, findInContext); songbird_holo_test (actor 4, spawnDespawn); Player (actor 5, findInContext).

Entries: `Start 9` → 3480; `Start 0` → 1; `Debug_before_elevator` → 73; `Start 4` → 2942; `johnny_unplugged` → 1705; `Start 3` → 1721; `q305_project_cynosure_johnny_in` → 350; `Start 5` → 3163; `elevator` → 1100; `Start 6` → 3293; `Start 8` → 3433.

Exits: `q305_08_elevator_scene_out` → 342; `q305_08_elevator_set_up_jumpscare` → 3256; `q305_08_elevator_scene_faster_out` → 667.

End nodes: 342: `<omitted>`; 667: `NonTerminating`; 3256: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 183 / 360 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/9` |
| `scnChangeIdleAnimEvent` | 44 | 105 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |
| `scnDialogLineEvent` | 121 | 103 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 133 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/39` |
| `scnIKEvent` | 12 | 105 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |
| `scnLookAtAdvancedEvent` | 57 | 161 / 322 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/63` |
| `scnLookAtEvent` | 100 | 105 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/8` |
| `scnOverridePhantomParamsEvent` | 9 | 133 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/16` |
| `scnPlaySkAnimEvent` | 136 | 105 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnPoseCorrectionEvent` | 7 | 105 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/7` |
| `scnUnmountEvent` | 5 | 133 / 212 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/37` |
| `scneventsAttachPropToPerformer` | 3 | 3138 / 4257 | `/Data/RootChunk/sceneGraph/Data/graph/503/Data/events/5` |
| `scneventsAttachPropToWorld` | 3 | 2997 / 4085 | `/Data/RootChunk/sceneGraph/Data/graph/484/Data/events/17` |
| `scneventsCameraParamsEvent` | 35 | 161 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scneventsCameraPlacementEvent` | 2 | 2997 / 4066 | `/Data/RootChunk/sceneGraph/Data/graph/484/Data/events/5` |
| `scneventsEquipItemToPerformer` | 14 | 161 / 229 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 5 | 133 / 209 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/35` |
| `scneventsSocket` | 143 | 99 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 4 | 370 / 749 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1280 / 1667 | `/Data/RootChunk/sceneGraph/Data/graph/178/Data/events/1` |
| `scneventsVFXEvent` | 39 | 133 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 31
- skeletal_animation: 9
- speech, socket_signal: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal: 5
- skeletal_animation, gaze: 4
- skeletal_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 2
- gaze: 2
- socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, camera: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1
- vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- vfx, socket_signal: 1
- gaze, socket_signal: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `22c57985a091dafec53d8c705aa0b53b0c9d61c22bbcc28a2fb69d4ae5f428b9`. Binary SHA-256: `f2844c26d11f1089aaf13a7f017a3a234361fd0ab71c6e3517c73960135e028e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_06b_bunker_intro.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08_outer_bunker_scenes.scene`

756 graph nodes, 921 edges; 36 event-bearing sections, 175 events; 45 screenplay lines, 19 screenplay options, 18 choice nodes.

Actors: johnny (actor 0, spawnDespawn); songbird_holo (actor 1, findInContext); security_ghost_01 (actor 2, community); command_ghost_01 (actor 3, community); netwatch_ghost_01 (actor 4, community); Kurtz (actor 5, spawnSet); Songbird (actor 6, spawnSet); myers (actor 7, spawnSet); ripperdoc (actor 8, community); Reed_Holo (actor 9, spawnSet); fake_robot (actor 10, community); Fake_songbird (actor 11, spawnSet); Security (actor 12, findInContext); cerberus (actor 13, community); V (actor 14, findInContext).

Entries: `Airlock Jumpscare` → 5766; `q305_airlock_doors_in` → 2490; `q305_08_robot_hits_door_in` → 31; `q305_08_see_robot_in` → 36; `q305_08_printing_room_in` → 1724; `q305_08_gate_shuts_down_in` → 161; `Start 71` → 5912; `Start 72` → 5917; `Start 73` → 5922; `Debug_prop_activation` → 7571; `Start 79` → 7740; `debug_gate_preview` → 3669; `q305_open_the_gate` → 2113; `q305_08_jumpscare_with_cargo` → 6231; `Start 64` → 5486; `Start 65` → 5552; `q305_08_engineering_jumpscare_in` → 1462; `q305_08_video_commented_in` → 1463; `Start 67` → 5724.

Exits: `q305_airlock_doors_out` → 2491; `q305_08_printing_room_out` → 1725; `q305_08_gate_shuts_down_out` → 162; `Autosaving_out_02` → 5207; `autosaving_out_03` → 5215; `End 53` → 6241; `q305_airlock_doors_terminating_out` → 7947; `q305_08_video_commented_out` → 1467; `dataterm_bravo_ou` → 4795.

End nodes: 162: `NonTerminating`; 1467: `<omitted>`; 1725: `<omitted>`; 2491: `NonTerminating`; 4795: `NonTerminating`; 5207: `NonTerminating`; 5215: `NonTerminating`; 6241: `NonTerminating`; 7947: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 13 | 1872 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/4` |
| `scnChangeIdleAnimEvent` | 22 | 1872 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/3` |
| `scnDialogLineEvent` | 24 | 1129 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 3400 / 605 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/8` |
| `scnIKEvent` | 4 | 3400 / 595 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/1` |
| `scnPlaySkAnimEvent` | 27 | 1872 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/0` |
| `scnUnmountEvent` | 2 | 3400 / 610 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/12` |
| `scneventsCameraParamsEvent` | 2 | 2554 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 2 | 3400 / 606 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/9` |
| `scneventsSocket` | 24 | 1872 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/10` |
| `scneventsVFXDurationEvent` | 1 | 1872 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/5` |
| `scneventsVFXEvent` | 52 | 1872 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- skeletal_animation, idle_animation: 6
- skeletal_animation, idle_animation, socket_signal: 4
- skeletal_animation: 2
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, socket_signal: 1
- camera, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx: 1

Raw SHA-256: `5fdc129b5c00d312824482381abb32fdb886bd119ce7bf85abcc013eb97056b7`. Binary SHA-256: `491fb0cb352d2e78008a10aafcb7267dcb874a8e728038f615229d31d451b9ca`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08_outer_bunker_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08b_bunker_holocalls.scene`

212 graph nodes, 253 edges; 78 event-bearing sections, 91 events; 121 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Songbird_holo (actor 0, spawnSet); Security (actor 1, spawnSet); Blackwall_AI (actor 2, spawnSet); Cerberus (actor 3, community); Cerberus_inner_bunker (actor 4, community); V (actor 5, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 3.

End nodes: 3: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 91 | 32 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 78

Raw SHA-256: `a6264adce0048f9c7d9110562387b0aa21ce6a00d409204e55f6cd0dc9de2409`. Binary SHA-256: `5cc3a388c2086ddebd6a6bf5309ba8842940fc8278f8ce94ae9f1dd7ae003563`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08b_bunker_holocalls.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08c_outer_bunker_hallucination_kurt.scene`

92 graph nodes, 98 edges; 12 event-bearing sections, 116 events; 23 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Kurt (actor 0, community); Songbird (actor 1, community); Songbird_holo (actor 2, spawnSet); Kurt_soldier_01 (actor 3, community); Kurt_soldier_02 (actor 4, community); cerberus_foreshadow (actor 5, community); Player (actor 6, findInContext).

Entries: `Start 0` → 1; `Start 2` → 724; `Start 3` → 760; `Start 4` → 762; `Cerb_foreshadow` → 1283; `Start 5` → 777; `Start 6` → 789.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 945 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/1` |
| `scnChangeIdleAnimEvent` | 4 | 32 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnDialogLineEvent` | 9 | 32 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scnGameplayTransitionEvent` | 2 | 32 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/25` |
| `scnIKEvent` | 4 | 32 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/17` |
| `scnLookAtEvent` | 21 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 32 | 32 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnUnmountEvent` | 2 | 32 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/26` |
| `scneventsSetAnimFeatureEvent` | 2 | 32 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/22` |
| `scneventsSocket` | 28 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXDurationEvent` | 4 | 945 / 436 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scneventsVFXEvent` | 6 | 652 / 248 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 4
- vfx: 3
- gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- audio, vfx, socket_signal: 1

Raw SHA-256: `ae554e794a5f6d739d0ae41946a541d5540d3816f16f8036988d4841215181f1`. Binary SHA-256: `e5d19071d26a9ec7faa14b405f71a64639e7f425e147bcb06ffa1b71ccfdc2cc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08c_outer_bunker_hallucination_kurt.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08d_outer_bunker_hallucination_upgrade.scene`

97 graph nodes, 96 edges; 10 event-bearing sections, 131 events; 59 screenplay lines, 5 screenplay options, 0 choice nodes.

Actors: Myers (actor 0, spawnSet); Songbird (actor 1, community); Songbird_holo (actor 2, spawnSet); Technician (actor 3, community); Nurse1 (actor 4, community); Nurse2 (actor 5, community); corridor_personel1 (actor 6, spawnDespawn); corridor_personel2 (actor 7, spawnDespawn); Player (actor 8, findInContext).

Entries: `Start 0` → 1; `Start 1` → 223; `Start 12` → 903; `Start 4` → 685; `Start 5` → 691; `Start 6` → 697; `Start 7` → 699; `Start 8` → 721; `preview` → 284; `Start 13` → 958; `Start 2` → 526; `Start 15` → 1466; `Start 11` → 847; `Start 14` → 1104.

Exits: `End 0` → 2; `End 1` → 262.

End nodes: 2: `<omitted>`; 262: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 13 | 99 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnDialogLineEvent` | 11 | 99 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/30` |
| `scnLookAtEvent` | 52 | 99 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/6` |
| `scnPlaySkAnimEvent` | 23 | 51 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsAttachPropToPerformer` | 3 | 51 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsCameraParamsEvent` | 1 | 1329 / 468 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/0` |
| `scneventsEquipItemToPerformer` | 3 | 76 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scneventsSocket` | 11 | 51 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scneventsVFXEvent` | 14 | 51 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 3
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, vfx: 1
- speech: 1
- camera: 1

Raw SHA-256: `c17b34d6d8b0c963328946884d172bfbd38acc8cffa467b66849604735d9b9fd`. Binary SHA-256: `60c41814feefb0ec4016da939db3b7e84dca68e772f6021ed21ecc0216569c88`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08d_outer_bunker_hallucination_upgrade.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08e_outer_bunker_cerberus_voice.scene`

125 graph nodes, 212 edges; 26 event-bearing sections, 26 events; 26 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Songbird__BW (actor 0, spawnSet); Songbird (actor 1, spawnSet).

Entries: `Start 0` → 1; `chase_debug_in` → 371.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 26 | 35 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 26

Raw SHA-256: `8f4ffa283f95ec89445e13006b289eab62e10195ca8f390a32d71e0beb6cb414`. Binary SHA-256: `c6f2b714b5891743e3cc990b98525cce89206a55bd64fbf4900675c03af25ebe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08e_outer_bunker_cerberus_voice.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08f_outer_bunker_minor_hallucinations.scene`

82 graph nodes, 94 edges; 8 event-bearing sections, 42 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: songbird_smoke (actor 0, community); songbird_netrunner (actor 1, community); songird_gate (actor 2, community); songbird_wheelchair (actor 3, community); Player (actor 4, findInContext).

Entries: `Start 3` → 130; `Start 6` → 369; `Start 4` → 154; `Start 7` → 979; `Start 2` → 49; `in_smoking` → 82; `behind_the_gratings` → 106.

Exits: `End 6` → 894.

End nodes: 894: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 380 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/5` |
| `scnChangeIdleAnimEvent` | 3 | 44 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 67 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnIKEvent` | 2 | 67 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnLookAtEvent` | 3 | 44 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 6 | 67 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnUnmountEvent` | 1 | 67 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsEquipItemToPerformer` | 1 | 170 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 1 | 67 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsSocket` | 16 | 44 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 803 / 319 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/2` |
| `scneventsVFXEvent` | 6 | 67 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- socket_signal: 2
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `d7b349ffdc0c59ae3051c19d41af00549769f3d2e76e8676413adcbbc0bc3035`. Binary SHA-256: `07e6f3bdb80d45880e04a2eb097e8440588fd6ab674012e0d19886f721850fbf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08f_outer_bunker_minor_hallucinations.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08g_outer_bunker_cerberus_intro.scene`

462 graph nodes, 465 edges; 12 event-bearing sections, 138 events; 21 screenplay lines, 4 screenplay options, 4 choice nodes.

Actors: Cerberus (actor 0, community); Fake_robot (actor 1, community); Songbird (actor 2, findInContext); Blackwall_AI (actor 3, findInContext); Player (actor 4, findInContext).

Entries: `Start 0` → 1; `debug_crawl_under_server_in` → 14; `debug_crawl_back_in` → 39; `Start 7` → 2302; `Start 3` → 1810; `test_killroom` → 1811; `Start 6` → 1858; `Start 1` → 406.

Exits: `q305_robot_introduction_out` → 184.

End nodes: 184: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 8 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnChangeIdleAnimEvent` | 10 | 8 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 10 | 257 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/37` |
| `scnPlaySkAnimEvent` | 21 | 8 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraParamsEvent` | 12 | 257 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/4` |
| `scneventsSocket` | 58 | 8 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 17 | 37 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation: 4
- speech, skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 2
- speech: 2
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `fea184a2f8c7a33f105cf6369d7cf13aec538e3cc4bf22746d228b9c143b3fa4`. Binary SHA-256: `19917918f66bfc33025eae7651fd94cb46d7379581cf676eb60627648749e569`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08g_outer_bunker_cerberus_intro.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08h_outer_bunker_killroom.scene`

258 graph nodes, 448 edges; 61 event-bearing sections, 169 events; 82 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: cerberus (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 1` → 313; `Start 0` → 1; `Start 11` → 50; `debug` → 153; `Waiti_for_grab_in` → 816; `instant_killroom` → 1511.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnPlaySkAnimEvent` | 109 | 170 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scneventsCameraParamsEvent` | 2 | 231 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/0` |
| `scneventsSocket` | 58 | 170 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 52
- skeletal_animation: 7
- camera, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `8638356044c06f7e36eccee3cefd5f6f6bb163bcc97cdb60e2547167a2a56f73`. Binary SHA-256: `ad8a8eb536c7cc2b2ef28ca0aa6a0bacd9b90f297dfa7739a4212b48d2e983cd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08h_outer_bunker_killroom.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09_inner_bunker_scenes.scene`

642 graph nodes, 762 edges; 29 event-bearing sections, 60 events; 56 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: songbird (actor 0, findInContext); Robot (actor 1, community); security (actor 2, findInContext); SongbirdBW (actor 3, findInContext); Cerberus_hunting (actor 4, community); V (actor 5, findInContext); Player (actor 6, findInContext).

Entries: `q305_09_enter_command_chamber_in` → 13; `q305_09_system_reset_in` → 52; `q305_10_kill_robot` → 2087; `Q305_09_IB_airlock_wait_in` → 10998; `Q305_09_IB_airlock_adjusting_pressure_in` → 10999; `Q305_09_IB_airlock_opened_in` → 11001; `Q305_09_IB_airlock_close_in` → 11003; `Q305_09_IB_command_room_computer_in` → 281; `q305_09_trolley_inner_bunker` → 9139; `trolley_devil_from_the_box` → 9154; `q305_09_subsystems_in` → 1150; `Start 18` → 8605; `trolley_compression` → 9296.

Exits: `autosaving_out` → 8131; `q305_09_enter_command_chamber_out` → 16; `End 15` → 8145; `q305_09_interupt_coolant_out` → 22; `End 13` → 2092; `Q305_09_IB_airlock_adjusting_pressure_out` → 11009; `Q305_09_IB_airlock_wait_out` → 11011; `Q305_09_IB_airlock_opened_out` → 11014; `Q305_09_IB_airlock_close_out` → 11016; `Q305_09_IB_command_room_computer_out` → 282; `Terminating_Scene_out` → 11301; `q305_09_subsystems_out` → 1205.

End nodes: 16: `NonTerminating`; 22: `NonTerminating`; 282: `NonTerminating`; 1205: `NonTerminating`; 2092: `<omitted>`; 8131: `NonTerminating`; 8145: `NonTerminating`; 11009: `NonTerminating`; 11011: `NonTerminating`; 11014: `NonTerminating`; 11016: `NonTerminating`; 11301: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 9140 / 1810 | `/Data/RootChunk/sceneGraph/Data/graph/283/Data/events/1` |
| `scnChangeIdleAnimEvent` | 6 | 9140 / 1811 | `/Data/RootChunk/sceneGraph/Data/graph/283/Data/events/2` |
| `scnDialogLineEvent` | 26 | 610 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 7 | 3557 / 568 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/5` |
| `scneventsSocket` | 6 | 3557 / 565 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/2` |
| `scneventsVFXEvent` | 13 | 3557 / 563 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 22
- skeletal_animation, idle_animation: 3
- skeletal_animation, vfx, socket_signal: 1
- speech, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, idle_animation, audio, vfx: 1

Raw SHA-256: `a201e320dd83a3bb657af3e450365f1e57ae5442ca96482589d3bbed83f2653f`. Binary SHA-256: `bb83f7c46664921d91ad212251ab81fa43fb945433fa07b5952c49105b0fdb95`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09_inner_bunker_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09a_inner_bunker_hallucination_oath.scene`

142 graph nodes, 178 edges; 13 event-bearing sections, 213 events; 39 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: Myers (actor 0, spawnDespawn); Songbird (actor 1, spawnDespawn); Songbird_holo (actor 2, spawnSet); Reed (actor 3, community); Songbird2 (actor 4, spawnDespawn); Player (actor 5, findInContext).

Entries: `Start 0` → 1; `Start 7` → 1678; `Start 3` → 862; `preview` → 1786; `Start 9` → 2222; `Start 5` → 974; `Start 6` → 1629; `Start1` → 2473.

Exits: `End 0` → 2; `End 1` → 1619.

End nodes: 2: `<omitted>`; 1619: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 795 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/12` |
| `scnChangeIdleAnimEvent` | 22 | 795 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnDialogLineEvent` | 19 | 795 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/8` |
| `scnLookAtAdvancedEvent` | 11 | 795 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/63` |
| `scnLookAtEvent` | 46 | 795 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |
| `scnPlaySkAnimEvent` | 52 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 5 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 30 | 663 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scneventsVFXEvent` | 21 | 795 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, animation_state: 2
- skeletal_animation, socket_signal: 2
- vfx: 2
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- gaze, vfx, socket_signal, animation_state: 1
- skeletal_animation, vfx, socket_signal: 1
- socket_signal: 1
- skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `fd06d71d08a9ad64d8f1b51caf8e14fbca96e7a52ec551eadcbf4889b095c221`. Binary SHA-256: `b652f7a06420209834929193e6e97d3127b41b10c952425fea4289a3020eddd5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09a_inner_bunker_hallucination_oath.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09b_inner_bunker_hallucination_flatline.scene`

273 graph nodes, 392 edges; 23 event-bearing sections, 279 events; 70 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: Reed (actor 0, community); Songbird (actor 1, community); Songbird_holo (actor 2, spawnSet); Reed2 (actor 3, community); Songbird2 (actor 4, community); Reed3 (actor 5, community); Songbird3 (actor 6, community); Reed4 (actor 7, community); Songbird4 (actor 8, community); Reed_holo (actor 9, spawnSet); Player (actor 10, findInContext).

Entries: `Start 0` → 1; `2nd instance` → 399; `3rd instance` → 434; `4rd instance` → 1419; `Start 9` → 2114; `Start 10` → 2116; `Start 5` → 1821; `Start 11` → 2151; `Start 12` → 2184; `Start 13` → 2189; `Start 14` → 2216; `escalation_preview` → 2546; `audible_hallucination_in` → 2249.

Exits: `End 4` → 2843; `End 3` → 1963.

End nodes: 1963: `<omitted>`; 2843: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 26 | 313 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnDialogLineEvent` | 49 | 313 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnLookAtAdvancedEvent` | 1 | 1910 / 1066 | `/Data/RootChunk/sceneGraph/Data/graph/134/Data/events/11` |
| `scnLookAtEvent` | 24 | 313 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnPlaySkAnimEvent` | 55 | 223 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPoseCorrectionEvent` | 7 | 313 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/25` |
| `scneventsAttachPropToPerformer` | 5 | 313 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scneventsEquipItemToPerformer` | 1 | 797 / 411 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |
| `scneventsSocket` | 66 | 223 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 313 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/24` |
| `scneventsVFXEvent` | 44 | 306 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 2
- socket_signal: 2
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- vfx: 1

Raw SHA-256: `9dcff607112d0d8fd80433f9e0aa8841cdb83feb645c9c8f0339416c0c2f58ea`. Binary SHA-256: `e6c0f029c7e20fa38518be9714decb0f68a8f5adfdbd25a6d541649fe4a97f07`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09b_inner_bunker_hallucination_flatline.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09c_inner_bunker_minor_hallucinations.scene`

87 graph nodes, 98 edges; 12 event-bearing sections, 61 events; 17 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: somi_angry (actor 0, community); somi_nightmare (actor 1, community); somi_crying (actor 2, community); somi_typing (actor 3, community); computer (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `start_ib_hallucinations` → 1; `Start 5` → 240; `somi_on_stairs_preview` → 10; `Start 6` → 269; `Start 2` → 40; `Start 7` → 277; `Start 3` → 69; `Start 4` → 82.

Exits: `End 4` → 646.

End nodes: 646: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 9 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 5 | 9 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnLookAtAdvancedEvent` | 6 | 9 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnLookAtEvent` | 2 | 83 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 15 | 9 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsSocket` | 18 | 9 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsVFXEvent` | 8 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- idle_animation, socket_signal: 3
- vfx: 3
- socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `0ad71f8221a066230a671be7fcdcf101bf0c113560bf6a4f37bbbb240fa82d5e`. Binary SHA-256: `fddee1d8b7409aa967ee0c2a5c7e478882d59d27358a53002dd9deec49e13f80`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09c_inner_bunker_minor_hallucinations.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09d_cerberus_finale.scene`

102 graph nodes, 117 edges; 3 event-bearing sections, 57 events; 7 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Cerberus (actor 0, community); Songbird (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 2` → 277; `q305_09_system_reset_in` → 38; `Cerber_dead` → 101.

Exits: `q305_09_system_reset_out` → 4; `End 1` → 113.

End nodes: 4: `NonTerminating`; 113: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 8 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnChangeIdleAnimEvent` | 3 | 8 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 3 | 8 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnPlaySkAnimEvent` | 5 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsCameraParamsEvent` | 5 | 8 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsSocket` | 17 | 8 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsVFXEvent` | 19 | 8 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- vfx: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `db2de1f50e95b1a54e021eea232377ded583c8e8cdcdf7fdce70006d2c357c0d`. Binary SHA-256: `a48f89c29bededb03b67fd22aa2d6a965143e4964517540f1f148643ba27e4f4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09d_cerberus_finale.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09e_inner_bunker_lab_scenes.scene`

207 graph nodes, 300 edges; 20 event-bearing sections, 336 events; 35 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: Cerberus (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 18` → 1365; `Start 13` → 1175; `Start 20` → 808; `Start 10` → 629; `Start 5` → 441; `Start 4` → 261; `Start 11` → 1101; `Start 12` → 1105; `Start 1` → 140; `Start 19` → 1492; `Start 2` → 142; `Start 16` → 1309; `Start 6` → 542; `Start 7` → 544; `Start 8` → 555; `CP77-65722_IN` → 1917; `Start 9` → 569; `Start 17` → 1342; `Start 3` → 189.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 30 | 10 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnChangeIdleAnimEvent` | 61 | 10 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnGameplayTransitionEvent` | 15 | 10 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/21` |
| `scnIKEvent` | 30 | 10 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/18` |
| `scnPlaySkAnimEvent` | 56 | 10 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnUnmountEvent` | 15 | 10 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/20` |
| `scneventsRagdollEvent` | 1 | 501 / 556 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 19 | 10 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scneventsSetAnimsetWeight` | 2 | 501 / 554 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/10` |
| `scneventsSocket` | 101 | 10 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsVFXEvent` | 6 | 634 / 712 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- skeletal_animation, idle_animation, audio, vfx: 4
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- idle_animation: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, vfx: 1

Raw SHA-256: `bcbf53d87e6e69f04d441e2562970ea1c7f0c013e880de3de06ed68d084c95ed`. Binary SHA-256: `57a2d334a9a4389b23317eaccc56613f85acc8a3a6b53ee899dab36f6b421c78`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09e_inner_bunker_lab_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09f_inner_bunker_killroom.scene`

278 graph nodes, 495 edges; 64 event-bearing sections, 180 events; 70 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Cerberus (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `instant_killroom` → 1191; `Start1` → 612; `Start 11` → 50.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnPlaySkAnimEvent` | 115 | 58 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scneventsCameraParamsEvent` | 2 | 956 / 1470 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/0` |
| `scneventsSocket` | 60 | 28 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |
| `scneventsVFXEvent` | 3 | 28 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 55
- skeletal_animation: 7
- vfx, socket_signal: 1
- camera, socket_signal: 1

Raw SHA-256: `b5e2ff6a45aa28e6f216dd77515fce701b28fb25198a6833ab532db980c41836`. Binary SHA-256: `2991083218edac7d97294abfafb7e5e65b12725970e693964eb2141c548c53f8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09f_inner_bunker_killroom.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_10_songbird_finale.scene`

203 graph nodes, 253 edges; 53 event-bearing sections, 751 events; 134 screenplay lines, 32 screenplay options, 12 choice nodes.

Actors: Songbird (actor 0, spawnSet); Reed (actor 1, spawnSet); reed_holo (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `Start 0` → 1; `Start 2` → 861; `Start 1` → 717; `Start 4` → 1195.

Exits: `End 0` → 2; `prefetch_out` → 728.

End nodes: 2: `<omitted>`; 728: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 64 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnChangeIdleAnimEvent` | 73 | 6 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scnDialogLineEvent` | 81 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnIKEvent` | 24 | 23 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scnLookAtAdvancedEvent` | 68 | 23 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/10` |
| `scnLookAtEvent` | 65 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnPlaySkAnimEvent` | 272 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 22 | 6 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsCameraParamsEvent` | 10 | 230 / 623 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/12` |
| `scneventsSocket` | 69 | 6 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/23` |
| `scneventsVFXEvent` | 3 | 313 / 799 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/18` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 6
- speech, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- gaze: 4
- speech, skeletal_animation, gaze, audio, socket_signal: 3
- speech: 3
- speech, audio: 2
- skeletal_animation, idle_animation, camera, audio, socket_signal: 2
- skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, socket_signal: 1
- idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, camera, socket_signal: 1

Raw SHA-256: `695fbf3f31f67d142dbc5dddd7a577c8d67d7c0d05b7785c4778df54b88b8dfd`. Binary SHA-256: `b56156e2a426eef392720d4a52b14327a64602be70980d35a7d8a2466baf2294`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_10_songbird_finale.scene" --events
```

