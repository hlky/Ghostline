# Dirty Second Hands

Journal: `ep1/quests/minor_quest/q304_gear_pickup` · `MinorQuest` · hash `3923743204`.

**Coverage: journal-linked.** 12 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

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
| `ep1\quest\ep1.questphase` / h58 / 4 | `ep1_additional_game_elements.questphase` | 2: Phase: ep1_bugfixing.questphase; 2: Phase: ep1_bugfixing.questphase; 9: CutControl; 7: PauseCondition: ep1_active GreaterOrEqual 1; 2:Out1 → 4:In2; 2:growl → 4:growl; 9:CutSource → 4:CutDestination; 7:Out → 4:In1 |

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
| `item_state` | q304_gear_return_messages.questphase / h0 / 12; q304_gear_return_messages.questphase / h0 / 43; q304_gear_return_messages.questphase / h174 / 11; q304_gear_return_messages.questphase / h174 / 5; +1 locations in catalogue.json | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `persistent_decision` | q304_gear_return_messages.questphase / h0 / 46; q304_gear_return_messages.questphase / h0 / 47 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `retire_branch` | q304_gear_return_messages.questphase / h174 / 14 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `world_variant` | q304_gear_return_messages.questphase / h0 / 8 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\quest\main_quests\q304\phases\q304_gear_return_messages.questphase` | content candidate; journal anchor | `ep1-q304` |

Evidence shards for this dossier (including parent context): [ep1-q304](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-q304.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
