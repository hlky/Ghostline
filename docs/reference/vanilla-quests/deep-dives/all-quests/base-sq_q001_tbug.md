# The Gift

Journal: `quests/side_quest/sq_q001_tbug` · `SideQuest` · hash `2549135402`.

Journal premise: T-Bug's prolly the last person you'd expect to do presents. She's not the kind of gal who goes around buyin' novelty coffee mugs or t-shirts of your favorite comic book hero. But a netrunner program...? For you? For the job? Shit... she must really like you, ese.

**Coverage: journal-linked.** 26 exact journal-linked nodes in 2 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Equip the Ping quickhack in your inventory and upload it to the camera. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/01_ba_use_ping_just` |
| Equip the Ping quickhack in your inventory. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` |
| Retrieve the Ping quickhack from the netrunner. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/01_pick_programms` |
| Equip the Ping quickhack in your inventory and upload it to the camera in order to locate an Access Point. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/01b_use_ping` |
| Use your personal link to connect to the Access Point and hack it. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point` |
| Upload Ping to the camera to find the Access Point. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/02_upload_ping_find_ap` |
| Upload Ping to the camera. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/02b_upload_ping_just` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `q001_quest_bugfixes.questphase / h315 / 8` (Condition) | `quests/side_quest/sq_q001_tbug/tbug/01b_use_ping` | 10:False → 8:In; 8:True → 11:In; 8:False → 9:In |
| `q001_quest_bugfixes.questphase / h315 / 9` (Condition) | `quests/side_quest/sq_q001_tbug/tbug/01_ba_use_ping_just` | 9:False → 1:In; 8:False → 9:In; 9:True → 11:In |
| `q001_quest_bugfixes.questphase / h315 / 12` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01b_use_ping` | 11:False → 12:Inactive; 12:Out → 13:Inactive |
| `q001_quest_bugfixes.questphase / h315 / 13` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_ba_use_ping_just` | 12:Out → 13:Inactive; 13:Out → 14:Active |
| `q001_quest_bugfixes.questphase / h315 / 14` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` | 13:Out → 14:Active; 14:Out → 22:In |
| `q001_quest_bugfixes.questphase / h315 / 15` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01b_use_ping` | 11:True → 15:Inactive; 15:Out → 16:Inactive |
| `q001_quest_bugfixes.questphase / h315 / 16` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_ba_use_ping_just` | 15:Out → 16:Inactive; 16:Out → 17:In |
| `q001_quest_bugfixes.questphase / h315 / 18` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02_upload_ping_find_ap` | 17:False → 18:Active; 18:Out → 21:In |
| `q001_quest_bugfixes.questphase / h315 / 19` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02b_upload_ping_just` | 17:True → 19:Active; 19:Out → 21:In |
| `q001_quest_bugfixes.questphase / h315 / 23` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` | 23:Out → 17:In; 22:Out → 23:Succeeded |
| `q001_quest_bugfixes.questphase / h635 / 8` (Condition) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` | 8:False → 1:In; 2:Out → 8:In; 8:True → 9:In |
| `q001_tbug_tutorial.questphase / h0 / 3` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_pick_programms` | 37:Out → 3:Active; 3:Out → 4:Active |
| `q001_tbug_tutorial.questphase / h0 / 4` (Journal) | `quests/side_quest/sq_q001_tbug/desc` | 3:Out → 4:Active; 4:Out → 5:In |
| `q001_tbug_tutorial.questphase / h0 / 6` (Journal) | `quests/side_quest/sq_q001_tbug` | 43:False → 6:Succeeded; 87:Out → 6:Succeeded; 6:Out → 76:In |
| `q001_tbug_tutorial.questphase / h0 / 7` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_pick_programms` | 5:Out → 7:Succeeded; 7:Out → 111:In |
| `q001_tbug_tutorial.questphase / h0 / 8` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point` | 50:False → 8:Active |
| `q001_tbug_tutorial.questphase / h0 / 11` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point` | 48:True → 11:Succeeded; 11:Out → 43:In |
| `q001_tbug_tutorial.questphase / h0 / 38` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` | 116:Out1 → 38:Active; 38:Out → 39:In; 38:Out → 54:In; 38:Out → 88:In |
| `q001_tbug_tutorial.questphase / h0 / 43` (Condition) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` | 43:False → 6:Succeeded; 11:Out → 43:In; 48:False → 43:In; 43:True → 86:In |
| `q001_tbug_tutorial.questphase / h0 / 48` (Condition) | `quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point` | 48:True → 11:Succeeded; 32:Out → 48:In; 48:False → 43:In |
| `q001_tbug_tutorial.questphase / h0 / 78` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` | 77:Out → 78:Succeeded; 78:Out → 79:In |
| `q001_tbug_tutorial.questphase / h0 / 80` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02_upload_ping_find_ap` | 79:False → 80:Active; 80:Out → 89:In |
| `q001_tbug_tutorial.questphase / h0 / 81` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02b_upload_ping_just` | 79:True → 81:Active; 81:Out → 89:In |
| `q001_tbug_tutorial.questphase / h0 / 83` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02_upload_ping_find_ap` | 83:Out → 50:In; 82:False → 83:Succeeded |
| `q001_tbug_tutorial.questphase / h0 / 84` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02b_upload_ping_just` | 84:Out → 50:In; 82:True → 84:Succeeded |
| `q001_tbug_tutorial.questphase / h0 / 112` (Journal) | `quests/side_quest/sq_q001_tbug` | 115:Out → 112:Succeeded; 112:Out → 113:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h24 / 7 | `q001_quest_bugfixes.questphase` | 0: Input; 0:Out → 7:In1 |
| `base\quest\persistent_content.questphase` / h1469 / 11 | `q001_tbug_tutorial.questphase` | 12: PauseCondition: q001_tbug_netrunner_tut GreaterOrEqual 1; 12:Out → 11:In1 |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.quest` / h0 / 10 | `persistent_content.questphase` | 0: Start; 0:Out → 10:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 17 | `persistent_content.questphase` | 0: Input; 36: Input; 0:Out → 17:In1; 36:Out → 17:EP1_Standalone |
| `base\quest\main_quests\part1\q108\q108_johnny.quest` / h0 / 24 | `persistent_content.questphase` | 0: Start; 0:Out → 24:In1 |
| `base\quest\minor_quests\mq025\batty\batty_quest.quest` / h0 / 3 | `persistent_content.questphase` | 0: Start; 0:Out → 3:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 4 | `bugfixing.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:Out_res_act1 → 14:In; 4:to_mq025 → 6:to_mq025; 4:sq026_02_signal → 5:sq026_02_signal; 9:Out1 → 4:In1; 21:Out → 4:In1; 4:CYB-656199 → 15:In; 4:ep1_active_out → 23:In |
| `base\quest\main_quests\epilogue\q201\q201_heir.quest` / h0 / 44 | `bugfixing.questphase` | 11: Start; 11:Out → 44:In1 |
| `base\quest\main_quests\part1\q101\q101.quest` / h0 / 47 | `bugfixing.questphase` | 0: Start; 0:Out → 47:In1 |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 76 | `bugfixing.questphase` | 0: Start; 0:Out → 76:In1 |
| `base\quest\main_quests\part1\q112\q112_abduction.quest` / h0 / 23 | `bugfixing.questphase` | 0: Start; 0:Out → 23:In1 |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 140 | `bugfixing.questphase` | 0: Start; 0:Out → 140:In1 |
| `base\quest\minor_quests\mq026\mq026.quest` / h0 / 5 | `bugfixing.questphase` | 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1:Out1 → 5:In1; 1:conspiracy_out → 5:In1; 1:combat_out → 5:In1; 1:death_out → 5:In1 |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 61 | `bugfixing.questphase` | 0: Start; 0:Out → 61:In1 |
| `base\quest\side_quests\sq023\sq023.quest` / h0 / 20 | `bugfixing.questphase` | 0: Start; 0:Out → 20:In1 |
| `base\quest\side_quests\sq025\sq025.quest` / h0 / 68 | `bugfixing.questphase` | 49: Phase; 49:additional_content_out → 68:In1 |
| `base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest` / h0 / 64 | `bugfixing.questphase` | 0: Start; 0:Out → 64:In1 |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 13 | `bugfixing.questphase` | 11: LogicalHub; 11:Out1 → 13:In1 |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest` / h0 / 10 | `additional_game_elements.questphase` | 1: Start; 1:Out → 10:Input |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest` / h0 / 4 | `additional_game_elements.questphase` | 5: FactsDBManager: sts_bls_ina_tier_1; 5:Out → 4:Input |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest` / h0 / 6 | `additional_game_elements.questphase` | 4: FactsDBManager: sts_bls_ina_tier_1; 4:Out → 6:Input |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest` / h0 / 5 | `additional_game_elements.questphase` | 4: FactsDBManager: sts_cct_dtn_tier_1; 4:Out → 5:Input |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_cct_dtn_tier_1; 3:Out → 2:Input |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest` / h0 / 6 | `additional_game_elements.questphase` | 4: Scene: ma_hey_spr_04_00_chickentest.scene; 4:End 0 → 6:Input |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest` / h0 / 4 | `additional_game_elements.questphase` | 5: FactsDBManager: sts_hey_spr_tier_1; 5:Out → 4:Input |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest` / h0 / 4 | `additional_game_elements.questphase` | 3: Scene: ma_pac_cvi_08_00_chickentest.scene; 3:End 0 → 4:Input |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_pac_cvi_tier_1; 3:Out → 2:Input |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest` / h0 / 3 | `additional_game_elements.questphase` | 2: Scene: mq_std_rcr_11_00_chickentest.scene; 2:End 0 → 3:Input |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest` / h0 / 6 | `additional_game_elements.questphase` | 1: Start; 1:Out → 6:Input |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest` / h0 / 7 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_wat_kab_tier_1; 3:Out → 7:Input |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: Scene: ma_wat_lch_06_chicken_test.scene; 3:End 0 → 2:Input |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest` / h0 / 8 | `additional_game_elements.questphase` | 9: FactsDBManager: ow_psychos_intro_done; 9:Out → 8:Input |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest` / h0 / 6 | `additional_game_elements.questphase` | 8: LogicalHub; 8:Out1 → 6:Input |
| `base\quest\cyberpunk2077.questphase` / h520 / 3 | `additional_game_elements.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 9:Out1 → 3:Input; 21:Out → 3:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 20 | `additional_game_elements.questphase` | 25: LogicalHub; 25:Out1 → 20:Input |
| `base\quest\main_quests\epilogue\q201\q201_heir.quest` / h0 / 29 | `additional_game_elements.questphase` | 11: Start; 11:Out → 29:Input |
| `base\quest\main_quests\epilogue\q202\q202.quest` / h0 / 22 | `additional_game_elements.questphase` | 0: Start; 0:Out → 22:Input |
| `base\quest\main_quests\epilogue\q203\q203_legend.quest` / h0 / 30 | `additional_game_elements.questphase` | 27: FactsDBManager: q204_var_test_def; 27:Out → 30:Input |
| `base\quest\main_quests\epilogue\q204\q204_reborn.quest` / h0 / 6 | `additional_game_elements.questphase` | 0: Start; 0:Out → 6:Input |
| `base\quest\main_quests\part1\q101\q101.quest` / h0 / 30 | `additional_game_elements.questphase` | 0: Start; 0:Out → 30:Input |
| `base\quest\main_quests\part1\q103\q103.quest` / h0 / 45 | `additional_game_elements.questphase` | 0: Start; 0:Out → 45:Input |
| `base\quest\main_quests\part1\q105\q105_main.quest` / h0 / 40 | `additional_game_elements.questphase` | 58: LogicalHub; 58:Out1 → 40:Input |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 17 | `additional_game_elements.questphase` | 0: Start; 0:Out → 17:Input |
| `base\quest\main_quests\part1\q112\q112_abduction.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\main_quests\part1\q113\q113.quest` / h0 / 40 | `additional_game_elements.questphase` | 36: FactsDBManager: q113_active; 36:Out → 40:Input |
| `base\quest\main_quests\part1\q114\q114_nomads.quest` / h0 / 16 | `additional_game_elements.questphase` | 0: Start; 0:Out → 16:Input |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 57 | `additional_game_elements.questphase` | 0: Start; 0:Out → 57:Input |
| `base\quest\main_quests\prologue\q000\q000.quest` / h0 / 10 | `additional_game_elements.questphase` | 2: Start; 2:Out → 10:Input |
| `base\quest\main_quests\prologue\q001\q001.quest` / h0 / 30 | `additional_game_elements.questphase` | 120: LogicalHub; 120:Out1 → 30:Input |
| `base\quest\main_quests\prologue\q003\q003.quest` / h0 / 26 | `additional_game_elements.questphase` | 0: Start; 0:Out → 26:Input |
| `base\quest\main_quests\prologue\q004\q004.quest` / h0 / 1087 | `additional_game_elements.questphase` | 24: Start; 24:Out → 1087:Input |
| `base\quest\main_quests\prologue\q005\q005_heist.quest` / h0 / 14 | `additional_game_elements.questphase` | 17: FactsDBManager: jackie_default_on write/default comparison 0; 17:Out → 14:Input |
| `base\quest\minor_quests\mq000\mq000.quest` / h0 / 12 | `additional_game_elements.questphase` | 3: Scene: mq000_00_chickentest.scene; 3:out → 12:Input |
| `base\quest\minor_quests\mq001\mq001.quest` / h0 / 10 | `additional_game_elements.questphase` | 21: Start; 21:Out → 10:Input |
| `base\quest\minor_quests\mq003\mq003_orbitals.quest` / h0 / 7 | `additional_game_elements.questphase` | 2: Start; 2:Out → 7:Input |
| `base\quest\minor_quests\mq006\mq006.quest` / h0 / 7 | `additional_game_elements.questphase` | 6: Scene: mq006_chicken_test.scene; 6:End 0 → 7:Input |
| `base\quest\minor_quests\mq007\mq007.quest` / h0 / 10 | `additional_game_elements.questphase` | 0: Start; 0:Out → 10:Input |
| `base\quest\minor_quests\mq008\mq008.quest` / h0 / 14 | `additional_game_elements.questphase` | 0: Start; 0:Out → 14:Input |
| `base\quest\minor_quests\mq011\mq011.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq012\mq012.quest` / h0 / 9 | `additional_game_elements.questphase` | 1: Start; 1:Out → 9:Input |
| `base\quest\minor_quests\mq013\mq013.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Start; 1:Out → 4:Input |
| `base\quest\minor_quests\mq014\mq014.quest` / h0 / 5 | `additional_game_elements.questphase` | 0: Start; 0:Out → 5:Input |
| `base\quest\minor_quests\mq015\mq015_wizardbook.quest` / h0 / 7 | `additional_game_elements.questphase` | 0: Start; 0:Out → 7:Input |
| `base\quest\minor_quests\mq016\mq016_bartmoss.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\minor_quests\mq017\mq017_streetkid.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq018\mq018.quest` / h0 / 5 | `additional_game_elements.questphase` | 1: Phase: mq018_00_chickentest.questphase; 1:additional_content_out → 5:Input |
| `base\quest\minor_quests\mq019\mq019_paparazzi.quest` / h0 / 7 | `additional_game_elements.questphase` | 0: Start; 0:Out → 7:Input |
| `base\quest\minor_quests\mq021\mq021.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq022\mq022.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq023\mq023_bootleg.quest` / h0 / 11 | `additional_game_elements.questphase` | 1: Start; 1:Out → 11:Input |
| `base\quest\minor_quests\mq024\mq024.quest` / h0 / 15 | `additional_game_elements.questphase` | 0: Start; 0:Out → 15:Input |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.quest` / h0 / 4 | `additional_game_elements.questphase` | 10: FactsDBManager: disable_tutorials; 10:Out → 4:Input |
| `base\quest\minor_quests\mq026\mq026.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Phase: mq026_00_chickentest.questphase; 1:additional_content_out → 4:Input |
| `base\quest\minor_quests\mq028\mq028.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Phase: mq028_00_chickentest.questphase; 1:additional_content_out → 4:Input |
| `base\quest\minor_quests\mq030\mq030.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\minor_quests\mq032\mq032_sacrum.quest` / h0 / 12 | `additional_game_elements.questphase` | 0: Start; 0:Out → 12:Input |
| `base\quest\minor_quests\mq033\mq033_tarot.quest` / h0 / 2 | `additional_game_elements.questphase` | 0: Start; 0:Out → 2:Input |
| `base\quest\minor_quests\mq035\mq035_ozob.quest` / h0 / 5 | `additional_game_elements.questphase` | 4: Scene: mq035_chicken_test.scene; 4:start → 5:Input |
| `base\quest\minor_quests\mq037\mq037_brendan.quest` / h0 / 4 | `additional_game_elements.questphase` | 0: Start; 0:Out → 4:Input |
| `base\quest\minor_quests\mq038\mq038.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq040\mq040_biosculpt.quest` / h0 / 10 | `additional_game_elements.questphase` | 22: Condition: mq040_add_ele_on Equal 1; 22:True → 10:Input |
| `base\quest\minor_quests\mq041\mq041_corpo.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq048\mq048.quest` / h0 / 12 | `additional_game_elements.questphase` | 1: Start; 1:Out → 12:Input |
| `base\quest\minor_quests\mq055\mq055.quest` / h0 / 4 | `additional_game_elements.questphase` | 3: Scene: mq055_chicken.scene; 3:End 0 → 4:EP1_Standalone |
| `base\quest\side_quests\sq004\sq004_riders_quest.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq006\sq006.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq011\sq011.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq012\sq012_the_law.quest` / h0 / 6 | `additional_game_elements.questphase` | 2: Start; 2:Out → 6:Input |
| `base\quest\side_quests\sq017\sq017.quest` / h0 / 5 | `additional_game_elements.questphase` | 0: Start; 0:Out → 5:Input |
| `base\quest\side_quests\sq018\sq018.quest` / h0 / 24 | `additional_game_elements.questphase` | 16: Start; 16:Out → 24:Input |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 17 | `additional_game_elements.questphase` | 0: Start; 0:Out → 17:Input |
| `base\quest\side_quests\sq023\sq023.quest` / h0 / 15 | `additional_game_elements.questphase` | 0: Start; 0:Out → 15:Input |
| `base\quest\side_quests\sq024\sq024.quest` / h0 / 29 | `additional_game_elements.questphase` | 0: Start; 0:Out → 29:Input |
| `base\quest\side_quests\sq025\sq025.quest` / h0 / 66 | `additional_game_elements.questphase` | 49: Phase; 49:additional_content_out → 66:Input |
| `base\quest\side_quests\sq026\sq026.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest` / h0 / 8 | `additional_game_elements.questphase` | 0: Start; 0:Out → 8:Input |
| `base\quest\side_quests\sq028\sq028.quest` / h0 / 4 | `additional_game_elements.questphase` | 0: Start; 0:Out → 4:Input |
| `base\quest\side_quests\sq029\sq029.quest` / h0 / 20 | `additional_game_elements.questphase` | 1: Start; 1:Out → 20:Input |
| `base\quest\side_quests\sq030\sq030.quest` / h0 / 11 | `additional_game_elements.questphase` | 4: SceneManager; 4:Out → 11:Input |
| `base\quest\side_quests\sq031\sq031.quest` / h0 / 6 | `additional_game_elements.questphase` | 0: Start; 0:Out → 6:Input |
| `base\quest\side_quests\sq032\sq032.quest` / h0 / 12 | `additional_game_elements.questphase` | 0: Start; 0:Out → 12:Input |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 11 | `additional_game_elements.questphase` | 6: FactsDBManager: ep1_side_content; 6:Out → 11:Input |
| `ep1\quest\main_quests\q304\q304.quest` / h0 / 20 | `additional_game_elements.questphase` | 12: Checkpoint; 12:Out → 20:EP1_Standalone |
| `ep1\quest\main_quests\q305\q305.quest` / h0 / 5 | `additional_game_elements.questphase` | 1: Start; 1:Out → 5:Input |
| `ep1\quest\main_quests\q306\q306.quest` / h0 / 8 | `additional_game_elements.questphase` | 9: PauseCondition: q306_DEBUG_useBaseGameAdditionalGameElements; 9:Out → 8:Input |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 3 | `additional_game_elements.questphase` | 4: LogicalHub; 10: CutControl; 4:Out1 → 3:Input; 10:CutSource → 3:CutDestination |
| `ep1\quest\minor_quests\mq301\mq301.quest` / h0 / 7 | `additional_game_elements.questphase` | 1: Start; 1:Out → 7:Input |
| `ep1\quest\minor_quests\mq303\mq303.quest` / h95 / 2 | `additional_game_elements.questphase` | 0: Input; 0:Out → 2:Input |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 3 | `additional_game_elements.questphase` | 4: LogicalHub; 4:Out1 → 3:Input |
| `ep1\quest\minor_quests\mq305\mq305.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Start; 1:Out → 4:Input |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| No resolved scene dependency in this scope | This does not prove the quest has no dialogue | — |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CP77-53955` | q001_quest_bugfixes.questphase / h973 / 2 | No reader in selected context |
| `CYB-12345` | q001_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-553644` | q001_quest_bugfixes.questphase / h77 / 2 | No reader in selected context |
| `CYB-554542` | q001_quest_bugfixes.questphase / h315 / 2 | No reader in selected context |
| `CYB-574353` | q001_quest_bugfixes.questphase / h486 / 2 | No reader in selected context |
| `CYB-590152` | q001_quest_bugfixes.questphase / h37 / 2 | No reader in selected context |
| `CYB-596966` | q001_quest_bugfixes.questphase / h139 / 2 | No reader in selected context |
| `CYB-623082` | q001_quest_bugfixes.questphase / h635 / 2 | No reader in selected context |
| `CYB-624947` | q001_quest_bugfixes.questphase / h920 / 2 | No reader in selected context |
| `CYB-633972` | q001_quest_bugfixes.questphase / h765 / 2 | No reader in selected context |
| `CYB-635412` | q001_quest_bugfixes.questphase / h717 / 2 | No reader in selected context |
| `CYB-635989` | q001_quest_bugfixes.questphase / h526 / 2 | No reader in selected context |
| `CYB-638088` | q001_quest_bugfixes.questphase / h669 / 2 | No reader in selected context |
| `CYB-640567` | q001_quest_bugfixes.questphase / h565 / 2 | No reader in selected context |
| `CYB-646395` | q001_quest_bugfixes.questphase / h604 / 2 | No reader in selected context |
| `CYB-655311` | q001_quest_bugfixes.questphase / h839 / 2 | No reader in selected context |
| `close_inventory_mode_tutorial` | q001_tbug_tutorial.questphase / h0 / 62 | q001_tbug_tutorial.questphase / h0 / 75 |
| `cyberdeck_inventory_tutorial` | q001_tbug_tutorial.questphase / h0 / 54 | q001_tbug_tutorial.questphase / h0 / 53 |
| `ping_installed` | Producer outside selected context | q001_quest_bugfixes.questphase / h315 / 11; q001_quest_bugfixes.questphase / h315 / 22; q001_tbug_tutorial.questphase / h0 / 77; q001_tbug_tutorial.questphase / h0 / 91 |
| `q001_checked_stash` | Producer outside selected context | q001_quest_bugfixes.questphase / h139 / 28; q001_quest_bugfixes.questphase / h139 / 29; q001_quest_bugfixes.questphase / h139 / 8 |
| `q001_completed` | Producer outside selected context | q001_quest_bugfixes.questphase / h526 / 3 |
| `q001_e3_fog_hack` | q001_quest_bugfixes.questphase / h839 / 12 | No reader in selected context |
| `q001_jackie_on_mistys_chair` | q001_quest_bugfixes.questphase / h526 / 5 | No reader in selected context |
| `q001_just_after_rd_scene` | Producer outside selected context | q001_quest_bugfixes.questphase / h37 / 8 |
| `q001_mission0_complete` | Producer outside selected context | q001_quest_bugfixes.questphase / h565 / 3 |
| `q001_show_sts_tut` | q001_quest_bugfixes.questphase / h839 / 9 | q001_quest_bugfixes.questphase / h839 / 8 |
| `q001_sq_tbug_done` | q001_tbug_tutorial.questphase / h0 / 76 | No reader in selected context |
| `q001_takedown_tutorial_failed` | q001_quest_bugfixes.questphase / h973 / 25 | No reader in selected context |
| `q001_tbug_netrunner_tut` | q001_tbug_tutorial.questphase / h0 / 51 | No reader in selected context |
| `q001_tut_ap_hacked_netrunner` | q001_tbug_tutorial.questphase / h0 / 49 | q001_quest_bugfixes.questphase / h315 / 17; q001_tbug_tutorial.questphase / h0 / 50; q001_tbug_tutorial.questphase / h0 / 79; q001_tbug_tutorial.questphase / h0 / 82 |
| `q001_tut_equip_upload_part_done` | q001_quest_bugfixes.questphase / h315 / 20; q001_tbug_tutorial.questphase / h0 / 85 | q001_tbug_tutorial.questphase / h0 / 87 |
| `q101_new_ping_tutorial_started` | q001_tbug_tutorial.questphase / h0 / 88 | q001_quest_bugfixes.questphase / h315 / 10 |
| `q101_no_cyberdeck_initially` | q001_tbug_tutorial.questphase / h0 / 115 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | q001_quest_bugfixes.questphase / h0 / 55 |

## Exact gates, joins and cancellation

<details><summary>77 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `q001_quest_bugfixes.questphase / h0 / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 56:Out → 55:In |
| `q001_quest_bugfixes.questphase / h37 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_just_after_rd_scene","value":1,"comparisonType":"GreaterOrEqual"}}}` | 8:True → 1:In; 2:Out → 8:In; 8:False → 9:In |
| `q001_quest_bugfixes.questphase / h77 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#v_room_stash"},"isPlayer":false,"itemID":"69784628567","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 2:Out → 8:In; 8:True → 13:In; 8:False → 11:In |
| `q001_quest_bugfixes.questphase / h77 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"69784628567","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 11:False → 1:In; 8:False → 11:In; 11:True → 12:In |
| `q001_quest_bugfixes.questphase / h139 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_checked_stash","value":1,"comparisonType":"GreaterOrEqual"}}}` | 25:True → 8:In; 8:True → 16:In; 8:False → 15:In |
| `q001_quest_bugfixes.questphase / h139 / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/ride_to_mb/05a_stash","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Inactive","inverted":true}}}` | 14:False → 1:In; 2:Out → 14:In; 14:True → 25:In |
| `q001_quest_bugfixes.questphase / h139 / 25` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterLifePath_ConditionType","lifePathID":"83574632792"}}}` | 25:True → 8:In; 14:True → 25:In; 25:False → 26:In |
| `q001_quest_bugfixes.questphase / h139 / 26` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterLifePath_ConditionType","lifePathID":"67091901544"}}}` | 25:False → 26:In; 26:True → 28:In; 26:False → 27:In |
| `q001_quest_bugfixes.questphase / h139 / 27` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterLifePath_ConditionType","lifePathID":"83635443133"}}}` | 27:False → 1:In; 26:False → 27:In; 27:True → 29:In |
| `q001_quest_bugfixes.questphase / h139 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_checked_stash","value":1,"comparisonType":"GreaterOrEqual"}}}` | 28:False → 19:In; 28:True → 20:In; 26:True → 28:In |
| `q001_quest_bugfixes.questphase / h139 / 29` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_checked_stash","value":1,"comparisonType":"GreaterOrEqual"}}}` | 29:False → 23:In; 29:True → 24:In; 27:True → 29:In |
| `q001_quest_bugfixes.questphase / h315 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_tbug/tbug/01b_use_ping","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 10:False → 8:In; 8:True → 11:In; 8:False → 9:In |
| `q001_quest_bugfixes.questphase / h315 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_tbug/tbug/01_ba_use_ping_just","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 9:False → 1:In; 8:False → 9:In; 9:True → 11:In |
| `q001_quest_bugfixes.questphase / h315 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_new_ping_tutorial_started","value":1,"comparisonType":"GreaterOrEqual"}}}` | 10:True → 1:In; 2:Out → 10:In; 10:False → 8:In |
| `q001_quest_bugfixes.questphase / h315 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ping_installed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 8:True → 11:In; 9:True → 11:In; 11:True → 15:Inactive; 11:False → 12:Inactive |
| `q001_quest_bugfixes.questphase / h315 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_tut_ap_hacked_netrunner","value":1,"comparisonType":"GreaterOrEqual"}}}` | 16:Out → 17:In; 23:Out → 17:In; 17:True → 19:Active; 17:False → 18:Active |
| `q001_quest_bugfixes.questphase / h315 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q001_exercise_device_quickhack","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"WasQuickHackJustPerformed","functionParameters":[{"$type":"questDevice_ConditionFunctionParameter","name":"quickHackName","value":{"$type":"Variant","$rawData":"DwAGAAAAgQA="}}]}}}` | 18:Out → 21:In; 19:Out → 21:In; 21:Out → 20:In |
| `q001_quest_bugfixes.questphase / h315 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ping_installed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 14:Out → 22:In; 22:Out → 23:Succeeded |
| `q001_quest_bugfixes.questphase / h486 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/ride_to_mb/05_go_to_vroom","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 3:False → 1:In; 2:Out → 3:In; 3:True → 4:In |
| `q001_quest_bugfixes.questphase / h526 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_completed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 3:False → 1:In; 2:Out → 3:In; 3:True → 5:In |
| `q001_quest_bugfixes.questphase / h565 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_mission0_complete","value":1,"comparisonType":"GreaterOrEqual"}}}` | 3:False → 1:In; 2:Out → 3:In; 3:True → 6:In |
| `q001_quest_bugfixes.questphase / h635 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_tbug/tbug/01_equip_ping","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 8:False → 1:In; 2:Out → 8:In; 8:True → 9:In |
| `q001_quest_bugfixes.questphase / h669 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson","fileEntryIndex":2},"state":"Succeeded"}}}` | 8:False → 1:In; 2:Out → 8:In; 8:True → 9:In |
| `q001_quest_bugfixes.questphase / h717 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_exercise_device_quickhack"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":40.0},"comparisonType":"LessOrEqual"}}}` | 2:Out → 10:In; 10:Out → 9:In |
| `q001_quest_bugfixes.questphase / h765 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/premission0/01b_exit_the_car","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/premission0/01b_exit_the_car","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 2:Out → 6:In; 6:True → 10:In |
| `q001_quest_bugfixes.questphase / h765 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/mission0","fileEntryIndex":3,"className":"gameJournalQuestPhase"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/premission0","fileEntryIndex":3,"className":"gameJournalQuestPhase"},"state":"Active"}}]}}` | 10:True → 3:In; 6:True → 10:In |
| `q001_quest_bugfixes.questphase / h839 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_show_sts_tut","value":1,"comparisonType":"GreaterOrEqual"}}}` | 8:True → 1:In; 13:True → 8:In; 8:False → 16:In |
| `q001_quest_bugfixes.questphase / h839 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_01_victor/megabuilding/talk_jackie_person","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 13:False → 1:In; 2:Out → 13:In; 13:True → 8:In |
| `q001_quest_bugfixes.questphase / h839 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 8:False → 16:In; 16:Out → 17:In |
| `q001_quest_bugfixes.questphase / h839 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","seconds":1}}}` | 17:Out → 10:In; 16:Out → 17:In |
| `q001_quest_bugfixes.questphase / h920 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151781844931","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 8:False → 1:In; 2:Out → 8:In; 8:True → 9:In |
| `q001_quest_bugfixes.questphase / h973 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/mission0/takedown_scavenger","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 2:Out → 7:In; 7:True → 13:In1; 7:False → 8:In |
| `q001_quest_bugfixes.questphase / h973 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/mission0/takedown_scavenger","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Failed"}}}` | 7:False → 8:In; 8:True → 13:In1; 8:False → 9:In |
| `q001_quest_bugfixes.questphase / h973 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/mission0/takedown_scavenger","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 8:False → 9:In; 9:Out → 10:In |
| `q001_quest_bugfixes.questphase / h973 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_scavengers_community_area","names":["scavenger4"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 9:Out → 10:In; 10:Out → 11:In |
| `q001_quest_bugfixes.questphase / h973 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_scavengers_community_area","names":["scavenger4"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":15.0},"comparisonType":"LessOrEqual"}}}` | 10:Out → 11:In; 11:Out → 19:In |
| `q001_quest_bugfixes.questphase / h973 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#q001_scavengers_community_area","names":["scavenger4"]}}}}` | 3:Out → 20:In; 20:Out → 32:In |
| `q001_quest_bugfixes.questphase / h973 / 27` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/mission0/takedown_scavenger","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 27:True → 26:Failed; 33:False → 27:In; 30:Out → 27:In; 27:False → 28:In |
| `q001_quest_bugfixes.questphase / h973 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/mission0/deal_scavengers","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 28:True → 24:In; 26:Out → 28:In; 27:False → 28:In; 28:False → 29:Active |
| `q001_quest_bugfixes.questphase / h973 / 32` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/mission0/get_to_takedown_room","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 20:Out → 32:In; 32:True → 31:Succeeded; 32:False → 33:In |
| `q001_quest_bugfixes.questphase / h973 / 33` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/mission0/approach_scavenger_remaining_in_stealth","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 33:False → 27:In; 33:True → 30:Failed; 31:Out → 33:In; 32:False → 33:In |
| `q001_quest_bugfixes.questphase / h973 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro/mission0/takedown_scavenger","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 39:Out → 1:In; 3:Out → 39:In |
| `q001_tbug_tutorial.questphase / h0 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151781844931","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 4:Out → 5:In; 5:Out → 7:Succeeded |
| `q001_tbug_tutorial.questphase / h0 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q001_exercise_access_point","deviceControllerClass":"AccessPointControllerPS","deviceConditionFunction":"WasHackingMinigameSucceeded"}}}` | 9:Out → 10:In; 10:Out → 49:In |
| `q001_tbug_tutorial.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q001_tr_accesspoint_shop_tutorial"}}` | 26:Out → 15:In; 36:Out1 → 15:In; 15:Out → 16:In; 15:Out → 27:In; 15:Out → 25:In |
| `q001_tbug_tutorial.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q001_tr_accesspoint_shop_tutorial"}}` | 15:Out → 25:In; 29:CutSource → 25:CutDestination; 25:Out → 26:In |
| `q001_tbug_tutorial.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q001_exercise_access_point","deviceControllerClass":"AccessPointControllerPS","deviceConditionFunction":"IsPersonalLinkConnecting"}}}` | 15:Out → 27:In; 27:Out → 29:In |
| `q001_tbug_tutorial.questphase / h0 / 29` | `questCutControlNodeDefinition` `{}` | 29:CutSource → 25:CutDestination; 29:CutSource → 26:CutDestination; 27:Out → 29:In; 29:Out → 28:In |
| `q001_tbug_tutorial.questphase / h0 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"112307738469","value":false}}}` | 49:Out → 32:In; 32:Out → 48:In |
| `q001_tbug_tutorial.questphase / h0 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q001_exercise_device_quickhack","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"WasQuickHackJustPerformed","functionParameters":[{"$type":"questDevice_ConditionFunctionParameter","name":"quickHackName","value":{"$type":"Variant","$rawData":"DwAGAAAAlwA="}}]}}}` | 38:Out → 39:In; 39:Out → 82:In |
| `q001_tbug_tutorial.questphase / h0 / 43` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_tbug/tbug/01_equip_ping","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 43:False → 6:Succeeded; 11:Out → 43:In; 48:False → 43:In; 43:True → 86:In |
| `q001_tbug_tutorial.questphase / h0 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 48:True → 11:Succeeded; 32:Out → 48:In; 48:False → 43:In |
| `q001_tbug_tutorial.questphase / h0 / 50` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_tut_ap_hacked_netrunner","value":1,"comparisonType":"GreaterOrEqual"}}}` | 50:False → 8:Active; 84:Out → 50:In; 83:Out → 50:In |
| `q001_tbug_tutorial.questphase / h0 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"cyberdeck_inventory_tutorial","value":1,"comparisonType":"GreaterOrEqual"}}}` | 53:Out → 21:In; 108:Out → 53:In; 53:Out → 62:In; 53:Out → 119:In |
| `q001_tbug_tutorial.questphase / h0 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q001_tr_turnoff_equip_ping_tut"}}` | 69:CutSource → 65:CutDestination; 114:Out → 65:In; 65:Out → 66:In |
| `q001_tbug_tutorial.questphase / h0 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q001_tr_turnoff_equip_ping_tut"}}` | 72:CutSource → 67:CutDestination; 74:Out → 67:In; 67:Out → 68:In |
| `q001_tbug_tutorial.questphase / h0 / 69` | `questCutControlNodeDefinition` `{}` | 69:CutSource → 65:CutDestination; 108:Out → 69:In; 69:Out → 74:In; 69:CutSource → 114:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q001_tr_turnoff_equip_ping_tut"}}` | 73:CutSource → 70:CutDestination; 75:Out → 70:In; 70:Out → 71:In |
| `q001_tbug_tutorial.questphase / h0 / 72` | `questCutControlNodeDefinition` `{}` | 62:Out → 72:In; 72:CutSource → 67:CutDestination; 72:Out → 75:In; 72:CutSource → 74:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 73` | `questCutControlNodeDefinition` `{}` | 61:Out → 73:In; 73:CutSource → 70:CutDestination; 73:CutSource → 75:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"118585379367","value":false}}}` | 74:Out → 67:In; 69:Out → 74:In; 72:CutSource → 74:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"close_inventory_mode_tutorial","value":1,"comparisonType":"GreaterOrEqual"}}}` | 75:Out → 70:In; 72:Out → 75:In; 73:CutSource → 75:CutDestination; 75:Out → 95:In |
| `q001_tbug_tutorial.questphase / h0 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ping_installed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 88:Out → 77:In; 77:Out → 78:Succeeded; 77:Out → 97:In; 77:Out → 103:In |
| `q001_tbug_tutorial.questphase / h0 / 79` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_tut_ap_hacked_netrunner","value":1,"comparisonType":"GreaterOrEqual"}}}` | 78:Out → 79:In; 79:True → 81:Active; 79:False → 80:Active |
| `q001_tbug_tutorial.questphase / h0 / 82` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_tut_ap_hacked_netrunner","value":1,"comparisonType":"GreaterOrEqual"}}}` | 39:Out → 82:In; 82:True → 84:Succeeded; 82:False → 83:Succeeded |
| `q001_tbug_tutorial.questphase / h0 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_tut_equip_upload_part_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 87:Out → 6:Succeeded; 86:Out → 87:In |
| `q001_tbug_tutorial.questphase / h0 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q001_exercise_device_quickhack","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"WasQuickHackJustPerformed","functionParameters":[{"$type":"questDevice_ConditionFunctionParameter","name":"quickHackName","value":{"$type":"Variant","$rawData":"DwAGAAAAlwA="}}]}}}` | 80:Out → 89:In; 81:Out → 89:In; 89:Out → 85:In |
| `q001_tbug_tutorial.questphase / h0 / 91` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ping_installed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 91:Out → 61:In; 90:Out → 91:In; 91:Out → 96:In |
| `q001_tbug_tutorial.questphase / h0 / 102` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"75582890960","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 98:Out → 102:In; 102:Out → 99:In |
| `q001_tbug_tutorial.questphase / h0 / 105` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"93763639497","value":false}},{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"HasCyberdeck","value":1.0,"comparisonType":"GreaterOrEqual"}}]}}` | 105:Out → 13:In; 106:Out → 105:In; 105:Out → 109:In |
| `q001_tbug_tutorial.questphase / h0 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"93763639497","value":false}}}` | 107:Out → 98:In; 106:Out → 107:In |
| `q001_tbug_tutorial.questphase / h0 / 108` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"118585379367"}},{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"HasCyberdeck","value":1.0,"comparisonType":"GreaterOrEqual"}}]}}` | 108:Out → 19:In; 108:Out → 20:In; 108:Out → 53:In; 108:Out → 69:In; 119:CutSource → 108:CutDestination; 109:Out → 108:In; 117:Out → 108:In; 108:Out → 117:In |
| `q001_tbug_tutorial.questphase / h0 / 111` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"HasCyberdeck","value":1.0,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 111:In; 111:True → 116:In1; 111:False → 115:In |
| `q001_tbug_tutorial.questphase / h0 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"HasCyberdeck","value":1.0,"comparisonType":"GreaterOrEqual"}}}` | 112:Out → 113:In; 113:Out → 116:In1 |
| `q001_tbug_tutorial.questphase / h0 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 13:Out → 114:In; 114:Out → 65:In; 69:CutSource → 114:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 117` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"118585379367","value":false}}]}}` | 117:Out → 108:In; 108:Out → 117:In; 119:CutSource → 117:CutDestination; 117:Out → 118:In; 117:Out → 120:In |
| `q001_tbug_tutorial.questphase / h0 / 119` | `questCutControlNodeDefinition` `{}` | 53:Out → 119:In; 119:CutSource → 108:CutDestination; 119:CutSource → 117:CutDestination |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | q001_quest_bugfixes.questphase / h973 / 10 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `call_lifecycle` | q001_quest_bugfixes.questphase / h37 / 9 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `community_lifecycle` | q001_quest_bugfixes.questphase / h565 / 6 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | q001_quest_bugfixes.questphase / h0 / 55; q001_quest_bugfixes.questphase / h139 / 28; q001_quest_bugfixes.questphase / h139 / 29; q001_quest_bugfixes.questphase / h139 / 8; +16 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | q001_quest_bugfixes.questphase / h973 / 35 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | q001_quest_bugfixes.questphase / h604 / 8; q001_quest_bugfixes.questphase / h717 / 8; q001_quest_bugfixes.questphase / h717 / 9; q001_tbug_tutorial.questphase / h0 / 37; +1 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | q001_quest_bugfixes.questphase / h315 / 21; q001_tbug_tutorial.questphase / h0 / 10; q001_tbug_tutorial.questphase / h0 / 27; q001_tbug_tutorial.questphase / h0 / 39; +1 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | q001_quest_bugfixes.questphase / h839 / 17 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | q001_quest_bugfixes.questphase / h77 / 11; q001_quest_bugfixes.questphase / h77 / 8; q001_quest_bugfixes.questphase / h920 / 8; q001_tbug_tutorial.questphase / h0 / 102; +1 locations in catalogue.json | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | q001_quest_bugfixes.questphase / h315 / 12; q001_quest_bugfixes.questphase / h315 / 13; q001_quest_bugfixes.questphase / h315 / 14; q001_quest_bugfixes.questphase / h315 / 15; +21 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | q001_quest_bugfixes.questphase / h139 / 2; q001_quest_bugfixes.questphase / h315 / 2; q001_quest_bugfixes.questphase / h315 / 20; q001_quest_bugfixes.questphase / h37 / 2; +25 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | q001_quest_bugfixes.questphase / h839 / 16; q001_tbug_tutorial.questphase / h0 / 114 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | q001_tbug_tutorial.questphase / h0 / 119; q001_tbug_tutorial.questphase / h0 / 29; q001_tbug_tutorial.questphase / h0 / 69; q001_tbug_tutorial.questphase / h0 / 72; +1 locations in catalogue.json | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `spatial_gate` | q001_tbug_tutorial.questphase / h0 / 15; q001_tbug_tutorial.questphase / h0 / 25; q001_tbug_tutorial.questphase / h0 / 65; q001_tbug_tutorial.questphase / h0 / 67; +1 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `weather_scope` | q001_quest_bugfixes.questphase / h839 / 11 | weather operation + named source + reset policy → weather request/reset dispatched. Completion follows the caller's full restoration sequence, not an early cleanup fact. |
| `workspot_performance` | q001_quest_bugfixes.questphase / h973 / 22 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` | repair; journal anchor | `base-q001` |
| `base\quest\main_quests\prologue\q001\phases\q001_tbug_tutorial.questphase` | content candidate; journal anchor | `base-q001` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q108](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q108.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

114 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 16 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `c8705a8da51824b73252` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h37 / 0 -> 2 -> 8 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `6497920d6ce0ac894daa` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h526 / 2 -> 3 -> 5 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; True -> In |
| `eee71431d3a4d265f718` | `base\quest\main_quests\prologue\q001\phases\q001_tbug_tutorial.questphase` / h0 / 36 -> 15 -> 25 | questLogicalHubNodeDefinition -> questPauseConditionNodeDefinition[questTriggerCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out1 -> In; Out -> In |
| `1666d7526b9bab74f2e2` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h315 / 13 -> 14 -> 22 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> Active; Out -> In |
| `1a9b8893087e174a603f` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h315 / 14 -> 22 -> 23 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `2cb6a780f07f49d4270b` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h717 / 9 -> 8 -> 1 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `d5204524c8aea0449912` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h315 / 16 -> 17 -> 19 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; True -> Active |
| `7bfcd8df5888d6d0d606` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h526 / 2 -> 3 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; False -> In |
| `abbf46d00a7c0ae464b9` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h973 / 33 -> 27 -> 28 | questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; False -> In; False -> In |
| `58839785c560a180ce48` | `base\quest\main_quests\prologue\q001\phases\q001_tbug_tutorial.questphase` / h0 / 6 -> 76 -> 1 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `ef1f1c4d9ff5cba71b71` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 21 -> 24 -> 27 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPhaseNodeDefinition[questQuestPrefabEntry]; Out -> In; Out -> In1 |
| `e48c9412076725b4905e` | `base\quest\main_quests\prologue\q001\phases\q001_tbug_tutorial.questphase` / h0 / 69 -> 114 -> 65 | questCutControlNodeDefinition -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; CutSource -> CutDestination; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 13 | `h37` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 16 | `h77` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 19 | `h139` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 22 | `h315` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 27 | `h486` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 30 | `h526` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 33 | `h565` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 36 | `h604` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 39 | `h635` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 41 | `h669` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 45 | `h717` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 48 | `h765` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 51 | `h839` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 54 | `h920` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 58 | `h973` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_def.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.gamedef` | content candidate | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest |
| `base\quest\minor_quests\mq000\mq000.gamedef` | content candidate | base\quest\minor_quests\mq000\mq000.quest |
| `base\quest\minor_quests\mq000\mq000_thank_you.gamedef` | content candidate | base\quest\minor_quests\mq000\mq000.quest |
| `base\quest\minor_quests\mq001\mq001.gamedef` | content candidate | base\quest\minor_quests\mq001\mq001.quest |
| `base\quest\minor_quests\mq003\mq003_orbitals.gamedef` | content candidate | base\quest\minor_quests\mq003\mq003_orbitals.quest |
| `base\quest\minor_quests\mq006\mq006.gamedef` | content candidate | base\quest\minor_quests\mq006\mq006.quest |
| `base\quest\minor_quests\mq007\mq007.gamedef` | content candidate | base\quest\minor_quests\mq007\mq007.quest |
| `base\quest\minor_quests\mq008\mq008.gamedef` | content candidate | base\quest\minor_quests\mq008\mq008.quest |
| `base\quest\minor_quests\mq011\mq011.gamedef` | content candidate | base\quest\minor_quests\mq011\mq011.quest |
| `base\quest\minor_quests\mq012\mq012.gamedef` | content candidate | base\quest\minor_quests\mq012\mq012.quest |
| `base\quest\minor_quests\mq013\mq013.gamedef` | content candidate | base\quest\minor_quests\mq013\mq013.quest |
| `base\quest\minor_quests\mq014\mq014.gamedef` | content candidate | base\quest\minor_quests\mq014\mq014.quest |
| `base\quest\minor_quests\mq015\mq015_wizardbook.gamedef` | content candidate | base\quest\minor_quests\mq015\mq015_wizardbook.quest |
| `base\quest\minor_quests\mq016\mq016_bartmoss.gamedef` | content candidate | base\quest\minor_quests\mq016\mq016_bartmoss.quest |
| `base\quest\minor_quests\mq017\mq017_streetkid.gamedef` | content candidate | base\quest\minor_quests\mq017\mq017_streetkid.quest |
| `base\quest\minor_quests\mq018\mq018.gamedef` | content candidate | base\quest\minor_quests\mq018\mq018.quest |
| `base\quest\minor_quests\mq019\mq019_paparazzi.gamedef` | content candidate | base\quest\minor_quests\mq019\mq019_paparazzi.quest |
| `base\quest\minor_quests\mq021\mq021.gamedef` | content candidate | base\quest\minor_quests\mq021\mq021.quest |
| `base\quest\minor_quests\mq022\mq022.gamedef` | content candidate | base\quest\minor_quests\mq022\mq022.quest |
| `base\quest\minor_quests\mq023\mq023_bootleg.gamedef` | content candidate | base\quest\minor_quests\mq023\mq023_bootleg.quest |
| `base\quest\minor_quests\mq024\mq024.gamedef` | content candidate | base\quest\minor_quests\mq024\mq024.quest |
| `base\quest\minor_quests\mq025\batty\batty_definition.gamedef` | content candidate | base\quest\minor_quests\mq025\batty\batty_quest.quest |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.gamedef` | content candidate | base\quest\minor_quests\mq025\mq025_psycho_brawl.quest |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
| `base\quest\minor_quests\mq028\mq028.gamedef` | content candidate | base\quest\minor_quests\mq028\mq028.quest |
| `base\quest\minor_quests\mq030\mq030.gamedef` | content candidate | base\quest\minor_quests\mq030\mq030.quest |
| `base\quest\minor_quests\mq032\mq032_sacrum.gamedef` | content candidate | base\quest\minor_quests\mq032\mq032_sacrum.quest |
| `base\quest\minor_quests\mq033\mq033_tarot.gamedef` | content candidate | base\quest\minor_quests\mq033\mq033_tarot.quest |
| `base\quest\minor_quests\mq035\mq035_ozob.gamedef` | content candidate | base\quest\minor_quests\mq035\mq035_ozob.quest |
| `base\quest\minor_quests\mq037\mq037_brendan.gamedef` | content candidate | base\quest\minor_quests\mq037\mq037_brendan.quest |
| `base\quest\minor_quests\mq038\mq038.gamedef` | content candidate | base\quest\minor_quests\mq038\mq038.quest |
| `base\quest\minor_quests\mq040\mq040_biosculpt.gamedef` | content candidate | base\quest\minor_quests\mq040\mq040_biosculpt.quest |
| `base\quest\minor_quests\mq041\mq041_corpo.gamedef` | content candidate | base\quest\minor_quests\mq041\mq041_corpo.quest |
| `base\quest\minor_quests\mq048\mq048.gamedef` | content candidate | base\quest\minor_quests\mq048\mq048.quest |
| `base\quest\minor_quests\mq055\mq055.gamedef` | content candidate | base\quest\minor_quests\mq055\mq055.quest |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.gamedef` | content candidate | base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest |
| `base\quest\main_quests\prologue\q000\q000.gamedef` | content candidate | base\quest\main_quests\prologue\q000\q000.quest |
| `base\quest\main_quests\prologue\q001\q001.gamedef` | content candidate | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q001\test\q001_miss0_mark_world.gamedef` | test/debug | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q003\q003.gamedef` | content candidate | base\quest\main_quests\prologue\q003\q003.quest |
| `base\quest\main_quests\prologue\q005\q005_heist.gamedef` | content candidate | base\quest\main_quests\prologue\q005\q005_heist.quest |
| `base\quest\main_quests\part1\q101\q101.gamedef` | content candidate | base\quest\main_quests\part1\q101\q101.quest |
| `base\quest\main_quests\part1\q103\q103.gamedef` | content candidate | base\quest\main_quests\part1\q103\q103.quest |
| `base\quest\main_quests\part1\q105\q105_main.gamedef` | content candidate | base\quest\main_quests\part1\q105\q105_main.quest |
| `base\quest\main_quests\part1\q108\q108_johnny.gamedef` | content candidate | base\quest\main_quests\part1\q108\q108_johnny.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q113\q113.gamedef` | content candidate | base\quest\main_quests\part1\q113\q113.quest |
| `base\quest\main_quests\part1\q114\q114_nomads.gamedef` | content candidate | base\quest\main_quests\part1\q114\q114_nomads.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\main_quests\epilogue\q202\q202.gamedef` | content candidate | base\quest\main_quests\epilogue\q202\q202.quest |
| `base\quest\main_quests\epilogue\q203\q203_legend.gamedef` | content candidate | base\quest\main_quests\epilogue\q203\q203_legend.quest |
| `base\quest\main_quests\epilogue\q204\q204_reborn.gamedef` | content candidate | base\quest\main_quests\epilogue\q204\q204_reborn.quest |
| `base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.gamedef` | content candidate | base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `base\quest\side_quests\sq004\sq004_riders_on_the_storm.gamedef` | content candidate | base\quest\side_quests\sq004\sq004_riders_quest.quest |
| `base\quest\side_quests\sq006\sq006.gamedef` | content candidate | base\quest\side_quests\sq006\sq006.quest |
| `base\quest\side_quests\sq011\sq011.gamedef` | content candidate | base\quest\side_quests\sq011\sq011.quest |
| `base\quest\side_quests\sq012\sq012_the_law.gamedef` | content candidate | base\quest\side_quests\sq012\sq012_the_law.quest |
| `base\quest\side_quests\sq017\sq017.gamedef` | content candidate | base\quest\side_quests\sq017\sq017.quest |
| `base\quest\side_quests\sq018\sq018.gamedef` | content candidate | base\quest\side_quests\sq018\sq018.quest |
| `base\quest\side_quests\sq021\sq021.gamedef` | content candidate | base\quest\side_quests\sq021\sq021.quest |
| `base\quest\side_quests\sq023\sq023.gamedef` | content candidate | base\quest\side_quests\sq023\sq023.quest |
| `base\quest\side_quests\sq024\sq024.gamedef` | content candidate | base\quest\side_quests\sq024\sq024.quest |
| `base\quest\side_quests\sq025\sq025.gamedef` | content candidate | base\quest\side_quests\sq025\sq025.quest |
| `base\quest\side_quests\sq026\sq026.gamedef` | content candidate | base\quest\side_quests\sq026\sq026.quest |
| `base\quest\side_quests\sq027\sq027_queen_of_the_highway.gamedef` | content candidate | base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest |
| `base\quest\side_quests\sq028\sq028.gamedef` | content candidate | base\quest\side_quests\sq028\sq028.quest |
| `base\quest\side_quests\sq029\sq029.gamedef` | content candidate | base\quest\side_quests\sq029\sq029.quest |
| `base\quest\side_quests\sq030\sq030.gamedef` | content candidate | base\quest\side_quests\sq030\sq030.quest |
| `base\quest\side_quests\sq031\sq031.gamedef` | content candidate | base\quest\side_quests\sq031\sq031.quest |
| `base\quest\side_quests\sq032\sq032.gamedef` | content candidate | base\quest\side_quests\sq032\sq032.quest |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq303\mq303.gamedef` | content candidate | ep1\quest\minor_quests\mq303\mq303.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq305\mq305.gamedef` | content candidate | ep1\quest\minor_quests\mq305\mq305.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.gamedef` | content candidate | ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest |
| `ep1\quest\main_quests\q304\q304.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\q304_car_retrieval_test.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_escape.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_lab.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_songbird_finale.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_stadium.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q305\q305.gamedef` | content candidate | ep1\quest\main_quests\q305\q305.quest |
| `ep1\quest\main_quests\q306\q306.gamedef` | content candidate | ep1\quest\main_quests\q306\q306.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| No attributed direct resource binding | Attribution unresolved | — |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `CYB-635989` | base\quest\bugfixing\prologue\q003\q003_quest_bugfixes.questphase / h225 / 11; base\quest\bugfixing\prologue\q005\q005_quest_bugfixes.questphase / h68 / 2; 2 total source locations in compressed evidence |
| `q001_checked_stash` | base\quest\main_quests\prologue\q001\phases\q001_ride_to_mb.questphase / h0 / 130; base\quest\main_quests\prologue\q001\q001.questphase / h586 / 66; 2 total source locations in compressed evidence |
| `q001_completed` | base\quest\main_quests\prologue\q001\phases\q001_cleanup.questphase / h0 / 3; 1 total source locations in compressed evidence |
| `q001_e3_fog_hack` | base\quest\main_quests\prologue\q001\phases\q001_path_to_diner.questphase / h0 / 305; base\quest\main_quests\prologue\q001\phases\q001_path_to_diner.questphase / h198 / 16; 2 total source locations in compressed evidence |
| `q001_jackie_on_mistys_chair` | base\quest\main_quests\prologue\q001\phases\q001_cleanup.questphase / h0 / 26; base\quest\main_quests\prologue\q001\scenes\q001_04a_rd_assistant.scene / scene / 802; 2 total source locations in compressed evidence |
| `q001_just_after_rd_scene` | base\quest\main_quests\prologue\q001\phases\q001_ripperdoc.questphase / h0 / 183; 1 total source locations in compressed evidence |
| `q001_mission0_complete` | base\quest\minor_quests\mq048\mq048.questphase / h32 / 26; base\quest\minor_quests\mq048\mq048.questphase / h198 / 11; base\quest\minor_quests\mq055\mq055.quest / h37 / 32; base\quest\main_quests\prologue\q001\phases\q001_mission0.questphase / h755 / 4; 14 total source locations in compressed evidence |
| `q001_show_sts_tut` | base\quest\minor_quests\mq007\mq007.quest / h0 / 15; base\quest\minor_quests\mq048\mq048.questphase / h198 / 22; base\quest\main_quests\prologue\q001\phases\q001_path_to_diner.questphase / h0 / 290; base\quest\main_quests\prologue\q001\phases\q001_path_to_diner.questphase / h198 / 2; 4 total source locations in compressed evidence |
| `q001_sq_tbug_done` | ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 649; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 663; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 676; 3 total source locations in compressed evidence |
| `q001_takedown_tutorial_failed` | base\quest\main_quests\prologue\q001\phases\q001_scavengers_gameplay.questphase / h136 / 46; 1 total source locations in compressed evidence |
| `q001_tbug_netrunner_tut` | base\quest\main_quests\prologue\q001\phases\q001_ride_to_mb.questphase / h1138 / 3; base\quest\main_quests\prologue\q001\q001.questphase / h226 / 3; 2 total source locations in compressed evidence |

NodeRef uses: 60; TweakDB binding uses: 59. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
