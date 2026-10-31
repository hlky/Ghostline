# Cyberpsycho Sighting: Seaside Cafe

Journal: `quests/minor_quest/ma_hey_spr_04` · `CyberPsycho` · hash `3642072802`.

Journal premise: Whoever killed them was packing a lot of hate, a lot of rage. And those feelings  don't fade quickly. Be careful.

**Coverage: journal-linked.** 22 exact journal-linked nodes in 1 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Read Regina's message in the cyberpsycho message thread. (Primary) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/check_message` |
| Find the cyberpsycho. (Primary) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/find_psycho` |
| Defeat the attacker. (Primary) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho` |
| Search the attacker. (Primary) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/loot_psycho` |
| Read the "Saigon Sisters: Season Finale" script. (Primary) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer` |
| Read the shard "Message to Linh Hyunh". (Primary) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer1` |
| Read the shard "Message to Dao Hyunh". (Primary) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_psycho` |
| Search the area to collect information. (Primary) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/search_clues` |
| Message Regina about Cyberpsycho Sighting: Seaside Cafe. (Primary) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `ma_hey_spr_04_phase.questphase / h0 / 47` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho` | 226:Out → 47:Active; 47:Out → 48:In |
| `ma_hey_spr_04_phase.questphase / h0 / 49` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho` | 136:Out1 → 49:Succeeded; 49:Out → 119:Active; 49:Out → 115:Active |
| `ma_hey_spr_04_phase.questphase / h0 / 54` (Journal) | `quests/minor_quest/ma_hey_spr_04` | 161:Out → 54:Succeeded; 54:Out → 63:In |
| `ma_hey_spr_04_phase.questphase / h0 / 115` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/search_clues` | 49:Out → 115:Active; 115:Out → 117:In; 115:Out → 152:In |
| `ma_hey_spr_04_phase.questphase / h0 / 119` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/loot_psycho` | 49:Out → 119:Active; 119:Out → 120:In |
| `ma_hey_spr_04_phase.questphase / h0 / 122` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/loot_psycho` | 120:Out → 122:Succeeded; 122:Out → 124:Active |
| `ma_hey_spr_04_phase.questphase / h0 / 124` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_psycho` | 122:Out → 124:Active; 124:Out → 123:In |
| `ma_hey_spr_04_phase.questphase / h0 / 125` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_psycho` | 123:Out → 125:Succeeded; 125:Out → 128:In1 |
| `ma_hey_spr_04_phase.questphase / h0 / 127` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer` | 117:Out → 127:Active; 127:Out → 159:In |
| `ma_hey_spr_04_phase.questphase / h0 / 129` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info` | 128:Out1 → 129:Active; 129:Out → 179:In; 129:Out → 269:In; 129:Out → 330:Active |
| `ma_hey_spr_04_phase.questphase / h0 / 153` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/search_clues` | 158:Out1 → 153:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 154` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer1` | 152:Out → 154:Active; 154:Out → 160:In |
| `ma_hey_spr_04_phase.questphase / h0 / 130` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer` | 130:Out → 128:In3; 159:Out → 130:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 156` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer1` | 156:Out → 128:In2; 160:Out → 156:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 161` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info` | 161:Out → 54:Succeeded; 189:Out1 → 161:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 224` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/find_psycho` | 363:False → 224:Active; 224:Out → 225:Active |
| `ma_hey_spr_04_phase.questphase / h0 / 225` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_decription` | 225:Out → 114:In1; 224:Out → 225:Active |
| `ma_hey_spr_04_phase.questphase / h0 / 226` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/find_psycho` | 226:Out → 47:Active; 109:Out1 → 226:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 330` (Journal) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info/reggie` | 129:Out → 330:Active |
| `ma_hey_spr_04_phase.questphase / h0 / 363` (Condition) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho`; `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho` | 99:Out → 363:In; 363:True → 114:In1; 363:False → 224:Active |
| `ma_hey_spr_04_phase.questphase / h0 / 390` (Condition: holo_setup_active; holo_setup_started) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho`; `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho` | 390:False → 185:Start 0; 358:Out1 → 390:In; 390:True → 362:In1 |
| `ma_hey_spr_04_phase.questphase / h0 / 392` (Condition) | `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info`; `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info` | 362:Out1 → 392:In; 392:False → 370:Active; 392:True → 393:Inactive |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `ma_hey_spr_04_phase.questphase / h0 / 162` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene`; `#may_sm_hey_spr_04_01_exposition` | 163:Out → 162:spawn_johnny_in; 164:Out1 → 162:lookats_in |
| `ma_hey_spr_04_phase.questphase / h0 / 185` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene`; `#ma_sm_hey_spr_04_01a_briefing` | 390:False → 185:Start 0; 185:rejected_out → 370:Active; 185:End 0 → 361:In1; 185:Holocall INT → 283:In; 185:Holocall RET → 282:In |
| `ma_hey_spr_04_phase.questphase / h0 / 207` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene`; `#may_sm_hey_spr_04_01_exposition` | 206:Out → 207:knockback |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest` / h0 / 0 | `ma_hey_spr_04_phase.questphase` | 0:Out1 → 3:In |
| `base\open_world\minor_activities\heywood\wellsprings\wellsprings_minor_activities.questphase` / h0 / 5 | `ma_hey_spr_04_phase.questphase` | 62: Journal; 62:Out → 5:In1 |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 185 | `ma_hey_spr_04_01a_briefing.scene` | 390: Condition: holo_setup_active; holo_setup_started; 390:False → 185:Start 0; 185:rejected_out → 370:Active; 185:End 0 → 361:In1; 185:Holocall INT → 283:In; 185:Holocall RET → 282:In |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 162 | `may_hey_spr_04_01_exposition.scene` | 163: PauseCondition: #ma_hey_spr_04_tr_fight_old; 164: LogicalHub; 163:Out → 162:spawn_johnny_in; 164:Out1 → 162:lookats_in |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 207 | `may_hey_spr_04_01_exposition.scene` | 206: PauseCondition: #ma_hey_spr_tr_jump_landing; #ma_hey_spr_tr_jump_landing; 206:Out → 207:knockback |
| `base\open_world\minor_activities\open_world_minor_activities.questphase` / h0 / 16 | `wellsprings_minor_activities.questphase` | 37: LogicalHub; 37:Out1 → 16:In1 |
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
| `ma_hey_spr_04_01a_briefing.scene` | Start 0 → rejected_out, End 0 | regina; regina_holo; Player; 22 nodes / 25 edges |
| `may_hey_spr_04_01_exposition.scene` | knockback, spawn_johnny_in, lookats_in →  | johnny; onlooker01; onlooker02; onlooker03; onlooker04; onlooker05; onlooker06; onlooker07; onlooker08; cyberpsycho; Player; 14 nodes / 12 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `glossary_cyberpsychosis` | ma_hey_spr_04_phase.questphase / h0 / 92 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | ma_hey_spr_04_01a_briefing.scene / scene / 195 |
| `holo_reggie_calls_v_end_activate` | ma_hey_spr_04_01a_briefing.scene / scene / 165; ma_hey_spr_04_phase.questphase / h0 / 283 | No reader in selected context |
| `holo_reggie_calls_v_end_done` | ma_hey_spr_04_01a_briefing.scene / scene / 133 | ma_hey_spr_04_01a_briefing.scene / scene / 132 |
| `holo_reggie_calls_v_rejectable` | ma_hey_spr_04_01a_briefing.scene / scene / 170; ma_hey_spr_04_01a_briefing.scene / scene / 193 | No reader in selected context |
| `holo_reggie_calls_v_rejected` | ma_hey_spr_04_01a_briefing.scene / scene / 172 | ma_hey_spr_04_01a_briefing.scene / scene / 174 |
| `holo_reggie_calls_v_start_activate` | ma_hey_spr_04_01a_briefing.scene / scene / 164; ma_hey_spr_04_01a_briefing.scene / scene / 191; ma_hey_spr_04_phase.questphase / h0 / 282 | No reader in selected context |
| `holo_reggie_calls_v_start_done` | ma_hey_spr_04_01a_briefing.scene / scene / 128 | ma_hey_spr_04_01a_briefing.scene / scene / 183 |
| `holo_setup_active` | Producer outside selected context | ma_hey_spr_04_01a_briefing.scene / scene / 195; ma_hey_spr_04_phase.questphase / h0 / 390 |
| `holo_setup_started` | Producer outside selected context | ma_hey_spr_04_01a_briefing.scene / scene / 195; ma_hey_spr_04_phase.questphase / h0 / 390 |
| `ma_hey_spr_04_jumped` | ma_hey_spr_04_phase.questphase / h0 / 191 | No reader in selected context |
| `ma_hey_spr_04_signpost_alerted` | ma_hey_spr_04_phase.questphase / h0 / 329 | ma_hey_spr_04_phase.questphase / h1155 / 20; ma_hey_spr_04_phase.questphase / h1155 / 5 |
| `ma_hey_spr_04_signpost_combat` | ma_hey_spr_04_phase.questphase / h0 / 288 | ma_hey_spr_04_phase.questphase / h1155 / 13; ma_hey_spr_04_phase.questphase / h1155 / 20; ma_hey_spr_04_phase.questphase / h1155 / 29; ma_hey_spr_04_phase.questphase / h1155 / 5 |
| `ma_hey_spr_04_signpost_ended` | ma_hey_spr_04_phase.questphase / h0 / 290 | ma_hey_spr_04_phase.questphase / h1155 / 13; ma_hey_spr_04_phase.questphase / h1155 / 19; ma_hey_spr_04_phase.questphase / h1155 / 20; ma_hey_spr_04_phase.questphase / h1155 / 29; ma_hey_spr_04_phase.questphase / h1155 / 5 |
| `ma_hey_spr_04_signpost_start` | ma_hey_spr_04_phase.questphase / h1155 / 27 | ma_hey_spr_04_phase.questphase / h1155 / 13; ma_hey_spr_04_phase.questphase / h1155 / 5 |
| `ma_hey_spr_04_signpost_stop` | ma_hey_spr_04_phase.questphase / h0 / 287 | No reader in selected context |
| `ma_hunt_for_psycho_tutorial` | ma_hey_spr_04_phase.questphase / h0 / 198 | No reader in selected context |
| `ma_spr_04_active` | ma_hey_spr_04_phase.questphase / h0 / 102; ma_hey_spr_04_phase.questphase / h0 / 270; ma_hey_spr_04_phase.questphase / h0 / 88 | ma_hey_spr_04_phase.questphase / h0 / 333; ma_hey_spr_04_phase.questphase / h240 / 8 |
| `ma_spr_04_done` | ma_hey_spr_04_phase.questphase / h0 / 101 | No reader in selected context |
| `ma_spr_04_finished` | ma_hey_spr_04_phase.questphase / h0 / 75 | ma_hey_spr_04_phase.questphase / h1155 / 8 |
| `ma_spr_04_start` | ma_hey_spr_04_phase.questphase / h0 / 74 | No reader in selected context |
| `ma_token` | ma_hey_spr_04_phase.questphase / h0 / 78 | No reader in selected context |
| `ow_psychos_done` | ma_hey_spr_04_phase.questphase / h0 / 188 | No reader in selected context |
| `ow_psychos_killed` | ma_hey_spr_04_phase.questphase / h0 / 186 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>82 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `ma_hey_spr_04_phase.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_04_tr_fight"}}` | 107:Out1 → 43:In; 43:Out → 45:In6 |
| `ma_hey_spr_04_phase.questphase / h0 / 45` | `questLogicalXorNodeDefinition` `{"inputSocketCount":8}` | 43:Out → 45:In6; 247:Out → 45:In1; 246:Out → 45:In2; 50:Out → 45:In3; 374:Out → 45:In4; 200:Out → 45:In5; 85:Out → 45:In7; 376:Out → 45:In8; 45:Out1 → 109:In1; 45:Out1 → 294:In |
| `ma_hey_spr_04_phase.questphase / h0 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 47:Out → 48:In; 48:Out → 187:In; 48:Out → 136:In1; 48:Out → 290:In; 48:Out → 408:In |
| `ma_hey_spr_04_phase.questphase / h0 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 164:Out1 → 66:In; 66:Out → 210:In; 66:Out → 107:In1 |
| `ma_hey_spr_04_phase.questphase / h0 / 85` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]}}}}` | 85:Out → 45:In7; 107:Out1 → 85:In |
| `ma_hey_spr_04_phase.questphase / h0 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]}}}}` | 107:Out1 → 103:In; 103:Out → 105:In1 |
| `ma_hey_spr_04_phase.questphase / h0 / 104` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"onScreenTest":true}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"Less"}}]}}` | 107:Out1 → 104:In; 104:Out → 105:In2 |
| `ma_hey_spr_04_phase.questphase / h0 / 105` | `questLogicalXorNodeDefinition` `{}` | 103:Out → 105:In1; 104:Out → 105:In2; 105:Out1 → 109:In2 |
| `ma_hey_spr_04_phase.questphase / h0 / 109` | `questLogicalXorNodeDefinition` `{}` | 45:Out1 → 109:In1; 105:Out1 → 109:In2; 109:Out1 → 226:Succeeded; 109:Out1 → 301:In |
| `ma_hey_spr_04_phase.questphase / h0 / 117` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_04/onscreens/ma_hey_spr_04_shard_producer","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}}}` | 115:Out → 117:In; 117:Out → 127:Active; 117:Out → 158:In2 |
| `ma_hey_spr_04_phase.questphase / h0 / 120` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_04/onscreens/ma_hey_spr_04_shard_psycho","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}}}` | 119:Out → 120:In; 120:Out → 122:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 123` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_04/onscreens/ma_hey_spr_04_shard_psycho","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 124:Out → 123:In; 123:Out → 125:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 128` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 125:Out → 128:In1; 156:Out → 128:In2; 130:Out → 128:In3; 128:Out1 → 129:Active; 128:Out1 → 266:In1 |
| `ma_hey_spr_04_phase.questphase / h0 / 152` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_04/onscreens/ma_hey_spr_04_shard_sister","fileEntryIndex":7,"className":"gameJournalOnscreen"},"state":"Active"}}}` | 115:Out → 152:In; 152:Out → 154:Active; 152:Out → 158:In1 |
| `ma_hey_spr_04_phase.questphase / h0 / 158` | `questLogicalAndNodeDefinition` `{}` | 117:Out → 158:In2; 152:Out → 158:In1; 158:Out1 → 153:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_04/onscreens/ma_hey_spr_04_shard_producer","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 127:Out → 159:In; 159:Out → 130:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 160` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_04/onscreens/ma_hey_spr_04_shard_sister","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}}` | 154:Out → 160:In; 160:Out → 156:Succeeded |
| `ma_hey_spr_04_phase.questphase / h0 / 163` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_04_tr_fight_old"}}` | 163:Out → 162:spawn_johnny_in; 164:Out1 → 163:In; 163:Out → 329:In |
| `ma_hey_spr_04_phase.questphase / h0 / 172` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","minutes":10}}}` | 171:Out → 172:In; 172:Out → 173:In |
| `ma_hey_spr_04_phase.questphase / h0 / 174` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","minutes":7}}}` | 169:Out → 174:In; 174:Out → 175:In |
| `ma_hey_spr_04_phase.questphase / h0 / 177` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":20}}}` | 136:Out1 → 177:In; 177:Out → 169:In |
| `ma_hey_spr_04_phase.questphase / h0 / 179` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"},"unconscious":false,"defeated":false}}}` | 129:Out → 179:In; 179:True → 253:Active; 179:False → 255:In1 |
| `ma_hey_spr_04_phase.questphase / h0 / 187` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"},"unconscious":false,"defeated":false}}}` | 48:Out → 187:In; 187:Out → 186:In |
| `ma_hey_spr_04_phase.questphase / h0 / 200` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"eventType":"Finished"}}}` | 200:Out → 45:In5; 107:Out1 → 200:In |
| `ma_hey_spr_04_phase.questphase / h0 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"observedTargetRef":{"$type":"gameEntityReference","reference":"#player"},"isObservedTargetPlayer":false}}}` | 50:Out → 45:In3; 107:Out1 → 50:In |
| `ma_hey_spr_04_phase.questphase / h0 / 206` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_tr_jump_landing"},{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_tr_jump_landing","activatorRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isPlayerActivator":false}]}}` | 310:CutSource → 206:CutDestination; 208:Out1 → 206:In; 206:Out → 207:knockback |
| `ma_hey_spr_04_phase.questphase / h0 / 241` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isPlayer":false,"percent":65.0,"comparisonType":"LessOrEqual"}}}` | 297:Out → 241:In; 241:Out → 242:In; 241:Out → 274:In; 241:Out → 275:In |
| `ma_hey_spr_04_phase.questphase / h0 / 246` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isObservedTargetPlayer":false}}}` | 246:Out → 45:In2; 107:Out1 → 246:In |
| `ma_hey_spr_04_phase.questphase / h0 / 247` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questVision_ConditionType","observerPuppetRef":{"$type":"gameEntityReference","reference":"#player"},"observedTargetRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isObservedTargetPlayer":false}}}` | 247:Out → 45:In1; 107:Out1 → 247:In |
| `ma_hey_spr_04_phase.questphase / h0 / 259` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"},"unconscious":false,"defeated":false}}}` | 255:Out1 → 259:In; 259:Out → 257:Inactive; 261:CutSource → 259:CutDestination |
| `ma_hey_spr_04_phase.questphase / h0 / 261` | `questCutControlNodeDefinition` `{}` | 261:Out → 181:Active; 261:CutSource → 259:CutDestination; 264:Out → 261:In |
| `ma_hey_spr_04_phase.questphase / h0 / 264` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_hey_spr_04/03a_ch_alive/03a_ch_alive","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 254:Out → 264:In; 264:Out → 261:In |
| `ma_hey_spr_04_phase.questphase / h0 / 265` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/regina_jones/ma_hey_spr_04/03b_ch_dead/03b_ch_dead","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 265:Out → 184:Active; 253:Out → 265:In |
| `ma_hey_spr_04_phase.questphase / h0 / 267` | `questLogicalAndNodeDefinition` `{}` | 267:Out1 → 1:In; 84:Out → 267:In1; 178:Out1 → 267:In2 |
| `ma_hey_spr_04_phase.questphase / h0 / 269` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","minutes":1}}}` | 129:Out → 269:In; 269:Out → 270:In |
| `ma_hey_spr_04_phase.questphase / h0 / 275` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_04_roof_check","activatorRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isPlayerActivator":false}}` | 241:Out → 275:In; 275:Out → 276:In |
| `ma_hey_spr_04_phase.questphase / h0 / 276` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_04_ground_check","activatorRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isPlayerActivator":false}}` | 275:Out → 276:In; 276:Out → 277:In |
| `ma_hey_spr_04_phase.questphase / h0 / 297` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_tr_jump_landing","activatorRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isPlayerActivator":false}}` | 297:Out → 191:In; 230:Out → 297:In; 297:Out → 241:In; 297:Out → 288:In; 297:Out → 299:In; 297:Out → 309:In |
| `ma_hey_spr_04_phase.questphase / h0 / 309` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 297:Out → 309:In; 309:Out → 310:In |
| `ma_hey_spr_04_phase.questphase / h0 / 310` | `questCutControlNodeDefinition` `{}` | 310:CutSource → 206:CutDestination; 309:Out → 310:In |
| `ma_hey_spr_04_phase.questphase / h0 / 315` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isPlayer":false,"inverted":true}}}` | 315:Out → 273:In; 316:Out → 315:In |
| `ma_hey_spr_04_phase.questphase / h0 / 333` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_spr_04_active"}}}` | 333:Out → 94:In1; 333:Out → 171:In; 358:Out1 → 333:In |
| `ma_hey_spr_04_phase.questphase / h0 / 334` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_04_tr_start"}}` | 334:Out → 327:In1; 340:Out → 334:In |
| `ma_hey_spr_04_phase.questphase / h0 / 341` | `questLogicalXorNodeDefinition` `{}` | 341:Out1 → 91:In; 114:Out1 → 341:In1; 327:Out1 → 341:In2 |
| `ma_hey_spr_04_phase.questphase / h0 / 348` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_04_roof_check"}}` | 348:True → 343:In; 345:Out → 348:In; 349:Out → 348:In; 352:Out → 348:In; 348:False → 349:In |
| `ma_hey_spr_04_phase.questphase / h0 / 349` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 349:Out → 348:In; 348:False → 349:In |
| `ma_hey_spr_04_phase.questphase / h0 / 350` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_hey_spr_04_roof_check"}}` | 343:Success → 350:In; 350:True → 344:In; 351:Out → 350:In; 350:False → 351:In |
| `ma_hey_spr_04_phase.questphase / h0 / 351` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 351:Out → 350:In; 350:False → 351:In |
| `ma_hey_spr_04_phase.questphase / h0 / 352` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 344:Success → 352:In; 352:Out → 348:In |
| `ma_hey_spr_04_phase.questphase / h0 / 363` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 99:Out → 363:In; 363:True → 114:In1; 363:False → 224:Active |
| `ma_hey_spr_04_phase.questphase / h0 / 368` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isPlayer":false}}}` | 368:False → 51:In; 191:Out → 368:In |
| `ma_hey_spr_04_phase.questphase / h0 / 374` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterAim_ConditionType","preciseAiming":true,"targetRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]}}}}` | 374:Out → 45:In4; 375:Out → 374:In |
| `ma_hey_spr_04_phase.questphase / h0 / 376` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"type":"Hacked"}}}` | 376:Out → 45:In8; 375:Out → 376:In |
| `ma_hey_spr_04_phase.questphase / h0 / 390` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started"}},{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","anyParent":true,"childIsPlayer":true}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType","isContentBlocked":true}},{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}]}}` | 390:False → 185:Start 0; 358:Out1 → 390:In; 390:True → 362:In1 |
| `ma_hey_spr_04_phase.questphase / h0 / 392` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}]}}` | 362:Out1 → 392:In; 392:False → 370:Active; 392:True → 393:Inactive |
| `ma_hey_spr_04_phase.questphase / h240 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_04_tr_fight_big"}}` | 0:Out → 2:In; 7:Out → 2:In; 2:Out → 3:In |
| `ma_hey_spr_04_phase.questphase / h240 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 3:Out → 4:In; 4:Out → 5:In |
| `ma_hey_spr_04_phase.questphase / h240 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_hey_spr_04_tr_fight_big"}}` | 4:Out → 5:In; 5:Out → 7:In |
| `ma_hey_spr_04_phase.questphase / h240 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_spr_04_active","value":1,"comparisonType":"Less"}}}` | 0:Out → 8:In; 8:Out → 1:In |
| `ma_hey_spr_04_phase.questphase / h658 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":12}}}` | 5:Out → 6:In; 6:Out → 9:In |
| `ma_hey_spr_04_phase.questphase / h658 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_hey_spr_04_tr_start"}}` | 0:Out → 8:In; 8:Out → 5:In; 8:Out → 10:In |
| `ma_hey_spr_04_phase.questphase / h658 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_hey_spr_04_tr_start"}}` | 9:Out → 3:In; 6:Out → 9:In |
| `ma_hey_spr_04_phase.questphase / h827 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","seconds":5}}}` | 0:Out → 5:In; 5:Out → 3:In |
| `ma_hey_spr_04_phase.questphase / h827 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["onlooker_02"]},"timeInterval":4.0,"onScreenTest":true,"inverted":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["onlooker_02"]},"timeInterval":4.0,"onScreenTest":true,"inverted":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["onlooker_03"]},"timeInterval":4.0,"onScreenTest":true,"inverted":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["onlooker_04"]},"timeInterval":4.0,"onScreenTest":true,"inverted":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["onlooker_05"]},"timeInterval":4.0,"onScreenTest":true,"inverted":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["onlooker_06"]},"timeInterval":4.0,"onScreenTest":true,"inverted":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["onlooker_07"]},"timeInterval":4.0,"onScreenTest":true,"inverted":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["onlooker_08"]},"timeInterval":4.0,"onScreenTest":true,"inverted":true}}]}}` | 4:Out1 → 7:In; 7:Out → 6:In |
| `ma_hey_spr_04_phase.questphase / h1155 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_spr_04_finished"}}}` | 0:Out → 8:In; 8:Out → 1:In |
| `ma_hey_spr_04_phase.questphase / h1155 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#ma_hey_spr_04_tr_fight_big"},{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_start"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_combat"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_ended"}}]}]}}` | 17:False → 13:In; 43:Out → 13:In; 13:Out → 5:In |
| `ma_hey_spr_04_phase.questphase / h1155 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_hey_spr_04_tr_fight_big"}}` | 7:Out1 → 17:In; 17:False → 13:In; 27:Out → 17:In; 17:True → 18:In |
| `ma_hey_spr_04_phase.questphase / h1155 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_hey_spr_04_tr_fight_big"},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_ended"}}]}}` | 32:Out → 19:In; 19:Out → 21:In2 |
| `ma_hey_spr_04_phase.questphase / h1155 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_hey_spr_04_tr_fight_big"},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_combat"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_ended"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_alerted"}}]}}` | 30:Out → 20:In; 20:Out → 21:In4 |
| `ma_hey_spr_04_phase.questphase / h1155 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_hey_spr_04_tr_fight_big"}}` | 22:Out → 21:In1; 34:Out → 22:In |
| `ma_hey_spr_04_phase.questphase / h1155 / 5` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_ended"}},"socketId":2383873679},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_combat"}},"socketId":2027139936},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_alerted"}},"socketId":1645361688},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_start"}},"socketId":3598342417}]}` | 5:Case2383873679 → 4:In; 13:Out → 5:In; 5:Case2027139936 → 14:In; 5:Case3598342417 → 15:In; 5:Case1645361688 → 28:In |
| `ma_hey_spr_04_phase.questphase / h1155 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#ma_hey_spr_04_tr_fight_big"},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_ended"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ma_hey_spr_04_signpost_combat"}}]}}` | 29:Out → 21:In3; 39:Out → 29:In |
| `ma_hey_spr_04_phase.questphase / h1155 / 37` | `questLogicalXorNodeDefinition` `{}` | 37:Out1 → 36:In; 32:Out → 37:In1 |
| `ma_hey_spr_04_01a_briefing.scene / scene / 132` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 132:0:0 → 133:0:1; 156:0:0 → 132:0:1 |
| `ma_hey_spr_04_01a_briefing.scene / scene / 174` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 164:0:0 → 174:0:1; 174:0:0 → 172:0:1 |
| `ma_hey_spr_04_01a_briefing.scene / scene / 183` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 124:666:0 → 183:0:1; 183:0:0 → 186:0:0 |
| `ma_hey_spr_04_01a_briefing.scene / scene / 189` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 124:666:0 → 189:0:1; 186:1:0 → 189:0:0; 189:0:0 → 195:0:1 |
| `ma_hey_spr_04_01a_briefing.scene / scene / 195` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 189:0:0 → 195:0:1; 195:0:0 → 193:0:1; 195:0:1 → 197:0:1; 197:0:0 → 195:0:1 |
| `ma_hey_spr_04_01a_briefing.scene / scene / 197` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 186:1:0 → 197:0:0; 195:0:1 → 197:0:1; 197:0:0 → 195:0:1 |
| `may_hey_spr_04_01_exposition.scene / scene / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#ma_hey_spr_04_com","names":["cyberpsycho"]},"isPlayer":false}}}` | 8:0:0 → 38:0:0; 20:0:0 → 8:0:1 |
| `may_hey_spr_04_01_exposition.scene / scene / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_may_hey_spr_04_01_exposition_johnny"},"onScreenTest":true,"inverted":true}}}` | 10:0:0 → 12:0:1; 38:0:0 → 10:0:1 |
| `may_hey_spr_04_01_exposition.scene / scene / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_may_hey_spr_04_01_exposition_johnny"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"Less"}}}` | 20:0:0 → 34:0:1; 34:0:0 → 36:0:1; 38:1:0 → 34:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | ma_hey_spr_04_phase.questphase / h0 / 66 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | ma_hey_spr_04_phase.questphase / h0 / 274 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | ma_hey_spr_04_phase.questphase / h0 / 342; ma_hey_spr_04_phase.questphase / h0 / 84; ma_hey_spr_04_phase.questphase / h0 / 91 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `combat_control` | ma_hey_spr_04_phase.questphase / h0 / 239; ma_hey_spr_04_phase.questphase / h0 / 343; ma_hey_spr_04_phase.questphase / h0 / 344; ma_hey_spr_04_phase.questphase / h0 / 364; +3 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | ma_hey_spr_04_phase.questphase / h0 / 41; ma_hey_spr_04_phase.questphase / h658 / 2; ma_hey_spr_04_phase.questphase / h827 / 3; ma_hey_spr_04_phase.questphase / h827 / 6 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | ma_hey_spr_04_01a_briefing.scene / scene / 132; ma_hey_spr_04_01a_briefing.scene / scene / 174; ma_hey_spr_04_01a_briefing.scene / scene / 183; ma_hey_spr_04_01a_briefing.scene / scene / 195; +9 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | ma_hey_spr_04_phase.questphase / h0 / 271; ma_hey_spr_04_phase.questphase / h0 / 95; ma_hey_spr_04_phase.questphase / h240 / 3; ma_hey_spr_04_phase.questphase / h240 / 7 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | ma_hey_spr_04_phase.questphase / h0 / 398; ma_hey_spr_04_phase.questphase / h0 / 405; ma_hey_spr_04_phase.questphase / h0 / 406; ma_hey_spr_04_phase.questphase / h0 / 407; +7 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `elapsed_time` | ma_hey_spr_04_phase.questphase / h658 / 6; ma_hey_spr_04_phase.questphase / h827 / 5 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_read` | ma_hey_spr_04_phase.questphase / h0 / 123; ma_hey_spr_04_phase.questphase / h0 / 159; ma_hey_spr_04_phase.questphase / h0 / 160 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | ma_hey_spr_04_phase.questphase / h0 / 113; ma_hey_spr_04_phase.questphase / h0 / 115; ma_hey_spr_04_phase.questphase / h0 / 119; ma_hey_spr_04_phase.questphase / h0 / 122; +26 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | ma_hey_spr_04_phase.questphase / h0 / 210 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `mount_state` | ma_hey_spr_04_phase.questphase / h0 / 390 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | ma_hey_spr_04_phase.questphase / h0 / 128; ma_hey_spr_04_phase.questphase / h0 / 158; ma_hey_spr_04_phase.questphase / h0 / 267 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | ma_hey_spr_04_01a_briefing.scene / scene / 128; ma_hey_spr_04_01a_briefing.scene / scene / 133; ma_hey_spr_04_01a_briefing.scene / scene / 164; ma_hey_spr_04_01a_briefing.scene / scene / 165; +23 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | ma_hey_spr_04_phase.questphase / h0 / 105; ma_hey_spr_04_phase.questphase / h0 / 109; ma_hey_spr_04_phase.questphase / h0 / 341; ma_hey_spr_04_phase.questphase / h0 / 45; +1 locations in catalogue.json | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | ma_hey_spr_04_01a_briefing.scene / scene / 189; ma_hey_spr_04_01a_briefing.scene / scene / 197; ma_hey_spr_04_phase.questphase / h0 / 172; ma_hey_spr_04_phase.questphase / h0 / 174; +7 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | ma_hey_spr_04_phase.questphase / h0 / 261; ma_hey_spr_04_phase.questphase / h0 / 310 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | ma_hey_spr_04_phase.questphase / h0 / 63 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | ma_hey_spr_04_phase.questphase / h0 / 103; ma_hey_spr_04_phase.questphase / h0 / 200 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | ma_hey_spr_04_phase.questphase / h0 / 162; ma_hey_spr_04_phase.questphase / h0 / 185; ma_hey_spr_04_phase.questphase / h0 / 207 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | ma_hey_spr_04_phase.questphase / h0 / 163; ma_hey_spr_04_phase.questphase / h0 / 206; ma_hey_spr_04_phase.questphase / h0 / 275; ma_hey_spr_04_phase.questphase / h0 / 276; +15 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | ma_hey_spr_04_phase.questphase / h0 / 179; ma_hey_spr_04_phase.questphase / h0 / 187; ma_hey_spr_04_phase.questphase / h0 / 259; ma_hey_spr_04_phase.questphase / h0 / 48 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | ma_hey_spr_04_phase.questphase / h0 / 212; ma_hey_spr_04_phase.questphase / h0 / 213; ma_hey_spr_04_phase.questphase / h0 / 214 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `weather_scope` | ma_hey_spr_04_phase.questphase / h0 / 169; ma_hey_spr_04_phase.questphase / h0 / 171; ma_hey_spr_04_phase.questphase / h0 / 173; ma_hey_spr_04_phase.questphase / h0 / 175; +1 locations in catalogue.json | weather operation + named source + reset policy → weather request/reset dispatched. Completion follows the caller's full restoration sequence, not an early cleanup fact. |
| `workspot_performance` | ma_hey_spr_04_phase.questphase / h0 / 293; may_hey_spr_04_01_exposition.scene / scene / 12; may_hey_spr_04_01_exposition.scene / scene / 6 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | ma_hey_spr_04_phase.questphase / h0 / 165; ma_hey_spr_04_phase.questphase / h658 / 4 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` | content candidate; journal anchor | `base-ma-hey-spr-04` |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` | content candidate; forward dependency | `base-ma-hey-spr-04` |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene` | content candidate; forward dependency | `base-ma-hey-spr-04` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

