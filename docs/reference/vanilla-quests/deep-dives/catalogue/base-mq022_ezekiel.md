# Ezekiel Saw the Wheel

Journal: `quests/minor_quest/mq022_ezekiel` · `MinorQuest` · hash `3697221403`.

**Coverage: journal-linked.** 12 exact journal-linked nodes in 4 resources; 4 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Identify the gunmen. (Primary) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/01_diner` |
| Here's a joke for you: V walks into a bar… and gets robbed. The end.\n\nJesus, you and your shit luck. You better figure something out quick or our epic story's about to get cut short in the stupidest way imaginable. Accidental deaths don't jive too well with me. Or with the birth of legends. (Primary) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide` |
| Talk to the diner owner. (Primary) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/03_outcome` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq022_quest_bugfixes.questphase / h30 / 10` (Condition) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mq022_description` | 10:True → 1:In; 9:Out → 10:In; 10:False → 11:Active |
| `mq022_quest_bugfixes.questphase / h30 / 11` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mq022_description` | 10:False → 11:Active; 11:Out → 12:Succeeded |
| `mq022_quest_bugfixes.questphase / h30 / 12` (Journal) | `quests/minor_quest/mq022_ezekiel` | 12:Out → 1:In; 11:Out → 12:Succeeded |
| `mq022_quest_bugfixes.questphase / h111 / 4` (Condition) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide` | 3:Out → 4:In; 4:True → 6:In |
| `mq022_beginning.questphase / h0 / 40` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide` | 47:Out → 40:Succeeded; 51:Out → 40:Succeeded; 40:Out → 41:Active |
| `mq022_beginning.questphase / h0 / 41` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/03_outcome` | 40:Out → 41:Active; 41:Out → 45:In; 41:Out → 78:In |
| `mq022_beginning.questphase / h0 / 52` (Journal) | `quests/minor_quest/mq022_ezekiel` | 43:mq022_owner_outcome_bad_out → 52:Succeeded; 52:Out → 44:In |
| `mq022_beginning.questphase / h0 / 54` (Journal) | `quests/minor_quest/mq022_ezekiel` | 43:mq022_owner_outcome_good_out → 54:Succeeded; 54:Out → 53:In |
| `mq022_combat.questphase / h0 / 33` (MappinManager) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mp_goon1` | 0:Out → 33:Inactive; 33:Out → 34:Active |
| `mq022_combat.questphase / h0 / 34` (MappinManager) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mp_area` | 33:Out → 34:Active |
| `mq022_01_diner.scene / scene / 152` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide` | 152:0:0 → 267:0:1; 466:0:0 → 152:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq022_01_diner.scene / scene / 267` (Journal) | `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mq022_description` | 152:0:0 → 267:0:1; 267:0:0 → 52:0:0; 267:0:0 → 596:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq022_beginning.questphase / h0 / 11` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene`; `#mq022_01_sm_diner` | 32:Out → 11:Start; 11:mq022_attacked → 39:In1; 11:mq022_outtalked → 50:In |
| `mq022_beginning.questphase / h0 / 39` | `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` | 11:mq022_attacked → 39:In1; 39:Out1 → 51:In |
| `mq022_beginning.questphase / h0 / 43` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene`; `#mq022_01_sm_diner` | 42:True → 43:mq022_people_dead; 42:False → 43:mq022_people_alive; 61:False → 43:mq022_people_alive; 43:mq022_owner_outcome_good_out → 54:Succeeded; 43:mq022_owner_outcome_bad_out → 52:Succeeded |
| `mq022_beginning.questphase / h202 / 10` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene`; `#mq022_01_sm_diner` | 11:Out → 10:mq022_01_attack |
| `mq022_combat.questphase / h0 / 14` | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene`; `#mq022_01_sm_diner` | 0:Out → 14:mq022_01_attack |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\mq022\mq022.questphase` / h0 / 84 | `mq022_beginning.questphase` | 2: Input; 2:Out → 84:In1; 84:Out1 → 89:In |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h0 / 39 | `mq022_combat.questphase` | 11: Scene: mq022_01_diner.scene; 11:mq022_attacked → 39:In1; 39:Out1 → 51:In |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h0 / 11 | `mq022_01_diner.scene` | 32: FactsDBManager: mq022_active; 32:Out → 11:Start; 11:mq022_attacked → 39:In1; 11:mq022_outtalked → 50:In |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h0 / 43 | `mq022_01_diner.scene` | 42: Condition; 42: Condition; 61: Condition: mq022_combat; 42:True → 43:mq022_people_dead; 42:False → 43:mq022_people_alive; 61:False → 43:mq022_people_alive; 43:mq022_owner_outcome_good_out → 54:Succeeded; 43:mq022_owner_outcome_bad_out → 52:Succeeded |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h202 / 10 | `mq022_01_diner.scene` | 11: FactsDBManager: mq022_no_choice_done write/default comparison 0; 11:Out → 10:mq022_01_attack |
| `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` / h0 / 14 | `mq022_01_diner.scene` | 0: Input; 0:Out → 14:mq022_01_attack |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 6 | `mq022.questphase` | 47: LogicalHub; 47:Out1 → 6:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq022_01_diner.scene` | std_arr_foodshop_04, mq022_01_attack, std_arr_foodshop_04_from_choice, mq022_people_dead, mq022_people_alive, Start → mq022_attacked, mq022_01_attack_out, std_arr_foodshop_04_end, mq022_outtalked, mq022_owner_outcome_good_out, std_arr_foodshop_04_to_choice, mq022_owner_outcome_bad_out | Ganger_01; Ganger_02; Ganger_03; Owner; Diner_01; Diner_02; Diner_03; Diner_04; Diner_05; Diner_06; Diner_07; Player; 165 nodes / 192 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq022_01_diner.scene / n93 / 0` | Somebody likes being the center of attention. (``) | No option-level predicate stored | 0:0 → 100:0:0; 0:0 → 522:0:2; 0:0 → 956:0:1 |
| `mq022_01_diner.scene / n104 / 0` | [Pay off] Take the money. (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "127415915065", "difficulty": "EASY"}}}} | 0:0 → 155:0:0; 0:0 → 246:0:0 |
| `mq022_01_diner.scene / n104 / 1` | You're on rival territory. (``) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83574632792"}}}} | 0:1 → 156:0:0; 0:1 → 246:0:0 |
| `mq022_01_diner.scene / n104 / 2` | You don't know who you're fucking with. (``) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "127415915065", "buildId": "75476658533", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:2 → 157:0:0; 0:2 → 246:0:0 |
| `mq022_01_diner.scene / n104 / 3` | You're sending mixed signals. (``) | No option-level predicate stored | 0:3 → 163:0:0 |
| `mq022_01_diner.scene / n132 / 0` | pl-pl[wyjmij broń] A teraz umrzecie. (``) | No option-level predicate stored | 0:0 → 776:0:1 |
| `mq022_01_diner.scene / n192 / 0` | [Lean] I'll take a Calavera Feliz. (``) | No option-level predicate stored | 0:0 → 197:0:0 |
| `mq022_01_diner.scene / n192 / 1` | [Lean] One Spunky Monkey, please. (``) | No option-level predicate stored | 0:1 → 208:0:0 |
| `mq022_01_diner.scene / n192 / 2` | [Lean] Get me a Tiancha. (``) | No option-level predicate stored | 0:2 → 210:0:0 |
| `mq022_01_diner.scene / n214 / 0` | Robbing a diner? That's sad. (``) | No option-level predicate stored | 0:0 → 215:0:0; 0:0 → 522:0:0 |
| `mq022_01_diner.scene / n214 / 1` | Leave them alone! (``) | No option-level predicate stored | 0:1 → 216:0:0; 0:1 → 522:0:1 |
| `mq022_01_diner.scene / n571 / 0` | [Step away] (``) | No option-level predicate stored | 0:0 → 575:0:0 |
| `mq022_01_diner.scene / n610 / 0` | Could use a drink. (``) | No option-level predicate stored | 0:0 → 637:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CYB-12345` | mq022_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-601738` | mq022_quest_bugfixes.questphase / h30 / 2 | mq022_quest_bugfixes.questphase / h30 / 8 |
| `CYB-623804` | mq022_quest_bugfixes.questphase / h111 / 3 | mq022_quest_bugfixes.questphase / h111 / 2 |
| `mq022_active` | mq022_beginning.questphase / h0 / 32 | No reader in selected context |
| `mq022_combat` | mq022_01_diner.scene / scene / 776; mq022_01_diner.scene / scene / 846 | mq022_01_diner.scene / scene / 775; mq022_01_diner.scene / scene / 849; mq022_beginning.questphase / h0 / 61 |
| `mq022_done` | Producer outside selected context | mq022_quest_bugfixes.questphase / h30 / 9 |
| `mq022_no_choice_done` | mq022_01_diner.scene / scene / 562; mq022_01_diner.scene / scene / 824; mq022_beginning.questphase / h202 / 11 | mq022_01_diner.scene / scene / 566; mq022_01_diner.scene / scene / 775 |
| `std_arr_foodshop_04_default_on` | mq022_01_diner.scene / scene / 838; mq022_beginning.questphase / h0 / 58 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | mq022_quest_bugfixes.questphase / h0 / 15 |

