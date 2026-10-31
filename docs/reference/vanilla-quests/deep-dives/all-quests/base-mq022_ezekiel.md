# Ezekiel Saw the Wheel

Journal: `quests/minor_quest/mq022_ezekiel` · `MinorQuest` · hash `3697221403`.

**Coverage: journal-linked.** 12 exact journal-linked nodes in 4 resources; 4 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Identify the gunmen. (Primary) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/01_diner` |
| Here's a joke for you: V walks into a bar… and gets robbed. The end.\n\nJesus, you and your shit luck. You better figure something out quick or our epic story's about to get cut short in the stupidest way imaginable. Accidental deaths don't jive too well with me. Or with the birth of legends. (Primary) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide` |
| Talk to the diner owner. (Primary) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/03_outcome` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq022_quest_bugfixes.questphase / h30 / 10` (Condition) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mq022_description` | 10:True → 1:In; 9:Out → 10:In; 10:False → 11:Active |
| `mq022_quest_bugfixes.questphase / h30 / 11` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mq022_description` | 10:False → 11:Active; 11:Out → 12:Succeeded |
| `mq022_quest_bugfixes.questphase / h30 / 12` (Journal) | `quests/minor_quest/mq022_ezekiel` | 12:Out → 1:In; 11:Out → 12:Succeeded |
| `mq022_quest_bugfixes.questphase / h111 / 4` (Condition) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide` | 3:Out → 4:In; 4:True → 6:In |
| `mq022_beginning.questphase / h0 / 40` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide` | 47:Out → 40:Succeeded; 51:Out → 40:Succeeded; 40:Out → 41:Active |
| `mq022_beginning.questphase / h0 / 41` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/03_outcome` | 40:Out → 41:Active; 41:Out → 45:In; 41:Out → 78:In |
| `mq022_beginning.questphase / h0 / 52` (Journal) | `quests/minor_quest/mq022_ezekiel` | 43:mq022_owner_outcome_bad_out → 52:Succeeded; 52:Out → 44:In |
| `mq022_beginning.questphase / h0 / 54` (Journal) | `quests/minor_quest/mq022_ezekiel` | 43:mq022_owner_outcome_good_out → 54:Succeeded; 54:Out → 53:In |
| `mq022_combat.questphase / h0 / 33` (MappinManager) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mp_goon1` | 0:Out → 33:Inactive; 33:Out → 34:Active |
| `mq022_combat.questphase / h0 / 34` (MappinManager) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mp_area` | 33:Out → 34:Active |
| `mq022_01_diner.scene / scene / 152` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide` | 152:0:0 → 267:0:1; 466:0:0 → 152:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq022_01_diner.scene / scene / 267` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mq022_description` | 152:0:0 → 267:0:1; 267:0:0 → 52:0:0; 267:0:0 → 596:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq022_beginning.questphase / h0 / 11` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene`; `#mq022_01_sm_diner` | 32:Out → 11:Start; 11:mq022_attacked → 39:In1; 11:mq022_outtalked → 50:In |
| `mq022_beginning.questphase / h0 / 39` | `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` | 11:mq022_attacked → 39:In1; 39:Out1 → 51:In |
| `mq022_beginning.questphase / h0 / 43` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene`; `#mq022_01_sm_diner` | 42:True → 43:mq022_people_dead; 42:False → 43:mq022_people_alive; 61:False → 43:mq022_people_alive; 43:mq022_owner_outcome_good_out → 54:Succeeded; 43:mq022_owner_outcome_bad_out → 52:Succeeded |
| `mq022_beginning.questphase / h202 / 10` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene`; `#mq022_01_sm_diner` | 11:Out → 10:mq022_01_attack |
| `mq022_combat.questphase / h0 / 14` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene`; `#mq022_01_sm_diner` | 0:Out → 14:mq022_01_attack |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 41 | `mq022_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 41:In1 |
| `base\quest\minor_quests\mq022\mq022.questphase` / h0 / 84 | `mq022_beginning.questphase` | 2: Input; 2:Out → 84:In1; 84:Out1 → 89:In |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h0 / 39 | `mq022_combat.questphase` | 11: Scene: mq022_01_diner.scene; 11:mq022_attacked → 39:In1; 39:Out1 → 51:In |
| `base\quest\default_dialogs.questphase` / h6891 / 4 | `mq022_01_diner.scene` | 10: PauseCondition: std_arr_foodshop_04_default_on; 10:Out → 4:std_arr_foodshop_04; 4:std_arr_foodshop_04_to_choice → 5:std_arr_foodshop_04 |
| `base\quest\default_dialogs.questphase` / h6891 / 6 | `mq022_01_diner.scene` | 5: Scene: wat_nid_foodshop_02.scene; 5:std_arr_foodshop_04_end → 6:std_arr_foodshop_04_from_choice; 6:std_arr_foodshop_04_end → 11:In1 |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h0 / 11 | `mq022_01_diner.scene` | 32: FactsDBManager: mq022_active; 32:Out → 11:Start; 11:mq022_attacked → 39:In1; 11:mq022_outtalked → 50:In |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h0 / 43 | `mq022_01_diner.scene` | 42: Condition; 42: Condition; 61: Condition: mq022_combat; 42:True → 43:mq022_people_dead; 42:False → 43:mq022_people_alive; 61:False → 43:mq022_people_alive; 43:mq022_owner_outcome_good_out → 54:Succeeded; 43:mq022_owner_outcome_bad_out → 52:Succeeded |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h202 / 10 | `mq022_01_diner.scene` | 11: FactsDBManager: mq022_no_choice_done write/default comparison 0; 11:Out → 10:mq022_01_attack |
| `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` / h0 / 14 | `mq022_01_diner.scene` | 0: Input; 0:Out → 14:mq022_01_attack |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 6 | `mq022.questphase` | 47: LogicalHub; 47:Out1 → 6:In1 |
| `base\quest\minor_quests\mq022\mq022.quest` / h0 / 6 | `mq022.questphase` | 14: Phase; 6:Out1 → 3:In; 14:Out1 → 6:In1 |
| `base\open_world\district_definitions\open_world_kabuki.quest` / h0 / 16 | `default_dialogs.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 16:In1 |
| `base\open_world\open_world_test.quest` / h0 / 16 | `default_dialogs.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 16:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 22 | `default_dialogs.questphase` | 30: PauseCondition: q000_done; 36: Input; 30:Out → 22:In1; 36:Out → 22:EP1_Standalone |
| `base\quest\side_quests\sq012\sq012_the_law.quest` / h0 / 8 | `default_dialogs.questphase` |  |
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
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
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
| `mq022_01_diner.scene` | std_arr_foodshop_04, mq022_01_attack, std_arr_foodshop_04_from_choice, mq022_people_dead, mq022_people_alive, Start → mq022_attacked, mq022_01_attack_out, std_arr_foodshop_04_end, mq022_outtalked, mq022_owner_outcome_good_out, std_arr_foodshop_04_to_choice, mq022_owner_outcome_bad_out | Ganger_01; Ganger_02; Ganger_03; Owner; Diner_01; Diner_02; Diner_03; Diner_04; Diner_05; Diner_06; Diner_07; Player; 165 nodes / 192 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq022_01_diner.scene / n93 / 0` | Somebody likes being the center of attention. (``) | No option-level predicate stored | 0:0 → 100:0:0; 0:0 → 522:0:2; 0:0 → 956:0:1 |
| `mq022_01_diner.scene / n104 / 0` | [Pay off] Take the money. (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "127415915065", "difficulty": "EASY"}}}} | 0:0 → 155:0:0; 0:0 → 246:0:0 |
| `mq022_01_diner.scene / n104 / 1` | You're on rival territory. (``) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83574632792"}}}} | 0:1 → 156:0:0; 0:1 → 246:0:0 |
| `mq022_01_diner.scene / n104 / 2` | You don't know who you're fucking with. (``) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "127415915065", "buildId": "75476658533", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 157:0:0; 0:2 → 246:0:0 |
| `mq022_01_diner.scene / n104 / 3` | You're sending mixed signals. (``) | No option-level predicate stored | 0:3 → 163:0:0 |
| `mq022_01_diner.scene / n132 / 0` | pl-pl[wyjmij broń] A teraz umrzecie. (``) | No option-level predicate stored | 0:0 → 776:0:1 |
| `mq022_01_diner.scene / n192 / 0` | [Lean] I'll take a Calavera Feliz. (``) | No option-level predicate stored | 0:0 → 197:0:0 |
| `mq022_01_diner.scene / n192 / 1` | [Lean] One Spunky Monkey, please. (``) | No option-level predicate stored | 0:1 → 208:0:0 |
| `mq022_01_diner.scene / n192 / 2` | [Lean] Get me a Tiancha. (``) | No option-level predicate stored | 0:2 → 210:0:0 |
| `mq022_01_diner.scene / n214 / 0` | Robbing a diner? That's sad. (``) | No option-level predicate stored | 0:0 → 215:0:0; 0:0 → 522:0:0 |
| `mq022_01_diner.scene / n214 / 1` | Leave them alone! (``) | No option-level predicate stored | 0:1 → 216:0:0; 0:1 → 522:0:1 |
| `mq022_01_diner.scene / n571 / 0` | [Step away] (``) | No option-level predicate stored | 0:0 → 575:0:0 |
| `mq022_01_diner.scene / n610 / 0` | Could use a drink. (``) | No option-level predicate stored | 0:0 → 637:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-12345` | mq022_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-601738` | mq022_quest_bugfixes.questphase / h30 / 2 | mq022_quest_bugfixes.questphase / h30 / 8 |
| `CYB-623804` | mq022_quest_bugfixes.questphase / h111 / 3 | mq022_quest_bugfixes.questphase / h111 / 2 |
| `mq022_active` | mq022_beginning.questphase / h0 / 32 | No reader in selected context |
| `mq022_combat` | mq022_01_diner.scene / scene / 776; mq022_01_diner.scene / scene / 846 | mq022_01_diner.scene / scene / 775; mq022_01_diner.scene / scene / 849; mq022_beginning.questphase / h0 / 61 |
| `mq022_done` | Producer outside selected context | mq022_quest_bugfixes.questphase / h30 / 9 |
| `mq022_no_choice_done` | mq022_01_diner.scene / scene / 562; mq022_01_diner.scene / scene / 824; mq022_beginning.questphase / h202 / 11 | mq022_01_diner.scene / scene / 566; mq022_01_diner.scene / scene / 775 |
| `std_arr_foodshop_04_default_on` | mq022_01_diner.scene / scene / 838; mq022_beginning.questphase / h0 / 58 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | mq022_quest_bugfixes.questphase / h0 / 15 |

## Exact gates, joins and cancellation

<details><summary>26 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq022_quest_bugfixes.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 16:Out → 15:In |
| `mq022_quest_bugfixes.questphase / h30 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-601738"}}}` | 0:Out → 8:In; 8:False → 2:In |
| `mq022_quest_bugfixes.questphase / h30 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_done"}}}` | 2:Out → 9:In; 9:Out → 10:In |
| `mq022_quest_bugfixes.questphase / h30 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mq022_description","fileEntryIndex":2,"className":"gameJournalQuestDescription"},"state":"Active"}}}` | 10:True → 1:In; 9:Out → 10:In; 10:False → 11:Active |
| `mq022_quest_bugfixes.questphase / h111 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-623804"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq022_quest_bugfixes.questphase / h111 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 3:Out → 4:In; 4:True → 6:In |
| `mq022_beginning.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq022_tr_ezekiel_starts"}}` | 38:Out → 2:In; 2:Out → 48:In; 2:Out → 75:In; 2:Out → 76:In; 2:Out → 77:In |
| `mq022_beginning.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3:Out → 6:In; 6:Out → 38:In; 6:Out → 72:In; 6:Out → 73:In; 6:Out → 74:In |
| `mq022_beginning.questphase / h0 / 42` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"},"unconscious":false,"defeated":false}}}` | 61:True → 42:In; 42:True → 43:mq022_people_dead; 42:False → 43:mq022_people_alive |
| `mq022_beginning.questphase / h0 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 47:Out → 40:Succeeded; 50:Out → 47:In |
| `mq022_beginning.questphase / h0 / 61` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_combat"}}}` | 61:True → 42:In; 61:False → 43:mq022_people_alive; 45:Out → 61:In |
| `mq022_beginning.questphase / h0 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_diner"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 70:Out → 3:In; 69:Out → 70:In |
| `mq022_beginning.questphase / h202 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2:Out → 3:In; 3:Out → 8:In; 3:Out → 14:In |
| `mq022_beginning.questphase / h202 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers","names":["ganger_01"]},"isPlayer":false}}}` | 3:Out → 8:In; 8:Out → 11:In |
| `mq022_beginning.questphase / h202 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 13:Out → 6:In; 14:Out → 13:In |
| `mq022_combat.questphase / h0 / 8` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 2:Out → 8:In1; 4:Out → 8:In2; 6:Out → 8:In3; 8:Out1 → 11:In; 8:Out1 → 10:In; 8:Out1 → 9:In |
| `mq022_combat.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers","names":["ganger_01"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 30:Out → 15:In; 15:Out → 18:In1 |
| `mq022_combat.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers","names":["ganger_02"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 31:Out → 16:In; 16:Out → 18:In2 |
| `mq022_combat.questphase / h0 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers","names":["ganger_03"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 32:Out → 17:In; 17:Out → 18:In3 |
| `mq022_combat.questphase / h0 / 18` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 18:Out1 → 1:In; 15:Out → 18:In1; 16:Out → 18:In2; 17:Out → 18:In3 |
| `mq022_01_diner.scene / scene / 566` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_no_choice_done"}}}` | 140:0:0 → 566:0:1; 566:0:0 → 139:0:0; 566:0:1 → 119:0:0 |
| `mq022_01_diner.scene / scene / 775` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_no_choice_done"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_combat"}}]}}` | 291:2:3 → 775:0:1; 775:0:0 → 779:0:0 |
| `mq022_01_diner.scene / scene / 831` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#std_arr_foodshop_04","names":["barman"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"Less"}}}` | 602:0:0 → 831:0:1; 831:0:0 → 610:0:0; 831:0:0 → 830:0:0 |
| `mq022_01_diner.scene / scene / 849` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_combat"}}}` | 171:0:0 → 849:0:1; 849:0:0 → 575:0:0; 849:0:1 → 571:0:0 |
| `mq022_01_diner.scene / scene / 935` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 163:0:0 → 935:0:1; 935:0:0 → 104:1:0; 935:0:0 → 246:0:0; 935:0:0 → 562:0:1; 940:1:0 → 935:0:0 |
| `mq022_01_diner.scene / scene / 956` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 93:0:0 → 956:0:1; 956:0:0 → 52:1:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq022_beginning.questphase / h0 / 6; mq022_beginning.questphase / h0 / 70; mq022_beginning.questphase / h202 / 3 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq022_01_diner.scene / scene / 441; mq022_01_diner.scene / scene / 442; mq022_01_diner.scene / scene / 443; mq022_01_diner.scene / scene / 804; +2 locations in catalogue.json | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | mq022_beginning.questphase / h0 / 44; mq022_beginning.questphase / h0 / 48; mq022_beginning.questphase / h0 / 53 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq022_01_diner.scene / scene / 104; mq022_01_diner.scene / scene / 132; mq022_01_diner.scene / scene / 192; mq022_01_diner.scene / scene / 214; +3 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq022_combat.questphase / h0 / 10; mq022_combat.questphase / h0 / 11; mq022_combat.questphase / h0 / 27; mq022_combat.questphase / h0 / 28; +2 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq022_01_diner.scene / scene / 412; mq022_01_diner.scene / scene / 413; mq022_01_diner.scene / scene / 414; mq022_01_diner.scene / scene / 444; +8 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq022_01_diner.scene / scene / 566; mq022_01_diner.scene / scene / 775; mq022_01_diner.scene / scene / 849; mq022_beginning.questphase / h0 / 61; +4 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | mq022_01_diner.scene / scene / 931; mq022_beginning.questphase / h202 / 6; mq022_combat.questphase / h0 / 30; mq022_combat.questphase / h0 / 31; +1 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `journal_transition` | mq022_01_diner.scene / scene / 152; mq022_01_diner.scene / scene / 267; mq022_01_diner.scene / scene / 466; mq022_01_diner.scene / scene / 839; +7 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | mq022_combat.questphase / h0 / 18; mq022_combat.questphase / h0 / 8 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq022_01_diner.scene / scene / 562; mq022_01_diner.scene / scene / 776; mq022_01_diner.scene / scene / 824; mq022_01_diner.scene / scene / 838; +7 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | mq022_01_diner.scene / scene / 935; mq022_01_diner.scene / scene / 956; mq022_beginning.questphase / h0 / 47 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | mq022_01_diner.scene / scene / 185 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq022_beginning.questphase / h0 / 11; mq022_beginning.questphase / h0 / 43; mq022_beginning.questphase / h202 / 10; mq022_combat.questphase / h0 / 14 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq022_beginning.questphase / h0 / 2 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | mq022_beginning.questphase / h0 / 42; mq022_beginning.questphase / h202 / 13; mq022_combat.questphase / h0 / 15; mq022_combat.questphase / h0 / 16; +1 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | mq022_01_diner.scene / scene / 308; mq022_01_diner.scene / scene / 314; mq022_01_diner.scene / scene / 318; mq022_01_diner.scene / scene / 320; +43 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq022_01_diner.scene / scene / 882; mq022_01_diner.scene / scene / 885; mq022_beginning.questphase / h202 / 2; mq022_beginning.questphase / h202 / 7 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` | repair; journal anchor | `base-mq022` |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` | content candidate; journal anchor | `base-mq022` |
| `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` | content candidate; journal anchor | `base-mq022` |
| `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` | content candidate; journal anchor | `base-mq022` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

