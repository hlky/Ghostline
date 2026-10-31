# Cyberpsycho Sighting: House on a Hill

Journal: `quests/minor_quest/ma_bls_ina_se1_08` · `CyberPsycho` · hash `3723374653`.

Journal premise: Shots were heard on the outskirts of NC – rare given the seemingly peaceful area. We oughta go and take a closer look. Why wait for the clean-up crew when there could still be lives that need saving?

**Coverage: journal-linked.** 23 exact journal-linked nodes in 3 resources; 4 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Read Regina's message in the cyberpsycho message thread. (Primary) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_message` |
| Read the shard located on the cyberpsycho's body. (Primary) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_shard` |
| Read the shard located on the dead woman. (Primary) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_woman_shard` |
| Search the area to collect information. (Primary) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues` |
| Neutralize the threat. (Primary) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/kill` |
| Find the cyberpsycho. (Primary) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/search` |
| Message Regina about Cyberspycho Sighting: House on a Hill (Primary) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 82` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/description` | 73:Out → 82:Active; 82:Out → 83:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 83` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/search` | 82:Out → 83:Active; 83:Out → 189:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 92` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/search` | 19:Out1 → 92:Succeeded; 92:Out → 93:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 93` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/kill` | 93:Out → 22:In; 92:Out → 93:Active; 93:Out → 132:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 94` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/kill` | 72:Out → 94:Succeeded; 191:True → 94:Succeeded; 94:Out → 144:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 97` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08` | 97:Out → 34:In; 102:Out → 97:Succeeded; 97:Out → 118:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 101` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info` | 121:Out1 → 101:Active; 101:Out → 175:In; 101:Out → 193:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 102` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info` | 102:Out → 97:Succeeded; 104:Out → 102:Succeeded |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 110` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues` | 144:False → 110:Active; 110:Out → 134:In; 110:Out → 154:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 112` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues` | 126:Out1 → 112:Succeeded; 112:Out → 120:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 114` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_shard` | 113:False → 114:Active; 114:Out → 148:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 116` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_shard` | 148:Out → 116:Succeeded; 116:Out → 121:In2 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 123` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_woman_shard` | 122:False → 123:Active; 123:Out → 124:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 125` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_woman_shard` | 125:Out → 121:In1; 124:Out → 125:Succeeded |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 150` (MappinManager) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues/cp` | 150:Out → 126:In1; 137:Out → 150:Inactive |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 151` (MappinManager) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues/arena` | 151:Out → 126:In2; 134:Out → 151:Inactive |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 157` (MappinManager) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues/arena_large` | 154:Out → 157:Inactive; 157:Out → 158:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 158` (MappinManager) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues/cp` | 158:Out → 137:In; 157:Out → 158:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 193` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info/contact` | 101:Out → 193:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 212` (Condition: holo_setup_active; holo_setup_started) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/search` | 212:False → 133:ma_bls_ina_se1_08_brief_in; 212:True → 195:In1; 213:Out → 212:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 215` (Condition) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info`; `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info` | 195:Out1 → 215:In; 215:False → 196:Active |
| `cyberpsycho_bugfixing.questphase / h0 / 14` (Journal) | `quests/minor_quest/ma_bls_ina_se1_08` | 13:Out → 14:Succeeded; 14:Out → 17:In7 |
| `ma_bls_ina_se1_08_quest_bugfixes.questphase / h52 / 8` (PauseCondition) | `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08` | 2:Out → 8:In; 8:Out → 4:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 133` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene`; `#ma_sm_bls_ina_se1_08_holocall` | 133:ma_bls_ina_se1_08_brief_out → 76:In; 212:False → 133:ma_bls_ina_se1_08_brief_in; 133:rejected_out → 196:Active; 133:Holocall INT → 186:In; 133:Holocall RET → 185:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_minor_activities.questphase` / h0 / 83 | `ma_bls_ina_se1_08_phase.questphase` | 175: PauseCondition: ow_psychos_intro_done; 175:Out → 83:In1 |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 133 | `ma_bls_ina_se1_08_holocall.scene` | 212: Condition: holo_setup_active; holo_setup_started; 133:ma_bls_ina_se1_08_brief_out → 76:In; 212:False → 133:ma_bls_ina_se1_08_brief_in; 133:rejected_out → 196:Active; 133:Holocall INT → 186:In; 133:Holocall RET → 185:In |
| `base\quest\bugfixing\additional_content_bugfixing.questphase` / h0 / 16 | `cyberpsycho_bugfixing.questphase` | 18: DeletionMarker; 18:Out → 16:In1 |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 3 | `ma_bls_ina_se1_08_quest_bugfixes.questphase` | 19: LogicalHub; 19:Out1 → 3:In1 |
| `base\open_world\minor_activities\badlands\badlands_minor_activities.questphase` / h0 / 6 | `ma_bls_ina_se1_minor_activities.questphase` | 9: PauseCondition: sts_bls_ina_tier_1; 9:Out → 6:In1 |
| `base\quest\bugfixing.questphase` / h0 / 19 | `additional_content_bugfixing.questphase` | 18: DeletionMarker; 18:Out → 19:In1 |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\open_world\minor_activities\open_world_minor_activities.questphase` / h0 / 6 | `badlands_minor_activities.questphase` | 37: LogicalHub; 37:Out1 → 6:In1 |
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
| `base\open_world\community\badlands\inland_avenue\bad_ina_quest.quest` / h0 / 9 | `open_world_minor_activities.questphase` |  |
| `base\open_world\phases\open_world_content.questphase` / h0 / 11 | `open_world_minor_activities.questphase` | 0: Input; 122: Input; 0:Out → 11:In1; 122:Out → 11:In1 |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 6 | `open_world_minor_activities.questphase` | 0: Start; 0:Out → 6:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
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
| `ma_bls_ina_se1_08_holocall.scene` | ma_bls_ina_se1_08_brief_in → ma_bls_ina_se1_08_brief_out, rejected_out | Regina; V; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-12345` | ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-684639` | ma_bls_ina_se1_08_quest_bugfixes.questphase / h52 / 2 | No reader in selected context |
| `glossary_cyberpsychosis` | ma_bls_ina_se1_08_phase.questphase / h0 / 77 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | ma_bls_ina_se1_08_holocall.scene / scene / 414 |
| `holo_reggie_calls_v_end_activate` | ma_bls_ina_se1_08_holocall.scene / scene / 379; ma_bls_ina_se1_08_phase.questphase / h0 / 186 | No reader in selected context |
| `holo_reggie_calls_v_end_done` | ma_bls_ina_se1_08_holocall.scene / scene / 375 | ma_bls_ina_se1_08_holocall.scene / scene / 374 |
| `holo_reggie_calls_v_rejectable` | ma_bls_ina_se1_08_holocall.scene / scene / 395; ma_bls_ina_se1_08_holocall.scene / scene / 412 | No reader in selected context |
| `holo_reggie_calls_v_rejected` | ma_bls_ina_se1_08_holocall.scene / scene / 403 | ma_bls_ina_se1_08_holocall.scene / scene / 401 |
| `holo_reggie_calls_v_start_activate` | ma_bls_ina_se1_08_holocall.scene / scene / 378; ma_bls_ina_se1_08_holocall.scene / scene / 410; ma_bls_ina_se1_08_phase.questphase / h0 / 185 | No reader in selected context |
| `holo_reggie_calls_v_start_done` | ma_bls_ina_se1_08_holocall.scene / scene / 373 | ma_bls_ina_se1_08_holocall.scene / scene / 423 |
| `holo_setup_active` | Producer outside selected context | ma_bls_ina_se1_08_holocall.scene / scene / 414; ma_bls_ina_se1_08_phase.questphase / h0 / 212 |
| `holo_setup_started` | Producer outside selected context | ma_bls_ina_se1_08_holocall.scene / scene / 414; ma_bls_ina_se1_08_phase.questphase / h0 / 212 |
| `ma_bls_ina_se1_08_alerted` | ma_bls_ina_se1_08_phase.questphase / h641 / 2 | ma_bls_ina_se1_08_phase.questphase / h1214 / 11; ma_bls_ina_se1_08_phase.questphase / h332 / 159 |
| `ma_bls_ina_se1_08_finished` | ma_bls_ina_se1_08_phase.questphase / h0 / 36 | cyberpsycho_bugfixing.questphase / h0 / 13; ma_bls_ina_se1_08_phase.questphase / h1336 / 10 |
| `ma_bls_ina_se1_08_psycho_combat_started` | ma_bls_ina_se1_08_phase.questphase / h332 / 120 | ma_bls_ina_se1_08_phase.questphase / h1398 / 9 |
| `ma_hunt_for_psycho_tutorial` | ma_bls_ina_se1_08_phase.questphase / h0 / 44 | No reader in selected context |
| `ma_ina_se1_08_start` | ma_bls_ina_se1_08_phase.questphase / h0 / 43 | No reader in selected context |
| `ma_token` | ma_bls_ina_se1_08_phase.questphase / h0 / 34 | No reader in selected context |
| `ow_psychos_done` | ma_bls_ina_se1_08_phase.questphase / h0 / 188 | No reader in selected context |
| `ow_psychos_killed` | ma_bls_ina_se1_08_phase.questphase / h0 / 130 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | ma_bls_ina_se1_08_quest_bugfixes.questphase / h0 / 12 |

