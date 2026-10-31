# Over the Edge

Journal: `quests/minor_quest/mq049_edgerunners` · `MinorQuest` · hash `692629639`.

Journal premise: Someone sprinklin’ XBDs around the city with cyberpsychos in the leading roles? The fuck’s that about? And that warning at the end... Strangest fuckin’ PSA I’ve ever seen. Only thread to follow here is the name dropped at the end – David Martinez. Sounds like the headstrong type. I like him already.

**Coverage: journal-linked.** 9 exact journal-linked nodes in 2 resources; 4 resources in the inspected dependency context.

Resource roles in that context: 4 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Text Muamar “El Capitan” Reyes and ask about David Martinez. (Primary) | `quests/minor_quest/mq049_edgerunners/01_el_captian/01_text_capitan` |
| Wait for Muamar “El Capitan” Reyes to respond about David Martinez. (Primary) | `quests/minor_quest/mq049_edgerunners/01_el_captian/02_wait` |
| Reply to Falco’s message. (Primary) | `quests/minor_quest/mq049_edgerunners/02_falco/01_respond_to_falco` |
| Collect the gift from Martinez’s crew left with Muamar “El Capitan” Reyes. (Primary) | `quests/minor_quest/mq049_edgerunners/03_gift/02_pick_up_gift` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq049.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq049_edgerunners/01_el_captian/01_text_capitan` | 19:Out → 4:Active; 4:Out → 5:Active; 4:Out → 11:In1 |
| `mq049.questphase / h0 / 5` (Journal) | `quests/minor_quest/mq049_edgerunners/desc` | 4:Out → 5:Active |
| `mq049.questphase / h0 / 13` (Journal) | `quests/minor_quest/mq049_edgerunners/01_el_captian/01_text_capitan` | 11:StartFalco → 13:Succeeded; 13:Out → 14:Active |
| `mq049.questphase / h0 / 14` (Journal) | `quests/minor_quest/mq049_edgerunners/01_el_captian/02_wait` | 13:Out → 14:Active; 14:Out → 20:In |
| `mq049_messages_falco.questphase / h0 / 16` (Journal) | `quests/minor_quest/mq049_edgerunners/01_el_captian/02_wait` | 27:Out → 16:Succeeded; 16:Out → 17:Active |
| `mq049_messages_falco.questphase / h0 / 17` (Journal) | `quests/minor_quest/mq049_edgerunners/02_falco/01_respond_to_falco` | 16:Out → 17:Active |
| `mq049_messages_falco.questphase / h0 / 21` (Journal) | `quests/minor_quest/mq049_edgerunners/02_falco/01_respond_to_falco` | 20:Out → 21:Succeeded; 21:Out → 23:In |
| `mq049_messages_falco.questphase / h0 / 24` (Journal) | `quests/minor_quest/mq049_edgerunners` | 24:Out → 1:In; 23:True → 24:Succeeded; 26:Out → 24:Succeeded |
| `mq049_messages_falco.questphase / h0 / 25` (Journal) | `quests/minor_quest/mq049_edgerunners/03_gift/02_pick_up_gift` | 23:False → 25:Active; 25:Out → 26:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq049.questphase / h0 / 11` | `base\quest\minor_quests\mq049\phases\mq049_messages_reyes.questphase` | 4:Out → 11:In1; 11:Out1 → 15:In1; 11:StartFalco → 13:Succeeded |
| `mq049.questphase / h0 / 12` | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` | 20:Out → 12:In1; 12:Out1 → 15:In2; 12:Jacket → 16:In1 |
| `mq049.questphase / h39 / 2` | `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene`; `#mq049_sm_braindance` | 0:Out → 2:mq049_in; 2:mq049_out → 7:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 64 | `mq049.questphase` | 63: DeletionMarker; 63:Out → 64:In1 |
| `base\quest\minor_quests\mq049\mq049.quest` / h0 / 2 | `mq049.questphase` | 3: PauseCondition: {"seconds": 2}; 2:Out1 → 1:In; 3:Out → 2:In1 |
| `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 12 | `mq049_messages_falco.questphase` | 20: Checkpoint; 20:Out → 12:In1; 12:Out1 → 15:In2; 12:Jacket → 16:In1 |
| `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 11 | `mq049_messages_reyes.questphase` | 4: Journal; 4:Out → 11:In1; 11:Out1 → 15:In1; 11:StartFalco → 13:Succeeded |
| `base\quest\minor_quests\mq049\mq049.questphase` / h39 / 2 | `mq049_braindance.scene` | 0: Input; 0:Out → 2:mq049_in; 2:mq049_out → 7:In |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
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
| `mq049_braindance.scene` | mq049_in, Start 1, Start 2 → mq049_out | Player; 94 nodes / 158 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq049_braindance.scene / n9 / 0` | pl-pl[puść braindance] (``) | {"questCondition": {"$type": "questCharacterCondition", "type": {"$type": "questCharacterState_ConditionType", "subType": {"$type": "questCharacterState_PlayerSubType", "vehicleComparisonType": "NotEqual", "vehicleState": "Driving"}}}} | 0:0 → 141:0:1; 0:0 → 521:0:0; 0:0 → 530:0:2 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `mq049_braindance_skipped` | mq049_braindance.scene / scene / 506 | mq049_braindance.scene / scene / 509 |
| `mq049_done` | mq049.questphase / h0 / 17 | No reader in selected context |
| `mq049_falco_done` | mq049_messages_falco.questphase / h0 / 20 | mq049_messages_reyes.questphase / h0 / 23 |
| `mq049_finished` | mq049.questphase / h0 / 18 | No reader in selected context |
| `mq049_jacket_looted` | mq049.questphase / h133 / 3 | mq049_messages_falco.questphase / h0 / 23; mq049_messages_falco.questphase / h0 / 26; mq049_messages_reyes.questphase / h0 / 29 |
| `mq049_reyes_distance_comment` | mq049_messages_reyes.questphase / h0 / 32; mq049_messages_reyes.questphase / h0 / 36 | mq049_messages_reyes.questphase / h0 / 30; mq049_messages_reyes.questphase / h0 / 34 |
| `mq049_started` | mq049.questphase / h39 / 7 | No reader in selected context |
| `q101_enable_side_content` | Producer outside selected context | mq049.questphase / h0 / 24 |

## Exact gates, joins and cancellation

<details><summary>36 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq049.questphase / h0 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq049_tr_braindance"}}` | 0:Out → 10:In; 10:Out → 6:In1; 9:Out1 → 10:In |
| `mq049.questphase / h0 / 15` | `questLogicalAndNodeDefinition` `{}` | 11:Out1 → 15:In1; 12:Out1 → 15:In2; 15:Out1 → 17:In |
| `mq049.questphase / h0 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 24:In; 24:Out → 25:Active |
| `mq049.questphase / h39 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq049_tr_braindance"}}` | 0:Out → 4:In; 4:Out → 5:In |
| `mq049.questphase / h133 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"118162581940","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 2:In; 2:Out → 3:In |
| `mq049.questphase / h178 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq049_tr_reyes_place"}}` | 0:Out → 2:In; 2:Out → 3:In |
| `mq049_messages_falco.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"SideQuest_MainPath"}},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq049_tr_reyes_place"}]}}` | 28:Out → 2:In; 2:Out → 19:In; 2:Out → 27:In; 2:Out → 30:In; 2:Out → 29:In |
| `mq049_messages_falco.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/falco/mq049_about_david/03_ch_about_david/03_about_david","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 5:Out → 6:In; 6:Out → 8:In1 |
| `mq049_messages_falco.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/falco/mq049_about_david/03_ch_about_david/03_about_xbd","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 5:Out → 7:In; 7:Out → 8:In2 |
| `mq049_messages_falco.questphase / h0 / 8` | `questLogicalXorNodeDefinition` `{}` | 6:Out → 8:In1; 7:Out → 8:In2; 8:Out1 → 9:Active |
| `mq049_messages_falco.questphase / h0 / 23` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq049_jacket_looted","value":1,"comparisonType":"GreaterOrEqual"}}}` | 21:Out → 23:In; 23:True → 24:Succeeded; 23:False → 25:Active |
| `mq049_messages_falco.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq049_jacket_looted","value":1,"comparisonType":"GreaterOrEqual"}}}` | 26:Out → 24:Succeeded; 25:Out → 26:In |
| `mq049_messages_falco.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 2:Out → 27:In; 27:Out → 16:Succeeded |
| `mq049_messages_falco.questphase / h0 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":1}}}` | 0:Out → 28:In; 28:Out → 2:In |
| `mq049_messages_falco.questphase / h0 / 30` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 2:Out → 30:In; 30:Out → 3:Active |
| `mq049_messages_reyes.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mq049_about_david_01/01_ch_do_you_know_david/01_braindance_about_david","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 2:Out → 3:In; 3:Out → 30:In |
| `mq049_messages_reyes.questphase / h0 / 9` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"83635443133"}}},"socketId":3384484177},{"$type":"questConditionItem","condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"83574632792"}}},"socketId":2712370139}]}` | 8:Out → 9:In; 9:Case3384484177 → 10:Active; 9:Case2712370139 → 11:Active; 9:Otherwise → 12:Active |
| `mq049_messages_reyes.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mq049_about_david_01/07_ch_corpo/07_about_arasaka","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 10:Out → 15:In; 15:Out → 21:In1 |
| `mq049_messages_reyes.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mq049_about_david_01/07_ch_corpo/07_wanna_meet","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 10:Out → 16:In; 16:Out → 21:In2 |
| `mq049_messages_reyes.questphase / h0 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mq049_about_david_01/07b_ch_street_kid/07_about_atlanta","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 11:Out → 17:In; 17:Out → 21:In3 |
| `mq049_messages_reyes.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mq049_about_david_01/07b_ch_street_kid/07_wanna_meet_sk","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 11:Out → 18:In; 18:Out → 21:In4 |
| `mq049_messages_reyes.questphase / h0 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mq049_about_david_01/07c_nomad/07_wanna_meet_nmd","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 12:Out → 19:In; 19:Out → 21:In5 |
| `mq049_messages_reyes.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mq049_about_david_01/07c_nomad/07c_learn_more_nmd","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 12:Out → 20:In; 20:Out → 21:In6 |
| `mq049_messages_reyes.questphase / h0 / 21` | `questLogicalXorNodeDefinition` `{"inputSocketCount":6}` | 15:Out → 21:In1; 16:Out → 21:In2; 17:Out → 21:In3; 18:Out → 21:In4; 19:Out → 21:In5; 20:Out → 21:In6; 21:Out1 → 34:In |
| `mq049_messages_reyes.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq049_falco_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 22:Out → 23:In; 23:Out → 24:In |
| `mq049_messages_reyes.questphase / h0 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq049_tr_reyes_place"},{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"SideQuest_MainPath"}}]}}` | 23:Out → 24:In; 24:Out → 29:In |
| `mq049_messages_reyes.questphase / h0 / 29` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq049_jacket_looted","comparisonType":"Equal"}}}` | 29:False → 1:In; 24:Out → 29:In; 29:True → 25:Active |
| `mq049_messages_reyes.questphase / h0 / 30` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#el_capitan"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#el_capitan"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":25.0},"comparisonType":"LessOrEqual"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq049_reyes_distance_comment","comparisonType":"Equal"}}]}}` | 3:Out → 30:In; 30:True → 31:Active; 30:False → 33:In2 |
| `mq049_messages_reyes.questphase / h0 / 34` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#el_capitan"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#el_capitan"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":25.0},"comparisonType":"LessOrEqual"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq049_reyes_distance_comment","comparisonType":"Equal"}}]}}` | 21:Out1 → 34:In; 34:True → 35:Active; 34:False → 37:In2 |
| `mq049_braindance.scene / scene / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":183}}}` | 11:2:1 → 38:0:1; 38:0:0 → 111:0:0; 38:0:0 → 151:0:1; 111:0:0 → 38:0:0 |
| `mq049_braindance.scene / scene / 111` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questInputAction_ConditionType","inputAction":"UI_Cancel"}}}` | 38:0:0 → 111:0:0; 111:0:0 → 38:0:0; 111:0:0 → 506:0:1; 119:0:0 → 111:0:1 |
| `mq049_braindance.scene / scene / 119` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 11:2:1 → 119:0:1; 119:0:0 → 111:0:1 |
| `mq049_braindance.scene / scene / 134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 134:0:0 → 57:0:0; 151:0:0 → 134:0:1 |
| `mq049_braindance.scene / scene / 151` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 38:0:0 → 151:0:1; 151:0:0 → 105:0:1; 151:0:0 → 134:0:1; 509:0:0 → 151:0:1 |
| `mq049_braindance.scene / scene / 232` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType","tickCount":5}}}` | 11:2:1 → 232:0:1; 232:0:0 → 24:0:1 |
| `mq049_braindance.scene / scene / 509` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq049_braindance_skipped","value":1,"comparisonType":"GreaterOrEqual"}}}` | 427:0:0 → 509:0:1; 509:0:0 → 151:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq049_messages_reyes.questphase / h0 / 30; mq049_messages_reyes.questphase / h0 / 34 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `call_lifecycle` | mq049_messages_falco.questphase / h0 / 29 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `checkpoint` | mq049.questphase / h0 / 19; mq049.questphase / h0 / 20; mq049.questphase / h133 / 5; mq049_braindance.scene / scene / 141 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq049_braindance.scene / scene / 9 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | mq049.questphase / h0 / 24; mq049_braindance.scene / scene / 509; mq049_messages_falco.questphase / h0 / 23; mq049_messages_falco.questphase / h0 / 26; +4 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `elapsed_time` | mq049_messages_falco.questphase / h0 / 28 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq049.questphase / h133 / 2 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | mq049.questphase / h0 / 13; mq049.questphase / h0 / 14; mq049.questphase / h0 / 25; mq049.questphase / h0 / 4; +30 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | mq049.questphase / h0 / 15 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq049.questphase / h0 / 17; mq049.questphase / h0 / 18; mq049.questphase / h133 / 3; mq049.questphase / h39 / 7; +4 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq049_messages_falco.questphase / h0 / 8; mq049_messages_reyes.questphase / h0 / 21 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq049_braindance.scene / scene / 119; mq049_braindance.scene / scene / 134; mq049_braindance.scene / scene / 151; mq049_braindance.scene / scene / 38; +2 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `scene_interface` | mq049.questphase / h39 / 2 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq049.questphase / h0 / 10; mq049.questphase / h178 / 2; mq049.questphase / h39 / 4; mq049_messages_falco.questphase / h0 / 2; +1 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `workspot_performance` | mq049_braindance.scene / scene / 83; mq049_braindance.scene / scene / 86; mq049_braindance.scene / scene / 88 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq049.questphase / h178 / 3; mq049_messages_falco.questphase / h0 / 19 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\minor_quests\mq049\mq049.questphase` | content candidate; journal anchor | `base-mq049` |
| `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` | content candidate; journal anchor | `base-mq049` |
| `base\quest\minor_quests\mq049\phases\mq049_messages_reyes.questphase` | content candidate; forward dependency | `base-mq049` |
| `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene` | content candidate; forward dependency | `base-mq049` |

