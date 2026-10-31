# Cyberpsycho Sighting: Demons of War

Journal: `quests/minor_quest/ma_wat_kab_02` · `CyberPsycho` · hash `1198579324`.

Journal premise: Usually, when a corpo gets his walking papers, he loses all his implants too. They dig those synth organs and cyber eyes right out of his body. But sometimes, the chrome's so far ingrown, it can't be removed safely. Even if someone really, really wants it...

**Coverage: journal-linked.** 21 exact journal-linked nodes in 2 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Read Regina's message in the cyberpsycho message thread. (Primary) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/check_message` |
| Read the shard by the cyberpsycho's body. (Primary) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/check_shard` |
| Find the cyberpsycho. (Primary) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/find_psycho` |
| Investigate the area by the bridge. (Primary) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/investigate_bridge` |
| Neutralize the threat. (Primary) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/kill_psycho` |
| Search the area to collect information. (Primary) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/search_clues` |
| Send the information to Regina. (Primary) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `ma_wat_kab_02_phase.questphase / h0 / 8` (Journal) | `quests/minor_quest/ma_wat_kab_02` | 290:CutSource → 8:CutDestination; 71:Out → 8:Active; 8:Out → 9:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 9` (Journal) | `quests/minor_quest/ma_wat_kab_02/description` | 8:Out → 9:Active; 290:CutSource → 9:CutDestination; 9:Out → 138:Inactive; 9:Out → 277:In; 9:Out → 283:In1 |
| `ma_wat_kab_02_phase.questphase / h0 / 16` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/kill_psycho` | 64:Out → 16:Active; 16:Out → 17:In; 16:Out → 265:In |
| `ma_wat_kab_02_phase.questphase / h0 / 18` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/kill_psycho` | 39:Out → 18:Succeeded; 18:Out → 279:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 19` (Journal) | `quests/minor_quest/ma_wat_kab_02` | 107:Out → 19:Succeeded; 19:Out → 29:In |
| `ma_wat_kab_02_phase.questphase / h0 / 46` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/investigate_bridge` | 290:CutSource → 46:CutDestination; 277:True → 46:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 64` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/investigate_bridge` | 14:Out1 → 64:Succeeded; 64:Out → 16:Active; 64:Out → 276:In |
| `ma_wat_kab_02_phase.questphase / h0 / 86` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/search_clues` | 85:False → 86:Active; 86:Out → 248:In; 86:Out → 145:In |
| `ma_wat_kab_02_phase.questphase / h0 / 88` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/search_clues` | 145:Out → 88:Succeeded; 88:Out → 93:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 93` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info` | 85:True → 93:Active; 88:Out → 93:Active; 93:Out → 231:In; 93:Out → 273:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 107` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info` | 107:Out → 19:Succeeded; 149:Out → 107:Succeeded; 107:Out → 274:Inactive |
| `ma_wat_kab_02_phase.questphase / h0 / 250` (MappinManager) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/search_clues/laptop` | 248:Out → 250:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 273` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info/regina` | 93:Out → 273:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 274` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info/regina` | 107:Out → 274:Inactive |
| `ma_wat_kab_02_phase.questphase / h0 / 279` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/search_clues` | 18:Out → 279:Active; 279:Out → 282:In |
| `ma_wat_kab_02_phase.questphase / h0 / 281` (Journal) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/search_clues` | 85:True → 281:Succeeded |
| `ma_wat_kab_02_phase.questphase / h0 / 282` (Condition) | `quests/minor_quest/ma_wat_kab_02/description` | 282:False → 278:In2; 282:True → 278:In2; 279:Out → 282:In; 282:True → 285:In2 |
| `ma_wat_kab_02_phase.questphase / h0 / 296` (Condition: holo_setup_active; holo_setup_started) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/investigate_bridge` | 78:Out → 296:In; 296:False → 230:ma_wat_kab_02_holocall_in; 296:True → 297:In |
| `ma_wat_kab_02_phase.questphase / h0 / 297` (Condition) | `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info`; `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info` | 297:False → 292:Active; 296:True → 297:In; 297:True → 298:Inactive |
| `ma_wat_kab_02_quest_bugfixes.questphase / h30 / 5` (Journal) | `quests/minor_quest/ma_wat_kab_02` | 6:True → 5:Succeeded; 5:Out → 8:In |
| `ma_wat_kab_02_quest_bugfixes.questphase / h30 / 6` (Condition) | `quests/minor_quest/ma_wat_kab_02` | 4:True → 6:In; 6:True → 5:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `ma_wat_kab_02_phase.questphase / h0 / 62` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene`; `#ma_sm_wat_kab_02` | 251:Out → 62:ma_wat_kab_02_in; 62:ma_wat_kab_02_out → 270:In |
| `ma_wat_kab_02_phase.questphase / h0 / 230` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene`; `#ma_sm_wat_kab_02` | 230:ma_wat_kab-02_holocall_out → 77:In; 296:False → 230:ma_wat_kab_02_holocall_in; 230:call_rejected → 292:Active; 230:Holocall INT → 272:In; 230:Holocall RET → 271:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\kabuki_minor_activities.questphase` / h0 / 45 | `ma_wat_kab_02_phase.questphase` | 116: PauseCondition: ow_psychos_intro_done; 112: CutControl; 116:Out → 45:In1; 112:CutSource → 45:CutDestination |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 62 | `ma_wat_kab_02.scene` | 251: PauseCondition: #ma_wat_kab_02_tr_sounds; 251:Out → 62:ma_wat_kab_02_in; 62:ma_wat_kab_02_out → 270:In |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 230 | `ma_wat_kab_02.scene` | 296: Condition: holo_setup_active; holo_setup_started; 230:ma_wat_kab-02_holocall_out → 77:In; 296:False → 230:ma_wat_kab_02_holocall_in; 230:call_rejected → 292:Active; 230:Holocall INT → 272:In; 230:Holocall RET → 271:In |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 13 | `ma_wat_kab_02_quest_bugfixes.questphase` | 19: LogicalHub; 19:Out1 → 13:In1 |
| `base\open_world\minor_activities\open_world_minor_activities.questphase` / h0 / 2 | `kabuki_minor_activities.questphase` | 35: Condition: ma_kab_02_finished; 37: LogicalHub; 35:True → 2:kill; 37:Out1 → 2:In1 |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
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
| `ma_wat_kab_02.scene` | ma_wat_kab_02_in, ma_wat_kab_02_holocall_in, ma_wat_kab_02_clue_choices_in → ma_wat_kab_02_out, ma_wat_kab-02_holocall_out, call_rejected, ma_wat_kab_02_clue_choices_out | psycho; ncpd; droid; regina; car; Player; 76 nodes / 104 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `ma_wat_kab_02.scene / n218 / 0` | Text join unresolved (`Option`) | No option-level predicate stored | 0:0 → 286:0:0 |
| `ma_wat_kab_02.scene / n221 / 0` | Text join unresolved (`Option`) | No option-level predicate stored | 0:0 → 286:0:0 |
| `ma_wat_kab_02.scene / n222 / 0` | Text join unresolved (`Option`) | No option-level predicate stored | 0:0 → 286:0:0 |
| `ma_wat_kab_02.scene / n225 / 0` | Text join unresolved (`Option`) | No option-level predicate stored | 0:0 → 286:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-12345` | ma_wat_kab_02_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-660072` | ma_wat_kab_02_quest_bugfixes.questphase / h30 / 2 | ma_wat_kab_02_quest_bugfixes.questphase / h30 / 7 |
| `ep1_standalone` | Producer outside selected context | ma_wat_kab_02_phase.questphase / h1449 / 9 |
| `glossary_cyberpsychosis` | ma_wat_kab_02_phase.questphase / h0 / 76 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | ma_wat_kab_02.scene / scene / 509 |
| `holo_reggie_calls_v_end_activate` | ma_wat_kab_02.scene / scene / 457; ma_wat_kab_02_phase.questphase / h0 / 272 | No reader in selected context |
| `holo_reggie_calls_v_end_done` | ma_wat_kab_02.scene / scene / 449 | ma_wat_kab_02.scene / scene / 447 |
| `holo_reggie_calls_v_rejectable` | ma_wat_kab_02.scene / scene / 490; ma_wat_kab_02.scene / scene / 507 | No reader in selected context |
| `holo_reggie_calls_v_rejected` | ma_wat_kab_02.scene / scene / 494 | ma_wat_kab_02.scene / scene / 492 |
| `holo_reggie_calls_v_start_activate` | ma_wat_kab_02.scene / scene / 455; ma_wat_kab_02.scene / scene / 505; ma_wat_kab_02_phase.questphase / h0 / 271 | No reader in selected context |
| `holo_reggie_calls_v_start_done` | ma_wat_kab_02.scene / scene / 445 | ma_wat_kab_02.scene / scene / 518 |
| `holo_setup_active` | Producer outside selected context | ma_wat_kab_02.scene / scene / 509; ma_wat_kab_02_phase.questphase / h0 / 296 |
| `holo_setup_started` | Producer outside selected context | ma_wat_kab_02.scene / scene / 509; ma_wat_kab_02_phase.questphase / h0 / 296 |
| `ma_hunt_for_psycho_tutorial` | ma_wat_kab_02_phase.questphase / h0 / 77 | No reader in selected context |
| `ma_kab_02_finished` | ma_wat_kab_02_phase.questphase / h0 / 29 | ma_wat_kab_02_quest_bugfixes.questphase / h30 / 4 |
| `ma_kab_02_start` | ma_wat_kab_02_phase.questphase / h0 / 78 | No reader in selected context |
| `ma_token` | ma_wat_kab_02_phase.questphase / h0 / 30 | No reader in selected context |
| `ma_wat_kab_02_bridge_investigated` | ma_wat_kab_02_phase.questphase / h0 / 276 | ma_wat_kab_02_phase.questphase / h0 / 277 |
| `ma_wat_kab_02_chicken_test` | Producer outside selected context | ma_wat_kab_02_phase.questphase / h1449 / 7 |
| `ma_wat_kab_02_combat_start` | ma_wat_kab_02_phase.questphase / h839 / 28 | ma_wat_kab_02.scene / scene / 24; ma_wat_kab_02.scene / scene / 363 |
| `ma_wat_kab_02_email_01_read` | Producer outside selected context | ma_wat_kab_02_phase.questphase / h0 / 145; ma_wat_kab_02_phase.questphase / h0 / 85 |
| `ma_wat_kab_02_email_02_read` | Producer outside selected context | ma_wat_kab_02_phase.questphase / h0 / 145; ma_wat_kab_02_phase.questphase / h0 / 85 |
| `ma_wat_kab_02_email_03_read` | Producer outside selected context | ma_wat_kab_02_phase.questphase / h0 / 145; ma_wat_kab_02_phase.questphase / h0 / 85 |
| `ow_psychos_done` | ma_wat_kab_02_phase.questphase / h0 / 267 | No reader in selected context |
| `ow_psychos_killed` | ma_wat_kab_02_phase.questphase / h0 / 266 | No reader in selected context |
| `q003_done` | Producer outside selected context | ma_wat_kab_02_phase.questphase / h1449 / 3 |
| `travelling_merchant_lives` | Producer outside selected context | ma_wat_kab_02_quest_bugfixes.questphase / h0 / 13 |

