# Only Pain

Journal: `quests/minor_quest/mq005_alley` · `MinorQuest` · hash `1268818328`.

**Coverage: journal-linked.** 18 exact journal-linked nodes in 4 resources; 4 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| "To serve and protect…" Funny, would've thought "To extort and torture" might fit better. Not sure what this guy's beef is with badges, but if you don't step in, they'll be scrapin' him off the sidewalk. Once they smear him there first, of course. But I dunno... maybe it's for the best? After all, no one's in Night City's dyin' an innocent soul. (Primary) | `quests/minor_quest/mq005_alley/mq005_main/01_deal_with_cops` |
| Wake the corpo. (Primary) | `quests/minor_quest/mq005_alley/mq005_main/02_check_on_corpo` |
| Talk to the corpo. (Primary) | `quests/minor_quest/mq005_alley/mq005_main/03_talk_to_corpo` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq005_quest_bugfixes.questphase / h37 / 3` (Condition) | `quests/minor_quest/mq005_alley` | 2:Out → 3:In; 3:True → 4:In |
| `mq005_quest_bugfixes.questphase / h125 / 3` (Condition) | `quests/minor_quest/mq005_alley/mq005_main/01_deal_with_cops` | 2:Out → 3:In; 3:True → 4:In; 3:False → 7:In |
| `mq005_quest_bugfixes.questphase / h125 / 6` (Journal) | `quests/minor_quest/mq005_alley` | 5:True → 6:Failed; 6:Out → 15:In |
| `mq005_quest_bugfixes.questphase / h125 / 7` (Condition) | `quests/minor_quest/mq005_alley/mq005_main/02_check_on_corpo` | 3:False → 7:In; 7:True → 4:In; 7:False → 8:In |
| `mq005_quest_bugfixes.questphase / h125 / 8` (Condition) | `quests/minor_quest/mq005_alley/mq005_main/03_talk_to_corpo` | 8:True → 4:In; 7:False → 8:In; 8:False → 16:In1 |
| `mq005.questphase / h47 / 11` (Journal) | `quests/minor_quest/mq005_alley` | 9:Out → 11:Succeeded; 11:Out → 10:In |
| `mq005.questphase / h47 / 15` (Journal) | `quests/minor_quest/mq005_alley` | 15:Out → 12:In; 39:True → 15:Failed |
| `mq005.questphase / h47 / 39` (Condition) | `quests/minor_quest/mq005_alley` | 7:Out1 → 39:In; 39:False → 12:In; 39:True → 15:Failed |
| `mq005_combat.questphase / h0 / 9` (Journal) | `quests/minor_quest/mq005_alley/mq005_main/01_deal_with_cops` | 22:True → 9:Active; 9:Out → 18:Active |
| `mq005_combat.questphase / h0 / 10` (Journal) | `quests/minor_quest/mq005_alley/mq005_main/01_deal_with_cops` | 10:Out → 1:In; 21:True → 10:Succeeded |
| `mq005_combat.questphase / h0 / 18` (Journal) | `quests/minor_quest/mq005_alley/mq005_main/01_deal_with_cops/description` | 9:Out → 18:Active |
| `mq005_01_alley.scene / scene / 95` (Journal) | `quests/minor_quest/mq005_alley/mq005_main/02_check_on_corpo` | 377:0:0 → 95:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq005_01_alley.scene / scene / 97` (Journal) | `quests/minor_quest/mq005_alley/mq005_main/02_check_on_corpo` | 97:0:0 → 99:0:1; 515:0:0 → 97:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq005_01_alley.scene / scene / 99` (Journal) | `quests/minor_quest/mq005_alley/mq005_main/03_talk_to_corpo` | 97:0:0 → 99:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq005_01_alley.scene / scene / 240` (Journal) | `quests/minor_quest/mq005_alley` | 240:0:0 → 244:0:0; 418:0:0 → 240:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq005_01_alley.scene / scene / 418` (Condition) | `quests/minor_quest/mq005_alley` | 234:0:0 → 418:0:1; 418:0:0 → 240:0:3; 418:0:1 → 244:0:0; input mappings: 0:0=CutDestination, 0:1=In |
| `mq005_01_alley.scene / scene / 424` (Condition) | `quests/minor_quest/mq005_alley` | 407:0:0 → 424:0:1; 424:0:0 → 698:0:3; 424:0:1 → 200:0:0; input mappings: 0:0=CutDestination, 0:1=In |
| `mq005_01_alley.scene / scene / 698` (Journal) | `quests/minor_quest/mq005_alley` | 424:0:0 → 698:0:3; 698:0:0 → 200:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq005.questphase / h47 / 3` | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene`; `#mq005_01_sm_alley` | 21:CutSource → 3:CutDestination; 40:Scene → 3:Start_in; 3:Combat_out → 4:In1; 3:CorpoKilledInCrossfire → 19:In1; 3:StreetKidSuccess_out → 6:In1; 3:CombatFromInterruption → 4:In1; 3:Ignored_out → 7:In1 |
| `mq005.questphase / h47 / 4` | `base\quest\minor_quests\mq005\phases\mq005_combat.questphase` | 3:Combat_out → 4:In1; 3:CombatFromInterruption → 4:In1; 6:ReturnToCombat → 4:In1; 42:Out1 → 4:In1; 4:Out1 → 21:In; 4:Out1 → 27:In1; 4:EscapedOut → 7:In1; 4:DefeatedFromLeavingOut → 44:In1 |
| `mq005.questphase / h47 / 5` | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene`; `#mq005_01_sm_alley` | 27:Out1 → 5:Wrapup_in; 5:End_Out → 9:In; 5:CorpoKilledInCrossfire → 18:In1; 5:Ignored_out → 7:In1; 5:player_attack_corpo_out → 38:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 25 | `mq005_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 25:In1 |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 19 | `mq005.questphase` | 62: LogicalHub; 62:Out1 → 19:In1 |
| `base\quest\minor_quests\mq005\mq005.quest` / h0 / 0 | `mq005.questphase` | 1: Start; 1:Out → 0:In1; 0:Out1 → 2:In |
| `base\quest\minor_quests\mq005\mq005.questphase` / h47 / 4 | `mq005_combat.questphase` | 3: Scene: mq005_01_alley.scene; 3: Scene: mq005_01_alley.scene; 6: Phase; 42: LogicalHub; 3:Combat_out → 4:In1; 3:CombatFromInterruption → 4:In1; 6:ReturnToCombat → 4:In1; 42:Out1 → 4:In1; 4:Out1 → 21:In; 4:Out1 → 27:In1; 4:EscapedOut → 7:In1; 4:DefeatedFromLeavingOut → 44:In1 |
| `base\quest\minor_quests\mq005\mq005.questphase` / h47 / 3 | `mq005_01_alley.scene` | 21: CutControl; 40: Phase; 21:CutSource → 3:CutDestination; 40:Scene → 3:Start_in; 3:Combat_out → 4:In1; 3:CorpoKilledInCrossfire → 19:In1; 3:StreetKidSuccess_out → 6:In1; 3:CombatFromInterruption → 4:In1; 3:Ignored_out → 7:In1 |
| `base\quest\minor_quests\mq005\mq005.questphase` / h47 / 5 | `mq005_01_alley.scene` | 27: LogicalHub; 27:Out1 → 5:Wrapup_in; 5:End_Out → 9:In; 5:CorpoKilledInCrossfire → 18:In1; 5:Ignored_out → 7:In1; 5:player_attack_corpo_out → 38:In |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
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
| `mq005_01_alley.scene` | Start_in, Wrapup_in, old → Combat_out, End_Out, StreetKidSuccess_out, Ignored_out, player_attack_corpo_out, CombatFromInterruption, CorpoKilledInCrossfire | Police_Officer_01; Police_Officer_02; Police_Officer_03; Corpo; car_01; car_02; Player; 156 nodes / 198 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq005_01_alley.scene / n20 / 0` | What's going on? (`Ask`) | No option-level predicate stored | 0:0 → 26:0:0; 0:0 → 763:1:0 |
| `mq005_01_alley.scene / n20 / 1` | Is this how you protect and serve? (`StreetKid`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83574632792"}}}} | 0:1 → 30:0:0; 0:1 → 763:1:0 |
| `mq005_01_alley.scene / n20 / 2` | Stop it or else you'll kill him. (`Object`) | No option-level predicate stored | 0:2 → 28:0:0; 0:2 → 763:1:0 |
| `mq005_01_alley.scene / n32 / 0` | Leave him alone. (`Leave Him`) | No option-level predicate stored | 0:0 → 38:0:0; 0:0 → 702:0:1; 0:0 → 784:1:0 |
| `mq005_01_alley.scene / n32 / 1` | I'll deal with him. (`StreetKid`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83574632792"}}}} | 0:1 → 694:0:1; 0:1 → 784:1:0 |
| `mq005_01_alley.scene / n32 / 2` | I was just about to leave. (`Carry On`) | No option-level predicate stored | 0:2 → 36:0:0; 0:2 → 784:1:0 |
| `mq005_01_alley.scene / n54 / 0` | [Wake] (`Wake up`) | No option-level predicate stored | No matching 0:ordinal output; inspect raw stamps |
| `mq005_01_alley.scene / n63 / 0` | Heard you've been showing spiked braindances. (`FullStory`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq005_01_full_story", "value": 1, "comparisonType": "GreaterOrEqual"}}, "bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83574632792"}}}} | 0:0 → 65:0:0 |
| `mq005_01_alley.scene / n63 / 1` | The truth. What did they want from you? (`NoFullStory`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "124667716888", "buildId": "92409620733", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 67:0:0 |
| `mq005_01_alley.scene / n63 / 2` | Eddies. (`moneyz`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "124667716888", "buildId": "74910219395", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 140:0:0 |
| `mq005_01_alley.scene / n63 / 3` | Nothing. It's your lucky day. (`nothing`) | No option-level predicate stored | 0:3 → 128:0:0 |
| `mq005_01_alley.scene / n71 / 0` | Go on, get outta here. (`FreeToGo`) | No option-level predicate stored | 0:0 → 132:0:0 |
| `mq005_01_alley.scene / n71 / 1` | Hand over your eddies. (`Money`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "124667716888", "buildId": "74910219395", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 85:0:0 |
| `mq005_01_alley.scene / n71 / 2` | [Shoot] (`FuckYou`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq005_01_admition_of_guilt_BLOCK", "value": 1, "comparisonType": "GreaterOrEqual"}}} | No matching 0:ordinal output; inspect raw stamps |
| `mq005_01_alley.scene / n71 / 3` | [Punch] (`Punch him`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq005_block_punching_choice", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:3 → 87:0:0 |
| `mq005_01_alley.scene / n159 / 0` | That'll do. (`Enough`) | No option-level predicate stored | 0:0 → 162:0:0 |
| `mq005_01_alley.scene / n159 / 1` | Give me everything you've got. (`Intimidate`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "buildId": "75476658533", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 158:0:0 |
| `mq005_01_alley.scene / n515 / 0` | Time to wake up. (`Wake up`) | No option-level predicate stored | 0:0 → 51:0:0; 0:0 → 97:0:3 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-12345` | mq005_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-592021` | mq005_quest_bugfixes.questphase / h37 / 2 | No reader in selected context |
| `CYB-648297` | mq005_quest_bugfixes.questphase / h69 / 5 | No reader in selected context |
| `CYB-688402` | mq005_quest_bugfixes.questphase / h125 / 17 | No reader in selected context |
| `mq005_01_admition_of_guilt` | mq005_01_alley.scene / scene / 75 | mq005_01_alley.scene / scene / 146; mq005_01_alley.scene / scene / 90 |
| `mq005_01_admition_of_guilt_BLOCK` | Producer outside selected context | mq005_01_alley.scene / scene / 71 |
| `mq005_01_full_story` | mq005_01_alley.scene / scene / 59 | mq005_01_alley.scene / scene / 63 |
| `mq005_block_punching_choice` | Producer outside selected context | mq005_01_alley.scene / scene / 71 |
| `mq005_done` | mq005.questphase / h47 / 36 | mq005_quest_bugfixes.questphase / h125 / 5 |
| `mq005_police_done` | mq005_combat.questphase / h0 / 19 | No reader in selected context |
| `mq005_police_left` | mq005.questphase / h155 / 29 | mq005.questphase / h47 / 43; mq005_01_alley.scene / scene / 677; mq005_combat.questphase / h0 / 20; mq005_combat.questphase / h0 / 21; mq005_combat.questphase / h0 / 22; mq005_quest_bugfixes.questphase / h69 / 4 |
| `travelling_merchant_lives` | Producer outside selected context | mq005_quest_bugfixes.questphase / h0 / 18 |
| `wanted_level` | Producer outside selected context | mq005.questphase / h598 / 9; mq005_01_alley.scene / scene / 849 |

## Exact gates, joins and cancellation

<details><summary>75 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq005_quest_bugfixes.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 19:Out → 18:In |
| `mq005_quest_bugfixes.questphase / h37 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq005_alley","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 2:Out → 3:In; 3:True → 4:In |
| `mq005_quest_bugfixes.questphase / h69 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq005_police_left","value":1,"comparisonType":"GreaterOrEqual"}}}` | 4:True → 2:In; 5:Out → 4:In |
| `mq005_quest_bugfixes.questphase / h125 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 17:Out → 2:In; 2:Out → 3:In |
| `mq005_quest_bugfixes.questphase / h125 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq005_alley/mq005_main/01_deal_with_cops","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 3:In; 3:True → 4:In; 3:False → 7:In |
| `mq005_quest_bugfixes.questphase / h125 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false}}}}` | 3:True → 4:In; 7:True → 4:In; 8:True → 4:In; 4:True → 5:In; 4:False → 16:In1 |
| `mq005_quest_bugfixes.questphase / h125 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq005_done","comparisonType":"Equal"}}}` | 4:True → 5:In; 5:True → 6:Failed; 5:False → 16:In1 |
| `mq005_quest_bugfixes.questphase / h125 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq005_alley/mq005_main/02_check_on_corpo","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:False → 7:In; 7:True → 4:In; 7:False → 8:In |
| `mq005_quest_bugfixes.questphase / h125 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq005_alley/mq005_main/03_talk_to_corpo","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 8:True → 4:In; 7:False → 8:In; 8:False → 16:In1 |
| `mq005.questphase / h47 / 21` | `questCutControlNodeDefinition` `{}` | 21:CutSource → 3:CutDestination; 4:Out1 → 21:In; 6:Out1 → 21:In |
| `mq005.questphase / h47 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1}}}}` | 37:Out → 9:In; 38:Out → 37:In |
| `mq005.questphase / h47 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq005_alley","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 7:Out1 → 39:In; 39:False → 12:In; 39:True → 15:Failed |
| `mq005.questphase / h47 / 43` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq005_police_left","value":1,"comparisonType":"GreaterOrEqual"}}}` | 27:Out1 → 43:In; 43:False → 44:In1 |
| `mq005.questphase / h155 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_001"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0}}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_001"},"timeInterval":0.25,"onScreenTest":true,"inverted":true}}]}}` | 33:Out → 26:In; 35:Out → 33:In |
| `mq005.questphase / h155 / 34` | `questLogicalXorNodeDefinition` `{}` | 34:Out1 → 30:In; 38:Success → 34:In1; 39:Success → 34:In2 |
| `mq005.questphase / h155 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_002"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0}}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_002"},"timeInterval":0.25,"onScreenTest":true,"inverted":true}}]}}` | 36:Out → 27:In; 37:Out → 36:In |
| `mq005.questphase / h155 / 42` | `questLogicalAndNodeDefinition` `{}` | 30:Out → 42:In2; 45:Out → 42:In1; 42:Out1 → 43:In |
| `mq005.questphase / h155 / 46` | `questLogicalAndNodeDefinition` `{}` | 30:Out → 46:In1; 46:Out1 → 44:In; 47:Out → 46:In2 |
| `mq005.questphase / h155 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","attackerRef":{"$type":"gameEntityReference","reference":"#player"},"isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]}}}]}}` | 54:Out1 → 48:In; 48:Out → 55:In1 |
| `mq005.questphase / h155 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"type":"Gunshot"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]},"type":"Gunshot"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]},"type":"Gunshot"}}]}}` | 54:Out2 → 49:In; 49:Out → 55:In2 |
| `mq005.questphase / h155 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"type":"AimingAt"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]},"type":"AimingAt"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]},"type":"AimingAt"}}]}}` | 54:Out3 → 50:In; 50:Out → 55:In3 |
| `mq005.questphase / h155 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"type":"Hacked"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]},"type":"Hacked"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]},"type":"Hacked"}}]}}` | 54:Out4 → 51:In; 51:Out → 55:In4 |
| `mq005.questphase / h155 / 55` | `questLogicalXorNodeDefinition` `{"inputSocketCount":5}` | 48:Out → 55:In1; 49:Out → 55:In2; 50:Out → 55:In3; 51:Out → 55:In4; 58:Out → 55:In5; 55:Out1 → 56:In |
| `mq005.questphase / h155 / 56` | `questCutControlNodeDefinition` `{}` | 56:CutSource → 38:CutDestination; 56:CutSource → 39:CutDestination; 56:CutSource → 43:CutDestination; 56:CutSource → 44:CutDestination; 55:Out1 → 56:In; 56:Out → 57:In |
| `mq005.questphase / h155 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","attackerRef":{"$type":"gameEntityReference","reference":"#player"},"isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_001"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_002"}}}]}}` | 54:Out5 → 58:In; 58:Out → 55:In5 |
| `mq005.questphase / h155 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq005_tr_alley_area","activatorRef":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_002"},"isPlayerActivator":false}}` | 59:Out → 41:In; 60:Out → 59:In |
| `mq005.questphase / h598 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq005_tr_start_hook"}}` | 0:Out → 2:In; 2:Out → 9:In |
| `mq005.questphase / h598 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","attackerRef":{"$type":"gameEntityReference","reference":"#player"},"isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]}}}]}}` | 6:Out1 → 4:In; 4:Out → 7:In1 |
| `mq005.questphase / h598 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1}}}]}}` | 6:Out2 → 5:In; 5:Out → 7:In2 |
| `mq005.questphase / h598 / 7` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 7:Out1 → 3:In; 4:Out → 7:In1; 5:Out → 7:In2; 8:Out → 7:In3 |
| `mq005.questphase / h598 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq005_tr_player_approaches_corpo"}}` | 6:Out3 → 8:In; 8:Out → 7:In3 |
| `mq005.questphase / h598 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wanted_level","comparisonType":"Equal"}}}` | 9:True → 1:In; 2:Out → 9:In; 9:False → 3:In |
| `mq005.questphase / h696 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq005_com_corpo"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"GreaterOrEqual"}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo"},"timeInterval":0.20000000298023224,"onScreenTest":true,"inverted":true}}]}}` | 16:Out → 10:In; 10:Out → 13:In |
| `mq005.questphase / h696 / 14` | `questLogicalAndNodeDefinition` `{}` | 14:Out1 → 1:In; 3:Out → 14:In1; 13:Out → 14:In2 |
| `mq005.questphase / h696 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq005_tr_big"},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_001"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0}}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_002"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0}}}]}}` | 15:Out → 7:In; 16:Out → 15:In |
| `mq005_combat.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 8:Out → 2:In; 2:Out → 15:In1 |
| `mq005_combat.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 8:Out → 3:In; 3:Out → 15:In2 |
| `mq005_combat.questphase / h0 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 8:Out → 4:In; 4:Out → 15:In3 |
| `mq005_combat.questphase / h0 / 15` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 2:Out → 15:In1; 3:Out → 15:In2; 4:Out → 15:In3; 15:Out1 → 19:In |
| `mq005_combat.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq005_tr_big"}}` | 0:Out → 16:In; 16:Out → 20:In |
| `mq005_combat.questphase / h0 / 20` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq005_police_left","comparisonType":"Equal"}}}` | 16:Out → 20:In; 20:True → 17:In |
| `mq005_combat.questphase / h0 / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq005_police_left","comparisonType":"Equal"}}}` | 21:True → 10:Succeeded; 19:Out → 21:In; 21:False → 23:In |
| `mq005_combat.questphase / h0 / 22` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq005_police_left","comparisonType":"Equal"}}}` | 0:Out → 22:In; 22:True → 9:Active |
| `mq005_01_alley.scene / scene / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq005_tr_big"}}` | 47:0:0 → 49:0:0; 196:0:0 → 47:0:1 |
| `mq005_01_alley.scene / scene / 90` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq005_01_admition_of_guilt","value":1,"comparisonType":"GreaterOrEqual"}}}` | 90:0:0 → 93:0:0; 90:0:1 → 128:0:0; 132:0:0 → 90:0:1 |
| `mq005_01_alley.scene / scene / 146` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq005_01_admition_of_guilt","value":1,"comparisonType":"GreaterOrEqual"}}}` | 87:0:0 → 146:0:1; 146:0:0 → 148:0:0; 146:0:1 → 150:0:0 |
| `mq005_01_alley.scene / scene / 171` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo","names":["Corpo"]}}}}` | 171:0:0 → 407:0:0; 228:0:0 → 171:0:1 |
| `mq005_01_alley.scene / scene / 231` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo","names":["Corpo"]},"comparisonParams":{"$type":"questComparisonParam","count":1,"comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 231:0:0 → 234:0:1; 231:0:1 → 192:0:1; 231:0:1 → 515:0:0; 377:0:0 → 231:0:1 |
| `mq005_01_alley.scene / scene / 234` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq005_com_corpo","names":["Corpo"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo","names":["Corpo"]},"timeInterval":0.20000000298023224,"angleTolerance":60.0}}]}}` | 231:0:0 → 234:0:1; 234:0:0 → 418:0:1 |
| `mq005_01_alley.scene / scene / 246` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1}}}]}}` | 246:0:0 → 251:0:1; 247:0:1 → 246:0:1; 601:1:0 → 246:0:0 |
| `mq005_01_alley.scene / scene / 346` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq005_officer_reacts_to_v"}}` | 126:0:0 → 346:0:1; 346:0:0 → 340:0:0; 346:0:1 → 352:0:0 |
| `mq005_01_alley.scene / scene / 349` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq005_officer_reacts_to_v"}}` | 340:0:0 → 349:0:1; 349:0:0 → 352:0:0 |
| `mq005_01_alley.scene / scene / 410` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo","names":["Corpo"]},"statusEffectID":"BaseStatusEffect.Grappled"}}}` | 228:0:0 → 410:0:1; 410:0:0 → 414:0:1 |
| `mq005_01_alley.scene / scene / 414` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 410:0:0 → 414:0:1; 414:0:0 → 413:0:1 |
| `mq005_01_alley.scene / scene / 418` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq005_alley","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 234:0:0 → 418:0:1; 418:0:0 → 240:0:3; 418:0:1 → 244:0:0 |
| `mq005_01_alley.scene / scene / 424` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq005_alley","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 407:0:0 → 424:0:1; 424:0:0 → 698:0:3; 424:0:1 → 200:0:0 |
| `mq005_01_alley.scene / scene / 551` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 36:0:0 → 551:0:1; 551:0:0 → 553:0:1 |
| `mq005_01_alley.scene / scene / 581` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_002"},"childRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"enterAnimationFinished":true,"role":"Driver"}}}` | 561:0:0 → 581:0:1; 581:0:0 → 587:0:0 |
| `mq005_01_alley.scene / scene / 583` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_002"},"childRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"enterAnimationFinished":true,"role":"Driver"}}}` | 566:0:0 → 583:0:1; 583:0:0 → 587:0:1 |
| `mq005_01_alley.scene / scene / 585` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq005_spwn_police_car_002"},"childRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"enterAnimationFinished":true,"role":"Driver"}}}` | 579:0:0 → 585:0:1; 585:0:0 → 587:0:2 |
| `mq005_01_alley.scene / scene / 606` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq005_tr_player_approaches_corpo"}}` | 40:2:0 → 606:0:0; 247:0:2 → 606:0:1; 606:0:0 → 251:0:2 |
| `mq005_01_alley.scene / scene / 639` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 637:0:0 → 639:0:1; 639:0:0 → 641:0:1 |
| `mq005_01_alley.scene / scene / 645` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 637:0:0 → 645:0:1; 645:0:0 → 644:0:1 |
| `mq005_01_alley.scene / scene / 649` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 648:0:0 → 649:0:1; 649:0:0 → 650:0:1 |
| `mq005_01_alley.scene / scene / 652` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 648:0:0 → 652:0:1; 652:0:0 → 658:0:1 |
| `mq005_01_alley.scene / scene / 677` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq005_police_left","value":1,"comparisonType":"GreaterOrEqual"}}}` | 677:0:0 → 803:0:0; 677:0:1 → 808:0:0; 822:0:0 → 677:0:1 |
| `mq005_01_alley.scene / scene / 709` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 707:0:0 → 709:0:1; 709:0:0 → 711:0:1 |
| `mq005_01_alley.scene / scene / 728` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo","names":["Corpo"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 228:0:0 → 728:0:1; 728:0:0 → 407:0:1 |
| `mq005_01_alley.scene / scene / 739` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","attackerRef":{"$type":"gameEntityReference","reference":"#player"},"isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]}}}]}}` | 117:666:0 → 739:0:1; 601:1:0 → 739:0:0; 739:0:0 → 748:0:0 |
| `mq005_01_alley.scene / scene / 744` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"type":"Gunshot"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]},"type":"Gunshot"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]},"type":"Gunshot"}}]}}` | 117:666:0 → 744:0:1; 601:1:0 → 744:0:0; 744:0:0 → 748:0:1 |
| `mq005_01_alley.scene / scene / 753` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"type":"AimingAt"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]},"type":"AimingAt"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]},"type":"AimingAt"}}]}}` | 117:666:0 → 753:0:1; 601:1:0 → 753:0:0; 753:0:0 → 748:0:2 |
| `mq005_01_alley.scene / scene / 758` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer01"]},"type":"Hacked"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer02"]},"type":"Hacked"}},{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_alley","names":["PoliceOfficer03"]},"type":"Hacked"}}]}}` | 117:666:0 → 758:0:1; 601:1:0 → 758:0:0; 758:0:0 → 748:0:3 |
| `mq005_01_alley.scene / scene / 827` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo","names":["Corpo"]},"type":"VehicleHit"}}}` | 228:0:0 → 827:0:1; 827:0:0 → 413:0:1 |
| `mq005_01_alley.scene / scene / 839` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSensesCondition","type":{"$type":"questStimuli_ConditionType","targetRef":{"$type":"gameEntityReference","reference":"#mq005_com_corpo","names":["Corpo"]},"type":"DodgeVehicle"}}}` | 228:0:0 → 839:0:1; 839:0:0 → 413:0:1 |
| `mq005_01_alley.scene / scene / 849` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wanted_level"}},{"$type":"questTriggerCondition","triggerAreaRef":"#mq005_tr_alley_area"}]}}` | 247:0:3 → 849:0:1; 849:0:0 → 251:0:3 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq005_quest_bugfixes.questphase / h125 / 4 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq005_01_alley.scene / scene / 219; mq005_01_alley.scene / scene / 559; mq005_01_alley.scene / scene / 565; mq005_01_alley.scene / scene / 680; +1 locations in catalogue.json | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | mq005.questphase / h47 / 10 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq005_01_alley.scene / scene / 159; mq005_01_alley.scene / scene / 20; mq005_01_alley.scene / scene / 32; mq005_01_alley.scene / scene / 515; +3 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq005_combat.questphase / h0 / 11; mq005_combat.questphase / h0 / 13; mq005_combat.questphase / h0 / 14 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq005.questphase / h12 / 2; mq005.questphase / h155 / 24; mq005.questphase / h155 / 28; mq005.questphase / h696 / 13; +3 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq005.questphase / h47 / 43; mq005.questphase / h598 / 9; mq005_01_alley.scene / scene / 146; mq005_01_alley.scene / scene / 63; +10 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq005.questphase / h696 / 4; mq005.questphase / h696 / 6 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq005.questphase / h47 / 35; mq005_01_alley.scene / scene / 722 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `journal_transition` | mq005.questphase / h12 / 5; mq005.questphase / h47 / 11; mq005.questphase / h47 / 15; mq005_01_alley.scene / scene / 156; +9 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | mq005_01_alley.scene / scene / 581; mq005_01_alley.scene / scene / 583; mq005_01_alley.scene / scene / 585 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | mq005.questphase / h155 / 42; mq005.questphase / h155 / 46; mq005.questphase / h696 / 14; mq005_combat.questphase / h0 / 15 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq005.questphase / h155 / 29; mq005.questphase / h47 / 36; mq005_01_alley.scene / scene / 59; mq005_01_alley.scene / scene / 75; +5 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq005.questphase / h155 / 34; mq005.questphase / h155 / 55; mq005.questphase / h598 / 7 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq005_01_alley.scene / scene / 414; mq005_01_alley.scene / scene / 551; mq005_01_alley.scene / scene / 639; mq005_01_alley.scene / scene / 645; +4 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq005.questphase / h155 / 56; mq005.questphase / h47 / 21 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq005.questphase / h47 / 9; mq005_01_alley.scene / scene / 644; mq005_01_alley.scene / scene / 658 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq005.questphase / h47 / 3; mq005.questphase / h47 / 5 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq005.questphase / h155 / 59; mq005.questphase / h598 / 2; mq005.questphase / h598 / 8; mq005.questphase / h696 / 15; +6 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | mq005.questphase / h47 / 37; mq005.questphase / h598 / 5; mq005_01_alley.scene / scene / 231; mq005_01_alley.scene / scene / 246; +4 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mq005.questphase / h47 / 25; mq005.questphase / h47 / 26; mq005.questphase / h47 / 28; mq005.questphase / h47 / 29; +11 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq005_01_alley.scene / scene / 224; mq005_01_alley.scene / scene / 259; mq005_01_alley.scene / scene / 265; mq005_01_alley.scene / scene / 310; +19 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` | repair; journal anchor | `base-mq005` |
| `base\quest\minor_quests\mq005\mq005.questphase` | content candidate; journal anchor | `base-mq005` |
| `base\quest\minor_quests\mq005\phases\mq005_combat.questphase` | content candidate; journal anchor | `base-mq005` |
| `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` | content candidate; journal anchor | `base-mq005` |

Evidence shards for this dossier (including parent context): [base-mq005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq005.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

171 repeated typed/socket path signatures in this selected graph context; 37 distinct direct resource identities; 10 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `c8705a8da51824b73252` | `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` / h69 / 0 -> 5 -> 4 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `cbae0fd3078e68426197` | `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` / h0 / 17 -> 19 -> 18 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `016828d499c85128303c` | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 87 -> 146 -> 148 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `d18fd8da12f6125e7cd7` | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 13 -> 763 -> 768 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `820c61dc6db2829126d7` | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 352 -> 13 -> 398 | scnHubNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `febb6c8a9471736a82ed` | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 146 -> 148 -> 211 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `58c8902cfee139a52219` | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 677 -> 808 -> 812 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]; 0:1 -> 0:0; 4:0 -> 0:1 |
| `e6c034452fb22e1aa2ae` | `base\quest\minor_quests\mq005\mq005.questphase` / h155 / 55 -> 56 -> 38 | questLogicalXorNodeDefinition -> questCutControlNodeDefinition -> questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]; Out1 -> In; CutSource -> CutDestination |
| `b88f09756d5e86cc7c83` | `base\quest\minor_quests\mq005\mq005.questphase` / h696 / 13 -> 14 -> 1 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questLogicalAndNodeDefinition -> questOutputNodeDefinition; Out -> In2; Out1 -> In |
| `47d2d60daf4a94e81e2f` | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 93 -> 207 -> 210 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId] -> scnHubNode[scnNodeId]; 2:0 -> 0:0; 0:0 -> 0:0 |
| `7bfcd8df5888d6d0d606` | `base\quest\minor_quests\mq005\phases\mq005_combat.questphase` / h0 / 19 -> 21 -> 23 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; False -> In |
| `abbf46d00a7c0ae464b9` | `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` / h125 / 3 -> 7 -> 8 | questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; False -> In; False -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` / h0 / 14 | `h37` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` / h0 / 15 | `h69` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` / h0 / 20 | `h125` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq005\mq005.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq005\mq005.questphase` / h0 / 3 | `h47` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"},{"$type":"questOutputNodeDefinition","id":12,"socketName":"IgnoredOut"}] |
| `base\quest\minor_quests\mq005\mq005.questphase` / h47 / 4 | `h101` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq005\mq005.questphase` / h47 / 6 | `h155` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"},{"$type":"questOutputNodeDefinition","id":57,"socketName":"ReturnToCombat","type":"NonTerminating"}] |
| `base\quest\minor_quests\mq005\mq005.questphase` / h47 / 40 | `h598` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Scene"},{"$type":"questOutputNodeDefinition","id":3,"socketName":"Combat"}] |
| `base\quest\minor_quests\mq005\mq005.questphase` / h0 / 4 | `h696` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq005\mq005.gamedef` | content candidate | base\quest\minor_quests\mq005\mq005.quest |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
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
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_idle.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__sit_chair_lean180__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_wall_lean180__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_wall_lean180__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_ground_lean180__rh_on_belly__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_on_chin__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_big_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\minor_quests\mq005\mq005_01_alley\body\mq005_01_alley__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\synced\encounter_workspots\synced_ma_encounter_workspot.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\synced\lore\ma_lore.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\minor_quests\mq005\phases\mq005_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq005\scenes\lipsync\en\mq005_01_alley\civ_high_m_02_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq005\scenes\lipsync\en\mq005_01_alley\ncpd_low_m_02_enus_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq005\scenes\lipsync\en\mq005_01_alley\ncpd_low_m_04_afam_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq005\scenes\lipsync\en\mq005_01_alley\ncpd_mid_f_02_mex_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq005\scenes\lipsync\en\mq005_01_alley\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\ground\big__stand__spit__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\big__stand_microwave__use__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__sit_ground_wall_lean_back__wounded__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__06.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__think__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__wait__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_arms_crossed__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\dirt__stand_wall_lean_back_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\minor_quests\mq005\mq005__male__lie_ground__unconscious__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `wanted_level` | ep1\openworld\sandbox_activities\courier_spot\ep1_courier_debug.quest / h44 / 7; 1 total source locations in compressed evidence |

NodeRef uses: 214; TweakDB binding uses: 30. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` | 28 / 270 | scnChangeIdleAnimEvent: 14; scnDialogLineEvent: 72; scnGameplayTransitionEvent: 5; scnIKEvent: 10; scnLookAtEvent: 57; scnPlaySkAnimEvent: 59; scnPoseCorrectionEvent: 7; scnUnmountEvent: 5; scneventsSetAnimFeatureEvent: 5; scneventsSocket: 35; scneventsUnequipItemFromPerformerByItem: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
