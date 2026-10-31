# New Person, Same Old Mistakes

Journal: `ep1/quests/minor_quest/wst_ep1_11_bill_meeting` · `SideQuest` · hash `270395742`.

**Coverage: journal-linked.** 15 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

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
| `ep1\openworld\vendors\vehicle_metaquest\phases\vehicle_metaquest_ep1_bugfixing.questphase` / h17 / 6 | `ep1_open_world.questphase` | 4: Condition: militech_hellhound_available; 4:False → 6:CP77-63752 |
| `ep1\quest\ep1.questphase` / h58 / 5 | `ep1_open_world.questphase` | 0: Input; 9: CutControl; 0:Out → 5:In1; 9:CutSource → 5:CutDestination |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 16 | `vehicle_metaquest_ep1_bugfixing.questphase` | 0: Input; 0:Out → 16:In1 |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 3 | `ep1_openworld_bugfixing.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\ep1.questphase` / h58 / 2 | `ep1_bugfixing.questphase` | 25: LogicalXor; 2:CP77-65722_out → 27:In; 2:CP77-64292_out → 26:In; 25:Out1 → 2:In1; 2:Out1 → 4:In2; 2:growl → 4:growl |

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

| Fact | Writers in context | Readers/conditions in context |
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
| `parallel_join` | wst_ep1_11.questphase / h0 / 89 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | wst_ep1_11.questphase / h0 / 100; wst_ep1_11.questphase / h0 / 69; wst_ep1_11.questphase / h0 / 99 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | wst_ep1_11.questphase / h0 / 71 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `retire_branch` | wst_ep1_11.questphase / h0 / 75; wst_ep1_11.questphase / h0 / 83 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` | content candidate; journal anchor | `ep1-wst-ep1-11` |

Evidence shards for this dossier (including parent context): [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz), [ep1-wst-ep1-11](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-wst-ep1-11.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
