# Dirty Second Hands

Journal: `ep1/quests/minor_quest/q304_gear_pickup` · `MinorQuest` · hash `3923743204`.

Journal premise: Nothin' in this world is free. Not even the shit you already own. Gotta pay the man Hands if you wanna pick up your things from the safehouse in Dogtown.  Or whatever, fuck it, maybe this is a good opportunity to downsize.

**Coverage: journal-linked.** 12 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Send payment to Mr. Hands to get your gear back. (Primary) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/01_pay_hands` |
| Collect €$20,000 for Mr. Hands to recover your lost gear. (Primary) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/01b_gather_money` |
| Wait for Mr. Hands to deliver your gear. (Primary) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/02_wait_until_delivery` |
| Collect your gear from the locker. (Primary) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/03_pick_up_gear` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `q304_gear_return_messages.questphase / h0 / 16` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/01_pay_hands` | 25:Out1 → 16:Succeeded; 16:Out → 17:Active |
| `q304_gear_return_messages.questphase / h0 / 17` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/02_wait_until_delivery` | 16:Out → 17:Active |
| `q304_gear_return_messages.questphase / h0 / 18` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/02_wait_until_delivery` | 8:Out → 18:Succeeded; 18:Out → 19:Active |
| `q304_gear_return_messages.questphase / h0 / 19` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/03_pick_up_gear` | 18:Out → 19:Active |
| `q304_gear_return_messages.questphase / h0 / 20` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup` | 23:Out → 20:Succeeded; 20:Out → 46:In |
| `q304_gear_return_messages.questphase / h0 / 45` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup` | 44:Out → 45:Failed; 45:Out → 47:In |
| `q304_gear_return_messages.questphase / h174 / 4` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/01_pay_hands` | 12:Out1 → 4:Active; 4:Out → 15:Active |
| `q304_gear_return_messages.questphase / h174 / 6` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/01b_gather_money` | 5:False → 6:Active; 13:Out → 6:Active; 6:Out → 7:In; 6:Out → 16:Active |
| `q304_gear_return_messages.questphase / h174 / 8` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/01b_gather_money` | 7:Out → 8:Succeeded; 8:Out → 12:In1 |
| `q304_gear_return_messages.questphase / h174 / 13` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/01_gear_pickup/01_pay_hands` | 13:Out → 6:Active; 10:Out → 13:Inactive; 13:Out → 14:In |
| `q304_gear_return_messages.questphase / h174 / 15` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/description` | 4:Out → 15:Active |
| `q304_gear_return_messages.questphase / h174 / 16` (Journal) | `ep1/quests/minor_quest/q304_gear_pickup/description` | 6:Out → 16:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\quest\main_quests\q304\phases\q304_gear_pickup.questphase` / h7 / 13 | `q304_gear_return_messages.questphase` | 14: PauseCondition; 14:Out → 13:In1; 13:Out1 → 25:In2 |
| `ep1\quest\ep1_persistent_content.questphase` / h388 / 3 | `q304_gear_pickup.questphase` | 19: LogicalHub; 19:Out2 → 3:In1 |
| `ep1\quest\ep1_additional_game_elements.questphase` / h0 / 2 | `ep1_persistent_content.questphase` | 0: Input; 15: Input; 0:Out → 2:In1; 15:Out → 2:growl |
| `ep1\openworld\ep1_open_world.quest` / h0 / 26 | `ep1_additional_game_elements.questphase` | 2: PauseCondition: {"seconds": 1}; 2:Out → 26:In1 |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 10 | `ep1_additional_game_elements.questphase` | 6: FactsDBManager: ep1_side_content; 6:Out → 10:In1 |
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_sandbox_activity.quest` / h0 / 5 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 5:In1 |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest` / h0 / 16 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 16:In1 |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest` / h0 / 20 | `ep1_additional_game_elements.questphase` | 0: Start; 0:Out → 20:In1 |
| `ep1\quest\ep1.questphase` / h58 / 4 | `ep1_additional_game_elements.questphase` | 2: Phase: ep1_bugfixing.questphase; 2: Phase: ep1_bugfixing.questphase; 9: CutControl; 7: PauseCondition: ep1_active GreaterOrEqual 1; 2:Out1 → 4:In2; 2:growl → 4:growl; 9:CutSource → 4:CutDestination; 7:Out → 4:In1 |
| `ep1\quest\main_quests\q301\q301.quest` / h0 / 13 | `ep1_additional_game_elements.questphase` | 4: CharacterManager; 4:Out → 13:In1 |
| `ep1\quest\main_quests\q302\q302.quest` / h0 / 6 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 6:In1 |
| `ep1\quest\main_quests\q303\q303.quest` / h0 / 4 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 4:In1 |
| `ep1\quest\main_quests\q304\q304.quest` / h0 / 5 | `ep1_additional_game_elements.questphase` | 12: Checkpoint; 12:Out → 5:In1 |
| `ep1\quest\main_quests\q305\q305.quest` / h0 / 4 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 4:In1 |
| `ep1\quest\main_quests\q306\q306.quest` / h354 / 3 | `ep1_additional_game_elements.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 2 | `ep1_additional_game_elements.questphase` | 4: LogicalHub; 10: CutControl; 4:Out1 → 2:In1; 10:CutSource → 2:CutDestination |
| `ep1\quest\minor_quests\mq301\mq301.quest` / h0 / 6 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 6:In1 |
| `ep1\quest\minor_quests\mq303\mq303.quest` / h95 / 3 | `ep1_additional_game_elements.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 2 | `ep1_additional_game_elements.questphase` | 4: LogicalHub; 4:Out1 → 2:In1 |
| `ep1\quest\minor_quests\mq305\mq305.quest` / h0 / 5 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 5:In1 |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |

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
| `q304_gear_pickup_done` | q304_gear_return_messages.questphase / h0 / 46 | No reader in selected context |
| `q304_gear_pickup_failed` | q304_gear_return_messages.questphase / h0 / 47 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>9 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `q304_gear_return_messages.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType"}},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q304_tr_gear_storage_at_squat_transfer_range"}]}}` | 6:Out → 7:In; 7:Out → 8:In; 7:Out → 9:Active |
| `q304_gear_return_messages.questphase / h0 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q304_tr_gear_storage_at_squat_transfer_range"}}` | 8:Out → 10:In; 10:Out → 11:In; 10:Out → 12:In; 10:Out → 22:In |
| `q304_gear_return_messages.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q304_gear_return_crate"},"isPlayer":false}}}` | 10:Out → 12:In; 12:Out → 21:In |
| `q304_gear_return_messages.questphase / h0 / 43` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"51369838828","quantity":20000,"comparisonType":"GreaterOrEqual"}}}` | 43:True → 25:In1; 42:Out1 → 43:In; 43:False → 44:Active |
| `q304_gear_return_messages.questphase / h174 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/q304_gear_return/03_ch_return_items/01_pay_for_gear","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 3:Out → 1:In; 2:Out → 3:In; 14:CutSource → 3:CutDestination |
| `q304_gear_return_messages.questphase / h174 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"51369838828","quantity":20000,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 5:In; 5:True → 12:In1; 5:False → 6:Active |
| `q304_gear_return_messages.questphase / h174 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"51369838828","quantity":20000,"comparisonType":"GreaterOrEqual"}}}` | 6:Out → 7:In; 7:Out → 8:Succeeded |
| `q304_gear_return_messages.questphase / h174 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"51369838828","quantity":20000,"comparisonType":"Less"}}}` | 11:Out → 10:Inactive; 12:Out2 → 11:In |
| `q304_gear_return_messages.questphase / h174 / 14` | `questCutControlNodeDefinition` `{}` | 14:CutSource → 3:CutDestination; 13:Out → 14:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `controller_event` | q304_gear_return_messages.questphase / h0 / 21; q304_gear_return_messages.questphase / h0 / 22; q304_gear_return_messages.questphase / h0 / 23 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `item_state` | q304_gear_return_messages.questphase / h0 / 12; q304_gear_return_messages.questphase / h0 / 43; q304_gear_return_messages.questphase / h174 / 11; q304_gear_return_messages.questphase / h174 / 5; +1 locations in catalogue.json | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | q304_gear_return_messages.questphase / h0 / 16; q304_gear_return_messages.questphase / h0 / 17; q304_gear_return_messages.questphase / h0 / 18; q304_gear_return_messages.questphase / h0 / 19; +15 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | q304_gear_return_messages.questphase / h0 / 46; q304_gear_return_messages.questphase / h0 / 47 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `retire_branch` | q304_gear_return_messages.questphase / h174 / 14 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `spatial_gate` | q304_gear_return_messages.questphase / h0 / 10; q304_gear_return_messages.questphase / h0 / 7 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `world_variant` | q304_gear_return_messages.questphase / h0 / 8 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` | content candidate; journal anchor | `ep1-q304` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-08.json.gz), [ep1-sts-ep1-13](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-13.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

23 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 1 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `7e7dbbc930b3717fd790` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h174 / 13 -> 6 -> 16 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `58839785c560a180ce48` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h0 / 20 -> 46 -> 1 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `e8092c906f4e8e5c2d6d` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h0 / 2 -> 3 -> 42 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPhaseNodeDefinition; Out -> Active; Out -> In1 |
| `4803de0710dd8d0fcd3d` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h174 / 6 -> 7 -> 8 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `4f64918875c7d975bed8` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h174 / 13 -> 6 -> 7 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]; Out -> Active; Out -> In |
| `c5b928b17fd0f76f4d35` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h0 / 0 -> 2 -> 3 | questInputNodeDefinition -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `806bcfb85ed5e3a580ad` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h174 / 8 -> 12 -> 4 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questLogicalHubNodeDefinition -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In1; Out1 -> Active |
| `bd5a6f93c73e722e1e3d` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h0 / 25 -> 16 -> 17 | questLogicalHubNodeDefinition -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out1 -> Succeeded; Out -> Active |
| `c40a35d8f53711d60407` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h0 / 44 -> 45 -> 47 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Failed; Out -> In |
| `fe492809833dacc55ded` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h174 / 5 -> 6 -> 7 | questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]; False -> Active; Out -> In |
| `45bf997c0ab55f3dc696` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h0 / 21 -> 23 -> 20 | questEventManagerNodeDefinition -> questEventManagerNodeDefinition -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `c6206398795d1ddd15e3` | `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h0 / 8 -> 18 -> 19 | questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` / h0 / 42 | `h174` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq303\mq303.gamedef` | content candidate | ep1\quest\minor_quests\mq303\mq303.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq305\mq305.gamedef` | content candidate | ep1\quest\minor_quests\mq305\mq305.quest |
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
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_sandbox_activity_test.gamedef` | content candidate | ep1\openworld\sandbox_activities\courier_spot\ep1_courier_sandbox_activity.quest |
| `ep1\quest\ep1.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_nc_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| No attributed direct resource binding | Attribution unresolved | — |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| No external graph writer located | External engine/device/script production remains possible |

NodeRef uses: 9; TweakDB binding uses: 9. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
