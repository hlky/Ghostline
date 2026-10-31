# Love Rollercoaster

Journal: `quests/minor_quest/mq006_rollercoaster` · `MinorQuest` · hash `2873500233`.

**Coverage: journal-linked.** 31 exact journal-linked nodes in 3 resources; 5 resources in the inspected dependency context.

Resource roles in that context: 5 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| And they say Pacificans don't like strangers… These kids must be an exception to the rule. They found themselves a good vantage point and it'd only be better if that got that old roller coaster runnin'. At least, that's what I'd try. (Primary) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal` |
| Use the control panel to activate the roller coaster. (Primary) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/02_restart_the_rollercoaster` |
| Inform Jean the roller coaster is working. (Primary) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/03_return_to_jean` |
| Talk to Jean. (Primary) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/04_talk_to_jean` |
| Get on the roller coaster. (Primary) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/05_get_into_the_rollercoaster` |
| Enjoy the ride. (Primary) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/06_enjoy_the_ride` |
| Exit the roller coaster. (Primary) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/07_get_out_of_the_rollercoaster` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq006.questphase / h53 / 3` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal` | 36:Out → 3:Active; 3:Out → 38:Active |
| `mq006.questphase / h53 / 7` (Condition) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal` | 5:Out → 7:In; 7:True → 8:Succeeded |
| `mq006.questphase / h53 / 8` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal` | 7:True → 8:Succeeded; 8:Out → 9:Active |
| `mq006.questphase / h53 / 9` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/02_restart_the_rollercoaster` | 8:Out → 9:Active |
| `mq006.questphase / h53 / 11` (Condition) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/02_restart_the_rollercoaster` | 23:Out → 11:In; 11:True → 12:Succeeded; 11:False → 48:Succeeded |
| `mq006.questphase / h53 / 12` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/02_restart_the_rollercoaster` | 11:True → 12:Succeeded; 12:Out → 13:Active |
| `mq006.questphase / h53 / 13` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/03_return_to_jean` | 12:Out → 13:Active; 48:Out → 13:Active |
| `mq006.questphase / h53 / 16` (MappinManager) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal/mq006_mp_control_box` | 15:Out → 16:Active |
| `mq006.questphase / h53 / 19` (Condition) | `quests/minor_quest/mq006_rollercoaster` | 18:Out → 19:In; 19:True → 20:Failed; 19:True → 21:In2 |
| `mq006.questphase / h53 / 20` (Journal) | `quests/minor_quest/mq006_rollercoaster` | 19:True → 20:Failed; 20:Out → 21:In1 |
| `mq006.questphase / h53 / 32` (Condition) | `quests/minor_quest/mq006_rollercoaster` | 30:Out → 32:In; 32:True → 33:Failed; 32:False → 34:In |
| `mq006.questphase / h53 / 33` (Journal) | `quests/minor_quest/mq006_rollercoaster` | 32:True → 33:Failed; 33:Out → 34:In |
| `mq006.questphase / h53 / 38` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal/description` | 3:Out → 38:Active |
| `mq006.questphase / h53 / 48` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal` | 11:False → 48:Succeeded; 48:Out → 13:Active |
| `mq006_repeatable_rollercoaster_controller.questphase / h0 / 24` (Condition) | `quests/minor_quest/mq006_rollercoaster` | 20:Out → 24:In; 24:True → 26:In |
| `mq006_02_finale.scene / scene / 56` (Condition) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/03_return_to_jean` | 3:0:0 → 56:0:1; 56:0:0 → 57:0:3; input mappings: 0:0=CutDestination, 0:1=In |
| `mq006_02_finale.scene / scene / 57` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/03_return_to_jean` | 56:0:0 → 57:0:3; 57:0:0 → 60:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 60` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/04_talk_to_jean` | 57:0:0 → 60:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 62` (Condition) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/04_talk_to_jean` | 19:2:0 → 62:0:1; 62:0:0 → 63:0:3; 62:0:1 → 64:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `mq006_02_finale.scene / scene / 63` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/04_talk_to_jean` | 62:0:0 → 63:0:3; 63:0:0 → 64:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 64` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/05_get_into_the_rollercoaster` | 62:0:1 → 64:0:1; 63:0:0 → 64:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 69` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/05_get_into_the_rollercoaster` | 69:0:0 → 71:0:1; 1005:0:0 → 69:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 71` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/06_enjoy_the_ride` | 69:0:0 → 71:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 74` (Condition) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/04_talk_to_jean` | 21:2:0 → 74:0:1; 74:0:0 → 76:0:3; input mappings: 0:0=CutDestination, 0:1=In |
| `mq006_02_finale.scene / scene / 76` (Journal) | `quests/minor_quest/mq006_rollercoaster` | 74:0:0 → 76:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 165` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/06_enjoy_the_ride` | 165:0:0 → 167:0:1; 1009:0:0 → 165:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 167` (Journal) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/07_get_out_of_the_rollercoaster` | 165:0:0 → 167:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 169` (Journal) | `quests/minor_quest/mq006_rollercoaster` | 169:0:0 → 1017:0:0; 1013:0:0 → 169:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq006_02_finale.scene / scene / 1005` (Condition) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster` | 133:0:1 → 1005:0:1; 1005:0:0 → 69:0:3; input mappings: 0:0=CutDestination, 0:1=In |
| `mq006_02_finale.scene / scene / 1009` (Condition) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster` | 50:2:0 → 1009:0:1; 1009:0:0 → 165:0:3; input mappings: 0:0=CutDestination, 0:1=In |
| `mq006_02_finale.scene / scene / 1013` (Condition) | `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster` | 170:0:1 → 1013:0:1; 1013:0:0 → 169:0:3; 1013:0:1 → 1017:0:1; input mappings: 0:0=CutDestination, 0:1=In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq006.questphase / h53 / 2` | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene`; `#mq006_01_sm_intro` | 49:Out → 2:mq006_01_intro_in; 2:mq006_01_intro_out → 4:mq006_02_finale_in; 2:StartJournal → 36:Inactive; 2:QuestTriggered → 18:In |
| `mq006.questphase / h53 / 4` | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene`; `#mq006_02_sm_finale` | 2:mq006_01_intro_out → 4:mq006_02_finale_in; 4:mq006_02_finale_out → 26:In; 4:StartRollercoaster → 22:In1 |
| `mq006.questphase / h53 / 22` | `base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase` | 4:StartRollercoaster → 22:In1 |
| `mq006.questphase / h558 / 6` | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene`; `#mq006_02_sm_finale` | 6:mq006_02_ride_no_quest_out → 1:In; 19:CutSource → 6:CutDestination; 17:Out → 6:mq006_02_ride_no_quest; 6:StartRollercoaster → 8:In1 |
| `mq006.questphase / h558 / 8` | `base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase` | 6:StartRollercoaster → 8:In1 |
| `mq006.questphase / h721 / 2` | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene`; `#mq006_02_sm_finale` | 0:Out → 2:mq006_quest_end_chat_in |
| `mq006_repeatable_rollercoaster_controller.questphase / h0 / 28` | `base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase` | 29:StartRollecoasterStandalone → 28:In1 |
| `mq006_repeatable_rollercoaster_controller.questphase / h0 / 29` | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene`; `#mq006_02_sm_finale` | 0:Out → 29:mq006_02_ride_standalone_in; 29:StartRollecoasterStandalone → 28:In1; 30:Out → 29:mq006_02_ride_standalone_in; 29:mq006_02_ride_standalone_out → 30:In |
| `mq006_repeatable_rollercoaster_controller.questphase / h46 / 2` | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene`; `#mq006_01_sm_intro` | 0:Out → 2:mq006_jean_post_q110_in |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 20 | `mq006.questphase` | 59: LogicalHub; 59:Out1 → 20:In1 |
| `base\quest\minor_quests\mq006\mq006.quest` / h0 / 2 | `mq006.questphase` | 6: Scene: mq006_chicken_test.scene; 2:Out1 → 1:In; 6:End 0 → 2:In1 |
| `base\quest\persistent_content.questphase` / h442 / 4 | `mq006_repeatable_rollercoaster_controller.questphase` | 3: PauseCondition: mq006_enable_repeatable_rollercoaster GreaterOrEqual 1; 3:Out → 4:In1 |
| `base\quest\minor_quests\mq006\mq006.questphase` / h53 / 22 | `mq006_rollercoaster_ride_controller.questphase` | 4: Scene: mq006_02_finale.scene; 4:StartRollercoaster → 22:In1 |
| `base\quest\minor_quests\mq006\mq006.questphase` / h558 / 8 | `mq006_rollercoaster_ride_controller.questphase` | 6: Scene: mq006_02_finale.scene; 6:StartRollercoaster → 8:In1 |
| `base\quest\minor_quests\mq006\phases\mq006_repeatable_rollercoaster_controller.questphase` / h0 / 28 | `mq006_rollercoaster_ride_controller.questphase` | 29: Scene: mq006_02_finale.scene; 29:StartRollecoasterStandalone → 28:In1 |
| `base\quest\minor_quests\mq006\mq006.questphase` / h53 / 2 | `mq006_01_intro.scene` | 49: PauseCondition: #mq006_tr_persistent_scenes; 49:Out → 2:mq006_01_intro_in; 2:mq006_01_intro_out → 4:mq006_02_finale_in; 2:StartJournal → 36:Inactive; 2:QuestTriggered → 18:In |
| `base\quest\minor_quests\mq006\phases\mq006_repeatable_rollercoaster_controller.questphase` / h46 / 2 | `mq006_01_intro.scene` | 0: Input; 0:Out → 2:mq006_jean_post_q110_in |
| `base\quest\minor_quests\mq006\mq006.questphase` / h53 / 4 | `mq006_02_finale.scene` | 2: Scene: mq006_01_intro.scene; 2:mq006_01_intro_out → 4:mq006_02_finale_in; 4:mq006_02_finale_out → 26:In; 4:StartRollercoaster → 22:In1 |
| `base\quest\minor_quests\mq006\mq006.questphase` / h558 / 6 | `mq006_02_finale.scene` | 19: CutControl; 17: PauseCondition; 6:mq006_02_ride_no_quest_out → 1:In; 19:CutSource → 6:CutDestination; 17:Out → 6:mq006_02_ride_no_quest; 6:StartRollercoaster → 8:In1 |
| `base\quest\minor_quests\mq006\mq006.questphase` / h721 / 2 | `mq006_02_finale.scene` | 0: Input; 0:Out → 2:mq006_quest_end_chat_in |
| `base\quest\minor_quests\mq006\phases\mq006_repeatable_rollercoaster_controller.questphase` / h0 / 29 | `mq006_02_finale.scene` | 0: Input; 30: PauseCondition: {"miliseconds": 500}; 0:Out → 29:mq006_02_ride_standalone_in; 29:StartRollecoasterStandalone → 28:In1; 30:Out → 29:mq006_02_ride_standalone_in; 29:mq006_02_ride_standalone_out → 30:In |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
| `base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.quest` / h0 / 10 | `persistent_content.questphase` | 0: Start; 0:Out → 10:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 17 | `persistent_content.questphase` | 0: Input; 36: Input; 0:Out → 17:In1; 36:Out → 17:EP1_Standalone |
| `base\quest\main_quests\part1\q108\q108_johnny.quest` / h0 / 24 | `persistent_content.questphase` | 0: Start; 0:Out → 24:In1 |
| `base\quest\minor_quests\mq025\batty\batty_quest.quest` / h0 / 3 | `persistent_content.questphase` | 0: Start; 0:Out → 3:In1 |
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
| `mq006_01_intro.scene` | mq006_01_intro_in, mq006_jean_post_q110_in, darline_fake_default_in, farah_fake_default_in, anel_preview, jean_preview, old → mq006_01_intro_out, StartJournal, QuestTriggered | jean; anel; darline; farah; sandley; roller_coaster_cart; Player; 159 nodes / 197 edges |
| `mq006_02_finale.scene` | mq006_02_finale_in, Old, mq006_quest_end_chat_in, mq006_jean_final_interaction_in, RollercoasterSittingTest, mq006_02_ride_standalone_in, mq006_02_ride_no_quest, ridestart, old, mq006_darlene_final_interaction_in → mq006_02_finale_out, StartRollercoaster, StartRollecoasterStandalone, mq006_02_ride_standalone_out, mq006_02_ride_no_quest_out | jean; anel; darline; farah; sandley; johnny; rollercoaster_cart; Player; 235 nodes / 279 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq006_01_intro.scene / n7 / 0` | What're you doing with the rollercoaster? (`Hook`) | No option-level predicate stored | 0:0 → 31:0:0 |
| `mq006_01_intro.scene / n7 / 1` | Heywood. (`watson`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83574632792"}}}} | 0:1 → 9:0:0 |
| `mq006_01_intro.scene / n7 / 2` | From outside of town. (`nomad`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "67091901544"}}}} | 0:2 → 83:0:0 |
| `mq006_01_intro.scene / n7 / 3` | Why's it matter where I'm from? (`corp`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83635443133"}}}} | 0:3 → 33:0:0 |
| `mq006_01_intro.scene / n12 / 0` | [Talk] (`talk to`) | No option-level predicate stored | 0:0 → 14:0:0 |
| `mq006_01_intro.scene / n21 / 0` | [Talk] (`talk to`) | No option-level predicate stored | 0:0 → 23:0:0 |
| `mq006_01_intro.scene / n44 / 0` | You're trying to fix this? (`first talk`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq006_01_anel_teased_jean", "comparisonType": "Equal"}}} | 0:0 → 52:0:0 |
| `mq006_01_intro.scene / n44 / 1` | How's it going? (`talked anel`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq006_01_anel_teased_jean", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:1 → 50:0:0 |
| `mq006_01_intro.scene / n44 / 2` | I've never been on one of these. (`never`) | No option-level predicate stored | 0:2 → 46:0:0 |
| `mq006_01_intro.scene / n44 / 3` | What happened to the Voodoo Boys? (`voodoo`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq006_do_not_display", "value": 1, "comparisonType": "GreaterOrEqual"}}} | No matching 0:ordinal output; inspect raw stamps |
| `mq006_01_intro.scene / n57 / 0` | Mind if I give it a shot? (`CanHelp`) | No option-level predicate stored | 0:0 → 60:0:0 |
| `mq006_01_intro.scene / n57 / 1` | Good luck. (`GoodLuck`) | No option-level predicate stored | 0:1 → 62:0:0 |
| `mq006_01_intro.scene / n107 / 0` | Any idea what happened to the Voodoo Boys? (`vboys`) | No option-level predicate stored | 0:0 → 105:0:0 |
| `mq006_01_intro.scene / n107 / 1` | Where is everyone? (`the rest`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq006_01_jean_met", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:1 → 277:0:1 |
| `mq006_01_intro.scene / n107 / 2` | Wanna take a ride on the rollercoaster? (`rollercoaster`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq006_01_jean_met", "comparisonType": "Equal"}}} | 0:2 → 278:0:1 |
| `mq006_01_intro.scene / n118 / 0` | Gossip. (`gossips`) | No option-level predicate stored | 0:0 → 109:0:0 |
| `mq006_01_intro.scene / n118 / 1` | Facts. (`facts`) | No option-level predicate stored | 0:1 → 111:0:0 |
| `mq006_01_intro.scene / n119 / 0` | You seem skeptical. (`skeptical`) | No option-level predicate stored | 0:0 → 128:0:0 |
| `mq006_01_intro.scene / n119 / 1` | What's religion got to do with it? (`religion`) | No option-level predicate stored | 0:1 → 131:0:0 |
| `mq006_01_intro.scene / n134 / 0` | All right, I'll try to fix it. (`Re-take quest`) | No option-level predicate stored | 0:0 → 136:0:0 |
| `mq006_01_intro.scene / n134 / 1` | How do you know each other? (`fluff`) | No option-level predicate stored | 0:1 → 274:0:1 |
| `mq006_02_finale.scene / n3 / 0` | Should be all set to go. (`Fixed`) | No option-level predicate stored | 0:0 → 8:0:0; 0:0 → 56:0:1; 0:0 → 1059:0:1 |
| `mq006_02_finale.scene / n3 / 1` | You come here often? (`Fluff`) | No option-level predicate stored | 0:1 → 5:0:0 |
| `mq006_02_finale.scene / n17 / 0` | All right, fine. (`Take ride`) | No option-level predicate stored | 0:0 → 19:0:0; 0:0 → 1102:0:1 |
| `mq006_02_finale.scene / n17 / 1` | No thanks. (`Don't take ride`) | No option-level predicate stored | 0:1 → 21:0:0 |
| `mq006_02_finale.scene / n233 / 0` | [Talk] (`talk to`) | No option-level predicate stored | No matching 0:ordinal output; inspect raw stamps |
| `mq006_02_finale.scene / n234 / 0` | [Talk] (`talk to`) | No option-level predicate stored | No matching 0:ordinal output; inspect raw stamps |
| `mq006_02_finale.scene / n335 / 0` | [Get in] (`GetIn`) | No option-level predicate stored | 0:0 → 133:0:1; 0:0 → 258:0:1; 0:0 → 341:0:0; 0:0 → 1074:0:0; 0:0 → 1082:0:0 |
| `mq006_02_finale.scene / n378 / 0` | [Get out] (`Exit`) | No option-level predicate stored | 0:0 → 596:0:1 |
| `mq006_02_finale.scene / n463 / 0` | [Raise arms] (`Handsup`) | No option-level predicate stored | 0:0 → 482:0:0 |
| `mq006_02_finale.scene / n526 / 0` | [Get out] (`Exit`) | No option-level predicate stored | 0:0 → 600:0:1 |
| `mq006_02_finale.scene / n557 / 0` | [Raise arms] (`Handsup`) | No option-level predicate stored | 0:0 → 561:0:0 |
| `mq006_02_finale.scene / n575 / 0` | [Get in] (`GetIn`) | No option-level predicate stored | 0:0 → 511:0:0; 0:0 → 1089:0:0; 0:0 → 1091:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `air_traffic_start_space_shuttle` | mq006_02_finale.scene / scene / 478 | No reader in selected context |
| `mq006` | mq006.questphase / h53 / 61 | No reader in selected context |
| `mq006_01_agreed_to_help` | mq006_01_intro.scene / scene / 64 | No reader in selected context |
| `mq006_01_anel_teased_jean` | mq006_01_intro.scene / scene / 37 | mq006_01_intro.scene / scene / 44 |
| `mq006_01_corp` | mq006_01_intro.scene / scene / 89 | mq006_02_finale.scene / scene / 180; mq006_02_finale.scene / scene / 211 |
| `mq006_01_jean_choice_selected` | mq006_01_intro.scene / scene / 354 | mq006_01_intro.scene / scene / 357 |
| `mq006_01_jean_met` | mq006_01_intro.scene / scene / 156 | mq006_01_intro.scene / scene / 107 |
| `mq006_01_lookat_loop` | mq006_01_intro.scene / scene / 548; mq006_01_intro.scene / scene / 550; mq006_01_intro.scene / scene / 560; mq006_01_intro.scene / scene / 576; mq006_01_intro.scene / scene / 579; mq006_01_intro.scene / scene / 584; mq006_01_intro.scene / scene / 589; mq006_01_intro.scene / scene / 596; mq006_01_intro.scene / scene / 598; mq006_01_intro.scene / scene / 605 | mq006_01_intro.scene / scene / 536; mq006_01_intro.scene / scene / 537 |
| `mq006_01_nomad` | mq006_01_intro.scene / scene / 88 | mq006_02_finale.scene / scene / 179; mq006_02_finale.scene / scene / 210 |
| `mq006_01_street_kid` | mq006_01_intro.scene / scene / 90 | mq006_02_finale.scene / scene / 181; mq006_02_finale.scene / scene / 212 |
| `mq006_02_finale_lookat_loop` | mq006_02_finale.scene / scene / 1057; mq006_02_finale.scene / scene / 1059; mq006_02_finale.scene / scene / 1062; mq006_02_finale.scene / scene / 1065 | mq006_02_finale.scene / scene / 1035; mq006_02_finale.scene / scene / 1037 |
| `mq006_control_box_located` | Producer outside selected context | mq006.questphase / h53 / 15 |
| `mq006_do_not_display` | Producer outside selected context | mq006_01_intro.scene / scene / 44 |
| `mq006_enable_repeatable_rollercoaster` | mq006.questphase / h498 / 5 | No reader in selected context |
| `mq006_fixing_the_rollercoaster_on` | mq006_01_intro.scene / scene / 428; mq006_01_intro.scene / scene / 66 | mq006.questphase / h53 / 6 |
| `mq006_ride_finished` | mq006_02_finale.scene / scene / 536; mq006_02_finale.scene / scene / 540; mq006_rollercoaster_ride_controller.questphase / h7 / 7 | mq006_02_finale.scene / scene / 44; mq006_02_finale.scene / scene / 46; mq006_02_finale.scene / scene / 522 |
| `mq006_ride_no_quest` | mq006.questphase / h558 / 7 | mq006_02_finale.scene / scene / 133; mq006_02_finale.scene / scene / 137; mq006_02_finale.scene / scene / 163; mq006_02_finale.scene / scene / 170; mq006_02_finale.scene / scene / 927 |
| `mq006_roller_coaster_fixed` | mq006.questphase / h53 / 29; mq006.questphase / h558 / 5 | mq006.questphase / h53 / 10; mq006.questphase / h558 / 20; mq006_01_intro.scene / scene / 70 |
| `q110_08a_netwatch_deal` | Producer outside selected context | mq006_01_intro.scene / scene / 100 |
| `q110_done` | Producer outside selected context | mq006_repeatable_rollercoaster_controller.questphase / h0 / 19 |
| `q110_mall_job_active` | Producer outside selected context | mq006_02_finale.scene / scene / 143 |
| `sq032_johnnys_motivation` | Producer outside selected context | mq006_02_finale.scene / scene / 222 |
| `this_is_for_testing_only_mq006` | Producer outside selected context | mq006_02_finale.scene / scene / 499 |

