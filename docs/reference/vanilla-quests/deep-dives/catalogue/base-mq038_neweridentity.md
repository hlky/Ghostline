# Big in Japan

Journal: `quests/minor_quest/mq038_neweridentity` · `MinorQuest` · hash `1453594350`.

**Coverage: journal-linked.** 39 exact journal-linked nodes in 4 resources; 6 resources in the inspected dependency context.

Resource roles in that context: 5 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Find the package, and deliver it from A to B. Simple job, huh? But then why not just book some delivery guy? And why not go through a fixer? Something smells off about this one, V. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/01_fishing_village` |
| Find and open the container with "No Future" graffiti'd on it. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02_find_dumpster` |
| Talk to Dennis. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02b_call_darryl` |
| Pick up the body. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body` |
| Carry the body to the car. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/04_deliver_to_car` |
| Put the body in the trunk. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/05_hide_trunk` |
| Deliver the body to the specified coordinates. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside` |
| Get in Dennis' car. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_enter_car` |
| Talk to Dennis. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/08_talk_cargo` |
| Leave the car. (Primary) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/09_leave_car` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq038_quest_bugfixes.questphase / h7 / 9` (PauseCondition) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside` | 2:Out → 9:In; 9:Out → 10:In |
| `mq038_quest_bugfixes.questphase / h53 / 5` (PauseCondition) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside` | 3:Out → 5:In; 5:Out → 6:In |
| `mq038_quest_bugfixes.questphase / h53 / 7` (PauseCondition) | `quests/minor_quest/mq038_neweridentity` | 3:Out → 7:In; 7:Out → 6:In |
| `mq038_quest_bugfixes.questphase / h121 / 7` (Condition) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/01_fishing_village/mq038_description` | 7:False → 1:In; 14:False → 7:In; 7:True → 10:In |
| `mq038_quest_bugfixes.questphase / h121 / 10` (Condition) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body` | 7:True → 10:In; 10:False → 9:In; 10:True → 11:In2 |
| `mq038_ending.questphase / h0 / 2` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside` | 0:Out → 2:Succeeded; 2:Out → 39:Active |
| `mq038_ending.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/08_talk_cargo` | 33:Out → 8:Succeeded; 8:Out → 12:Succeeded |
| `mq038_ending.questphase / h0 / 12` (Journal) | `quests/minor_quest/mq038_neweridentity` | 8:Out → 12:Succeeded; 12:Out → 16:In |
| `mq038_ending.questphase / h0 / 39` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/09_leave_car` | 2:Out → 39:Active; 39:Out → 21:In; 39:Out → 61:In |
| `mq038_village.questphase / h0 / 12` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/01_fishing_village` | 3:Out → 12:Active; 12:Out → 89:Active |
| `mq038_village.questphase / h0 / 14` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/01_fishing_village` | 70:Out → 14:Succeeded; 14:Out → 15:Active |
| `mq038_village.questphase / h0 / 15` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02_find_dumpster` | 15:Out → 6:In; 14:Out → 15:Active; 15:Out → 110:In; 15:Out → 111:In |
| `mq038_village.questphase / h0 / 17` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body` | 75:Out → 17:Active; 17:Out → 81:In |
| `mq038_village.questphase / h0 / 19` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body` | 199:Out → 19:Succeeded; 19:Out → 71:In1; 19:Out → 203:In |
| `mq038_village.questphase / h0 / 20` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/04_deliver_to_car` | 29:Out → 20:Active; 20:Out → 33:In |
| `mq038_village.questphase / h0 / 34` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/04_deliver_to_car` | 82:Out → 34:Succeeded; 34:Out → 35:Active |
| `mq038_village.questphase / h0 / 35` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/05_hide_trunk` | 34:Out → 35:Active; 35:Out → 36:In |
| `mq038_village.questphase / h0 / 38` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/05_hide_trunk` | 151:Out → 38:Succeeded; 38:Out → 80:Inactive |
| `mq038_village.questphase / h0 / 44` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_enter_car` | 80:Out → 44:Active; 51:Out → 44:Active; 44:Out → 45:In |
| `mq038_village.questphase / h0 / 49` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_enter_car` | 179:Out → 49:Succeeded; 49:Out → 50:Active |
| `mq038_village.questphase / h0 / 50` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside` | 50:Out → 48:In; 49:Out → 50:Active; 50:Out → 175:In |
| `mq038_village.questphase / h0 / 51` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside` | 51:Out → 44:Active; 182:Out → 51:Inactive |
| `mq038_village.questphase / h0 / 75` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02b_call_darryl` | 75:Out → 17:Active; 129:Out → 75:Succeeded |
| `mq038_village.questphase / h0 / 80` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body` | 38:Out → 80:Inactive; 80:Out → 44:Active |
| `mq038_village.questphase / h0 / 89` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/01_fishing_village/mq038_description` | 12:Out → 89:Active; 89:Out → 13:In |
| `mq038_village.questphase / h0 / 131` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02_find_dumpster` | 76:body_seen_out → 131:Succeeded; 131:Out → 132:Active; 131:Out → 170:In |
| `mq038_village.questphase / h0 / 132` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02b_call_darryl` | 131:Out → 132:Active; 132:Out → 159:Active; 132:Out → 139:call |
| `mq038_village.questphase / h0 / 43` (Journal) | `quests/minor_quest/mq038_neweridentity` | 157:Out → 43:Failed; 43:Out → 2:In |
| `mq038_village.questphase / h0 / 159` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02b_call_darryl/contact` | 132:Out → 159:Active |
| `mq038_village.questphase / h494 / 4` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body` | 3:Out → 4:Succeeded; 4:Out → 13:In |
| `mq038_village.questphase / h494 / 5` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body` | 5:Out → 3:In; 9:False → 5:Active; 12:Out → 5:Active |
| `mq038_village.questphase / h494 / 6` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/04_deliver_to_car` | 7:True → 6:Inactive; 6:Out → 11:In |
| `mq038_village.questphase / h494 / 7` (Condition) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/04_deliver_to_car` | 2:Out → 7:In; 7:True → 6:Inactive; 7:False → 9:In |
| `mq038_village.questphase / h494 / 8` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/05_hide_trunk` | 9:True → 8:Inactive; 8:Out → 12:In |
| `mq038_village.questphase / h494 / 9` (Condition) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/05_hide_trunk` | 9:False → 5:Active; 7:False → 9:In; 9:True → 8:Inactive; 11:Out → 9:In |
| `mq038_village.questphase / h494 / 15` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/04_deliver_to_car` | 13:True → 15:Active; 15:Out → 18:In |
| `mq038_village.questphase / h494 / 16` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/05_hide_trunk` | 14:True → 16:Active; 16:Out → 19:In |
| `mq038_02_ending.scene / scene / 143` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/08_talk_cargo` | 144:0:0 → 143:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq038_02_ending.scene / scene / 144` (Journal) | `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/09_leave_car` | 144:0:0 → 143:0:1; 145:0:0 → 144:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq038_ending.questphase / h0 / 7` | `base\quest\minor_quests\mq038\scenes\mq038_02_ending.scene`; `#mq038_02_sm_ending` | 37:Out → 7:Start 0; 7:End 0 → 33:In |
| `mq038_ending.questphase / h0 / 18` | `base\quest\minor_quests\mq038\scenes\mq038_02_ending.scene`; `#mq038_02_sm_ending` | 51:CutSource → 18:CutDestination; 19:Out → 18:talk_loop; 41:Out → 18:talk_loop; 18:talk_loop_out → 19:In |
| `mq038_tyger_combat.questphase / h0 / 11` | `base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene`; `#mq038_01b_sm_fisher_village` | 3:Out → 11:combat_01; 5:Out → 11:combat_02; 7:Out → 11:combat_03; 9:Out → 11:combat_04 |
| `mq038_village.questphase / h0 / 71` | `base\quest\minor_quests\mq038\phases\mq038_tyger_combat.questphase` | 19:Out → 71:In1 |
| `mq038_village.questphase / h0 / 76` | `base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene`; `#mq038_01b_sm_fisher_village` | 90:Out → 76:body_seen; 76:body_seen_out → 131:Succeeded; 76:body_seen_out_cut → 210:In |
| `mq038_village.questphase / h0 / 139` | `base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene`; `#mq038_01b_sm_fisher_village` | 139:call_out → 129:In; 132:Out → 139:call; 139:call_out_cut → 211:In; 139:call_out → 167:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\mq038\mq038.questphase` / h0 / 99 | `mq038_ending.questphase` | 97: Phase: mq038_village.questphase; 109: Input; 97:Out1 → 99:In1; 99:Out1 → 104:In; 109:Out → 99:In1 |
| `base\quest\minor_quests\mq038\phases\mq038_village.questphase` / h0 / 71 | `mq038_tyger_combat.questphase` | 19: Journal; 19:Out → 71:In1 |
| `base\quest\minor_quests\mq038\mq038.questphase` / h0 / 97 | `mq038_village.questphase` | 96: Phase: mq038_briefing.questphase; 112: Input; 96:Out1 → 97:In1; 112:Out → 97:In1; 97:Out1 → 99:In1; 97:quest_ends → 116:In1 |
| `base\quest\minor_quests\mq038\phases\mq038_tyger_combat.questphase` / h0 / 11 | `mq038_01b_fisher_village.scene` | 3: PauseCondition; 5: PauseCondition; 7: PauseCondition; 9: PauseCondition; 3:Out → 11:combat_01; 5:Out → 11:combat_02; 7:Out → 11:combat_03; 9:Out → 11:combat_04 |
| `base\quest\minor_quests\mq038\phases\mq038_village.questphase` / h0 / 76 | `mq038_01b_fisher_village.scene` | 90: PauseCondition: {"seconds": 3}; 90:Out → 76:body_seen; 76:body_seen_out → 131:Succeeded; 76:body_seen_out_cut → 210:In |
| `base\quest\minor_quests\mq038\phases\mq038_village.questphase` / h0 / 139 | `mq038_01b_fisher_village.scene` | 132: Journal; 139:call_out → 129:In; 132:Out → 139:call; 139:call_out_cut → 211:In; 139:call_out → 167:In |
| `base\quest\minor_quests\mq038\phases\mq038_ending.questphase` / h0 / 7 | `mq038_02_ending.scene` | 37: Vehicle; 37:Out → 7:Start 0; 7:End 0 → 33:In |
| `base\quest\minor_quests\mq038\phases\mq038_ending.questphase` / h0 / 18 | `mq038_02_ending.scene` | 51: CutControl; 19: PauseCondition: {"seconds": 1}; 41: PauseCondition; 51:CutSource → 18:CutDestination; 19:Out → 18:talk_loop; 41:Out → 18:talk_loop; 18:talk_loop_out → 19:In |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 11 | `mq038.questphase` | 70: LogicalHub; 70:Out1 → 11:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq038_01b_fisher_village.scene` | body_seen, mq038_surgeon_facial, combat_01, combat_02, combat_03, combat_04, call → body_seen_out, End1, combat_01_out, combat_02_out, combat_03_out, combat_04_out, body_seen_out_cut, call_out_cut, call_out | Tyger_claw_01; Tyger_claw_02; Tyger_claw_03; Tyger_claw_04; Denis; Surgeon; Player; 42 nodes / 38 edges |
| `mq038_02_ending.scene` | Start 0, talk_loop → End 0, talk_loop_out | Surgeon; Darryl; Player; 46 nodes / 47 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq038_01b_fisher_village.scene / n44 / 0` | I did. (``) | No option-level predicate stored | 0:0 → 46:0:0 |
| `mq038_01b_fisher_village.scene / n44 / 1` | Could've told me this "package" is a person. (``) | No option-level predicate stored | 0:1 → 48:0:0 |
| `mq038_02_ending.scene / n6 / 0` | Job's done. (``) | No option-level predicate stored | 0:0 → 8:0:0; 0:0 → 93:0:1 |
| `mq038_02_ending.scene / n28 / 0` | What's your name? (``) | No option-level predicate stored | 0:0 → 30:0:0 |
| `mq038_02_ending.scene / n28 / 1` | Where are you from? (``) | No option-level predicate stored | 0:1 → 31:0:0 |
| `mq038_02_ending.scene / n38 / 0` | My payment. (``) | No option-level predicate stored | 0:0 → 11:0:0 |
| `mq038_02_ending.scene / n38 / 1` | Who is this guy? (``) | No option-level predicate stored | 0:1 → 129:0:1 |
| `mq038_02_ending.scene / n38 / 2` | Early warning about the Tygers would've been nice. (``) | No option-level predicate stored | 0:2 → 132:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CYB-590220` | mq038_quest_bugfixes.questphase / h7 / 2 | mq038_quest_bugfixes.questphase / h7 / 8 |
| `CYB-632793` | mq038_quest_bugfixes.questphase / h121 / 2 | mq038_quest_bugfixes.questphase / h121 / 3 |
| `CYB-634740` | mq038_quest_bugfixes.questphase / h53 / 3 | mq038_quest_bugfixes.questphase / h53 / 2 |
| `holo_dennis_calls_v_end_activate` | mq038_01b_fisher_village.scene / scene / 144; mq038_01b_fisher_village.scene / scene / 272 | No reader in selected context |
| `holo_dennis_calls_v_end_done` | mq038_01b_fisher_village.scene / scene / 140; mq038_01b_fisher_village.scene / scene / 270 | mq038_01b_fisher_village.scene / scene / 139; mq038_01b_fisher_village.scene / scene / 268 |
| `holo_dennis_calls_v_start_activate` | mq038_01b_fisher_village.scene / scene / 143 | No reader in selected context |
| `holo_dennis_calls_v_start_done` | mq038_01b_fisher_village.scene / scene / 138 | mq038_01b_fisher_village.scene / scene / 137 |
| `holo_interrupt_call_manual` | mq038_village.questphase / h0 / 167; mq038_village.questphase / h0 / 168; mq038_village.questphase / h0 / 212 | No reader in selected context |
| `mq038_deliver_inactive` | mq038_village.questphase / h494 / 11; mq038_village.questphase / h494 / 18 | mq038_village.questphase / h494 / 13 |
| `mq038_done` | Producer outside selected context | mq038_quest_bugfixes.questphase / h121 / 14 |
| `mq038_dumpster_opened` | Producer outside selected context | mq038_village.questphase / h0 / 6 |
| `mq038_fake_01_opened` | Producer outside selected context | mq038_village.questphase / h0 / 110 |
| `mq038_fake_02_opened` | Producer outside selected context | mq038_village.questphase / h0 / 111 |
| `mq038_hide_inactive` | mq038_village.questphase / h494 / 12; mq038_village.questphase / h494 / 19 | mq038_village.questphase / h494 / 14 |
| `travelling_merchant_lives` | Producer outside selected context | mq038_quest_bugfixes.questphase / h0 / 15 |

