# New Person, Same Old Mistakes

Journal: `ep1/quests/minor_quest/wst_ep1_11_bill_meeting` · `SideQuest` · hash `270395742`.

Journal premise: Well, well! Word from Bill Mitchell! I wonder what brilliant idea Mr. None-Too-Bright has come up with this time.

**Coverage: journal-linked.** 15 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Meet with Bill in the Glen. (Primary) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/meet_bill` |
| Read the message from Bill. (Primary) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/read_message` |
| Talk to Bill. (Primary) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/talk_bill` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `wst_ep1_11.questphase / h0 / 25` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/meet_bill` | 107:Out → 25:Succeeded; 25:Out → 48:Active |
| `wst_ep1_11.questphase / h0 / 35` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/talk_bill` | 109:Out → 35:Succeeded; 35:Out → 80:Succeeded |
| `wst_ep1_11.questphase / h0 / 47` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/meet_bill` | 102:Out → 47:Inactive; 101:False → 47:Succeeded; 47:Out → 53:Active |
| `wst_ep1_11.questphase / h0 / 48` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/talk_bill` | 25:Out → 48:Active; 48:Out → 110:In |
| `wst_ep1_11.questphase / h0 / 50` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11` | 58:Out → 50:Active; 50:Out → 103:Active |
| `wst_ep1_11.questphase / h0 / 51` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/meet_bill` | 83:Out → 51:Active; 51:Out → 108:In |
| `wst_ep1_11.questphase / h0 / 52` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/meet_bill` | 77:Out → 52:Active; 52:Out → 82:In1 |
| `wst_ep1_11.questphase / h0 / 53` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/talk_bill` | 47:Out → 53:Active; 53:Out → 110:In |
| `wst_ep1_11.questphase / h0 / 76` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/read_message` | 59:Out → 76:Active; 76:Out → 79:In |
| `wst_ep1_11.questphase / h0 / 77` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/read_message` | 77:Out → 52:Active; 79:Out → 77:Succeeded |
| `wst_ep1_11.questphase / h0 / 80` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11` | 35:Out → 80:Succeeded; 80:Out → 81:Succeeded |
| `wst_ep1_11.questphase / h0 / 81` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting` | 81:Out → 38:In; 80:Out → 81:Succeeded |
| `wst_ep1_11.questphase / h0 / 101` (Condition) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/read_message` | 101:False → 47:Succeeded; 113:Out → 101:In; 101:True → 102:Inactive |
| `wst_ep1_11.questphase / h0 / 102` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/read_message` | 102:Out → 47:Inactive; 101:True → 102:Inactive |
| `wst_ep1_11.questphase / h0 / 103` (Journal) | `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/description` | 50:Out → 103:Active; 103:Out → 59:Active; 103:Out → 100:In; 103:Out → 114:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 11 | `wst_ep1_11.questphase` | 35: PauseCondition: sts_ep1_10_finished; 35:Out → 11:In1 |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 14 | `ep1_world_stories.questphase` | 11: LogicalHub; 11:Out1 → 14:In1 |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest` / h0 / 7 | `ep1_world_stories.questphase` | 3: PauseCondition: {"seconds": 2}; 3:Out → 7:In1 |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest` / h0 / 112 | `ep1_world_stories.questphase` | 118: PauseCondition: sts_ep1_06_close_club; 118:Out → 112:In1 |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest` / h0 / 13 | `ep1_world_stories.questphase` | 7: PauseCondition: {"seconds": 2}; 7:Out → 13:In1 |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest` / h0 / 19 | `ep1_world_stories.questphase` | 3: FactsDBManager: ep1_12_test_def; 3:Out → 19:In1 |
| `ep1\openworld\ep1_open_world.quest` / h0 / 5 | `ep1_open_world.questphase` | 2: PauseCondition: {"seconds": 1}; 2:Out → 5:In1 |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 9 | `ep1_open_world.questphase` | 6: FactsDBManager: ep1_side_content; 6:Out → 9:In1 |
| `ep1\openworld\vendors\vehicle_metaquest\phases\vehicle_metaquest_ep1_bugfixing.questphase` / h17 / 6 | `ep1_open_world.questphase` | 4: Condition: militech_hellhound_available; 4:False → 6:CP77-63752 |
| `ep1\quest\ep1.questphase` / h58 / 5 | `ep1_open_world.questphase` | 0: Input; 9: CutControl; 0:Out → 5:In1; 9:CutSource → 5:CutDestination |
| `ep1\quest\main_quests\q301\q301.quest` / h0 / 19 | `ep1_open_world.questphase` | 4: CharacterManager; 4:Out → 19:In1 |
| `ep1\quest\main_quests\q302\q302.quest` / h0 / 23 | `ep1_open_world.questphase` | 1: Start; 1:Out → 23:In1 |
| `ep1\quest\main_quests\q303\q303.quest` / h0 / 12 | `ep1_open_world.questphase` | 1: Start; 1:Out → 12:In1 |
| `ep1\quest\main_quests\q304\q304.quest` / h0 / 26 | `ep1_open_world.questphase` | 12: Checkpoint; 12:Out → 26:In1 |
| `ep1\quest\main_quests\q305\q305.quest` / h0 / 10 | `ep1_open_world.questphase` | 1: Start; 1:Out → 10:In1 |
| `ep1\quest\main_quests\q306\q306.quest` / h354 / 2 | `ep1_open_world.questphase` | 0: Input; 0:Out → 2:In1 |
| `ep1\quest\minor_quests\mq301\mq301.quest` / h0 / 4 | `ep1_open_world.questphase` | 1: Start; 1:Out → 4:In1 |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 7 | `ep1_open_world.questphase` | 4: LogicalHub; 4:Out1 → 7:In1 |
| `ep1\quest\minor_quests\mq306\mq306.quest` / h0 / 9 | `ep1_open_world.questphase` | 1: Start; 1:Out → 9:In1 |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 16 | `vehicle_metaquest_ep1_bugfixing.questphase` | 0: Input; 0:Out → 16:In1 |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 3 | `ep1_openworld_bugfixing.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\ep1.questphase` / h58 / 2 | `ep1_bugfixing.questphase` | 25: LogicalXor; 2:CP77-65722_out → 27:In; 2:CP77-64292_out → 26:In; 25:Out1 → 2:In1; 2:Out1 → 4:In2; 2:growl → 4:growl |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 12 | `ep1_bugfixing.questphase` | 11: LogicalHub; 11:Out1 → 12:In1 |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 5 | `ep1_bugfixing.questphase` | 4: LogicalHub; 4:Out1 → 5:In1 |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| No resolved scene dependency in this scope | This does not prove the quest has no dialogue | — |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `bill_default_on` | wst_ep1_11.questphase / h0 / 100; wst_ep1_11.questphase / h0 / 69; wst_ep1_11.questphase / h0 / 99 | wst_ep1_11.questphase / h0 / 118; wst_ep1_11.questphase / h0 / 121 |
| `ep1_standalone` | Producer outside selected context | wst_ep1_11.questphase / h0 / 94 |
| `sts_ep1_10_debug_fact_1111` | Producer outside selected context | wst_ep1_11.questphase / h0 / 106 |
| `sts_ep1_10_dodger_dead` | Producer outside selected context | wst_ep1_11.questphase / h0 / 132; wst_ep1_11.questphase / h0 / 56 |
| `ws_ep1_11_chicken_test_journal_start` | Producer outside selected context | wst_ep1_11.questphase / h0 / 93 |
| `wst_ep1_11_hotdog_finished` | Producer outside selected context | wst_ep1_11.questphase / h0 / 109 |
| `wst_ep1_11_ncpd_finished` | Producer outside selected context | wst_ep1_11.questphase / h0 / 64 |
| `wst_ep1_11_ncpd_start` | Producer outside selected context | wst_ep1_11.questphase / h0 / 72 |

## Exact gates, joins and cancellation

<details><summary>33 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `wst_ep1_11.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":32}}}` | 0:Out → 3:In; 3:Out → 9:In |
| `wst_ep1_11.questphase / h0 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_11_activate"}}` | 3:Out → 9:In; 9:Out → 56:In |
| `wst_ep1_11.questphase / h0 / 56` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_10_dodger_dead"}}}` | 9:Out → 56:In; 56:True → 94:In; 56:False → 63:In; 56:False → 62:In; 56:False → 99:In |
| `wst_ep1_11.questphase / h0 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_11_ncpd_finished"}}}` | 75:CutSource → 64:CutDestination; 73:Out2 → 64:In; 64:Out → 65:In |
| `wst_ep1_11.questphase / h0 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_11_activate"}}` | 64:Out → 65:In; 75:Out → 65:In; 65:Out → 67:In; 65:Out → 68:In; 65:Out → 69:In |
| `wst_ep1_11.questphase / h0 / 71` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 71:Out1 → 38:In; 67:Out → 71:In1; 68:Out → 71:In2; 69:Out → 71:In3 |
| `wst_ep1_11.questphase / h0 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_11_ncpd_start"}}}` | 73:Out1 → 72:In; 72:Out → 74:In |
| `wst_ep1_11.questphase / h0 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":12}}}` | 72:Out → 74:In; 74:Out → 75:In |
| `wst_ep1_11.questphase / h0 / 75` | `questCutControlNodeDefinition` `{}` | 75:CutSource → 64:CutDestination; 75:Out → 65:In; 74:Out → 75:In |
| `wst_ep1_11.questphase / h0 / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/bill/wst_ep1_11_bill_invitation/bill_invitation","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 76:Out → 79:In; 79:Out → 77:Succeeded |
| `wst_ep1_11.questphase / h0 / 83` | `questCutControlNodeDefinition` `{}` | 83:Out → 51:Active; 82:track → 83:In; 83:CutSource → 113:CutDestination |
| `wst_ep1_11.questphase / h0 / 87` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/bill/wst_ep1_11_bill_invitation/bill_track","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"state":"Succeeded"}}}` | 90:Out1 → 87:In; 87:False → 89:In1 |
| `wst_ep1_11.questphase / h0 / 88` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/bill/wst_ep1_11_bill_invitation/bill_dont_track","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"state":"Succeeded"}}}` | 90:Out2 → 88:In; 88:False → 89:In2 |
| `wst_ep1_11.questphase / h0 / 89` | `questLogicalAndNodeDefinition` `{}` | 89:Out1 → 86:Inactive; 87:False → 89:In1; 88:False → 89:In2 |
| `wst_ep1_11.questphase / h0 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ws_ep1_11_chicken_test_journal_start"}}}` | 0:Out → 93:In |
| `wst_ep1_11.questphase / h0 / 94` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone"}}}` | 56:True → 94:In; 94:True → 95:In; 94:False → 96:In |
| `wst_ep1_11.questphase / h0 / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"EP1_Minor"}}}` | 94:True → 95:In; 95:Out → 97:In1 |
| `wst_ep1_11.questphase / h0 / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"MinorQuestAndSts"}}}` | 94:False → 96:In; 96:Out → 97:In2 |
| `wst_ep1_11.questphase / h0 / 101` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/read_message","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 101:False → 47:Succeeded; 113:Out → 101:In; 101:True → 102:Inactive |
| `wst_ep1_11.questphase / h0 / 106` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_10_debug_fact_1111"}}}` | 58:Out → 106:In; 106:Out → 104:In |
| `wst_ep1_11.questphase / h0 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_11_bill_met"}}` | 107:Out → 25:Succeeded; 107:Out → 90:In1; 108:Out → 107:In; 107:Out → 115:In |
| `wst_ep1_11.questphase / h0 / 109` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_11_hotdog_finished"}}}` | 109:Out → 35:Succeeded; 110:Out → 109:In |
| `wst_ep1_11.questphase / h0 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_11_bill_met"}}` | 83:CutSource → 113:CutDestination; 113:Out → 90:In2; 113:Out → 101:In; 114:Out → 113:In; 113:Out → 115:In |
| `wst_ep1_11.questphase / h0 / 115` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#wst_ep1_11_hot_dog_bill_gate","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsClosed"}}}` | 107:Out → 115:In; 110:Out → 115:In; 115:True → 111:In; 113:Out → 115:In |
| `wst_ep1_11.questphase / h0 / 118` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"bill_default_on"}}}` | 119:Out → 118:In; 118:Out → 132:In |
| `wst_ep1_11.questphase / h0 / 120` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#wst_ep1_11_hot_dog_bill_gate","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsClosed"}}}` | 117:Out → 120:In; 120:Out → 126:In |
| `wst_ep1_11.questphase / h0 / 121` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"bill_default_on"}}}` | 126:Out → 121:In; 121:Out → 122:In |
| `wst_ep1_11.questphase / h0 / 126` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_11_activate"}}` | 120:Out → 126:In; 126:Out → 121:In |
| `wst_ep1_11.questphase / h0 / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_11_bill_met"}}` | 117:Out → 127:In; 131:Out1 → 127:In; 127:Out → 128:In |
| `wst_ep1_11.questphase / h0 / 130` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_11_bill_met"}}` | 129:Out → 130:In; 130:Out → 131:In1 |
| `wst_ep1_11.questphase / h0 / 132` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_10_dodger_dead"}}}` | 132:True → 116:In; 118:Out → 132:In |
| `wst_ep1_11.questphase / h329 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/bill/wst_ep1_11_bill_invitation/v_choice/track","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 0:Out → 2:In; 2:Out → 4:Active |
| `wst_ep1_11.questphase / h329 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/bill/wst_ep1_11_bill_invitation/v_choice/dont_track","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 0:Out → 3:In; 3:Out → 5:Active |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `community_lifecycle` | wst_ep1_11.questphase / h0 / 62; wst_ep1_11.questphase / h0 / 63; wst_ep1_11.questphase / h0 / 67; wst_ep1_11.questphase / h0 / 68 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | wst_ep1_11.questphase / h0 / 106; wst_ep1_11.questphase / h0 / 109; wst_ep1_11.questphase / h0 / 118; wst_ep1_11.questphase / h0 / 121; +6 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | wst_ep1_11.questphase / h0 / 104; wst_ep1_11.questphase / h0 / 105; wst_ep1_11.questphase / h0 / 111; wst_ep1_11.questphase / h0 / 112; +8 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | wst_ep1_11.questphase / h0 / 115; wst_ep1_11.questphase / h0 / 120 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | wst_ep1_11.questphase / h0 / 3; wst_ep1_11.questphase / h0 / 74 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_read` | wst_ep1_11.questphase / h0 / 79 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | wst_ep1_11.questphase / h0 / 102; wst_ep1_11.questphase / h0 / 103; wst_ep1_11.questphase / h0 / 14; wst_ep1_11.questphase / h0 / 18; +16 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | wst_ep1_11.questphase / h0 / 89 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | wst_ep1_11.questphase / h0 / 100; wst_ep1_11.questphase / h0 / 69; wst_ep1_11.questphase / h0 / 99 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | wst_ep1_11.questphase / h0 / 71 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `retire_branch` | wst_ep1_11.questphase / h0 / 75; wst_ep1_11.questphase / h0 / 83 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `spatial_gate` | wst_ep1_11.questphase / h0 / 107; wst_ep1_11.questphase / h0 / 113; wst_ep1_11.questphase / h0 / 126; wst_ep1_11.questphase / h0 / 127; +3 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` | content candidate; journal anchor | `ep1-wst-ep1-11` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq306.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-01](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-01.json.gz), [ep1-sts-ep1-06-zembinsky](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-06-zembinsky.json.gz), [ep1-sts-ep1-10](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-10.json.gz), [ep1-sts-ep1-12](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-12.json.gz), [ep1-wst-ep1-11](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-wst-ep1-11.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

79 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 1 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `ea4cb15199b9b3fa8e63` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 0 -> 3 -> 9 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `4e9253a72e6b0134b8dd` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 107 -> 25 -> 48 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `9c634ff27b9a7aa77918` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 0 -> 119 -> 118 | questInputNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `c596b6ad38e138adae94` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 69 -> 71 -> 38 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questLogicalXorNodeDefinition -> questOutputNodeDefinition; Out -> In3; Out1 -> In |
| `7e7dbbc930b3717fd790` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 50 -> 103 -> 59 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `0781ef00ea04c05ee418` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 50 -> 103 -> 114 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questDeletionMarkerNodeDefinition; Out -> Active; Out -> In |
| `da44faaa63ffe9d69306` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 127 -> 128 -> 129 | questPauseConditionNodeDefinition[questTriggerCondition] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out -> In; Out -> In |
| `62513b1c2fdaf0c74a1c` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 50 -> 103 -> 100 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Active; Out -> In |
| `e8092c906f4e8e5c2d6d` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 77 -> 52 -> 82 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPhaseNodeDefinition; Out -> Active; Out -> In1 |
| `e48dab4f1ad9e4057bc0` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 109 -> 35 -> 80 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Succeeded |
| `58fcd67b0afde536eb35` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 51 -> 108 -> 107 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `240148efc76953d1c5d4` | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 76 -> 79 -> 77 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 82 | `h329` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"track"},{"$type":"questOutputNodeDefinition","id":6,"socketName":"dont_track"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\minor_quests\mq306\mq306.quest |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.gamedef` | content candidate | ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest |
| `ep1\quest\main_quests\q301\q301.gamedef` | content candidate | ep1\quest\main_quests\q301\q301.quest |
| `ep1\quest\main_quests\q302\q302.gamedef` | content candidate | ep1\quest\main_quests\q302\q302.quest |
| `ep1\quest\main_quests\q303\q303.gamedef` | content candidate | ep1\quest\main_quests\q303\q303.quest |
| `ep1\quest\main_quests\q304\q304.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\q304_car_retrieval_test.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_escape.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_lab.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_songbird_finale.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_stadium.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q305\q305.gamedef` | content candidate | ep1\quest\main_quests\q305\q305.quest |
| `ep1\quest\main_quests\q306\q306.gamedef` | content candidate | ep1\quest\main_quests\q306\q306.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\openworld\ep1_open_world.gamedef` | content candidate | ep1\openworld\ep1_open_world.quest |
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01_testworld.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10_def.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| No attributed direct resource binding | Attribution unresolved | — |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `ep1_standalone` | ep1\quest\ep1_standalone.quest / h0 / 5; 1 total source locations in compressed evidence |
| `sts_ep1_10_dodger_dead` | ep1\openworld\street_stories\sts_ep1_10\phases\sts_ep1_10_openworld.questphase / h1109 / 146; ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_dodger_garage_scene.scene / scene / 914; ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_dodger_garage_scene.scene / scene / 2520; ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest / h76 / 17; 4 total source locations in compressed evidence |
| `ws_ep1_11_chicken_test_journal_start` | ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest / h76 / 47; 1 total source locations in compressed evidence |
| `wst_ep1_11_hotdog_finished` | ep1\quest\tertiary_characters\default_dialogs\bill_default\sts_10_bill_default.scene / scene / 108; 1 total source locations in compressed evidence |
| `wst_ep1_11_ncpd_finished` | ep1\quest\tertiary_characters\default_dialogs\bill_default\sts_10_bill_default.scene / scene / 116; 1 total source locations in compressed evidence |
| `wst_ep1_11_ncpd_start` | ep1\quest\tertiary_characters\default_dialogs\bill_default\sts_10_bill_default.scene / scene / 112; 1 total source locations in compressed evidence |

NodeRef uses: 34; TweakDB binding uses: 0. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
