# Shape of a Pony

Journal: `quests/minor_quest/mws_se5_07` · `MinorQuest` · hash `1052046523`.

Journal premise: I dunno if I should be flattered or embarrassed. It's a fine line beween superfan and superpsycho. But only a gonk says no to a Porsche 911 Turbo (930) – and a convertible at that. Especially if it's already bought and paid for.

**Coverage: journal-linked.** 25 exact journal-linked nodes in 2 resources; 4 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Go the car's last known location. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` |
| Inspect the body for clues. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` |
| Read and reply to the message from Muamar. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` |
| Find the car. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective` |
| Defeat the Wraiths and recover the key. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective1` |
| Get in the car. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective2` |
| Text Muamar about recovering the car. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective3` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `ma_ina_south_bugfixing.questphase / h1100 / 2` (PauseCondition) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective`; `quests/minor_quest/mws_se5_07/mws_se5_07/corpse`; `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1`; `quests/minor_quest/mws_se5_07/mws_se5_07c/objective`; `quests/minor_quest/mws_se5_07/mws_se5_07c/objective1` | 0:Out → 2:In; 2:Out → 3:In |
| `mws_se5_07.questphase / h0 / 7` (Journal) | `quests/minor_quest/mws_se5_07` | 4:Out → 7:Active; 35:Out → 7:Active; 7:Out → 154:In |
| `mws_se5_07.questphase / h0 / 27` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` | 141:True → 27:Succeeded; 27:Out → 29:Active |
| `mws_se5_07.questphase / h0 / 28` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` | 28:Out → 8:Active; 28:Out → 10:In; 154:Out → 28:Active; 28:Out → 139:In; 28:Out → 147:In1 |
| `mws_se5_07.questphase / h0 / 29` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` | 27:Out → 29:Active; 29:Out → 50:In |
| `mws_se5_07.questphase / h0 / 52` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` | 50:Out → 52:Succeeded; 52:Out → 53:Active |
| `mws_se5_07.questphase / h0 / 53` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` | 52:Out → 53:Active; 53:Out → 54:In |
| `mws_se5_07.questphase / h0 / 55` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` | 54:Out → 55:Succeeded; 55:Out → 56:Active |
| `mws_se5_07.questphase / h0 / 56` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective` | 55:Out → 56:Active; 56:Out → 65:In |
| `mws_se5_07.questphase / h0 / 66` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective` | 65:Out → 66:Succeeded; 66:Out → 67:Active |
| `mws_se5_07.questphase / h0 / 67` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective1` | 67:Out → 62:In; 66:Out → 67:Active; 152:Out → 67:Active; 67:Out → 101:In |
| `mws_se5_07.questphase / h0 / 68` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective1` | 101:Out → 68:Succeeded; 68:Out → 104:Active |
| `mws_se5_07.questphase / h0 / 70` (Journal) | `quests/minor_quest/mws_se5_07` | 108:Out → 70:Succeeded; 70:Out → 155:In |
| `mws_se5_07.questphase / h0 / 104` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective2` | 68:Out → 104:Active; 104:Out → 103:In |
| `mws_se5_07.questphase / h0 / 105` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective2` | 105:Out → 58:In; 103:Out → 105:Succeeded |
| `mws_se5_07.questphase / h0 / 142` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` | 140:Out → 142:Inactive; 142:Out → 143:Inactive |
| `mws_se5_07.questphase / h0 / 143` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` | 142:Out → 143:Inactive; 143:Out → 144:Active |
| `mws_se5_07.questphase / h0 / 144` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` | 144:Out → 54:In; 143:Out → 144:Active |
| `mws_se5_07.questphase / h0 / 149` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` | 148:Out → 149:Inactive; 149:Out → 150:Inactive |
| `mws_se5_07.questphase / h0 / 150` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` | 149:Out → 150:Inactive; 150:Out → 151:Inactive |
| `mws_se5_07.questphase / h0 / 151` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` | 150:Out → 151:Inactive; 151:Out → 152:Inactive |
| `mws_se5_07.questphase / h0 / 152` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective` | 152:Out → 67:Active; 151:Out → 152:Inactive |
| `mws_se5_07.questphase / h0 / 174` (Journal) | `quests/minor_quest/mws_se5_07/description` | 8:Out → 174:Active; 174:Out → 24:Active |
| `mws_se5_07.questphase / h0 / 178` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective3` | 176:Out → 178:Active; 178:Out → 177:In |
| `mws_se5_07.questphase / h0 / 179` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective3` | 179:Out → 106:Active; 177:Out → 179:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mws_se5_07.questphase / h0 / 14` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene`; `#mws_sm_se5_07` | 13:Out → 14:Start 0 |
| `mws_se5_07.questphase / h0 / 16` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene`; `#mws_sm_se5_07_camp` | 15:Out → 16:Start 0 |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h3390 / 20 | `ma_ina_south_bugfixing.questphase` | 22: DeletionMarker; 22:Out → 20:In1 |
| `base\open_world\mini_world_stories\badlands\badlands_mini_world_stories.questphase` / h0 / 53 | `mws_se5_07.questphase` | 54: Condition; 54:True → 53:In1 |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.quest` / h0 / 2 | `mws_se5_07.questphase` | 1: Scene: mws_se5_07_chicken_test.scene; 1:End 0 → 2:In1 |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 14 | `mws_se5_07.scene` | 13: PauseCondition: #mws_se5_07_insvestigation; 13:Out → 14:Start 0 |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 16 | `mws_se5_07_camp.scene` | 15: PauseCondition: #mws_se5_07_tr_encounter; 15:Out → 16:Start 0 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\mini_world_stories\ow_mini_world_stories.questphase` / h0 / 2 | `badlands_mini_world_stories.questphase` | 13: LogicalHub; 13:Out1 → 2:In1 |
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
| `base\open_world\phases\open_world_content.questphase` / h0 / 93 | `ow_mini_world_stories.questphase` | 92: DeletionMarker; 92:Out → 93:In1; 93:SignalPickup → 101:In |
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
| `mws_se5_07.scene` | Start 0 → End 0 | Johnny; player; 10 nodes / 9 edges |
| `mws_se5_07_camp.scene` | Start 0 → End 0 | johnny; porsche_cabrio; player; 10 nodes / 9 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `mws_se5_07_done` | mws_se5_07.questphase / h0 / 155 | No reader in selected context |
| `mws_se5_07_objective_cut1` | mws_se5_07.questphase / h0 / 140 | mws_se5_07.questphase / h0 / 141 |
| `mws_se5_07_started` | mws_se5_07.questphase / h0 / 154 | No reader in selected context |
| `porsche_911_930_turbo_cabriolet_owned` | Producer outside selected context | mws_se5_07.questphase / h0 / 3 |
| `q101_enable_side_content` | Producer outside selected context | mws_se5_07.questphase / h0 / 200 |
| `wms_se5_07_debug` | Producer outside selected context | mws_se5_07.questphase / h0 / 33 |

