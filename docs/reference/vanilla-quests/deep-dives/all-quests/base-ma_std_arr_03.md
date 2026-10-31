# NO_TITLE

Journal: `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_03` · `Contract` · hash `2927611447`.

**Coverage: POI-linked; quest activation unresolved.** 7 exact POI-linked nodes in 5 resources; 6 resources in the inspected dependency context.

Resource roles in that context: 4 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Neutralize all enemies. (Primary) | `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_03/ma_std_arr_03/get_rid_of_hostile_enemies_in_area` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `open_world_minor_activities.questphase / h1068 / 12` (Journal) | `points_of_interest/minor_activities/ma_std_arr_03` | 0:Out → 12:Active |
| `arroyo_minor_activities.questphase / h0 / 45` (Journal) | `points_of_interest/minor_activities/ma_std_arr_03` | 45:Out → 3:In1; 57:Out → 45:In |
| `ma_std_arr_03_phase.questphase / h0 / 52` (Journal) | `points_of_interest/minor_activities/ma_std_arr_03` | 0:Out → 52:Active; 52:Out → 53:In |
| `ma_std_arr_03_phase.questphase / h0 / 56` (Journal) | `points_of_interest/minor_activities/ma_std_arr_03` | 167:Out1 → 56:In; 56:Out → 66:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 7` (Journal) | `points_of_interest/minor_activities/ma_std_arr_03` | 2:Out → 7:Active; 7:Out → 8:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 9` (Journal) | `points_of_interest/minor_activities/ma_std_arr_03` | 64:False → 9:In; 44:Out → 9:In; 9:Out → 16:In |
| `open_world_bugfixing.questphase / h3474 / 76` (Journal) | `points_of_interest/minor_activities/ma_std_arr_03` | 87:False → 76:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `arroyo_minor_activities.questphase / h0 / 3` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` | 45:Out → 3:In1 |
| `ma_std_arr_03_phase.questphase / h0 / 162` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene`; `#ma_sm_std_arr_03_holocall_brief` | 178:False → 162:Start 0; 162:rejected_out → 179:Active; 162:Holocall INT → 170:In; 162:Holocall RET → 169:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 32` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene`; `#ma_sm_std_arr_03_holocall_brief` | 41:False → 32:Start 0; 32:rejected_out → 42:Active; 32:Holocall INT → 36:In; 32:Holocall RET → 35:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\community\badlands\inland_avenue\bad_ina_quest.quest` / h0 / 9 | `open_world_minor_activities.questphase` |  |
| `base\open_world\phases\open_world_content.questphase` / h0 / 11 | `open_world_minor_activities.questphase` | 0: Input; 122: Input; 0:Out → 11:In1; 122:Out → 11:In1 |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 6 | `open_world_minor_activities.questphase` | 0: Start; 0:Out → 6:In1 |
| `base\open_world\district_definitions\open_world_kabuki.quest` / h842 / 61 | `arroyo_minor_activities.questphase` | 0: Input; 0:Out → 61:In1 |
| `base\open_world\minor_activities\open_world_minor_activities.questphase` / h0 / 12 | `arroyo_minor_activities.questphase` | 37: LogicalHub; 37:Out1 → 12:In1 |
| `base\open_world\open_world_test.quest` / h851 / 61 | `arroyo_minor_activities.questphase` | 0: Input; 0:Out → 61:In1 |
| `base\open_world\minor_activities\santo_domingo\arroyo\arroyo_minor_activities.questphase` / h0 / 3 | `ma_std_arr_03_phase.questphase` | 45: Journal; 45:Out → 3:In1 |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03.quest` / h0 / 0 | `ma_std_arr_03_phase.questphase` | 1: TeleportPuppet; 1:Out → 0:In1 |
| `base\open_world\bugfixing\ma\ma_arroyo_bugfixing.questphase` / h0 / 22 | `ma_std_arr_03_bugfixing.questphase` | 24: DeletionMarker; 24:Out → 22:In1 |
| `base\open_world\bugfixing\ma\ma_arroyo_bugfixing.questphase` / h0 / 30 | `ma_std_arr_03_bugfixing.questphase` | 32: DeletionMarker; 32:Out → 30:cast_review_signal |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h0 / 162 | `ma_std_arr_03_holocall_brief.scene` | 178: Condition; 178:False → 162:Start 0; 162:rejected_out → 179:Active; 162:Holocall INT → 170:In; 162:Holocall RET → 169:In |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase` / h65 / 32 | `ma_std_arr_03_holocall_brief.scene` | 41: Condition; 41:False → 32:Start 0; 32:rejected_out → 42:Active; 32:Holocall INT → 36:In; 32:Holocall RET → 35:In |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\district_definitions\open_world_kabuki.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\metro\ue_metro\ue_metro.quest` / h0 / 21 | `open_world_content.questphase` | 0: Start; 0:Out → 21:EP1_Standalone |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest` / h0 / 7 | `open_world_content.questphase` | 8: Scene: ma_bls_ina_07_chicken.scene; 8:start → 7:In1 |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest` / h0 / 3 | `open_world_content.questphase` | 2: FactsDBManager: sts_std_arr_tier_1; 2:Out → 3:In1 |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest` / h0 / 4 | `open_world_content.questphase` | 3: FactsDBManager: sts_wat_kab_tier_1; 3:Out → 4:In1 |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.quest` / h0 / 3 | `open_world_content.questphase` | 2: FactsDBManager: sts_wat_nid_tier_1; 2:Out → 3:In1 |
| `base\open_world\open_world_test.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\police_system\police_system_test.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest` / h0 / 4 | `open_world_content.questphase` | 0: Start; 0:Out → 4:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 19 | `open_world_content.questphase` | 0: Input; 36: Input; 0:Out → 19:In1; 36:Out → 19:EP1_Standalone |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h3390 / 14 | `ma_arroyo_bugfixing.questphase` | 22: DeletionMarker; 22:Out → 14:In1 |
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
| `ma_std_arr_03_holocall_brief.scene` | Start 0 → End 0, rejected_out | NCPD_dispatcher; 15 nodes / 14 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-641040` | ma_std_arr_03_bugfixing.questphase / h0 / 2 | ma_std_arr_03_bugfixing.questphase / h0 / 48 |
| `CYB-663009` | ma_std_arr_03_bugfixing.questphase / h0 / 47 | ma_std_arr_03_bugfixing.questphase / h0 / 8; ma_std_arr_03_phase.questphase / h0 / 195 |
| `holo_ncpd_dispatcher_calls_v_end_activate` | ma_std_arr_03_bugfixing.questphase / h65 / 36; ma_std_arr_03_holocall_brief.scene / scene / 66; ma_std_arr_03_phase.questphase / h0 / 170 | No reader in selected context |
| `holo_ncpd_dispatcher_calls_v_end_done` | ma_std_arr_03_holocall_brief.scene / scene / 62 | ma_std_arr_03_holocall_brief.scene / scene / 61 |
| `holo_ncpd_dispatcher_calls_v_rejectable` | ma_std_arr_03_holocall_brief.scene / scene / 254 | No reader in selected context |
| `holo_ncpd_dispatcher_calls_v_rejected` | ma_std_arr_03_holocall_brief.scene / scene / 256 | ma_std_arr_03_holocall_brief.scene / scene / 258 |
| `holo_ncpd_dispatcher_calls_v_start_activate` | ma_std_arr_03_bugfixing.questphase / h65 / 35; ma_std_arr_03_holocall_brief.scene / scene / 65; ma_std_arr_03_phase.questphase / h0 / 169 | No reader in selected context |
| `holo_ncpd_dispatcher_calls_v_start_done` | ma_std_arr_03_holocall_brief.scene / scene / 60 | ma_std_arr_03_holocall_brief.scene / scene / 59 |
| `ma_arr_03_finished` | ma_std_arr_03_bugfixing.questphase / h65 / 16; ma_std_arr_03_phase.questphase / h0 / 66 | ma_std_arr_03_bugfixing.questphase / h0 / 6; ma_std_arr_03_bugfixing.questphase / h0 / 9; open_world_bugfixing.questphase / h3474 / 87 |
| `ma_arr_03_start` | ma_std_arr_03_bugfixing.questphase / h65 / 22; ma_std_arr_03_phase.questphase / h0 / 96 | No reader in selected context |
| `ma_outpost_tutorial` | ma_std_arr_03_bugfixing.questphase / h65 / 18; ma_std_arr_03_phase.questphase / h0 / 68 | No reader in selected context |
| `ma_std_arr_03_combat_triggered` | ma_std_arr_03_bugfixing.questphase / h65 / 60 | ma_std_arr_03_bugfixing.questphase / h65 / 64 |
| `ma_token` | ma_std_arr_03_bugfixing.questphase / h65 / 17; ma_std_arr_03_phase.questphase / h0 / 67 | No reader in selected context |
| `std_achievement` | ma_std_arr_03_bugfixing.questphase / h65 / 23; ma_std_arr_03_phase.questphase / h0 / 97 | ma_std_arr_03_bugfixing.questphase / h0 / 28 |
| `travelling_merchant` | Producer outside selected context | ma_std_arr_03_bugfixing.questphase / h0 / 45 |

## Exact gates, joins and cancellation

<details><summary>81 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `arroyo_minor_activities.questphase / h0 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType"}}}` | 21:Out → 57:In; 57:Out → 4:In1; 57:Out → 43:In; 57:Out → 44:In; 57:Out → 45:In; 57:Out → 46:In |
| `ma_std_arr_03_phase.questphase / h0 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_std_arr_03_tr"}}` | 51:Out → 50:In1; 176:Out → 51:In |
| `ma_std_arr_03_phase.questphase / h0 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_03_tr"}}` | 52:Out → 53:In; 53:Out → 68:In |
| `ma_std_arr_03_phase.questphase / h0 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_com"},"comparisonParams":{"$type":"questComparisonParam","count":6,"comparisonType":"GreaterOrEqual"}}}}` | 45:Out → 58:In; 58:Out → 111:In; 58:Out → 109:In; 58:Out → 60:In; 58:Out → 59:In; 58:Out → 107:In; 58:Out → 87:In; 58:Out → 155:In1; 58:Out → 174:In; 58:Out → 184:In |
| `ma_std_arr_03_phase.questphase / h0 / 111` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_03_patrol_tr_01"}}` | 58:Out → 111:In; 111:Out → 63:In |
| `ma_std_arr_03_phase.questphase / h0 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_car_01"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 113:Out → 61:In; 64:Out → 113:In |
| `ma_std_arr_03_phase.questphase / h0 / 161` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_03_tr_brief"},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}}]}}` | 0:Out → 161:In; 163:CutSource → 161:CutDestination; 161:Out → 178:In |
| `ma_std_arr_03_phase.questphase / h0 / 163` | `questCutControlNodeDefinition` `{}` | 163:CutSource → 161:CutDestination; 167:Out1 → 163:In; 163:Out → 175:In |
| `ma_std_arr_03_phase.questphase / h0 / 167` | `questLogicalXorNodeDefinition` `{}` | 167:Out1 → 56:In; 167:Out1 → 163:In; 188:Out1 → 167:In1; 183:Out1 → 167:In2 |
| `ma_std_arr_03_phase.questphase / h0 / 171` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questSaveLock_ConditionType"}}}` | 96:Out → 171:In; 171:False → 103:In |
| `ma_std_arr_03_phase.questphase / h0 / 172` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questSaveLock_ConditionType"}}}` | 88:Out → 172:In; 172:False → 104:In |
| `ma_std_arr_03_phase.questphase / h0 / 176` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 176:Out → 51:In; 175:Out → 176:In |
| `ma_std_arr_03_phase.questphase / h0 / 177` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\minor_activities\\santo_domingo\\arroyo\\ma_std_arr_03\\scenes\\ma_std_arr_03_holocall_brief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 177:Out → 1:In; 50:Out1 → 177:In |
| `ma_std_arr_03_phase.questphase / h0 / 178` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"ncpd_dispatcher"}}}` | 161:Out → 178:In; 178:False → 162:Start 0; 178:True → 179:Active |
| `ma_std_arr_03_phase.questphase / h0 / 181` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_std_arr_03_sec_sys","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 184:Out → 181:In; 181:Out → 183:In2 |
| `ma_std_arr_03_phase.questphase / h0 / 182` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinforcements"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 184:Out → 182:In; 182:Out → 183:In3 |
| `ma_std_arr_03_phase.questphase / h0 / 183` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 183:Out1 → 167:In2; 181:Out → 183:In2; 182:Out → 183:In3; 194:Out → 183:In1 |
| `ma_std_arr_03_phase.questphase / h0 / 185` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_std_arr_03_sec_sys","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemSafe"}}}` | 190:Out → 185:In; 185:Out → 189:In1 |
| `ma_std_arr_03_phase.questphase / h0 / 187` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_std_arr_03_sec_sys","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemAlerted"}}}` | 190:Out → 187:In; 187:Out → 189:In2 |
| `ma_std_arr_03_phase.questphase / h0 / 188` | `questLogicalAndNodeDefinition` `{}` | 188:Out1 → 167:In1; 192:Out → 188:In1; 189:Out1 → 188:In2 |
| `ma_std_arr_03_phase.questphase / h0 / 189` | `questLogicalXorNodeDefinition` `{}` | 185:Out → 189:In1; 187:Out → 189:In2; 189:Out1 → 188:In2 |
| `ma_std_arr_03_phase.questphase / h0 / 192` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_com"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 192:Out → 188:In1; 190:Out → 192:In |
| `ma_std_arr_03_phase.questphase / h0 / 194` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_com"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 194:Out → 183:In1; 184:Out → 194:In |
| `ma_std_arr_03_phase.questphase / h0 / 195` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-663009"}}}` | 195:Out → 1:In; 190:Out → 195:In |
| `ma_std_arr_03_phase.questphase / h239 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinf_car_01"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2:Out → 3:In; 3:Out → 4:In |
| `ma_std_arr_03_phase.questphase / h239 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinforcements","names":["ganger_01","ganger_02","ganger_03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":3,"comparisonType":"GreaterOrEqual"}}}}` | 4:Out → 11:In; 11:Out → 12:In1; 11:Out → 48:In |
| `ma_std_arr_03_phase.questphase / h239 / 13` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 5:Out → 13:In1; 6:Out → 13:In2; 7:Out → 13:In3; 13:Out1 → 15:In |
| `ma_std_arr_03_phase.questphase / h239 / 20` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 20:Out1 → 9:In; 16:Out → 20:In1; 17:Out → 20:In2; 18:Out → 20:In3; 20:Out1 → 62:In; 20:Out1 → 63:In; 20:Out1 → 64:In |
| `ma_std_arr_03_phase.questphase / h239 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinf_car_02"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 41:Out → 22:In; 22:Out → 23:In |
| `ma_std_arr_03_phase.questphase / h239 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinforcements","names":["ganger_05","ganger_06"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":2,"comparisonType":"GreaterOrEqual"}}}}` | 23:Out → 24:In; 24:Out → 29:In1; 24:Out → 45:In |
| `ma_std_arr_03_phase.questphase / h239 / 30` | `questLogicalAndNodeDefinition` `{}` | 25:Out → 30:In1; 26:Out → 30:In2; 30:Out1 → 31:In |
| `ma_std_arr_03_phase.questphase / h239 / 38` | `questLogicalAndNodeDefinition` `{}` | 32:Out → 38:In1; 33:Out → 38:In2; 38:Out1 → 36:In; 38:Out1 → 59:In; 38:Out1 → 61:In |
| `ma_std_arr_03_phase.questphase / h239 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 24:Out → 45:In; 45:Out → 43:In; 45:Out → 44:In |
| `ma_std_arr_03_phase.questphase / h239 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 11:Out → 48:In; 48:Out → 46:In; 48:Out → 47:In; 48:Out → 49:In |
| `ma_std_arr_03_phase.questphase / h239 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_com"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":3,"comparisonType":"GreaterOrEqual"}}}}` | 52:Out → 50:In; 50:Out → 65:In |
| `ma_std_arr_03_phase.questphase / h239 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_std_arr_03_sec_sys","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 52:Out → 50:In; 55:Out → 52:In; 52:Out → 57:In |
| `ma_std_arr_03_phase.questphase / h239 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_com"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 57:Out → 2:In; 52:Out → 57:In |
| `ma_std_arr_03_phase.questphase / h239 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_std_arr_03_sec_sys","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 65:Out → 41:In; 50:Out → 65:In |
| `ma_std_arr_03_bugfixing.questphase / h0 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_std_arr_03_tr"}}` | 4:Out → 3:In; 5:Out → 4:In |
| `ma_std_arr_03_bugfixing.questphase / h0 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 5:Out → 4:In; 6:True → 5:In |
| `ma_std_arr_03_bugfixing.questphase / h0 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_arr_03_finished"}}}` | 2:Out → 6:In; 6:True → 5:In |
| `ma_std_arr_03_bugfixing.questphase / h0 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-663009"}}}` | 46:Out1 → 8:In; 8:False → 47:In |
| `ma_std_arr_03_bugfixing.questphase / h0 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_arr_03_finished"}}}` | 43:Out → 9:In; 9:False → 31:In |
| `ma_std_arr_03_bugfixing.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_std_arr_03_tr_reset"}}` | 43:Out → 9:In; 42:Out → 43:In |
| `ma_std_arr_03_bugfixing.questphase / h0 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant","value":9999}}}` | 44:Out → 45:In |
| `ma_std_arr_03_bugfixing.questphase / h0 / 46` | `questLogicalXorNodeDefinition` `{}` | 0:Out → 46:In1; 46:Out1 → 8:In; 44:Out → 46:In2 |
| `ma_std_arr_03_bugfixing.questphase / h0 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-641040"}}}` | 0:Out → 48:In; 48:False → 2:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_03_tr"}}` | 7:Out → 8:In; 8:Out → 18:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_com"},"comparisonParams":{"$type":"questComparisonParam","count":6,"comparisonType":"GreaterOrEqual"}}}}` | 4:Out → 10:In; 10:Out → 28:In; 10:Out → 27:In; 10:Out → 12:In; 10:Out → 11:In; 10:Out → 26:In; 10:Out → 20:In; 10:Out → 50:In; 10:Out → 55:In; 10:Out → 59:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_03_patrol_tr_01"}}` | 10:Out → 28:In; 28:Out → 14:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_car_01"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 29:Out → 13:In; 15:Out → 29:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_03_tr_brief"},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}}]}}` | 2:Out → 31:In; 33:CutSource → 31:CutDestination; 31:Out → 41:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 33` | `questCutControlNodeDefinition` `{}` | 33:CutSource → 31:CutDestination; 64:False → 33:In; 44:Out → 33:In; 33:Out → 79:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 37` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questSaveLock_ConditionType"}}}` | 22:Out → 37:In; 37:False → 24:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 38` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questSaveLock_ConditionType"}}}` | 21:Out → 38:In; 38:False → 25:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 41` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"ncpd_dispatcher"}}}` | 31:Out → 41:In; 41:False → 32:Start 0; 41:True → 42:Active |
| `ma_std_arr_03_bugfixing.questphase / h65 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinforcements"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 44:Out → 9:In; 44:Out → 33:In; 64:True → 44:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_com"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 10:Out → 50:In; 57:Out → 50:In; 56:Out → 50:In; 63:Out → 50:In; 61:Out → 50:In; 58:Out → 50:In; 62:Out → 50:In; 66:Out → 50:In; 65:Out → 50:In; 50:Out → 64:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_std_arr_03_sec_sys","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 10:Out → 59:In; 59:Out → 60:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 64` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_std_arr_03_combat_triggered","value":1,"comparisonType":"GreaterOrEqual"}}}` | 64:False → 9:In; 64:False → 33:In; 64:True → 44:In; 50:Out → 64:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 76` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_std_arr_03_tr"}}` | 76:Out → 75:In1; 77:Out → 76:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 77:Out → 76:In; 79:Out → 77:In |
| `ma_std_arr_03_bugfixing.questphase / h65 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\minor_activities\\santo_domingo\\arroyo\\ma_std_arr_03\\scenes\\ma_std_arr_03_holocall_brief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 75:Out1 → 78:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinf_car_01"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3:Out → 4:In; 4:Out → 5:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinforcements","names":["ganger_01","ganger_02","ganger_03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":3,"comparisonType":"GreaterOrEqual"}}}}` | 5:Out → 10:In; 10:Out → 11:In1; 10:Out → 38:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 12` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 6:Out → 12:In1; 7:Out → 12:In2; 8:Out → 12:In3; 12:Out1 → 13:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 17` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 17:Out1 → 9:In; 14:Out → 17:In1; 15:Out → 17:In2; 16:Out → 17:In3; 17:Out1 → 45:In; 17:Out1 → 46:In; 17:Out1 → 47:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinf_car_02"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 32:Out → 19:In; 19:Out → 20:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_reinforcements","names":["ganger_05","ganger_06"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":2,"comparisonType":"GreaterOrEqual"}}}}` | 20:Out → 21:In; 21:Out → 24:In1; 21:Out → 35:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 25` | `questLogicalAndNodeDefinition` `{}` | 22:Out → 25:In1; 23:Out → 25:In2; 25:Out1 → 26:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 30` | `questLogicalAndNodeDefinition` `{}` | 27:Out → 30:In1; 28:Out → 30:In2; 30:Out1 → 29:In; 30:Out1 → 43:In; 30:Out1 → 44:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 21:Out → 35:In; 35:Out → 33:In; 35:Out → 34:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 10:Out → 38:In; 38:Out → 36:In; 38:Out → 37:In; 38:Out → 39:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_com"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":3,"comparisonType":"GreaterOrEqual"}}}}` | 41:Out → 40:In; 40:Out → 48:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_std_arr_03_sec_sys","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 2:Out → 41:In; 41:Out → 40:In; 41:Out → 42:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_03_com"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 42:Out → 3:In; 41:Out → 42:In |
| `ma_std_arr_03_bugfixing.questphase / h353 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_std_arr_03_sec_sys","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 48:Out → 32:In; 40:Out → 48:In |
| `ma_std_arr_03_holocall_brief.scene / scene / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_ncpd_dispatcher_calls_v_start_done"}}}` | 59:0:0 → 60:0:1; 254:0:0 → 59:0:1 |
| `ma_std_arr_03_holocall_brief.scene / scene / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_ncpd_dispatcher_calls_v_end_done"}}}` | 61:0:0 → 62:0:1; 66:0:0 → 61:0:1 |
| `ma_std_arr_03_holocall_brief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_ncpd_dispatcher_calls_v_rejected"}}}` | 254:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `open_world_bugfixing.questphase / h3474 / 87` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_arr_03_finished"}}}` | 87:False → 76:In; 135:Out1 → 87:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | ma_std_arr_03_bugfixing.questphase / h353 / 10; ma_std_arr_03_bugfixing.questphase / h353 / 19; ma_std_arr_03_bugfixing.questphase / h353 / 21; ma_std_arr_03_bugfixing.questphase / h353 / 4; +8 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | ma_std_arr_03_bugfixing.questphase / h65 / 24; ma_std_arr_03_bugfixing.questphase / h65 / 25; ma_std_arr_03_phase.questphase / h0 / 103; ma_std_arr_03_phase.questphase / h0 / 104 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `combat_control` | ma_std_arr_03_bugfixing.questphase / h353 / 18; ma_std_arr_03_bugfixing.questphase / h353 / 29; ma_std_arr_03_bugfixing.questphase / h353 / 31; ma_std_arr_03_bugfixing.questphase / h353 / 9; +4 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | ma_std_arr_03_bugfixing.questphase / h0 / 3; ma_std_arr_03_bugfixing.questphase / h0 / 32; ma_std_arr_03_bugfixing.questphase / h0 / 33; ma_std_arr_03_bugfixing.questphase / h0 / 34; +11 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | ma_std_arr_03_bugfixing.questphase / h0 / 45; ma_std_arr_03_bugfixing.questphase / h0 / 48; ma_std_arr_03_bugfixing.questphase / h0 / 6; ma_std_arr_03_bugfixing.questphase / h0 / 8; +7 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | ma_std_arr_03_bugfixing.questphase / h0 / 41; ma_std_arr_03_bugfixing.questphase / h737 / 4; ma_std_arr_03_phase.questphase / h28 / 4 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_state` | ma_std_arr_03_bugfixing.questphase / h353 / 41; ma_std_arr_03_bugfixing.questphase / h353 / 48; ma_std_arr_03_bugfixing.questphase / h65 / 59; ma_std_arr_03_phase.questphase / h0 / 181; +4 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | ma_std_arr_03_bugfixing.questphase / h0 / 5; ma_std_arr_03_bugfixing.questphase / h65 / 77; ma_std_arr_03_phase.questphase / h0 / 176 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | arroyo_minor_activities.questphase / h0 / 45; ma_std_arr_03_bugfixing.questphase / h65 / 42; ma_std_arr_03_bugfixing.questphase / h65 / 7; ma_std_arr_03_bugfixing.questphase / h65 / 9; +5 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | ma_std_arr_03_bugfixing.questphase / h65 / 20; ma_std_arr_03_phase.questphase / h0 / 87 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `parallel_join` | ma_std_arr_03_bugfixing.questphase / h353 / 12; ma_std_arr_03_bugfixing.questphase / h353 / 17; ma_std_arr_03_bugfixing.questphase / h353 / 25; ma_std_arr_03_bugfixing.questphase / h353 / 30; +6 locations in catalogue.json | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | ma_std_arr_03_bugfixing.questphase / h0 / 2; ma_std_arr_03_bugfixing.questphase / h0 / 47; ma_std_arr_03_bugfixing.questphase / h65 / 16; ma_std_arr_03_bugfixing.questphase / h65 / 17; +19 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | ma_std_arr_03_bugfixing.questphase / h0 / 46; ma_std_arr_03_phase.questphase / h0 / 167; ma_std_arr_03_phase.questphase / h0 / 189 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | ma_std_arr_03_bugfixing.questphase / h353 / 35; ma_std_arr_03_bugfixing.questphase / h353 / 38; ma_std_arr_03_phase.questphase / h239 / 45; ma_std_arr_03_phase.questphase / h239 / 48 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | ma_std_arr_03_bugfixing.questphase / h65 / 33; ma_std_arr_03_phase.questphase / h0 / 163 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | ma_std_arr_03_bugfixing.questphase / h65 / 21; ma_std_arr_03_phase.questphase / h0 / 88 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `save_eligibility` | ma_std_arr_03_bugfixing.questphase / h65 / 37; ma_std_arr_03_bugfixing.questphase / h65 / 38; ma_std_arr_03_phase.questphase / h0 / 171; ma_std_arr_03_phase.questphase / h0 / 172 | save-lock predicate + fallback path → save eligibility branch. Separate blocked-save fallback from checkpoint creation and verify installed behavior. |
| `scene_interface` | ma_std_arr_03_bugfixing.questphase / h65 / 32; ma_std_arr_03_phase.questphase / h0 / 162 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | ma_std_arr_03_bugfixing.questphase / h0 / 4; ma_std_arr_03_bugfixing.questphase / h0 / 43; ma_std_arr_03_bugfixing.questphase / h65 / 28; ma_std_arr_03_bugfixing.questphase / h65 / 31; +6 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | ma_std_arr_03_bugfixing.questphase / h353 / 40; ma_std_arr_03_bugfixing.questphase / h353 / 42; ma_std_arr_03_bugfixing.questphase / h65 / 44; ma_std_arr_03_bugfixing.questphase / h65 / 50; +5 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | ma_std_arr_03_bugfixing.questphase / h353 / 14; ma_std_arr_03_bugfixing.questphase / h353 / 15; ma_std_arr_03_bugfixing.questphase / h353 / 16; ma_std_arr_03_bugfixing.questphase / h353 / 22; +18 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\minor_activities\open_world_minor_activities.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\minor_activities\santo_domingo\arroyo\arroyo_minor_activities.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` | content candidate; journal anchor | `base-ma-std-arr-03` |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase` | repair; journal anchor | `base-ma-std-arr-03` |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` | content candidate; forward dependency | `base-ma-std-arr-03` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-03.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

125 repeated typed/socket path signatures in this selected graph context; 3 distinct direct resource identities; 6 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h0 / 66 -> 67 -> 97 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `20a77143a898bc753a26` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase` / h0 / 32 -> 33 -> 34 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `987122e5e2fcd167cf6c` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h0 / 0 -> 45 -> 58 | questInputNodeDefinition -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` / scene / 254 -> 258 -> 256 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h0 / 175 -> 176 -> 51 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` / scene / 64 -> 66 -> 61 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` / scene / 258 -> 256 -> 260 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` / scene / 60 -> 63 -> 29 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` / scene / 29 -> 64 -> 66 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` / scene / 65 -> 254 -> 59 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` / scene / 1 -> 65 -> 254 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase` / h0 / 0 -> 48 -> 2 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h0 / 50 | `h28` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h0 / 155 | `h239` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase` / h0 / 26 | `h65` | [{"$type":"questInputNodeDefinition","id":2,"socketName":"In"},{"$type":"questOutputNodeDefinition","id":67,"socketName":"Out1","type":"NonTerminating"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase` / h65 / 55 | `h353` | [{"$type":"questInputNodeDefinition","id":2,"socketName":"In"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase` / h65 / 75 | `h737` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\arroyo_minor_activities.questphase` / h0 / 3 | `h55` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03.quest |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_def.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.gamedef` | content candidate | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.quest |
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
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q113\q113.gamedef` | content candidate | base\quest\main_quests\part1\q113\q113.quest |
| `base\quest\main_quests\part1\q114\q114_nomads.gamedef` | content candidate | base\quest\main_quests\part1\q114\q114_nomads.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\main_quests\epilogue\q202\q202.gamedef` | content candidate | base\quest\main_quests\epilogue\q202\q202.quest |
| `base\quest\main_quests\epilogue\q203\q203_legend.gamedef` | content candidate | base\quest\main_quests\epilogue\q203\q203_legend.quest |
| `base\quest\main_quests\epilogue\q204\q204_reborn.gamedef` | content candidate | base\quest\main_quests\epilogue\q204\q204_reborn.quest |
| `base\open_world\community\badlands\inland_avenue\bad_ina_se1_test_def.gamedef` | content candidate | base\open_world\community\badlands\inland_avenue\bad_ina_quest.quest |
| `base\open_world\community\badlands\inland_avenue\bad_ina_se5_test_def.gamedef` | content candidate | base\open_world\community\badlands\inland_avenue\bad_ina_quest.quest |
| `base\open_world\community\heywood\glen\hey_gle_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\heywood\wellsprings\hey_spr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\heywood\wellsprings\hey_spr_testdef.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\pacifica\west_wind_estate\pac_wwd_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\santo_domingo\arroyo\std_arr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\santo_domingo\rancho_coronado\std_rcr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\kabuki\wat_kab_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\kabuki\wat_kab_testdef.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\little_china\wat_lch_prolog_ow_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\northside\wat_nid_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\district_definitions\open_world_kabuki.gamedef` | content candidate | base\open_world\district_definitions\open_world_kabuki.quest |
| `base\open_world\open_world_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\police_system\police_system_test.gamedef` | content candidate | base\open_world\police_system\police_system_test.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_kabuki.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_kabuki.quest |
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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\metro\ue_metro\ue_metro.gamedef` | content candidate | base\open_world\metro\ue_metro\ue_metro.quest |
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
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\lipsync\en\ma_std_arr_03_holocall_brief\ncpd_dispatcher.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `holo_ncpd_dispatcher_calls_v_end_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase / h0 / 68; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene / scene / 97; base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase / h0 / 109; base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene / scene / 80; 34 total source locations in compressed evidence |
| `holo_ncpd_dispatcher_calls_v_end_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene / scene / 93; base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene / scene / 76; base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene / scene / 60; base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene / scene / 61; 19 total source locations in compressed evidence |
| `holo_ncpd_dispatcher_calls_v_rejectable` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene / scene / 254; base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene / scene / 254; base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene / scene / 254; base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene / scene / 254; 18 total source locations in compressed evidence |
| `holo_ncpd_dispatcher_calls_v_rejected` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene / scene / 259; base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene / scene / 258; base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene / scene / 258; base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene / scene / 258; 17 total source locations in compressed evidence |
| `holo_ncpd_dispatcher_calls_v_start_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase / h0 / 67; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene / scene / 96; base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase / h0 / 108; base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene / scene / 79; 35 total source locations in compressed evidence |
| `holo_ncpd_dispatcher_calls_v_start_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene / scene / 91; base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene / scene / 74; base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene / scene / 58; base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene / scene / 59; 19 total source locations in compressed evidence |
| `ma_outpost_tutorial` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase / h0 / 40; base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase / h0 / 28; base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase / h0 / 13; base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase / h0 / 42; 17 total source locations in compressed evidence |
| `ma_token` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_01\ma_bls_ina_se1_01_phase.questphase / h0 / 31; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_02\ma_bls_ina_se1_02_phase.questphase / h0 / 18; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase / h0 / 21; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase / h0 / 38; 339 total source locations in compressed evidence |
| `std_achievement` | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase / h0 / 28; base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase / h0 / 77; base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase / h0 / 92; base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase / h0 / 86; 79 total source locations in compressed evidence |

NodeRef uses: 206; TweakDB binding uses: 5. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` | 1 / 3 | scnDialogLineEvent: 3 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
