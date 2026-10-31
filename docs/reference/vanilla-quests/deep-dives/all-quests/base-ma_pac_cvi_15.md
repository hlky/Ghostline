# Cyberpsycho Sighting: Lex Talionis

Journal: `quests/minor_quest/ma_pac_cvi_15` · `CyberPsycho` · hash `355911891`.

Journal premise: The underpass near GIM is like NC's Bermuda Triangle for the homeless. Sound like a piece of cake? In the heart of Pacifica, nothing ever is.\n\nEnter at your own risk.

**Coverage: journal-linked.** 17 exact journal-linked nodes in 2 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Read Regina's message in the cyberpsycho message thread. (Primary) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/check_message` |
| Search the computer for more info. (Primary) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/check_shard` |
| Search the area to collect information. (Primary) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/clues` |
| Find the cyberpsycho. (Primary) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/find_psycho` |
| Neutralize the threat. (Primary) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/kill_psycho` |
| Message Regina about Cyberpsycho Sighting: Lex Talionis (Primary) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `ma_pac_cvi_15_bugfixing.questphase / h9 / 8` (Condition) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info`; `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info` | 2:Out → 8:In; 8:True → 11:Inactive |
| `ma_pac_cvi_15_bugfixing.questphase / h169 / 3` (Condition: IsLocked) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/find_psycho` | 2:Out → 3:In; 3:True → 5:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 5` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/find_psycho` | 90:Out → 5:Succeeded; 5:Out → 6:Active |
| `ma_pac_cvi_15_phase.questphase / h0 / 6` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/kill_psycho` | 5:Out → 6:Active; 6:Out → 7:In; 6:Out → 41:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 8` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/kill_psycho` | 42:Out1 → 8:Succeeded; 8:Out → 141:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 10` (Journal) | `quests/minor_quest/ma_pac_cvi_15` | 23:Out → 10:Succeeded; 10:Out → 13:In; 10:Out → 16:In1 |
| `ma_pac_cvi_15_phase.questphase / h0 / 22` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info` | 37:Out → 22:Active; 34:True → 22:Active; 22:Out → 120:In; 22:Out → 142:Active |
| `ma_pac_cvi_15_phase.questphase / h0 / 23` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info` | 23:Out → 10:Succeeded; 25:Out → 23:Succeeded |
| `ma_pac_cvi_15_phase.questphase / h0 / 31` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/clues` | 103:False → 31:Active; 31:Out → 106:In; 31:Out → 109:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 33` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/clues` | 110:Out1 → 33:Succeeded; 33:Out → 34:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 35` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/check_shard` | 34:False → 35:Active; 35:Out → 105:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 37` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/check_shard` | 37:Out → 22:Active; 105:Out → 37:Succeeded |
| `ma_pac_cvi_15_phase.questphase / h0 / 61` (Journal) | `quests/minor_quest/ma_pac_cvi_15/description` | 63:Out → 61:Active; 61:Out → 131:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 63` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/find_psycho` | 63:Out → 61:Active; 62:Out → 63:Active |
| `ma_pac_cvi_15_phase.questphase / h0 / 142` (Journal) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info` | 22:Out → 142:Active |
| `ma_pac_cvi_15_phase.questphase / h0 / 158` (Condition: holo_setup_active; holo_setup_started) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/find_psycho` | 158:False → 2:ma_pac_cvi_15_brief_in; 158:True → 144:In1; 163:Out → 158:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 159` (Condition) | `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info`; `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info` | 144:Out1 → 159:In; 159:False → 145:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `ma_pac_cvi_15_phase.questphase / h0 / 2` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene`; `#ma_sm_pac_cvi_15_brief` | 158:False → 2:ma_pac_cvi_15_brief_in; 2:ma_pac_cvi_15_brief_out → 162:In; 2:rejected_out → 145:Active; 2:Holocall INT → 137:In; 2:Holocall RET → 136:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\bugfixing\ma\ma_coast_view_bugfixing.questphase` / h0 / 10 | `ma_pac_cvi_15_bugfixing.questphase` | 12: DeletionMarker; 12:Out → 10:In1 |
| `base\open_world\minor_activities\pacifica\coastview\coastview_minor_activities.questphase` / h0 / 35 | `ma_pac_cvi_15_phase.questphase` | 60: Journal; 60:Out → 35:In1 |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 2 | `ma_pac_cvi_15_brief.scene` | 158: Condition: holo_setup_active; holo_setup_started; 158:False → 2:ma_pac_cvi_15_brief_in; 2:ma_pac_cvi_15_brief_out → 162:In; 2:rejected_out → 145:Active; 2:Holocall INT → 137:In; 2:Holocall RET → 136:In |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h3390 / 18 | `ma_coast_view_bugfixing.questphase` | 22: DeletionMarker; 22:Out → 18:In1 |
| `base\open_world\community\pacifica\coastview\pac_civ_quest.quest` / h0 / 6 | `coastview_minor_activities.questphase` | 1: Start; 1:Out → 6:In1 |
| `base\open_world\minor_activities\open_world_minor_activities.questphase` / h0 / 7 | `coastview_minor_activities.questphase` | 37: LogicalHub; 37:Out1 → 7:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\community\badlands\inland_avenue\bad_ina_quest.quest` / h0 / 9 | `open_world_minor_activities.questphase` |  |
| `base\open_world\phases\open_world_content.questphase` / h0 / 11 | `open_world_minor_activities.questphase` | 0: Input; 122: Input; 0:Out → 11:In1; 122:Out → 11:In1 |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 6 | `open_world_minor_activities.questphase` | 0: Start; 0:Out → 6:In1 |
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
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
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

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `ma_pac_cvi_15_brief.scene` | ma_pac_cvi_15_brief_in → ma_pac_cvi_15_brief_out, rejected_out | Regina; V; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-603473` | ma_pac_cvi_15_bugfixing.questphase / h9 / 2 | ma_pac_cvi_15_bugfixing.questphase / h9 / 10 |
| `CYB-609775` | ma_pac_cvi_15_bugfixing.questphase / h62 / 2 | ma_pac_cvi_15_bugfixing.questphase / h62 / 10 |
| `CYB-663511` | ma_pac_cvi_15_bugfixing.questphase / h169 / 2 | ma_pac_cvi_15_bugfixing.questphase / h169 / 4 |
| `glossary_cyberpsychosis` | ma_pac_cvi_15_phase.questphase / h0 / 56 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | ma_pac_cvi_15_brief.scene / scene / 422 |
| `holo_reggie_calls_v_end_activate` | ma_pac_cvi_15_brief.scene / scene / 381; ma_pac_cvi_15_phase.questphase / h0 / 137 | No reader in selected context |
| `holo_reggie_calls_v_end_done` | ma_pac_cvi_15_brief.scene / scene / 377 | ma_pac_cvi_15_brief.scene / scene / 376 |
| `holo_reggie_calls_v_rejectable` | ma_pac_cvi_15_brief.scene / scene / 395; ma_pac_cvi_15_brief.scene / scene / 420 | No reader in selected context |
| `holo_reggie_calls_v_rejected` | ma_pac_cvi_15_brief.scene / scene / 403 | ma_pac_cvi_15_brief.scene / scene / 401 |
| `holo_reggie_calls_v_start_activate` | ma_pac_cvi_15_brief.scene / scene / 380; ma_pac_cvi_15_brief.scene / scene / 418; ma_pac_cvi_15_phase.questphase / h0 / 136 | No reader in selected context |
| `holo_reggie_calls_v_start_done` | ma_pac_cvi_15_brief.scene / scene / 375 | ma_pac_cvi_15_brief.scene / scene / 410 |
| `holo_setup_active` | Producer outside selected context | ma_pac_cvi_15_brief.scene / scene / 422; ma_pac_cvi_15_phase.questphase / h0 / 158 |
| `holo_setup_started` | Producer outside selected context | ma_pac_cvi_15_brief.scene / scene / 422; ma_pac_cvi_15_phase.questphase / h0 / 158 |
| `ma_hunt_for_psycho_tutorial` | ma_pac_cvi_15_phase.questphase / h0 / 55 | No reader in selected context |
| `ma_pac_cvi_15_alerted` | ma_pac_cvi_15_phase.questphase / h543 / 149 | ma_pac_cvi_15_phase.questphase / h1352 / 11 |
| `ma_pac_cvi_15_combat_start` | ma_pac_cvi_15_phase.questphase / h543 / 157 | ma_pac_cvi_15_phase.questphase / h1536 / 9 |
| `ma_pac_cvi_15_email_read` | Producer outside selected context | ma_pac_cvi_15_phase.questphase / h0 / 103; ma_pac_cvi_15_phase.questphase / h0 / 105; ma_pac_cvi_15_phase.questphase / h0 / 34 |
| `ma_pac_cvi_15_fight_start` | ma_pac_cvi_15_phase.questphase / h543 / 23 | ma_pac_cvi_15_phase.questphase / h0 / 90 |
| `ma_pac_cvi_15_finished` | ma_pac_cvi_15_phase.questphase / h0 / 15 | ma_pac_cvi_15_phase.questphase / h1474 / 10 |
| `ma_pac_cvi_15_start` | ma_pac_cvi_15_phase.questphase / h0 / 57 | ma_pac_cvi_15_bugfixing.questphase / h125 / 2; ma_pac_cvi_15_bugfixing.questphase / h62 / 17; ma_pac_cvi_15_bugfixing.questphase / h62 / 8 |
| `ma_token` | ma_pac_cvi_15_phase.questphase / h0 / 13 | No reader in selected context |
| `ow_psychos_done` | ma_pac_cvi_15_phase.questphase / h0 / 139 | No reader in selected context |
| `ow_psychos_killed` | ma_pac_cvi_15_phase.questphase / h0 / 40 | No reader in selected context |
| `sts_pac_cvi_tier_1` | Producer outside selected context | ma_pac_cvi_15_bugfixing.questphase / h62 / 13 |
| `travelling_merchant_lives` | Producer outside selected context | ma_pac_cvi_15_bugfixing.questphase / h0 / 10 |

