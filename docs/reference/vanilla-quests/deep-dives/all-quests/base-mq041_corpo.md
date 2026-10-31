# War Pigs

Journal: `quests/minor_quest/mq041_corpo` · `MinorQuest` · hash `479196099`.

**Coverage: journal-linked.** 24 exact journal-linked nodes in 4 resources; 6 resources in the inspected dependency context.

Resource roles in that context: 5 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| A voice from beyond the grave, the promise of dirt on old enemies… I'll admit, I'm a little curious. But in your shoes, I'd be careful with this one. Corpos are like wasps – they can sting even after they're dead. (Primary) | `quests/minor_quest/mq041_corpo/corpo/01_find_the_briefcase` |
| Talk to Johnny. (Primary) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny` |
| Move the dumpster. (Primary) | `quests/minor_quest/mq041_corpo/corpo/01b_lift_the_dumpster` |
| Open the briefcase. (Primary) | `quests/minor_quest/mq041_corpo/corpo/02_open_the_briefcase` |
| Talk to the stranger. (Primary) | `quests/minor_quest/mq041_corpo/corpo/03_talk_with_stranger` |
| Confront Frank. (Primary) | `quests/minor_quest/mq041_corpo/corpo/04_confront_frank` |
| Talk to Johnny. (Optional) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq041_quest_bugfixes.questphase / h7 / 9` (Condition) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny` | 2:Out → 9:In; 9:True → 10:In |
| `mq041_quest_bugfixes.questphase / h77 / 10` (Condition) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny` | 10:False → 1:In; 19:False → 10:In; 10:True → 11:In |
| `mq041_corpo_01_hook.questphase / h0 / 5` (Journal) | `quests/minor_quest/mq041_corpo/corpo/01_find_the_briefcase` | 9:Out → 5:Active; 16:Out → 5:Active; 5:Out → 13:Active |
| `mq041_corpo_01_hook.questphase / h0 / 13` (Journal) | `quests/minor_quest/mq041_corpo/corpo/01_find_the_briefcase/description` | 5:Out → 13:Active; 13:Out → 7:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 7` (Journal) | `quests/minor_quest/mq041_corpo/corpo/01_find_the_briefcase` | 7:Out → 5:Start 0; 44:Out → 7:Succeeded; 7:Out → 42:In1 |
| `mq041_corpo_02_confrontation.questphase / h0 / 32` (Condition) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny` | 30:Out1 → 32:In; 32:True → 31:In |
| `mq041_corpo_02_confrontation.scene / scene / 5` (Journal) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1` | 1:0:0 → 5:0:1; 5:0:0 → 147:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 12` (Journal) | `quests/minor_quest/mq041_corpo/corpo/02_open_the_briefcase` | 12:0:0 → 14:0:0; 1158:0:0 → 12:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 63` (Journal) | `quests/minor_quest/mq041_corpo/corpo/03_talk_with_stranger` | 63:0:0 → 29:0:0; 258:0:0 → 63:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 66` (Journal) | `quests/minor_quest/mq041_corpo/corpo/03_talk_with_stranger` | 29:0:0 → 66:0:3; 66:0:0 → 67:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 67` (Journal) | `quests/minor_quest/mq041_corpo/corpo/04_confront_frank` | 66:0:0 → 67:0:1; 67:0:0 → 39:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 219` (Journal) | `quests/minor_quest/mq041_corpo/corpo/02_open_the_briefcase` | 219:0:0 → 7:0:0; 219:0:0 → 20:0:1; 225:0:0 → 219:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 222` (Journal) | `quests/minor_quest/mq041_corpo/corpo/01b_lift_the_dumpster` | 1:0:0 → 222:0:1; 222:0:0 → 414:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 225` (Journal) | `quests/minor_quest/mq041_corpo/corpo/01b_lift_the_dumpster` | 225:0:0 → 219:0:1; 523:0:0 → 225:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 367` (Journal) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny` | 367:0:0 → 441:0:1; 663:0:0 → 367:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 370` (Journal) | `quests/minor_quest/mq041_corpo` | 370:0:0 → 527:0:1; 966:0:0 → 370:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 663` (Journal) | `quests/minor_quest/mq041_corpo/corpo/04_confront_frank` | 438:0:0 → 663:0:3; 533:0:0 → 663:0:3; 663:0:0 → 367:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 729` (Condition) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1` | 727:666:0 → 729:0:1; 729:0:0 → 523:0:1; 729:0:1 → 523:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `mq041_corpo_02_confrontation.scene / scene / 748` (Journal) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1` | 173:0:0 → 748:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 751` (Journal) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1` | 751:0:0 → 736:0:1; 751:0:0 → 845:0:1; 840:0:1 → 751:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 840` (Condition) | `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1` | 812:0:0 → 840:0:1; 840:0:1 → 751:0:2; input mappings: 0:0=CutDestination, 0:1=In |
| `mq041_corpo_02_confrontation.scene / scene / 1335` (Journal) | `quests/minor_quest/mq041_corpo/corpo/04_confront_frank` | 1337:0:1 → 1335:0:1; 1340:0:0 → 1335:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq041_corpo_02_confrontation.scene / scene / 1337` (Condition) | `quests/minor_quest/mq041_corpo/corpo/03_talk_with_stranger` | 1322:0:0 → 1337:0:1; 1337:0:0 → 1340:0:4; 1337:0:1 → 1335:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `mq041_corpo_02_confrontation.scene / scene / 1340` (Journal) | `quests/minor_quest/mq041_corpo/corpo/03_talk_with_stranger` | 1337:0:0 → 1340:0:4; 1340:0:0 → 1335:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq041_quest_bugfixes.questphase / h7 / 11` | `base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase` | 11:Out1 → 1:In; 10:Out → 11:CYB-637601 |
| `mq041_quest_bugfixes.questphase / h77 / 12` | `base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase` | 11:Out → 12:CYB-637601; 12:Out1 → 34:CYB-656187 |
| `mq041_quest_bugfixes.questphase / h77 / 34` | `base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase` | 34:Out1 → 1:In; 12:Out1 → 34:CYB-656187 |
| `mq041_corpo_00_main.questphase / h0 / 2` | `base\quest\minor_quests\mq041\phases\mq041_corpo_01_hook.questphase` | 0:Out → 2:In1; 2:Out1 → 3:In1 |
| `mq041_corpo_00_main.questphase / h0 / 3` | `base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase` | 2:Out1 → 3:In1; 3:Out1 → 4:In1 |
| `mq041_corpo_01_hook.questphase / h0 / 4` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene`; `#mq041_sm_corpo_01_deadmans_switch` | 0:Out → 4:Start 0; 4:End 0 → 9:Active; 4:rejected_out → 14:Active; 4:Holocall INT → 12:In; 4:Holocall RET → 11:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 5` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene`; `#mq041_sm_corpo_02_confrontation` | 33:CutSource → 5:CutDestination; 7:Out → 5:Start 0; 24:Out → 5:CYB-637601; 5:End 0 → 12:In; 5:End 0 → 15:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 58 | `mq041_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 58:In1 |
| `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` / h77 / 34 | `mq041_corpo_00_main.questphase` | 12: Phase: mq041_corpo_02_confrontation.questphase; 34:Out1 → 1:In; 12:Out1 → 34:CYB-656187 |
| `base\quest\minor_quests\mq041\mq041_corpo.questphase` / h0 / 20 | `mq041_corpo_00_main.questphase` | 22: LogicalHub; 26: PauseCondition; 30: PauseCondition: #pacifica_content_tr; 20:Out1 → 1:In; 22:Out1 → 20:In1; 26:Out → 20:In1; 30:Out → 20:In1 |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase` / h0 / 2 | `mq041_corpo_01_hook.questphase` | 0: Input; 0:Out → 2:In1; 2:Out1 → 3:In1 |
| `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` / h7 / 11 | `mq041_corpo_02_confrontation.questphase` | 10: PauseCondition: #mq041_tr_frank_defeated_01; #mq041_tr_frank_defeated_02; #mq041_tr_frank_defeated_03; #mq041_tr_frank_defeated_04; #mq041_tr_frank_defeated_05; 11:Out1 → 1:In; 10:Out → 11:CYB-637601 |
| `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` / h77 / 12 | `mq041_corpo_02_confrontation.questphase` | 11: PauseCondition: #mq041_tr_frank_defeated_01; #mq041_tr_frank_defeated_02; #mq041_tr_frank_defeated_03; #mq041_tr_frank_defeated_04; #mq041_tr_frank_defeated_05; 11:Out → 12:CYB-637601; 12:Out1 → 34:CYB-656187 |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase` / h0 / 3 | `mq041_corpo_02_confrontation.questphase` | 2: Phase: mq041_corpo_01_hook.questphase; 2:Out1 → 3:In1; 3:Out1 → 4:In1 |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_01_hook.questphase` / h0 / 4 | `mq041_corpo_01_deadmans_switch.scene` | 0: Input; 0:Out → 4:Start 0; 4:End 0 → 9:Active; 4:rejected_out → 14:Active; 4:Holocall INT → 12:In; 4:Holocall RET → 11:In |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase` / h0 / 5 | `mq041_corpo_02_confrontation.scene` | 33: CutControl; 7: Journal; 24: Input; 33:CutSource → 5:CutDestination; 7:Out → 5:Start 0; 24:Out → 5:CYB-637601; 5:End 0 → 12:In; 5:End 0 → 15:In |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 106 | `mq041_corpo.questphase` | 70: LogicalHub; 70:Out1 → 106:In1 |
| `base\quest\minor_quests\mq041\mq041_corpo.quest` / h0 / 2 | `mq041_corpo.questphase` | 5: Scene: mq041_corpo_chicken_test.scene; 2:Out1 → 4:In; 5:End 0 → 2:In1 |
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
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq041_corpo_01_deadmans_switch.scene` | Start 0 → End 0, rejected_out | Frank; Player; 17 nodes / 16 edges |
| `mq041_corpo_02_confrontation.scene` | Start 0, CYB-637601, Start 2, Start1 → End 0 | Frank; johnny; Player; 167 nodes / 238 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq041_corpo_02_confrontation.scene / n7 / 0` | [Open] (`open`) | No option-level predicate stored | 0:0 → 623:0:1; 0:0 → 717:0:1; 0:0 → 812:0:0; 0:0 → 1158:0:1 |
| `mq041_corpo_02_confrontation.scene / n41 / 0` | I'm nobody to Abernathy. (`wrong`) | No option-level predicate stored | 0:0 → 42:0:0 |
| `mq041_corpo_02_confrontation.scene / n41 / 1` | You're pathetic. (`pathetic`) | No option-level predicate stored | 0:1 → 46:0:0 |
| `mq041_corpo_02_confrontation.scene / n41 / 2` | Here's another idea - I kill you right here and now. (`kill`) | No option-level predicate stored | 0:2 → 182:0:0 |
| `mq041_corpo_02_confrontation.scene / n55 / 0` | Not my problem. (`no_chance`) | No option-level predicate stored | 0:0 → 57:0:0; 0:0 → 1179:0:0; 0:0 → 1283:0:1 |
| `mq041_corpo_02_confrontation.scene / n55 / 1` | Gotta start over. (`possible`) | No option-level predicate stored | 0:1 → 204:0:0; 0:1 → 1179:0:0; 0:1 → 1315:0:1 |
| `mq041_corpo_02_confrontation.scene / n168 / 0` | Got a few scores to settle. (`benefits`) | No option-level predicate stored | 0:0 → 178:0:0 |
| `mq041_corpo_02_confrontation.scene / n168 / 1` | Butt out. (`myproblem`) | No option-level predicate stored | 0:1 → 171:0:0 |
| `mq041_corpo_02_confrontation.scene / n185 / 0` | Go ahead, try. (`try`) | No option-level predicate stored | 0:0 → 188:0:0 |
| `mq041_corpo_02_confrontation.scene / n185 / 1` | Want you to open your eyes. (`eyes`) | No option-level predicate stored | 0:1 → 191:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-637601` | mq041_quest_bugfixes.questphase / h7 / 2 | mq041_quest_bugfixes.questphase / h7 / 8; mq041_quest_bugfixes.questphase / h77 / 19 |
| `CYB-656187` | mq041_quest_bugfixes.questphase / h77 / 4 | mq041_quest_bugfixes.questphase / h77 / 5 |
| `air_traffic_off` | mq041_corpo_00_main.questphase / h39 / 14; mq041_corpo_02_confrontation.questphase / h0 / 19; mq041_corpo_02_confrontation.questphase / h0 / 20 | No reader in selected context |
| `holo_frank_calls_v_end_activate` | mq041_corpo_01_deadmans_switch.scene / scene / 79; mq041_corpo_01_hook.questphase / h0 / 12 | No reader in selected context |
| `holo_frank_calls_v_start_activate` | mq041_corpo_01_deadmans_switch.scene / scene / 78; mq041_corpo_01_hook.questphase / h0 / 11 | No reader in selected context |
| `holo_frank_nostra_calls_v_end_done` | mq041_corpo_01_deadmans_switch.scene / scene / 75 | mq041_corpo_01_deadmans_switch.scene / scene / 74 |
| `holo_frank_nostra_calls_v_rejectable` | mq041_corpo_01_deadmans_switch.scene / scene / 260 | No reader in selected context |
| `holo_frank_nostra_calls_v_rejected` | mq041_corpo_01_deadmans_switch.scene / scene / 262 | mq041_corpo_01_deadmans_switch.scene / scene / 264 |
| `holo_frank_nostra_calls_v_start_done` | mq041_corpo_01_deadmans_switch.scene / scene / 73 | mq041_corpo_01_deadmans_switch.scene / scene / 72 |
| `mq041_corpo_started` | mq041_corpo_01_hook.questphase / h0 / 7 | No reader in selected context |
| `mq041_done` | mq041_corpo_02_confrontation.questphase / h0 / 12 | No reader in selected context |
| `mq041_var_frank_sofa` | mq041_corpo_02_confrontation.scene / scene / 438 | mq041_corpo_02_confrontation.scene / scene / 441 |
| `q000_corpo_02_choice_02_done` | Producer outside selected context | mq041_corpo_02_confrontation.scene / scene / 195; mq041_corpo_02_confrontation.scene / scene / 44 |
| `travelling_merchant_lives` | Producer outside selected context | mq041_quest_bugfixes.questphase / h0 / 12 |
| `wanted_level` | Producer outside selected context | mq041_corpo_02_confrontation.questphase / h0 / 44 |

## Exact gates, joins and cancellation

<details><summary>58 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq041_quest_bugfixes.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 13:Out → 12:In |
| `mq041_quest_bugfixes.questphase / h7 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-637601"}}}` | 0:Out → 8:In; 8:False → 2:In |
| `mq041_quest_bugfixes.questphase / h7 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 9:In; 9:True → 10:In |
| `mq041_quest_bugfixes.questphase / h7 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_01","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_02","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_03","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_04","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_05","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false}]}}` | 9:True → 10:In; 10:Out → 11:CYB-637601 |
| `mq041_quest_bugfixes.questphase / h77 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-656187"}}}` | 0:Out → 5:In; 5:False → 4:In |
| `mq041_quest_bugfixes.questphase / h77 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 10:False → 1:In; 19:False → 10:In; 10:True → 11:In |
| `mq041_quest_bugfixes.questphase / h77 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_01","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_02","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_03","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_04","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_05","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false}]}}` | 10:True → 11:In; 11:Out → 12:CYB-637601 |
| `mq041_quest_bugfixes.questphase / h77 / 19` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-637601"}}}` | 4:Out → 19:In; 19:False → 10:In |
| `mq041_corpo_00_main.questphase / h39 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q000_corpo_friend"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":65.0},"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 3:In; 3:Out → 4:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq041_tr_av_zone"}}` | 26:Out → 19:In; 48:CutSource → 26:CutDestination; 27:Out → 26:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_av_zone"}}` | 28:Out → 20:In; 29:Out → 28:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 30` | `questLogicalXorNodeDefinition` `{}` | 27:Out → 30:In1; 29:Out → 30:In2; 30:Out1 → 32:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 31` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_01","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_02","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_03","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_04","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_frank_defeated_05","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false}]}}` | 32:True → 31:In; 31:True → 33:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 32` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 30:Out1 → 32:In; 32:True → 31:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 33` | `questCutControlNodeDefinition` `{}` | 33:CutSource → 5:CutDestination; 31:True → 33:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#mq041_briefcase_located"},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wanted_level","comparisonType":"Equal"}}]}}` | 44:Out → 7:Succeeded; 45:Out → 44:In |
| `mq041_corpo_02_confrontation.questphase / h0 / 48` | `questCutControlNodeDefinition` `{"permanent":true}` | 48:Out → 11:In; 13:Out → 48:In; 48:CutSource → 26:CutDestination |
| `mq041_corpo_02_confrontation.questphase / h197 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq041_tr_av_zone"}}` | 0:Out → 2:In; 5:CutSource → 2:CutDestination; 7:Out → 2:In; 2:Out → 3:In |
| `mq041_corpo_02_confrontation.questphase / h197 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 3:Out → 4:In; 4:Out → 5:In |
| `mq041_corpo_02_confrontation.questphase / h197 / 5` | `questCutControlNodeDefinition` `{"permanent":true}` | 5:Out → 1:In; 5:CutSource → 2:CutDestination; 5:CutSource → 3:CutDestination; 4:Out → 5:In; 5:CutSource → 7:CutDestination |
| `mq041_corpo_02_confrontation.questphase / h197 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 7:Out → 2:In; 3:Out → 7:In; 5:CutSource → 7:CutDestination |
| `mq041_corpo_01_deadmans_switch.scene / scene / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","inverted":true}}}` | 1:0:0 → 42:0:1; 42:0:0 → 22:0:1 |
| `mq041_corpo_01_deadmans_switch.scene / scene / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_frank_nostra_calls_v_start_done"}}}` | 72:0:0 → 73:0:1; 78:0:0 → 72:0:1 |
| `mq041_corpo_01_deadmans_switch.scene / scene / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_frank_nostra_calls_v_end_done"}}}` | 74:0:0 → 75:0:1; 79:0:0 → 74:0:1 |
| `mq041_corpo_01_deadmans_switch.scene / scene / 264` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_frank_nostra_calls_v_rejected"}}}` | 78:0:0 → 264:0:1; 264:0:0 → 262:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 44` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q000_corpo_02_choice_02_done","value":1,"comparisonType":"Less"}}}` | 44:0:0 → 49:0:0; 44:0:1 → 51:0:0; 46:0:0 → 44:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 195` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q000_corpo_02_choice_02_done","value":1,"comparisonType":"Less"}}}` | 42:0:0 → 195:0:1; 195:0:0 → 197:0:0; 195:0:1 → 201:0:0 |
| `mq041_corpo_02_confrontation.scene / scene / 441` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq041_var_frank_sofa","value":1,"comparisonType":"GreaterOrEqual"}}}` | 367:0:0 → 441:0:1; 441:0:0 → 930:0:0; 441:0:1 → 493:0:0 |
| `mq041_corpo_02_confrontation.scene / scene / 456` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"XOR","conditions":[{"$type":"questTriggerCondition","type":"Exited","triggerAreaRef":"#mq041_tr_conversation_zone"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterAttack_ConditionType","attackerRef":{"$type":"gameEntityReference","reference":"#player"},"targetRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType"}}]}}` | 419:1:0 → 456:0:0; 456:0:0 → 1322:0:0; 1166:0:0 → 456:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 523` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 523:0:0 → 225:0:3; 729:0:0 → 523:0:1; 729:0:1 → 523:0:1; 845:0:0 → 523:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 705` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 705:0:0 → 209:0:0; 1249:0:0 → 705:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 710` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#mq041_dumpster","eventType":"Executed"}}}` | 710:0:0 → 727:666:0; 722:0:0 → 710:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 729` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 727:666:0 → 729:0:1; 729:0:0 → 523:0:1; 729:0:1 → 523:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 736` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq041_corpo_02_confrontation_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":80.0,"inverted":true}}}` | 736:0:0 → 738:0:1; 751:0:0 → 736:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 777` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 272:666:0 → 777:0:1; 777:0:0 → 780:0:0 |
| `mq041_corpo_02_confrontation.scene / scene / 787` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":60.0},"comparisonType":"GreaterOrEqual"}}}` | 272:666:0 → 787:0:1; 780:1:0 → 787:0:0; 785:0:0 → 787:0:1; 787:0:0 → 783:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 789` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":20.0},"comparisonType":"Less"}}}` | 780:1:0 → 789:0:0; 783:0:0 → 789:0:1; 789:0:0 → 785:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 803` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq041_tr_av_zone","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]}}}` | 803:0:0 → 1041:0:0; 1385:0:1 → 803:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 840` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 812:0:0 → 840:0:1; 840:0:1 → 751:0:2 |
| `mq041_corpo_02_confrontation.scene / scene / 845` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition"}}` | 751:0:0 → 845:0:1; 845:0:0 → 523:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 855` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 419:1:0 → 855:0:0; 855:0:0 → 1322:0:1; 1166:0:0 → 855:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 860` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 240:0:0 → 860:0:1; 860:0:0 → 1147:0:0; 860:0:1 → 887:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 876` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 419:1:0 → 876:0:0; 876:0:0 → 904:0:1; 876:0:0 → 1322:0:2; 1166:0:0 → 876:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 887` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"statusEffectID":"BaseStatusEffect.Grappled","inverted":true}}}` | 860:0:1 → 887:0:1; 887:0:0 → 244:0:0; 887:0:1 → 890:0:1; 887:0:1 → 1174:0:0 |
| `mq041_corpo_02_confrontation.scene / scene / 890` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"statusEffectID":"BaseStatusEffect.Grappled","inverted":true}}}` | 887:0:1 → 890:0:1; 890:0:0 → 899:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 899` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition"}}` | 890:0:0 → 899:0:1; 899:0:0 → 244:0:0 |
| `mq041_corpo_02_confrontation.scene / scene / 1158` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":250}}}` | 7:0:0 → 1158:0:1; 1158:0:0 → 4:0:1; 1158:0:0 → 12:0:3; 1197:0:0 → 1158:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1246` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 701:0:0 → 1246:0:1; 1246:0:0 → 1249:0:1; 1246:0:0 → 1291:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1310` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 655:0:0 → 1310:0:1; 1310:0:1 → 774:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1331` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterEquippedItem_ConditionType","puppetRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"itemID":"114306797067"}}}` | 1322:0:0 → 1331:0:1; 1331:0:1 → 1215:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1337` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq041_corpo/corpo/03_talk_with_stranger","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 1322:0:0 → 1337:0:1; 1337:0:0 → 1340:0:4; 1337:0:1 → 1335:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1355` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 20:0:0 → 1355:0:1; 1355:0:0 → 652:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1363` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq041_tr_frank_defeated_01","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false}}` | 1363:0:0 → 212:0:0; 1363:0:1 → 1373:0:1; 1396:0:0 → 1363:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1373` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq041_tr_frank_defeated_02","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false}}` | 1363:0:1 → 1373:0:1; 1373:0:0 → 1028:0:0; 1373:0:1 → 1377:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1377` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq041_tr_frank_defeated_03","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false}}` | 1373:0:1 → 1377:0:1; 1377:0:0 → 1041:0:0; 1377:0:1 → 1381:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1381` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq041_tr_frank_defeated_04","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false}}` | 1377:0:1 → 1381:0:1; 1381:0:0 → 1055:0:0; 1381:0:1 → 1385:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1385` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq041_tr_frank_defeated_05","activatorRef":{"$type":"gameEntityReference","reference":"#q000_corpo_friend","names":["frank"]},"isPlayerActivator":false}}` | 1381:0:1 → 1385:0:1; 1385:0:0 → 1069:0:0; 1385:0:1 → 803:0:1 |
| `mq041_corpo_02_confrontation.scene / scene / 1396` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType"}}}` | 642:1:0 → 1396:0:0; 642:1:0 → 1396:1026:0; 1364:0:0 → 1396:0:1; 1396:0:0 → 1363:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq041_corpo_02_confrontation.scene / scene / 1355 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq041_corpo_02_confrontation.scene / scene / 247 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `call_lifecycle` | mq041_corpo_00_main.questphase / h39 / 13; mq041_corpo_01_deadmans_switch.scene / scene / 22 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `checkpoint` | mq041_corpo_00_main.questphase / h39 / 9; mq041_corpo_01_hook.questphase / h0 / 6; mq041_corpo_02_confrontation.questphase / h0 / 11 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq041_corpo_02_confrontation.scene / scene / 168; mq041_corpo_02_confrontation.scene / scene / 185; mq041_corpo_02_confrontation.scene / scene / 41; mq041_corpo_02_confrontation.scene / scene / 55; +1 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq041_corpo_02_confrontation.scene / scene / 774 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `conditional_route` | mq041_corpo_01_deadmans_switch.scene / scene / 264; mq041_corpo_01_deadmans_switch.scene / scene / 72; mq041_corpo_01_deadmans_switch.scene / scene / 74; mq041_corpo_02_confrontation.questphase / h0 / 44; +7 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq041_corpo_02_confrontation.questphase / h0 / 13; mq041_corpo_02_confrontation.scene / scene / 258; mq041_corpo_02_confrontation.scene / scene / 528; mq041_corpo_02_confrontation.scene / scene / 783; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `journal_transition` | mq041_corpo_01_hook.questphase / h0 / 13; mq041_corpo_01_hook.questphase / h0 / 14; mq041_corpo_01_hook.questphase / h0 / 16; mq041_corpo_01_hook.questphase / h0 / 5; +17 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | mq041_corpo_00_main.questphase / h39 / 14; mq041_corpo_01_deadmans_switch.scene / scene / 260; mq041_corpo_01_deadmans_switch.scene / scene / 262; mq041_corpo_01_deadmans_switch.scene / scene / 73; +12 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq041_corpo_02_confrontation.questphase / h0 / 30 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq041_corpo_02_confrontation.questphase / h197 / 7; mq041_corpo_02_confrontation.scene / scene / 1158; mq041_corpo_02_confrontation.scene / scene / 1246; mq041_corpo_02_confrontation.scene / scene / 523; +1 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq041_corpo_02_confrontation.questphase / h0 / 33; mq041_corpo_02_confrontation.questphase / h0 / 48; mq041_corpo_02_confrontation.questphase / h197 / 5 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq041_corpo_02_confrontation.scene / scene / 527 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq041_corpo_01_hook.questphase / h0 / 4; mq041_corpo_02_confrontation.questphase / h0 / 5 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq041_corpo_02_confrontation.questphase / h0 / 26; mq041_corpo_02_confrontation.questphase / h0 / 28; mq041_corpo_02_confrontation.questphase / h0 / 31; mq041_corpo_02_confrontation.questphase / h0 / 44; +12 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | mq041_corpo_02_confrontation.questphase / h197 / 4; mq041_corpo_02_confrontation.scene / scene / 777; mq041_corpo_02_confrontation.scene / scene / 855; mq041_corpo_02_confrontation.scene / scene / 860 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | mq041_corpo_02_confrontation.scene / scene / 1012; mq041_corpo_02_confrontation.scene / scene / 1014; mq041_corpo_02_confrontation.scene / scene / 1034; mq041_corpo_02_confrontation.scene / scene / 1036; +19 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` | repair; journal anchor | `base-mq041` |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase` | content candidate; forward dependency | `base-mq041` |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_01_hook.questphase` | content candidate; journal anchor | `base-mq041` |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase` | content candidate; journal anchor | `base-mq041` |
| `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` | content candidate; forward dependency | `base-mq041` |
| `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` | content candidate; journal anchor | `base-mq041` |

