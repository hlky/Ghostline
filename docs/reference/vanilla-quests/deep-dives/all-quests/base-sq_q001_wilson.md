# The Gun

Journal: `quests/side_quest/sq_q001_wilson` · `SideQuest` · hash `3374603296`.

Journal premise: We've got this tradition in Heywood – on your sixteenth birthday your dad gives you a gun. I didn't get one, cuz I had a shitty dad. But you're way past your sixteenth, aren't ya? High time to get yourself a solid piece of iron.

**Coverage: journal-linked.** 44 exact journal-linked nodes in 5 resources; 5 resources in the inspected dependency context.

Resource roles in that context: 4 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Talk to Wilson. (Primary) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson` |
| Enter the shooting range. (Primary) | `quests/side_quest/sq_q001_wilson/wilson/03_enter_range` |
| Collect your gun from Wilson. (Primary) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `wat_lch_gunsmith_01.scene / scene / 209` (Journal) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` | 209:0:0 → 369:0:3; 430:0:0 → 209:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 363` (Journal) | `quests/side_quest/sq_q001_wilson` | 361:0:0 → 363:0:3; 363:0:0 → 650:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 365` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` | 356:0:0 → 365:0:1; 365:0:0 → 361:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `wat_lch_gunsmith_01.scene / scene / 369` (Journal) | `quests/side_quest/sq_q001_wilson` | 209:0:0 → 369:0:3; 369:0:0 → 212:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 373` (Journal) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson` | 149:0:0 → 373:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 377` (Journal) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson` | 377:0:0 → 378:0:1; 399:0:0 → 377:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 378` (Journal) | `quests/side_quest/sq_q001_wilson/wilson/03_enter_range` | 377:0:0 → 378:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 383` (Journal) | `quests/side_quest/sq_q001_wilson/wilson/03_enter_range` | 151:0:0 → 383:0:3; 383:0:0 → 385:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 385` (Journal) | `quests/side_quest/sq_q001_wilson` | 383:0:0 → 385:0:3; 385:0:0 → 412:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 387` (Journal) | `quests/side_quest/sq_q001_wilson/wilson/03_enter_range` | 387:0:0 → 199:0:1; 568:0:0 → 387:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 399` (Condition) | `quests/side_quest/sq_q001_wilson` | 147:0:0 → 399:0:1; 399:0:0 → 377:0:3; input mappings: 0:0=CutDestination, 0:1=In |
| `wat_lch_gunsmith_01.scene / scene / 405` (Journal) | `quests/side_quest/sq_q001_wilson` | 555:0:0 → 405:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `wat_lch_gunsmith_01.scene / scene / 415` (Journal) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` | 169:0:1 → 415:0:1; 415:0:0 → 579:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wat_lch_gunsmith_01.scene / scene / 579` (Journal) | `quests/side_quest/sq_q001_wilson/desc` | 415:0:0 → 579:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q001_quest_bugfixes.questphase / h669 / 8` (Condition) | `quests/side_quest/sq_q001_wilson` | 8:False → 1:In; 2:Out → 8:In; 8:True → 9:In |
| `default_dialogs.questphase / h7727 / 18` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` | 10:Out → 18:In; 18:True → 20:Inactive; 18:False → 19:In |
| `default_dialogs.questphase / h7727 / 19` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson` | 19:False → 15:In2; 18:False → 19:In; 19:True → 21:Inactive |
| `default_dialogs.questphase / h7727 / 20` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson/wilson_mp` | 18:True → 20:Inactive; 20:Out → 22:Active |
| `default_dialogs.questphase / h7727 / 21` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson/wilson` | 19:True → 21:Inactive; 21:Out → 23:Active |
| `default_dialogs.questphase / h7727 / 22` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson/wilson_static_mp_gun_gives` | 22:Out → 15:In1; 20:Out → 22:Active |
| `default_dialogs.questphase / h7727 / 23` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson/wilson_static_mp_gun_gives` | 23:Out → 15:In1; 21:Out → 23:Active |
| `default_dialogs.questphase / h7727 / 32` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` | 14:Out → 32:In; 32:True → 34:Inactive; 32:False → 33:In |
| `default_dialogs.questphase / h7727 / 33` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson` | 33:False → 31:In2; 32:False → 33:In; 33:True → 35:Inactive |
| `default_dialogs.questphase / h7727 / 34` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson/wilson_mp` | 32:True → 34:Inactive; 34:Out → 36:Active |
| `default_dialogs.questphase / h7727 / 35` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson/wilson` | 33:True → 35:Inactive; 35:Out → 37:Active |
| `default_dialogs.questphase / h7727 / 36` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson/wilson_static_mp_greets` | 36:Out → 31:In1; 34:Out → 36:Active |
| `default_dialogs.questphase / h7727 / 37` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson/wilson_static_mp_greets` | 37:Out → 31:In1; 35:Out → 37:Active |
| `default_dialogs.questphase / h7727 / 40` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` | 5:Out → 40:In; 40:True → 42:Inactive; 40:False → 41:In |
| `default_dialogs.questphase / h7727 / 41` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson` | 41:False → 39:In2; 40:False → 41:In; 41:True → 43:Inactive |
| `default_dialogs.questphase / h7727 / 42` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson/wilson_mp` | 40:True → 42:Inactive; 42:Out → 44:Active |
| `default_dialogs.questphase / h7727 / 43` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson/wilson` | 41:True → 43:Inactive; 43:Out → 45:Active |
| `default_dialogs.questphase / h7727 / 44` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson/wilson_static_mp_shop` | 44:Out → 39:In1; 42:Out → 44:Active |
| `default_dialogs.questphase / h7727 / 45` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson/wilson_static_mp_shop` | 45:Out → 39:In1; 43:Out → 45:Active |
| `default_dialogs.questphase / h7727 / 47` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` | 8:Out → 47:In; 47:True → 49:Inactive; 47:False → 48:In |
| `default_dialogs.questphase / h7727 / 48` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson` | 48:False → 9:In; 47:False → 48:In; 48:True → 50:Inactive |
| `default_dialogs.questphase / h7727 / 49` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson/wilson_mp` | 47:True → 49:Inactive; 49:Out → 51:Active |
| `default_dialogs.questphase / h7727 / 50` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson/wilson` | 48:True → 50:Inactive; 50:Out → 52:Active |
| `default_dialogs.questphase / h7727 / 51` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson/wilson_static_mp_shop` | 51:Out → 9:In; 49:Out → 51:Active |
| `default_dialogs.questphase / h7727 / 52` (MappinManager) | `quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson/wilson_static_mp_shop` | 52:Out → 9:In; 50:Out → 52:Active |
| `q001_wilson.questphase / h0 / 41` (Journal) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` | 61:Out → 41:Active; 41:Out → 50:Active |
| `q001_wilson.questphase / h0 / 50` (Journal) | `quests/side_quest/sq_q001_wilson/desc` | 41:Out → 50:Active; 50:Out → 65:In2 |
| `mq011.questphase / h163 / 93` (Condition) | `quests/side_quest/sq_q001_wilson/wilson/meet_wilson` | 73:Out → 93:In; 93:True → 95:Inactive |
| `mq011.questphase / h163 / 94` (Journal) | `quests/side_quest/sq_q001_wilson` | 96:Out1 → 94:Active |
| `mq011.questphase / h163 / 95` (Journal) | `quests/side_quest/sq_q001_wilson` | 93:True → 95:Inactive; 95:Out → 96:In2 |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\default_dialogs.questphase` / h7727 / 4 | `wat_lch_gunsmith_01.scene` | 56: CutControl; 53: PauseCondition; 56:CutSource → 4:CutDestination; 53:Out → 4:wilson_default_in |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h24 / 7 | `q001_quest_bugfixes.questphase` | 0: Input; 0:Out → 7:In1 |
| `base\open_world\district_definitions\open_world_kabuki.quest` / h0 / 16 | `default_dialogs.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 16:In1 |
| `base\open_world\open_world_test.quest` / h0 / 16 | `default_dialogs.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 16:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 22 | `default_dialogs.questphase` | 30: PauseCondition: q000_done; 36: Input; 30:Out → 22:In1; 36:Out → 22:EP1_Standalone |
| `base\quest\side_quests\sq012\sq012_the_law.quest` / h0 / 8 | `default_dialogs.questphase` |  |
| `base\quest\persistent_content.questphase` / h1469 / 9 | `q001_wilson.questphase` | 10: PauseCondition: q001_start_wilson_quest GreaterOrEqual 1; 24: LogicalHub; 10:Out → 9:In1; 24:Out1 → 9:EP1_Standalone |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 15 | `mq011.questphase` | 93: PauseCondition; 184: Condition: ep1_standalone Less 1; 93:Out → 15:In1; 184:False → 15:EP1_Standalone |
| `base\quest\minor_quests\mq011\mq011.quest` / h0 / 0 | `mq011.questphase` | 4: UIManager; 0:Out1 → 2:In; 4:Out → 0:chicken |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
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
| `base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.quest` / h0 / 10 | `persistent_content.questphase` | 0: Start; 0:Out → 10:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 17 | `persistent_content.questphase` | 0: Input; 36: Input; 0:Out → 17:In1; 36:Out → 17:EP1_Standalone |
| `base\quest\main_quests\part1\q108\q108_johnny.quest` / h0 / 24 | `persistent_content.questphase` | 0: Start; 0:Out → 24:In1 |
| `base\quest\minor_quests\mq025\batty\batty_quest.quest` / h0 / 3 | `persistent_content.questphase` | 0: Start; 0:Out → 3:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
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
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `wat_lch_gunsmith_01.scene` | wilson_default_in, backup_lines →  | wilson; v; 107 nodes / 120 edges |

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
| `ping_installed` | Producer outside selected context | q001_quest_bugfixes.questphase / h315 / 11; q001_quest_bugfixes.questphase / h315 / 22 |
| `q001_checked_stash` | Producer outside selected context | q001_quest_bugfixes.questphase / h139 / 28; q001_quest_bugfixes.questphase / h139 / 29; q001_quest_bugfixes.questphase / h139 / 8 |
| `q001_completed` | Producer outside selected context | q001_quest_bugfixes.questphase / h526 / 3 |
| `q001_e3_fog_hack` | q001_quest_bugfixes.questphase / h839 / 12 | No reader in selected context |
| `q001_jackie_on_mistys_chair` | q001_quest_bugfixes.questphase / h526 / 5 | No reader in selected context |
| `q001_just_after_rd_scene` | Producer outside selected context | q001_quest_bugfixes.questphase / h37 / 8 |
| `q001_mission0_complete` | Producer outside selected context | q001_quest_bugfixes.questphase / h565 / 3 |
| `q001_show_sts_tut` | q001_quest_bugfixes.questphase / h839 / 9 | q001_quest_bugfixes.questphase / h839 / 8 |
| `q001_spawn_wilson_attention` | q001_wilson.questphase / h0 / 66 | No reader in selected context |
| `q001_takedown_tutorial_failed` | q001_quest_bugfixes.questphase / h973 / 25 | No reader in selected context |
| `q001_tut_ap_hacked_netrunner` | Producer outside selected context | q001_quest_bugfixes.questphase / h315 / 17 |
| `q001_tut_equip_upload_part_done` | q001_quest_bugfixes.questphase / h315 / 20 | No reader in selected context |
| `q001_used_mb_elevator` | Producer outside selected context | q001_wilson.questphase / h0 / 52 |
| `q001_wilson_shop_tutorial_seen` | Producer outside selected context | q001_wilson.questphase / h0 / 53 |
| `q001_wilson_sms_tut` | q001_wilson.questphase / h0 / 56 | No reader in selected context |
| `q101_new_ping_tutorial_started` | Producer outside selected context | q001_quest_bugfixes.questphase / h315 / 10 |
| `travelling_merchant_lives` | Producer outside selected context | q001_quest_bugfixes.questphase / h0 / 55 |
| `wat_lch_gunsmith_01_default_on` | mq011.questphase / h163 / 73 | No reader in selected context |
| `wilson_default_shooting_tutorial` | wat_lch_gunsmith_01.scene / scene / 199 | No reader in selected context |
| `wilson_met` | Producer outside selected context | wat_lch_gunsmith_01.scene / scene / 169 |

