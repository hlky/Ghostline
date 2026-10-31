# Full Disclosure

Journal: `quests/minor_quest/mq024_sandra` · `MinorQuest` · hash `1278009373`.

Journal premise: Sandra Dorsett… that chick you pulled out of a scavs' nest? Man, give someone an inch and they take a mile… This databank must be pretty special to her if she ain't even willing to go through a fixer. Well, damn… now I'm kinda curious. Gonna help out – or play by the rules of the game?

**Coverage: journal-linked.** 29 exact journal-linked nodes in 10 resources; 12 resources in the inspected dependency context.

Resource roles in that context: 10 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Find Sandra's databank. (Primary) | `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier` |
| Sandra Dorsett who we rescued from scavengers called V and asked to find and retrieve her data carrier. (Primary) | `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra` |
| Meet with Sandra. (Primary) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` |
| Defeat Sandra. (Primary) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_wat_kab_05_openworld.questphase / h789 / 113` (Condition) | `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier` | 113:False → 9:Succeeded; 72:Out1 → 113:In; 113:True → 114:Succeeded |
| `sts_wat_kabuki.questphase / h3924 / 113` (Condition) | `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier` | 113:False → 9:Succeeded; 72:Out1 → 113:In; 113:True → 114:Succeeded |
| `mq024_quest_bugfixes.questphase / h98 / 5` (Condition) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 11:True → 5:In; 5:True → 12:In |
| `mq024_quest_bugfixes.questphase / h98 / 7` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 12:Out → 7:Succeeded; 7:Out → 8:Succeeded |
| `mq024_quest_bugfixes.questphase / h98 / 8` (Journal) | `quests/minor_quest/mq024_sandra` | 7:Out → 8:Succeeded; 8:Out → 9:In |
| `mq024.questphase / h0 / 14` (Journal) | `quests/minor_quest/mq024_sandra/description` | 14:Out → 3:In1; 5:False → 14:Active |
| `mq024.questphase / h0 / 15` (Journal) | `quests/minor_quest/mq024_sandra/description` | 15:Out → 4:In1; 5:True → 15:Active |
| `mq024_02_scavengers.questphase / h0 / 2` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier` | 0:Out → 2:Active; 2:Out → 3:In |
| `mq024_02_scavengers.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier` | 3:Out → 4:Succeeded; 4:Out → 5:In |
| `mq024_03_sandra_apartment.questphase / h0 / 2` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra` | 17:Out → 2:Active; 2:Out → 3:In; 2:Out → 72:Active |
| `mq024_03_sandra_apartment.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra` | 4:Out → 8:Succeeded; 8:Out → 9:Active |
| `mq024_03_sandra_apartment.questphase / h0 / 9` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` | 8:Out → 9:Active; 9:Out → 18:In |
| `mq024_03_sandra_apartment.questphase / h0 / 11` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` | 11:Out → 1:In; 30:False → 11:Succeeded; 11:Out → 62:In |
| `mq024_03_sandra_apartment.questphase / h0 / 49` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 55:False → 49:Active; 49:Out → 52:In |
| `mq024_03_sandra_apartment.questphase / h0 / 50` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 52:Out → 50:Succeeded; 50:Out → 56:In1 |
| `mq024_03_sandra_apartment.questphase / h0 / 57` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` | 57:Out → 54:In; 61:False → 57:Failed |
| `mq024_03_sandra_apartment.questphase / h0 / 72` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra/sandra` | 2:Out → 72:Active |
| `mq024_cleanup.questphase / h0 / 2` (Journal) | `quests/minor_quest/mq024_sandra` | 4:Out → 2:Succeeded; 2:Out → 7:In |
| `mq024_cleanup.questphase / h0 / 24` (Condition) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 24:False → 1:In; 10:True → 24:In; 19:Out1 → 24:In; 24:True → 26:In |
| `mq024_cleanup.questphase / h0 / 25` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 26:Out → 25:Succeeded; 25:Out → 29:In |
| `mq024_02_meet_sandra.scene / scene / 390` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` | 390:0:0 → 396:0:1; 391:0:0 → 390:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq024_02_meet_sandra.scene / scene / 396` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 390:0:0 → 396:0:1; 396:0:0 → 395:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq024_02_meet_sandra.scene / scene / 397` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 397:0:0 → 2:0:0; 440:0:0 → 397:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq024_02_meet_sandra.scene / scene / 443` (MappinManager) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra/sandra_mp` | 265:0:0 → 443:0:1; 443:0:0 → 53:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq024_02_meet_sandra.scene / scene / 542` (Journal) | `quests/minor_quest/mq024_sandra` | 529:1:0 → 542:0:0; 539:0:0 → 542:0:4; 542:0:0 → 527:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `ep1_standalone_quest_bugfixing.questphase / h77 / 29` (Journal) | `quests/minor_quest/mq024_sandra` | 28:Out → 29:Succeeded; 29:Out → 31:Succeeded |
| `ep1_standalone_quest_bugfixing.questphase / h372 / 59` (Journal) | `quests/minor_quest/mq024_sandra/description` | 28:Out → 59:Active; 59:Out → 65:Active |
| `ep1.questphase / h3753 / 29` (Journal) | `quests/minor_quest/mq024_sandra` | 28:Out → 29:Succeeded; 29:Out → 64:Succeeded |
| `ep1.questphase / h4048 / 29` (Journal) | `quests/minor_quest/mq024_sandra/description` | 28:Out → 29:Active; 29:Out → 43:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq024.questphase / h0 / 2` | `base\quest\minor_quests\mq024\phases\mq024_01_hook.questphase` | 17:Out1 → 2:In1; 2:Out1 → 5:In; 2:Out1 → 8:In |
| `mq024.questphase / h0 / 3` | `base\quest\minor_quests\mq024\phases\mq024_02_scavengers.questphase` | 14:Out → 3:In1; 3:Out1 → 4:In1 |
| `mq024.questphase / h0 / 4` | `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` | 3:Out1 → 4:In1; 4:Out1 → 10:In1; 9:Out → 4:In1; 15:Out → 4:In1; 4:Out_door → 10:In_door |
| `mq024.questphase / h0 / 10` | `base\quest\minor_quests\mq024\phases\mq024_cleanup.questphase` | 10:Out1 → 1:In; 4:Out1 → 10:In1; 4:Out_door → 10:In_door |
| `mq024_03_sandra_apartment.questphase / h0 / 5` | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene`; `#mq024_01_sm_call_sandra` | 3:Out → 5:Start 0; 5:End 0 → 4:In; 5:Holocall INT → 41:In; 5:Holocall RET → 40:In |
| `mq024_03_sandra_apartment.questphase / h0 / 10` | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene`; `#mq024_02_sm_meet_sandra` | 54:CutSource → 10:CutDestination; 18:Out → 10:Start 0; 10:End 0 → 30:In; 10:End_killed_door → 74:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\phases\sts_wat_kab_05.questphase` / h0 / 14 | `sts_wat_kab_05_openworld.questphase` | 0: Input; 0:Out → 14:In1; 14:Out1 → 1:In |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h14387 / 14 | `sts_wat_kab_05_openworld.questphase` | 0: Input; 0:Out → 14:In1; 14:Out1 → 1:In |
| `base\open_world\street_stories\watson\sts_watson.questphase` / h0 / 2 | `sts_wat_kabuki.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 4 | `sts_wat_kabuki.questphase` | 0: Start; 0:Out → 4:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h15 / 5 | `sts_wat_kabuki.questphase` | 0: Input; 0:Out → 5:In1 |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 43 | `mq024_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 43:In1 |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 9 | `mq024.questphase` | 172: Condition: mq024_done GreaterOrEqual 1; 172:False → 9:In1 |
| `base\quest\minor_quests\mq024\mq024.quest` / h0 / 2 | `mq024.questphase` | 9: TeleportPuppet; 7: PauseCondition; 8: Condition: mq024_test_with_sts GreaterOrEqual 1; 8: Condition: mq024_test_with_sts GreaterOrEqual 1; 2:Out1 → 1:In; 9:Out → 2:test_has_carrier; 7:Out → 2:In1; 8:False → 2:In1; 8:True → 2:In1 |
| `base\quest\minor_quests\mq024\mq024.questphase` / h0 / 2 | `mq024_01_hook.questphase` | 17: LogicalAnd; 17:Out1 → 2:In1; 2:Out1 → 5:In; 2:Out1 → 8:In |
| `base\quest\minor_quests\mq024\mq024.questphase` / h0 / 3 | `mq024_02_scavengers.questphase` | 14: Journal; 14:Out → 3:In1; 3:Out1 → 4:In1 |
| `base\quest\minor_quests\mq024\mq024.questphase` / h0 / 4 | `mq024_03_sandra_apartment.questphase` | 3: Phase: mq024_02_scavengers.questphase; 9: Input; 15: Journal; 3:Out1 → 4:In1; 4:Out1 → 10:In1; 9:Out → 4:In1; 15:Out → 4:In1; 4:Out_door → 10:In_door |
| `base\quest\minor_quests\mq024\mq024.questphase` / h0 / 10 | `mq024_cleanup.questphase` | 4: Phase: mq024_03_sandra_apartment.questphase; 4: Phase: mq024_03_sandra_apartment.questphase; 10:Out1 → 1:In; 4:Out1 → 10:In1; 4:Out_door → 10:In_door |
| `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` / h0 / 5 | `mq024_01_call_sandra.scene` | 3: PauseCondition; 3:Out → 5:Start 0; 5:End 0 → 4:In; 5:Holocall INT → 41:In; 5:Holocall RET → 40:In |
| `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` / h0 / 10 | `mq024_02_meet_sandra.scene` | 54: CutControl; 18: PauseCondition; 54:CutSource → 10:CutDestination; 18:Out → 10:Start 0; 10:End 0 → 30:In; 10:End_killed_door → 74:In |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 7 | `ep1_standalone_quest_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 7:In1 |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\sts_wat_kab_05.quest` / h0 / 4 | `sts_wat_kab_05.questphase` | 7: FactsDBManager: kab_05_testdef; 7:Out → 4:In1 |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` / h0 / 10 | `sts_wat_kab_05.questphase` | 57: FactsDBManager: kab_05_activated; 57:Out → 10:In1; 10:Out1 → 78:In |
| `base\quest\minor_quests\mq024\mq024.quest` / h0 / 3 | `sts_wat_kab_05.questphase` | 4: PauseCondition: mq024_test_with_sts GreaterOrEqual 1; 4:Out → 3:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 7 | `sts_watson.questphase` | 0: Input; 0:Out → 7:In1 |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
| `ep1\quest\ep1.questphase` / h58 / 2 | `ep1_bugfixing.questphase` | 25: LogicalXor; 2:CP77-65722_out → 27:In; 2:CP77-64292_out → 26:In; 25:Out1 → 2:In1; 2:Out1 → 4:In2; 2:growl → 4:growl |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 12 | `ep1_bugfixing.questphase` | 11: LogicalHub; 11:Out1 → 12:In1 |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 5 | `ep1_bugfixing.questphase` | 4: LogicalHub; 4:Out1 → 5:In1 |
| `base\open_world\community\heywood\wellsprings\hey_spr_quest.quest` / h0 / 4 | `street_stories.questphase` | 1: Start; 1:Out → 4:In1 |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest` / h0 / 21 | `street_stories.questphase` | 0: Start; 0:Out → 21:In1 |
| `base\open_world\phases\open_world_content.questphase` / h0 / 2 | `street_stories.questphase` | 33: PauseCondition: sts_loop_start; 122: Input; 33:Out → 2:In1; 122:Out → 2:In1 |
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
| `mq024_01_call_sandra.scene` | Start 0 → End 0 | sandra; Player; 23 nodes / 26 edges |
| `mq024_02_meet_sandra.scene` | Start 0, prev_cross, prev_good_normal → End 0, End_killed_door | sandra; Player; 132 nodes / 152 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq024_01_call_sandra.scene / n6 / 0` | Yep. (``) | No option-level predicate stored | 0:0 → 8:0:0 |
| `mq024_01_call_sandra.scene / n6 / 1` | Glad you're holding up. (``) | No option-level predicate stored | 0:1 → 23:0:0 |
| `mq024_01_call_sandra.scene / n11 / 0` | You're safe now. (``) | No option-level predicate stored | 0:0 → 13:0:0 |
| `mq024_01_call_sandra.scene / n11 / 1` | I don't think I'm the right person to talk to... (``) | No option-level predicate stored | 0:1 → 14:0:0 |
| `mq024_01_call_sandra.scene / n26 / 0` | Sure thing. (``) | No option-level predicate stored | 0:0 → 28:0:0 |
| `mq024_01_call_sandra.scene / n26 / 1` | Jackie's dead. (``) | No option-level predicate stored | 0:1 → 29:0:0 |
| `mq024_02_meet_sandra.scene / n8 / 0` | [Hand over databank] Got it right here. (`give`) | No option-level predicate stored | 0:0 → 10:0:0; 0:0 → 115:1:0; 0:0 → 120:1:0; 0:0 → 121:1:0; 0:0 → 507:0:1 |
| `mq024_02_meet_sandra.scene / n8 / 1` | What are you worried about? (`Option`) | No option-level predicate stored | 0:1 → 90:0:0 |
| `mq024_02_meet_sandra.scene / n12 / 0` | Of course not. (`no`) | No option-level predicate stored | 0:0 → 14:0:1 |
| `mq024_02_meet_sandra.scene / n12 / 1` | Yes, I did. (`yes`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq024_hacked_data_carrier", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:1 → 43:0:1 |
| `mq024_02_meet_sandra.scene / n18 / 0` | It couldn't have been me. (`still lie`) | No option-level predicate stored | 0:0 → 20:0:0 |
| `mq024_02_meet_sandra.scene / n18 / 1` | Alright, you got me. (`admit`) | No option-level predicate stored | 0:1 → 23:0:0 |
| `mq024_02_meet_sandra.scene / n25 / 0` | I wanna congratulate you. (`good job`) | No option-level predicate stored | 0:0 → 27:0:0 |
| `mq024_02_meet_sandra.scene / n25 / 1` | Blackmail you, of course. (`blackmail`) | No option-level predicate stored | 0:1 → 37:0:0 |
| `mq024_02_meet_sandra.scene / n25 / 2` | Nothing. (`dont care`) | No option-level predicate stored | 0:2 → 480:0:1 |
| `mq024_02_meet_sandra.scene / n29 / 0` | What daemons did you use? (`blueline`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "125694326540", "buildId": "95189197130", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:0 → 492:0:1 |
| `mq024_02_meet_sandra.scene / n29 / 1` | What they're doing... how's it even possible? (`continue`) | No option-level predicate stored | 0:1 → 487:0:1 |
| `mq024_02_meet_sandra.scene / n49 / 0` | [Knock] (`knock`) | No option-level predicate stored | 0:0 → 66:0:1; 0:0 → 110:0:0 |
| `mq024_02_meet_sandra.scene / n94 / 0` | How much for keeping my mouth shut? (`Option_01`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "128271491759", "buildId": "74910219395", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:0 → 93:0:0; 0:0 → 435:0:1 |
| `mq024_02_meet_sandra.scene / n94 / 1` | I was just kidding. (`Option_02`) | No option-level predicate stored | 0:1 → 483:0:1 |
| `mq024_02_meet_sandra.scene / n115 / 0` | You have good taste. (`compliment`) | No option-level predicate stored | 0:0 → 126:0:2 |
| `mq024_02_meet_sandra.scene / n120 / 0` | Cozy place. (`compliment`) | No option-level predicate stored | 0:0 → 126:0:1 |
| `mq024_02_meet_sandra.scene / n121 / 0` | Nice digs. (`compliment`) | No option-level predicate stored | 0:0 → 126:0:0 |
| `mq024_02_meet_sandra.scene / n200 / 0` | [Knock] Sandra? (`knock`) | No option-level predicate stored | 0:0 → 50:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CP77-48800` | mq024_quest_bugfixes.questphase / h37 / 3 | mq024_quest_bugfixes.questphase / h37 / 2 |
| `CP77-65021` | mq024_quest_bugfixes.questphase / h98 / 3 | mq024_quest_bugfixes.questphase / h98 / 2 |
| `CYB-12345` | mq024_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `codex_sandra_dorsett` | mq024_01_hook.questphase / h0 / 12; mq024_quest_bugfixes.questphase / h37 / 5 | mq024_quest_bugfixes.questphase / h37 / 4 |
| `holo_v_calls_sandra_dorsett_end_activate` | mq024_01_call_sandra.scene / scene / 117; mq024_03_sandra_apartment.questphase / h0 / 41 | No reader in selected context |
| `holo_v_calls_sandra_dorsett_end_done` | mq024_01_call_sandra.scene / scene / 112 | mq024_01_call_sandra.scene / scene / 111 |
| `holo_v_calls_sandra_dorsett_start_activate` | mq024_01_call_sandra.scene / scene / 116; mq024_03_sandra_apartment.questphase / h0 / 40 | No reader in selected context |
| `holo_v_calls_sandra_dorsett_start_done` | mq024_01_call_sandra.scene / scene / 110 | mq024_01_call_sandra.scene / scene / 109 |
| `kab_05_activated` | Producer outside selected context | mq024.questphase / h0 / 16 |
| `mq024_active` | mq024_01_hook.questphase / h0 / 9; mq024_cleanup.questphase / h0 / 3 | mq024_quest_bugfixes.questphase / h37 / 4 |
| `mq024_admit_that_looked` | mq024_02_meet_sandra.scene / scene / 43 | No reader in selected context |
| `mq024_combat_sandra` | mq024_02_meet_sandra.scene / scene / 416 | mq024_03_sandra_apartment.questphase / h0 / 30; mq024_03_sandra_apartment.questphase / h0 / 61; mq024_cleanup.questphase / h0 / 10 |
| `mq024_done` | mq024_cleanup.questphase / h0 / 4 | mq024_quest_bugfixes.questphase / h37 / 4; mq024_quest_bugfixes.questphase / h98 / 11 |
| `mq024_hacked_data_carrier` | Producer outside selected context | mq024_02_meet_sandra.scene / scene / 12; mq024_02_meet_sandra.scene / scene / 14; mq024_03_sandra_apartment.questphase / h0 / 13 |
| `mq024_hook_taken` | mq024.questphase / h0 / 8 | No reader in selected context |
| `mq024_sandra_opened_door` | mq024_02_meet_sandra.scene / scene / 469 | mq024_03_sandra_apartment.questphase / h0 / 44 |
| `q101_done` | Producer outside selected context | mq024.questphase / h0 / 13 |
| `q305_haunted_weapon_random_whisper_02` | mq024_03_sandra_apartment.questphase / h0 / 76 | No reader in selected context |
| `q305_haunted_weapon_random_whisper_02_used` | Producer outside selected context | mq024_03_sandra_apartment.questphase / h0 / 75 |
| `travelling_merchant_lives` | Producer outside selected context | mq024_quest_bugfixes.questphase / h0 / 15 |

