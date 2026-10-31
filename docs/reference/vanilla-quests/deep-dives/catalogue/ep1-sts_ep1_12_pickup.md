# Corpo of the Month

Journal: `ep1/quests/minor_quest/sts_ep1_12_pickup` · `MinorQuest` · hash `2068165795`.

**Coverage: journal-linked.** 9 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Read the message from Alan Noël. (Primary) | `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/read_message` |
| Collect your reward from Alan Noel. (Primary) | `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/take_reward` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `wst_ep1_02.questphase / h0 / 9` (Journal) | `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/take_reward` | 33:Out → 9:Active; 9:Out → 60:Active |
| `wst_ep1_02.questphase / h0 / 11` (Journal) | `ep1/quests/minor_quest/sts_ep1_12_pickup` | 10:Out → 11:Succeeded; 11:Out → 32:In |
| `wst_ep1_02.questphase / h0 / 33` (Journal) | `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/read_message` | 33:Out → 9:Active; 34:Out → 33:Succeeded |
| `wst_ep1_02.questphase / h0 / 35` (Journal) | `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/read_message` | 6:Out → 35:Active; 35:Out → 57:Active |
| `wst_ep1_02.questphase / h0 / 57` (Journal) | `ep1/quests/minor_quest/sts_ep1_12_pickup/description` | 35:Out → 57:Active; 57:Out → 58:Active |
| `wst_ep1_02.questphase / h0 / 58` (Journal) | `ep1/quests/minor_quest/sts_ep1_12_pickup/alan_codex` | 57:Out → 58:Active; 58:Out → 59:Active |
| `wst_ep1_02.questphase / h0 / 59` (Journal) | `ep1/quests/minor_quest/sts_ep1_12_pickup/alan_message` | 59:Out → 26:Active; 59:Out → 34:In; 58:Out → 59:Active |
| `wst_ep1_02.questphase / h0 / 60` (MappinManager) | `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/take_reward/mp2` | 9:Out → 60:Active; 60:Out → 61:In |
| `wst_ep1_02.questphase / h0 / 62` (MappinManager) | `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/take_reward/mp` | 62:Out → 10:In; 61:Out → 62:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 2 | `wst_ep1_02.questphase` | 26: PauseCondition: wst_ep1_02_active; 26:Out → 2:In1 |
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
| `ep1_standalone` | Producer outside selected context | wst_ep1_02.questphase / h0 / 48 |
| `sts_ep1_12_corpo_blueline` | Producer outside selected context | wst_ep1_02.questphase / h0 / 5 |
| `travelling_merchant_lives` | Producer outside selected context | wst_ep1_02.questphase / h0 / 56 |
| `wst_ep1_02_finished` | wst_ep1_02.questphase / h0 / 24 | No reader in selected context |
| `wst_ep1_02_start` | wst_ep1_02.questphase / h0 / 23 | No reader in selected context |
| `wst_ep1_14_active` | wst_ep1_02.questphase / h0 / 47 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>13 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `wst_ep1_02.questphase / h0 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_12_corpo_blueline"}}}` | 5:False → 2:Active; 47:Out → 5:In; 5:True → 36:In |
| `wst_ep1_02.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_02_tr"}}` | 55:Out1 → 7:In; 7:Out → 23:In |
| `wst_ep1_02.questphase / h0 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#sts_ep1_12_corpo_loot","eventType":"Executed"}}}` | 62:Out → 10:In; 10:Out → 11:Succeeded |
| `wst_ep1_02.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02_reply/wst_ep1_02_reply_b","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 26:Out → 27:In; 27:Out → 28:Active |
| `wst_ep1_02.questphase / h0 / 32` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02_reply/wst_ep1_02_reply_a","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02_reply/wst_ep1_02_reply_b","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Active"}}]}}` | 32:True → 8:In; 11:Out → 32:In; 32:False → 31:Inactive |
| `wst_ep1_02.questphase / h0 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02_corpo_blueline","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 34:Out → 33:Succeeded; 59:Out → 34:In |
| `wst_ep1_02.questphase / h0 / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_02_tr"}}` | 24:Out → 40:In; 40:Out → 37:In |
| `wst_ep1_02.questphase / h0 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone"}}}` | 0:Out → 48:In; 48:True → 49:In; 48:False → 50:In |
| `wst_ep1_02.questphase / h0 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"EP1_Minor"}}}` | 48:True → 49:In; 49:Out → 55:In1 |
| `wst_ep1_02.questphase / h0 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"MinorQuestAndSts"}}}` | 48:False → 50:In; 50:Out → 55:In2 |
| `wst_ep1_02.questphase / h0 / 55` | `questLogicalXorNodeDefinition` `{}` | 55:Out1 → 7:In; 49:Out → 55:In1; 50:Out → 55:In2 |
| `wst_ep1_02.questphase / h0 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":999}}}` | 0:Out → 56:In |
| `wst_ep1_02.questphase / h0 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sts_ep1_12_wst_02_mapping_trigger"}}` | 60:Out → 61:In; 61:Out → 62:Active |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `community_lifecycle` | wst_ep1_02.questphase / h0 / 41; wst_ep1_02.questphase / h0 / 42; wst_ep1_02.questphase / h0 / 44; wst_ep1_02.questphase / h0 / 45 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | wst_ep1_02.questphase / h0 / 48; wst_ep1_02.questphase / h0 / 5; wst_ep1_02.questphase / h0 / 56 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | wst_ep1_02.questphase / h0 / 20; wst_ep1_02.questphase / h0 / 37; wst_ep1_02.questphase / h0 / 53 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `journal_read` | wst_ep1_02.questphase / h0 / 34 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `persistent_decision` | wst_ep1_02.questphase / h0 / 23; wst_ep1_02.questphase / h0 / 24; wst_ep1_02.questphase / h0 / 47 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | wst_ep1_02.questphase / h0 / 55 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `reward_commit` | wst_ep1_02.questphase / h0 / 8 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `world_variant` | wst_ep1_02.questphase / h0 / 36 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` | content candidate; journal anchor | `ep1-wst-ep1-02` |

Evidence shards for this dossier (including parent context): [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz), [ep1-wst-ep1-02](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-wst-ep1-02.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