## Exact gates, joins and cancellation

<details><summary>64 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `wat_lch_gunsmith_01.scene / scene / 151` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q001_tr_wilson_range_tut"}}` | 151:0:0 → 383:0:3; 194:0:0 → 151:0:1; 313:0:0 → 151:0:1 |
| `wat_lch_gunsmith_01.scene / scene / 169` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wilson_met","value":1,"comparisonType":"GreaterOrEqual"}}}` | 169:0:0 → 177:0:0; 169:0:0 → 184:0:1; 169:0:1 → 172:0:1; 169:0:1 → 402:0:1; 169:0:1 → 415:0:1; 224:0:0 → 169:0:1 |
| `wat_lch_gunsmith_01.scene / scene / 361` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"116004762186","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 361:0:0 → 363:0:3; 365:0:0 → 361:0:1 |
| `wat_lch_gunsmith_01.scene / scene / 365` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/meet_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 356:0:0 → 365:0:1; 365:0:0 → 361:0:1 |
| `wat_lch_gunsmith_01.scene / scene / 399` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 147:0:0 → 399:0:1; 399:0:0 → 377:0:3 |
| `wat_lch_gunsmith_01.scene / scene / 412` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_01_victor","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 385:0:0 → 412:0:1; 412:0:0 → 411:0:1 |
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
| `default_dialogs.questphase / h7727 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#loading_conditions_ent_wat_lch_gunsmith_01"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":80.0}}}}` | 0:Out → 8:In; 8:Out → 47:In |
| `default_dialogs.questphase / h7727 / 18` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/meet_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 10:Out → 18:In; 18:True → 20:Inactive; 18:False → 19:In |
| `default_dialogs.questphase / h7727 / 19` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 19:False → 15:In2; 18:False → 19:In; 19:True → 21:Inactive |
| `default_dialogs.questphase / h7727 / 32` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/meet_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 14:Out → 32:In; 32:True → 34:Inactive; 32:False → 33:In |
| `default_dialogs.questphase / h7727 / 33` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 33:False → 31:In2; 32:False → 33:In; 33:True → 35:Inactive |
| `default_dialogs.questphase / h7727 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/meet_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 5:Out → 40:In; 40:True → 42:Inactive; 40:False → 41:In |
| `default_dialogs.questphase / h7727 / 41` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 41:False → 39:In2; 40:False → 41:In; 41:True → 43:Inactive |
| `default_dialogs.questphase / h7727 / 47` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/meet_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 8:Out → 47:In; 47:True → 49:Inactive; 47:False → 48:In |
| `default_dialogs.questphase / h7727 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/02_talk_to_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 48:False → 9:In; 47:False → 48:In; 48:True → 50:Inactive |
| `q001_wilson.questphase / h0 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_used_mb_elevator","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 52:In; 52:Out → 53:In |
| `q001_wilson.questphase / h0 / 53` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_wilson_shop_tutorial_seen","value":1,"comparisonType":"GreaterOrEqual"}}}` | 53:False → 49:Active; 52:Out → 53:In |
| `q001_wilson.questphase / h0 / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 61:Out → 54:In; 54:Out → 55:In |
| `q001_wilson.questphase / h0 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questUICondition","type":{"$type":"questJournalNotification_ConditionType","journalPath":{"$type":"gameJournalPath","realPath":"contacts/wilson/q001_new_gun/01_wilson_msg_gun","fileEntryIndex":1,"className":"gameJournalPhoneMessage"}}}}` | 61:Out → 41:Active; 61:Out → 46:In; 61:Out → 54:In; 56:Out → 61:In |
| `q001_wilson.questphase / h0 / 65` | `questLogicalAndNodeDefinition` `{}` | 65:Out1 → 23:In; 50:Out → 65:In2; 55:Out → 65:In1 |
| `mq011.questphase / h163 / 93` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_wilson/wilson/meet_wilson","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 73:Out → 93:In; 93:True → 95:Inactive |
| `mq011.questphase / h163 / 96` | `questLogicalAndNodeDefinition` `{}` | 69:mq011_01_competition_out → 96:In1; 96:Out1 → 94:Active; 95:Out → 96:In2 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | q001_quest_bugfixes.questphase / h973 / 10 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `call_lifecycle` | q001_quest_bugfixes.questphase / h37 / 9 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `community_lifecycle` | q001_quest_bugfixes.questphase / h565 / 6 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | q001_quest_bugfixes.questphase / h0 / 55; q001_quest_bugfixes.questphase / h139 / 28; q001_quest_bugfixes.questphase / h139 / 29; q001_quest_bugfixes.questphase / h139 / 8; +11 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | q001_quest_bugfixes.questphase / h973 / 35 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | q001_quest_bugfixes.questphase / h604 / 8; q001_quest_bugfixes.questphase / h717 / 8; q001_quest_bugfixes.questphase / h717 / 9 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | q001_quest_bugfixes.questphase / h315 / 21 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | q001_quest_bugfixes.questphase / h839 / 17 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | q001_quest_bugfixes.questphase / h77 / 11; q001_quest_bugfixes.questphase / h77 / 8; q001_quest_bugfixes.questphase / h920 / 8; wat_lch_gunsmith_01.scene / scene / 361 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | mq011.questphase / h163 / 94; mq011.questphase / h163 / 95; q001_quest_bugfixes.questphase / h315 / 12; q001_quest_bugfixes.questphase / h315 / 13; +28 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | mq011.questphase / h163 / 96; q001_wilson.questphase / h0 / 65 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq011.questphase / h163 / 73; q001_quest_bugfixes.questphase / h139 / 2; q001_quest_bugfixes.questphase / h315 / 2; q001_quest_bugfixes.questphase / h315 / 20; +21 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | q001_quest_bugfixes.questphase / h839 / 16; q001_wilson.questphase / h0 / 54 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | wat_lch_gunsmith_01.scene / scene / 212 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `spatial_gate` | wat_lch_gunsmith_01.scene / scene / 151 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `weather_scope` | q001_quest_bugfixes.questphase / h839 / 11 | weather operation + named source + reset policy → weather request/reset dispatched. Completion follows the caller's full restoration sequence, not an early cleanup fact. |
| `workspot_performance` | q001_quest_bugfixes.questphase / h973 / 22 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` | repair; journal anchor | `base-q001` |
| `base\quest\default_dialogs.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\main_quests\prologue\q001\phases\q001_wilson.questphase` | content candidate; journal anchor | `base-q001` |
| `base\quest\minor_quests\mq011\mq011.questphase` | content candidate; journal anchor | `base-mq011` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q108](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q108.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

96 repeated typed/socket path signatures in this selected graph context; 5 distinct direct resource identities; 16 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `c8705a8da51824b73252` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h37 / 0 -> 2 -> 8 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `6497920d6ce0ac894daa` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h526 / 2 -> 3 -> 5 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; True -> In |
| `1666d7526b9bab74f2e2` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h315 / 13 -> 14 -> 22 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> Active; Out -> In |
| `1a9b8893087e174a603f` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h315 / 14 -> 22 -> 23 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `2cb6a780f07f49d4270b` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h717 / 9 -> 8 -> 1 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `d5204524c8aea0449912` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h315 / 16 -> 17 -> 19 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; True -> Active |
| `7bfcd8df5888d6d0d606` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h526 / 2 -> 3 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; False -> In |
| `abbf46d00a7c0ae464b9` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h973 / 33 -> 27 -> 28 | questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; False -> In; False -> In |
| `ef1f1c4d9ff5cba71b71` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h0 / 21 -> 24 -> 27 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPhaseNodeDefinition[questQuestPrefabEntry]; Out -> In; Out -> In1 |
| `b4d4aca04dc8f419d68d` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h315 / 12 -> 13 -> 14 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Inactive; Out -> Active |
| `d480467281c6014d993d` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h526 / 3 -> 5 -> 1 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questOutputNodeDefinition; True -> In; Out -> In |
| `11d868e716a778724f9f` | `base\quest\bugfixing\prologue\q001\q001_quest_bugfixes.questphase` / h973 / 2 -> 7 -> 8 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> In; False -> In |

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
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__stand_bar_lean0__2h_on_bar_wide__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\lipsync\en\wat_lch_gunsmith_01\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\lipsync\en\wat_lch_gunsmith_01\wilson.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\workspots\bar\bar\generic__stand_bar__work__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

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
| `q001_spawn_wilson_attention` | base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene / scene / 582; 1 total source locations in compressed evidence |
| `q001_takedown_tutorial_failed` | base\quest\main_quests\prologue\q001\phases\q001_scavengers_gameplay.questphase / h136 / 46; 1 total source locations in compressed evidence |
| `q001_tut_ap_hacked_netrunner` | base\quest\main_quests\prologue\q001\phases\q001_tbug_tutorial.questphase / h0 / 49; 1 total source locations in compressed evidence |
| `q001_tut_equip_upload_part_done` | base\quest\main_quests\prologue\q001\phases\q001_tbug_tutorial.questphase / h0 / 85; 1 total source locations in compressed evidence |
| `q001_used_mb_elevator` | base\quest\main_quests\prologue\q001\q001.questphase / h74 / 28; 1 total source locations in compressed evidence |
| `q001_wilson_shop_tutorial_seen` | base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene / scene / 288; base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene / scene / 353; 2 total source locations in compressed evidence |
| `q101_new_ping_tutorial_started` | base\quest\main_quests\prologue\q001\phases\q001_tbug_tutorial.questphase / h0 / 88; 1 total source locations in compressed evidence |
| `wat_lch_gunsmith_01_default_on` | base\quest\bugfixing\minor_quests\mq011\mq011_quest_bugfixes.questphase / h211 / 33; base\quest\minor_quests\mq011\mq011.questphase / h44 / 33; base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene / scene / 1287; base\quest\bugfixing\part1\q101\q101_quest_bugfixes.questphase / h561 / 66; 14 total source locations in compressed evidence |
| `wilson_met` | base\quest\main_quests\part1\q101\q101.quest / h0 / 46; base\quest\main_quests\part1\q101\test\profiling\q101_hammer_club_backalley_helipad.quest / h0 / 46; base\quest\main_quests\part1\q101\test\profiling\q101_hammer_club_concert.quest / h0 / 46; base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene / scene / 172; 4 total source locations in compressed evidence |

NodeRef uses: 62; TweakDB binding uses: 52. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene` | 14 / 42 | scnChangeIdleAnimEvent: 1; scnDialogLineEvent: 22; scnLookAtEvent: 8; scnPlaySkAnimEvent: 6; scneventsSocket: 5 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