## Exact gates, joins and cancellation

<details><summary>63 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_wat_kab_05_openworld.questphase / h789 / 72` | `questLogicalXorNodeDefinition` `{}` | 70:Out → 72:In1; 71:Out → 72:In2; 72:Out1 → 113:In |
| `sts_wat_kab_05_openworld.questphase / h789 / 113` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 113:False → 9:Succeeded; 72:Out1 → 113:In; 113:True → 114:Succeeded |
| `sts_wat_kabuki.questphase / h3924 / 72` | `questLogicalXorNodeDefinition` `{}` | 70:Out → 72:In1; 71:Out → 72:In2; 72:Out1 → 113:In |
| `sts_wat_kabuki.questphase / h3924 / 113` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 113:False → 9:Succeeded; 72:Out1 → 113:In; 113:True → 114:Succeeded |
| `mq024_quest_bugfixes.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 17:Out1 → 15:In |
| `mq024_quest_bugfixes.questphase / h37 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-48800"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq024_quest_bugfixes.questphase / h37 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_active"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_done"}}]},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"codex_sandra_dorsett","value":1,"comparisonType":"Less"}}]}}` | 3:Out → 4:In; 4:True → 5:In |
| `mq024_quest_bugfixes.questphase / h98 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-65021"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq024_quest_bugfixes.questphase / h98 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 3:Out → 4:In; 4:Out → 11:In |
| `mq024_quest_bugfixes.questphase / h98 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 11:True → 5:In; 5:True → 12:In |
| `mq024_quest_bugfixes.questphase / h98 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"GreaterOrEqual"}}}` | 8:Out → 9:In; 9:Out → 10:In |
| `mq024_quest_bugfixes.questphase / h98 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_done"}}}` | 4:Out → 11:In; 11:True → 5:In |
| `mq024_quest_bugfixes.questphase / h98 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 5:True → 12:In; 12:Out → 7:Succeeded |
| `mq024.questphase / h0 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"134302024498","quantity":1}}}` | 2:Out1 → 5:In; 5:True → 15:Active; 5:False → 14:Active |
| `mq024.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 13:In; 13:Out → 17:In1 |
| `mq024.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_05_activated","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 16:In; 16:Out → 17:In2 |
| `mq024.questphase / h0 / 17` | `questLogicalAndNodeDefinition` `{}` | 17:Out1 → 2:In1; 13:Out → 17:In1; 16:Out → 17:In2 |
| `mq024_02_scavengers.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"134302024498","quantity":1}}}` | 2:Out → 3:In; 3:Out → 4:Succeeded |
| `mq024_03_sandra_apartment.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhone_ConditionType","caller":{"$type":"gameJournalPath","realPath":"contacts/player","fileEntryIndex":1,"className":"gameJournalContact"},"addressee":{"$type":"gameJournalPath","realPath":"contacts/sandra_dorsett","fileEntryIndex":1,"className":"gameJournalContact"}}}}` | 2:Out → 3:In; 3:Out → 5:Start 0 |
| `mq024_03_sandra_apartment.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_hacked_data_carrier","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 13:In; 13:Out → 73:In; 13:Out → 77:In |
| `mq024_03_sandra_apartment.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"LessOrEqual"}}}` | 9:Out → 18:In; 18:Out → 10:Start 0; 18:Out → 35:In; 18:Out → 44:In |
| `mq024_03_sandra_apartment.questphase / h0 / 30` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_combat_sandra","value":1,"comparisonType":"GreaterOrEqual"}}}` | 30:True → 1:In; 10:End 0 → 30:In; 30:False → 11:Succeeded |
| `mq024_03_sandra_apartment.questphase / h0 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0},"comparisonType":"GreaterOrEqual"}}}` | 35:Out → 36:In; 36:Out → 37:In |
| `mq024_03_sandra_apartment.questphase / h0 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0},"comparisonType":"LessOrEqual"}}}` | 38:Out → 35:In; 37:Out → 38:In |
| `mq024_03_sandra_apartment.questphase / h0 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterQuickHacked_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}}}}` | 44:Out → 42:In; 42:Out → 53:In1 |
| `mq024_03_sandra_apartment.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType"}}}` | 44:Out → 43:In; 43:Out → 53:In2 |
| `mq024_03_sandra_apartment.questphase / h0 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_sandra_opened_door","value":1,"comparisonType":"GreaterOrEqual"}}}` | 18:Out → 44:In; 44:Out → 42:In; 44:Out → 43:In; 44:Out → 58:In; 44:Out → 60:In |
| `mq024_03_sandra_apartment.questphase / h0 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 49:Out → 52:In; 52:Out → 50:Succeeded |
| `mq024_03_sandra_apartment.questphase / h0 / 53` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 42:Out → 53:In1; 43:Out → 53:In2; 58:Out → 53:In3; 60:Out → 53:In4; 53:Out1 → 61:In; 53:Out1 → 65:In |
| `mq024_03_sandra_apartment.questphase / h0 / 54` | `questCutControlNodeDefinition` `{}` | 54:CutSource → 10:CutDestination; 54:Out → 45:In; 57:Out → 54:In |
| `mq024_03_sandra_apartment.questphase / h0 / 55` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 55:False → 49:Active; 67:Out → 55:In; 55:True → 56:In1 |
| `mq024_03_sandra_apartment.questphase / h0 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","slotName":"mq024_sandra"},"isPlayer":false}}}` | 44:Out → 58:In; 58:Out → 53:In3 |
| `mq024_03_sandra_apartment.questphase / h0 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 44:Out → 60:In; 60:Out → 53:In4 |
| `mq024_03_sandra_apartment.questphase / h0 / 61` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_combat_sandra","value":1,"comparisonType":"GreaterOrEqual"}}}` | 53:Out1 → 61:In; 61:False → 57:Failed |
| `mq024_03_sandra_apartment.questphase / h0 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 11:Out → 62:In; 62:Out → 63:In |
| `mq024_03_sandra_apartment.questphase / h0 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 4:Out → 68:In; 68:Out → 69:In |
| `mq024_03_sandra_apartment.questphase / h0 / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 69:Out → 64:In; 68:Out → 69:In |
| `mq024_03_sandra_apartment.questphase / h0 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq024_sandras_turret","deviceControllerClass":"SecurityTurretControllerPS","deviceConditionFunction":"IsON"}}}` | 70:Out → 71:In |
| `mq024_03_sandra_apartment.questphase / h0 / 75` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q305_haunted_weapon_random_whisper_02_used"}}}` | 78:Out → 75:In; 75:False → 76:In |
| `mq024_03_sandra_apartment.questphase / h0 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questUICondition","type":{"$type":"questMenuState_ConditionType","state":"Closed"}}}` | 13:Out → 77:In; 77:Out → 78:In |
| `mq024_03_sandra_apartment.questphase / h0 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":100}}}` | 78:Out → 75:In; 77:Out → 78:In |
| `mq024_cleanup.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"GreaterOrEqual"}}}` | 5:Out → 8:In; 8:Out → 10:In |
| `mq024_cleanup.questphase / h0 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_combat_sandra","value":1,"comparisonType":"GreaterOrEqual"}}}` | 8:Out → 10:In; 10:True → 24:In; 10:False → 11:In |
| `mq024_cleanup.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 11:Out → 18:In; 18:Out → 12:In; 18:Out → 19:In2 |
| `mq024_cleanup.questphase / h0 / 19` | `questLogicalAndNodeDefinition` `{}` | 16:Success → 19:In1; 18:Out → 19:In2; 19:Out1 → 24:In |
| `mq024_cleanup.questphase / h0 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"GreaterOrEqual"}}}` | 21:Out → 22:In; 22:Out → 23:In |
| `mq024_cleanup.questphase / h0 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 24:False → 1:In; 10:True → 24:In; 19:Out1 → 24:In; 24:True → 26:In |
| `mq024_cleanup.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 24:True → 26:In; 26:Out → 25:Succeeded |
| `mq024_cleanup.questphase / h0 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"GreaterOrEqual"}}}` | 25:Out → 29:In; 29:Out → 30:In |
| `mq024_01_call_sandra.scene / scene / 109` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_v_calls_sandra_dorsett_start_done"}}}` | 109:0:0 → 110:0:1; 116:0:0 → 109:0:1 |
| `mq024_01_call_sandra.scene / scene / 111` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_v_calls_sandra_dorsett_end_done"}}}` | 111:0:0 → 112:0:1; 117:0:0 → 111:0:1 |
| `mq024_02_meet_sandra.scene / scene / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_hacked_data_carrier","value":1,"comparisonType":"GreaterOrEqual"}}}` | 12:0:0 → 14:0:1; 14:0:0 → 16:0:0; 14:0:1 → 476:0:1 |
| `mq024_02_meet_sandra.scene / scene / 209` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 203:0:0 → 209:0:1; 209:0:0 → 208:0:1 |
| `mq024_02_meet_sandra.scene / scene / 215` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 212:0:0 → 215:0:1; 215:0:0 → 214:0:1 |
| `mq024_02_meet_sandra.scene / scene / 226` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 223:0:0 → 226:0:1; 226:0:0 → 225:0:1 |
| `mq024_02_meet_sandra.scene / scene / 238` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 235:0:0 → 238:0:1; 238:0:0 → 237:0:1 |
| `mq024_02_meet_sandra.scene / scene / 245` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 242:0:0 → 245:0:1; 245:0:0 → 244:0:1 |
| `mq024_02_meet_sandra.scene / scene / 259` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 256:0:0 → 259:0:1; 259:0:0 → 258:0:1 |
| `mq024_02_meet_sandra.scene / scene / 266` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 50:0:0 → 266:0:1; 266:0:0 → 265:0:0 |
| `mq024_02_meet_sandra.scene / scene / 395` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 395:0:0 → 440:0:1; 396:0:0 → 395:0:1 |
| `mq024_02_meet_sandra.scene / scene / 514` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 508:0:0 → 514:0:1; 514:0:0 → 133:0:1 |
| `mq024_02_meet_sandra.scene / scene / 522` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}}}}` | 1:0:0 → 522:0:1; 522:0:0 → 539:0:0; 529:1:0 → 522:0:0 |
| `mq024_02_meet_sandra.scene / scene / 536` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq024_ss_sandra","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 1:0:0 → 536:0:1; 529:1:0 → 536:0:0; 536:0:0 → 539:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq024_03_sandra_apartment.questphase / h0 / 68 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq024_02_meet_sandra.scene / scene / 273 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `call_lifecycle` | mq024_01_hook.questphase / h0 / 4 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `checkpoint` | mq024_01_hook.questphase / h0 / 10; mq024_02_meet_sandra.scene / scene / 69; mq024_02_scavengers.questphase / h0 / 5; mq024_cleanup.questphase / h0 / 5 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq024_01_call_sandra.scene / scene / 11; mq024_01_call_sandra.scene / scene / 26; mq024_01_call_sandra.scene / scene / 6; mq024_02_meet_sandra.scene / scene / 115; +10 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq024_02_meet_sandra.scene / scene / 392; mq024_02_meet_sandra.scene / scene / 394 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq024_02_meet_sandra.scene / scene / 476; mq024_02_meet_sandra.scene / scene / 480; mq024_02_meet_sandra.scene / scene / 483; mq024_02_meet_sandra.scene / scene / 487; +7 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq024.questphase / h0 / 13; mq024.questphase / h0 / 16; mq024_01_call_sandra.scene / scene / 109; mq024_01_call_sandra.scene / scene / 111; +13 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq024_03_sandra_apartment.questphase / h0 / 35; mq024_03_sandra_apartment.questphase / h0 / 37; mq024_cleanup.questphase / h0 / 21; mq024_cleanup.questphase / h0 / 6; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq024_02_meet_sandra.scene / scene / 393; mq024_03_sandra_apartment.questphase / h0 / 46 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | mq024_02_meet_sandra.scene / scene / 435; mq024_02_meet_sandra.scene / scene / 440; mq024_02_meet_sandra.scene / scene / 53; mq024_02_meet_sandra.scene / scene / 55; +5 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | mq024_02_meet_sandra.scene / scene / 536; mq024_03_sandra_apartment.questphase / h0 / 70 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `item_state` | mq024.questphase / h0 / 5; mq024_02_scavengers.questphase / h0 / 3 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | ep1.questphase / h3753 / 28; ep1.questphase / h3753 / 29; ep1.questphase / h3753 / 64; ep1.questphase / h4048 / 28; +33 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | mq024.questphase / h0 / 17; mq024_cleanup.questphase / h0 / 19 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq024.questphase / h0 / 8; mq024_01_call_sandra.scene / scene / 110; mq024_01_call_sandra.scene / scene / 112; mq024_01_call_sandra.scene / scene / 116; +15 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq024_03_sandra_apartment.questphase / h0 / 53; sts_wat_kab_05_openworld.questphase / h789 / 72; sts_wat_kabuki.questphase / h3924 / 72 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq024_02_meet_sandra.scene / scene / 209; mq024_02_meet_sandra.scene / scene / 215; mq024_02_meet_sandra.scene / scene / 226; mq024_02_meet_sandra.scene / scene / 238; +9 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq024_03_sandra_apartment.questphase / h0 / 54 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq024_02_meet_sandra.scene / scene / 255; mq024_02_meet_sandra.scene / scene / 72; mq024_02_meet_sandra.scene / scene / 75; mq024_02_meet_sandra.scene / scene / 81; +3 locations in catalogue.json | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq024_03_sandra_apartment.questphase / h0 / 10; mq024_03_sandra_apartment.questphase / h0 / 5 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `target_resolution` | mq024_02_meet_sandra.scene / scene / 395; mq024_03_sandra_apartment.questphase / h0 / 52; mq024_03_sandra_apartment.questphase / h0 / 55; mq024_03_sandra_apartment.questphase / h0 / 60; +2 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | mq024_02_meet_sandra.scene / scene / 140; mq024_02_meet_sandra.scene / scene / 141; mq024_02_meet_sandra.scene / scene / 153; mq024_02_meet_sandra.scene / scene / 155; +16 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\phases\sts_wat_kab_05_openworld.questphase` | content candidate; journal anchor | `base-sts-wat-kab-05` |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` | repair; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\mq024.questphase` | content candidate; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\phases\mq024_01_hook.questphase` | content candidate; forward dependency | `base-mq024` |
| `base\quest\minor_quests\mq024\phases\mq024_02_scavengers.questphase` | content candidate; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` | content candidate; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\phases\mq024_cleanup.questphase` | content candidate; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` | content candidate; forward dependency | `base-mq024` |
| `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` | content candidate; journal anchor | `base-mq024` |
| `ep1\quest\bugfixing\ep1_standalone_quest_bugfixing.questphase` | repair; journal anchor | `ep1-shared` |
| `ep1\quest\ep1.questphase` | content candidate; journal anchor | `ep1-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-wat-kab-05](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-wat-kab-05.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

144 repeated typed/socket path signatures in this selected graph context; 52 distinct direct resource identities; 3 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 116 -> 109 -> 110 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 114 -> 117 -> 111 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `26762f051e7728f090ca` | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 110 -> 113 -> 4 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 19 -> 114 -> 117 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` / h37 / 0 -> 2 -> 3 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `7e7dbbc930b3717fd790` | `ep1\quest\bugfixing\ep1_standalone_quest_bugfixing.questphase` / h372 / 28 -> 59 -> 65 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `c1b6601d2f647c8a694d` | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 16 -> 18 -> 20 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `e70b0765e99ad324f9b7` | `base\quest\minor_quests\mq024\phases\mq024_cleanup.questphase` / h0 / 0 -> 3 -> 4 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `0b487c56874911c2ea72` | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 50 -> 266 -> 265 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `1fa539921730278ef7fb` | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 18 -> 20 -> 181 | scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `1d4ec6ef90134c9e080e` | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 18 -> 20 -> 153 | scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `642f6926d840e7c88178` | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 109 -> 110 -> 113 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]; 0:0 -> 0:1; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` / h0 / 14 | `h37` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` / h0 / 18 | `h98` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test_03_02.gamedef` | content candidate | base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest |
| `base\open_world\district_definitions\open_world_kabuki.gamedef` | content candidate | base\open_world\district_definitions\open_world_kabuki.quest |
| `base\open_world\open_world_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\police_system\police_system_test.gamedef` | content candidate | base\open_world\police_system\police_system_test.quest |
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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\sts_wat_kab_05.gamedef` | content candidate | base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\sts_wat_kab_05.quest |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\sts_wat_kab_05_nc.gamedef` | content candidate | base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\sts_wat_kab_05.quest |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\sts_wat_kab_05_testdef.gamedef` | content candidate | base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\sts_wat_kab_05.quest |
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
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest; ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest; ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_stand_2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__2h_tablet__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q112\q112_10_safe_house\body\q112_10_safe_house__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\synced\synced__passing_item_to_player__female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\synced\synced__passing_item_to_player__player.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\phases\sts_wat_kab_04.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\phases\sts_wat_kab_04_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\phases\sts_wat_kab_04_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\phases\sts_wat_kab_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\phases\sts_wat_kab_05_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\phases\sts_wat_kab_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_07\phase\sts_wat_kab_07.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_07\phase\sts_wat_kab_07_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_07\phase\sts_wat_kab_07_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\phases\sts_wat_kab_08.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\phases\sts_wat_kab_08_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\phases\sts_wat_kab_08_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq024\phases\mq024_01_hook.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq024\phases\mq024_02_scavengers.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq024\phases\mq024_cleanup.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq024\scenes\lipsync\en\mq024_01_call_sandra\civ_high_f_01_enus_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq024\scenes\lipsync\en\mq024_01_call_sandra\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq024\scenes\lipsync\en\mq024_02_meet_sandra\civ_high_f_01_enus_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq024\scenes\lipsync\en\mq024_02_meet_sandra\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__wait__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_tablet__use__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `codex_sandra_dorsett` | ep1\quest\main_quests\q305\phases\q305_01_task.questphase / h83 / 117; 1 total source locations in compressed evidence |
| `holo_v_calls_sandra_dorsett_end_activate` | base\quest\holocalls\sandra\sandra_holocall.questphase / h0 / 13; ep1\quest\main_quests\q305\phases\q305_01_task.questphase / h510 / 170; ep1\quest\main_quests\q305\scenes\q305_01_holocalls_to_netrunner.scene / scene / 535; ep1\quest\main_quests\q305\scenes\q305_01_holocalls_to_netrunner.scene / scene / 779; 5 total source locations in compressed evidence |
| `holo_v_calls_sandra_dorsett_end_done` | base\quest\holocalls\sandra\sandra_holocall.scene / scene / 44; base\quest\holocalls\sandra\sandra_holocall.scene / scene / 578; ep1\quest\main_quests\q305\phases\q305_01_task.questphase / h510 / 172; ep1\quest\main_quests\q305\scenes\q305_01_holocalls_to_netrunner.scene / scene / 527; 6 total source locations in compressed evidence |
| `holo_v_calls_sandra_dorsett_start_activate` | base\quest\holocalls\sandra\sandra_holocall.questphase / h0 / 12; ep1\quest\main_quests\q305\phases\q305_01_task.questphase / h510 / 232; ep1\quest\main_quests\q305\scenes\q305_01_holocalls_to_netrunner.scene / scene / 533; ep1\quest\main_quests\q305\scenes\q305_01_holocalls_to_netrunner.scene / scene / 561; 4 total source locations in compressed evidence |
| `holo_v_calls_sandra_dorsett_start_done` | base\quest\holocalls\sandra\sandra_holocall.scene / scene / 43; base\quest\holocalls\sandra\sandra_holocall.scene / scene / 600; ep1\quest\main_quests\q305\phases\q305_01_task.questphase / h510 / 235; ep1\quest\main_quests\q305\scenes\q305_01_holocalls_to_netrunner.scene / scene / 523; 5 total source locations in compressed evidence |
| `kab_05_activated` | base\quest\minor_quests\mq024\mq024.quest / h0 / 13; base\open_world\street_stories\watson\kabuki\sts_wat_kabuki.questphase / h0 / 57; 2 total source locations in compressed evidence |
| `mq024_admit_that_looked` | base\quest\minor_quests\mq055\mq055.quest / h37 / 50; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 613; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 770; ep1\quest\ep1.questphase / h2539 / 57; 5 total source locations in compressed evidence |
| `mq024_combat_sandra` | ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 1024; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 1028; 2 total source locations in compressed evidence |
| `mq024_done` | base\quest\minor_quests\mq055\mq055.quest / h37 / 49; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 585; ep1\quest\main_quests\q305\scenes\debug\q305_xx_chicken_test.scene / scene / 611; ep1\quest\ep1.questphase / h2539 / 56; 5 total source locations in compressed evidence |
| `q101_done` | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\test\ma_wat_lch_06_chicken_test.scene / scene / 6; base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest / h0 / 24; base\quest\minor_quests\mq010\mq010.quest / h0 / 12; base\quest\minor_quests\mq018\phases\mq018_00_chickentest.questphase / h0 / 27; 51 total source locations in compressed evidence |
| `q305_haunted_weapon_random_whisper_02` | base\quest\minor_quests\mq016\phases\mq016_01_freezer.questphase / h0 / 18; base\quest\main_quests\part1\q116\scenes\q116_04_mikoshi_intro.scene / scene / 3745; ep1\quest\minor_quests\mq305\scenes\mq305_04_bunker.scene / scene / 5138; ep1\quest\main_quests\q305\phases\q305_12_haunted_weapon.questphase / h19 / 52; 6 total source locations in compressed evidence |
| `q305_haunted_weapon_random_whisper_02_used` | ep1\quest\main_quests\q305\scenes\q305_16_haunted_weapons_reactions.scene / scene / 164; 1 total source locations in compressed evidence |

NodeRef uses: 118; TweakDB binding uses: 69. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` | 8 / 34 | scnDialogLineEvent: 33; scneventsSocket: 1 |
| `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` | 21 / 165 | scnAudioEvent: 3; scnDialogLineEvent: 65; scnGameplayTransitionEvent: 2; scnIKEvent: 4; scnLookAtEvent: 6; scnPlaySkAnimEvent: 31; scnPoseCorrectionEvent: 6; scnUnmountEvent: 2; scneventsAttachPropToPerformer: 2; scneventsAttachPropToWorld: 2; scneventsEquipItemToPerformer: 6; scneventsSetAnimFeatureEvent: 2; scneventsSocket: 34 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