## Exact gates, joins and cancellation

<details><summary>118 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `ma_pac_cvi_15_bugfixing.questphase / h0 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 11:Out → 10:In |
| `ma_pac_cvi_15_bugfixing.questphase / h9 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 2:Out → 8:In; 8:True → 11:Inactive |
| `ma_pac_cvi_15_bugfixing.questphase / h9 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-603473"}}}` | 0:Out → 10:In; 10:False → 2:In |
| `ma_pac_cvi_15_bugfixing.questphase / h62 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_start","value":1,"comparisonType":"Equal"}}}` | 13:Out → 8:In; 8:True → 18:In; 8:False → 14:In |
| `ma_pac_cvi_15_bugfixing.questphase / h62 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-609775"}}}` | 0:Out → 10:In; 10:False → 2:In |
| `ma_pac_cvi_15_bugfixing.questphase / h62 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_pac_cvi_tier_1"}}}` | 2:Out → 13:In; 13:Out → 8:In |
| `ma_pac_cvi_15_bugfixing.questphase / h62 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_start","value":1,"comparisonType":"Equal"}}}` | 14:Out → 17:In; 17:Out → 15:In |
| `ma_pac_cvi_15_bugfixing.questphase / h125 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_start"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `ma_pac_cvi_15_bugfixing.questphase / h169 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_dvc_garage_door","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsLocked"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/find_psycho","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}]}}` | 2:Out → 3:In; 3:True → 5:In |
| `ma_pac_cvi_15_bugfixing.questphase / h169 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-663511"}}}` | 0:Out → 4:In; 4:False → 2:In |
| `ma_pac_cvi_15_bugfixing.questphase / h169 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_pac_cvi_15_tr_lock_door"}}` | 5:Out → 6:In; 6:Out → 8:In |
| `ma_pac_cvi_15_bugfixing.questphase / h169 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"killed":false}}}` | 7:Out → 9:In; 9:Out → 12:In1 |
| `ma_pac_cvi_15_bugfixing.questphase / h169 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 7:Out → 11:In; 11:Out → 12:In2 |
| `ma_pac_cvi_15_bugfixing.questphase / h169 / 12` | `questLogicalXorNodeDefinition` `{}` | 9:Out → 12:In1; 11:Out → 12:In2; 12:Out1 → 13:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"killed":false}}}` | 6:Out → 7:In; 7:Out → 42:In1 |
| `ma_pac_cvi_15_phase.questphase / h0 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"93268646650","value":false}},{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"85882596286","value":false}},{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"87833202724","value":false}}]}}` | 118:Out1 → 24:In; 24:Out → 25:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 25:Out → 23:Succeeded; 24:Out → 25:In; 25:Out → 165:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 34` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_email_read","value":1,"comparisonType":"GreaterOrEqual"}}}` | 34:True → 22:Active; 33:Out → 34:In; 103:True → 34:In; 34:False → 35:Active |
| `ma_pac_cvi_15_phase.questphase / h0 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 6:Out → 41:In; 41:Out → 40:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 42` | `questLogicalXorNodeDefinition` `{}` | 7:Out → 42:In1; 42:Out1 → 8:Succeeded; 42:Out1 → 11:In; 40:Out → 42:In2; 42:Out1 → 130:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 53:Out1 → 54:In; 54:Out → 55:In; 54:Out → 91:In1; 54:Out → 138:In1; 54:Out → 163:In; 54:Out → 164:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_fight_start","value":1,"comparisonType":"Equal"}}}` | 90:Out → 5:Succeeded; 60:Out → 90:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 101` | `questLogicalAndNodeDefinition` `{}` | 101:Out1 → 1:In; 16:Out1 → 101:In1; 17:Out → 101:In2 |
| `ma_pac_cvi_15_phase.questphase / h0 / 103` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_dvc_laptop","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"IsControlledByThePlayer"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_email_read","value":1,"comparisonType":"GreaterOrEqual"}}]}}` | 103:False → 31:Active; 103:True → 34:In; 141:Out → 103:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 105` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_email_read","value":1,"comparisonType":"GreaterOrEqual"}}}` | 35:Out → 105:In; 105:Out → 37:Succeeded |
| `ma_pac_cvi_15_phase.questphase / h0 / 109` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_dvc_laptop"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_dvc_laptop"},"timeInterval":0.5,"onScreenTest":true}}]}}` | 31:Out → 109:In; 109:Out → 110:In2 |
| `ma_pac_cvi_15_phase.questphase / h0 / 106` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_dvc_laptop"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":2.0},"comparisonType":"LessOrEqual"}}}` | 31:Out → 106:In; 106:Out → 110:In1 |
| `ma_pac_cvi_15_phase.questphase / h0 / 110` | `questLogicalXorNodeDefinition` `{}` | 110:Out1 → 33:Succeeded; 109:Out → 110:In2; 106:Out → 110:In1 |
| `ma_pac_cvi_15_phase.questphase / h0 / 116` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_pac_cvi_15/01_ch_info/01_ch_info","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 114:Out → 116:In; 116:Out → 115:Active; 123:CutSource → 116:CutDestination |
| `ma_pac_cvi_15_phase.questphase / h0 / 117` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_pac_cvi_15/01_ch_info_lethal/01_ch_info_lethal","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 121:Out → 117:In; 117:Out → 119:Active |
| `ma_pac_cvi_15_phase.questphase / h0 / 118` | `questLogicalXorNodeDefinition` `{}` | 118:Out1 → 24:In; 115:Out → 118:In2; 119:Out → 118:In1 |
| `ma_pac_cvi_15_phase.questphase / h0 / 120` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 22:Out → 120:In; 120:False → 114:Active; 120:True → 121:Active |
| `ma_pac_cvi_15_phase.questphase / h0 / 122` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 114:Out → 122:In; 123:CutSource → 122:CutDestination; 125:CutSource → 122:CutDestination; 122:Out → 123:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 123` | `questCutControlNodeDefinition` `{}` | 123:CutSource → 114:CutDestination; 123:CutSource → 116:CutDestination; 123:CutSource → 122:CutDestination; 122:Out → 123:In; 123:Out → 124:Inactive; 123:Out → 126:In1 |
| `ma_pac_cvi_15_phase.questphase / h0 / 125` | `questCutControlNodeDefinition` `{"permanent":true}` | 125:CutSource → 114:CutDestination; 115:Out → 125:In; 119:Out → 125:In; 125:CutSource → 121:CutDestination; 125:CutSource → 122:CutDestination |
| `ma_pac_cvi_15_phase.questphase / h0 / 131` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_pac_cvi_15_tr_lock_door"}}` | 61:Out → 131:In; 131:Out → 134:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 158` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started"}},{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","anyParent":true,"childIsPlayer":true}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType","isContentBlocked":true}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/find_psycho","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 158:False → 2:ma_pac_cvi_15_brief_in; 158:True → 144:In1; 163:Out → 158:In |
| `ma_pac_cvi_15_phase.questphase / h0 / 159` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}]}}` | 144:Out1 → 159:In; 159:False → 145:Active |
| `ma_pac_cvi_15_phase.questphase / h0 / 162` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 2:ma_pac_cvi_15_brief_out → 162:In; 162:Out → 161:In |
| `ma_pac_cvi_15_phase.questphase / h131 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":2}}}` | 15:Out → 5:In; 5:Out → 26:In |
| `ma_pac_cvi_15_phase.questphase / h131 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":6}}}` | 0:Out → 9:In; 9:Out → 23:In |
| `ma_pac_cvi_15_phase.questphase / h131 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#ma_pac_cvi_15_tr_start"},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_after_com","names":["hobo_01"]},"onScreenTest":true}}]}}` | 4:Out → 15:In; 15:Out → 5:In |
| `ma_pac_cvi_15_phase.questphase / h131 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 9:Out → 23:In; 23:Out → 28:In |
| `ma_pac_cvi_15_phase.questphase / h131 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 5:Out → 26:In; 26:Out → 27:In |
| `ma_pac_cvi_15_phase.questphase / h345 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["droid_02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 26:Out → 3:In; 3:Out → 22:In1; 3:Out → 31:In |
| `ma_pac_cvi_15_phase.questphase / h345 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 25:Out → 1:In; 31:Out → 25:In |
| `ma_pac_cvi_15_phase.questphase / h345 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["droid_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 26:Out → 3:In; 32:Out → 26:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"isPlayer":false,"percent":50.0,"comparisonType":"LessOrEqual"}}}` | 112:Out → 32:In; 32:Out → 33:In; 32:Out → 57:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"isPlayer":false,"percent":20.0,"comparisonType":"LessOrEqual"}}}` | 32:Out → 57:In; 57:Out → 56:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 65:Out → 34:In; 112:Out → 65:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 74:Out → 50:In; 72:Out → 74:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 76` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_01","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsDisabled"}}}` | 177:Out1 → 76:In; 76:Out → 161:In1 |
| `ma_pac_cvi_15_phase.questphase / h543 / 104` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["goon_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 110:Out5 → 104:In; 104:Out → 202:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 106` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["goon_02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 110:Out6 → 106:In; 106:Out → 203:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 112` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"isPlayer":false,"percent":80.0,"comparisonType":"LessOrEqual"}}}` | 112:Out → 32:In; 112:Out → 65:In; 197:Out → 112:In; 112:Out → 131:In; 112:Out → 143:In2; 112:Out → 142:In2; 112:Out → 157:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 136` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["droid_01"]}}}}` | 0:Out → 136:In; 136:Out → 143:In1 |
| `ma_pac_cvi_15_phase.questphase / h543 / 137` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["droid_02"]}}}}` | 0:Out → 137:In; 137:Out → 142:In1 |
| `ma_pac_cvi_15_phase.questphase / h543 / 141` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 141:Out → 138:In; 140:Out → 141:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 142` | `questLogicalXorNodeDefinition` `{}` | 142:Out1 → 72:In; 112:Out → 142:In2; 137:Out → 142:In1 |
| `ma_pac_cvi_15_phase.questphase / h543 / 143` | `questLogicalXorNodeDefinition` `{}` | 112:Out → 143:In2; 136:Out → 143:In1; 143:Out1 → 140:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 155` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 155:Out1 → 149:In; 187:Out → 155:In1; 188:Out → 155:In2; 189:Out → 155:In3; 190:Out → 155:In4 |
| `ma_pac_cvi_15_phase.questphase / h543 / 158` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_01","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"WasQuickHacked"}}}` | 177:Out2 → 158:In; 158:Out → 161:In2 |
| `ma_pac_cvi_15_phase.questphase / h543 / 159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_01","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"HackingPerformed"}}}` | 177:Out3 → 159:In; 159:Out → 161:In3 |
| `ma_pac_cvi_15_phase.questphase / h543 / 161` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 76:Out → 161:In1; 158:Out → 161:In2; 159:Out → 161:In3; 161:Out1 → 198:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 162` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_02","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsDisabled"}}}` | 178:Out1 → 162:In; 162:Out → 166:In1 |
| `ma_pac_cvi_15_phase.questphase / h543 / 164` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_02","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"WasQuickHacked"}}}` | 178:Out2 → 164:In; 164:Out → 166:In2 |
| `ma_pac_cvi_15_phase.questphase / h543 / 165` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_02","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"HackingPerformed"}}}` | 178:Out3 → 165:In; 165:Out → 166:In3 |
| `ma_pac_cvi_15_phase.questphase / h543 / 166` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 162:Out → 166:In1; 164:Out → 166:In2; 165:Out → 166:In3; 166:Out1 → 199:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 167` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_03","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsDisabled"}}}` | 179:Out1 → 167:In; 167:Out → 171:In1 |
| `ma_pac_cvi_15_phase.questphase / h543 / 169` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_03","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"WasQuickHacked"}}}` | 179:Out2 → 169:In; 169:Out → 171:In2 |
| `ma_pac_cvi_15_phase.questphase / h543 / 170` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_03","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"HackingPerformed"}}}` | 179:Out3 → 170:In; 170:Out → 171:In3 |
| `ma_pac_cvi_15_phase.questphase / h543 / 171` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 167:Out → 171:In1; 169:Out → 171:In2; 170:Out → 171:In3; 171:Out1 → 200:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 172` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_04","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"IsDisabled"}}}` | 180:Out1 → 172:In; 172:Out → 176:In1 |
| `ma_pac_cvi_15_phase.questphase / h543 / 174` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_04","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"WasQuickHacked"}}}` | 180:Out2 → 174:In; 174:Out → 176:In2 |
| `ma_pac_cvi_15_phase.questphase / h543 / 175` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_camera_04","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"HackingPerformed"}}}` | 180:Out3 → 175:In; 175:Out → 176:In3 |
| `ma_pac_cvi_15_phase.questphase / h543 / 176` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 172:Out → 176:In1; 174:Out → 176:In2; 175:Out → 176:In3; 176:Out1 → 201:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["goon_03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 110:Out7 → 107:In; 107:Out → 204:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 183` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"isPlayer":false,"inverted":true}}}` | 23:Out → 183:In; 183:Out → 147:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 187` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["droid_01"]}}}}` | 187:Out → 155:In1; 191:Out → 187:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 188` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["droid_02"]}}}}` | 188:Out → 155:In2; 191:Out → 188:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 189` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["goon_01"]}}}}` | 189:Out → 155:In3; 191:Out → 189:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 190` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["goon_02"]}}}}` | 190:Out → 155:In4; 191:Out → 190:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 196` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 196:Out → 194:In; 195:Out → 196:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 197` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 0:Out → 197:In; 197:Out → 112:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 198` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 198:Out → 99:In; 161:Out1 → 198:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 199` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 199:Out → 163:In; 166:Out1 → 199:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 200` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 200:Out → 168:In; 171:Out1 → 200:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 201` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 201:Out → 173:In; 176:Out1 → 201:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 202` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 104:Out → 202:In; 202:Out → 105:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 203` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 106:Out → 203:In; 203:Out → 108:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 204` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 204:Out → 109:In; 107:Out → 204:In |
| `ma_pac_cvi_15_phase.questphase / h543 / 207` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#ma_pac_cvi_15_tr_lock_door"},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_pac_cvi_15_dvc_garage_door","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}]}}` | 207:Out → 195:In; 208:Out → 207:In |
| `ma_pac_cvi_15_phase.questphase / h1352 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 7:Out → 3:In; 3:Out → 4:In |
| `ma_pac_cvi_15_phase.questphase / h1352 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:Out → 5:In; 5:Out → 6:In |
| `ma_pac_cvi_15_phase.questphase / h1352 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 5:Out → 6:In; 6:Out → 8:In |
| `ma_pac_cvi_15_phase.questphase / h1352 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 3:In; 8:Out → 7:In |
| `ma_pac_cvi_15_phase.questphase / h1352 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_alerted"}}}` | 0:Out → 11:In; 11:Out → 1:In |
| `ma_pac_cvi_15_phase.questphase / h1411 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 7:Out → 3:In; 3:Out → 4:In |
| `ma_pac_cvi_15_phase.questphase / h1411 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:Out → 5:In; 5:Out → 6:In |
| `ma_pac_cvi_15_phase.questphase / h1411 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 5:Out → 6:In; 6:Out → 8:In |
| `ma_pac_cvi_15_phase.questphase / h1411 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 3:In; 8:Out → 7:In |
| `ma_pac_cvi_15_phase.questphase / h1411 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_pac_cvi_15_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 14:In; 14:Out → 1:In |
| `ma_pac_cvi_15_phase.questphase / h1474 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 7:Out → 3:In; 3:Out → 4:In |
| `ma_pac_cvi_15_phase.questphase / h1474 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:Out → 5:In; 5:Out → 6:In |
| `ma_pac_cvi_15_phase.questphase / h1474 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 5:Out → 6:In; 6:Out → 8:In |
| `ma_pac_cvi_15_phase.questphase / h1474 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 3:In; 8:Out → 7:In |
| `ma_pac_cvi_15_phase.questphase / h1474 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_finished"}}}` | 0:Out → 10:In; 10:Out → 1:In |
| `ma_pac_cvi_15_phase.questphase / h1536 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 7:Out → 3:In; 3:Out → 4:In |
| `ma_pac_cvi_15_phase.questphase / h1536 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:Out → 5:In; 5:Out → 6:In |
| `ma_pac_cvi_15_phase.questphase / h1536 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_pac_cvi_15_tr_start"}}` | 5:Out → 6:In; 6:Out → 8:In |
| `ma_pac_cvi_15_phase.questphase / h1536 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 3:In; 8:Out → 7:In |
| `ma_pac_cvi_15_phase.questphase / h1536 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_pac_cvi_15_combat_start"}}}` | 0:Out → 9:In; 9:Out → 1:In |
| `ma_pac_cvi_15_brief.scene / scene / 376` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 376:0:0 → 377:0:1; 381:0:0 → 376:0:1 |
| `ma_pac_cvi_15_brief.scene / scene / 401` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 380:0:0 → 401:0:1; 401:0:0 → 403:0:1 |
| `ma_pac_cvi_15_brief.scene / scene / 410` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 374:666:0 → 410:0:1; 410:0:0 → 413:0:0 |
| `ma_pac_cvi_15_brief.scene / scene / 416` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 374:666:0 → 416:0:1; 413:1:0 → 416:0:0; 416:0:0 → 422:0:1 |
| `ma_pac_cvi_15_brief.scene / scene / 422` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 416:0:0 → 422:0:1; 422:0:0 → 420:0:1; 422:0:1 → 424:0:1; 424:0:0 → 422:0:1 |
| `ma_pac_cvi_15_brief.scene / scene / 424` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 413:1:0 → 424:0:0; 422:0:1 → 424:0:1; 424:0:0 → 422:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | ma_pac_cvi_15_phase.questphase / h345 / 26; ma_pac_cvi_15_phase.questphase / h345 / 3; ma_pac_cvi_15_phase.questphase / h543 / 196; ma_pac_cvi_15_phase.questphase / h543 / 197; +7 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | ma_pac_cvi_15_phase.questphase / h0 / 133; ma_pac_cvi_15_phase.questphase / h0 / 17; ma_pac_cvi_15_phase.questphase / h0 / 60 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `combat_control` | ma_pac_cvi_15_phase.questphase / h543 / 138; ma_pac_cvi_15_phase.questphase / h543 / 139; ma_pac_cvi_15_phase.questphase / h543 / 148; ma_pac_cvi_15_phase.questphase / h543 / 24; +2 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | ma_pac_cvi_15_bugfixing.questphase / h125 / 3; ma_pac_cvi_15_phase.questphase / h131 / 24; ma_pac_cvi_15_phase.questphase / h131 / 27; ma_pac_cvi_15_phase.questphase / h131 / 4; +3 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | ma_pac_cvi_15_brief.scene / scene / 376; ma_pac_cvi_15_brief.scene / scene / 401; ma_pac_cvi_15_brief.scene / scene / 410; ma_pac_cvi_15_brief.scene / scene / 422; +16 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | ma_pac_cvi_15_phase.questphase / h0 / 11; ma_pac_cvi_15_phase.questphase / h0 / 164; ma_pac_cvi_15_phase.questphase / h0 / 165; ma_pac_cvi_15_phase.questphase / h131 / 18; +2 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | ma_pac_cvi_15_bugfixing.questphase / h169 / 13; ma_pac_cvi_15_bugfixing.questphase / h169 / 5; ma_pac_cvi_15_bugfixing.questphase / h169 / 7; ma_pac_cvi_15_bugfixing.questphase / h169 / 8; +4 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | ma_pac_cvi_15_bugfixing.questphase / h169 / 3; ma_pac_cvi_15_phase.questphase / h0 / 103; ma_pac_cvi_15_phase.questphase / h543 / 158; ma_pac_cvi_15_phase.questphase / h543 / 159; +11 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | ma_pac_cvi_15_phase.questphase / h131 / 5; ma_pac_cvi_15_phase.questphase / h131 / 9 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | ma_pac_cvi_15_bugfixing.questphase / h9 / 11; ma_pac_cvi_15_phase.questphase / h0 / 10; ma_pac_cvi_15_phase.questphase / h0 / 114; ma_pac_cvi_15_phase.questphase / h0 / 115; +19 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | ma_pac_cvi_15_phase.questphase / h0 / 158 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | ma_pac_cvi_15_phase.questphase / h0 / 101 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | ma_pac_cvi_15_brief.scene / scene / 375; ma_pac_cvi_15_brief.scene / scene / 377; ma_pac_cvi_15_brief.scene / scene / 380; ma_pac_cvi_15_brief.scene / scene / 381; +19 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | ma_pac_cvi_15_bugfixing.questphase / h169 / 12; ma_pac_cvi_15_phase.questphase / h0 / 110; ma_pac_cvi_15_phase.questphase / h0 / 118; ma_pac_cvi_15_phase.questphase / h0 / 42; +7 locations in catalogue.json | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | ma_pac_cvi_15_brief.scene / scene / 416; ma_pac_cvi_15_brief.scene / scene / 424; ma_pac_cvi_15_phase.questphase / h0 / 162; ma_pac_cvi_15_phase.questphase / h0 / 25; +12 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | ma_pac_cvi_15_phase.questphase / h0 / 123; ma_pac_cvi_15_phase.questphase / h0 / 125 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | ma_pac_cvi_15_phase.questphase / h0 / 12 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | ma_pac_cvi_15_phase.questphase / h0 / 2 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | ma_pac_cvi_15_bugfixing.questphase / h169 / 6; ma_pac_cvi_15_phase.questphase / h0 / 131; ma_pac_cvi_15_phase.questphase / h0 / 54; ma_pac_cvi_15_phase.questphase / h131 / 15; +11 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | ma_pac_cvi_15_bugfixing.questphase / h169 / 11; ma_pac_cvi_15_bugfixing.questphase / h169 / 9; ma_pac_cvi_15_phase.questphase / h0 / 120; ma_pac_cvi_15_phase.questphase / h0 / 122; +6 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `world_variant` | ma_pac_cvi_15_phase.questphase / h131 / 21; ma_pac_cvi_15_phase.questphase / h131 / 22; ma_pac_cvi_15_phase.questphase / h345 / 14 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_bugfixing.questphase` | repair; journal anchor | `base-ma-pac-cvi-15` |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` | content candidate; journal anchor | `base-ma-pac-cvi-15` |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` | content candidate; forward dependency | `base-ma-pac-cvi-15` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

177 repeated typed/socket path signatures in this selected graph context; 3 distinct direct resource identities; 12 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 55 -> 56 -> 57 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` / scene / 381 -> 376 -> 377 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` / scene / 379 -> 381 -> 376 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` / scene / 376 -> 377 -> 2 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` / scene / 375 -> 378 -> 4 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` / scene / 4 -> 379 -> 381 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `a909c836470d2b0e7fbc` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1352 / 0 -> 11 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` / scene / 395 -> 380 -> 401 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `ea4cb15199b9b3fa8e63` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h131 / 0 -> 9 -> 23 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `2beeeaa3b4da5300c035` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` / scene / 1 -> 395 -> 380 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_bugfixing.questphase` / h9 / 0 -> 10 -> 2 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `bbf9efd740881cf31a37` | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` / scene / 410 -> 413 -> 416 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_bugfixing.questphase` / h0 / 2 | `h9` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_bugfixing.questphase` / h0 / 6 | `h62` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_bugfixing.questphase` / h0 / 7 | `h125` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_bugfixing.questphase` / h0 / 12 | `h169` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 16 | `h131` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 53 | `h345` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 91 | `h543` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 138 | `h1340` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1340 / 13 | `h1352` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1340 / 15 | `h1411` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1340 / 16 | `h1474` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1340 / 19 | `h1536` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\community\pacifica\coastview\pac_civ_def.gamedef` | content candidate | base\open_world\community\pacifica\coastview\pac_civ_quest.quest |
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
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\lipsync\en\ma_pac_cvi_15_brief\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\lipsync\en\ma_pac_cvi_15_brief\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `glossary_cyberpsychosis` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 134; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 77; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 38; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 35; 19 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 212; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 125; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 186; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 379; 196 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 211; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 121; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 375; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 305; 75 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejectable` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 249; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 266; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 395; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 412; 103 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejected` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 251; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 403; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 256; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 256; 64 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 124; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 264; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 185; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 378; 256 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 119; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 373; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 58; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 55; 70 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `ma_hunt_for_psycho_tutorial` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 133; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 44; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 37; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 39; 15 total source locations in compressed evidence |
| `ma_token` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_01\ma_bls_ina_se1_01_phase.questphase / h0 / 31; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_02\ma_bls_ina_se1_02_phase.questphase / h0 / 18; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase / h0 / 21; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase / h0 / 38; 340 total source locations in compressed evidence |
| `ow_psychos_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 110; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 188; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 176; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 111; 16 total source locations in compressed evidence |
| `ow_psychos_killed` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 166; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 217; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 130; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 279; 19 total source locations in compressed evidence |
| `sts_pac_cvi_tier_1` | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest / h0 / 7; base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest / h0 / 3; base\open_world\fixers\mr_hands\phases\mr_hands.questphase / h0 / 3; 3 total source locations in compressed evidence |

NodeRef uses: 142; TweakDB binding uses: 12. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` | 1 / 2 | scnDialogLineEvent: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