## Exact gates, joins and cancellation

<details><summary>75 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq038_quest_bugfixes.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 16:Out → 15:In |
| `mq038_quest_bugfixes.questphase / h7 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-590220"}}}` | 0:Out → 8:In; 8:False → 2:In |
| `mq038_quest_bugfixes.questphase / h7 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 9:In; 9:Out → 10:In |
| `mq038_quest_bugfixes.questphase / h53 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-634740"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq038_quest_bugfixes.questphase / h53 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 3:Out → 5:In; 5:Out → 6:In |
| `mq038_quest_bugfixes.questphase / h53 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq038_neweridentity","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Failed"}}}` | 3:Out → 7:In; 7:Out → 6:In |
| `mq038_quest_bugfixes.questphase / h121 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-632793"}}}` | 0:Out → 3:In; 3:False → 2:In; 3:True → 12:In1 |
| `mq038_quest_bugfixes.questphase / h121 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq038_neweridentity/mq038_neweridentity/01_fishing_village/mq038_description","fileEntryIndex":2,"className":"gameJournalQuestDescription"},"state":"Active"}}}` | 7:False → 1:In; 14:False → 7:In; 7:True → 10:In |
| `mq038_quest_bugfixes.questphase / h121 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 7:True → 10:In; 10:False → 9:In; 10:True → 11:In2 |
| `mq038_quest_bugfixes.questphase / h121 / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq038_done"}}}` | 2:Out → 14:In; 14:False → 7:In; 14:True → 15:In1 |
| `mq038_ending.questphase / h0 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 19:Out → 18:talk_loop; 18:talk_loop_out → 19:In; 51:CutSource → 19:CutDestination |
| `mq038_ending.questphase / h0 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"119335728359","comparisonType":"Greater"}}}` | 41:Out → 18:talk_loop; 16:Out → 41:In; 51:CutSource → 41:CutDestination |
| `mq038_ending.questphase / h0 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":15.0}}}}` | 60:Out → 44:In; 44:Out → 46:In; 44:Out → 47:In; 44:Out → 51:In |
| `mq038_ending.questphase / h0 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"childRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"},"enterAnimationFinished":true}}}` | 46:Out → 48:In; 48:Out → 50:In1 |
| `mq038_ending.questphase / h0 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"childRef":{"$type":"gameEntityReference","reference":"#mq038_com_darryl"},"enterAnimationFinished":true}}}` | 47:Out → 49:In; 49:Out → 50:In2 |
| `mq038_ending.questphase / h0 / 50` | `questLogicalAndNodeDefinition` `{}` | 48:Out → 50:In1; 49:Out → 50:In2; 50:Out1 → 53:In; 50:Out1 → 63:In |
| `mq038_ending.questphase / h0 / 51` | `questCutControlNodeDefinition` `{}` | 51:CutSource → 18:CutDestination; 51:CutSource → 19:CutDestination; 51:CutSource → 41:CutDestination; 44:Out → 51:In; 51:Out → 59:In; 51:CutSource → 55:CutDestination; 51:CutSource → 57:CutDestination |
| `mq038_ending.questphase / h0 / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq038_com_darryl"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0}}}}` | 54:Out → 1:In; 53:Out → 54:In |
| `mq038_ending.questphase / h0 / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq038_tr_delivery_point","activatorRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"}}}` | 0:Out → 55:In; 51:CutSource → 55:CutDestination; 58:Out → 55:In; 55:Out → 56:In |
| `mq038_ending.questphase / h0 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq038_tr_delivery_point","activatorRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"}}}` | 51:CutSource → 57:CutDestination; 56:Out → 57:In; 57:Out → 58:In |
| `mq038_tyger_combat.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_tyger"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 1:Out → 2:In; 2:Out → 3:In; 2:Out → 5:In; 2:Out → 7:In; 2:Out → 9:In; 2:Out → 12:In |
| `mq038_tyger_combat.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_tyger","names":["tyg_01"]},"isPlayer":false}}}` | 2:Out → 3:In; 3:Out → 11:combat_01 |
| `mq038_tyger_combat.questphase / h0 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_tyger","names":["tyg_02"]},"isPlayer":false}}}` | 2:Out → 5:In; 5:Out → 11:combat_02 |
| `mq038_tyger_combat.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_tyger","names":["tyg_03"]},"isPlayer":false}}}` | 2:Out → 7:In; 7:Out → 11:combat_03 |
| `mq038_tyger_combat.questphase / h0 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_tyger","names":["tyg_04"]},"isPlayer":false}}}` | 2:Out → 9:In; 9:Out → 11:combat_04 |
| `mq038_tyger_combat.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq03_tr_enemy_005"}}` | 2:Out → 12:In; 12:Out → 13:In |
| `mq038_tyger_combat.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Exited","triggerAreaRef":"#mq038_tr_favelas_entered"}}` | 14:Out → 15:In; 19:CutSource → 15:CutDestination; 15:Out → 17:In |
| `mq038_tyger_combat.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Entered","triggerAreaRef":"#mq038_tr_favelas_entered"}}` | 16:Out → 14:In; 19:CutSource → 16:CutDestination; 27:Out → 16:In |
| `mq038_tyger_combat.questphase / h0 / 19` | `questCutControlNodeDefinition` `{}` | 19:CutSource → 15:CutDestination; 19:CutSource → 16:CutDestination; 22:Out → 19:In; 19:Out → 26:In |
| `mq038_tyger_combat.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_tyger"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 23:Out → 20:In; 20:Out → 28:In |
| `mq038_tyger_combat.questphase / h0 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleTrunk_ConditionType","playerVehicle":false,"vehicleRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"}}}}` | 22:Out → 19:In; 23:Out → 22:In |
| `mq038_tyger_combat.questphase / h0 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq038_tr_favelas_entered"}}` | 20:Out → 28:In; 28:True → 24:In; 28:False → 29:In |
| `mq038_tyger_combat.questphase / h0 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq038_tr_favelas_entered"}}` | 29:Out → 24:In; 28:False → 29:In |
| `mq038_village.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq038_dumpster_opened"}}}` | 15:Out → 6:In; 6:Out → 109:In; 6:Out → 128:In; 6:Out → 161:In |
| `mq038_village.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq038_tr_favelas_entered"}}` | 89:Out → 13:In; 13:Out → 70:In |
| `mq038_village.questphase / h0 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 29:Out → 32:In; 32:Out → 91:In |
| `mq038_village.questphase / h0 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq038_tr_car_approached","activatorRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"},"isPlayerActivator":false}}` | 20:Out → 33:In; 33:Out → 82:In |
| `mq038_village.questphase / h0 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleTrunk_ConditionType","playerVehicle":false,"vehicleRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"}}}}` | 35:Out → 36:In; 36:Out → 103:In; 36:Out → 118:In; 36:Out → 151:In |
| `mq038_village.questphase / h0 / 42` | `questLogicalXorNodeDefinition` `{"inputSocketCount":5}` | 196:Out1 → 42:In1; 156:Out → 42:In2; 204:Out → 42:In3; 103:Out → 42:In4; 216:Out1 → 42:In5; 42:Out1 → 198:In |
| `mq038_village.questphase / h0 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"childIsPlayer":true}}}` | 44:Out → 45:In; 45:Out → 179:In |
| `mq038_village.questphase / h0 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"childIsPlayer":true,"condition":"OnUnmount"}}}` | 50:Out → 48:In; 48:Out → 182:In |
| `mq038_village.questphase / h0 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq038_tr_delivery_point","activatorRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"isPlayerActivator":false}}` | 79:Out → 61:In; 61:Out → 184:In |
| `mq038_village.questphase / h0 / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_darryl"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 79:Out → 61:In; 78:Out → 79:In |
| `mq038_village.questphase / h0 / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 90:Out → 76:body_seen; 109:Out → 90:In |
| `mq038_village.questphase / h0 / 100` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 102:Out → 100:In; 100:Out → 101:In |
| `mq038_village.questphase / h0 / 102` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 102:Out → 95:In; 102:Out → 99:In; 102:Out → 100:In; 128:Out → 102:In; 102:Out → 146:In |
| `mq038_village.questphase / h0 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq038_com_car"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":1000.0}}}}` | 36:Out → 103:In; 103:Out → 42:In4 |
| `mq038_village.questphase / h0 / 110` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq038_fake_01_opened"}}}` | 15:Out → 110:In; 110:Out → 108:In |
| `mq038_village.questphase / h0 / 111` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq038_fake_02_opened"}}}` | 15:Out → 111:In; 111:Out → 107:In |
| `mq038_village.questphase / h0 / 163` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3:Out → 163:In; 163:Out → 162:In |
| `mq038_village.questphase / h0 / 192` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 192:Out → 153:In; 193:Out → 192:In |
| `mq038_village.questphase / h0 / 194` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":190.0}}}}` | 193:Out → 194:In; 201:Out1 → 194:In; 194:Out → 196:In1 |
| `mq038_village.questphase / h0 / 198` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType","isContentBlocked":true}}}` | 42:Out1 → 198:In; 198:False → 119:In; 198:True → 150:In |
| `mq038_village.questphase / h0 / 199` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"}}}}` | 199:Out → 19:Succeeded; 200:Out → 199:In |
| `mq038_village.questphase / h0 / 204` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 204:Out → 42:In3; 205:Out → 204:In |
| `mq038_village.questphase / h0 / 207` | `questLogicalXorNodeDefinition` `{}` | 29:Out → 207:In2; 207:Out1 → 193:In; 208:Out1 → 207:In1 |
| `mq038_village.questphase / h0 / 213` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"isPlayer":false}}}` | 214:Out → 213:In; 213:Out → 216:In1 |
| `mq038_village.questphase / h0 / 215` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleWater_ConditionType","anyVehicle":false,"vehicleRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"}}}}` | 214:Out → 215:In; 215:Out → 216:In2 |
| `mq038_village.questphase / h0 / 216` | `questLogicalXorNodeDefinition` `{}` | 216:Out1 → 42:In5; 213:Out → 216:In1; 215:Out → 216:In2 |
| `mq038_village.questphase / h494 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"},"condition":"OnUnmount"}}}` | 0:Out → 2:In; 17:Out1 → 2:In; 2:Out → 7:In |
| `mq038_village.questphase / h494 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentIsPlayer":true,"childRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"}}}}` | 5:Out → 3:In; 3:Out → 4:Succeeded |
| `mq038_village.questphase / h494 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq038_neweridentity/mq038_neweridentity/04_deliver_to_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 7:In; 7:True → 6:Inactive; 7:False → 9:In |
| `mq038_village.questphase / h494 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq038_neweridentity/mq038_neweridentity/05_hide_trunk","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 9:False → 5:Active; 7:False → 9:In; 9:True → 8:Inactive; 11:Out → 9:In |
| `mq038_village.questphase / h494 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleTrunk_ConditionType","playerVehicle":false,"vehicleRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"}}}}` | 0:Out → 10:In; 10:Out → 1:In |
| `mq038_village.questphase / h494 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq038_deliver_inactive"}}}` | 4:Out → 13:In; 13:True → 15:Active; 13:False → 14:In |
| `mq038_village.questphase / h494 / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq038_hide_inactive"}}}` | 13:False → 14:In; 18:Out → 14:In; 14:True → 16:Active; 14:False → 17:In1 |
| `mq038_01b_fisher_village.scene / scene / 137` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dennis_calls_v_start_done"}}}` | 137:0:0 → 138:0:1; 143:0:0 → 137:0:1 |
| `mq038_01b_fisher_village.scene / scene / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dennis_calls_v_end_done"}}}` | 139:0:0 → 140:0:1; 144:0:0 → 139:0:1 |
| `mq038_01b_fisher_village.scene / scene / 268` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dennis_calls_v_end_done"}}}` | 268:0:0 → 270:0:1; 272:0:0 → 268:0:1 |
| `mq038_01b_fisher_village.scene / scene / 280` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 1:0:0 → 280:0:1; 280:0:0 → 282:0:0 |
| `mq038_01b_fisher_village.scene / scene / 285` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 138:0:0 → 285:0:1; 285:0:0 → 272:0:1 |
| `mq038_02_ending.scene / scene / 129` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\minor_quests\\mq038\\scenes\\mq038_02_ending.scene","Flags":"Soft"},"sectionName":"mq038_02_who_is_he","type":"IsOutside"}}}` | 38:0:1 → 129:0:1; 129:0:0 → 37:0:0 |
| `mq038_02_ending.scene / scene / 132` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\minor_quests\\mq038\\scenes\\mq038_02_ending.scene","Flags":"Soft"},"sectionName":"mq038_02_professional","type":"IsOutside"}}}` | 38:0:2 → 132:0:1; 132:0:0 → 47:0:0 |
| `mq038_02_ending.scene / scene / 145` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq038_com_car"},"childIsPlayer":true,"condition":"OnUnmount"}}}` | 145:0:0 → 144:0:3; 145:0:0 → 211:0:1; 229:0:0 → 145:0:1 |
| `mq038_02_ending.scene / scene / 152` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq038_com_surgeon","names":["surgeon"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 93:0:0 → 152:0:1; 152:0:0 → 204:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq038_02_ending.scene / scene / 152; mq038_tyger_combat.questphase / h0 / 2; mq038_tyger_combat.questphase / h0 / 20; mq038_village.questphase / h0 / 163; +2 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq038_02_ending.scene / scene / 92 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `call_lifecycle` | mq038_ending.questphase / h0 / 33; mq038_village.questphase / h0 / 77 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `choice_gate` | mq038_01b_fisher_village.scene / scene / 44; mq038_02_ending.scene / scene / 28; mq038_02_ending.scene / scene / 38; mq038_02_ending.scene / scene / 6 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | mq038_02_ending.scene / scene / 88; mq038_02_ending.scene / scene / 93; mq038_tyger_combat.questphase / h0 / 1; mq038_village.questphase / h0 / 29; +4 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq038_01b_fisher_village.scene / scene / 137; mq038_01b_fisher_village.scene / scene / 139; mq038_01b_fisher_village.scene / scene / 268; mq038_quest_bugfixes.questphase / h0 / 15; +9 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq038_ending.questphase / h0 / 56; mq038_ending.questphase / h0 / 58; mq038_ending.questphase / h0 / 59; mq038_quest_bugfixes.questphase / h53 / 6; +7 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `item_state` | mq038_ending.questphase / h0 / 41 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `mount_state` | mq038_02_ending.scene / scene / 145; mq038_ending.questphase / h0 / 48; mq038_ending.questphase / h0 / 49; mq038_village.questphase / h0 / 199; +4 locations in catalogue.json | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | mq038_ending.questphase / h0 / 50 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq038_01b_fisher_village.scene / scene / 138; mq038_01b_fisher_village.scene / scene / 140; mq038_01b_fisher_village.scene / scene / 143; mq038_01b_fisher_village.scene / scene / 144; +12 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq038_village.questphase / h0 / 207; mq038_village.questphase / h0 / 216; mq038_village.questphase / h0 / 42 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq038_ending.questphase / h0 / 19; mq038_village.questphase / h0 / 100; mq038_village.questphase / h0 / 102; mq038_village.questphase / h0 / 90 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq038_ending.questphase / h0 / 51; mq038_tyger_combat.questphase / h0 / 19 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq038_ending.questphase / h0 / 16 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq038_ending.questphase / h0 / 18; mq038_ending.questphase / h0 / 7; mq038_tyger_combat.questphase / h0 / 11; mq038_village.questphase / h0 / 139; +1 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `target_resolution` | mq038_01b_fisher_village.scene / scene / 280; mq038_01b_fisher_village.scene / scene / 285; mq038_village.questphase / h0 / 192; mq038_village.questphase / h0 / 204 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mq038_02_ending.scene / scene / 211; mq038_ending.questphase / h0 / 21; mq038_ending.questphase / h0 / 37; mq038_ending.questphase / h0 / 46; +11 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq038_02_ending.scene / scene / 108; mq038_02_ending.scene / scene / 197; mq038_02_ending.scene / scene / 198; mq038_02_ending.scene / scene / 271; +12 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq038_quest_bugfixes.questphase / h7 / 10; mq038_village.questphase / h0 / 104; mq038_village.questphase / h0 / 158 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq038\mq038_quest_bugfixes.questphase` | repair; journal anchor | `base-mq038` |
| `base\quest\minor_quests\mq038\phases\mq038_ending.questphase` | content candidate; journal anchor | `base-mq038` |
| `base\quest\minor_quests\mq038\phases\mq038_tyger_combat.questphase` | content candidate; forward dependency | `base-mq038` |
| `base\quest\minor_quests\mq038\phases\mq038_village.questphase` | content candidate; journal anchor | `base-mq038` |
| `base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene` | content candidate; forward dependency | `base-mq038` |
| `base\quest\minor_quests\mq038\scenes\mq038_02_ending.scene` | content candidate; journal anchor | `base-mq038` |

Evidence shards for this dossier (including parent context): [base-mq038](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq038.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
