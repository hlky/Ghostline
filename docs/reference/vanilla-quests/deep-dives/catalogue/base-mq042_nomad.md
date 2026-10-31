# These Boots Are Made for Walkin'

Journal: `quests/minor_quest/mq042_nomad` · `MinorQuest` · hash `3369099861`.

**Coverage: journal-linked.** 42 exact journal-linked nodes in 4 resources; 6 resources in the inspected dependency context.

Resource roles in that context: 5 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Here you thought your old ride was totaled for good – yet here you are now. Like a phoenix from the ashes, it lives again. But how? Why now? You'd already closed that chapter of kickin' up sand with nomads out in the desert… But I mean, it'd be stupid if you didn't check it out... right? You never can underestimate the past. Because it sure as shit likes to take revenge. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone` |
| Go to the indicated location. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location` |
| Look under the hood. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood` |
| Check the engine. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/02b_inspect_the_engine` |
| Close the hood. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/02c_close_the_hood` |
| Scan your old car. (Optional) | `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car` |
| Talk to the stranger. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger` |
| Confront the stranger. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/03a_confront_stranger` |
| Get in your old car. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/04_get_inside_the_car` |
| Talk to Johnny. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/05_talk_with_johnny` |
| Return to the landfill. (Primary) | `quests/minor_quest/mq042_nomad/mq042_nomad/06_get_back` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq042_quest_bugfixes.questphase / h30 / 4` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone` | 3:Out → 4:In; 4:True → 7:In1 |
| `mq042_quest_bugfixes.questphase / h30 / 5` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location` | 3:Out → 5:In; 5:True → 7:In2 |
| `mq042_quest_bugfixes.questphase / h151 / 3` (Condition) | `quests/minor_quest/mq042_nomad` | 4:Out → 3:In; 3:True → 12:In |
| `mq042_quest_bugfixes.questphase / h197 / 3` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone` | 4:Out → 3:In; 3:True → 24:In1 |
| `mq042_quest_bugfixes.questphase / h197 / 25` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location` | 4:Out → 25:In; 25:True → 24:In2 |
| `mq042_quest_bugfixes.questphase / h197 / 27` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car` | 4:Out → 27:In; 27:True → 24:In3 |
| `mq042_quest_bugfixes.questphase / h197 / 28` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood` | 4:Out → 28:In; 28:True → 24:In4 |
| `mq042_quest_bugfixes.questphase / h323 / 19` (PauseCondition) | `quests/minor_quest/mq042_nomad/mq042_nomad/04_get_inside_the_car` | 2:Out → 19:In; 19:Out → 3:In |
| `mq042_quest_bugfixes.questphase / h323 / 39` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone` | 5:Out → 39:In; 39:False → 41:In1 |
| `mq042_quest_bugfixes.questphase / h323 / 42` (PauseCondition) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone` | 41:Out1 → 42:In; 42:Out → 84:In |
| `mq042_quest_bugfixes.questphase / h323 / 15` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location` | 15:True → 14:In2; 37:Out1 → 15:In |
| `mq042_quest_bugfixes.questphase / h323 / 16` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car` | 16:True → 14:In3; 37:Out1 → 16:In |
| `mq042_quest_bugfixes.questphase / h323 / 17` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood` | 17:True → 14:In4; 37:Out1 → 17:In |
| `mq042_quest_bugfixes.questphase / h323 / 40` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone` | 5:Out → 40:In; 40:False → 41:In2; 40:True → 14:In1; 40:False → 37:In1 |
| `mq042_quest_bugfixes.questphase / h323 / 61` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone`; `quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location`; `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car`; `quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood` | 61:True → 57:In; 59:Out → 61:In |
| `mq042_nomad_01_hook.questphase / h0 / 11` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location` | 25:Out → 11:Active; 11:Out → 43:In; 11:Out → 44:In |
| `mq042_nomad_01_hook.questphase / h0 / 24` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone` | 3:Out → 24:Active; 24:Out → 32:Active |
| `mq042_nomad_01_hook.questphase / h0 / 25` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone` | 25:Out → 11:Active; 26:Out → 25:Succeeded |
| `mq042_nomad_01_hook.questphase / h0 / 32` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone/description` | 32:Out → 22:Active; 24:Out → 32:Active; 32:Out → 35:In |
| `mq042_nomad_02_car.questphase / h0 / 3` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location` | 2:Out → 3:Succeeded; 3:Out → 23:In1; 3:Out → 8:Start 0 |
| `mq042_nomad_02_car.questphase / h0 / 27` (Journal) | `quests/minor_quest/mq042_nomad` | 24:Out → 27:Succeeded; 27:Out → 28:In |
| `mq042_nomad_02_car.questphase / h0 / 35` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger` | 34:Out → 35:In; 35:True → 37:Inactive |
| `mq042_nomad_02_car.questphase / h0 / 36` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/06_get_back` | 37:Out → 36:Active; 36:Out → 38:In |
| `mq042_nomad_02_car.questphase / h0 / 37` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger` | 35:True → 37:Inactive; 37:Out → 36:Active |
| `mq042_nomad_02_car.questphase / h0 / 39` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/06_get_back` | 38:Out → 39:Inactive; 39:Out → 40:Active |
| `mq042_nomad_02_car.questphase / h0 / 40` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger` | 39:Out → 40:Active; 40:Out → 41:In1 |
| `mq042_nomad_02_car_found.scene / scene / 4` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car` | 4:0:0 → 232:0:1; 810:0:0 → 4:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 11` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car` | 9:0:0 → 11:0:3; 11:0:0 → 815:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 17` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger` | 17:0:0 → 336:0:0; 17:0:0 → 830:0:0; 294:0:0 → 17:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 96` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/04_get_inside_the_car` | 96:0:0 → 564:0:1; 131:0:0 → 96:0:1; 199:0:0 → 96:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 102` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/04_get_inside_the_car` | 102:0:0 → 176:0:1; 834:0:0 → 102:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 123` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger` | 117:0:0 → 123:0:3; 123:0:0 → 131:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 152` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger` | 134:2:0 → 152:0:3; 152:0:0 → 561:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 202` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger` | 202:0:0 → 199:0:1; 219:0:0 → 202:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 232` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood` | 4:0:0 → 232:0:1; 232:0:0 → 6:0:0; 232:0:0 → 9:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 238` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood` | 238:0:0 → 240:0:1; 797:0:0 → 238:0:3; 807:0:0 → 238:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 240` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/02b_inspect_the_engine` | 238:0:0 → 240:0:1; 240:0:0 → 236:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 294` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/02b_inspect_the_engine` | 294:0:0 → 17:0:1; 855:0:0 → 294:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 561` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/05_talk_with_johnny` | 152:0:0 → 561:0:1; 561:0:0 → 136:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 781` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/05_talk_with_johnny` | 176:0:0 → 781:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq042_nomad_02_car_found.scene / scene / 797` (Condition) | `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car` | 797:0:0 → 238:0:3; 797:0:1 → 807:0:2; 800:0:0 → 797:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `mq042_nomad_02_car_found.scene / scene / 807` (Journal) | `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car` | 797:0:1 → 807:0:2; 807:0:0 → 238:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq042_nomad_01_hook.questphase / h0 / 5` | `base\quest\minor_quests\mq042\scenes\mq042_nomad_01_gps_signal.scene`; `#mq042_sm_nomad_01_gps_signal` | 45:Out1 → 5:Start 0; 5:End 0 → 13:In |
| `mq042_nomad_02_car.questphase / h0 / 8` | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene`; `#mq042_sm_nomad_02_car_found` | 3:Out → 8:Start 0; 8:End 0 → 25:In; 8:journal_update → 34:In |
| `mq042_nomad_02_car.questphase / h0 / 16` | `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene`; `#mq023_01_sm_johnny` | 16:interrupt_out → 19:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase` / h0 / 4 | `mq023_01_johnny.scene` | 11: LogicalHub; 11:Out1 → 4:Start 0; 4:mq023_johnny_out → 26:In |
| `base\quest\minor_quests\mq042\phases\mq042_nomad_02_car.questphase` / h0 / 16 | `mq023_01_johnny.scene` | 16:interrupt_out → 19:In |
| `base\quest\minor_quests\mq042\mq042_nomad.questphase` / h0 / 2 | `mq042_nomad_01_hook.questphase` | 12: LogicalHub; 17: PauseCondition; 20: PauseCondition: #pacifica_content_tr; 12:Out1 → 2:In1; 17:Out → 2:In1; 20:Out → 2:In1; 2:Out1 → 3:In1 |
| `base\quest\minor_quests\mq042\mq042_nomad.questphase` / h0 / 3 | `mq042_nomad_02_car.questphase` | 2: Phase: mq042_nomad_01_hook.questphase; 2:Out1 → 3:In1; 3:Out1 → 4:In1 |
| `base\quest\minor_quests\mq042\phases\mq042_nomad_01_hook.questphase` / h0 / 5 | `mq042_nomad_01_gps_signal.scene` | 45: LogicalAnd; 45:Out1 → 5:Start 0; 5:End 0 → 13:In |
| `base\quest\minor_quests\mq042\phases\mq042_nomad_02_car.questphase` / h0 / 8 | `mq042_nomad_02_car_found.scene` | 3: Journal; 3:Out → 8:Start 0; 8:End 0 → 25:In; 8:journal_update → 34:In |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 2 | `mq023_bootleg_01_hook.questphase` | 0: Input; 0:Out → 2:In1; 2:Out1 → 3:In1 |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 24 | `mq042_nomad.questphase` | 90: LogicalHub; 90:Out1 → 24:In1 |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 27 | `mq023_bootleg.questphase` | 70: LogicalHub; 70:Out1 → 27:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq023_01_johnny.scene` | Start 0, interrupt_in → End 0, interrupt_out, mq023_johnny_out | johnny; performer; Player; 41 nodes / 43 edges |
| `mq042_nomad_01_gps_signal.scene` | Start 0 → End 0 | Player; 3 nodes / 2 edges |
| `mq042_nomad_02_car_found.scene` | Start 5, Start 0, Start 6, debug_input, Start 4 → End 0, journal_update | Lana; johnny; nomad_car; temp_car; Player; 142 nodes / 159 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq023_01_johnny.scene / n34 / 0` | Weak. Amateur hour. (`Option`) | No option-level predicate stored | 0:0 → 36:0:0 |
| `mq023_01_johnny.scene / n34 / 1` | Not bad. I guess. (`Option_01`) | No option-level predicate stored | 0:1 → 38:0:0 |
| `mq023_01_johnny.scene / n44 / 0` | Success gives you a platform. (`Option_02`) | No option-level predicate stored | 0:0 → 46:0:0 |
| `mq023_01_johnny.scene / n44 / 1` | Losers tend to say that. (`Option_03`) | No option-level predicate stored | 0:1 → 48:0:0 |
| `mq023_01_johnny.scene / n54 / 0` | Old tapes could be worth somethin'... (`Option_04`) | No option-level predicate stored | 0:0 → 56:0:0 |
| `mq023_01_johnny.scene / n54 / 1` | Lemme find those tapes, I'll be your fan. (`Option_05`) | No option-level predicate stored | 0:1 → 58:0:0 |
| `mq042_nomad_02_car_found.scene / n20 / 0` | It broke down. (``) | No option-level predicate stored | 0:0 → 24:0:0 |
| `mq042_nomad_02_car_found.scene / n20 / 1` | Not your business! (``) | No option-level predicate stored | 0:1 → 27:0:0 |
| `mq042_nomad_02_car_found.scene / n35 / 0` | Almost hate to admit it, but good work. (``) | No option-level predicate stored | 0:0 → 37:0:0 |
| `mq042_nomad_02_car_found.scene / n35 / 1` | You're a piss poor mechanic, then. (``) | No option-level predicate stored | 0:1 → 48:0:0 |
| `mq042_nomad_02_car_found.scene / n35 / 2` | Shoulda started with the step motor. (``) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "128795424191", "buildId": "85601791440", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 228:0:0 |
| `mq042_nomad_02_car_found.scene / n115 / 0` | Buy the car off you. (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "128795424191", "difficulty": "MEDIUM"}}}} | 0:0 → 117:0:0 |
| `mq042_nomad_02_car_found.scene / n115 / 1` | They're my wheels. That's that. (``) | No option-level predicate stored | 0:1 → 119:0:0 |
| `mq042_nomad_02_car_found.scene / n115 / 2` | You can keep the car. (``) | No option-level predicate stored | 0:2 → 656:0:1 |
| `mq042_nomad_02_car_found.scene / n115 / 3` | Why you so desperate to leave? (``) | No option-level predicate stored | 0:3 → 210:0:0 |
| `mq042_nomad_02_car_found.scene / n234 / 0` | [Lift hood] (``) | No option-level predicate stored | 0:0 → 800:0:0 |
| `mq042_nomad_02_car_found.scene / n245 / 0` | [Examine engine] (``) | No option-level predicate stored | 0:0 → 13:0:0; 0:0 → 633:0:1 |
| `mq042_nomad_02_car_found.scene / n258 / 0` | [Check radiator] (``) | No option-level predicate stored | 0:0 → 271:0:0 |
| `mq042_nomad_02_car_found.scene / n258 / 1` | [Check oil pan] (``) | No option-level predicate stored | 0:1 → 272:0:0 |
| `mq042_nomad_02_car_found.scene / n262 / 0` | [Drop hood] What? This car's mine! (``) | No option-level predicate stored | 0:0 → 858:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CYB-12345` | mq042_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-645655` | mq042_quest_bugfixes.questphase / h30 / 3 | mq042_quest_bugfixes.questphase / h30 / 2 |
| `CYB-649535` | mq042_quest_bugfixes.questphase / h197 / 4 | mq042_quest_bugfixes.questphase / h197 / 7 |
| `CYB-653599` | mq042_quest_bugfixes.questphase / h151 / 4 | mq042_quest_bugfixes.questphase / h151 / 7 |
| `CYB-665207` | mq042_quest_bugfixes.questphase / h323 / 5 | mq042_quest_bugfixes.questphase / h323 / 6 |
| `mq042_car_taken` | mq042_nomad_02_car_found.scene / scene / 219 | mq042_nomad_02_car_found.scene / scene / 222 |
| `mq042_done` | mq042_nomad_02_car.questphase / h0 / 11 | No reader in selected context |
| `mq042_started` | mq042_nomad_01_hook.questphase / h0 / 13 | No reader in selected context |
| `mq042_talk_started` | mq042_nomad_02_car_found.scene / scene / 633 | mq042_nomad_02_car.questphase / h71 / 8 |
| `mq042_var_interrupt_played` | mq042_nomad_02_car.questphase / h0 / 19 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | mq042_quest_bugfixes.questphase / h0 / 23 |

## Exact gates, joins and cancellation

<details><summary>61 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq042_quest_bugfixes.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 24:Out → 23:In |
| `mq042_quest_bugfixes.questphase / h30 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-645655"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq042_quest_bugfixes.questphase / h30 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:Out → 4:In; 4:True → 7:In1 |
| `mq042_quest_bugfixes.questphase / h30 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:Out → 5:In; 5:True → 7:In2 |
| `mq042_quest_bugfixes.questphase / h30 / 7` | `questLogicalXorNodeDefinition` `{}` | 4:True → 7:In1; 5:True → 7:In2; 7:Out1 → 8:In |
| `mq042_quest_bugfixes.questphase / h30 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 8:Out → 9:In; 9:Out → 14:In |
| `mq042_quest_bugfixes.questphase / h30 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleRef":{"$type":"gameEntityReference","reference":"#mq042_nomad_car"},"vehicleName":"Vehicle.v_standard2_thorton_galena_bobas_player","vehicleGlobalName":"#mq042_nomad_car"}}}` | 13:Out → 10:In; 14:Out → 13:In |
| `mq042_quest_bugfixes.questphase / h151 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 4:Out → 3:In; 3:True → 12:In |
| `mq042_quest_bugfixes.questphase / h151 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-653599"}}}` | 0:Out → 7:In; 7:False → 4:In |
| `mq042_quest_bugfixes.questphase / h197 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 4:Out → 3:In; 3:True → 24:In1 |
| `mq042_quest_bugfixes.questphase / h197 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-649535"}}}` | 0:Out → 7:In; 7:False → 4:In |
| `mq042_quest_bugfixes.questphase / h197 / 15` | `questConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleName":"Vehicle.v_standard2_thorton_galena_bobas_player"}}}` | 24:Out1 → 15:In; 15:False → 20:In |
| `mq042_quest_bugfixes.questphase / h197 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleRef":{"$type":"gameEntityReference","reference":"#mq042_nomad_car"},"vehicleName":"Vehicle.v_standard2_thorton_galena_bobas_player","vehicleGlobalName":"#mq042_nomad_car"}}}` | 19:Out → 16:In; 20:Out → 19:In |
| `mq042_quest_bugfixes.questphase / h197 / 24` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 3:True → 24:In1; 24:Out1 → 15:In; 25:True → 24:In2; 27:True → 24:In3; 28:True → 24:In4 |
| `mq042_quest_bugfixes.questphase / h197 / 25` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 4:Out → 25:In; 25:True → 24:In2 |
| `mq042_quest_bugfixes.questphase / h197 / 27` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 4:Out → 27:In; 27:True → 24:In3 |
| `mq042_quest_bugfixes.questphase / h197 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 4:Out → 28:In; 28:True → 24:In4 |
| `mq042_quest_bugfixes.questphase / h323 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-665207"}}}` | 6:False → 5:In; 66:Out → 6:In |
| `mq042_quest_bugfixes.questphase / h323 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/04_get_inside_the_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 2:Out → 19:In; 19:Out → 3:In |
| `mq042_quest_bugfixes.questphase / h323 / 20` | `questConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mq042_nomad_car"},"vehicleName":"Vehicle.v_standard2_thorton_galena_bobas_player","vehicleGlobalName":"#mq042_nomad_car"}}}` | 84:Out → 20:In; 20:True → 59:In; 20:False → 25:In |
| `mq042_quest_bugfixes.questphase / h323 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 5:Out → 39:In; 39:False → 41:In1 |
| `mq042_quest_bugfixes.questphase / h323 / 41` | `questLogicalAndNodeDefinition` `{}` | 39:False → 41:In1; 40:False → 41:In2; 41:Out1 → 42:In |
| `mq042_quest_bugfixes.questphase / h323 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 41:Out1 → 42:In; 42:Out → 84:In |
| `mq042_quest_bugfixes.questphase / h323 / 14` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 40:True → 14:In1; 15:True → 14:In2; 16:True → 14:In3; 17:True → 14:In4; 14:Out1 → 84:In |
| `mq042_quest_bugfixes.questphase / h323 / 15` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 15:True → 14:In2; 37:Out1 → 15:In |
| `mq042_quest_bugfixes.questphase / h323 / 16` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 16:True → 14:In3; 37:Out1 → 16:In |
| `mq042_quest_bugfixes.questphase / h323 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 17:True → 14:In4; 37:Out1 → 17:In |
| `mq042_quest_bugfixes.questphase / h323 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 5:Out → 40:In; 40:False → 41:In2; 40:True → 14:In1; 40:False → 37:In1 |
| `mq042_quest_bugfixes.questphase / h323 / 57` | `questConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mq042_nomad_spwn_v_nomad_car"},"vehicleName":"Vehicle.v_standard2_thorton_galena_bobas_player","vehicleGlobalName":"#mq042_nomad_car"}}}` | 57:False → 25:In; 61:True → 57:In; 57:True → 60:In |
| `mq042_quest_bugfixes.questphase / h323 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq042_tr_respawn_the_car"}}` | 20:True → 59:In; 60:Out → 59:In; 59:Out → 61:In |
| `mq042_quest_bugfixes.questphase / h323 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq042_tr_respawn_the_car"}}` | 26:Out → 60:In; 57:True → 60:In; 60:Out → 59:In |
| `mq042_quest_bugfixes.questphase / h323 / 61` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}]}}` | 61:True → 57:In; 59:Out → 61:In |
| `mq042_quest_bugfixes.questphase / h323 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 2:Out → 66:In; 66:Out → 6:In |
| `mq042_quest_bugfixes.questphase / h323 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleRef":{"$type":"gameEntityReference","reference":"#mq042_nomad_car"},"vehicleName":"Vehicle.v_standard2_thorton_galena_bobas_player","vehicleGlobalName":"#mq042_nomad_car"}}}` | 78:Out → 21:In; 25:Out → 78:In |
| `mq042_quest_bugfixes.questphase / h323 / 84` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq042_tr_respawn_the_car"}}` | 84:Out → 20:In; 42:Out → 84:In; 14:Out1 → 84:In |
| `mq023_01_johnny.scene / scene / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq023_01_johnny_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":80.0,"inverted":true}}}` | 79:0:0 → 206:0:1; 239:0:0 → 79:0:1 |
| `mq023_01_johnny.scene / scene / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq023_01_johnny_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":80.0,"inverted":true}}}` | 82:0:0 → 95:0:1; 95:0:0 → 94:0:1 |
| `mq042_nomad_01_hook.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 0:Out → 3:In; 3:Out → 24:Active |
| `mq042_nomad_01_hook.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/galena_80845/mq042_gps_message/02_gps_location_sent","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 26:Out → 25:Succeeded; 27:Out → 26:In |
| `mq042_nomad_01_hook.questphase / h0 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleRef":{"$type":"gameEntityReference","reference":"#mq042_nomad_car"},"vehicleName":"Vehicle.v_standard2_thorton_galena_bobas_player","vehicleGlobalName":"#mq042_nomad_car"}}}` | 34:Out → 30:In; 35:Out → 34:In |
| `mq042_nomad_01_hook.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 11:Out → 43:In; 43:Out → 45:In1 |
| `mq042_nomad_01_hook.questphase / h0 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","inverted":true}}}` | 11:Out → 44:In; 44:Out → 45:In2 |
| `mq042_nomad_01_hook.questphase / h0 / 45` | `questLogicalAndNodeDefinition` `{}` | 45:Out1 → 5:Start 0; 43:Out → 45:In1; 44:Out → 45:In2 |
| `mq042_nomad_02_car.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq042_mp_dumpster_zone"}}` | 13:Out → 2:In; 2:Out → 3:Succeeded |
| `mq042_nomad_02_car.questphase / h0 / 25` | `questCutControlNodeDefinition` `{}` | 8:End 0 → 25:In; 25:CutSource → 22:CutDestination; 25:Out → 24:In |
| `mq042_nomad_02_car.questphase / h0 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq042_tr_interrupt_area"}}` | 8:journal_update → 34:In; 42:Out1 → 34:In; 34:Out → 35:In |
| `mq042_nomad_02_car.questphase / h0 / 35` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 34:Out → 35:In; 35:True → 37:Inactive |
| `mq042_nomad_02_car.questphase / h0 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq042_tr_interrupt_area"}}` | 36:Out → 38:In; 38:Out → 39:Inactive |
| `mq042_nomad_02_car.questphase / h71 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq042_tr_interrupt_area"}}` | 4:Out → 2:In; 2:Out → 6:In1 |
| `mq042_nomad_02_car.questphase / h71 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq042_tr_interrupt_area"}}` | 9:Out → 3:In; 3:Out → 4:In |
| `mq042_nomad_02_car.questphase / h71 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq042_talk_started","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 8:In; 8:Out → 9:In |
| `mq042_nomad_02_car_found.scene / scene / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq042_nomad_car"},"eventType":"Finished"}}}` | 9:0:0 → 11:0:3; 232:0:0 → 9:0:1; 800:1:0 → 9:0:0 |
| `mq042_nomad_02_car_found.scene / scene / 99` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq042_nomad_car"},"childIsPlayer":true,"role":"Driver"}}}` | 99:0:0 → 834:0:1; 300:0:0 → 99:0:1 |
| `mq042_nomad_02_car_found.scene / scene / 175` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq042_nomad_car"},"childRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq042_nomad_02_car_found_johnny"},"role":"Passenger"}}}` | 104:0:0 → 175:0:1; 175:0:0 → 222:0:1 |
| `mq042_nomad_02_car_found.scene / scene / 222` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq042_car_taken","value":1,"comparisonType":"GreaterOrEqual"}}}` | 175:0:0 → 222:0:1; 222:0:0 → 225:0:0; 222:0:1 → 161:0:0 |
| `mq042_nomad_02_car_found.scene / scene / 771` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq042_nomad_02_car_found_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":80.0,"inverted":true}}}` | 107:0:0 → 771:0:1; 771:0:0 → 772:0:1 |
| `mq042_nomad_02_car_found.scene / scene / 797` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 797:0:0 → 238:0:3; 797:0:1 → 807:0:2; 800:0:0 → 797:0:1 |
| `mq042_nomad_02_car_found.scene / scene / 834` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 99:0:0 → 834:0:1; 834:0:0 → 102:0:3; 834:0:0 → 833:0:1 |
| `mq042_nomad_02_car_found.scene / scene / 1033` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1029:0:0 → 1033:0:1; 1033:0:0 → 1029:0:0 |
| `mq042_nomad_02_car_found.scene / scene / 1041` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1039:0:0 → 1041:0:1; 1041:0:0 → 1039:0:0 |
| `mq042_nomad_02_car_found.scene / scene / 1048` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1046:0:0 → 1048:0:1; 1048:0:0 → 1046:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_route` | mq042_nomad_02_car_found.scene / scene / 475; mq042_nomad_02_car_found.scene / scene / 930; mq042_nomad_02_car_found.scene / scene / 946 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `choice_gate` | mq023_01_johnny.scene / scene / 34; mq023_01_johnny.scene / scene / 44; mq023_01_johnny.scene / scene / 54; mq042_nomad_02_car_found.scene / scene / 115; +6 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | mq042_nomad_02_car.questphase / h71 / 8; mq042_nomad_02_car_found.scene / scene / 222; mq042_quest_bugfixes.questphase / h0 / 23; mq042_quest_bugfixes.questphase / h151 / 7; +3 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq042_nomad_02_car.questphase / h0 / 24; mq042_nomad_02_car.questphase / h0 / 26; mq042_nomad_02_car.questphase / h71 / 4; mq042_nomad_02_car.questphase / h71 / 9 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `journal_read` | mq042_nomad_01_hook.questphase / h0 / 26 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `mount_state` | mq042_nomad_02_car_found.scene / scene / 175; mq042_nomad_02_car_found.scene / scene / 99 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | mq042_nomad_01_hook.questphase / h0 / 45; mq042_quest_bugfixes.questphase / h323 / 41 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq042_nomad_01_hook.questphase / h0 / 13; mq042_nomad_02_car.questphase / h0 / 11; mq042_nomad_02_car.questphase / h0 / 19; mq042_nomad_02_car_found.scene / scene / 219; +6 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq042_quest_bugfixes.questphase / h197 / 24; mq042_quest_bugfixes.questphase / h30 / 7; mq042_quest_bugfixes.questphase / h323 / 14 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq042_nomad_01_hook.questphase / h0 / 3; mq042_nomad_02_car_found.scene / scene / 1033; mq042_nomad_02_car_found.scene / scene / 1041; mq042_nomad_02_car_found.scene / scene / 1048; +3 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq042_nomad_02_car.questphase / h0 / 25 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq042_nomad_02_car.questphase / h0 / 28 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | mq042_nomad_02_car_found.scene / scene / 9 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | mq042_nomad_01_hook.questphase / h0 / 5; mq042_nomad_02_car.questphase / h0 / 16; mq042_nomad_02_car.questphase / h0 / 8 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `vehicle_control` | mq042_nomad_01_hook.questphase / h0 / 30; mq042_nomad_01_hook.questphase / h0 / 31; mq042_nomad_01_hook.questphase / h0 / 33; mq042_nomad_01_hook.questphase / h0 / 35; +25 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq023_01_johnny.scene / scene / 182; mq023_01_johnny.scene / scene / 197; mq023_01_johnny.scene / scene / 206; mq023_01_johnny.scene / scene / 228; +28 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` | repair; journal anchor | `base-mq042` |
| `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` | content candidate; forward dependency | `base-mq023` |
| `base\quest\minor_quests\mq042\phases\mq042_nomad_01_hook.questphase` | content candidate; journal anchor | `base-mq042` |
| `base\quest\minor_quests\mq042\phases\mq042_nomad_02_car.questphase` | content candidate; journal anchor | `base-mq042` |
| `base\quest\minor_quests\mq042\scenes\mq042_nomad_01_gps_signal.scene` | content candidate; forward dependency | `base-mq042` |
| `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` | content candidate; journal anchor | `base-mq042` |

Evidence shards for this dossier (including parent context): [base-mq023](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq023.json.gz), [base-mq042](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq042.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