## Exact gates, joins and cancellation

<details><summary>52 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `ma_ina_south_bugfixing.questphase / h1100 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"}}},{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mws_se5_07/mws_se5_07a/objective","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mws_se5_07/mws_se5_07/corpse","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mws_se5_07/mws_se5_07/corpse1","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mws_se5_07/mws_se5_07c/objective","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mws_se5_07/mws_se5_07c/objective1","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}]}]}}` | 0:Out → 2:In; 2:Out → 3:In |
| `mws_se5_07.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"porsche_911_930_turbo_cabriolet_owned","value":1,"comparisonType":"GreaterOrEqual"}}}` | 199:Out → 3:In; 3:Out → 9:In; 3:Out → 203:In |
| `mws_se5_07.questphase / h0 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 195:Out → 4:In; 4:Out → 7:Active |
| `mws_se5_07.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_insvestigation"}}` | 11:Out → 13:In; 13:Out → 14:Start 0 |
| `mws_se5_07.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_tr_encounter"}}` | 11:Out → 15:In; 15:Out → 12:In; 15:Out → 16:Start 0; 15:Out → 181:In |
| `mws_se5_07.questphase / h0 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_007"}}}}` | 11:Out → 19:In; 19:Out → 18:In |
| `mws_se5_07.questphase / h0 / 31` | `questCutControlNodeDefinition` `{}` | 139:Out → 31:In; 31:Out → 140:In; 31:CutSource → 50:CutDestination |
| `mws_se5_07.questphase / h0 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wms_se5_07_debug"}}}` | 44:Out → 33:In; 33:Out → 34:In |
| `mws_se5_07.questphase / h0 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 11:Out → 44:In; 44:Out → 33:In |
| `mws_se5_07.questphase / h0 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_b","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 24:Out → 48:In; 48:Out → 26:Active; 148:CutSource → 48:CutDestination |
| `mws_se5_07.questphase / h0 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_tr_corpse"}}` | 29:Out → 50:In; 31:CutSource → 50:CutDestination; 148:CutSource → 50:CutDestination; 50:Out → 52:Succeeded |
| `mws_se5_07.questphase / h0 / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"94462363387","comparisonType":"Greater"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se5/mws_se5_07/shards1/gps","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}]}}` | 53:Out → 54:In; 148:CutSource → 54:CutDestination; 144:Out → 54:In; 54:Out → 55:Succeeded; 54:Out → 175:In |
| `mws_se5_07.questphase / h0 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_combat"}}` | 56:Out → 65:In; 148:CutSource → 65:CutDestination; 65:Out → 66:Succeeded |
| `mws_se5_07.questphase / h0 / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_a","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 24:Out → 71:In; 71:Out → 26:Active; 148:CutSource → 71:CutDestination |
| `mws_se5_07.questphase / h0 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":75600},"end":{"$type":"GameTime","seconds":18000}}}}` | 80:Out → 17:In; 80:Out → 79:In; 93:Out1 → 80:In; 181:Out → 80:In; 80:Out → 82:In; 80:Out → 83:In; 80:Out → 84:In |
| `mws_se5_07.questphase / h0 / 81` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":18000},"end":{"$type":"GameTime","seconds":75600}}}}` | 17:Out → 81:In; 79:Out → 81:In; 83:Out → 81:In; 82:Out → 81:In; 84:Out → 81:In; 81:Out → 86:In; 81:Out → 87:In; 81:Out → 88:In; 81:Out → 89:In; 81:Out → 90:In |
| `mws_se5_07.questphase / h0 / 92` | `questLogicalXorNodeDefinition` `{}` | 86:Out → 92:In1; 87:Out → 92:In1; 88:Out → 92:In1; 89:Out → 92:In2; 90:Out → 92:In2; 92:Out1 → 93:In1 |
| `mws_se5_07.questphase / h0 / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":5,"comparisonType":"GreaterOrEqual"}}}}` | 12:Out → 97:In; 97:Out → 99:In; 97:Out → 156:In; 97:Out → 157:In; 97:Out → 162:In; 97:Out → 163:In; 97:Out → 164:In |
| `mws_se5_07.questphase / h0 / 101` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"124890420321","quantity":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community","names":["ganger1","ganger2","ganger3","ganger4","ganger5"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":5,"comparisonType":"GreaterOrEqual"}}}]}}` | 67:Out → 101:In; 101:Out → 68:Succeeded; 101:Out → 76:In |
| `mws_se5_07.questphase / h0 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"},"childIsPlayer":true,"enterAnimationFinished":true}}}` | 103:Out → 72:In; 104:Out → 103:In; 103:Out → 105:Succeeded; 103:Out → 116:In |
| `mws_se5_07.questphase / h0 / 110` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mws_se5_07_chase"}}` | 119:Out → 110:In; 110:Out → 123:In; 110:Out → 128:In |
| `mws_se5_07.questphase / h0 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"},"count":1,"comparisonType":"GreaterOrEqual"}}}` | 111:Out → 113:In; 113:Out → 115:In1 |
| `mws_se5_07.questphase / h0 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community","names":["chaser1","chaser2"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 112:Out → 114:In; 114:Out → 115:In2 |
| `mws_se5_07.questphase / h0 / 115` | `questLogicalAndNodeDefinition` `{}` | 113:Out → 115:In1; 114:Out → 115:In2; 115:Out1 → 117:In; 115:Out1 → 127:In |
| `mws_se5_07.questphase / h0 / 116` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"},"inverted":true}}}` | 103:Out → 116:In; 116:Out → 111:In; 116:Out → 112:In |
| `mws_se5_07.questphase / h0 / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":250.0}}},{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community","names":["chaser1","chaser2"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":2,"comparisonType":"GreaterOrEqual"}}},{"$type":"questVehicleCondition","type":{"$type":"questVehicleDestruction_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"},"destruction":90.0}}]}]}}` | 115:Out1 → 127:In; 127:Out → 129:In |
| `mws_se5_07.questphase / h0 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 110:Out → 128:In; 128:Out → 125:In |
| `mws_se5_07.questphase / h0 / 129` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"},"inverted":true}}}` | 127:Out → 129:In; 129:Out → 172:In |
| `mws_se5_07.questphase / h0 / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_tr_corpse"},{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/car_dealership/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_a","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded","inverted":true}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/car_dealership/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_b","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded","inverted":true}}]}]}}` | 28:Out → 139:In; 139:Out → 31:In; 148:CutSource → 139:CutDestination |
| `mws_se5_07.questphase / h0 / 141` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_se5_07_objective_cut1","comparisonType":"Equal"}}}` | 26:Out → 141:In; 141:True → 27:Succeeded |
| `mws_se5_07.questphase / h0 / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_combat"}}` | 147:Out1 → 146:In; 146:Out → 148:In |
| `mws_se5_07.questphase / h0 / 148` | `questCutControlNodeDefinition` `{}` | 148:CutSource → 48:CutDestination; 148:CutSource → 50:CutDestination; 148:CutSource → 54:CutDestination; 148:CutSource → 65:CutDestination; 148:CutSource → 71:CutDestination; 148:CutSource → 139:CutDestination; 146:Out → 148:In; 148:Out → 149:Inactive |
| `mws_se5_07.questphase / h0 / 153` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"}}}}` | 11:Out → 153:In; 153:Out → 204:In |
| `mws_se5_07.questphase / h0 / 168` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mws_se5_07_corpse"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":200.0}}}]}}` | 155:Out → 168:In; 168:Out → 165:In |
| `mws_se5_07.questphase / h0 / 171` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_007"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":200.0}}}]}}` | 155:Out → 171:In; 171:Out → 169:In |
| `mws_se5_07.questphase / h0 / 177` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_job_done/job_done","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 178:Out → 177:In; 177:Out → 179:Succeeded |
| `mws_se5_07.questphase / h0 / 181` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_car_search"}}` | 15:Out → 181:In; 181:Out → 80:In |
| `mws_se5_07.questphase / h0 / 184` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleName":"Vehicle.v_sport2_porsche_911turbo_cabrio_player"}}}` | 58:Out → 184:In; 187:Out → 184:In; 184:Out → 185:In |
| `mws_se5_07.questphase / h0 / 185` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"},"timeInterval":0.0,"onScreenTest":true}}}` | 184:Out → 185:In; 185:True → 187:In; 185:False → 186:In |
| `mws_se5_07.questphase / h0 / 186` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"},"childIsPlayer":true}}}` | 186:False → 183:In; 185:False → 186:In; 186:True → 187:In |
| `mws_se5_07.questphase / h0 / 190` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 190:Out1 → 131:In; 165:Out → 190:In3; 170:Out → 190:In2; 173:Out → 190:In4; 182:Out → 190:In1 |
| `mws_se5_07.questphase / h0 / 191` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_response/porsche_911_cabrio_message3_response_a","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 107:Out → 191:In; 191:Out → 180:Active |
| `mws_se5_07.questphase / h0 / 192` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_response/porsche_911_cabrio_message3_response_b","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 107:Out → 192:In; 192:Out → 180:Active |
| `mws_se5_07.questphase / h0 / 199` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 199:Out → 3:In; 200:Out → 199:In; 199:Out → 202:In |
| `mws_se5_07.questphase / h0 / 200` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content","value":1,"comparisonType":"GreaterOrEqual"}}}` | 196:Out → 200:In; 200:Out → 199:In |
| `mws_se5_07.questphase / h0 / 202` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":4}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 202:Out → 194:Active; 199:Out → 202:In; 203:CutSource → 202:CutDestination |
| `mws_se5_07.questphase / h0 / 203` | `questCutControlNodeDefinition` `{}` | 3:Out → 203:In; 203:CutSource → 202:CutDestination |
| `mws_se5_07.scene / scene / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_tr_corpse"}}` | 16:0:0 → 50:0:1; 50:0:0 → 6:0:0; 50:0:0 → 12:0:1 |
| `mws_se5_07.scene / scene / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"94462363387"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se5/mws_se5_07/shards1/gps","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}]},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]},"onScreenTest":true,"inverted":true}}]}}` | 44:0:0 → 54:0:1; 54:0:0 → 32:0:1 |
| `mws_se5_07_camp.scene / scene / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"},"childIsPlayer":true,"enterAnimationFinished":true}}}` | 8:0:0 → 12:0:1; 12:0:0 → 18:0:1 |
| `mws_se5_07_camp.scene / scene / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_near_car"}}` | 24:0:0 → 8:0:0; 48:0:0 → 24:0:1 |
| `mws_se5_07_camp.scene / scene / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"124890420321","quantity":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community","names":["ganger1","ganger2","ganger3","ganger4","ganger5"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":5,"comparisonType":"GreaterOrEqual"}}}]}}` | 1:0:0 → 48:0:1; 48:0:0 → 14:0:1; 48:0:0 → 24:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mws_se5_07.questphase / h0 / 114; mws_se5_07.questphase / h0 / 97 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `combat_control` | mws_se5_07.questphase / h0 / 126 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mws_se5_07.questphase / h0 / 112; mws_se5_07.questphase / h0 / 12; mws_se5_07.questphase / h0 / 170; mws_se5_07.questphase / h0 / 173 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mws_se5_07.questphase / h0 / 141; mws_se5_07.questphase / h0 / 200; mws_se5_07.questphase / h0 / 3; mws_se5_07.questphase / h0 / 33 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | mws_se5_07.questphase / h0 / 79; mws_se5_07.questphase / h0 / 82; mws_se5_07.questphase / h0 / 83; mws_se5_07.questphase / h0 / 84; +4 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | mws_se5_07.questphase / h0 / 17; mws_se5_07.questphase / h0 / 86 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | mws_se5_07.questphase / h0 / 168; mws_se5_07.questphase / h0 / 171; mws_se5_07.questphase / h0 / 202 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mws_se5_07.questphase / h0 / 101; mws_se5_07.questphase / h0 / 54; mws_se5_07.scene / scene / 54; mws_se5_07_camp.scene / scene / 48 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_read` | mws_se5_07.questphase / h0 / 54; mws_se5_07.scene / scene / 54 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | mws_se5_07.questphase / h0 / 104; mws_se5_07.questphase / h0 / 105; mws_se5_07.questphase / h0 / 106; mws_se5_07.questphase / h0 / 107; +29 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | mws_se5_07.questphase / h0 / 77 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `mount_state` | mws_se5_07.questphase / h0 / 103; mws_se5_07.questphase / h0 / 186; mws_se5_07_camp.scene / scene / 12 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | mws_se5_07.questphase / h0 / 115; mws_se5_07.questphase / h0 / 190 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mws_se5_07.questphase / h0 / 140; mws_se5_07.questphase / h0 / 154; mws_se5_07.questphase / h0 / 155 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mws_se5_07.questphase / h0 / 92 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mws_se5_07.questphase / h0 / 128; mws_se5_07.questphase / h0 / 4; mws_se5_07.questphase / h0 / 44 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mws_se5_07.questphase / h0 / 148; mws_se5_07.questphase / h0 / 203; mws_se5_07.questphase / h0 / 31 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mws_se5_07.questphase / h0 / 108 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mws_se5_07.questphase / h0 / 14; mws_se5_07.questphase / h0 / 16 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mws_se5_07.questphase / h0 / 110; mws_se5_07.questphase / h0 / 13; mws_se5_07.questphase / h0 / 139; mws_se5_07.questphase / h0 / 146; +6 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | mws_se5_07.questphase / h0 / 101; mws_se5_07.questphase / h0 / 127; mws_se5_07_camp.scene / scene / 48 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | ma_ina_south_bugfixing.questphase / h1100 / 3; mws_se5_07.questphase / h0 / 117; mws_se5_07.questphase / h0 / 119; mws_se5_07.questphase / h0 / 134; +9 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mws_se5_07.questphase / h0 / 156; mws_se5_07.questphase / h0 / 157; mws_se5_07.questphase / h0 / 162; mws_se5_07.questphase / h0 / 163; +3 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mws_se5_07.questphase / h0 / 10; mws_se5_07.questphase / h0 / 165 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\bugfixing\ma\ma_ina_south_bugfixing.questphase` | repair; journal anchor | `base-shared` |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` | content candidate; journal anchor | `base-mws-se5-07` |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene` | content candidate; forward dependency | `base-mws-se5-07` |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene` | content candidate; forward dependency | `base-mws-se5-07` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-se5-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-se5-07.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

81 repeated typed/socket path signatures in this selected graph context; 11 distinct direct resource identities; 0 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `4e9253a72e6b0134b8dd` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 50 -> 52 -> 53 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `cbae0fd3078e68426197` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 201 -> 196 -> 200 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `a53561b4c002bc02b58a` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 27 -> 29 -> 50 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> Active; Out -> In |
| `138cff49923a75e07348` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 29 -> 50 -> 52 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `8e1d2b6d16b0384b26b3` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 112 -> 114 -> 115 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam] -> questLogicalAndNodeDefinition; Out -> In; Out -> In2 |
| `7e7dbbc930b3717fd790` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 179 -> 106 -> 107 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `a36102ceee6fef729c5f` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 114 -> 115 -> 117 | questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam] -> questLogicalAndNodeDefinition -> questVehicleNodeDefinition[questAssignCharacter_NodeType]; Out -> In2; Out1 -> In |
| `9791d641ee7ee2d5b2e7` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene` / scene / 50 -> 6 -> 8 | questPauseConditionNodeDefinition[questTriggerCondition] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `3e6f03030764fcc75954` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 107 -> 191 -> 180 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Active |
| `b54739889d4d9a0745d2` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 106 -> 107 -> 191 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> Active; Out -> In |
| `956a18e11770fe167253` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 146 -> 148 -> 50 | questPauseConditionNodeDefinition[questTriggerCondition] -> questCutControlNodeDefinition -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; CutSource -> CutDestination |
| `b88f09756d5e86cc7c83` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 170 -> 190 -> 131 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questLogicalAndNodeDefinition -> questOutputNodeDefinition; Out -> In2; Out1 -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| No embedded handoff in resolved context | — | External calls remain in the main dossier |

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
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.gamedef` | content candidate | base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.quest |
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
| `base\open_world\police_system\police_system_test.gamedef` | content candidate | base\open_world\police_system\police_system_test.quest |
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
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_bench_lean0__lh_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q115\q115_00_johnny\body\q115_00_johnny__ma_johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\lipsync\en\mws_se5_07\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\lipsync\en\mws_se5_07\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\lipsync\en\mws_se5_07_camp\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\lipsync\en\mws_se5_07_camp\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\main_characters\johnny\ground\johnny__kneel_ground_lean_front__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_bench__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `porsche_911_930_turbo_cabriolet_owned` | base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_chicken_test.scene / scene / 39; 1 total source locations in compressed evidence |
| `q101_enable_side_content` | base\quest\minor_quests\mq025\mq025_psycho_brawl.quest / h0 / 14; base\quest\minor_quests\mq032\scenes\mq032_00_chicken_test_setup.scene / scene / 6; base\quest\minor_quests\mq048\mq048.questphase / h435 / 6; base\quest\minor_quests\mq049\mq049.quest / h0 / 5; 36 total source locations in compressed evidence |
| `wms_se5_07_debug` | base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_chicken_test.scene / scene / 49; 1 total source locations in compressed evidence |

NodeRef uses: 135; TweakDB binding uses: 11. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene` | 2 / 5 | scnDialogLineEvent: 1; scnOverridePhantomParamsEvent: 1; scnPlaySkAnimEvent: 1; scneventsSocket: 2 |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene` | 2 / 5 | scnDialogLineEvent: 1; scnLookAtEvent: 1; scnPlaySkAnimEvent: 1; scneventsSocket: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
