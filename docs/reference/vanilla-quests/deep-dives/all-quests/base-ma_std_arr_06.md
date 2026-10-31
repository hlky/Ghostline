# Cyberpsycho Sighting: Under the Bridge

Journal: `quests/minor_quest/ma_std_arr_06` · `CyberPsycho` · hash `1568141133`.

Journal premise: V, you don't have anywhere else to be? Only thing you'll stir up here is trouble. I'd beat it, but... you do you.

**Coverage: journal-linked.** 25 exact journal-linked nodes in 1 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Read Regina's message in the cyberpsycho message thread. (Primary) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/check_message` |
| Read the shard "Archived Conversation: Tamara Cosby and Tony Ludic". (Primary) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/check_shard` |
| Search the area to collect information. (Primary) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/clues` |
| Find the cyberpsycho. (Primary) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho` |
| Neutralize the threat. (Primary) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/kill_psycho` |
| Message Regina about Cyberpsycho Sighting: Under The Bridge (Primary) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `ma_std_arr_06_phase.questphase / h0 / 179` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_description` | 321:True → 179:Active; 179:Out → 190:In |
| `ma_std_arr_06_phase.questphase / h0 / 180` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/kill_psycho` | 184:Out → 180:Active; 180:Out → 182:In |
| `ma_std_arr_06_phase.questphase / h0 / 181` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/kill_psycho` | 138:Out → 181:Succeeded; 181:Out → 216:In |
| `ma_std_arr_06_phase.questphase / h0 / 184` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho` | 184:Out → 180:Active; 240:Out → 184:Succeeded |
| `ma_std_arr_06_phase.questphase / h0 / 186` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho` | 320:True → 186:Active; 186:Out → 321:In |
| `ma_std_arr_06_phase.questphase / h0 / 195` (Journal) | `quests/minor_quest/ma_std_arr_06` | 195:Out → 165:In; 228:Out → 195:Succeeded |
| `ma_std_arr_06_phase.questphase / h0 / 217` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/clues` | 216:False → 217:Active; 217:Out → 218:In; 217:Out → 236:In; 217:Out → 263:In; 217:Out → 265:In |
| `ma_std_arr_06_phase.questphase / h0 / 219` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/clues` | 231:Out1 → 219:Succeeded; 219:Out → 220:In |
| `ma_std_arr_06_phase.questphase / h0 / 221` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/check_shard` | 220:False → 221:Active; 221:Out → 222:In |
| `ma_std_arr_06_phase.questphase / h0 / 223` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/check_shard` | 222:Out → 223:Succeeded; 223:Out → 224:Active |
| `ma_std_arr_06_phase.questphase / h0 / 224` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info` | 220:True → 224:Active; 223:Out → 224:Active; 224:Out → 256:In; 224:Out → 292:Active |
| `ma_std_arr_06_phase.questphase / h0 / 228` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info` | 228:Out → 195:Succeeded; 235:Out → 228:Succeeded |
| `ma_std_arr_06_phase.questphase / h0 / 264` (MappinManager) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/clues/area` | 266:Out1 → 264:Inactive; 264:Out → 267:Active |
| `ma_std_arr_06_phase.questphase / h0 / 267` (MappinManager) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/clues/area1` | 264:Out → 267:Active |
| `ma_std_arr_06_phase.questphase / h0 / 292` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info/contact` | 224:Out → 292:Active |
| `ma_std_arr_06_phase.questphase / h0 / 310` (Condition: holo_setup_active; holo_setup_started) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho` | 310:False → 250:brief_call; 312:Out → 310:In; 310:True → 311:In |
| `ma_std_arr_06_phase.questphase / h0 / 311` (Condition) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info`; `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info` | 311:False → 306:In1; 310:True → 311:In |
| `ma_std_arr_06_phase.questphase / h0 / 316` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_description` | 317:Out → 316:Active |
| `ma_std_arr_06_phase.questphase / h0 / 317` (Journal) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho` | 317:Out → 316:Active; 318:Out → 317:Active |
| `ma_std_arr_06_phase.questphase / h0 / 320` (Condition) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho` | 320:True → 186:Active; 245:Out → 320:In; 319:False → 320:In; 320:False → 321:In |
| `ma_std_arr_06_phase.questphase / h0 / 321` (Condition) | `quests/minor_quest/ma_std_arr_06/ma_description` | 321:True → 179:Active; 186:Out → 321:In; 321:False → 190:In; 320:False → 321:In |
| `ma_std_arr_06_phase.questphase / h1075 / 8` (MappinManager) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho/turret_01` | 0:Out → 8:Active |
| `ma_std_arr_06_phase.questphase / h1075 / 9` (MappinManager) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho/turret_02` | 0:Out → 9:Active |
| `ma_std_arr_06_phase.questphase / h1075 / 10` (MappinManager) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho/turret_01` | 7:Out → 10:Inactive; 10:Out → 12:In2 |
| `ma_std_arr_06_phase.questphase / h1075 / 11` (MappinManager) | `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho/turret_02` | 7:Out → 11:Inactive; 11:Out → 12:In3 |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `ma_std_arr_06_phase.questphase / h0 / 250` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene`; `#ma_sm_std_arr_06_briefing` | 250:brief_call_end → 237:Active; 310:False → 250:brief_call; 250:rejected_out → 302:Active; 250:brief_call_end → 318:Inactive |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\arroyo_minor_activities.questphase` / h0 / 17 | `ma_std_arr_06_phase.questphase` | 62: PauseCondition: ow_psychos_intro_done; 62:Out → 17:In1 |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest` / h0 / 1 | `ma_std_arr_06_phase.questphase` |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 250 | `ma_std_arr_06_briefing.scene` | 310: Condition: holo_setup_active; holo_setup_started; 250:brief_call_end → 237:Active; 310:False → 250:brief_call; 250:rejected_out → 302:Active; 250:brief_call_end → 318:Inactive |
| `base\open_world\district_definitions\open_world_kabuki.quest` / h842 / 61 | `arroyo_minor_activities.questphase` | 0: Input; 0:Out → 61:In1 |
| `base\open_world\minor_activities\open_world_minor_activities.questphase` / h0 / 12 | `arroyo_minor_activities.questphase` | 37: LogicalHub; 37:Out1 → 12:In1 |
| `base\open_world\open_world_test.quest` / h851 / 61 | `arroyo_minor_activities.questphase` | 0: Input; 0:Out → 61:In1 |
| `base\open_world\community\badlands\inland_avenue\bad_ina_quest.quest` / h0 / 9 | `open_world_minor_activities.questphase` |  |
| `base\open_world\phases\open_world_content.questphase` / h0 / 11 | `open_world_minor_activities.questphase` | 0: Input; 122: Input; 0:Out → 11:In1; 122:Out → 11:In1 |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 6 | `open_world_minor_activities.questphase` | 0: Start; 0:Out → 6:In1 |
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
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `ma_std_arr_06_briefing.scene` | brief_call → brief_call_end, rejected_out | Regina; Player; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `glossary_cyberpsychosis` | ma_std_arr_06_phase.questphase / h0 / 234 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | ma_std_arr_06_briefing.scene / scene / 268 |
| `holo_reggie_calls_v_end_activate` | ma_std_arr_06_briefing.scene / scene / 125 | No reader in selected context |
| `holo_reggie_calls_v_end_done` | ma_std_arr_06_briefing.scene / scene / 121; ma_std_arr_06_phase.questphase / h0 / 279 | ma_std_arr_06_briefing.scene / scene / 120; ma_std_arr_06_phase.questphase / h0 / 278 |
| `holo_reggie_calls_v_rejectable` | ma_std_arr_06_briefing.scene / scene / 249; ma_std_arr_06_briefing.scene / scene / 266 | No reader in selected context |
| `holo_reggie_calls_v_rejected` | ma_std_arr_06_briefing.scene / scene / 251 | ma_std_arr_06_briefing.scene / scene / 253 |
| `holo_reggie_calls_v_start_activate` | ma_std_arr_06_briefing.scene / scene / 124; ma_std_arr_06_briefing.scene / scene / 264 | No reader in selected context |
| `holo_reggie_calls_v_start_done` | ma_std_arr_06_briefing.scene / scene / 119 | ma_std_arr_06_briefing.scene / scene / 277 |
| `holo_setup_active` | Producer outside selected context | ma_std_arr_06_briefing.scene / scene / 268; ma_std_arr_06_phase.questphase / h0 / 310 |
| `holo_setup_started` | Producer outside selected context | ma_std_arr_06_briefing.scene / scene / 268; ma_std_arr_06_phase.questphase / h0 / 310 |
| `ma_arr_06_finished` | ma_std_arr_06_phase.questphase / h0 / 199 | ma_std_arr_06_phase.questphase / h989 / 14 |
| `ma_arr_06_start` | ma_std_arr_06_phase.questphase / h0 / 238 | No reader in selected context |
| `ma_hunt_for_psycho_tutorial` | ma_std_arr_06_phase.questphase / h0 / 233 | No reader in selected context |
| `ma_std_arr_06_audio` | ma_std_arr_06_phase.questphase / h0 / 272; ma_std_arr_06_phase.questphase / h0 / 273; ma_std_arr_06_phase.questphase / h0 / 274 | ma_std_arr_06_phase.questphase / h989 / 10; ma_std_arr_06_phase.questphase / h989 / 9 |
| `ma_std_arr_06_psycho_killed` | ma_std_arr_06_phase.questphase / h0 / 255 | ma_std_arr_06_phase.questphase / h0 / 256 |
| `ma_token` | ma_std_arr_06_phase.questphase / h0 / 200 | No reader in selected context |
| `ow_psychos_done` | ma_std_arr_06_phase.questphase / h0 / 229 | No reader in selected context |
| `ow_psychos_killed` | ma_std_arr_06_phase.questphase / h0 / 253; ma_std_arr_06_phase.questphase / h0 / 285 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>74 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `ma_std_arr_06_phase.questphase / h0 / 182` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_com_psycho"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 180:Out → 182:In; 182:Out → 252:In; 182:Out → 270:In |
| `ma_std_arr_06_phase.questphase / h0 / 190` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_06_tr_psycho_attacks"}}` | 179:Out → 190:In; 321:False → 190:In; 190:Out → 276:In1; 190:Out → 291:In |
| `ma_std_arr_06_phase.questphase / h0 / 194` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_arr_06_tr_psycho_area"}}` | 208:Out1 → 194:In; 194:Out → 210:In2 |
| `ma_std_arr_06_phase.questphase / h0 / 210` | `questLogicalXorNodeDefinition` `{}` | 194:Out → 210:In2; 207:Out1 → 210:In1; 210:Out1 → 286:In |
| `ma_std_arr_06_phase.questphase / h0 / 216` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"134356299255","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 181:Out → 216:In; 216:True → 220:In; 216:False → 217:Active |
| `ma_std_arr_06_phase.questphase / h0 / 218` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"134356299255","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 217:Out → 218:In; 218:Out → 231:In1 |
| `ma_std_arr_06_phase.questphase / h0 / 220` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_06/onscreens/ma_std_arr_06_onscreen_02","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 216:True → 220:In; 219:Out → 220:In; 220:True → 224:Active; 220:False → 221:Active |
| `ma_std_arr_06_phase.questphase / h0 / 222` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_06/onscreens/ma_std_arr_06_onscreen_02","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 221:Out → 222:In; 222:Out → 223:Succeeded |
| `ma_std_arr_06_phase.questphase / h0 / 227` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_std_arr_06/01_ch_info/01_ch_info","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 225:Out → 227:In; 227:Out → 283:In |
| `ma_std_arr_06_phase.questphase / h0 / 230` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 203:Out → 230:In; 286:True → 230:In; 230:Out → 319:In |
| `ma_std_arr_06_phase.questphase / h0 / 231` | `questLogicalXorNodeDefinition` `{}` | 218:Out → 231:In1; 231:Out1 → 219:Succeeded; 236:Out → 231:In2 |
| `ma_std_arr_06_phase.questphase / h0 / 232` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_arr_06_tr_psycho_area"}}` | 208:Out1 → 232:In; 232:Out → 244:In1 |
| `ma_std_arr_06_phase.questphase / h0 / 235` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"93268646650","value":false}},{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"85882596286","value":false}},{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"87833202724","value":false}}]}}` | 226:Out → 235:In; 235:Out → 228:Succeeded; 258:Out → 235:In |
| `ma_std_arr_06_phase.questphase / h0 / 236` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_06/onscreens/ma_std_arr_06_onscreen_02","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}}}` | 217:Out → 236:In; 236:Out → 231:In2 |
| `ma_std_arr_06_phase.questphase / h0 / 240` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_com_psycho"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 240:Out → 184:Succeeded; 240:Out → 211:In1; 241:Out → 240:In; 240:Out → 269:In |
| `ma_std_arr_06_phase.questphase / h0 / 243` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_06_tr_hook_starts"}}` | 208:Out1 → 243:In; 243:Out → 244:In2 |
| `ma_std_arr_06_phase.questphase / h0 / 244` | `questLogicalXorNodeDefinition` `{}` | 232:Out → 244:In1; 244:Out1 → 233:In; 243:Out → 244:In2; 244:Out1 → 268:In; 244:Out1 → 294:In |
| `ma_std_arr_06_phase.questphase / h0 / 252` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_com_psycho"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 182:Out → 252:In; 252:True → 253:In; 252:False → 301:In |
| `ma_std_arr_06_phase.questphase / h0 / 256` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_std_arr_06_psycho_killed"}}}` | 224:Out → 256:In; 256:False → 225:Active; 256:True → 257:Active; 256:False → 281:In; 256:False → 284:In |
| `ma_std_arr_06_phase.questphase / h0 / 259` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_std_arr_06/01_ch_info/01_ch_info_killed","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 257:Out → 259:In; 259:Out → 258:Active |
| `ma_std_arr_06_phase.questphase / h0 / 263` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"136655354957","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 217:Out → 263:In; 263:Out → 266:In1 |
| `ma_std_arr_06_phase.questphase / h0 / 265` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_06/onscreens/ma_std_arr_06_onscreen_01","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}}}` | 217:Out → 265:In; 265:Out → 266:In2 |
| `ma_std_arr_06_phase.questphase / h0 / 266` | `questLogicalXorNodeDefinition` `{}` | 263:Out → 266:In1; 266:Out1 → 264:Inactive; 265:Out → 266:In2 |
| `ma_std_arr_06_phase.questphase / h0 / 278` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 278:Out → 279:In |
| `ma_std_arr_06_phase.questphase / h0 / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_com_psycho"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 256:False → 281:In; 283:CutSource → 281:CutDestination; 281:Out → 282:Inactive |
| `ma_std_arr_06_phase.questphase / h0 / 283` | `questCutControlNodeDefinition` `{}` | 283:Out → 226:Active; 227:Out → 283:In; 283:CutSource → 281:CutDestination |
| `ma_std_arr_06_phase.questphase / h0 / 284` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_com_psycho"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 256:False → 284:In; 284:Out → 285:In |
| `ma_std_arr_06_phase.questphase / h0 / 286` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questSaveLock_ConditionType"}}}` | 286:False → 203:In; 210:Out1 → 286:In; 286:True → 230:In |
| `ma_std_arr_06_phase.questphase / h0 / 287` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questSaveLock_ConditionType"}}}` | 287:False → 204:In; 297:Out → 287:In |
| `ma_std_arr_06_phase.questphase / h0 / 289` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 290:Out → 289:In; 289:Out → 298:In |
| `ma_std_arr_06_phase.questphase / h0 / 291` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 190:Out → 291:In; 291:Out → 241:In |
| `ma_std_arr_06_phase.questphase / h0 / 294` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 244:Out1 → 294:In; 294:Out → 275:In1 |
| `ma_std_arr_06_phase.questphase / h0 / 297` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_std_arr_06_tr_hook_starts"}}` | 297:Out → 153:In; 297:Out → 175:In1; 297:Out → 287:In; 298:Out → 297:In |
| `ma_std_arr_06_phase.questphase / h0 / 310` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started"}},{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","anyParent":true,"childIsPlayer":true}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType","isContentBlocked":true}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 310:False → 250:brief_call; 312:Out → 310:In; 310:True → 311:In |
| `ma_std_arr_06_phase.questphase / h0 / 311` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}]}}` | 311:False → 306:In1; 310:True → 311:In |
| `ma_std_arr_06_phase.questphase / h0 / 319` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"points_of_interest/minor_quests/ma_std_arr_06","fileEntryIndex":1,"className":"gameJournalPointOfInterestMappin"},"state":"Active"}}}` | 230:Out → 319:In; 319:True → 245:Inactive; 319:False → 320:In |
| `ma_std_arr_06_phase.questphase / h0 / 320` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Inactive"}}}` | 320:True → 186:Active; 245:Out → 320:In; 319:False → 320:In; 320:False → 321:In |
| `ma_std_arr_06_phase.questphase / h0 / 321` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_std_arr_06/ma_description","fileEntryIndex":2,"className":"gameJournalQuestDescription"},"state":"Inactive"}}}` | 321:True → 179:Active; 186:Out → 321:In; 321:False → 190:In; 320:False → 321:In |
| `ma_std_arr_06_phase.questphase / h75 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"$/03_night_city/#c_santo_domingo/arroyo/arr_cs_prefab4OUIGHQ/cs_cyberpsycho_disposal_openworld_prefabRCXRD7A/cs_tr_reset"},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"$/03_night_city/#c_santo_domingo/arroyo/arr_cs_prefab4OUIGHQ/cs_cyberpsycho_disposal_openworld_prefabRCXRD7A/cs_cyberpsycho_disposal_com","names":["investigator"]},"onScreenTest":true}}]}}` | 3:Out → 4:In; 4:Out → 5:In |
| `ma_std_arr_06_phase.questphase / h75 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":24}}}` | 4:Out → 5:In; 5:Out → 10:In |
| `ma_std_arr_06_phase.questphase / h75 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"$/03_night_city/#c_santo_domingo/arroyo/arr_cs_prefab4OUIGHQ/cs_cyberpsycho_disposal_openworld_prefabRCXRD7A/cs_tr_reset"}}` | 0:Out → 9:In; 9:Out → 2:In |
| `ma_std_arr_06_phase.questphase / h75 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"$/03_night_city/#c_santo_domingo/arroyo/arr_cs_prefab4OUIGHQ/cs_cyberpsycho_disposal_openworld_prefabRCXRD7A/cs_tr_reset"}}` | 5:Out → 10:In; 10:Out → 6:In |
| `ma_std_arr_06_phase.questphase / h75 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":3}}}` | 0:Out → 15:In; 15:Out → 16:In |
| `ma_std_arr_06_phase.questphase / h75 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"$/03_night_city/#c_santo_domingo/arroyo/arr_cs_prefab4OUIGHQ/cs_cyberpsycho_disposal_openworld_prefabRCXRD7A/cs_tr_reset"}}` | 16:Out → 6:In; 15:Out → 16:In |
| `ma_std_arr_06_phase.questphase / h75 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"$/03_night_city/#c_santo_domingo/arroyo/arr_cs_prefab4OUIGHQ/cs_cyberpsycho_disposal_openworld_prefabRCXRD7A/cs_cyberpsycho_disposal_com"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2:Out → 19:In; 19:Out → 18:In |
| `ma_std_arr_06_phase.questphase / h310 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_corpses_002"},"eventType":"Finished"}}}` | 0:Out → 2:In; 2:Out → 10:In2 |
| `ma_std_arr_06_phase.questphase / h310 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_corpses_003"},"eventType":"Finished"}}}` | 0:Out → 3:In; 3:Out → 10:In3 |
| `ma_std_arr_06_phase.questphase / h310 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_corpses_004"},"eventType":"Finished"}}}` | 0:Out → 4:In; 4:Out → 10:In4 |
| `ma_std_arr_06_phase.questphase / h310 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_corpses_005"},"eventType":"Finished"}}}` | 0:Out → 5:In; 5:Out → 10:In5 |
| `ma_std_arr_06_phase.questphase / h310 / 10` | `questLogicalXorNodeDefinition` `{"inputSocketCount":8}` | 2:Out → 10:In2; 3:Out → 10:In3; 4:Out → 10:In4; 5:Out → 10:In5; 33:Out → 10:In1; 34:Out → 10:In6; 35:Out → 10:In7; 31:Out → 10:In8; 10:Out1 → 32:In |
| `ma_std_arr_06_phase.questphase / h310 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_06/onscreens/ma_std_arr_06_onscreen_01","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 0:Out → 31:In; 31:Out → 10:In8 |
| `ma_std_arr_06_phase.questphase / h310 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 10:Out1 → 32:In; 32:Out → 13:In |
| `ma_std_arr_06_phase.questphase / h310 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_corpses_01"},"eventType":"Finished"}}}` | 0:Out → 33:In; 33:Out → 10:In1 |
| `ma_std_arr_06_phase.questphase / h310 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_corpses_006"},"eventType":"Finished"}}}` | 0:Out → 34:In; 34:Out → 10:In6 |
| `ma_std_arr_06_phase.questphase / h310 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_corpses_007"},"eventType":"Finished"}}}` | 0:Out → 35:In; 35:Out → 10:In7 |
| `ma_std_arr_06_phase.questphase / h412 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_com_homeless","names":["survival"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 41:Out → 35:In; 42:Out → 41:In |
| `ma_std_arr_06_phase.questphase / h477 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_arr_06_tr_psycho_area"}}` | 0:Out → 22:In; 22:Out → 24:In1 |
| `ma_std_arr_06_phase.questphase / h477 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_06_tr_hook_starts"}}` | 0:Out → 23:In; 23:Out → 24:In2 |
| `ma_std_arr_06_phase.questphase / h477 / 24` | `questLogicalXorNodeDefinition` `{}` | 22:Out → 24:In1; 23:Out → 24:In2; 24:Out1 → 25:In |
| `ma_std_arr_06_phase.questphase / h538 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_com_psycho"},"isPlayer":false,"percent":30.0,"comparisonType":"LessOrEqual"}}}` | 0:Out → 8:In; 8:Out → 9:In |
| `ma_std_arr_06_phase.questphase / h538 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_std_arr_06_com_psycho","names":["cyberpsycho"]},"isPlayer":false,"inverted":true}}}` | 39:Out → 13:In; 40:Out → 39:In |
| `ma_std_arr_06_phase.questphase / h989 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_std_arr_06_tr_audio"}}` | 0:Out → 3:In; 13:Out1 → 3:In; 3:Out → 6:In |
| `ma_std_arr_06_phase.questphase / h989 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_std_arr_06_tr_audio"}}` | 6:Out → 8:In; 8:Out → 9:In |
| `ma_std_arr_06_phase.questphase / h989 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_std_arr_06_audio","value":1,"comparisonType":"Equal"}}}` | 9:True → 4:In; 8:Out → 9:In; 9:False → 10:In |
| `ma_std_arr_06_phase.questphase / h989 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_std_arr_06_audio","value":3,"comparisonType":"Equal"}}}` | 4:Out → 10:In; 10:True → 5:In; 10:False → 7:In; 9:False → 10:In |
| `ma_std_arr_06_phase.questphase / h989 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_arr_06_finished"}}}` | 0:Out → 14:In; 14:Out → 15:In |
| `ma_std_arr_06_phase.questphase / h1075 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 7:Out → 2:In; 7:Out → 4:In; 13:Out → 7:In; 7:Out → 10:Inactive; 7:Out → 11:Inactive |
| `ma_std_arr_06_phase.questphase / h1075 / 12` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 12:Out1 → 1:In; 3:Out → 12:In1; 5:Out → 12:In4; 10:Out → 12:In2; 11:Out → 12:In3 |
| `ma_std_arr_06_briefing.scene / scene / 120` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 120:0:0 → 121:0:1; 125:0:0 → 120:0:1 |
| `ma_std_arr_06_briefing.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 124:0:0 → 253:0:1; 253:0:0 → 251:0:1 |
| `ma_std_arr_06_briefing.scene / scene / 262` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 118:666:0 → 262:0:1; 262:0:0 → 268:0:1; 280:1:0 → 262:0:0 |
| `ma_std_arr_06_briefing.scene / scene / 268` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 262:0:0 → 268:0:1; 268:0:0 → 266:0:1; 268:0:1 → 270:0:1; 270:0:0 → 268:0:1 |
| `ma_std_arr_06_briefing.scene / scene / 270` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 268:0:1 → 270:0:1; 270:0:0 → 268:0:1; 280:1:0 → 270:0:0 |
| `ma_std_arr_06_briefing.scene / scene / 277` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 118:666:0 → 277:0:1; 277:0:0 → 280:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | ma_std_arr_06_phase.questphase / h0 / 240; ma_std_arr_06_phase.questphase / h412 / 41; ma_std_arr_06_phase.questphase / h75 / 19 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | ma_std_arr_06_phase.questphase / h477 / 27 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | ma_std_arr_06_phase.questphase / h0 / 203; ma_std_arr_06_phase.questphase / h0 / 204 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `combat_control` | ma_std_arr_06_phase.questphase / h538 / 41 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | ma_std_arr_06_phase.questphase / h0 / 174; ma_std_arr_06_phase.questphase / h0 / 241; ma_std_arr_06_phase.questphase / h0 / 296; ma_std_arr_06_phase.questphase / h412 / 34; +3 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | ma_std_arr_06_briefing.scene / scene / 120; ma_std_arr_06_briefing.scene / scene / 253; ma_std_arr_06_briefing.scene / scene / 268; ma_std_arr_06_briefing.scene / scene / 277; +6 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | ma_std_arr_06_phase.questphase / h0 / 138; ma_std_arr_06_phase.questphase / h0 / 322; ma_std_arr_06_phase.questphase / h412 / 43 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | ma_std_arr_06_phase.questphase / h1075 / 2; ma_std_arr_06_phase.questphase / h1075 / 3; ma_std_arr_06_phase.questphase / h1075 / 4; ma_std_arr_06_phase.questphase / h1075 / 5 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | ma_std_arr_06_phase.questphase / h0 / 289; ma_std_arr_06_phase.questphase / h75 / 15; ma_std_arr_06_phase.questphase / h75 / 5 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | ma_std_arr_06_phase.questphase / h0 / 216; ma_std_arr_06_phase.questphase / h0 / 218; ma_std_arr_06_phase.questphase / h0 / 263 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_read` | ma_std_arr_06_phase.questphase / h0 / 220; ma_std_arr_06_phase.questphase / h0 / 222; ma_std_arr_06_phase.questphase / h310 / 31 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | ma_std_arr_06_phase.questphase / h0 / 165; ma_std_arr_06_phase.questphase / h0 / 166; ma_std_arr_06_phase.questphase / h0 / 179; ma_std_arr_06_phase.questphase / h0 / 180; +22 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | ma_std_arr_06_phase.questphase / h0 / 310 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | ma_std_arr_06_phase.questphase / h1075 / 12 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | ma_std_arr_06_briefing.scene / scene / 119; ma_std_arr_06_briefing.scene / scene / 121; ma_std_arr_06_briefing.scene / scene / 124; ma_std_arr_06_briefing.scene / scene / 125; +17 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | ma_std_arr_06_phase.questphase / h0 / 210; ma_std_arr_06_phase.questphase / h0 / 231; ma_std_arr_06_phase.questphase / h0 / 244; ma_std_arr_06_phase.questphase / h0 / 266; +2 locations in catalogue.json | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | ma_std_arr_06_briefing.scene / scene / 262; ma_std_arr_06_briefing.scene / scene / 270; ma_std_arr_06_phase.questphase / h0 / 230; ma_std_arr_06_phase.questphase / h0 / 291; +3 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | ma_std_arr_06_phase.questphase / h0 / 283 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | ma_std_arr_06_phase.questphase / h0 / 158 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `save_eligibility` | ma_std_arr_06_phase.questphase / h0 / 286; ma_std_arr_06_phase.questphase / h0 / 287 | save-lock predicate + fallback path → save eligibility branch. Separate blocked-save fallback from checkpoint creation and verify installed behavior. |
| `scan_evidence` | ma_std_arr_06_phase.questphase / h310 / 2; ma_std_arr_06_phase.questphase / h310 / 3; ma_std_arr_06_phase.questphase / h310 / 33; ma_std_arr_06_phase.questphase / h310 / 34; +3 locations in catalogue.json | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | ma_std_arr_06_phase.questphase / h0 / 250 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | ma_std_arr_06_phase.questphase / h0 / 190; ma_std_arr_06_phase.questphase / h0 / 194; ma_std_arr_06_phase.questphase / h0 / 232; ma_std_arr_06_phase.questphase / h0 / 243; +9 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | ma_std_arr_06_phase.questphase / h0 / 182; ma_std_arr_06_phase.questphase / h0 / 252; ma_std_arr_06_phase.questphase / h0 / 281; ma_std_arr_06_phase.questphase / h0 / 284 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | ma_std_arr_06_phase.questphase / h75 / 18 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | ma_std_arr_06_phase.questphase / h477 / 29 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | ma_std_arr_06_phase.questphase / h0 / 153; ma_std_arr_06_phase.questphase / h0 / 249; ma_std_arr_06_phase.questphase / h412 / 37; ma_std_arr_06_phase.questphase / h412 / 38 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` | content candidate; journal anchor | `base-ma-std-arr-06` |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` | content candidate; forward dependency | `base-ma-std-arr-06` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

203 repeated typed/socket path signatures in this selected graph context; 3 distinct direct resource identities; 7 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `07baf99c782e2088a11d` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 297 -> 287 -> 204 | questPauseConditionNodeDefinition[questTriggerCondition] -> questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition] -> questCheckpointNodeDefinition; Out -> In; False -> In |
| `9af8a87f20a910659fa8` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 229 -> 199 -> 200 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 125 -> 120 -> 121 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 123 -> 125 -> 120 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 120 -> 121 -> 6 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 119 -> 122 -> 5 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 5 -> 123 -> 125 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `a909c836470d2b0e7fbc` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h989 / 0 -> 14 -> 15 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 249 -> 124 -> 253 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `ea4cb15199b9b3fa8e63` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h75 / 0 -> 15 -> 16 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `2beeeaa3b4da5300c035` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 4 -> 249 -> 124 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `bbf9efd740881cf31a37` | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 277 -> 280 -> 262 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 175 | `h75` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 207 | `h310` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 208 | `h412` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 209 | `h477` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 211 | `h538` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 275 | `h989` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":15,"socketName":"Out1"}] |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 276 | `h1075` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\lipsync\en\ma_std_arr_06_briefing\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\lipsync\en\ma_std_arr_06_briefing\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `glossary_cyberpsychosis` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 134; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 77; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 38; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 35; 19 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 212; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 125; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 186; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 379; 197 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 211; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 121; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 375; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 305; 74 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejectable` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 249; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 266; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 395; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 412; 103 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejected` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 251; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 403; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 256; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 256; 64 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 124; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 264; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 185; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 378; 257 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 119; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 373; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 58; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 55; 70 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `ma_hunt_for_psycho_tutorial` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 133; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 44; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 37; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 39; 15 total source locations in compressed evidence |
| `ma_token` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_01\ma_bls_ina_se1_01_phase.questphase / h0 / 31; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_02\ma_bls_ina_se1_02_phase.questphase / h0 / 18; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase / h0 / 21; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase / h0 / 38; 340 total source locations in compressed evidence |
| `ow_psychos_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 110; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 188; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 176; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase / h0 / 111; 16 total source locations in compressed evidence |
| `ow_psychos_killed` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 166; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 217; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 130; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 279; 18 total source locations in compressed evidence |

NodeRef uses: 76; TweakDB binding uses: 9. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` | 1 / 3 | scnDialogLineEvent: 3 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