Evidence shards for this dossier (including parent context): [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

189 repeated typed/socket path signatures in this selected graph context; 32 distinct direct resource identities; 7 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` / scene / 78 -> 264 -> 262 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` / scene / 77 -> 79 -> 74 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` / scene / 264 -> 262 -> 270 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` / scene / 73 -> 76 -> 8 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` / scene / 8 -> 77 -> 79 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `9e5e28ecb38ea2a53a15` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` / scene / 260 -> 78 -> 72 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` / h7 / 0 -> 8 -> 2 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `fe9d2c1bdd2cebf30eb2` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` / scene / 76 -> 8 -> 77 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `cbae0fd3078e68426197` | `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` / h0 / 10 -> 13 -> 12 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `5c76d3bf7160f29b884f` | `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` / h77 / 5 -> 4 -> 19 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; False -> In; Out -> In |
| `7e7dbbc930b3717fd790` | `base\quest\minor_quests\mq041\phases\mq041_corpo_01_hook.questphase` / h0 / 14 -> 16 -> 5 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `c1b6601d2f647c8a694d` | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 147 -> 168 -> 178 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` / h0 / 14 | `h77` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase` / h0 / 3 | `h24` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase` / h0 / 4 | `h39` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase` / h0 / 4 | `h16` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase` / h0 / 42 | `h197` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
| `base\quest\minor_quests\mq041\mq041_corpo.gamedef` | content candidate | base\quest\minor_quests\mq041\mq041_corpo.quest |
| `base\quest\main_quests\part1\q101\q101.gamedef` | content candidate | base\quest\main_quests\part1\q101\q101.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_kabuki.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_kabuki.quest |
| `base\quest\demos\handson_2020\handson_2020_little_china.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_little_china.quest |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_speed_test.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_speed_test.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `base\quest\side_quests\sq021\sq021.gamedef` | content candidate | base\quest\side_quests\sq021\sq021.quest |
| `base\quest\side_quests\sq023\sq023.gamedef` | content candidate | base\quest\side_quests\sq023\sq023.quest |
| `base\quest\side_quests\sq025\sq025.gamedef` | content candidate | base\quest\side_quests\sq025\sq025.quest |
| `base\quest\side_quests\sq027\sq027_queen_of_the_highway.gamedef` | content candidate | base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
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
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_bar__2h_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_wall_lean180__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__rh_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_wall_lean270__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_wall_lean90__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q112\q112_11_shotgun\body\q112_11_shotgun__ma_johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_03_third_episode\sq032_03_third_episode__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_01_hook.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq041\scenes\lipsync\en\mq041_corpo_01_deadmans_switch\civ_mid_m_22_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq041\scenes\lipsync\en\mq041_corpo_01_deadmans_switch\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq041\scenes\lipsync\en\mq041_corpo_02_confrontation\civ_mid_m_22_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq041\scenes\lipsync\en\mq041_corpo_02_confrontation\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq041\scenes\lipsync\en\mq041_corpo_02_confrontation\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\ground\big__stand_ground__pee__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\corpo__stand_ground_gun__idle__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_wall_lean_right__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\side_quests\sq006\sq006_02b_investigation\sq006__johnny__stand_wall_lean_left__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\side_quests\sq006\sq006_06a_clandestine\sq006__johnny__sit_barstool_bar__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `air_traffic_off` | base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene / scene / 1440; base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene / scene / 1442; base\quest\minor_quests\mq014\mq014.questphase / h215 / 83; base\quest\minor_quests\mq014\mq014.questphase / h643 / 50; 170 total source locations in compressed evidence |
| `holo_frank_calls_v_end_activate` | base\quest\holocalls\frank\frank_holocall.questphase / h0 / 11; 1 total source locations in compressed evidence |
| `holo_frank_calls_v_start_activate` | base\quest\holocalls\frank\frank_holocall.questphase / h0 / 10; 1 total source locations in compressed evidence |
| `holo_frank_nostra_calls_v_end_done` | base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 115; base\quest\holocalls\frank\frank_holocall.scene / scene / 42; base\quest\holocalls\frank\frank_holocall.scene / scene / 551; 3 total source locations in compressed evidence |
| `holo_frank_nostra_calls_v_rejectable` | base\quest\holocalls\frank\frank_holocall.scene / scene / 618; 1 total source locations in compressed evidence |
| `holo_frank_nostra_calls_v_rejected` | base\quest\holocalls\frank\frank_holocall.scene / scene / 626; 1 total source locations in compressed evidence |
| `holo_frank_nostra_calls_v_start_done` | base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 114; base\quest\holocalls\frank\frank_holocall.scene / scene / 41; base\quest\holocalls\frank\frank_holocall.scene / scene / 576; 3 total source locations in compressed evidence |
| `q000_corpo_02_choice_02_done` | base\quest\minor_quests\mq055\mq055.quest / h37 / 43; base\quest\main_quests\prologue\q000\scenes\q000_corpo_02_to_elevators.scene / scene / 1101; ep1\quest\ep1.questphase / h2539 / 50; ep1\quest\ep1.questphase / h3117 / 57; 4 total source locations in compressed evidence |
| `wanted_level` | ep1\openworld\sandbox_activities\courier_spot\ep1_courier_debug.quest / h44 / 7; 1 total source locations in compressed evidence |

NodeRef uses: 117; TweakDB binding uses: 21. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` | 1 / 9 | scnDialogLineEvent: 9 |
| `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` | 29 / 301 | scnChangeIdleAnimEvent: 34; scnDialogLineEvent: 69; scnGameplayTransitionEvent: 8; scnIKEvent: 16; scnLookAtEvent: 50; scnPlaySkAnimEvent: 71; scnUnmountEvent: 8; scneventsSetAnimFeatureEvent: 8; scneventsSocket: 37 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