## Exact gates, joins and cancellation

<details><summary>26 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq022_quest_bugfixes.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 16:Out → 15:In |
| `mq022_quest_bugfixes.questphase / h30 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-601738"}}}` | 0:Out → 8:In; 8:False → 2:In |
| `mq022_quest_bugfixes.questphase / h30 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_done"}}}` | 2:Out → 9:In; 9:Out → 10:In |
| `mq022_quest_bugfixes.questphase / h30 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mq022_description","fileEntryIndex":2,"className":"gameJournalQuestDescription"},"state":"Active"}}}` | 10:True → 1:In; 9:Out → 10:In; 10:False → 11:Active |
| `mq022_quest_bugfixes.questphase / h111 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-623804"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq022_quest_bugfixes.questphase / h111 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 3:Out → 4:In; 4:True → 6:In |
| `mq022_beginning.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq022_tr_ezekiel_starts"}}` | 38:Out → 2:In; 2:Out → 48:In; 2:Out → 75:In; 2:Out → 76:In; 2:Out → 77:In |
| `mq022_beginning.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3:Out → 6:In; 6:Out → 38:In; 6:Out → 72:In; 6:Out → 73:In; 6:Out → 74:In |
| `mq022_beginning.questphase / h0 / 42` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"},"unconscious":false,"defeated":false}}}` | 61:True → 42:In; 42:True → 43:mq022_people_dead; 42:False → 43:mq022_people_alive |
| `mq022_beginning.questphase / h0 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 47:Out → 40:Succeeded; 50:Out → 47:In |
| `mq022_beginning.questphase / h0 / 61` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_combat"}}}` | 61:True → 42:In; 61:False → 43:mq022_people_alive; 45:Out → 61:In |
| `mq022_beginning.questphase / h0 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_diner"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 70:Out → 3:In; 69:Out → 70:In |
| `mq022_beginning.questphase / h202 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2:Out → 3:In; 3:Out → 8:In; 3:Out → 14:In |
| `mq022_beginning.questphase / h202 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers","names":["ganger_01"]},"isPlayer":false}}}` | 3:Out → 8:In; 8:Out → 11:In |
| `mq022_beginning.questphase / h202 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 13:Out → 6:In; 14:Out → 13:In |
| `mq022_combat.questphase / h0 / 8` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 2:Out → 8:In1; 4:Out → 8:In2; 6:Out → 8:In3; 8:Out1 → 11:In; 8:Out1 → 10:In; 8:Out1 → 9:In |
| `mq022_combat.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers","names":["ganger_01"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 30:Out → 15:In; 15:Out → 18:In1 |
| `mq022_combat.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers","names":["ganger_02"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 31:Out → 16:In; 16:Out → 18:In2 |
| `mq022_combat.questphase / h0 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq022_com_gangers","names":["ganger_03"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 32:Out → 17:In; 17:Out → 18:In3 |
| `mq022_combat.questphase / h0 / 18` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 18:Out1 → 1:In; 15:Out → 18:In1; 16:Out → 18:In2; 17:Out → 18:In3 |
| `mq022_01_diner.scene / scene / 566` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_no_choice_done"}}}` | 140:0:0 → 566:0:1; 566:0:0 → 139:0:0; 566:0:1 → 119:0:0 |
| `mq022_01_diner.scene / scene / 775` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_no_choice_done"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_combat"}}]}}` | 291:2:3 → 775:0:1; 775:0:0 → 779:0:0 |
| `mq022_01_diner.scene / scene / 831` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#std_arr_foodshop_04","names":["barman"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"Less"}}}` | 602:0:0 → 831:0:1; 831:0:0 → 610:0:0; 831:0:0 → 830:0:0 |
| `mq022_01_diner.scene / scene / 849` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq022_combat"}}}` | 171:0:0 → 849:0:1; 849:0:0 → 575:0:0; 849:0:1 → 571:0:0 |
| `mq022_01_diner.scene / scene / 935` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 163:0:0 → 935:0:1; 935:0:0 → 104:1:0; 935:0:0 → 246:0:0; 935:0:0 → 562:0:1; 940:1:0 → 935:0:0 |
| `mq022_01_diner.scene / scene / 956` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 93:0:0 → 956:0:1; 956:0:0 → 52:1:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq022_beginning.questphase / h0 / 6; mq022_beginning.questphase / h0 / 70; mq022_beginning.questphase / h202 / 3 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq022_01_diner.scene / scene / 441; mq022_01_diner.scene / scene / 442; mq022_01_diner.scene / scene / 443; mq022_01_diner.scene / scene / 804; +2 locations in catalogue.json | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `choice_gate` | mq022_01_diner.scene / scene / 104; mq022_01_diner.scene / scene / 132; mq022_01_diner.scene / scene / 192; mq022_01_diner.scene / scene / 214; +3 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq022_combat.questphase / h0 / 10; mq022_combat.questphase / h0 / 11; mq022_combat.questphase / h0 / 27; mq022_combat.questphase / h0 / 28; +2 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq022_01_diner.scene / scene / 412; mq022_01_diner.scene / scene / 413; mq022_01_diner.scene / scene / 414; mq022_01_diner.scene / scene / 444; +8 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq022_01_diner.scene / scene / 566; mq022_01_diner.scene / scene / 775; mq022_01_diner.scene / scene / 849; mq022_beginning.questphase / h0 / 61; +4 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `parallel_join` | mq022_combat.questphase / h0 / 18; mq022_combat.questphase / h0 / 8 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq022_01_diner.scene / scene / 562; mq022_01_diner.scene / scene / 776; mq022_01_diner.scene / scene / 824; mq022_01_diner.scene / scene / 838; +7 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | mq022_01_diner.scene / scene / 935; mq022_01_diner.scene / scene / 956; mq022_beginning.questphase / h0 / 47 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | mq022_01_diner.scene / scene / 185 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq022_beginning.questphase / h0 / 11; mq022_beginning.questphase / h0 / 43; mq022_beginning.questphase / h202 / 10; mq022_combat.questphase / h0 / 14 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `target_resolution` | mq022_beginning.questphase / h0 / 42; mq022_beginning.questphase / h202 / 13; mq022_combat.questphase / h0 / 15; mq022_combat.questphase / h0 / 16; +1 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | mq022_01_diner.scene / scene / 308; mq022_01_diner.scene / scene / 314; mq022_01_diner.scene / scene / 318; mq022_01_diner.scene / scene / 320; +43 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq022_01_diner.scene / scene / 882; mq022_01_diner.scene / scene / 885; mq022_beginning.questphase / h202 / 2; mq022_beginning.questphase / h202 / 7 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` | repair; journal anchor | `base-mq022` |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` | content candidate; journal anchor | `base-mq022` |
| `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` | content candidate; journal anchor | `base-mq022` |
| `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` | content candidate; journal anchor | `base-mq022` |

Evidence shards for this dossier (including parent context): [base-mq022](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq022.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