## Exact gates, joins and cancellation

<details><summary>115 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq006.questphase / h53 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_control_terminal"}}` | 53:Out → 5:In; 5:Out → 7:In; 5:Out → 10:In; 5:Out → 43:In |
| `mq006.questphase / h53 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_fixing_the_rollercoaster_on","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 6:In; 6:Out → 53:In |
| `mq006.questphase / h53 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 5:Out → 7:In; 7:True → 8:Succeeded |
| `mq006.questphase / h53 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_roller_coaster_fixed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 5:Out → 10:In; 10:Out → 28:In2 |
| `mq006.questphase / h53 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/02_restart_the_rollercoaster","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 23:Out → 11:In; 11:True → 12:Succeeded; 11:False → 48:Succeeded |
| `mq006.questphase / h53 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_control_box_located","value":1,"comparisonType":"GreaterOrEqual"}}}` | 53:Out → 15:In; 15:Out → 16:Active |
| `mq006.questphase / h53 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq006_tr_area_big"}}` | 2:QuestTriggered → 18:In; 18:Out → 19:In |
| `mq006.questphase / h53 / 19` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 18:Out → 19:In; 19:True → 20:Failed; 19:True → 21:In2 |
| `mq006.questphase / h53 / 28` | `questLogicalXorNodeDefinition` `{}` | 10:Out → 28:In2; 43:Out → 28:In1; 28:Out1 → 29:In; 28:Out1 → 58:In |
| `mq006.questphase / h53 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/act_01/q110_01_voodooboys","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 0:Out → 30:In; 30:Out → 32:In |
| `mq006.questphase / h53 / 32` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 30:Out → 32:In; 32:True → 33:Failed; 32:False → 34:In |
| `mq006.questphase / h53 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq006_rollercoaster_cart_001"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 39:In; 39:Out → 40:In; 39:Out → 62:In |
| `mq006.questphase / h53 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#mq006_dvc_rollcer_coaster_control_panel","eventType":"Executed"}}}` | 5:Out → 43:In; 43:Out → 28:In1 |
| `mq006.questphase / h53 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_persistent_scenes"}}` | 0:Out → 49:In; 49:Out → 2:mq006_01_intro_in |
| `mq006.questphase / h53 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 51:Out → 52:In; 52:Out → 55:In |
| `mq006.questphase / h498 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq006_tr_area_big"}}` | 3:Out → 2:In; 5:Out → 3:In |
| `mq006.questphase / h558 / 4` | `questLogicalXorNodeDefinition` `{}` | 22:Out → 4:In1; 20:Out → 4:In2; 4:Out1 → 5:In; 4:Out1 → 12:In |
| `mq006.questphase / h558 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_rollercoaster_cart_001"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":25.0},"comparisonType":"LessOrEqual"}}}` | 17:Out → 6:mq006_02_ride_no_quest; 13:Out → 17:In; 18:Out → 17:In; 17:Out → 18:In |
| `mq006.questphase / h558 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_rollercoaster_cart_001"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0}}}}` | 18:Out → 17:In; 17:Out → 18:In; 18:Out → 19:In |
| `mq006.questphase / h558 / 19` | `questCutControlNodeDefinition` `{}` | 19:CutSource → 6:CutDestination; 18:Out → 19:In |
| `mq006.questphase / h558 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_roller_coaster_fixed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 20:Out → 4:In2; 7:Out → 20:In |
| `mq006.questphase / h558 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#mq006_dvc_rollcer_coaster_control_panel","eventType":"Executed"}}}` | 22:Out → 4:In1; 7:Out → 22:In |
| `mq006.questphase / h699 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 0:Out → 3:In; 3:Out → 7:In |
| `mq006.questphase / h699 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_persistent_scenes"}}` | 3:Out → 7:In; 8:Out1 → 7:In; 7:Out → 8:In1 |
| `mq006.questphase / h721 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq006_tr_persistent_scenes"}}` | 0:Out → 6:In; 6:Out → 1:In |
| `mq006.questphase / h765 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_weather_area"}}` | 0:Out → 2:In; 3:Out → 2:In; 2:Out → 3:In; 2:Out → 4:In |
| `mq006.questphase / h765 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq006_tr_weather_area"}}` | 3:Out → 2:In; 2:Out → 3:In; 3:Out → 5:In |
| `mq006_repeatable_rollercoaster_controller.questphase / h0 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q110_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 19:In; 19:Out → 20:In |
| `mq006_repeatable_rollercoaster_controller.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":10}}}` | 19:Out → 20:In; 20:Out → 24:In |
| `mq006_repeatable_rollercoaster_controller.questphase / h0 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["jean"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":20.0},"comparisonType":"LessOrEqual"}}}` | 21:Out → 22:In; 23:Out1 → 22:In; 22:Out → 23:In1 |
| `mq006_repeatable_rollercoaster_controller.questphase / h0 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 20:Out → 24:In; 24:True → 26:In |
| `mq006_repeatable_rollercoaster_controller.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq006_tr_area_big"}}` | 26:Out → 21:In; 24:True → 26:In |
| `mq006_repeatable_rollercoaster_controller.questphase / h0 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 30:Out → 29:mq006_02_ride_standalone_in; 29:mq006_02_ride_standalone_out → 30:In |
| `mq006_repeatable_rollercoaster_controller.questphase / h46 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["jean"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0}}}}` | 4:Out → 1:In; 5:Out → 4:In |
| `mq006_rollercoaster_ride_controller.questphase / h7 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 6:Out → 8:In; 8:Out → 7:In; 8:Out → 13:In |
| `mq006_rollercoaster_ride_controller.questphase / h7 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 0:Out → 9:In; 9:Out → 2:In; 9:Out → 12:In |
| `mq006_01_intro.scene / scene / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_party_approached"}}` | 1:0:0 → 3:0:1; 3:0:0 → 5:0:0; 3:0:0 → 40:0:0; 3:0:0 → 77:0:0; 40:0:0 → 3:0:0 |
| `mq006_01_intro.scene / scene / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_jean_approached"}}` | 1:0:0 → 40:0:1; 3:0:0 → 40:0:0; 40:0:0 → 3:0:0; 40:0:0 → 77:0:0; 40:0:0 → 208:0:0 |
| `mq006_01_intro.scene / scene / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_roller_coaster_fixed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 1:0:0 → 70:0:1; 70:0:0 → 2:0:0 |
| `mq006_01_intro.scene / scene / 100` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q110_08a_netwatch_deal","value":1,"comparisonType":"GreaterOrEqual"}}}` | 100:0:0 → 261:0:1; 100:0:1 → 103:0:0; 105:2:0 → 100:0:1 |
| `mq006_01_intro.scene / scene / 162` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["anel"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"LessOrEqual"}},{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_party_approached"}]}}` | 5:0:0 → 162:0:1; 44:1:0 → 162:0:0; 162:0:0 → 80:0:0 |
| `mq006_01_intro.scene / scene / 210` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 204:0:0 → 210:0:1; 210:0:0 → 208:0:1 |
| `mq006_01_intro.scene / scene / 261` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\minor_quests\\mq006\\scenes\\mq006_01_intro.scene","Flags":"Soft"},"sectionName":"mq006_01_netwatch_yes","type":"IsOutside"}}}` | 100:0:0 → 261:0:1; 261:0:0 → 101:0:0 |
| `mq006_01_intro.scene / scene / 274` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\minor_quests\\mq006\\scenes\\mq006_01_intro.scene","Flags":"Soft"},"sectionName":"mq006_01_re_take_fluff","type":"IsOutside"}}}` | 134:0:1 → 274:0:1; 274:0:0 → 139:0:0 |
| `mq006_01_intro.scene / scene / 277` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\minor_quests\\mq006\\scenes\\mq006_01_intro.scene","Flags":"Soft"},"sectionName":"mq006_01_the_rest","type":"IsOutside"}}}` | 107:0:1 → 277:0:1; 277:0:0 → 150:0:0 |
| `mq006_01_intro.scene / scene / 278` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\minor_quests\\mq006\\scenes\\mq006_01_intro.scene","Flags":"Soft"},"sectionName":"mq006_01_try_to_repare","type":"IsOutside"}}}` | 107:0:2 → 278:0:1; 278:0:0 → 153:0:0 |
| `mq006_01_intro.scene / scene / 357` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_01_jean_choice_selected","comparisonType":"Equal"}}}` | 80:2:0 → 357:0:1; 357:0:0 → 7:0:0; 357:0:0 → 536:0:1; 357:0:0 → 548:0:1 |
| `mq006_01_intro.scene / scene / 441` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["anel"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}}}` | 434:0:0 → 441:0:1; 441:0:0 → 437:0:0; 441:0:0 → 442:0:1; 441:0:0 → 448:1:0; 442:0:0 → 441:0:1 |
| `mq006_01_intro.scene / scene / 442` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["anel"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0}}}}` | 441:0:0 → 442:0:1; 442:0:0 → 441:0:1; 442:0:0 → 448:0:0 |
| `mq006_01_intro.scene / scene / 454` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["jean"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}}}` | 434:0:0 → 454:0:1; 454:0:0 → 452:0:0; 454:0:0 → 456:0:1; 454:0:0 → 458:1:0; 456:0:0 → 454:0:1 |
| `mq006_01_intro.scene / scene / 456` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["jean"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0}}}}` | 454:0:0 → 456:0:1; 456:0:0 → 454:0:1; 456:0:0 → 458:0:0 |
| `mq006_01_intro.scene / scene / 473` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["jean"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":12.0}}}}` | 471:0:0 → 473:0:1; 473:0:0 → 475:0:0 |
| `mq006_01_intro.scene / scene / 486` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["jean"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"LessOrEqual"}}}` | 148:0:0 → 486:0:1; 475:0:0 → 486:0:1; 486:0:0 → 471:0:0 |
| `mq006_01_intro.scene / scene / 536` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_01_lookat_loop"}}}` | 357:0:0 → 536:0:1; 536:0:0 → 534:0:0; 536:0:0 → 537:0:1; 536:0:0 → 569:0:0; 537:0:0 → 536:0:1; 593:0:0 → 536:0:1 |
| `mq006_01_intro.scene / scene / 537` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_01_lookat_loop","comparisonType":"Equal"}}}` | 536:0:0 → 537:0:1; 537:0:0 → 534:1:0; 537:0:0 → 535:0:0; 537:0:0 → 536:0:1; 537:0:0 → 569:1:0 |
| `mq006_02_finale.scene / scene / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 26:0:0 → 23:0:0; 415:0:0 → 26:0:1 |
| `mq006_02_finale.scene / scene / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 29:0:0 → 249:0:0; 133:0:1 → 29:0:1 |
| `mq006_02_finale.scene / scene / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_ride_finished","value":1,"comparisonType":"GreaterOrEqual"}}}` | 44:0:0 → 151:0:1; 44:0:0 → 163:0:1; 44:0:0 → 490:0:0; 44:0:0 → 915:0:0; 44:0:0 → 917:1:0; 258:0:0 → 44:0:1 |
| `mq006_02_finale.scene / scene / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_ride_finished","value":1,"comparisonType":"GreaterOrEqual"}}}` | 46:0:0 → 23:0:0; 46:0:0 → 52:0:0; 415:0:0 → 46:0:1 |
| `mq006_02_finale.scene / scene / 56` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/03_return_to_jean","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:0:0 → 56:0:1; 56:0:0 → 57:0:3 |
| `mq006_02_finale.scene / scene / 62` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/04_talk_to_jean","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 19:2:0 → 62:0:1; 62:0:0 → 63:0:3; 62:0:1 → 64:0:1 |
| `mq006_02_finale.scene / scene / 74` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/04_talk_to_jean","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 21:2:0 → 74:0:1; 74:0:0 → 76:0:3 |
| `mq006_02_finale.scene / scene / 105` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_001"}}` | 105:0:0 → 107:0:0; 105:0:0 → 463:0:0; 369:0:0 → 105:0:1 |
| `mq006_02_finale.scene / scene / 109` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_002"}}` | 109:0:0 → 111:0:0; 109:0:0 → 463:0:0; 369:0:1 → 109:0:1 |
| `mq006_02_finale.scene / scene / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_003"}}` | 113:0:0 → 115:0:0; 113:0:0 → 463:0:0; 369:0:2 → 113:0:1 |
| `mq006_02_finale.scene / scene / 117` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_004"}}` | 117:0:0 → 127:0:0; 369:0:3 → 117:0:1 |
| `mq006_02_finale.scene / scene / 121` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_004b"}}` | 121:0:0 → 123:0:0; 121:0:0 → 463:0:0; 369:0:4 → 121:0:1 |
| `mq006_02_finale.scene / scene / 125` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_005"}}` | 125:0:0 → 119:0:0; 369:0:5 → 125:0:1 |
| `mq006_02_finale.scene / scene / 133` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_ride_no_quest","value":1,"comparisonType":"GreaterOrEqual"}}}` | 133:0:1 → 29:0:1; 133:0:1 → 1005:0:1; 335:0:0 → 133:0:1 |
| `mq006_02_finale.scene / scene / 137` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_ride_no_quest","value":1,"comparisonType":"GreaterOrEqual"}}}` | 137:0:0 → 143:0:1; 137:0:1 → 154:0:1; 490:0:0 → 137:0:1 |
| `mq006_02_finale.scene / scene / 143` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q110_mall_job_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 137:0:0 → 143:0:1; 143:0:0 → 141:0:0; 143:0:1 → 146:0:0 |
| `mq006_02_finale.scene / scene / 151` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq006_02_finale_johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":90.0,"inverted":true}}}` | 44:0:0 → 151:0:1; 151:0:0 → 153:0:1 |
| `mq006_02_finale.scene / scene / 163` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_ride_no_quest","value":1,"comparisonType":"GreaterOrEqual"}}}` | 44:0:0 → 163:0:1; 163:0:1 → 851:0:1; 163:0:1 → 910:0:1 |
| `mq006_02_finale.scene / scene / 170` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_ride_no_quest","value":1,"comparisonType":"GreaterOrEqual"}}}` | 170:0:0 → 175:0:0; 170:0:1 → 1013:0:1; 540:0:0 → 170:0:1 |
| `mq006_02_finale.scene / scene / 179` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_01_nomad","value":1,"comparisonType":"Equal"}}}` | 179:0:0 → 185:0:0; 179:0:1 → 180:0:1; 181:0:1 → 179:0:1 |
| `mq006_02_finale.scene / scene / 180` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_01_corp","value":1,"comparisonType":"Equal"}}}` | 179:0:1 → 180:0:1; 180:0:0 → 184:0:0; 180:0:1 → 10:0:0 |
| `mq006_02_finale.scene / scene / 181` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_01_street_kid","value":1,"comparisonType":"Equal"}}}` | 181:0:0 → 183:0:0; 181:0:1 → 179:0:1; 444:0:0 → 181:0:1 |
| `mq006_02_finale.scene / scene / 210` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_01_nomad","value":1,"comparisonType":"Equal"}}}` | 210:0:0 → 209:0:0; 210:0:1 → 211:0:1; 212:0:1 → 210:0:1 |
| `mq006_02_finale.scene / scene / 211` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_01_corp","value":1,"comparisonType":"Equal"}}}` | 210:0:1 → 211:0:1; 211:0:0 → 208:0:0 |
| `mq006_02_finale.scene / scene / 212` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_01_street_kid","value":1,"comparisonType":"Equal"}}}` | 212:0:0 → 207:0:0; 212:0:1 → 210:0:1; 364:0:0 → 212:0:1 |
| `mq006_02_finale.scene / scene / 222` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_johnnys_motivation","value":1,"comparisonType":"GreaterOrEqual"}}}` | 141:0:0 → 222:0:1; 222:0:0 → 223:0:0; 222:0:1 → 156:0:2 |
| `mq006_02_finale.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_approaching_ride_end"}}` | 258:0:0 → 44:0:1; 258:0:0 → 364:0:0; 335:0:0 → 258:0:1 |
| `mq006_02_finale.scene / scene / 447` | `questConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["jean"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 52:0:0 → 447:0:1; 447:0:0 → 446:0:0; 447:0:1 → 450:0:1 |
| `mq006_02_finale.scene / scene / 476` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_rocket_start"}}` | 369:0:6 → 476:0:1; 476:0:0 → 478:0:1 |
| `mq006_02_finale.scene / scene / 499` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"this_is_for_testing_only_mq006","value":1,"comparisonType":"GreaterOrEqual"}}}` | 98:0:0 → 499:0:1; 499:0:0 → 490:0:0 |
| `mq006_02_finale.scene / scene / 522` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_ride_finished","value":1,"comparisonType":"GreaterOrEqual"}}}` | 515:0:0 → 522:0:1; 522:0:0 → 530:0:0 |
| `mq006_02_finale.scene / scene / 543` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_001"}}` | 543:0:0 → 557:0:0; 549:0:0 → 543:0:1 |
| `mq006_02_finale.scene / scene / 544` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_002"}}` | 544:0:0 → 557:0:0; 549:0:1 → 544:0:1 |
| `mq006_02_finale.scene / scene / 545` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_003"}}` | 545:0:0 → 557:0:0; 549:0:2 → 545:0:1 |
| `mq006_02_finale.scene / scene / 546` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_004"}}` | 546:0:0 → 557:0:0; 549:0:3 → 546:0:1 |
| `mq006_02_finale.scene / scene / 547` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_004b"}}` | 547:0:0 → 557:0:0; 549:0:4 → 547:0:1 |
| `mq006_02_finale.scene / scene / 548` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_tr_johnny_ride_reaction_005"}}` | 548:0:0 → 557:0:0; 549:0:5 → 548:0:1 |
| `mq006_02_finale.scene / scene / 828` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq006_02_finale_johnny"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 199:0:0 → 828:0:1; 828:0:0 → 198:0:0 |
| `mq006_02_finale.scene / scene / 833` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq006_02_finale_johnny"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 627:0:0 → 833:0:1; 833:0:0 → 98:0:0 |
| `mq006_02_finale.scene / scene / 840` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 98:0:0 → 840:0:1; 840:0:0 → 842:0:0 |
| `mq006_02_finale.scene / scene / 907` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 235:0:0 → 907:0:1; 907:0:0 → 232:0:0 |
| `mq006_02_finale.scene / scene / 915` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":12}}}` | 44:0:0 → 915:0:0; 98:0:0 → 915:0:1; 915:0:0 → 917:0:0; 917:0:0 → 915:0:1 |
| `mq006_02_finale.scene / scene / 927` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_ride_no_quest","value":1,"comparisonType":"GreaterOrEqual"}}}` | 154:0:0 → 927:0:1; 927:0:0 → 378:0:0 |
| `mq006_02_finale.scene / scene / 932` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq006_approaching_ride_end"}}` | 515:2:1 → 932:0:1; 932:0:0 → 935:0:1 |
| `mq006_02_finale.scene / scene / 935` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["anel"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 932:0:0 → 935:0:1; 935:0:0 → 937:0:0 |
| `mq006_02_finale.scene / scene / 959` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["anel"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":2.0},"comparisonType":"LessOrEqual"}}}` | 959:0:0 → 957:0:0; 959:0:0 → 961:0:1; 959:0:0 → 963:1:0; 961:0:0 → 959:0:1; 985:0:1 → 959:0:1 |
| `mq006_02_finale.scene / scene / 961` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["anel"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":4.0}}}}` | 959:0:0 → 961:0:1; 961:0:0 → 959:0:1; 961:0:0 → 963:0:0 |
| `mq006_02_finale.scene / scene / 967` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["jean"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":2.0},"comparisonType":"LessOrEqual"}}}` | 967:0:0 → 965:0:0; 967:0:0 → 969:0:1; 967:0:0 → 971:1:0; 969:0:0 → 967:0:1; 985:0:2 → 967:0:1 |
| `mq006_02_finale.scene / scene / 969` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq006_com_party","names":["jean"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":4.0}}}}` | 967:0:0 → 969:0:1; 969:0:0 → 967:0:1; 969:0:0 → 971:0:0 |
| `mq006_02_finale.scene / scene / 1005` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster","fileEntryIndex":2,"className":"gameJournalQuestPhase"},"state":"Active"}}}` | 133:0:1 → 1005:0:1; 1005:0:0 → 69:0:3 |
| `mq006_02_finale.scene / scene / 1009` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster","fileEntryIndex":2,"className":"gameJournalQuestPhase"},"state":"Active"}}}` | 50:2:0 → 1009:0:1; 1009:0:0 → 165:0:3 |
| `mq006_02_finale.scene / scene / 1013` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster","fileEntryIndex":2,"className":"gameJournalQuestPhase"},"state":"Active"}}}` | 170:0:1 → 1013:0:1; 1013:0:0 → 169:0:3; 1013:0:1 → 1017:0:1 |
| `mq006_02_finale.scene / scene / 1035` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_02_finale_lookat_loop"}}}` | 1:0:0 → 1035:0:1; 1035:0:0 → 1037:0:1; 1035:0:0 → 1042:0:0; 1035:0:0 → 1049:0:0; 1037:0:0 → 1035:0:1 |
| `mq006_02_finale.scene / scene / 1037` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq006_02_finale_lookat_loop","comparisonType":"Equal"}}}` | 1035:0:0 → 1037:0:1; 1037:0:0 → 1035:0:1; 1037:0:0 → 1042:1:0; 1037:0:0 → 1047:0:0; 1037:0:0 → 1049:1:0 |
| `mq006_02_finale.scene / scene / 1074` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq006_rollercoaster_cart_001"},"timeInterval":0.20000000298023224,"onScreenTest":true,"inverted":true}}}` | 335:0:0 → 1074:0:0; 1074:0:0 → 335:1:0; 1074:0:0 → 1082:0:1; 1082:0:0 → 1074:0:1 |
| `mq006_02_finale.scene / scene / 1082` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq006_rollercoaster_cart_001"},"timeInterval":0.20000000298023224,"onScreenTest":true}}}` | 335:0:0 → 1082:0:0; 1074:0:0 → 1082:0:1; 1075:0:0 → 1082:0:1; 1082:0:0 → 335:0:0; 1082:0:0 → 1074:0:1 |
| `mq006_02_finale.scene / scene / 1089` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq006_rollercoaster_cart_001"},"timeInterval":0.20000000298023224,"onScreenTest":true,"inverted":true}}}` | 575:0:0 → 1089:0:0; 1089:0:0 → 575:1:0; 1089:0:0 → 1091:0:1; 1091:0:0 → 1089:0:1 |
| `mq006_02_finale.scene / scene / 1091` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq006_rollercoaster_cart_001"},"timeInterval":0.20000000298023224,"onScreenTest":true}}}` | 509:0:0 → 1091:0:1; 575:0:0 → 1091:0:0; 1089:0:0 → 1091:0:1; 1091:0:0 → 575:0:0; 1091:0:0 → 1089:0:1 |
| `mq006_02_finale.scene / scene / 1142` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 530:2:0 → 1142:0:1; 1142:0:0 → 1136:0:1 |
| `mq006_02_finale.scene / scene / 1147` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":50}}}` | 1136:0:0 → 1147:0:1; 1147:0:0 → 1150:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq006.questphase / h53 / 39; mq006_02_finale.scene / scene / 828; mq006_02_finale.scene / scene / 833; mq006_02_finale.scene / scene / 935 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq006_01_intro.scene / scene / 221; mq006_01_intro.scene / scene / 371; mq006_02_finale.scene / scene / 413 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | mq006.questphase / h53 / 23; mq006.questphase / h53 / 24 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq006_01_intro.scene / scene / 107; mq006_01_intro.scene / scene / 118; mq006_01_intro.scene / scene / 119; mq006_01_intro.scene / scene / 12; +15 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | mq006.questphase / h498 / 2; mq006.questphase / h53 / 34 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq006.questphase / h53 / 10; mq006.questphase / h53 / 15; mq006.questphase / h53 / 6; mq006.questphase / h558 / 20; +27 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq006.questphase / h498 / 4; mq006.questphase / h498 / 9 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq006.questphase / h53 / 53; mq006.questphase / h53 / 54; mq006.questphase / h53 / 57; mq006.questphase / h53 / 58; +6 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | mq006.questphase / h53 / 44; mq006.questphase / h53 / 45; mq006.questphase / h53 / 46; mq006.questphase / h53 / 47; +2 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | mq006_repeatable_rollercoaster_controller.questphase / h0 / 20 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | mq006.questphase / h12 / 3; mq006.questphase / h53 / 12; mq006.questphase / h53 / 13; mq006.questphase / h53 / 20; +18 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | mq006.questphase / h498 / 5; mq006.questphase / h53 / 29; mq006.questphase / h53 / 61; mq006.questphase / h558 / 5; +28 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq006.questphase / h53 / 28; mq006.questphase / h558 / 4 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq006.questphase / h53 / 52; mq006.questphase / h699 / 3; mq006_01_intro.scene / scene / 210; mq006_02_finale.scene / scene / 1142; +9 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq006.questphase / h558 / 19 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq006.questphase / h53 / 25; mq006.questphase / h53 / 26 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq006.questphase / h53 / 2; mq006.questphase / h53 / 4; mq006.questphase / h558 / 6; mq006.questphase / h721 / 2; +2 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq006.questphase / h498 / 3; mq006.questphase / h53 / 18; mq006.questphase / h53 / 49; mq006.questphase / h53 / 5; +23 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | mq006.questphase / h53 / 40; mq006_rollercoaster_ride_controller.questphase / h7 / 2; mq006_rollercoaster_ride_controller.questphase / h7 / 3; mq006_rollercoaster_ride_controller.questphase / h7 / 4; +2 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `weather_scope` | mq006.questphase / h498 / 7; mq006.questphase / h765 / 4; mq006.questphase / h765 / 5 | weather operation + named source + reset policy → weather request/reset dispatched. Completion follows the caller's full restoration sequence, not an early cleanup fact. |
| `workspot_performance` | mq006_01_intro.scene / scene / 165; mq006_01_intro.scene / scene / 219; mq006_01_intro.scene / scene / 220; mq006_01_intro.scene / scene / 292; +66 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq006.questphase / h12 / 6; mq006.questphase / h498 / 8 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\minor_quests\mq006\mq006.questphase` | content candidate; journal anchor | `base-mq006` |
| `base\quest\minor_quests\mq006\phases\mq006_repeatable_rollercoaster_controller.questphase` | content candidate; journal anchor | `base-mq006` |
| `base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase` | content candidate; forward dependency | `base-mq006` |
| `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` | content candidate; forward dependency | `base-mq006` |
| `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` | content candidate; journal anchor | `base-mq006` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q108](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q108.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

340 repeated typed/socket path signatures in this selected graph context; 64 distinct direct resource identities; 10 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `d7c45735730cd667dcd2` | `base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase` / h7 / 8 -> 7 -> 1 | questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `2f42e8df5c81cf29a5fc` | `base\quest\minor_quests\mq006\mq006.questphase` / h53 / 0 -> 6 -> 53 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questEventManagerNodeDefinition; Out -> In; Out -> In |
| `19665e3783f6f51a7337` | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 1 -> 295 -> 301 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `70a05da84d2007f79060` | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 88 -> 204 -> 210 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnHubNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `95d4997362b664c5c23b` | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 139 -> 134 -> 136 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |
| `276aca4a2dc348a877d5` | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 109 -> 113 -> 521 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `016828d499c85128303c` | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` / scene / 141 -> 222 -> 223 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `1cf9adcdd8714d9f07e3` | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 221 -> 313 -> 316 | questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `0b487c56874911c2ea72` | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` / scene / 415 -> 26 -> 23 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `1d4ec6ef90134c9e080e` | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 57 -> 60 -> 409 | scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `bd44fd6ebe28bd80c073` | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 217 -> 371 -> 318 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 3:0 -> 0:1; 0:0 -> 0:0 |
| `2fd99f4299806c136bfa` | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` / scene / 239 -> 237 -> 235 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\minor_quests\mq006\mq006.questphase` / h0 / 15 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq006\mq006.questphase` / h0 / 50 | `h53` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":31,"socketName":"RideNoQuest"}] |
| `base\quest\minor_quests\mq006\mq006.questphase` / h0 / 51 | `h498` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq006\mq006.questphase` / h0 / 52 | `h558` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq006\mq006.questphase` / h0 / 53 | `h699` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\minor_quests\mq006\mq006.questphase` / h699 / 8 | `h721` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq006\mq006.questphase` / h0 / 55 | `h765` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\minor_quests\mq006\phases\mq006_repeatable_rollercoaster_controller.questphase` / h0 / 23 | `h46` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq006\phases\mq006_repeatable_rollercoaster_controller.questphase` / h0 / 28 | `h95` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase` / h0 / 18 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_stand_2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_rail_lean0__2h_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_wall_lean90__lh_on_hip__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\open_world_master\generic_female_average__stand_rail_lean0__2h_on_rail__ow__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__kneel__rk_on_ground__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_car_emperor__2h_folded__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean0__2h_elbow_on_knees__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean0_rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean180__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_wall_lean180__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__sit_chair__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__sit_chair_lean0__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\female\body\player_locomotion_johnny_guitar.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\male\body\player_locomotion_sick.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\quest\minor_quests\mq006\johnny__sit_rollercoaster__2h_on_chest__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\minor_quests\mq006\sit_rollercoaster__2h_on_chest__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\minor_quests\mq006\sit_rollercoaster__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_01_intro\civ_low_f_114_car_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_01_intro\civ_low_m_110_car_20.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_01_intro\civ_mid_f_71_car_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_01_intro\civ_mid_m_71_car_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_01_intro\civ_mid_m_72_car_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_01_intro\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_02_finale\civ_low_f_114_car_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_02_finale\civ_low_m_110_car_20.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_02_finale\civ_mid_f_71_car_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_02_finale\civ_mid_m_71_car_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_02_finale\civ_mid_m_72_car_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_02_finale\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\lipsync\en\mq006_02_finale\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\car\v_standard3_chevalier_emperor_01\male__sit_car_emperor_lean_back__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_lean_back_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_lean_front__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_lean_front__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__kneel_ground__inspect__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__cheer__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__wait__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_arms_crossed__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_right__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q202\q202_05_convoy\q202__kerry__stand__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\minor_quests\mq006\johnny__sit_rollercoaster_train_lean_back__excited__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\minor_quests\mq006\player__sit_rollercoaster_train_lean_back__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\minor_quests\mq006\player__sit_rollercoaster_train_lean_back__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `air_traffic_start_space_shuttle` | base\gameplay\air_traffic\phases\air_traffic.questphase / h537 / 5; 1 total source locations in compressed evidence |
| `mq006_roller_coaster_fixed` | ep1\quest\minor_quests\mq303\test\mq303_chickentest.scene / scene / 249; ep1\quest\minor_quests\mq303\test\mq303_chickentest.scene / scene / 293; 2 total source locations in compressed evidence |
| `q110_08a_netwatch_deal` | base\quest\minor_quests\mq055\mq055.quest / h37 / 47; base\quest\main_quests\part1\q110\scenes\q110_08a_agent.scene / scene / 547; base\quest\main_quests\part1\q110\scenes\q110_08a_agent.scene / scene / 712; base\quest\main_quests\part1\q110\test\q110_chicken_test.scene / scene / 278; 13 total source locations in compressed evidence |
| `q110_done` | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_sasquatch.quest / h0 / 3; base\quest\minor_quests\mq018\test\mq018_00_chickentest.scene / scene / 88; base\quest\minor_quests\mq025\mq025_psycho_brawl.quest / h0 / 8; base\quest\minor_quests\mq026\test\mq026_00_chickentest.scene / scene / 231; 12 total source locations in compressed evidence |
| `q110_mall_job_active` | base\quest\main_quests\part1\q110\phases\q110_06_mall.questphase / h19 / 50; base\quest\main_quests\part1\q110\phases\q110_06_mall_cleanup.questphase / h0 / 44; 2 total source locations in compressed evidence |
| `sq032_johnnys_motivation` | base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene / scene / 550; 1 total source locations in compressed evidence |

NodeRef uses: 247; TweakDB binding uses: 88. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` | 43 / 416 | scnAudioEvent: 2; scnChangeIdleAnimEvent: 34; scnDialogLineEvent: 85; scnGameplayTransitionEvent: 2; scnIKEvent: 4; scnLookAtEvent: 106; scnPlaySkAnimEvent: 103; scnUnmountEvent: 2; scneventsEquipItemToPerformer: 10; scneventsSetAnimFeatureEvent: 2; scneventsSocket: 61; scneventsUnequipItemFromPerformer: 3; scneventsUnequipItemFromPerformerByItem: 2 |
| `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` | 59 / 333 | scnAudioEvent: 14; scnChangeIdleAnimEvent: 12; scnDialogLineEvent: 74; scnGameplayTransitionEvent: 6; scnIKEvent: 12; scnLookAtEvent: 89; scnPlaySkAnimEvent: 57; scnUnmountEvent: 6; scneventsSetAnimFeatureEvent: 15; scneventsSocket: 48 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
