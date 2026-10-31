# Hi Ho Silver Lining

Journal: `ep1/quests/street_stories/combat_zone_reward` · `StreetStory` · hash `1418121422`.

Journal premise: Hands is one megalomaniacal buffoon - and that’s comin’ from me. Let’s hope at least those fuckin’ slippers fit your feet like a glove.

**Coverage: journal-linked.** 29 exact journal-linked nodes in 3 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Get in the car. (Primary) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/enter_vehicle` |
| Meet with Mr. Hands. (Primary) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands` |
| Leave Heavy Hearts. (Primary) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/leave_pyramid` |
| Talk to Mr. Hands. (Primary) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands` |
| Wait for the Heavy Hearts club to open. (Primary) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/wait_for_hh_to_open` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mr_hands_fixers_loop.questphase / h117 / 3` (Journal) | `ep1/quests/street_stories/combat_zone_reward` | 46:False → 3:Active; 48:Out → 3:Active; 3:Out → 4:Active |
| `mr_hands_fixers_loop.questphase / h117 / 4` (Journal) | `ep1/quests/street_stories/combat_zone_reward/description` | 3:Out → 4:Active; 4:Out → 5:Active |
| `mr_hands_fixers_loop.questphase / h117 / 5` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands` | 4:Out → 5:Active; 5:Out → 35:In1; 5:Out → 104:In |
| `mr_hands_fixers_loop.questphase / h117 / 12` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands` | 103:Out → 12:Succeeded; 12:Out → 13:Active |
| `mr_hands_fixers_loop.questphase / h117 / 13` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands` | 12:Out → 13:Active; 13:Out → 21:In; 13:Out → 36:In1 |
| `mr_hands_fixers_loop.questphase / h117 / 16` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands` | 22:Out → 16:Succeeded; 16:Out → 23:Active |
| `mr_hands_fixers_loop.questphase / h117 / 23` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/leave_pyramid` | 16:Out → 23:Active; 23:Out → 85:In |
| `mr_hands_fixers_loop.questphase / h117 / 27` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/enter_vehicle` | 32:Out → 27:Succeeded; 27:Out → 28:Succeeded |
| `mr_hands_fixers_loop.questphase / h117 / 28` (Journal) | `ep1/quests/street_stories/combat_zone_reward` | 27:Out → 28:Succeeded; 28:Out → 51:Active |
| `mr_hands_fixers_loop.questphase / h117 / 47` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/wait_for_hh_to_open` | 46:True → 47:Active; 47:Out → 49:In |
| `mr_hands_fixers_loop.questphase / h117 / 48` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/wait_for_hh_to_open` | 48:Out → 3:Active; 49:Out → 48:Succeeded |
| `mr_hands_fixers_loop.questphase / h117 / 66` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/enter_vehicle` | 69:Out → 66:Active; 66:Out → 70:In |
| `mr_hands_fixers_loop.questphase / h117 / 69` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/leave_pyramid` | 69:Out → 66:Active; 67:Out → 69:Succeeded |
| `mr_hands_fixers_loop.questphase / h308 / 5` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands/mr_hands` | 5:Out → 6:Inactive |
| `mr_hands_fixers_loop.questphase / h308 / 6` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands/fake_mr_hands` | 5:Out → 6:Inactive |
| `mr_hands_fixers_loop.questphase / h308 / 7` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands/mr_hands` | 8:Out → 7:Inactive |
| `mr_hands_fixers_loop.questphase / h308 / 8` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands/fake_mr_hands` | 8:Out → 7:Inactive |
| `mr_hands_fixers_loop.questphase / h308 / 10` (PauseCondition) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands` | 0:Out → 10:In; 10:Out → 1:In |
| `mr_hands_fixers_loop.questphase / h308 / 11` (MappinManager) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands/mr_hands` | 2:Out → 11:Active; 11:Out → 9:In |
| `mr_hands_fixers_loop.questphase / h308 / 12` (MappinManager) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands/fake_mr_hands` | 12:Out → 2:In; 9:Out → 12:Active |
| `mr_hands_fixers_loop.questphase / h396 / 5` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands/mr_hands` | 5:Out → 6:Inactive |
| `mr_hands_fixers_loop.questphase / h396 / 6` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands/fake_mr_hands` | 5:Out → 6:Inactive |
| `mr_hands_fixers_loop.questphase / h396 / 7` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands/mr_hands` | 8:Out → 7:Inactive |
| `mr_hands_fixers_loop.questphase / h396 / 8` (Journal) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands/fake_mr_hands` | 8:Out → 7:Inactive |
| `mr_hands_fixers_loop.questphase / h396 / 10` (PauseCondition) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands` | 0:Out → 10:In; 10:Out → 1:In |
| `mr_hands_fixers_loop.questphase / h396 / 11` (MappinManager) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands/mr_hands` | 2:Out → 11:Active; 11:Out → 9:In |
| `mr_hands_fixers_loop.questphase / h396 / 12` (MappinManager) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands/fake_mr_hands` | 12:Out → 2:In; 9:Out → 12:Active |
| `ep1_street_stories.questphase / h105 / 14` (PauseCondition) | `ep1/quests/street_stories/combat_zone_reward` | 7:Out → 14:In; 14:Out → 16:In |
| `sts_ep1_06_cleanup.questphase / h704 / 2` (PauseCondition) | `ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/wait_for_hh_to_open` | 0:Out → 2:In; 2:Out → 7:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\street_stories\ep1_street_stories.questphase` / h0 / 46 | `mr_hands_fixers_loop.questphase` | 0: Input; 0:Out → 46:In1 |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 2 | `ep1_street_stories.questphase` | 33: PauseCondition: ep1_side_content GreaterOrEqual 1; 33:Out → 2:In1 |
| `ep1\openworld\street_stories\ep1_street_stories.questphase` / h470 / 16 | `sts_ep1_06_cleanup.questphase` | 8: Input; 8:Out → 16:In1 |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest` / h0 / 20 | `sts_ep1_06_cleanup.questphase` | 1: Phase: sts_ep1_06_zembinsky.questphase; 1:Out1 → 20:In1 |
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
| `mr_hands_reward_received` | Producer outside selected context | mr_hands_fixers_loop.questphase / h117 / 22 |
| `mr_hands_reward_waiting` | mr_hands_fixers_loop.questphase / h117 / 21 | No reader in selected context |
| `sts_ep1_06_wait_mq304` | Producer outside selected context | mr_hands_fixers_loop.questphase / h117 / 46; mr_hands_fixers_loop.questphase / h117 / 49 |