## Exact gates, joins and cancellation

<details><summary>101 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `ma_wat_kab_02_phase.questphase / h0 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]}}}}` | 112:Out1 → 11:In; 11:Out → 14:In1 |
| `ma_wat_kab_02_phase.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterAttack_ConditionType","attackerRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"isTargetPlayer":true}}}` | 112:Out1 → 12:In; 12:Out → 14:In2 |
| `ma_wat_kab_02_phase.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]}}}}` | 112:Out1 → 13:In; 13:Out → 14:In3 |
| `ma_wat_kab_02_phase.questphase / h0 / 14` | `questLogicalXorNodeDefinition` `{"inputSocketCount":5}` | 11:Out → 14:In1; 12:Out → 14:In2; 13:Out → 14:In3; 144:Out → 14:In4; 270:Out → 14:In5; 14:Out1 → 120:In; 14:Out1 → 64:Succeeded; 14:Out1 → 163:In1; 14:Out1 → 172:In1; 14:Out1 → 214:In |
| `ma_wat_kab_02_phase.questphase / h0 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 16:Out → 17:In; 17:Out → 39:In; 17:Out → 209:In1; 17:Out → 215:In; 17:Out → 306:In |
| `ma_wat_kab_02_phase.questphase / h0 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":6}}}` | 24:Out → 31:In; 31:Out → 35:In |
| `ma_wat_kab_02_phase.questphase / h0 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_wat_kab_02_tr_distant_sounds"}}` | 31:Out → 35:In; 35:Out → 33:In; 35:Out → 40:In1 |
| `ma_wat_kab_02_phase.questphase / h0 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_wat_kab_02_tr_distant_sounds"}}` | 223:CutSource → 72:CutDestination; 254:Out1 → 72:In; 72:Out → 261:In; 72:Out → 299:In; 72:Out → 303:In |
| `ma_wat_kab_02_phase.questphase / h0 / 85` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_email_01_read"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_email_02_read"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_email_03_read"}}]}}` | 229:Out → 85:In; 85:True → 93:Active; 85:True → 210:In; 85:True → 281:Succeeded; 85:False → 86:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_wat_kab_02/01_ch_info/01_ch_info","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 94:Out → 96:In; 96:Out → 95:Active; 237:CutSource → 96:CutDestination |
| `ma_wat_kab_02_phase.questphase / h0 / 99` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"93268646650","value":false}},{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"85882596286","value":false}},{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"87833202724","value":false}}]}}` | 95:Out → 99:In; 240:Out → 99:In; 99:Out → 134:In1; 99:Out → 149:In; 99:Out → 267:In |
| `ma_wat_kab_02_phase.questphase / h0 / 137` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 137:Out1 → 78:In; 299:Out → 137:In1; 300:Out → 137:In2; 301:Out → 137:In3 |
| `ma_wat_kab_02_phase.questphase / h0 / 144` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_wat_kab_02_tr_search_area"}}` | 144:Out → 14:In4; 112:Out1 → 144:In |
| `ma_wat_kab_02_phase.questphase / h0 / 145` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_email_01_read"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_email_02_read"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_email_03_read"}}]}}` | 86:Out → 145:In; 145:Out → 88:Succeeded; 145:Out → 148:In; 145:Out → 166:In |
| `ma_wat_kab_02_phase.questphase / h0 / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 99:Out → 149:In; 149:Out → 107:Succeeded; 149:Out → 216:In; 149:Out → 221:In1 |
| `ma_wat_kab_02_phase.questphase / h0 / 153` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 210:CutSource → 153:CutDestination; 229:Out → 153:In; 153:Out → 156:In |
| `ma_wat_kab_02_phase.questphase / h0 / 210` | `questCutControlNodeDefinition` `{}` | 85:True → 210:In; 210:Out → 148:In; 210:CutSource → 153:CutDestination |
| `ma_wat_kab_02_phase.questphase / h0 / 223` | `questCutControlNodeDefinition` `{}` | 223:CutSource → 72:CutDestination; 222:Out1 → 223:In; 223:CutSource → 264:CutDestination; 223:CutSource → 263:CutDestination |
| `ma_wat_kab_02_phase.questphase / h0 / 231` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 93:Out → 231:In; 231:False → 94:Active; 231:True → 233:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 235` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_wat_kab_02/01_ch_info_killed/01_ch_info_killed","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 233:Out → 235:In; 235:Out → 240:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 236` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 94:Out → 236:In; 238:CutSource → 236:CutDestination; 236:Out → 237:In |
| `ma_wat_kab_02_phase.questphase / h0 / 237` | `questCutControlNodeDefinition` `{}` | 237:CutSource → 96:CutDestination; 236:Out → 237:In; 237:Out → 239:Inactive; 237:Out → 241:In1 |
| `ma_wat_kab_02_phase.questphase / h0 / 238` | `questCutControlNodeDefinition` `{"permanent":true}` | 238:CutSource → 94:CutDestination; 95:Out → 238:In; 238:CutSource → 233:CutDestination; 238:CutSource → 236:CutDestination; 240:Out → 238:In |
| `ma_wat_kab_02_phase.questphase / h0 / 248` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_dvc_laptop"},"angleTolerance":10.0}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_dvc_laptop"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":8.0},"comparisonType":"LessOrEqual"}}]},{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_dvc_laptop"}}}]}}` | 86:Out → 248:In; 248:Out → 250:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_wat_kab_02_tr_sounds"}}` | 251:Out → 62:ma_wat_kab_02_in; 111:Out1 → 251:In |
| `ma_wat_kab_02_phase.questphase / h0 / 263` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_wat_kab_02_tr_sounds"}}` | 223:CutSource → 263:CutDestination; 261:Out → 263:In; 263:Out → 262:In |
| `ma_wat_kab_02_phase.questphase / h0 / 264` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_wat_kab_02_tr_sounds"}}` | 223:CutSource → 264:CutDestination; 264:Out → 261:In; 262:Out → 264:In |
| `ma_wat_kab_02_phase.questphase / h0 / 265` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"},"unconscious":false,"defeated":false}}}` | 16:Out → 265:In; 265:Out → 266:In |
| `ma_wat_kab_02_phase.questphase / h0 / 277` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_bridge_investigated","comparisonType":"Equal"}}}` | 9:Out → 277:In; 277:True → 46:Active |
| `ma_wat_kab_02_phase.questphase / h0 / 278` | `questLogicalAndNodeDefinition` `{}` | 278:Out1 → 229:In; 285:Out1 → 278:In1; 282:False → 278:In2; 282:True → 278:In2; 278:Out1 → 290:In |
| `ma_wat_kab_02_phase.questphase / h0 / 282` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"points_of_interest/minor_quests/ma_wat_kab_02","fileEntryIndex":1,"className":"gameJournalPointOfInterestMappin"},"state":"Inactive"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"points_of_interest/minor_activities/ma_wat_kab_02","fileEntryIndex":1,"className":"gameJournalPointOfInterestMappin"},"state":"Inactive"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_wat_kab_02/description","fileEntryIndex":2,"className":"gameJournalQuestDescription"},"state":"Active"}}]}}` | 282:False → 278:In2; 282:True → 278:In2; 279:Out → 282:In; 282:True → 285:In2 |
| `ma_wat_kab_02_phase.questphase / h0 / 285` | `questLogicalXorNodeDefinition` `{}` | 285:Out1 → 278:In1; 282:True → 285:In2; 284:Out1 → 285:In1 |
| `ma_wat_kab_02_phase.questphase / h0 / 290` | `questCutControlNodeDefinition` `{"permanent":true}` | 290:CutSource → 8:CutDestination; 290:CutSource → 9:CutDestination; 290:CutSource → 46:CutDestination; 290:CutSource → 138:CutDestination; 290:CutSource → 211:CutDestination; 278:Out1 → 290:In |
| `ma_wat_kab_02_phase.questphase / h0 / 294` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":300}}}` | 294:Out → 77:In; 292:Out → 294:In |
| `ma_wat_kab_02_phase.questphase / h0 / 296` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started"}},{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","anyParent":true,"childIsPlayer":true}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType","isContentBlocked":true}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/investigate_bridge","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 78:Out → 296:In; 296:False → 230:ma_wat_kab_02_holocall_in; 296:True → 297:In |
| `ma_wat_kab_02_phase.questphase / h0 / 297` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}]}}` | 297:False → 292:Active; 296:True → 297:In; 297:True → 298:Inactive |
| `ma_wat_kab_02_phase.questphase / h210 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"$/03_night_city/c_watson/kabuki/kab_cs_prefabVIKCXXI/cs_cyberpsycho_disposal_openworld_003_prefabJGAV5ZA/cs_tr_reset"},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_after_com","names":["investigator"]},"onScreenTest":true}}]}}` | 3:Out → 4:In; 4:Out → 5:In |
| `ma_wat_kab_02_phase.questphase / h210 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":24}}}` | 4:Out → 5:In; 5:Out → 12:In |
| `ma_wat_kab_02_phase.questphase / h210 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"$/03_night_city/c_watson/kabuki/kab_cs_prefabVIKCXXI/cs_cyberpsycho_disposal_openworld_003_prefabJGAV5ZA/cs_tr_reset"}}` | 11:Out → 10:In; 19:Out → 11:In |
| `ma_wat_kab_02_phase.questphase / h210 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"$/03_night_city/c_watson/kabuki/kab_cs_prefabVIKCXXI/cs_cyberpsycho_disposal_openworld_003_prefabJGAV5ZA/cs_tr_reset"}}` | 5:Out → 12:In; 12:Out → 6:In |
| `ma_wat_kab_02_phase.questphase / h210 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":3}}}` | 19:Out → 17:In; 17:Out → 18:In |
| `ma_wat_kab_02_phase.questphase / h210 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"$/03_night_city/c_watson/kabuki/kab_cs_prefabVIKCXXI/cs_cyberpsycho_disposal_openworld_003_prefabJGAV5ZA/cs_tr_reset"}}` | 18:Out → 14:In; 17:Out → 18:In |
| `ma_wat_kab_02_phase.questphase / h210 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":18}}}` | 0:Out → 19:In; 19:Out → 11:In; 19:Out → 17:In |
| `ma_wat_kab_02_phase.questphase / h210 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_after_com"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2:Out → 23:In; 23:Out → 24:In |
| `ma_wat_kab_02_phase.questphase / h384 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 6:Out → 1:In; 2:Out → 6:In; 6:Out → 8:In |
| `ma_wat_kab_02_phase.questphase / h384 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["droid"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 2:Out → 13:In; 13:Out → 12:In |
| `ma_wat_kab_02_phase.questphase / h384 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["ncpd"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 2:Out → 17:In; 17:Out → 16:In |
| `ma_wat_kab_02_phase.questphase / h839 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 8:Out → 7:In; 19:Out → 8:In |
| `ma_wat_kab_02_phase.questphase / h839 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":25}}}` | 11:Out1 → 10:In; 10:Out → 14:In1 |
| `ma_wat_kab_02_phase.questphase / h839 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":20}}}` | 11:Out2 → 12:In; 12:Out → 14:In2 |
| `ma_wat_kab_02_phase.questphase / h839 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"isPlayer":false,"percent":5.0,"comparisonType":"LessOrEqual"}}}` | 0:Out → 18:In; 18:Out → 19:In |
| `ma_wat_kab_02_phase.questphase / h839 / 19` | `questCutControlNodeDefinition` `{"permanent":true}` | 19:Out → 8:In; 19:CutSource → 9:CutDestination; 18:Out → 19:In |
| `ma_wat_kab_02_phase.questphase / h839 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 0:Out → 20:In; 20:Out → 16:In1 |
| `ma_wat_kab_02_phase.questphase / h839 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_wat_kab_02_tr_sounds"}}` | 24:Out1 → 21:In; 21:Out → 22:In |
| `ma_wat_kab_02_phase.questphase / h839 / 22` | `questCutControlNodeDefinition` `{}` | 22:CutSource → 3:CutDestination; 21:Out → 22:In; 22:Out → 25:In1 |
| `ma_wat_kab_02_phase.questphase / h839 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_wat_kab_02_tr_sounds"}}` | 25:Out1 → 23:In; 23:Out → 24:In1 |
| `ma_wat_kab_02_phase.questphase / h839 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"isPlayer":false,"inverted":true}}}` | 35:Out → 32:In; 36:Out → 35:In |
| `ma_wat_kab_02_phase.questphase / h1029 / 22` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 22:Out1 → 8:In; 26:Out → 22:In1; 23:Out → 22:In2; 24:Out → 22:In3; 25:Out → 22:In4 |
| `ma_wat_kab_02_phase.questphase / h1029 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_corpse_000"},"eventType":"Finished"}}}` | 0:Out → 23:In; 23:Out → 22:In2 |
| `ma_wat_kab_02_phase.questphase / h1029 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_corpse_001"},"eventType":"Finished"}}}` | 0:Out → 24:In; 24:Out → 22:In3 |
| `ma_wat_kab_02_phase.questphase / h1029 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_corpse_002"},"eventType":"Finished"}}}` | 0:Out → 25:In; 25:Out → 22:In4 |
| `ma_wat_kab_02_phase.questphase / h1029 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_corpse_003"},"eventType":"Finished"}}}` | 0:Out → 26:In; 26:Out → 22:In1 |
| `ma_wat_kab_02_phase.questphase / h1109 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/watson/kabuki/ma_wat_kab_02/onscreens/ma_wat_kab_02_onscreen_02","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}},{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_corpse_000"},"eventType":"Finished"}}]}}` | 6:Out → 4:In; 4:Out → 5:In |
| `ma_wat_kab_02_phase.questphase / h1109 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"eventType":"Finished"}}}` | 2:Out → 7:In; 7:Out → 12:In; 7:Out → 8:In |
| `ma_wat_kab_02_phase.questphase / h1109 / 9` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 9:Out1 → 1:In; 5:Out → 9:In3; 8:Out → 9:In2; 11:Out → 9:In1 |
| `ma_wat_kab_02_phase.questphase / h1109 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 12:In; 12:Out → 11:In |
| `ma_wat_kab_02_phase.questphase / h1222 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_wat_kab_02_tr_mute_distant_sounds"}}` | 19:Out → 4:In; 4:Out → 18:In; 4:Out → 23:In |
| `ma_wat_kab_02_phase.questphase / h1222 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_wat_kab_02_tr_distant_sounds"}}` | 0:Out → 7:In; 7:Out → 15:In |
| `ma_wat_kab_02_phase.questphase / h1222 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 4:Out → 18:In; 18:Out → 16:In |
| `ma_wat_kab_02_phase.questphase / h1222 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 19:Out → 2:In; 19:Out → 4:In; 15:Out → 19:In |
| `ma_wat_kab_02_phase.questphase / h1222 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_wat_kab_02_tr_judy_disable_sounds"}}` | 2:Out → 20:In; 23:CutSource → 20:CutDestination; 20:Out → 22:In; 20:Out → 24:In |
| `ma_wat_kab_02_phase.questphase / h1222 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_wat_kab_02_tr_judy_disable_sounds"}}` | 21:Out → 2:In; 23:CutSource → 21:CutDestination; 22:Out → 21:In; 21:Out → 25:In |
| `ma_wat_kab_02_phase.questphase / h1222 / 23` | `questCutControlNodeDefinition` `{}` | 23:Out → 3:In; 4:Out → 23:In; 23:CutSource → 20:CutDestination; 23:CutSource → 21:CutDestination |
| `ma_wat_kab_02_phase.questphase / h1449 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q003_done"}}}` | 9:False → 3:In; 3:Out → 4:In |
| `ma_wat_kab_02_phase.questphase / h1449 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_wat_kab_02_tr_distant_sounds"}}` | 3:Out → 4:In; 4:Out → 6:In |
| `ma_wat_kab_02_phase.questphase / h1449 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_wat_kab_02_tr_distant_sounds"}}` | 5:Out → 2:Active; 6:Out → 5:In; 9:True → 5:In |
| `ma_wat_kab_02_phase.questphase / h1449 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":8}}}` | 4:Out → 6:In; 6:Out → 5:In |
| `ma_wat_kab_02_phase.questphase / h1449 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_chicken_test"}}}` | 0:Out → 7:In; 7:True → 2:Active; 7:False → 9:In |
| `ma_wat_kab_02_phase.questphase / h1449 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone","value":1,"comparisonType":"GreaterOrEqual"}}}` | 9:False → 3:In; 9:True → 5:In; 7:False → 9:In |
| `ma_wat_kab_02.scene / scene / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_combat_start"}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["ncpd"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":15.0},"comparisonType":"LessOrEqual"}}]}}` | 10:2:0 → 24:0:0; 24:0:0 → 21:0:0; 24:0:0 → 151:0:1; 24:0:0 → 380:0:1; 105:0:0 → 24:0:1; 368:1:0 → 24:0:0; 368:1:0 → 24:1026:0 |
| `ma_wat_kab_02.scene / scene / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"observedTargetRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["droid"]},"isObservedTargetPlayer":false}},{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}]}}` | 21:0:0 → 48:0:1; 48:0:0 → 140:0:0; 48:0:0 → 202:0:0; 48:0:0 → 392:0:1; 305:0:0 → 48:0:1; 368:1:0 → 48:0:0; 368:1:0 → 48:1026:0 |
| `ma_wat_kab_02.scene / scene / 105` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#ma_wat_kab_02_tr"},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["ncpd"]},"timeInterval":3.0,"angleTolerance":4.0}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["droid"]},"timeInterval":3.0,"angleTolerance":4.0}}]}}` | 1:0:0 → 105:0:1; 105:0:0 → 10:0:0; 105:0:0 → 24:0:1; 105:0:0 → 182:0:1; 105:0:0 → 300:0:1; 105:0:0 → 363:0:0; 105:0:0 → 367:0:1; 105:0:0 → 377:0:1; 368:1:0 → 105:0:0; 368:1:0 → 105:1026:0 |
| `ma_wat_kab_02.scene / scene / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":300}}}` | 97:0:0 → 146:0:1; 146:0:0 → 60:0:1 |
| `ma_wat_kab_02.scene / scene / 182` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 105:0:0 → 182:0:1; 182:0:0 → 178:0:1; 368:1:0 → 182:0:0; 368:1:0 → 182:1026:0 |
| `ma_wat_kab_02.scene / scene / 207` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["ncpd"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0},"comparisonType":"LessOrEqual"}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["ncpd"]},"timeInterval":0.0,"onScreenTest":true}}]}}` | 10:2:0 → 207:0:1; 21:2:0 → 207:0:1; 207:0:0 → 169:0:0 |
| `ma_wat_kab_02.scene / scene / 212` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["ncpd"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 1:0:0 → 212:0:1 |
| `ma_wat_kab_02.scene / scene / 300` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 105:0:0 → 300:0:1; 300:0:0 → 185:0:1 |
| `ma_wat_kab_02.scene / scene / 305` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 10:0:0 → 305:0:1; 305:0:0 → 48:0:1 |
| `ma_wat_kab_02.scene / scene / 363` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_wat_kab_02_combat_start"}}}` | 1:0:0 → 363:0:1; 105:0:0 → 363:0:0; 363:0:0 → 202:0:0; 363:0:0 → 368:0:0; 363:0:0 → 384:0:1 |
| `ma_wat_kab_02.scene / scene / 392` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"Greater"}}}}` | 48:0:0 → 392:0:1; 392:0:1 → 97:0:1 |
| `ma_wat_kab_02.scene / scene / 447` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 447:0:0 → 449:0:1; 457:0:0 → 447:0:1 |
| `ma_wat_kab_02.scene / scene / 483` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_wat_kab_02_com_psycho","names":["ncpd"]},"eventType":"Finished"}}}` | 478:0:0 → 483:0:1; 483:0:0 → 482:0:1 |
| `ma_wat_kab_02.scene / scene / 492` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 455:0:0 → 492:0:1; 492:0:0 → 494:0:1 |
| `ma_wat_kab_02.scene / scene / 503` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 443:666:0 → 503:0:1; 503:0:0 → 509:0:1; 521:1:0 → 503:0:0 |
| `ma_wat_kab_02.scene / scene / 509` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 503:0:0 → 509:0:1; 509:0:0 → 507:0:1; 509:0:1 → 511:0:1; 511:0:0 → 509:0:1 |
| `ma_wat_kab_02.scene / scene / 511` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 509:0:1 → 511:0:1; 511:0:0 → 509:0:1; 521:1:0 → 511:0:0 |
| `ma_wat_kab_02.scene / scene / 518` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 443:666:0 → 518:0:1; 518:0:0 → 521:0:0 |
| `ma_wat_kab_02_quest_bugfixes.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 14:Out → 13:In |
| `ma_wat_kab_02_quest_bugfixes.questphase / h30 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_kab_02_finished"}}}` | 2:Out → 4:In; 4:True → 6:In |
| `ma_wat_kab_02_quest_bugfixes.questphase / h30 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_wat_kab_02","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 4:True → 6:In; 6:True → 5:Succeeded |
| `ma_wat_kab_02_quest_bugfixes.questphase / h30 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-660072","comparisonType":"Equal"}}}` | 0:Out → 7:In; 7:True → 2:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | ma_wat_kab_02.scene / scene / 212; ma_wat_kab_02_phase.questphase / h210 / 23; ma_wat_kab_02_phase.questphase / h384 / 13; ma_wat_kab_02_phase.questphase / h384 / 17; +1 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | ma_wat_kab_02.scene / scene / 115; ma_wat_kab_02.scene / scene / 163; ma_wat_kab_02.scene / scene / 202 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | ma_wat_kab_02_phase.questphase / h0 / 247; ma_wat_kab_02_phase.questphase / h0 / 37 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | ma_wat_kab_02.scene / scene / 218; ma_wat_kab_02.scene / scene / 221; ma_wat_kab_02.scene / scene / 222; ma_wat_kab_02.scene / scene / 225 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | ma_wat_kab_02_phase.questphase / h839 / 3 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | ma_wat_kab_02_phase.questphase / h0 / 33; ma_wat_kab_02_phase.questphase / h210 / 14; ma_wat_kab_02_phase.questphase / h210 / 2; ma_wat_kab_02_phase.questphase / h210 / 6; +3 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | ma_wat_kab_02.scene / scene / 24; ma_wat_kab_02.scene / scene / 363; ma_wat_kab_02.scene / scene / 447; ma_wat_kab_02.scene / scene / 492; +12 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | ma_wat_kab_02.scene / scene / 396; ma_wat_kab_02.scene / scene / 398; ma_wat_kab_02.scene / scene / 478; ma_wat_kab_02.scene / scene / 482; +24 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `elapsed_time` | ma_wat_kab_02_phase.questphase / h0 / 31; ma_wat_kab_02_phase.questphase / h1449 / 6; ma_wat_kab_02_phase.questphase / h210 / 17; ma_wat_kab_02_phase.questphase / h210 / 19; +1 locations in catalogue.json | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | ma_wat_kab_02_phase.questphase / h0 / 107; ma_wat_kab_02_phase.questphase / h0 / 138; ma_wat_kab_02_phase.questphase / h0 / 16; ma_wat_kab_02_phase.questphase / h0 / 18; +23 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | ma_wat_kab_02_phase.questphase / h0 / 296 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | ma_wat_kab_02_phase.questphase / h0 / 278; ma_wat_kab_02_phase.questphase / h1109 / 9 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | ma_wat_kab_02.scene / scene / 445; ma_wat_kab_02.scene / scene / 449; ma_wat_kab_02.scene / scene / 455; ma_wat_kab_02.scene / scene / 457; +17 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | ma_wat_kab_02_phase.questphase / h0 / 137; ma_wat_kab_02_phase.questphase / h0 / 14; ma_wat_kab_02_phase.questphase / h0 / 285; ma_wat_kab_02_phase.questphase / h1029 / 22 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | ma_wat_kab_02.scene / scene / 146; ma_wat_kab_02.scene / scene / 182; ma_wat_kab_02.scene / scene / 300; ma_wat_kab_02.scene / scene / 305; +12 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | ma_wat_kab_02_phase.questphase / h0 / 210; ma_wat_kab_02_phase.questphase / h0 / 223; ma_wat_kab_02_phase.questphase / h0 / 237; ma_wat_kab_02_phase.questphase / h0 / 238; +4 locations in catalogue.json | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | ma_wat_kab_02_phase.questphase / h0 / 24 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | ma_wat_kab_02.scene / scene / 483; ma_wat_kab_02_phase.questphase / h0 / 11; ma_wat_kab_02_phase.questphase / h0 / 248; ma_wat_kab_02_phase.questphase / h1029 / 23; +5 locations in catalogue.json | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | ma_wat_kab_02_phase.questphase / h0 / 230; ma_wat_kab_02_phase.questphase / h0 / 62 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | ma_wat_kab_02.scene / scene / 105; ma_wat_kab_02_phase.questphase / h0 / 144; ma_wat_kab_02_phase.questphase / h0 / 251; ma_wat_kab_02_phase.questphase / h0 / 263; +15 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | ma_wat_kab_02.scene / scene / 392; ma_wat_kab_02_phase.questphase / h0 / 17; ma_wat_kab_02_phase.questphase / h0 / 231; ma_wat_kab_02_phase.questphase / h0 / 236; +2 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | ma_wat_kab_02_phase.questphase / h0 / 229; ma_wat_kab_02_phase.questphase / h210 / 24; ma_wat_kab_02_phase.questphase / h210 / 25; ma_wat_kab_02_phase.questphase / h384 / 15 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `weighted_branch` | ma_wat_kab_02_phase.questphase / h0 / 156; ma_wat_kab_02_phase.questphase / h839 / 11; ma_wat_kab_02_phase.questphase / h839 / 9 | ordered output weights + explicit route bindings → one authored weighted output. Preserve output ordering, reset scope and persistence; compose difficulty and timing as separate gates. |
| `workspot_performance` | ma_wat_kab_02.scene / scene / 117; ma_wat_kab_02.scene / scene / 119; ma_wat_kab_02.scene / scene / 19; ma_wat_kab_02.scene / scene / 22; +1 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | ma_wat_kab_02_phase.questphase / h0 / 244; ma_wat_kab_02_phase.questphase / h0 / 41; ma_wat_kab_02_phase.questphase / h1222 / 15; ma_wat_kab_02_phase.questphase / h1222 / 16; +9 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` | content candidate; journal anchor | `base-ma-wat-kab-02` |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` | content candidate; forward dependency | `base-ma-wat-kab-02` |
| `base\quest\bugfixing\minor_quests\ma_wat_kab_02\ma_wat_kab_02_quest_bugfixes.questphase` | repair; journal anchor | `base-ma-wat-kab-02` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