Evidence shards for this dossier (including parent context): [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq049](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq049.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

64 repeated typed/socket path signatures in this selected graph context; 13 distinct direct resource identities; 3 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `7e7dbbc930b3717fd790` | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 9 -> 10 -> 11 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `1a9b8893087e174a603f` | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 25 -> 26 -> 24 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `2aa0f3a3b004f071652f` | `base\quest\minor_quests\mq049\mq049.questphase` / h178 / 2 -> 3 -> 1 | questPauseConditionNodeDefinition[questTriggerCondition] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `658fe17f8b47d2c016b7` | `base\quest\minor_quests\mq049\mq049.questphase` / h39 / 0 -> 4 -> 5 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questTriggerCondition] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `2179acd57cd33a158da3` | `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene` / scene / 134 -> 57 -> 83 | questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]; 0:0 -> 0:0; 4:0 -> 0:1 |
| `e92ddd1f938cdb586df5` | `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 18 -> 23 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPhaseNodeDefinition -> questOutputNodeDefinition; Out -> In1; Out1 -> In |
| `07a508d9181a1ec44ac6` | `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 17 -> 18 -> 23 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPhaseNodeDefinition; Out -> In; Out -> In1 |
| `62513b1c2fdaf0c74a1c` | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 14 -> 15 -> 20 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Active; Out -> In |
| `b54739889d4d9a0745d2` | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 4 -> 5 -> 6 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> Active; Out -> In |
| `44903fec4308710947a9` | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 21 -> 23 -> 25 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; False -> Active |
| `647ea9ce31c01a3e6527` | `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 0 -> 10 -> 6 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questTriggerCondition] -> questPhaseNodeDefinition; Out -> In; Out -> In1 |
| `f0a623166642f21156e9` | `base\quest\minor_quests\mq049\mq049.questphase` / h133 / 3 -> 5 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questCheckpointNodeDefinition -> questOutputNodeDefinition; Out -> In; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 6 | `h39` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":5,"socketName":"Loop"}] |
| `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 16 | `h133` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 23 | `h178` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
| `base\quest\minor_quests\mq049\mq049.gamedef` | content candidate | base\quest\minor_quests\mq049\mq049.quest |
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
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\player\female\body\player_locomotion_johnny_guitar.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand_thorton_mackinaw__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\male\body\player_locomotion_sick.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q201\q201_03_cabin_day_1\body\q201_03_cabin_day_1__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\gameplay\gui\quests\mq049\mq049_braindance.inkwidget` | UI | content/basegame_4_gamedata.archive; index evidence only |
| `base\movies\fullscreen\er\er_braindance.bk2` | asset binding .bk2 | content/basegame_5_video.archive; index evidence only |
| `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq049\phases\mq049_messages_reyes.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq049\scenes\lipsync\en\mq049_braindance\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\player\ground\player__stand_ground__idle__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q201\q201_03_cabin_day_1\player__lie_ground__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `q101_enable_side_content` | base\quest\minor_quests\mq025\mq025_psycho_brawl.quest / h0 / 14; base\quest\minor_quests\mq032\scenes\mq032_00_chicken_test_setup.scene / scene / 6; base\quest\minor_quests\mq048\mq048.questphase / h435 / 6; base\quest\minor_quests\mq049\mq049.quest / h0 / 5; 36 total source locations in compressed evidence |

NodeRef uses: 23; TweakDB binding uses: 14. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene` | 5 / 30 | scnAudioEvent: 1; scnDialogLineEvent: 3; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnPlaySkAnimEvent: 2; scnUnmountEvent: 1; scneventsAttachPropToNode: 1; scneventsAttachPropToPerformer: 2; scneventsAttachPropToWorld: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 8; scneventsVFXEvent: 7 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