125 repeated typed/socket path signatures in this selected graph context; 50 distinct direct resource identities; 4 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `eaf5aab427d50e5598b6` | `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` / h30 / 0 -> 8 -> 2 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `cbae0fd3078e68426197` | `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` / h0 / 14 -> 16 -> 15 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `19665e3783f6f51a7337` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 178 -> 171 -> 420 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `95d4997362b664c5c23b` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 190 -> 192 -> 197 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |
| `02ad6c50ebc6c8472fdf` | `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` / h30 / 8 -> 2 -> 9 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; False -> In; Out -> In |
| `276aca4a2dc348a877d5` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 100 -> 105 -> 946 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `016828d499c85128303c` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 171 -> 849 -> 575 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `c11cf4b8fc2f0bbc6f96` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 779 -> 790 -> 767 | scnCutControlNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId]; 1:0 -> 1:0; 0:0 -> 0:0 |
| `a737198437424e66c57c` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 527 -> 246 -> 250 | scnHubNode[scnNodeId] -> scnHubNode[scnNodeId] -> scnHubNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `09ab8874517e792939a0` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 152 -> 267 -> 52 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `6301eecf83656b7e9f6a` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 935 -> 246 -> 250 | questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> scnHubNode[scnNodeId] -> scnHubNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `39515e8ce0f193571bb7` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 849 -> 575 -> 576 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]; 0:0 -> 0:0; 4:0 -> 0:1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` / h0 / 13 | `h30` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` / h0 / 17 | `h111` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h0 / 57 | `h202` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_kabuki.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_kabuki.quest |
| `base\quest\demos\handson_2020\handson_2020_little_china.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_little_china.quest |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_speed_test.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_speed_test.quest |
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
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\corpo_male\interactive_scene\corpo_male__stand__rh_gun.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male__stand__rh_gun_aim__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_stand_bar_lean0__2h_on_bar__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_barstool__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_barstool_bar_lean0__2h_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair__2h_up__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_table_lean0__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_up__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_bar_lean0__2h_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_wall_lean180__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\female\body\player_locomotion_johnny_guitar.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__sit_barstool_bar_lean270__lh_on_bar.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__sit_barstool_bar_lean270__lh_on_bar.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\male\body\player_locomotion_sick.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q000\q000_kid_02a_confront_jackie\anim\body\q000_kid_02a_confront_jackie__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q003\q003_01a_militech\anim\body\q003_01a_militech__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q003\q003_01a_militech\anim\body\q003_01a_militech__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq017\sq017_04_highway_kerry_approach_truck\body\sq017_04_highway_kerry_approach_truck__male_average_kerry.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq022\scenes\lipsync\en\mq022_01_diner\civ_depr_m_03_jap_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq022\scenes\lipsync\en\mq022_01_diner\civ_low_m_101_nat_20.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq022\scenes\lipsync\en\mq022_01_diner\civ_low_m_10_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq022\scenes\lipsync\en\mq022_01_diner\civ_low_m_46_afam_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq022\scenes\lipsync\en\mq022_01_diner\civ_low_m_66_mex_40_mt.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq022\scenes\lipsync\en\mq022_01_diner\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\bar\bar_and_barstool\generic__sit_barstool__look__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair__scared__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair_table\generic__sit_chair_table_lean_front_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__scared__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__wait__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_gun__aim__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\jackie\jackie__sit_barstool_bar_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\bar\player__sit_barstool_bar_lean_left__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\player\bar\player__sit_barstool_bar_lean_left__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\bar\player__stand_bar_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\bar\player__stand_bar_lean_front__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\prologue\q000\q000_kid_02a_confront_jackie\q000__corpo__stand_ground_gun__aim__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `mq022_active` | base\quest\minor_quests\mq022\mq022.questphase / h0 / 89; 1 total source locations in compressed evidence |
| `mq022_done` | base\quest\minor_quests\mq022\mq022.questphase / h0 / 90; 1 total source locations in compressed evidence |

NodeRef uses: 163; TweakDB binding uses: 35. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` | 27 / 350 | scnChangeIdleAnimEvent: 33; scnDialogLineEvent: 44; scnGameplayTransitionEvent: 18; scnIKEvent: 36; scnLookAtEvent: 40; scnPlaySkAnimEvent: 57; scnPoseCorrectionEvent: 1; scnUnmountEvent: 18; scneventsPlayerLookAtEvent: 1; scneventsSetAnimFeatureEvent: 18; scneventsSocket: 83; scneventsVFXDurationEvent: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