## Exact gates, joins and cancellation

<details><summary>15 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mr_hands_fixers_loop.questphase / h117 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mr_hands_reward_received"}}}` | 22:Out → 16:Succeeded; 21:Out → 22:In |
| `mr_hands_fixers_loop.questphase / h117 / 46` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_06_wait_mq304"}}}` | 2:Out → 46:In; 46:False → 3:Active; 46:True → 47:Active |
| `mr_hands_fixers_loop.questphase / h117 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_06_wait_mq304","comparisonType":"Equal"}}}` | 47:Out → 49:In; 49:Out → 48:Succeeded |
| `mr_hands_fixers_loop.questphase / h117 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#combat_zone_reward_vehicle"},"childIsPlayer":true}}}` | 70:Out → 33:In; 70:Out → 54:In; 66:Out → 70:In |
| `mr_hands_fixers_loop.questphase / h117 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mr_hands_tr_reward_scene"}}` | 103:Out → 12:Succeeded; 103:Out → 43:In; 94:Out → 103:In |
| `mr_hands_fixers_loop.questphase / h308 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mr_hands_combat_zone"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 0:Out → 2:In; 12:Out → 2:In; 2:Out → 11:Active |
| `mr_hands_fixers_loop.questphase / h308 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mr_hands_combat_zone"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false}}}}` | 11:Out → 9:In; 9:Out → 12:Active |
| `mr_hands_fixers_loop.questphase / h308 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/go_meet_hands","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 0:Out → 10:In; 10:Out → 1:In |
| `mr_hands_fixers_loop.questphase / h396 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mr_hands_combat_zone"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 12:Out → 2:In; 2:Out → 11:Active |
| `mr_hands_fixers_loop.questphase / h396 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mr_hands_combat_zone"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false}}}}` | 0:Out → 9:In; 11:Out → 9:In; 9:Out → 12:Active |
| `mr_hands_fixers_loop.questphase / h396 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/talk_with_hands","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 0:Out → 10:In; 10:Out → 1:In |
| `ep1_street_stories.questphase / h105 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/combat_zone_reward","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 7:Out → 14:In; 14:Out → 16:In |
| `ep1_street_stories.questphase / h105 / 16` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"NOR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/mr_hands_global_msg/new_sts_unlocked_answer/new_sts_unlocked_answer","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/mr_hands_global_msg/new_sts_unlocked_answer/new_sts_unlocked_answer_2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}]}}` | 14:Out → 16:In; 16:True → 15:Inactive |
| `sts_ep1_06_cleanup.questphase / h704 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/combat_zone_reward/combat_zone_reward/wait_for_hh_to_open","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 0:Out → 2:In; 2:Out → 7:In |
| `sts_ep1_06_cleanup.questphase / h704 / 7` | `questCutControlNodeDefinition` `{"permanent":true}` | 7:Out → 1:In; 2:Out → 7:In; 4:Out → 7:In; 7:CutSource → 5:CutDestination; 8:CutSource → 7:CutDestination |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mr_hands_fixers_loop.questphase / h308 / 2; mr_hands_fixers_loop.questphase / h308 / 9; mr_hands_fixers_loop.questphase / h396 / 2; mr_hands_fixers_loop.questphase / h396 / 9 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `conditional_route` | mr_hands_fixers_loop.questphase / h117 / 22; mr_hands_fixers_loop.questphase / h117 / 46; mr_hands_fixers_loop.questphase / h117 / 49 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | mr_hands_fixers_loop.questphase / h117 / 67 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `journal_transition` | ep1_street_stories.questphase / h105 / 7; mr_hands_fixers_loop.questphase / h117 / 12; mr_hands_fixers_loop.questphase / h117 / 13; mr_hands_fixers_loop.questphase / h117 / 16; +19 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | mr_hands_fixers_loop.questphase / h117 / 70 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `persistent_decision` | mr_hands_fixers_loop.questphase / h117 / 21 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `retire_branch` | sts_ep1_06_cleanup.questphase / h704 / 7 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `spatial_gate` | mr_hands_fixers_loop.questphase / h117 / 103 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | mr_hands_fixers_loop.questphase / h117 / 32 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` | content candidate; journal anchor | `ep1-shared` |
| `ep1\openworld\street_stories\ep1_street_stories.questphase` | content candidate; journal anchor | `ep1-shared` |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\phases\sts_ep1_06_cleanup.questphase` | content candidate; journal anchor | `ep1-sts-ep1-06-zembinsky` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq306.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-06-zembinsky](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-06-zembinsky.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

17 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 2 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `4e9253a72e6b0134b8dd` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 103 -> 12 -> 13 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `7e7dbbc930b3717fd790` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 48 -> 3 -> 4 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `0781ef00ea04c05ee418` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 16 -> 23 -> 85 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questDeletionMarkerNodeDefinition; Out -> Active; Out -> In |
| `1a9b8893087e174a603f` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 47 -> 49 -> 48 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `235ed1f97cea566186b0` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 22 -> 16 -> 23 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `62513b1c2fdaf0c74a1c` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 12 -> 13 -> 21 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Active; Out -> In |
| `223048580b7b66384a57` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 46 -> 3 -> 4 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; False -> Active; Out -> Active |
| `e8092c906f4e8e5c2d6d` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 12 -> 13 -> 36 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPhaseNodeDefinition; Out -> Active; Out -> In1 |
| `5db090327cb2f56e5c66` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 69 -> 66 -> 70 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]; Out -> Active; Out -> In |
| `afac8a0a934d956c841e` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h308 / 0 -> 10 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `4516825c8e1071cd9cb7` | `ep1\openworld\street_stories\sts_ep1_06_zembinsky\phases\sts_ep1_06_cleanup.questphase` / h704 / 0 -> 2 -> 7 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questCutControlNodeDefinition; Out -> In; Out -> In |
| `5cd775fe045e92b72670` | `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 13 -> 21 -> 22 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 35 | `h308` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `ep1\openworld\fixers\mr_hands\phases\mr_hands_fixers_loop.questphase` / h117 / 36 | `h396` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| No attributed direct resource binding | Attribution unresolved | — |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `mr_hands_reward_received` | ep1\openworld\fixers\mr_hands\scenes\mr_hands_combat_zone_default.scene / scene / 943; 1 total source locations in compressed evidence |
| `sts_ep1_06_wait_mq304` | ep1\openworld\street_stories\sts_ep1_06_zembinsky\phases\sts_ep1_06_cleanup.questphase / h0 / 74; ep1\openworld\street_stories\sts_ep1_06_zembinsky\phases\sts_ep1_06_cleanup.questphase / h0 / 92; 2 total source locations in compressed evidence |

NodeRef uses: 7; TweakDB binding uses: 0. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