196 repeated typed/socket path signatures in this selected graph context; 9 distinct direct resource identities; 4 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 75 -> 101 -> 102 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `598920ee48558917ab4e` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 91 -> 74 -> 92 | questCheckpointNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 164 -> 174 -> 172 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 132 -> 133 -> 2 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 128 -> 137 -> 29 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `a909c836470d2b0e7fbc` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h240 / 0 -> 8 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 170 -> 164 -> 174 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 1 -> 170 -> 164 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `bbf9efd740881cf31a37` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 183 -> 186 -> 189 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 193 -> 191 -> 176 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `3fe0ae98a8cf5496b004` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h240 / 7 -> 2 -> 3 | questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]; Out -> In; Out -> In |
| `eb252b7e42db30cea85d` | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h240 / 5 -> 7 -> 2 | questPauseConditionNodeDefinition[questTriggerCondition] -> questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 94 | `h240` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 178 | `h658` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 197 | `h827` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 285 | `h1155` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\animations\player\female\body\player_exploration.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\player\male\body\player_exploration.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\lipsync\en\ma_hey_spr_04_01a_briefing\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\lipsync\en\ma_hey_spr_04_01a_briefing\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\lipsync\en\may_hey_spr_04_01_exposition\civ_high_f_04_enus_50.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\lipsync\en\may_hey_spr_04_01_exposition\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\lipsync\en\may_hey_spr_04_01_exposition\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

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

NodeRef uses: 165; TweakDB binding uses: 13. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` | 1 / 4 | scnDialogLineEvent: 3; scnLookAtEvent: 1 |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene` | 4 / 11 | scnDialogLineEvent: 1; scnLookAtEvent: 9; scnPlaySkAnimEvent: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