## Exact gates, joins and cancellation

<details><summary>96 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]}}}}` | 78:Out → 16:In; 190:Out1 → 16:In; 16:Out → 19:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterAttack_ConditionType","attackerRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"isTargetPlayer":true}}}` | 78:Out → 17:In; 190:Out1 → 17:In; 17:Out → 19:In2 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterAttack_ConditionType","attackerRef":{"$type":"gameEntityReference","reference":"#player"},"targetRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]}}}}` | 78:Out → 18:In; 190:Out1 → 18:In; 18:Out → 19:In3 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 19` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 16:Out → 19:In1; 17:Out → 19:In2; 18:Out → 19:In3; 25:Out → 19:In4; 19:Out1 → 77:In; 19:Out1 → 92:Succeeded |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 93:Out → 22:In; 22:Out → 130:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]}}}}` | 25:Out → 19:In4; 78:Out → 25:In; 190:Out1 → 25:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"},"unconscious":false,"defeated":false}}}` | 36:Out → 28:In; 28:True → 29:In; 28:False → 30:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 76` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 76:Out → 75:Active; 133:ma_bls_ina_se1_08_brief_out → 76:In; 196:Out → 76:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_bls_ina_se1_08/01_ch_info/01_ch_info","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 98:Out → 100:In; 100:Out → 99:Active; 178:CutSource → 100:CutDestination |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"93268646650","value":false}},{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"85882596286","value":false}},{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"87833202724","value":false}}]}}` | 140:Out1 → 103:In; 103:Out → 104:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 104` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 104:Out → 102:Succeeded; 103:Out → 104:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 113` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_01","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 120:Out2 → 113:In; 113:True → 121:In2; 113:False → 114:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 121` | `questLogicalAndNodeDefinition` `{}` | 121:Out1 → 101:Active; 113:True → 121:In2; 116:Out → 121:In2; 122:True → 121:In1; 125:Out → 121:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 122` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_02","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 120:Out1 → 122:In; 122:True → 121:In1; 122:False → 123:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_02","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 123:Out → 124:In; 124:Out → 125:Succeeded |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 126` | `questLogicalAndNodeDefinition` `{}` | 126:Out1 → 112:Succeeded; 150:Out → 126:In1; 151:Out → 126:In2 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 131` | `questLogicalXorNodeDefinition` `{}` | 131:Out1 → 4:In; 130:Out → 131:In2; 132:Out → 131:In1; 131:Out1 → 191:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 132` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"killed":false}}}` | 93:Out → 132:In; 132:Out → 131:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_02","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}}}` | 110:Out → 134:In; 134:Out → 151:Inactive |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 137` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_01","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}}}` | 158:Out → 137:In; 137:Out → 150:Inactive |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_bls_ina_se1_08/01_ch_info_lethal/01_ch_info_lethal","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 176:Out → 139:In; 139:Out → 141:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 140` | `questLogicalXorNodeDefinition` `{}` | 99:Out → 140:In2; 140:Out1 → 103:In; 141:Out → 140:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 144` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_01","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_02","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}}]}}` | 94:Out → 144:In; 144:False → 110:Active; 144:True → 120:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 148` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_01","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 114:Out → 148:In; 148:Out → 116:Succeeded |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 154` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"LessOrEqual"}}}` | 110:Out → 154:In; 154:Out → 157:Inactive |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 175` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 175:False → 98:Active; 101:Out → 175:In; 175:True → 176:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 177` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 98:Out → 177:In; 178:CutSource → 177:CutDestination; 180:CutSource → 177:CutDestination; 177:Out → 178:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 178` | `questCutControlNodeDefinition` `{}` | 178:CutSource → 98:CutDestination; 178:CutSource → 100:CutDestination; 178:CutSource → 177:CutDestination; 177:Out → 178:In; 178:Out → 179:Inactive; 178:Out → 181:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 180` | `questCutControlNodeDefinition` `{"permanent":true}` | 180:CutSource → 98:CutDestination; 99:Out → 180:In; 141:Out → 180:In; 180:CutSource → 176:CutDestination; 180:CutSource → 177:CutDestination |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 189` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questSaveLock_ConditionType"}}}` | 189:False → 78:In; 83:Out → 189:In; 189:True → 190:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 191` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questSaveLock_ConditionType"}}}` | 191:False → 72:In; 191:True → 94:Succeeded; 131:Out1 → 191:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 212` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started"}},{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","anyParent":true,"childIsPlayer":true}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType","isContentBlocked":true}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/search","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 212:False → 133:ma_bls_ina_se1_08_brief_in; 212:True → 195:In1; 213:Out → 212:In |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 215` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}]}}` | 195:Out1 → 215:In; 215:False → 196:Active |
| `ma_bls_ina_se1_08_phase.questphase / h0 / 216` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 216:Out → 44:In; 216:Out → 84:In1; 216:Out → 187:In1; 216:Out → 213:In; 217:Out → 216:In; 216:Out → 218:In |
| `ma_bls_ina_se1_08_phase.questphase / h170 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2:Out → 4:In; 4:Out → 8:In |
| `ma_bls_ina_se1_08_phase.questphase / h170 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_vehicle_01","names":["None"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 2:Out → 5:In; 5:Out → 6:In |
| `ma_bls_ina_se1_08_phase.questphase / h170 / 9` | `questLogicalAndNodeDefinition` `{}` | 9:Out1 → 1:In; 17:Out → 9:In1; 18:Out → 9:In2 |
| `ma_bls_ina_se1_08_phase.questphase / h170 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_vehicle_02","names":["None"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 7:Out → 19:In; 19:Out → 18:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 57:Out → 4:In; 86:Out → 57:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 86` | `questCutControlNodeDefinition` `{"permanent":true}` | 86:CutSource → 33:CutDestination; 86:CutSource → 82:CutDestination; 86:Out → 57:In; 161:Out → 86:In; 86:CutSource → 110:CutDestination |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_vehicle_01"},"childIsPlayer":true,"enterAnimationFinished":true,"role":"Driver"}}}` | 0:Out → 87:In; 87:Out → 126:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 98:Out2 → 93:In; 93:Out → 99:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 94` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"killed":false}}}` | 98:Out1 → 94:In; 94:Out → 99:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 96:Out → 91:In; 129:Out → 96:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_bls_ina_se1_08_garage_door"}}` | 0:Out → 100:In; 100:Out → 109:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#ma_bls_ina_08_dvc_garage_door","eventType":"Executed"}}}` | 104:Out → 103:In; 103:Out → 137:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 105` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 105:Out → 34:In; 105:Out → 43:In; 134:Out1 → 105:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":250}}}` | 107:Out → 30:In; 134:Out1 → 107:In; 107:Out → 161:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 125` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 125:Out → 95:In; 124:Out → 125:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 126` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpeed_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_vehicle_01"},"speed":10.0,"comparisonType":"CT_GREATER_EQUAL"}}}` | 87:Out → 126:In; 126:Out → 127:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 132` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0},"comparisonType":"LessOrEqual"}}}` | 0:Out → 132:In; 132:Out → 83:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 134` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 134:Out1 → 105:In; 134:Out1 → 107:In; 134:Out1 → 120:In; 137:Out → 134:In1; 136:Out → 134:In2; 160:Out → 134:In3; 134:Out1 → 138:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 135` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterAttack_ConditionType","attackerRef":{"$type":"gameEntityReference","reference":"#player"},"targetRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]}}}}` | 104:Out → 135:In; 137:CutSource → 135:CutDestination; 135:Out → 136:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 137` | `questCutControlNodeDefinition` `{}` | 103:Out → 137:In; 137:Out → 134:In1; 137:CutSource → 135:CutDestination; 137:CutSource → 159:CutDestination |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 140` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"isPlayer":false,"inverted":true}}}` | 140:Out → 113:In; 141:Out → 140:In |
| `ma_bls_ina_se1_08_phase.questphase / h332 / 159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_bls_ina_se1_08_alerted","value":1,"comparisonType":"Equal"}}}` | 104:Out → 159:In; 137:CutSource → 159:CutDestination; 159:Out → 160:In |
| `ma_bls_ina_se1_08_phase.questphase / h641 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#ma_bls_ina_se1_08_sec_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemAlerted"}}}` | 0:Out → 3:In; 3:Out → 4:In4 |
| `ma_bls_ina_se1_08_phase.questphase / h641 / 4` | `questLogicalXorNodeDefinition` `{"inputSocketCount":6}` | 4:Out1 → 2:In; 3:Out → 4:In4; 5:Out → 4:In1; 6:Out → 4:In2; 7:Out → 4:In3; 8:Out → 4:In5; 9:Out → 4:In6 |
| `ma_bls_ina_se1_08_phase.questphase / h641 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PuppetSubType","puppetRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"upperBodyState":0}}}}` | 0:Out → 5:In; 5:Out → 4:In1 |
| `ma_bls_ina_se1_08_phase.questphase / h641 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PuppetSubType","puppetRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["drone_01"]},"upperBodyState":0}}}}` | 0:Out → 6:In; 6:Out → 4:In2 |
| `ma_bls_ina_se1_08_phase.questphase / h641 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PuppetSubType","puppetRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["drone_02"]},"upperBodyState":0}}}}` | 0:Out → 7:In; 7:Out → 4:In3 |
| `ma_bls_ina_se1_08_phase.questphase / h641 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["drone_01"]}}}}` | 0:Out → 8:In; 8:Out → 4:In5 |
| `ma_bls_ina_se1_08_phase.questphase / h641 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["drone_02"]}}}}` | 0:Out → 9:In; 9:Out → 4:In6 |
| `ma_bls_ina_se1_08_phase.questphase / h928 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 0:Out → 2:In; 2:Out → 3:In |
| `ma_bls_ina_se1_08_phase.questphase / h928 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":1}}}` | 2:Out → 3:In; 3:Out → 4:In |
| `ma_bls_ina_se1_08_phase.questphase / h928 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 3:Out → 4:In; 4:Out → 5:In |
| `ma_bls_ina_se1_08_phase.questphase / h1214 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 7:Out → 3:In; 3:Out → 4:In |
| `ma_bls_ina_se1_08_phase.questphase / h1214 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:Out → 5:In; 5:Out → 6:In |
| `ma_bls_ina_se1_08_phase.questphase / h1214 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 5:Out → 6:In; 6:Out → 8:In |
| `ma_bls_ina_se1_08_phase.questphase / h1214 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 3:In; 8:Out → 7:In |
| `ma_bls_ina_se1_08_phase.questphase / h1214 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_bls_ina_se1_08_alerted"}}}` | 0:Out → 11:In; 11:Out → 1:In |
| `ma_bls_ina_se1_08_phase.questphase / h1273 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 7:Out → 3:In; 3:Out → 4:In |
| `ma_bls_ina_se1_08_phase.questphase / h1273 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:Out → 5:In; 5:Out → 6:In |
| `ma_bls_ina_se1_08_phase.questphase / h1273 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 5:Out → 6:In; 6:Out → 8:In |
| `ma_bls_ina_se1_08_phase.questphase / h1273 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 3:In; 8:Out → 7:In |
| `ma_bls_ina_se1_08_phase.questphase / h1273 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_bls_ina_se1_08_com","names":["psycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 13:In; 13:Out → 1:In |
| `ma_bls_ina_se1_08_phase.questphase / h1336 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 7:Out → 3:In; 3:Out → 4:In |
| `ma_bls_ina_se1_08_phase.questphase / h1336 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:Out → 5:In; 5:Out → 6:In |
| `ma_bls_ina_se1_08_phase.questphase / h1336 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 5:Out → 6:In; 6:Out → 8:In |
| `ma_bls_ina_se1_08_phase.questphase / h1336 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 3:In; 8:Out → 7:In |
| `ma_bls_ina_se1_08_phase.questphase / h1336 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_bls_ina_se1_08_finished"}}}` | 0:Out → 10:In; 10:Out → 1:In |
| `ma_bls_ina_se1_08_phase.questphase / h1398 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 7:Out → 3:In; 3:Out → 4:In |
| `ma_bls_ina_se1_08_phase.questphase / h1398 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 4:Out → 5:In; 5:Out → 6:In |
| `ma_bls_ina_se1_08_phase.questphase / h1398 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_bls_ina_se1_08_tr"}}` | 5:Out → 6:In; 6:Out → 8:In |
| `ma_bls_ina_se1_08_phase.questphase / h1398 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 3:In; 8:Out → 7:In |
| `ma_bls_ina_se1_08_phase.questphase / h1398 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_bls_ina_se1_08_psycho_combat_started"}}}` | 0:Out → 9:In; 9:Out → 1:In |
| `ma_bls_ina_se1_08_holocall.scene / scene / 374` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 374:0:0 → 375:0:1; 379:0:0 → 374:0:1 |
| `ma_bls_ina_se1_08_holocall.scene / scene / 401` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 378:0:0 → 401:0:1; 401:0:0 → 403:0:1 |
| `ma_bls_ina_se1_08_holocall.scene / scene / 408` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 372:666:0 → 408:0:1; 408:0:0 → 414:0:1; 428:1:0 → 408:0:0 |
| `ma_bls_ina_se1_08_holocall.scene / scene / 414` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 408:0:0 → 414:0:1; 414:0:0 → 412:0:1; 414:0:1 → 416:0:1; 416:0:0 → 414:0:1 |
| `ma_bls_ina_se1_08_holocall.scene / scene / 416` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 414:0:1 → 416:0:1; 416:0:0 → 414:0:1; 428:1:0 → 416:0:0 |
| `ma_bls_ina_se1_08_holocall.scene / scene / 423` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 372:666:0 → 423:0:1; 423:0:0 → 428:0:0 |
| `cyberpsycho_bugfixing.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_bls_ina_se1_08_finished","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 13:In; 13:Out → 14:Succeeded |
| `cyberpsycho_bugfixing.questphase / h0 / 17` | `questLogicalAndNodeDefinition` `{"inputSocketCount":8}` | 2:Out → 17:In1; 4:Out → 17:In2; 6:Out → 17:In3; 8:Out → 17:In4; 10:Out → 17:In5; 12:Out → 17:In6; 14:Out → 17:In7; 16:Out → 17:In8; 17:Out1 → 18:In |
| `ma_bls_ina_se1_08_quest_bugfixes.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 15:Out1 → 12:In |
| `ma_bls_ina_se1_08_quest_bugfixes.questphase / h52 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08","fileEntryIndex":2,"className":"gameJournalQuestPhase"},"state":"Active"}}}` | 2:Out → 8:In; 8:Out → 4:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | ma_bls_ina_se1_08_phase.questphase / h170 / 19; ma_bls_ina_se1_08_phase.questphase / h170 / 4; ma_bls_ina_se1_08_phase.questphase / h170 / 5 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | ma_bls_ina_se1_08_phase.questphase / h332 / 110; ma_bls_ina_se1_08_phase.questphase / h332 / 82 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | ma_bls_ina_se1_08_phase.questphase / h0 / 72; ma_bls_ina_se1_08_phase.questphase / h0 / 78 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `combat_control` | ma_bls_ina_se1_08_phase.questphase / h332 / 106; ma_bls_ina_se1_08_phase.questphase / h332 / 33; ma_bls_ina_se1_08_phase.questphase / h332 / 4; ma_bls_ina_se1_08_phase.questphase / h332 / 5 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | ma_bls_ina_se1_08_phase.questphase / h170 / 2; ma_bls_ina_se1_08_phase.questphase / h332 / 49; ma_bls_ina_se1_08_phase.questphase / h928 / 5 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | cyberpsycho_bugfixing.questphase / h0 / 13; ma_bls_ina_se1_08_holocall.scene / scene / 374; ma_bls_ina_se1_08_holocall.scene / scene / 401; ma_bls_ina_se1_08_holocall.scene / scene / 414; +7 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | ma_bls_ina_se1_08_phase.questphase / h0 / 218; ma_bls_ina_se1_08_phase.questphase / h0 / 219; ma_bls_ina_se1_08_phase.questphase / h0 / 4; ma_bls_ina_se1_08_phase.questphase / h170 / 12; +1 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | ma_bls_ina_se1_08_phase.questphase / h170 / 14; ma_bls_ina_se1_08_phase.questphase / h332 / 104; ma_bls_ina_se1_08_phase.questphase / h332 / 136; ma_bls_ina_se1_08_phase.questphase / h332 / 160; +4 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | ma_bls_ina_se1_08_phase.questphase / h641 / 3 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | ma_bls_ina_se1_08_phase.questphase / h928 / 3 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_read` | ma_bls_ina_se1_08_phase.questphase / h0 / 113; ma_bls_ina_se1_08_phase.questphase / h0 / 122; ma_bls_ina_se1_08_phase.questphase / h0 / 124; ma_bls_ina_se1_08_phase.questphase / h0 / 148 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | cyberpsycho_bugfixing.questphase / h0 / 14; ma_bls_ina_se1_08_phase.questphase / h0 / 101; ma_bls_ina_se1_08_phase.questphase / h0 / 102; ma_bls_ina_se1_08_phase.questphase / h0 / 110; +21 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | ma_bls_ina_se1_08_phase.questphase / h170 / 17 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `mount_state` | ma_bls_ina_se1_08_phase.questphase / h0 / 212; ma_bls_ina_se1_08_phase.questphase / h332 / 87 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | cyberpsycho_bugfixing.questphase / h0 / 17; ma_bls_ina_se1_08_phase.questphase / h0 / 121; ma_bls_ina_se1_08_phase.questphase / h0 / 126; ma_bls_ina_se1_08_phase.questphase / h170 / 9 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | ma_bls_ina_se1_08_holocall.scene / scene / 373; ma_bls_ina_se1_08_holocall.scene / scene / 375; ma_bls_ina_se1_08_holocall.scene / scene / 378; ma_bls_ina_se1_08_holocall.scene / scene / 379; +17 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | ma_bls_ina_se1_08_phase.questphase / h0 / 131; ma_bls_ina_se1_08_phase.questphase / h0 / 140; ma_bls_ina_se1_08_phase.questphase / h0 / 19; ma_bls_ina_se1_08_phase.questphase / h332 / 134; +1 locations in catalogue.json | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | ma_bls_ina_se1_08_holocall.scene / scene / 408; ma_bls_ina_se1_08_holocall.scene / scene / 416; ma_bls_ina_se1_08_phase.questphase / h0 / 104; ma_bls_ina_se1_08_phase.questphase / h0 / 76; +13 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | ma_bls_ina_se1_08_phase.questphase / h0 / 178; ma_bls_ina_se1_08_phase.questphase / h0 / 180; ma_bls_ina_se1_08_phase.questphase / h332 / 137; ma_bls_ina_se1_08_phase.questphase / h332 / 86 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | ma_bls_ina_se1_08_phase.questphase / h0 / 29; ma_bls_ina_se1_08_phase.questphase / h0 / 30 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `save_eligibility` | ma_bls_ina_se1_08_phase.questphase / h0 / 189; ma_bls_ina_se1_08_phase.questphase / h0 / 191 | save-lock predicate + fallback path → save eligibility branch. Separate blocked-save fallback from checkpoint creation and verify installed behavior. |
| `scan_evidence` | ma_bls_ina_se1_08_phase.questphase / h0 / 16 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | ma_bls_ina_se1_08_phase.questphase / h0 / 133 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | ma_bls_ina_se1_08_phase.questphase / h0 / 216; ma_bls_ina_se1_08_phase.questphase / h1214 / 3; ma_bls_ina_se1_08_phase.questphase / h1214 / 6; ma_bls_ina_se1_08_phase.questphase / h1273 / 3; +8 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | ma_bls_ina_se1_08_phase.questphase / h0 / 132; ma_bls_ina_se1_08_phase.questphase / h0 / 175; ma_bls_ina_se1_08_phase.questphase / h0 / 177; ma_bls_ina_se1_08_phase.questphase / h0 / 22; +4 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | ma_bls_ina_se1_08_phase.questphase / h170 / 18; ma_bls_ina_se1_08_phase.questphase / h170 / 6; ma_bls_ina_se1_08_phase.questphase / h170 / 7; ma_bls_ina_se1_08_phase.questphase / h332 / 124; +1 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` | content candidate; journal anchor | `base-ma-bls-ina-08` |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` | content candidate; forward dependency | `base-ma-bls-ina-08` |
| `base\quest\bugfixing\additional_content\cyberpsycho_bugfixing.questphase` | repair; journal anchor | `base-shared` |
| `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase` | repair; journal anchor | `base-ma-bls-ina-se1-08` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

171 repeated typed/socket path signatures in this selected graph context; 4 distinct direct resource identities; 11 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 34 -> 188 -> 36 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 379 -> 374 -> 375 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 377 -> 379 -> 374 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 374 -> 375 -> 2 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 373 -> 376 -> 4 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 4 -> 377 -> 379 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `a909c836470d2b0e7fbc` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1214 / 0 -> 11 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 395 -> 378 -> 401 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 1 -> 395 -> 378 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `bbf9efd740881cf31a37` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 423 -> 428 -> 408 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 412 -> 410 -> 399 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `fe9d2c1bdd2cebf30eb2` | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 376 -> 4 -> 377 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]; 0:0 -> 0:0; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 74 | `h170` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 84 | `h332` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":99,"socketName":"Out1"}] |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h332 / 157 | `h641` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 118 | `h928` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 187 | `h1202` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1202 / 13 | `h1214` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1202 / 15 | `h1273` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1202 / 16 | `h1336` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1202 / 19 | `h1398` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase` / h0 / 16 | `h52` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\media\radio\scenes\radio_01_conspiracy.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\lipsync\en\ma_bls_ina_se1_08_holocall\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\lipsync\en\ma_bls_ina_se1_08_holocall\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_06\ma_hey_spr_06_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `glossary_cyberpsychosis` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 134; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 38; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 35; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase / h0 / 85; 19 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 212; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 125; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 243; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 306; 196 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 211; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 121; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 305; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 60; 75 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejectable` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 249; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 266; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 254; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 273; 103 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejected` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 251; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 256; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 256; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\scene\ma_cct_dtn_07_brief.scene / scene / 403; 64 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 124; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 264; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 242; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 63; 256 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 119; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 58; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 55; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\scene\ma_cct_dtn_07_brief.scene / scene / 373; 70 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `ma_hunt_for_psycho_tutorial` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 133; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 37; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 39; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase / h0 / 65; 15 total source locations in compressed evidence |
| `ma_token` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_01\ma_bls_ina_se1_01_phase.questphase / h0 / 31; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_02\ma_bls_ina_se1_02_phase.questphase / h0 / 18; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase / h0 / 21; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase / h0 / 38; 340 total source locations in compressed evidence |
| `ow_psychos_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 110; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 176; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 111; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase / h0 / 130; 16 total source locations in compressed evidence |
| `ow_psychos_killed` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 166; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 217; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 279; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 149; 19 total source locations in compressed evidence |

NodeRef uses: 103; TweakDB binding uses: 9. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` | 1 / 3 | scnDialogLineEvent: 3 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
