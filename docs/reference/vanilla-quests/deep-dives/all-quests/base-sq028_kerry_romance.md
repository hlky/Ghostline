# Boat Drinks

Journal: `quests/side_quest/sq028_kerry_romance` · `SideQuest` · hash `2905849433`.

Journal premise: The marina, huh? Wonder what Kerry's got up his sleeve this time. Maybe he wants to get rid of someone – toss their body parts in the bay. Or maybe he just wants an audience while he waxes poetic about yachts over shrimp cocktails. Oh well, he's your problem now. Not mine.

**Coverage: journal-linked.** 60 exact journal-linked nodes in 10 resources; 12 resources in the inspected dependency context.

Resource roles in that context: 11 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Leave with Kerry. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/aftermath` |
| Swim to the shore. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/escape` |
| Help Kerry. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/help_kerry` |
| (Optional) Join Kerry. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/join_song` |
| (Optional) Set the yacht on fire. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/light_match` |
| Talk to Kerry. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry` |
| Talk to Kerry. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry2` |
| Wait for Kerry. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry` |
| Break whatever you find! (Optional) | `quests/side_quest/sq028_kerry_romance/cruiser/break_shit` |
| Talk to Kerry. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry3` |
| Wait for Kerry. (Primary) | `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry_break_things` |
| Go onto the deck. (Primary) | `quests/side_quest/sq028_kerry_romance/marina/climb_aboard` |
| Meet Kerry at the marina at 7:00 PM. (Primary) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry` |
| Talk to Kerry on the holo. (Primary) | `quests/side_quest/sq028_kerry_romance/marina/phone_call` |
| Talk to Kerry. (Primary) | `quests/side_quest/sq028_kerry_romance/marina/talk_kerry` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sq028_quest_bugfixes.questphase / h37 / 8` (Condition) | `quests/side_quest/sq028_kerry_romance/cruiser/escape` | 2:Out → 8:In; 8:True → 12:In; 8:False → 9:In |
| `sq028_quest_bugfixes.questphase / h37 / 9` (Condition) | `quests/side_quest/sq028_kerry_romance/cruiser/escape` | 8:False → 9:In; 9:True → 12:In; 9:False → 10:In |
| `sq028_quest_bugfixes.questphase / h37 / 10` (Condition) | `quests/side_quest/sq028_kerry_romance/cruiser/escape` | 10:False → 1:In; 9:False → 10:In; 10:True → 12:In |
| `sq028_quest_bugfixes.questphase / h101 / 8` (Condition) | `quests/side_quest/sq028_kerry_romance` | 8:False → 1:In; 2:Out → 8:In; 8:True → 15:In |
| `sq028_01_marina.questphase / h0 / 10` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry` | 56:Out → 10:Active; 10:Out → 75:In; 10:Out → 97:In |
| `sq028_01_marina.questphase / h0 / 11` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/phone_call` | 61:Out → 11:Active; 11:Out → 66:Active |
| `sq028_01_marina.questphase / h0 / 12` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/phone_call` | 3:End_call → 12:Succeeded; 12:Out → 56:In |
| `sq028_01_marina.questphase / h0 / 38` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/talk_kerry` | 22:End_cruiser → 38:Succeeded; 38:Out → 110:In |
| `sq028_01_marina.questphase / h0 / 42` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/talk_kerry` | 22:End_no_go → 42:Succeeded; 42:Out → 44:Failed |
| `sq028_01_marina.questphase / h0 / 44` (Journal) | `quests/side_quest/sq028_kerry_romance` | 44:Out → 34:In; 42:Out → 44:Failed |
| `sq028_01_marina.questphase / h0 / 66` (Journal) | `quests/side_quest/sq028_kerry_romance/description` | 66:Out → 3:Start_call; 11:Out → 66:Active |
| `sq028_01_marina.questphase / h0 / 93` (MappinManager) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry/wait_mp` | 97:True → 93:Active; 93:Out → 100:wait_kerry_in |
| `sq028_01_marina.questphase / h0 / 94` (MappinManager) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry/kerry` | 60:Out → 94:Active; 94:Out → 95:In |
| `sq028_01_marina.questphase / h0 / 99` (MappinManager) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry/wait_mp` | 96:False → 99:Active; 99:Out → 98:In |
| `sq028_01_marina.questphase / h0 / 103` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry` | 88:Out1 → 103:Active; 103:Out → 89:In |
| `sq028_01_marina.questphase / h0 / 112` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/phone_call` | 112:Out → 56:In; 111:Out → 112:Inactive |
| `sq028_02_cruiser.questphase / h0 / 13` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/break_shit` | 11:Out → 13:Active |
| `sq028_02_cruiser.questphase / h0 / 15` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry` | 15:Out → 5:Start 0; 15:Out → 6:Start 0; 48:Out → 15:Active |
| `sq028_02_cruiser.questphase / h0 / 18` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry2` | 50:Out → 18:Active; 18:Out → 23:Start 0 |
| `sq028_02_cruiser.questphase / h0 / 20` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry` | 6:End_break_stuff → 20:Succeeded; 20:Out → 55:In; 20:Out → 63:Active |
| `sq028_02_cruiser.questphase / h0 / 22` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry2` | 59:Out → 22:Succeeded; 22:Out → 24:Active |
| `sq028_02_cruiser.questphase / h0 / 24` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/escape` | 24:Out → 1:In; 22:Out → 24:Active; 111:Out → 24:Active; 24:Out → 106:In |
| `sq028_02_cruiser.questphase / h0 / 63` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry_break_things` | 20:Out → 63:Active; 63:Out → 62:In |
| `sq028_02_cruiser.questphase / h0 / 74` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/break_shit` | 75:True → 74:Succeeded; 74:Out → 76:In |
| `sq028_02_cruiser.questphase / h0 / 75` (Condition) | `quests/side_quest/sq028_kerry_romance/cruiser/break_shit` | 47:False → 75:In; 75:True → 74:Succeeded; 75:False → 76:In |
| `sq028_02_cruiser.questphase / h0 / 76` (Condition) | `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry_break_things` | 76:False → 50:In; 74:Out → 76:In; 75:False → 76:In; 76:True → 77:Succeeded |
| `sq028_02_cruiser.questphase / h0 / 77` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry_break_things` | 77:Out → 50:In; 76:True → 77:Succeeded |
| `sq028_03_beach.questphase / h0 / 2` (Journal) | `quests/side_quest/sq028_kerry_romance` | 35:False → 2:Succeeded; 2:Out → 76:In |
| `sq028_03_beach.questphase / h0 / 11` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry3` | 7:back_together_out → 11:Succeeded; 11:Out → 64:In |
| `sq028_03_beach.questphase / h0 / 33` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/aftermath` | 77:Out1 → 33:Succeeded; 33:Out → 50:Succeeded |
| `sq028_03_beach.questphase / h0 / 50` (Journal) | `quests/side_quest/sq028_kerry_romance` | 33:Out → 50:Succeeded; 50:Out → 75:In |
| `sq028_fail.questphase / h0 / 6` (Journal) | `quests/side_quest/sq028_kerry_romance` | 12:Out → 6:Failed; 6:Out → 14:In |
| `sq028_fail.questphase / h0 / 17` (Journal) | `quests/side_quest/sq028_kerry_romance` | 17:Out → 14:In; 16:True → 17:Succeeded |
| `sq028_fail.questphase / h0 / 18` (Condition) | `quests/side_quest/sq028_kerry_romance` | 2:Out → 18:In; 18:False → 11:Active; 18:True → 14:In |
| `sq028_02_welcome_aboard.scene / scene / 29` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry` | 4:2:0 → 29:0:3; 29:0:0 → 30:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_02_welcome_aboard.scene / scene / 30` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/climb_aboard` | 29:0:0 → 30:0:1; 30:0:0 → 121:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_02_welcome_aboard.scene / scene / 31` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/climb_aboard` | 28:0:0 → 31:0:3; 31:0:0 → 32:0:1; 209:0:0 → 31:0:3; 2603:0:0 → 31:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_02_welcome_aboard.scene / scene / 32` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/talk_kerry` | 31:0:0 → 32:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_02_welcome_aboard.scene / scene / 424` (MappinManager) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry/wait_mp` | 422:0:0 → 424:0:2; 424:0:0 → 427:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `sq028_02_welcome_aboard.scene / scene / 427` (MappinManager) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry/kerry` | 424:0:0 → 427:0:1; 427:0:0 → 2456:0:0; 427:0:0 → 2467:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `sq028_02_welcome_aboard.scene / scene / 2603` (Journal) | `quests/side_quest/sq028_kerry_romance/marina/meet_kerry` | 184:0:0 → 2603:0:3; 2603:0:0 → 31:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_04_destructive_tendencies.scene / scene / 592` (MappinManager) | `quests/side_quest/sq028_kerry_romance/cruiser/break_shit/painting_mp` | 592:0:0 → 674:0:0; 629:0:0 → 592:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `sq028_04_destructive_tendencies.scene / scene / 594` (MappinManager) | `quests/side_quest/sq028_kerry_romance/cruiser/break_shit/coffee_machine_mp` | 594:0:0 → 674:0:1; 633:0:0 → 594:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `sq028_04_destructive_tendencies.scene / scene / 596` (MappinManager) | `quests/side_quest/sq028_kerry_romance/cruiser/break_shit/gramophone_mp` | 596:0:0 → 674:0:2; 637:0:0 → 596:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `sq028_05_sex.scene / scene / 49` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/help_kerry` | 45:0:0 → 49:0:3; 49:0:0 → 9:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_05_sex.scene / scene / 333` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/break_shit` | 333:0:0 → 336:0:1; 335:0:0 → 333:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_05_sex.scene / scene / 334` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/help_kerry` | 334:0:0 → 58:0:0; 336:0:1 → 334:0:1; 337:0:0 → 334:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_05_sex.scene / scene / 335` (Condition) | `quests/side_quest/sq028_kerry_romance/cruiser/break_shit` | 335:0:0 → 333:0:3; 335:0:1 → 336:0:1; 522:2:1 → 335:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `sq028_05_sex.scene / scene / 336` (Condition) | `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry_break_things` | 333:0:0 → 336:0:1; 335:0:1 → 336:0:1; 336:0:0 → 337:0:3; 336:0:1 → 334:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `sq028_05_sex.scene / scene / 337` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry_break_things` | 336:0:0 → 337:0:3; 337:0:0 → 334:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_05_sex.scene / scene / 647` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry2` | 10:0:1 → 647:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_06_wrap_up.scene / scene / 17` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/light_match` | 17:0:0 → 6:0:0; 53:2:0 → 17:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_06_wrap_up.scene / scene / 18` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/light_match` | 8:2:1 → 18:0:3; 18:0:0 → 165:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_06_wrap_up.scene / scene / 19` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/light_match` | 10:2:1 → 19:0:2; 19:0:0 → 165:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_07_trashy_beach.scene / scene / 121` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/escape` | 121:0:0 → 137:0:1; 124:0:0 → 121:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_07_trashy_beach.scene / scene / 125` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry` | 125:0:0 → 128:0:1; 137:0:0 → 125:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_07_trashy_beach.scene / scene / 126` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry` | 126:0:0 → 135:0:1; 128:0:0 → 126:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_07_trashy_beach.scene / scene / 127` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry3` | 127:0:0 → 243:0:0; 127:0:0 → 281:0:0; 135:0:0 → 127:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_07_trashy_beach.scene / scene / 130` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/escape` | 123:0:0 → 130:0:4; 130:0:0 → 129:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq028_07_trashy_beach.scene / scene / 132` (Journal) | `quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry3` | 132:0:0 → 245:0:1; 132:0:0 → 281:0:1; 136:0:0 → 132:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sq028_01_marina.questphase / h0 / 3` | `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene`; `#sq028_01_sm_phone_call` | 66:Out → 3:Start_call; 3:End_call → 12:Succeeded; 3:rejected_out → 111:Active; 3:Holocall INT → 105:In; 3:Holocall RET → 104:In |
| `sq028_01_marina.questphase / h0 / 22` | `base\quest\side_quests\sq028\scenes\sq028_02_welcome_aboard.scene`; `#sq028_02_sm_welcome_aboard` | 57:Out → 22:Start 0; 22:End_cruiser → 38:Succeeded; 22:End_no_go → 42:Succeeded |
| `sq028_01_marina.questphase / h0 / 100` | `base\quest\side_quests\sq028\scenes\sq028_02_welcome_aboard.scene`; `#sq028_02_sm_welcome_aboard` | 100:wait_kerry_out → 89:In; 93:Out → 100:wait_kerry_in; 98:Out → 100:wait_kerry_in |
| `sq028_02_cruiser.questphase / h0 / 5` | `base\quest\side_quests\sq028\scenes\sq028_03_chilling_out.scene`; `#sq028_03_sm_chilling_out` | 15:Out → 5:Start 0 |
| `sq028_02_cruiser.questphase / h0 / 6` | `base\quest\side_quests\sq028\scenes\sq028_04_destructive_tendencies.scene`; `#sq028_04_sm_destructive_tendencies` | 15:Out → 6:Start 0; 101:Out → 6:animation_stop; 6:End_break_stuff → 20:Succeeded |
| `sq028_02_cruiser.questphase / h0 / 21` | `base\quest\side_quests\sq028\scenes\sq028_05_sex.scene`; `#sq028_05_sm_sex` | 47:True → 21:Start_demolition; 71:Out → 21:Start_demolition; 55:Out → 21:Start_demolition; 21:End 0 → 50:In; 21:sex_ending → 111:In |
| `sq028_02_cruiser.questphase / h0 / 23` | `base\quest\side_quests\sq028\scenes\sq028_06_wrap_up.scene`; `#sq028_06_sm_wrap_up` | 18:Out → 23:Start 0; 23:End 0 → 108:In |
| `sq028_03_beach.questphase / h0 / 7` | `base\quest\side_quests\sq028\scenes\sq028_07_trashy_beach.scene`; `#sq028_07_sm_trashy_beach` | 0:Out → 7:beach_in; 7:back_together_out → 11:Succeeded |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h152 / 14 | `sq028_quest_bugfixes.questphase` | 0: Input; 0:Out → 14:In1 |
| `base\quest\side_quests\sq028\sq028.questphase` / h0 / 2 | `sq028_01_marina.questphase` | 0: Input; 19: Input; 0:Out → 2:In1; 2:Out_cruiser → 14:In1; 2:Out_no_go → 15:In; 19:Out → 2:test_yacht |
| `base\quest\side_quests\sq028\sq028.questphase` / h0 / 3 | `sq028_02_cruiser.questphase` | 16: Input; 5: Input; 14: LogicalHub; 16:Out → 3:sexOnly; 5:Out → 3:In2; 14:Out1 → 3:In1; 3:Out1 → 4:In1 |
| `base\quest\side_quests\sq028\sq028.questphase` / h0 / 4 | `sq028_03_beach.questphase` | 3: Phase: sq028_02_cruiser.questphase; 7: Input; 3:Out1 → 4:In1; 4:Out1 → 15:In; 7:Out → 4:In1; 4:Out_no_relation → 15:In |
| `base\quest\side_quests\sq028\sq028.questphase` / h0 / 13 | `sq028_fail.questphase` | 14: LogicalHub; 15: CutControl; 13:Out1 → 12:In_fail; 14:Out1 → 13:In1; 15:CutSource → 13:CutDestination |
| `base\quest\side_quests\sq028\phases\sq028_01_marina.questphase` / h0 / 3 | `sq028_01_phone_call.scene` | 66: Journal; 66:Out → 3:Start_call; 3:End_call → 12:Succeeded; 3:rejected_out → 111:Active; 3:Holocall INT → 105:In; 3:Holocall RET → 104:In |
| `base\quest\side_quests\sq028\phases\sq028_01_marina.questphase` / h0 / 22 | `sq028_02_welcome_aboard.scene` | 57: Checkpoint; 57:Out → 22:Start 0; 22:End_cruiser → 38:Succeeded; 22:End_no_go → 42:Succeeded |
| `base\quest\side_quests\sq028\phases\sq028_01_marina.questphase` / h0 / 100 | `sq028_02_welcome_aboard.scene` | 93: MappinManager; 98: PauseCondition: #sq028_tr_clear_weather; 100:wait_kerry_out → 89:In; 93:Out → 100:wait_kerry_in; 98:Out → 100:wait_kerry_in |
| `base\quest\side_quests\sq028\phases\sq028_02_cruiser.questphase` / h0 / 5 | `sq028_03_chilling_out.scene` | 15: Journal; 15:Out → 5:Start 0 |
| `base\quest\side_quests\sq028\phases\sq028_02_cruiser.questphase` / h0 / 6 | `sq028_04_destructive_tendencies.scene` | 15: Journal; 101: PauseCondition: {"seconds": 3}; 15:Out → 6:Start 0; 101:Out → 6:animation_stop; 6:End_break_stuff → 20:Succeeded |
| `base\quest\side_quests\sq028\phases\sq028_02_cruiser.questphase` / h0 / 21 | `sq028_05_sex.scene` | 47: Condition: sq017_kerry_kiss GreaterOrEqual 1; 71: TeleportPuppet; 55: PauseCondition: {"seconds": 25}; 47:True → 21:Start_demolition; 71:Out → 21:Start_demolition; 55:Out → 21:Start_demolition; 21:End 0 → 50:In; 21:sex_ending → 111:In |
| `base\quest\side_quests\sq028\phases\sq028_02_cruiser.questphase` / h0 / 23 | `sq028_06_wrap_up.scene` | 18: Journal; 18:Out → 23:Start 0; 23:End 0 → 108:In |
| `base\quest\side_quests\sq028\phases\sq028_03_beach.questphase` / h0 / 7 | `sq028_07_trashy_beach.scene` | 0: Input; 0:Out → 7:beach_in; 7:back_together_out → 11:Succeeded |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\quest\side_quests\sidequests.questphase` / h0 / 41 | `sq028.questphase` | 116: PauseCondition; 116:Out → 41:In1 |
| `base\quest\side_quests\sq028\sq028.quest` / h0 / 2 | `sq028.questphase` | 3: Phase: sq028_chicken_test.questphase; 3: Phase: sq028_chicken_test.questphase; 3: Phase: sq028_chicken_test.questphase; 3: Phase: sq028_chicken_test.questphase; 3: Phase: sq028_chicken_test.questphase; 2:Out1 → 1:In; 3:Out_sex → 2:In_sex; 3:Out_beach → 2:In_beach; 3:Out_cruiser → 2:In_cruiser; 3:Out_yacht → 2:test_yacht; 3:Out1 → 2:In1 |
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
| `base\quest\cyberpunk2077.questphase` / h520 / 5 | `sidequests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:sq026_02_signal → 5:sq026_02_signal; 7:Out1 → 5:In1; 8:Out → 5:In1; 21:Out → 5:EP1_Standalone |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sq028_01_phone_call.scene` | Start_call, Start 0 → End_call, rejected_out | kerry; v; 33 nodes / 40 edges |
| `sq028_02_welcome_aboard.scene` | Start 0, wait_kerry_in, Start 1 → End_cruiser, End1, End_no_go, wait_kerry_out | kerry; johnny; yacht; v; 132 nodes / 162 edges |
| `sq028_03_chilling_out.scene` | Start 0, scene_preview, Start 3 → End 0, End 3 | kerry; johnny; sq028_com_yacht; v; 75 nodes / 88 edges |
| `sq028_04_destructive_tendencies.scene` | Start 0, Start 4, Start 5, Start 6, Start 3, Start 7, seamurai_start, animation_stop, Start1 → End_break_stuff, cleanup, seamurai_end | kerry; johnny; sq028_yacht; spawner_yaccht; v; 149 nodes / 178 edges |
| `sq028_05_sex.scene` | Start_demolition, Start 4, Start 5, Start 6, Start 3, rip, Start 2 → End 0, sex_ending | kerry; johnny; sq028yacht; v; 91 nodes / 111 edges |
| `sq028_06_wrap_up.scene` | Start 0, refuse, Start 5, Start 2, Start 6, Start 1, Start 3 → End 0 | kerry; johnny; spawner; v; 58 nodes / 64 edges |
| `sq028_07_trashy_beach.scene` | beach_in, Start 1, Start 2, mainline, Start 4 → back_together_out, cleanup | kerry; sq028_yacht; sq028_yacht_no_enviro; v; 103 nodes / 145 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sq028_01_phone_call.scene / n17 / 0` | Say no more, on my way. (``) | No option-level predicate stored | 0:0 → 19:0:0 |
| `sq028_01_phone_call.scene / n17 / 1` | Can't. Strapped for time. (``) | No option-level predicate stored | 0:1 → 21:0:0 |
| `sq028_02_welcome_aboard.scene / n7 / 0` | Ahoy back atcha. (`Greet`) | No option-level predicate stored | 0:0 → 9:0:0 |
| `sq028_02_welcome_aboard.scene / n7 / 1` | Nice dinghy ya got there. (`NiceBoat`) | No option-level predicate stored | 0:1 → 49:0:0 |
| `sq028_02_welcome_aboard.scene / n11 / 0` | [Sit] Yeah. (`yes`) | No option-level predicate stored | 0:0 → 13:0:0 |
| `sq028_02_welcome_aboard.scene / n11 / 1` | Afraid I'll have to take a rain check. (`no`) | No option-level predicate stored | 0:1 → 15:0:0 |
| `sq028_02_welcome_aboard.scene / n11 / 2` | What's the occasion? (`why`) | No option-level predicate stored | 0:2 → 265:0:1 |
| `sq028_02_welcome_aboard.scene / n11 / 3` | Nice dinghy ya got there. (`NiceBoat`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "backentry", "value": 1, "comparisonType": "Equal"}}} | 0:3 → 297:0:1 |
| `sq028_02_welcome_aboard.scene / n415 / 0` | [Wait for Kerry] (`wait`) | No option-level predicate stored | 0:0 → 2429:0:0 |
| `sq028_02_welcome_aboard.scene / n2453 / 0` | Text join unresolved (`Option`) | No option-level predicate stored | 0:0 → 2435:0:0; 0:0 → 2518:0:1 |
| `sq028_03_chilling_out.scene / n38 / 0` | What's this all about? (``) | No option-level predicate stored | 0:0 → 4:0:0 |
| `sq028_03_chilling_out.scene / n38 / 1` | Don't recognize that riff. (``) | No option-level predicate stored | 0:1 → 290:0:1 |
| `sq028_03_chilling_out.scene / n38 / 2` | Nice guitar. (``) | No option-level predicate stored | 0:2 → 285:0:1 |
| `sq028_03_chilling_out.scene / n42 / 0` | I'll bite. Tell me about the loops. (``) | No option-level predicate stored | 0:0 → 44:0:0 |
| `sq028_03_chilling_out.scene / n42 / 1` | Your... guru? (``) | No option-level predicate stored | 0:1 → 48:0:0 |
| `sq028_03_chilling_out.scene / n59 / 0` | What was that little number? (``) | No option-level predicate stored | 0:0 → 279:0:1 |
| `sq028_03_chilling_out.scene / n59 / 1` | And you needed company for that? (``) | No option-level predicate stored | 0:1 → 63:0:0 |
| `sq028_03_chilling_out.scene / n69 / 0` | Epiphany? Sounds more like maturity. (``) | No option-level predicate stored | 0:0 → 71:0:0 |
| `sq028_03_chilling_out.scene / n69 / 1` | We'll see how that works out for you. (``) | No option-level predicate stored | 0:1 → 73:0:0 |
| `sq028_03_chilling_out.scene / n99 / 0` | So what's with these loops? (``) | No option-level predicate stored | 0:0 → 44:0:0 |
| `sq028_03_chilling_out.scene / n99 / 1` | This got anything to do with the past? With Johnny? (``) | No option-level predicate stored | 0:1 → 277:0:1 |
| `sq028_04_destructive_tendencies.scene / n6 / 0` | [Stand] Let's play! (`why`) | No option-level predicate stored | 0:0 → 8:0:0; 0:0 → 395:0:1 |
| `sq028_04_destructive_tendencies.scene / n6 / 1` | [Stand] You lost your fuckin' mind?! (`nuts`) | No option-level predicate stored | 0:1 → 12:0:0; 0:1 → 395:0:1 |
| `sq028_04_destructive_tendencies.scene / n19 / 0` | Let's rip the whole fuckin' boat apart. (`OK`) | {"questCondition": {"$type": "questSystemCondition", "type": {"$type": "questCameraFocus_ConditionType", "objectRef": {"$type": "gameEntityReference", "reference": "#kerry"}, "timeInterval": 0.10000000149011612, "onScreenTest": true}}} | 0:0 → 373:0:1; 0:0 → 397:0:1 |
| `sq028_04_destructive_tendencies.scene / n19 / 1` | Think I'll sit this one out. (`Nope`) | {"questCondition": {"$type": "questSystemCondition", "type": {"$type": "questCameraFocus_ConditionType", "objectRef": {"$type": "gameEntityReference", "reference": "#kerry"}, "timeInterval": -1.0, "onScreenTest": true}}} | 0:1 → 378:0:1 |
| `sq028_04_destructive_tendencies.scene / n64 / 0` | Fine, but doin' this for you, not me. (`join kerry`) | No option-level predicate stored | 0:0 → 21:0:0; 0:0 → 164:1:0; 0:0 → 397:0:1 |
| `sq028_04_destructive_tendencies.scene / n164 / 0` | The answer's no. (`no`) | No option-level predicate stored | 0:0 → 64:1:0; 0:0 → 166:0:0; 0:0 → 698:0:1 |
| `sq028_04_destructive_tendencies.scene / n578 / 0` | [Destroy painting] (`Option`) | No option-level predicate stored | 0:0 → 629:0:0; 0:0 → 811:0:0 |
| `sq028_04_destructive_tendencies.scene / n581 / 0` | [Destroy coffee machine] (`Option`) | No option-level predicate stored | 0:0 → 633:0:0; 0:0 → 811:0:0 |
| `sq028_04_destructive_tendencies.scene / n582 / 0` | [Destroy record player] (`Option`) | No option-level predicate stored | 0:0 → 637:0:0; 0:0 → 811:0:0 |
| `sq028_05_sex.scene / n10 / 0` | [Kiss] (`sex`) | No option-level predicate stored | 0:0 → 550:0:0; 0:0 → 616:0:1; 0:0 → 650:0:1 |
| `sq028_05_sex.scene / n10 / 1` | [Stop Kerry] You got the wrong idea... (`no_sex`) | No option-level predicate stored | 0:1 → 15:0:0; 0:1 → 199:0:1; 0:1 → 647:0:1 |
| `sq028_05_sex.scene / n45 / 0` | [Help Kerry] (`RIP_OUT_E`) | No option-level predicate stored | 0:0 → 49:0:3; 0:0 → 589:0:1; 0:0 → 614:0:1 |
| `sq028_06_wrap_up.scene / n6 / 0` | [Set yacht on fire] To getting even! (`agree`) | No option-level predicate stored | 0:0 → 8:0:0 |
| `sq028_06_wrap_up.scene / n6 / 1` | It's your party – you finish it. (`refuse`) | No option-level predicate stored | 0:1 → 10:0:0 |
| `sq028_07_trashy_beach.scene / n20 / 0` | Preem way to settle a score. (`Fun`) | No option-level predicate stored | 0:0 → 22:0:0 |
| `sq028_07_trashy_beach.scene / n20 / 1` | How's it feel to be livin' on the edge? (`Crazy`) | No option-level predicate stored | 0:1 → 24:0:0 |
| `sq028_07_trashy_beach.scene / n20 / 2` | Got what you wanted. What now? (`What now`) | No option-level predicate stored | 0:2 → 26:0:0 |
| `sq028_07_trashy_beach.scene / n49 / 0` | [Fast travel] 'Course. (`sure`) | No option-level predicate stored | 0:0 → 52:0:0 |
| `sq028_07_trashy_beach.scene / n49 / 1` | [Stand] I'll be all right. (`no`) | No option-level predicate stored | 0:1 → 55:0:0; 0:1 → 459:0:0 |
| `sq028_07_trashy_beach.scene / n59 / 0` | [Hug] Pencil me in. (`commit`) | No option-level predicate stored | 0:0 → 60:0:0 |
| `sq028_07_trashy_beach.scene / n59 / 1` | [pl_pl][wstań] To była jednorazowa przygoda. (`on_night_stand`) | No option-level predicate stored | 0:1 → 61:0:0; 0:1 → 459:0:0 |
| `sq028_07_trashy_beach.scene / n76 / 0` | [Sit] Beautiful, isn't it. (`sit`) | No option-level predicate stored | 0:0 → 270:0:0 |
| `sq028_07_trashy_beach.scene / n76 / 1` | [Sit] What if it doesn't blow? (`boom`) | No option-level predicate stored | 0:1 → 266:0:0 |
| `sq028_07_trashy_beach.scene / n76 / 2` | [Sit] So many eddies're gonna go under… (`money`) | No option-level predicate stored | 0:2 → 260:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `#sq028_kerry_talk_finished` | sq028_03_chilling_out.scene / scene / 187 | sq028_04_destructive_tendencies.scene / scene / 246; sq028_04_destructive_tendencies.scene / scene / 305 |
| `CYB-12345` | sq028_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-588988` | sq028_quest_bugfixes.questphase / h37 / 2 | No reader in selected context |
| `CYB-613840` | sq028_quest_bugfixes.questphase / h101 / 2 | No reader in selected context |
| `backentry` | sq028_02_welcome_aboard.scene / scene / 205 | sq028_02_welcome_aboard.scene / scene / 11 |
| `censorship_homosexuality` | Producer outside selected context | sq028_03_chilling_out.scene / scene / 159; sq028_04_destructive_tendencies.scene / scene / 753; sq028_05_sex.scene / scene / 209 |
| `censorship_oversexualized` | Producer outside selected context | sq028_05_sex.scene / scene / 124 |
| `ep1_active` | Producer outside selected context | sq028_04_destructive_tendencies.scene / scene / 853 |
| `holo_kerry_calls_v_end_activate` | sq028_01_marina.questphase / h0 / 105; sq028_01_phone_call.scene / scene / 154 | No reader in selected context |
| `holo_kerry_calls_v_end_done` | sq028_01_phone_call.scene / scene / 150 | sq028_01_phone_call.scene / scene / 149 |
| `holo_kerry_calls_v_rejectable` | sq028_01_phone_call.scene / scene / 249 | No reader in selected context |
| `holo_kerry_calls_v_rejected` | sq028_01_phone_call.scene / scene / 251 | sq028_01_phone_call.scene / scene / 253 |
| `holo_kerry_calls_v_start_activate` | sq028_01_marina.questphase / h0 / 104; sq028_01_phone_call.scene / scene / 153 | No reader in selected context |
| `holo_kerry_calls_v_start_done` | sq028_01_phone_call.scene / scene / 148 | sq028_01_phone_call.scene / scene / 147 |
| `kerry_default_on` | sq028_01_marina.questphase / h0 / 58; sq028_01_marina.questphase / h272 / 2 | No reader in selected context |
| `kerry_romanceable` | Producer outside selected context | sq028_03_chilling_out.scene / scene / 159 |
| `sq017_kerry_kiss` | Producer outside selected context | sq028_02_cruiser.questphase / h0 / 47; sq028_04_destructive_tendencies.scene / scene / 752; sq028_05_sex.scene / scene / 67 |
| `sq028_02_welcome_aboard_kerry_lookat_02` | sq028_02_welcome_aboard.scene / scene / 2523; sq028_02_welcome_aboard.scene / scene / 335; sq028_02_welcome_aboard.scene / scene / 336 | sq028_02_welcome_aboard.scene / scene / 334; sq028_02_welcome_aboard.scene / scene / 337 |
| `sq028_04_breathing` | sq028_04_destructive_tendencies.scene / scene / 796; sq028_04_destructive_tendencies.scene / scene / 804 | sq028_04_destructive_tendencies.scene / scene / 810 |
| `sq028_05_sex_scene_started` | sq028_05_sex.scene / scene / 589 | sq028_04_destructive_tendencies.scene / scene / 718; sq028_04_destructive_tendencies.scene / scene / 758 |
| `sq028_active` | sq028_01_marina.questphase / h0 / 61; sq028_01_marina.questphase / h272 / 4 | No reader in selected context |
| `sq028_break_shit` | sq028_02_cruiser.questphase / h0 / 11 | No reader in selected context |
| `sq028_chilling_idle_active` | sq028_03_chilling_out.scene / scene / 336 | sq028_01_marina.questphase / h0 / 107; sq028_02_welcome_aboard.scene / scene / 2473 |
| `sq028_close_to_beach` | sq028_04_destructive_tendencies.scene / scene / 190 | sq028_03_chilling_out.scene / scene / 251; sq028_fail.questphase / h0 / 10 |
| `sq028_cut_choices_from_04` | sq028_02_cruiser.questphase / h0 / 110 | sq028_04_destructive_tendencies.scene / scene / 835 |
| `sq028_decided_to_demo_with_kerry` | sq028_04_destructive_tendencies.scene / scene / 174 | sq028_02_cruiser.questphase / h0 / 60; sq028_02_cruiser.questphase / h0 / 62 |
| `sq028_getting_a_lift` | sq028_03_beach.questphase / h156 / 12 | sq028_fail.questphase / h0 / 8 |
| `sq028_kerry_dislike` | sq028_07_trashy_beach.scene / scene / 118 | No reader in selected context |
| `sq028_kerry_eurodyne_nude` | sq028_05_sex.scene / scene / 196 | sq028_05_sex.scene / scene / 556 |
| `sq028_kerry_friend` | sq028_07_trashy_beach.scene / scene / 115 | No reader in selected context |
| `sq028_kerry_goes_home_alone` | sq028_03_beach.questphase / h0 / 83 | No reader in selected context |
| `sq028_kerry_relationship` | sq028_07_trashy_beach.scene / scene / 66 | No reader in selected context |
| `sq028_kerry_sex` | sq028_05_sex.scene / scene / 35 | sq028_02_cruiser.questphase / h0 / 108; sq028_07_trashy_beach.scene / scene / 92 |
| `sq028_kerry_song_finished` | sq028_03_chilling_out.scene / scene / 419 | sq028_04_destructive_tendencies.scene / scene / 727 |
| `sq028_kerry_song_travel_skipped` | sq028_04_destructive_tendencies.scene / scene / 737 | sq028_03_chilling_out.scene / scene / 429 |
| `sq028_started` | sq028_01_marina.questphase / h0 / 63; sq028_01_marina.questphase / h272 / 5 | No reader in selected context |
| `sq028_taxi_together` | sq028_07_trashy_beach.scene / scene / 70 | sq028_03_beach.questphase / h0 / 35; sq028_fail.questphase / h0 / 16 |
| `sq028_yacht_burnt` | sq028_02_cruiser.questphase / h0 / 59 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | sq028_quest_bugfixes.questphase / h0 / 16 |
| `urge` | sq028_01_phone_call.scene / scene / 63; sq028_01_phone_call.scene / scene / 66 | sq028_01_phone_call.scene / scene / 62; sq028_01_phone_call.scene / scene / 64 |

## Exact gates, joins and cancellation

<details><summary>135 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sq028_quest_bugfixes.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` |  |
| `sq028_quest_bugfixes.questphase / h37 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq028_kerry_romance/cruiser/escape","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 8:In; 8:True → 12:In; 8:False → 9:In |
| `sq028_quest_bugfixes.questphase / h37 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq028_kerry_romance/cruiser/escape","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 8:False → 9:In; 9:True → 12:In; 9:False → 10:In |
| `sq028_quest_bugfixes.questphase / h37 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq028_kerry_romance/cruiser/escape","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Failed"}}}` | 10:False → 1:In; 9:False → 10:In; 10:True → 12:In |
| `sq028_quest_bugfixes.questphase / h101 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq028_kerry_romance","fileEntryIndex":2},"state":"Failed"}}}` | 8:False → 1:In; 2:Out → 8:In; 8:True → 15:In |
| `sq028_quest_bugfixes.questphase / h101 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 15:Out → 18:In; 18:Out → 16:In |
| `sq028_01_marina.questphase / h0 / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0},"comparisonType":"GreaterOrEqual"}}}` | 57:Out → 71:In; 74:Out → 71:In; 71:Out → 72:In |
| `sq028_01_marina.questphase / h0 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":90.0},"comparisonType":"Less"}}}` | 72:Out → 73:In; 73:Out → 74:In |
| `sq028_01_marina.questphase / h0 / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_clear_weather"}}` | 10:Out → 75:In; 78:Out → 75:In; 75:Out → 76:In |
| `sq028_01_marina.questphase / h0 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#sq028_tr_clear_weather"}}` | 76:Out → 77:In; 77:Out → 79:In |
| `sq028_01_marina.questphase / h0 / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 77:Out → 79:In; 79:Out → 78:In |
| `sq028_01_marina.questphase / h0 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":90.0},"comparisonType":"Less"}}}` | 89:Out → 70:In; 95:Out → 89:In; 103:Out → 89:In; 100:wait_kerry_out → 89:In |
| `sq028_01_marina.questphase / h0 / 91` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 0:Out → 91:In; 91:Out → 64:In |
| `sq028_01_marina.questphase / h0 / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_clear_weather"}}` | 95:Out → 89:In; 94:Out → 95:In |
| `sq028_01_marina.questphase / h0 / 96` | `questConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":64800},"end":{"$type":"GameTime","seconds":70200}}}}` | 96:True → 60:In; 97:False → 96:In; 96:False → 99:Active |
| `sq028_01_marina.questphase / h0 / 97` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_clear_weather"}}` | 10:Out → 97:In; 97:True → 93:Active; 97:False → 96:In |
| `sq028_01_marina.questphase / h0 / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_clear_weather"}}` | 99:Out → 98:In; 98:Out → 100:wait_kerry_in |
| `sq028_01_marina.questphase / h0 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_chilling_idle_active","value":1,"comparisonType":"Equal"}}}` | 62:Out → 107:In; 107:Out → 108:In |
| `sq028_02_cruiser.questphase / h0 / 47` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_kerry_kiss","value":1,"comparisonType":"GreaterOrEqual"}}}` | 47:True → 21:Start_demolition; 102:Out → 47:In; 47:False → 75:In |
| `sq028_02_cruiser.questphase / h0 / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":25}}}` | 20:Out → 55:In; 55:Out → 21:Start_demolition; 55:Out → 110:In |
| `sq028_02_cruiser.questphase / h0 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_decided_to_demo_with_kerry","value":1,"comparisonType":"GreaterOrEqual"}}}` | 60:Out → 11:In; 62:False → 60:In |
| `sq028_02_cruiser.questphase / h0 / 62` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_decided_to_demo_with_kerry","value":1,"comparisonType":"GreaterOrEqual"}}}` | 62:True → 11:In; 62:False → 60:In; 63:Out → 62:In |
| `sq028_02_cruiser.questphase / h0 / 75` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq028_kerry_romance/cruiser/break_shit","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 47:False → 75:In; 75:True → 74:Succeeded; 75:False → 76:In |
| `sq028_02_cruiser.questphase / h0 / 76` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry_break_things","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 76:False → 50:In; 74:Out → 76:In; 75:False → 76:In; 76:True → 77:Succeeded |
| `sq028_02_cruiser.questphase / h0 / 101` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 101:Out → 6:animation_stop; 97:Out → 101:In |
| `sq028_02_cruiser.questphase / h0 / 106` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 24:Out → 106:In; 106:Out → 107:In |
| `sq028_02_cruiser.questphase / h0 / 108` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_kerry_sex","value":1,"comparisonType":"GreaterOrEqual"}}}` | 23:End 0 → 108:In; 108:True → 59:In; 108:False → 109:In |
| `sq028_03_beach.questphase / h0 / 35` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_taxi_together","value":1,"comparisonType":"GreaterOrEqual"}}}` | 35:False → 2:Succeeded; 28:Out → 35:In; 35:True → 77:In1 |
| `sq028_03_beach.questphase / h0 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry_vehicle"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 37:Out → 38:In; 38:Out → 79:In; 38:Out → 81:In2 |
| `sq028_03_beach.questphase / h0 / 81` | `questLogicalAndNodeDefinition` `{}` | 38:Out → 81:In2; 39:Out → 81:In1; 81:Out1 → 42:In; 81:Out1 → 86:In |
| `sq028_03_beach.questphase / h0 / 85` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 37:Out → 85:In; 85:Out → 84:In |
| `sq028_03_beach.questphase / h156 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 8:Out → 6:In; 6:Out → 7:In |
| `sq028_03_beach.questphase / h156 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3:Out → 9:In; 9:Out → 11:In1 |
| `sq028_03_beach.questphase / h156 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry_vehicle"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 3:Out → 10:In; 10:Out → 11:In2 |
| `sq028_03_beach.questphase / h156 / 11` | `questLogicalAndNodeDefinition` `{}` | 11:Out1 → 4:In; 9:Out → 11:In1; 10:Out → 11:In2 |
| `sq028_fail.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0}}}}` | 7:Out → 2:In; 2:Out → 18:In |
| `sq028_fail.questphase / h0 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":200.0}}}}` | 16:False → 4:In; 4:Out → 12:Active |
| `sq028_fail.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 7:Out → 2:In; 10:Out → 7:In |
| `sq028_fail.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_getting_a_lift","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 8:In; 8:Out → 15:In |
| `sq028_fail.questphase / h0 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_close_to_beach","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 10:In; 10:Out → 7:In |
| `sq028_fail.questphase / h0 / 16` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_taxi_together","value":1,"comparisonType":"GreaterOrEqual"}}}` | 16:False → 4:In; 11:Out → 16:In; 16:True → 17:Succeeded |
| `sq028_fail.questphase / h0 / 18` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq028_kerry_romance","fileEntryIndex":2},"state":"Succeeded"}}}` | 2:Out → 18:In; 18:False → 11:Active; 18:True → 14:In |
| `sq028_01_phone_call.scene / scene / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 59:0:0 → 63:0:1; 62:0:1 → 59:0:1; 68:1:0 → 59:0:0 |
| `sq028_01_phone_call.scene / scene / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":33}}}` | 60:0:0 → 67:0:0; 64:0:0 → 60:0:1; 68:1:0 → 60:0:0 |
| `sq028_01_phone_call.scene / scene / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":25}}}` | 61:0:0 → 66:0:1; 64:0:1 → 61:0:1; 68:1:0 → 61:0:0 |
| `sq028_01_phone_call.scene / scene / 62` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"urge"}}}` | 58:0:0 → 62:0:1; 62:0:0 → 64:0:1; 62:0:1 → 59:0:1; 71:0:0 → 62:0:1 |
| `sq028_01_phone_call.scene / scene / 64` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"urge","value":1}}}` | 62:0:0 → 64:0:1; 64:0:0 → 60:0:1; 64:0:1 → 61:0:1 |
| `sq028_01_phone_call.scene / scene / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 4:2:0 → 69:0:1; 68:1:0 → 69:0:0; 69:0:0 → 67:0:0 |
| `sq028_01_phone_call.scene / scene / 147` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_kerry_calls_v_start_done"}}}` | 147:0:0 → 148:0:1; 153:0:0 → 147:0:1 |
| `sq028_01_phone_call.scene / scene / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_kerry_calls_v_end_done"}}}` | 149:0:0 → 150:0:1; 154:0:0 → 149:0:1 |
| `sq028_01_phone_call.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_kerry_calls_v_rejected"}}}` | 153:0:0 → 253:0:1; 253:0:0 → 251:0:1 |
| `sq028_02_welcome_aboard.scene / scene / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_cabin_cruiser"}}` | 28:0:0 → 7:0:0; 28:0:0 → 31:0:3; 117:2:0 → 28:0:1 |
| `sq028_02_welcome_aboard.scene / scene / 121` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_come_aboard"}}` | 30:0:0 → 121:0:1; 121:0:0 → 117:0:0; 121:0:0 → 209:0:1 |
| `sq028_02_welcome_aboard.scene / scene / 184` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_backentrance"}}` | 114:0:0 → 184:0:1; 184:0:0 → 111:0:0; 184:0:0 → 186:0:0; 184:0:0 → 197:0:0; 184:0:0 → 205:0:1; 184:0:0 → 2603:0:3; 200:1:0 → 184:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 192` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_near_kerry"}}` | 114:0:0 → 192:0:1; 192:0:0 → 4:0:0; 192:0:0 → 200:0:0; 197:1:0 → 192:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 209` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_cheeky_player"}}` | 7:1:0 → 209:0:0; 121:0:0 → 209:0:1; 209:0:0 → 31:0:3; 209:0:0 → 222:0:0; 209:0:0 → 226:0:1; 209:0:0 → 2505:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 226` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 209:0:0 → 226:0:1; 226:0:0 → 211:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 229` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 9:0:0 → 229:0:1; 229:0:0 → 179:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 244` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 114:0:0 → 244:0:1; 244:0:0 → 80:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 265` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq028\\scenes\\sq028_02_welcome_aboard.scene","Flags":"Soft"},"sectionName":"sq028_02_details","type":"IsOutside"}}}` | 11:0:2 → 265:0:1; 265:0:0 → 17:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 297` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq028\\scenes\\sq028_02_welcome_aboard.scene","Flags":"Soft"},"sectionName":"sq028_02_NiceBoat","type":"IsOutside"}}}` | 11:0:3 → 297:0:1; 297:0:0 → 204:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 316` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 314:0:0 → 316:0:1; 316:0:0 → 319:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 317` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 314:0:1 → 317:0:1; 317:0:0 → 319:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 318` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 314:0:2 → 318:0:1; 318:0:0 → 319:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 327` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 326:0:0 → 327:0:1; 327:0:0 → 330:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 328` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 326:0:1 → 328:0:1; 328:0:0 → 330:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 329` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 326:0:2 → 329:0:1; 329:0:0 → 330:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 334` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_02_welcome_aboard_kerry_lookat_02"}}}` | 333:0:0 → 334:0:1; 334:0:0 → 332:0:0; 334:0:1 → 337:0:1; 336:0:0 → 334:0:1 |
| `sq028_02_welcome_aboard.scene / scene / 337` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_02_welcome_aboard_kerry_lookat_02"}}}` | 334:0:1 → 337:0:1; 337:0:0 → 332:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 422` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 422:0:0 → 424:0:2; 425:0:0 → 422:0:1 |
| `sq028_02_welcome_aboard.scene / scene / 2473` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_chilling_idle_active","value":1,"comparisonType":"Equal"}}}` | 175:0:0 → 2473:0:1; 2473:0:0 → 2481:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 2489` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 2456:2:0 → 2489:0:1; 2489:0:0 → 2492:0:1 |
| `sq028_02_welcome_aboard.scene / scene / 2529` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":15.0}}}}` | 15:0:0 → 2529:0:1; 2529:0:0 → 2530:0:0; 2529:0:0 → 2591:0:1 |
| `sq028_02_welcome_aboard.scene / scene / 2591` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0}}}}` | 2529:0:0 → 2591:0:1; 2591:0:0 → 2594:0:0 |
| `sq028_02_welcome_aboard.scene / scene / 2630` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0}}}}` | 232:0:0 → 2630:0:1; 2616:2:0 → 2630:0:1; 2630:0:0 → 2631:0:1 |
| `sq028_02_welcome_aboard.scene / scene / 2631` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0},"comparisonType":"Less"}}}` | 2630:0:0 → 2631:0:1; 2631:0:0 → 2616:0:0 |
| `sq028_03_chilling_out.scene / scene / 159` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kerry_romanceable","value":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_homosexuality","comparisonType":"Equal"}}]}}` | 63:0:0 → 159:0:1; 159:0:0 → 66:0:0; 159:0:1 → 162:0:0 |
| `sq028_03_chilling_out.scene / scene / 206` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 1:0:0 → 206:0:1; 206:0:0 → 214:0:1; 206:0:0 → 343:0:0; 206:0:0 → 357:0:0; 206:0:0 → 429:0:1 |
| `sq028_03_chilling_out.scene / scene / 214` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 206:0:0 → 214:0:1; 214:0:0 → 38:0:0 |
| `sq028_03_chilling_out.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_close_to_beach","value":1,"comparisonType":"GreaterOrEqual"}}}` | 187:0:0 → 251:0:1; 251:0:0 → 253:0:1 |
| `sq028_03_chilling_out.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq028_03_chilling_out_johnny"},"timeInterval":0.5,"onScreenTest":true,"angleTolerance":75.0,"inverted":true}}}` | 251:0:0 → 253:0:1; 253:0:0 → 255:0:0 |
| `sq028_03_chilling_out.scene / scene / 277` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq028\\scenes\\sq028_03_chilling_out.scene","Flags":"Soft"},"sectionName":"sq028_03_johnny","type":"IsOutside"}}}` | 99:0:1 → 277:0:1; 277:0:0 → 55:0:0 |
| `sq028_03_chilling_out.scene / scene / 279` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq028\\scenes\\sq028_03_chilling_out.scene","Flags":"Soft"},"sectionName":"sq028_03_bleedthebeat","type":"IsOutside"}}}` | 59:0:0 → 279:0:1; 279:0:0 → 61:0:0 |
| `sq028_03_chilling_out.scene / scene / 285` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq028\\scenes\\sq028_03_chilling_out.scene","Flags":"Soft"},"sectionName":"sq028_kerrys_guitar","type":"IsOutside"}}}` | 38:0:2 → 285:0:1; 285:0:0 → 79:0:0 |
| `sq028_03_chilling_out.scene / scene / 290` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq028\\scenes\\sq028_03_chilling_out.scene","Flags":"Soft"},"sectionName":"sq28_03_new_song","type":"IsOutside"}}}` | 38:0:1 → 290:0:1; 290:0:0 → 91:0:0 |
| `sq028_03_chilling_out.scene / scene / 319` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}}}` | 317:0:0 → 319:0:1; 319:0:0 → 321:0:0 |
| `sq028_03_chilling_out.scene / scene / 327` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"timeInterval":0.10000000149011612,"onScreenTest":true}}}` | 321:0:0 → 327:0:1; 327:0:0 → 317:0:0 |
| `sq028_03_chilling_out.scene / scene / 429` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_kerry_song_travel_skipped","value":1,"comparisonType":"Equal"}}}` | 206:0:0 → 429:0:1; 429:0:0 → 430:0:0 |
| `sq028_03_chilling_out.scene / scene / 439` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 419:0:0 → 439:0:1; 439:0:0 → 422:0:0 |
| `sq028_04_destructive_tendencies.scene / scene / 153` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 146:0:0 → 153:0:1; 153:0:0 → 108:0:0 |
| `sq028_04_destructive_tendencies.scene / scene / 246` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#sq028_kerry_talk_finished"}}}` | 235:0:0 → 246:0:1; 246:0:0 → 413:0:1; 265:1:0 → 246:0:0 |
| `sq028_04_destructive_tendencies.scene / scene / 260` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questInputAction_ConditionType","inputAction":"Exit"}}}` | 260:0:0 → 261:0:1; 260:0:0 → 425:0:1; 268:1:0 → 260:0:0; 858:0:0 → 260:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 263` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":600}}}` | 261:0:0 → 263:0:1; 263:0:0 → 262:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_near_beach"}}` | 258:0:0 → 267:0:1; 267:0:0 → 309:0:0 |
| `sq028_04_destructive_tendencies.scene / scene / 272` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 266:0:0 → 272:0:1; 272:0:0 → 273:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 274` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 273:0:0 → 274:0:1; 274:0:0 → 862:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 305` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"#sq028_kerry_talk_finished"}}}` | 1:0:0 → 305:0:1; 305:0:0 → 258:0:0 |
| `sq028_04_destructive_tendencies.scene / scene / 308` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#sq028_tp_skip_kerry_cruise"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0},"comparisonType":"LessOrEqual"}}}` | 258:0:0 → 308:0:1; 308:0:0 → 309:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 315` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpeed_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#sq028_com_yacht"},"speed":7.0,"comparisonType":"CT_GREATER_EQUAL"}}}` | 1:0:0 → 315:0:1; 315:0:0 → 270:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 370` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 14:0:0 → 370:0:1; 370:0:0 → 369:0:0 |
| `sq028_04_destructive_tendencies.scene / scene / 383` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq028_04_destructive_tendencies_johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 383:0:0 → 435:0:0; 698:0:0 → 383:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 410` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 410:0:0 → 4:0:0; 410:0:0 → 555:0:1; 727:0:0 → 410:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 413` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 246:0:0 → 413:0:1; 345:0:0 → 413:0:1; 386:0:0 → 413:0:1; 413:0:0 → 406:0:1; 413:0:0 → 853:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 563` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":600}}}` | 563:0:0 → 271:0:1; 607:0:0 → 563:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 705` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq028_04_destructive_tendencies_johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 674:0:0 → 705:0:1; 705:0:0 → 720:0:0 |
| `sq028_04_destructive_tendencies.scene / scene / 718` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_05_sex_scene_started","value":1,"comparisonType":"Equal"}}}` | 170:0:0 → 718:0:1; 718:0:0 → 720:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 727` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_kerry_song_finished","value":1,"comparisonType":"Equal"}}}` | 406:0:0 → 727:0:1; 727:0:0 → 410:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 748` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_04_water_level_check"}}` | 748:0:0 → 764:0:1; 755:0:0 → 748:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 752` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_kerry_kiss","comparisonType":"Equal"}}}` | 752:0:0 → 755:0:0; 758:0:1 → 752:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 753` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_homosexuality","comparisonType":"Equal"}}}` | 753:0:0 → 755:0:1; 758:0:1 → 753:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 758` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_05_sex_scene_started","value":1,"comparisonType":"Equal"}},null]}}` | 707:3:0 → 758:0:1; 758:0:0 → 764:0:0; 758:0:1 → 752:0:1; 758:0:1 → 753:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 799` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 775:0:0 → 799:0:1; 799:0:0 → 776:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 810` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_04_breathing"}}}` | 810:0:1 → 796:0:1; 811:0:0 → 810:0:1 |
| `sq028_04_destructive_tendencies.scene / scene / 835` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_cut_choices_from_04","value":1,"comparisonType":"GreaterOrEqual"}}}` | 61:0:0 → 835:0:1; 835:0:0 → 64:1:0; 835:0:0 → 164:1:0 |
| `sq028_04_destructive_tendencies.scene / scene / 853` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_active","comparisonType":"Equal"}}}` | 413:0:0 → 853:0:1; 853:0:0 → 849:0:1 |
| `sq028_05_sex.scene / scene / 67` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq017_kerry_kiss","value":1,"comparisonType":"GreaterOrEqual"}}}` | 67:0:0 → 10:0:0; 67:0:0 → 205:0:1; 67:0:1 → 70:0:0; 209:0:1 → 67:0:1 |
| `sq028_05_sex.scene / scene / 124` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_oversexualized"}}}` | 124:0:0 → 128:0:0; 124:0:0 → 224:0:1; 124:0:1 → 94:0:0; 124:0:1 → 106:0:1; 158:0:0 → 124:0:1 |
| `sq028_05_sex.scene / scene / 209` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_homosexuality"}}}` | 9:0:0 → 209:0:1; 209:0:0 → 243:0:0; 209:0:1 → 67:0:1 |
| `sq028_05_sex.scene / scene / 335` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq028_kerry_romance/cruiser/break_shit","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 335:0:0 → 333:0:3; 335:0:1 → 336:0:1; 522:2:1 → 335:0:1 |
| `sq028_05_sex.scene / scene / 336` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq028_kerry_romance/cruiser/wait_kerry_break_things","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 333:0:0 → 336:0:1; 335:0:1 → 336:0:1; 336:0:0 → 337:0:3; 336:0:1 → 334:0:1 |
| `sq028_05_sex.scene / scene / 556` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_kerry_eurodyne_nude"}}}` | 94:2:15 → 556:0:1; 128:2:8 → 556:0:1; 556:0:0 → 557:0:1 |
| `sq028_05_sex.scene / scene / 594` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 158:0:0 → 594:0:1; 594:0:0 → 592:0:1 |
| `sq028_06_wrap_up.scene / scene / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq028_06_wrap_up_johnny"},"timeInterval":0.5,"onScreenTest":true,"inverted":true}}}` | 6:1:0 → 128:0:1; 128:0:0 → 180:0:0 |
| `sq028_06_wrap_up.scene / scene / 145` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":10}}}` | 8:2:1 → 145:0:1; 10:2:0 → 145:0:1; 145:0:0 → 142:0:1; 145:0:0 → 264:0:1 |
| `sq028_06_wrap_up.scene / scene / 153` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":30}}}` | 8:2:1 → 153:0:1; 10:2:0 → 153:0:1; 153:0:0 → 152:0:1; 153:0:0 → 246:0:1; 153:0:0 → 256:0:1 |
| `sq028_06_wrap_up.scene / scene / 234` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":30}}}` | 8:2:1 → 234:0:1; 10:2:0 → 234:0:1; 234:0:0 → 236:0:1; 234:0:0 → 248:0:1 |
| `sq028_06_wrap_up.scene / scene / 238` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":30}}}` | 8:2:1 → 238:0:1; 10:2:0 → 238:0:1; 238:0:0 → 240:0:1; 238:0:0 → 250:0:1; 238:0:0 → 252:0:1; 238:0:0 → 253:0:1; 238:0:0 → 274:0:1 |
| `sq028_06_wrap_up.scene / scene / 266` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq028_06_wrap_up_johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}}}` | 70:0:0 → 266:0:1; 266:0:0 → 269:0:0 |
| `sq028_07_trashy_beach.scene / scene / 92` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq028_kerry_sex","value":1,"comparisonType":"GreaterOrEqual"}}}` | 22:0:0 → 92:0:1; 24:0:0 → 92:0:1; 26:0:0 → 92:0:1; 92:0:0 → 42:0:0; 92:0:1 → 97:0:0 |
| `sq028_07_trashy_beach.scene / scene / 106` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 100:0:0 → 106:0:1; 106:0:0 → 103:0:1 |
| `sq028_07_trashy_beach.scene / scene / 122` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_beach"}}` | 1:0:0 → 122:0:1; 122:0:0 → 124:0:0; 122:0:0 → 501:0:1; 129:1:0 → 122:0:0 |
| `sq028_07_trashy_beach.scene / scene / 123` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_beach","activatorRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"isPlayerActivator":false}}` | 1:0:0 → 123:0:1; 123:0:0 → 130:0:4; 124:1:0 → 123:0:0 |
| `sq028_07_trashy_beach.scene / scene / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq028_tr_beach","activatorRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"isPlayerActivator":false}}` | 125:0:0 → 128:0:1; 128:0:0 → 126:0:3 |
| `sq028_07_trashy_beach.scene / scene / 448` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"timeInterval":0.30000001192092896,"onScreenTest":true,"inverted":true}}}` | 197:0:0 → 448:0:1; 448:0:0 → 450:0:0; 455:0:0 → 448:0:1; 459:1:0 → 448:0:0; 459:1:0 → 448:1026:0 |
| `sq028_07_trashy_beach.scene / scene / 452` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"timeInterval":0.30000001192092896,"onScreenTest":true}}}` | 450:0:0 → 452:0:1; 452:0:0 → 455:0:0; 459:1:0 → 452:0:0; 459:1:0 → 452:1026:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sq028_02_welcome_aboard.scene / scene / 244; sq028_03_beach.questphase / h0 / 38; sq028_03_beach.questphase / h156 / 10; sq028_03_beach.questphase / h156 / 9; +1 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | sq028_03_beach.questphase / h0 / 39; sq028_04_destructive_tendencies.scene / scene / 150; sq028_04_destructive_tendencies.scene / scene / 84; sq028_05_sex.scene / scene / 327; +2 locations in catalogue.json | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | sq028_01_marina.questphase / h0 / 56; sq028_01_marina.questphase / h0 / 57; sq028_02_cruiser.questphase / h0 / 48; sq028_02_cruiser.questphase / h0 / 50; +5 locations in catalogue.json | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sq028_01_phone_call.scene / scene / 17; sq028_02_welcome_aboard.scene / scene / 11; sq028_02_welcome_aboard.scene / scene / 2453; sq028_02_welcome_aboard.scene / scene / 415; +20 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | sq028_01_marina.questphase / h0 / 65; sq028_01_marina.questphase / h272 / 7; sq028_07_trashy_beach.scene / scene / 491; sq028_07_trashy_beach.scene / scene / 493; +1 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | sq028_01_marina.questphase / h0 / 107; sq028_01_phone_call.scene / scene / 147; sq028_01_phone_call.scene / scene / 149; sq028_01_phone_call.scene / scene / 253; +33 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sq028_01_marina.questphase / h0 / 70; sq028_01_marina.questphase / h0 / 72; sq028_01_marina.questphase / h0 / 74 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sq028_02_cruiser.questphase / h0 / 111; sq028_05_sex.scene / scene / 642 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sq028_05_sex.scene / scene / 592 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `journal_transition` | sq028_01_marina.questphase / h0 / 10; sq028_01_marina.questphase / h0 / 102; sq028_01_marina.questphase / h0 / 103; sq028_01_marina.questphase / h0 / 11; +43 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | sq028_03_beach.questphase / h0 / 81; sq028_03_beach.questphase / h156 / 11 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sq028_01_marina.questphase / h0 / 104; sq028_01_marina.questphase / h0 / 105; sq028_01_marina.questphase / h0 / 58; sq028_01_marina.questphase / h0 / 61; +39 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sq028_01_marina.questphase / h0 / 79; sq028_01_phone_call.scene / scene / 59; sq028_01_phone_call.scene / scene / 60; sq028_01_phone_call.scene / scene / 61; +35 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sq028_03_beach.questphase / h0 / 75; sq028_03_beach.questphase / h0 / 76; sq028_07_trashy_beach.scene / scene / 137 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sq028_01_marina.questphase / h0 / 100; sq028_01_marina.questphase / h0 / 22; sq028_01_marina.questphase / h0 / 3; sq028_02_cruiser.questphase / h0 / 21; +4 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sq028_01_marina.questphase / h0 / 75; sq028_01_marina.questphase / h0 / 77; sq028_01_marina.questphase / h0 / 95; sq028_01_marina.questphase / h0 / 97; +11 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | sq028_01_marina.questphase / h0 / 109; sq028_01_marina.questphase / h0 / 110; sq028_03_beach.questphase / h0 / 42; sq028_03_beach.questphase / h0 / 79; +4 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `weather_scope` | sq028_01_marina.questphase / h0 / 76; sq028_01_marina.questphase / h0 / 78; sq028_02_welcome_aboard.scene / scene / 2515; sq028_03_chilling_out.scene / scene / 449; +2 locations in catalogue.json | weather operation + named source + reset policy → weather request/reset dispatched. Completion follows the caller's full restoration sequence, not an early cleanup fact. |
| `workspot_performance` | sq028_02_welcome_aboard.scene / scene / 148; sq028_02_welcome_aboard.scene / scene / 150; sq028_02_welcome_aboard.scene / scene / 154; sq028_02_welcome_aboard.scene / scene / 156; +101 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sq028_01_marina.questphase / h0 / 62; sq028_01_marina.questphase / h0 / 90; sq028_01_marina.questphase / h272 / 8; sq028_02_cruiser.questphase / h0 / 104; +19 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\sidequests\sq028\sq028_quest_bugfixes.questphase` | repair; journal anchor | `base-sq028` |
| `base\quest\side_quests\sq028\phases\sq028_01_marina.questphase` | content candidate; journal anchor | `base-sq028` |
| `base\quest\side_quests\sq028\phases\sq028_02_cruiser.questphase` | content candidate; journal anchor | `base-sq028` |
| `base\quest\side_quests\sq028\phases\sq028_03_beach.questphase` | content candidate; journal anchor | `base-sq028` |
| `base\quest\side_quests\sq028\phases\sq028_fail.questphase` | content candidate; journal anchor | `base-sq028` |
| `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` | content candidate; forward dependency | `base-sq028` |
| `base\quest\side_quests\sq028\scenes\sq028_02_welcome_aboard.scene` | content candidate; journal anchor | `base-sq028` |
| `base\quest\side_quests\sq028\scenes\sq028_03_chilling_out.scene` | content candidate; forward dependency | `base-sq028` |
| `base\quest\side_quests\sq028\scenes\sq028_04_destructive_tendencies.scene` | content candidate; journal anchor | `base-sq028` |
| `base\quest\side_quests\sq028\scenes\sq028_05_sex.scene` | content candidate; journal anchor | `base-sq028` |
| `base\quest\side_quests\sq028\scenes\sq028_06_wrap_up.scene` | content candidate; journal anchor | `base-sq028` |
| `base\quest\side_quests\sq028\scenes\sq028_07_trashy_beach.scene` | content candidate; journal anchor | `base-sq028` |

