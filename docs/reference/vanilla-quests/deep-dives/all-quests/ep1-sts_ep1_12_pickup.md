# Corpo of the Month

Journal: `ep1/quests/minor_quest/sts_ep1_12_pickup` · `MinorQuest` · hash `2068165795`.

Journal premise: Guess we really do live in a gonk's paradise. You let a corp play you and still feel like a "winner." The fixer's happy 'cause NetWatch owes him a favor. NetWatch is happy 'cause their covert op didn't go to shit. And V's happy 'cause the money's good... Christ, whatever happened to reason and human fuckin' dignity?

**Coverage: journal-linked.** 9 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

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
| `journal_transition` | wst_ep1_02.questphase / h0 / 11; wst_ep1_02.questphase / h0 / 2; wst_ep1_02.questphase / h0 / 26; wst_ep1_02.questphase / h0 / 28; +8 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | wst_ep1_02.questphase / h0 / 23; wst_ep1_02.questphase / h0 / 24; wst_ep1_02.questphase / h0 / 47 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | wst_ep1_02.questphase / h0 / 55 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `reward_commit` | wst_ep1_02.questphase / h0 / 8 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `spatial_gate` | wst_ep1_02.questphase / h0 / 40; wst_ep1_02.questphase / h0 / 61; wst_ep1_02.questphase / h0 / 7 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `world_variant` | wst_ep1_02.questphase / h0 / 36 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` | content candidate; journal anchor | `ep1-wst-ep1-02` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq306.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-01](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-01.json.gz), [ep1-sts-ep1-06-zembinsky](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-06-zembinsky.json.gz), [ep1-sts-ep1-10](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-10.json.gz), [ep1-sts-ep1-12](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-12.json.gz), [ep1-wst-ep1-02](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-wst-ep1-02.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

27 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 0 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `7e7dbbc930b3717fd790` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 6 -> 35 -> 57 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `d272838924cecebd72ca` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 41 -> 42 -> 13 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `3e6f03030764fcc75954` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 26 -> 27 -> 28 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Active |
| `b54739889d4d9a0745d2` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 59 -> 26 -> 27 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> Active; Out -> In |
| `80c436c3f41257230312` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 47 -> 5 -> 2 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; False -> Active |
| `85ba174646d56b45d66c` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 44 -> 45 -> 47 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `d1f111c26d5b25a439ba` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 53 -> 20 -> 44 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `8852f0dbd6d859b59497` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 23 -> 53 -> 20 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out -> In; Out -> In |
| `ff3adc95658d38e3e68e` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 2 -> 8 -> 24 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questRewardManagerNodeDefinition[questGiveReward_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `240148efc76953d1c5d4` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 59 -> 34 -> 33 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `70cdd8ca93455e047152` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 33 -> 9 -> 60 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questMappinManagerNodeDefinition; Out -> Active; Out -> Active |
| `a71df082e9c50e7aa5be` | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 20 -> 44 -> 45 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| No embedded handoff in resolved context | — | External calls remain in the main dossier |

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
| `sts_ep1_12_corpo_blueline` | ep1\openworld\street_stories\sts_ep1_12\phases\sts_ep1_12_cleanup.questphase / h0 / 38; ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_final_scene.scene / scene / 875; 2 total source locations in compressed evidence |
| `wst_ep1_14_active` | ep1\openworld\street_stories\sts_ep1_12\phases\sts_ep1_12_cleanup.questphase / h195 / 12; 1 total source locations in compressed evidence |

NodeRef uses: 13; TweakDB binding uses: 1. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