229 repeated typed/socket path signatures in this selected graph context; 10 distinct direct resource identities; 10 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 457 -> 447 -> 449 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `a3e5f861a4b71433135a` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h210 / 19 -> 11 -> 10 | questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]; Out -> In; Out -> In |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 447 -> 449 -> 332 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 445 -> 451 -> 335 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 490 -> 455 -> 492 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `ea4cb15199b9b3fa8e63` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h210 / 0 -> 19 -> 11 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `2beeeaa3b4da5300c035` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 331 -> 490 -> 455 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `bbf9efd740881cf31a37` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 363 -> 368 -> 182 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 507 -> 505 -> 496 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `cbae0fd3078e68426197` | `base\quest\bugfixing\minor_quests\ma_wat_kab_02\ma_wat_kab_02_quest_bugfixes.questphase` / h0 / 10 -> 14 -> 13 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `129f2cf1d416edbd0fd1` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 518 -> 521 -> 445 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `19665e3783f6f51a7337` | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 1 -> 95 -> 119 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 40 | `h210` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 67 | `h384` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 134 | `h713` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 172 | `h839` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 201 | `h1029` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 209 | `h1109` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 228 | `h1222` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 254 | `h1449` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\ma_wat_kab_02\ma_wat_kab_02_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\ma_wat_kab_02\ma_wat_kab_02_quest_bugfixes.questphase` / h0 / 12 | `h30` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\animations\quest\main_quests\part1\q101\06c_memories_p2\q101_06c_memories_p2__man_average_animation.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q104\q104_07b_haru_found\body\q104_07b_haru_found__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\lipsync\en\ma_wat_kab_02\civ_prnd_m_01_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\lipsync\en\ma_wat_kab_02\droid_combat.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\lipsync\en\ma_wat_kab_02\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\lipsync\en\ma_wat_kab_02\sec_mid_m_04_afam_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\lipsync\en\ma_wat_kab_02\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\ground\generic__lie_ground_lean_front__dead__05.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q101\06c_memories_adam_smasher\q101_06c_adam_smasher__arasaka_soldier_standing__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `ep1_standalone` | ep1\quest\ep1_standalone.quest / h0 / 5; 1 total source locations in compressed evidence |
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
| `ma_wat_kab_02_chicken_test` | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest / h0 / 5; 1 total source locations in compressed evidence |
| `ow_psychos_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 110; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 188; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 176; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 111; 16 total source locations in compressed evidence |
| `ow_psychos_killed` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 166; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 217; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 130; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 279; 19 total source locations in compressed evidence |
| `q003_done` | base\quest\minor_quests\mq018\test\mq018_00_chickentest.scene / scene / 31; base\quest\minor_quests\mq018\test\mq018_00_chickentest.scene / scene / 32; base\quest\minor_quests\mq018\test\mq018_00_chickentest.scene / scene / 34; base\quest\minor_quests\mq018\test\mq018_00_chickentest.scene / scene / 71; 17 total source locations in compressed evidence |

NodeRef uses: 172; TweakDB binding uses: 20. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` | 7 / 21 | scnChangeIdleAnimEvent: 2; scnDialogLineEvent: 3; scnLookAtAdvancedEvent: 3; scnPlaySkAnimEvent: 2; scneventsSocket: 9; scneventsVFXEvent: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