Evidence shards for this dossier (including parent context): [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

629 repeated typed/socket path signatures in this selected graph context; 110 distinct direct resource identities; 5 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | `base\quest\side_quests\sq028\phases\sq028_01_marina.questphase` / h0 / 58 -> 63 -> 61 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `215ca95d939006973a7d` | `base\quest\side_quests\sq028\phases\sq028_01_marina.questphase` / h272 / 5 -> 4 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` / scene / 153 -> 147 -> 148 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `1d933adb5a617880c93e` | `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` / scene / 152 -> 154 -> 149 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` / scene / 149 -> 150 -> 2 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` / scene / 148 -> 151 -> 4 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` / scene / 28 -> 152 -> 154 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `8cd3b647ae3f592ad947` | `base\quest\side_quests\sq028\scenes\sq028_05_sex.scene` / scene / 198 -> 15 -> 2 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `9e5e28ecb38ea2a53a15` | `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` / scene / 249 -> 153 -> 147 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` / scene / 1 -> 249 -> 153 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `19665e3783f6f51a7337` | `base\quest\side_quests\sq028\scenes\sq028_03_chilling_out.scene` / scene / 244 -> 114 -> 183 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `95d4997362b664c5c23b` | `base\quest\side_quests\sq028\scenes\sq028_07_trashy_beach.scene` / scene / 13 -> 20 -> 22 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\sidequests\sq028\sq028_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\sidequests\sq028\sq028_quest_bugfixes.questphase` / h0 / 15 | `h37` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\sidequests\sq028\sq028_quest_bugfixes.questphase` / h0 / 18 | `h101` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\side_quests\sq028\phases\sq028_01_marina.questphase` / h0 / 88 | `h272` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\side_quests\sq028\phases\sq028_03_beach.questphase` / h0 / 77 | `h156` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
| `base\quest\main_quests\part1\q101\q101.gamedef` | content candidate | base\quest\main_quests\part1\q101\q101.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `base\quest\side_quests\sq021\sq021.gamedef` | content candidate | base\quest\side_quests\sq021\sq021.quest |
| `base\quest\side_quests\sq023\sq023.gamedef` | content candidate | base\quest\side_quests\sq023\sq023.quest |
| `base\quest\side_quests\sq025\sq025.gamedef` | content candidate | base\quest\side_quests\sq025\sq025.quest |
| `base\quest\side_quests\sq027\sq027_queen_of_the_highway.gamedef` | content candidate | base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest |
| `base\quest\side_quests\sq028\sq028.gamedef` | content candidate | base\quest\side_quests\sq028\sq028.quest |
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
| `base\animations\facial\generic\interactive_scene\generic_facial_additives.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\quest_custom\kerry\kerry_facial_custom_animations.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand_stairs__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__lie_ground_lean180__lh_on_knee__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean180__arms_legs_crossed__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__lh_cigarette__aggressive__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_wall_lean180__lh_pocket__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\female\body\player_locomotion_johnny_guitar.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__stand_rail_lean270__lh_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand_rail_lean270__lh_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\male\body\player_locomotion_sick.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q112\q112_00b_secret_meeting\body\q112_00b_secret_meeting__player_female_sit_rail.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q112\q112_00b_secret_meeting\body\q112_00b_secret_meeting__player_sit_rail.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q112\q112_04_takemura\body\q112_04_takemura__ma_johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q115\q115_00_johnny\body\q115_00_johnny__ma_johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_02_welcome_aboard\body\sq028_02_welcome_aboard__ma_kerry.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_02_welcome_aboard\body\sq028_02_welcome_aboard__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_02_welcome_aboard\sq028_02_welcome_aboard__offset_position.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\body\sq028_04_destructive_tendencies__bar_stool.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\body\sq028_04_destructive_tendencies__bottles.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\body\sq028_04_destructive_tendencies__ma_kerry.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\body\sq028_04_destructive_tendencies__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\body\sq028_04_destructive_tendencies__yacht.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\rid\sq028_04_destructive_tendencies_jp.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\rid\sq028_04_destructive_tendencies_new_camera_edit.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\synced\synced__breaking_flag__01__kerry.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\synced\synced__breaking_flag__01__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\synced\synced__breaking_flag__01__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\synced\synced__player_destroys_painting__01__painting.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_04_destructive_tendencies\synced\synced__sq028_destructive__cofee_machine.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_06_wrap_up\body\sq028_06_wrap_up__ma_kerry.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_06_wrap_up\body\sq028_06_wrap_up__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_06_wrap_up\synced\synced__sq028_06_wrap_up__kerry.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_06_wrap_up\synced\synced__sq028_06_wrap_up__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_06_wrap_up\synced\synced__sq028_06_wrap_up__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_06_wrap_up\synced\synced__sq028_06_wrap_up__record_player_a.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_07_trashy_beach\body\sq028_07_trashy_beach__boat.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_07_trashy_beach\body\sq028_07_trashy_beach__ma_kerry.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_07_trashy_beach\body\sq028_07_trashy_beach__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_07_trashy_beach\body\sq028_07_trashy_beach__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_07_trashy_beach\synced\sq028_07_trashy_beach__kerry.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq028\sq028_07_trashy_beach\synced\sq028_07_trashy_beach__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\characters\base_entities\man_base\man_base.rig` | asset binding .rig | content/basegame_1_engine.archive; content/basegame_4_appearance.archive; index evidence only |
| `base\fx\quest\sq028\sq028_underewater_fx.effect` | asset binding .effect | content/basegame_4_gamedata.archive; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_01_phone_call\kerry.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_01_phone_call\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_02_welcome_aboard\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_02_welcome_aboard\kerry.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_02_welcome_aboard\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_03_chilling_out\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_03_chilling_out\kerry.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_03_chilling_out\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_04_destructive_tendencies\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_04_destructive_tendencies\kerry.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_04_destructive_tendencies\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_05_sex\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_05_sex\kerry.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_05_sex\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_06_wrap_up\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_06_wrap_up\kerry.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_06_wrap_up\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_07_trashy_beach\kerry.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\lipsync\en\sq028_07_trashy_beach\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq028\scenes\sq028_02_welcome_aboard.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq028\scenes\sq028_03_chilling_out.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq028\scenes\sq028_04_destructive_tendencies.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq028\scenes\sq028_05_sex.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq028\scenes\sq028_06_wrap_up.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq028\scenes\sq028_07_trashy_beach.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\archetype\dirtboy\dirt__stand_stairs__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\big__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_bar__pull_up__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_left__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\ground\johnny__walk_ground_cigarette__aggressive__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__lie_car_lean_back__lie_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_back__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_wall_lean_back__think__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\kerry\bar\kerry__stand_bar_lean_front__breaking__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\main_characters\kerry\bar\kerry__stand_ground__aggressive__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\kerry\bar\kerry__stand_ground_cigarette__hold__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\main_characters\kerry\bar\kerry__stand_ground_flag__breaking__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\kerry\couch\kerry__sit_couch_lean_back_guitar__hold__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\kerry\couch\kerry__sit_couch_lean_back_guitar__hold__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\main_characters\kerry\couch\kerry__sit_couch_lean_back_guitar__hold__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\kerry\couch\kerry__sit_couch_lean_back_guitar__hold__04.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\kerry\ground\kerry__sit_beach_lean_back__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\main_characters\kerry\stairs\kerry__stand_stairs_lean_front__wait__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\bar\player__sit_rail__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\player\couch\player__sit_couch__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\player\ground\player__sit_beach_lean_front__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\player\ground\player__stand_beach_cigarette__hold__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q112\q112_04_takemura\q112__johnny__lie_ledge__lie_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q115\q115_00_johnny\q115__johnny__stand_cigarette__hold__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\side_quests\sq028\sq028_02_welcome_aboard\kerry__sit_couch_lean180__2h_guitar__01__play_guitar.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq028\sq028_04_destructive_tendencies\sq028__kerry__stand_ground_flag__breaking__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq028\sq028_04_destructive_tendencies\sq028__player__sit_couch_lean0__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq028\sq028_04_destructive_tendencies\sq028__player__stand_ground_flag__breaking__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq028\sq028_07_trashy_beach\sq028__kerry__swim_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\synced\lore\lore_ganger_gang_hostilities_01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `censorship_homosexuality` | base\quest\side_quests\sq017\test\sq017_chicken_test.scene / scene / 55; base\quest\side_quests\sq026\definitions\sq026_chicken_test.scene / scene / 468; base\quest\side_quests\sq030\definitions\sq030_chicken_test.scene / scene / 155; 3 total source locations in compressed evidence |
| `censorship_oversexualized` | base\quest\side_quests\sq030\definitions\sq030_chicken_test.scene / scene / 277; 1 total source locations in compressed evidence |
| `ep1_active` | base\quest\main_quests\part1\q110\q110b.questphase / h0 / 289; base\quest\bugfixing.questphase / h309 / 3; base\quest\test\cp77_chicken_test.scene / scene / 2067; ep1\quest\minor_quests\mq301\phases\mq301_00_debug.questphase / h0 / 25; 33 total source locations in compressed evidence |
| `holo_kerry_calls_v_end_activate` | base\quest\holocalls\kerry\kerry_holocall.questphase / h0 / 11; base\quest\side_quests\sq017\phases\sq017_01a_truck_meeting.questphase / h0 / 90; base\quest\side_quests\sq017\phases\sq017_02a_club_outside.questphase / h602 / 43; base\quest\side_quests\sq017\phases\sq017_03a_premiere_pachinko.questphase / h0 / 49; 7 total source locations in compressed evidence |
| `holo_kerry_calls_v_end_done` | base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 149; base\quest\holocalls\kerry\kerry_holocall.scene / scene / 42; base\quest\holocalls\kerry\kerry_holocall.scene / scene / 551; base\quest\side_quests\sq017\scenes\sq017_01_phone_call_1.scene / scene / 402; 6 total source locations in compressed evidence |
| `holo_kerry_calls_v_rejectable` | base\quest\holocalls\kerry\kerry_holocall.scene / scene / 618; base\quest\side_quests\sq017\scenes\sq017_01_phone_call_1.scene / scene / 438; base\quest\side_quests\sq017\scenes\sq017_07_phone_call_2.scene / scene / 436; base\quest\side_quests\sq017\scenes\sq017_16_phone_call_3.scene / scene / 259; 4 total source locations in compressed evidence |
| `holo_kerry_calls_v_rejected` | base\quest\holocalls\kerry\kerry_holocall.scene / scene / 626; base\quest\side_quests\sq017\scenes\sq017_01_phone_call_1.scene / scene / 440; base\quest\side_quests\sq017\scenes\sq017_07_phone_call_2.scene / scene / 438; base\quest\side_quests\sq017\scenes\sq017_16_phone_call_3.scene / scene / 261; 4 total source locations in compressed evidence |
| `holo_kerry_calls_v_start_activate` | base\quest\holocalls\kerry\kerry_holocall.questphase / h0 / 10; base\quest\side_quests\sq017\phases\sq017_01a_truck_meeting.questphase / h0 / 89; base\quest\side_quests\sq017\phases\sq017_02a_club_outside.questphase / h602 / 42; base\quest\side_quests\sq017\phases\sq017_03a_premiere_pachinko.questphase / h0 / 48; 7 total source locations in compressed evidence |
| `holo_kerry_calls_v_start_done` | base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 148; base\quest\holocalls\kerry\kerry_holocall.scene / scene / 41; base\quest\holocalls\kerry\kerry_holocall.scene / scene / 576; base\quest\side_quests\sq017\scenes\sq017_01_phone_call_1.scene / scene / 400; 6 total source locations in compressed evidence |
| `kerry_default_on` | base\quest\minor_quests\mq055\phases\mq055_apartment.questphase / h0 / 35; base\quest\minor_quests\mq055\phases\mq055_apartment.questphase / h0 / 46; base\quest\minor_quests\mq055\phases\mq055_message_kerry.questphase / h0 / 14; base\quest\minor_quests\mq055\phases\mq055_message_kerry.questphase / h0 / 21; 40 total source locations in compressed evidence |
| `kerry_romanceable` | base\quest\side_quests\sq017\test\sq017_chicken_test.scene / scene / 61; base\quest\side_quests\sq028\test\sq028_chicken_test.scene / scene / 33; 2 total source locations in compressed evidence |
| `sq017_kerry_kiss` | base\quest\side_quests\sq017\scenes\sq017_18_premiere.scene / scene / 208; base\quest\side_quests\sq028\test\sq028_chicken_test.scene / scene / 17; 2 total source locations in compressed evidence |
| `sq028_active` | base\quest\side_quests\sq028\phases\sq028_cleanup.questphase / h0 / 3; base\quest\side_quests\sq028\phases\sq028_cleanup.questphase / h0 / 15; 2 total source locations in compressed evidence |
| `sq028_kerry_dislike` | base\quest\main_quests\epilogue\q201\scenes\q201_00_chicken_test.scene / scene / 42; 1 total source locations in compressed evidence |
| `sq028_kerry_friend` | base\quest\side_quests\sq028\test\sq028_chicken_test.scene / scene / 42; 1 total source locations in compressed evidence |
| `sq028_kerry_relationship` | base\quest\minor_quests\mq055\test\mq055_chicken.scene / scene / 13; base\quest\minor_quests\mq055\test\mq055_chicken.scene / scene / 16; base\quest\minor_quests\mq055\test\mq055_chicken.scene / scene / 88; base\quest\minor_quests\mq055\test\mq055_chicken.scene / scene / 137; 13 total source locations in compressed evidence |
| `sq028_kerry_sex` | base\quest\side_quests\sq028\test\sq028_chicken_test.scene / scene / 28; ep1\quest\main_quests\q306\test\q306_00_chickentest.scene / scene / 1141; 2 total source locations in compressed evidence |
| `urge` | base\quest\main_quests\part1\q112\scenes\q112_00b_secret_meeting.scene / scene / 3518; base\quest\main_quests\part1\q112\scenes\q112_00b_secret_meeting.scene / scene / 3520; base\quest\main_quests\part1\q112\scenes\q112_00b_secret_meeting.scene / scene / 3521; base\quest\main_quests\part1\q112\scenes\q112_01_market.scene / scene / 1981; 38 total source locations in compressed evidence |

NodeRef uses: 559; TweakDB binding uses: 179. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\side_quests\sq028\scenes\sq028_01_phone_call.scene` | 4 / 17 | scnChangeIdleAnimEvent: 2; scnDialogLineEvent: 8; scnLookAtEvent: 2; scnPlaySkAnimEvent: 3; scneventsSocket: 2 |
| `base\quest\side_quests\sq028\scenes\sq028_02_welcome_aboard.scene` | 28 / 173 | scnAudioEvent: 6; scnChangeIdleAnimEvent: 3; scnDialogLineEvent: 29; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 23; scnPlaySkAnimEvent: 55; scnUnmountEvent: 1; scneventsAttachPropToPerformer: 2; scneventsAttachPropToWorld: 3; scneventsCameraParamsEvent: 1; scneventsSetAnimFeatureEvent: 4; scneventsSocket: 41; scneventsVFXEvent: 2 |
| `base\quest\side_quests\sq028\scenes\sq028_03_chilling_out.scene` | 22 / 221 | scnAudioEvent: 14; scnChangeIdleAnimEvent: 12; scnDialogLineEvent: 47; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 58; scnPlaySkAnimEvent: 53; scnUnmountEvent: 1; scneventsAttachPropToPerformer: 1; scneventsCameraParamsEvent: 2; scneventsSetAnimFeatureEvent: 5; scneventsSocket: 25 |
| `base\quest\side_quests\sq028\scenes\sq028_04_destructive_tendencies.scene` | 29 / 177 | scnAudioEvent: 7; scnChangeIdleAnimEvent: 21; scnDialogLineEvent: 25; scnGameplayTransitionEvent: 3; scnIKEvent: 6; scnLookAtEvent: 17; scnPlaySkAnimEvent: 30; scnUnmountEvent: 3; scneventsAttachPropToPerformer: 3; scneventsAttachPropToWorld: 3; scneventsCameraParamsEvent: 7; scneventsSetAnimFeatureEvent: 10; scneventsSocket: 31; scneventsVFXEvent: 11 |
| `base\quest\side_quests\sq028\scenes\sq028_05_sex.scene` | 10 / 296 | scnAudioEvent: 22; scnChangeIdleAnimEvent: 7; scnDialogLineEvent: 7; scnGameplayTransitionEvent: 4; scnIKEvent: 8; scnLookAtEvent: 13; scnPlayRidAnimEvent: 24; scnPlaySkAnimEvent: 87; scnUnmountEvent: 4; scneventsAttachPropToPerformer: 1; scneventsAttachPropToWorld: 2; scneventsCameraParamsEvent: 6; scneventsPlayRidCameraAnimEvent: 22; scneventsSetAnimFeatureEvent: 4; scneventsSocket: 55; scneventsVFXEvent: 30 |
| `base\quest\side_quests\sq028\scenes\sq028_06_wrap_up.scene` | 12 / 82 | scnAudioEvent: 4; scnChangeIdleAnimEvent: 1; scnDialogLineEvent: 12; scnGameplayTransitionEvent: 3; scnIKEvent: 6; scnLookAtEvent: 8; scnPlaySkAnimEvent: 9; scnUnmountEvent: 3; scneventsAttachPropToPerformer: 5; scneventsAttachPropToWorld: 3; scneventsCameraParamsEvent: 2; scneventsSetAnimFeatureEvent: 3; scneventsSocket: 19; scneventsVFXEvent: 4 |
| `base\quest\side_quests\sq028\scenes\sq028_07_trashy_beach.scene` | 26 / 203 | scnAudioEvent: 6; scnChangeIdleAnimEvent: 15; scnDialogLineEvent: 51; scnGameplayTransitionEvent: 4; scnIKEvent: 8; scnLookAtEvent: 46; scnPlaySkAnimEvent: 26; scnUnmountEvent: 4; scneventsCameraParamsEvent: 4; scneventsSetAnimFeatureEvent: 4; scneventsSocket: 34; scneventsVFXEvent: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
