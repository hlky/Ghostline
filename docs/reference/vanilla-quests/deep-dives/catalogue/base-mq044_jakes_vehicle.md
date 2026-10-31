# Sex On Wheels

Journal: `quests/minor_quest/mq044_jakes_vehicle` · `MinorQuest` · hash `522295962`.

**Coverage: journal-linked.** 14 exact journal-linked nodes in 2 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Who ever said no to a free car? Not to mention it's a Quadra Turbo Fuckin' R. So quit picking your nose, head down to Rancho Coronado and get behind that wheel. (Primary) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage` |
| Get in the car. (Primary) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/03_get_in_car` |
| Leave the area. (Primary) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/04_leave_area` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq044_quest_bugfixes.questphase / h37 / 8` (Journal) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage` | 10:Out → 8:Active; 9:Out → 8:Active; 8:Out → 11:Active |
| `mq044_quest_bugfixes.questphase / h37 / 11` (Journal) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage/brief` | 11:Out → 1:In; 8:Out → 11:Active |
| `mq044_quest_bugfixes.questphase / h37 / 12` (Condition) | `quests/minor_quest/mq044_jakes_vehicle`; `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage` | 5:True → 12:In; 12:True → 7:In |
| `mq044_quest_bugfixes.questphase / h130 / 4` (Condition) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage` | 2:Out → 4:In; 4:True → 6:In; 4:False → 5:In |
| `mq044_quest_bugfixes.questphase / h130 / 5` (Condition) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/03_get_in_car` | 4:False → 5:In; 5:True → 6:In; 5:False → 8:In |
| `mq044_main.questphase / h0 / 5` (Condition) | `quests/minor_quest/mq044_jakes_vehicle`; `quests/minor_quest/mq044_jakes_vehicle` | 0:Out → 5:In; 5:False → 1:In; 5:True → 2:In1 |
| `mq044_main.questphase / h14 / 56` (Journal) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage` | 54:Out → 56:Active; 56:Out → 59:Active |
| `mq044_main.questphase / h14 / 59` (Journal) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage/brief` | 59:Out → 53:In; 56:Out → 59:Active |
| `mq044_main.questphase / h231 / 14` (Journal) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/03_get_in_car` | 17:Out → 14:Active; 14:Out → 16:In |
| `mq044_main.questphase / h231 / 15` (Journal) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/04_leave_area` | 18:Out → 15:Active; 15:Out → 19:In |
| `mq044_main.questphase / h231 / 17` (Journal) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage` | 12:Out → 17:Succeeded; 17:Out → 14:Active |
| `mq044_main.questphase / h231 / 18` (Journal) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/03_get_in_car` | 18:Out → 15:Active; 37:Out → 18:Succeeded |
| `mq044_main.questphase / h231 / 20` (Journal) | `quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/04_leave_area` | 19:Out → 20:Succeeded; 20:Out → 28:In |
| `mq044_main.questphase / h231 / 21` (Journal) | `quests/minor_quest/mq044_jakes_vehicle` | 26:Out → 21:Succeeded; 27:Out → 21:Succeeded; 21:Out → 39:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\mq044\phases\mq044.questphase` / h0 / 2 | `mq044_main.questphase` | 4: PauseCondition; 2:Out1 → 1:In; 4:Out → 2:In1 |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 149 | `mq044.questphase` | 150: PauseCondition: {"days": 3}; 150:Out → 149:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |

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
| `CYB-12345` | mq044_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-616764` | mq044_quest_bugfixes.questphase / h37 / 2 | No reader in selected context |
| `CYB-664521` | mq044_quest_bugfixes.questphase / h130 / 2 | mq044_quest_bugfixes.questphase / h130 / 3 |
| `CYB-664521_B` | mq044_quest_bugfixes.questphase / h130 / 7 | No reader in selected context |
| `CYB-664521_C` | mq044_quest_bugfixes.questphase / h130 / 8 | No reader in selected context |
| `gle_06_succeed` | Producer outside selected context | mq044_main.questphase / h14 / 28; mq044_main.questphase / h231 / 2; mq044_main.questphase / h231 / 28; mq044_quest_bugfixes.questphase / h37 / 6 |
| `mq044_done` | mq044_main.questphase / h231 / 22 | No reader in selected context |
| `mq044_started` | mq044_main.questphase / h14 / 55; mq044_quest_bugfixes.questphase / h37 / 7 | No reader in selected context |
| `mq_044_started_in_main` | Producer outside selected context | mq044_quest_bugfixes.questphase / h37 / 5 |
| `travelling_merchant_lives` | Producer outside selected context | mq044_quest_bugfixes.questphase / h0 / 17 |

## Exact gates, joins and cancellation

<details><summary>20 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq044_quest_bugfixes.questphase / h0 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 18:Out → 17:In |
| `mq044_quest_bugfixes.questphase / h37 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq_044_started_in_main","value":1,"comparisonType":"GreaterOrEqual"}}}` | 2:Out → 5:In; 5:True → 12:In |
| `mq044_quest_bugfixes.questphase / h37 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_06_succeed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 6:In; 6:True → 9:Active; 6:False → 10:Active |
| `mq044_quest_bugfixes.questphase / h37 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq044_jakes_vehicle","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded","inverted":true}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active","inverted":true}}]}}` | 5:True → 12:In; 12:True → 7:In |
| `mq044_quest_bugfixes.questphase / h130 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-664521"}}}` | 0:Out → 3:In; 3:False → 2:In; 3:True → 7:In |
| `mq044_quest_bugfixes.questphase / h130 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/01_reach_garage","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 4:In; 4:True → 6:In; 4:False → 5:In |
| `mq044_quest_bugfixes.questphase / h130 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq044_jakes_vehicle/mq044_jakes_vehicle/03_get_in_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 4:False → 5:In; 5:True → 6:In; 5:False → 8:In |
| `mq044_main.questphase / h0 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq044_jakes_vehicle","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active","inverted":true}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq044_jakes_vehicle","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded","inverted":true}}]}}` | 0:Out → 5:In; 5:False → 1:In; 5:True → 2:In1 |
| `mq044_main.questphase / h14 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_06_succeed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 55:Out → 28:In; 28:True → 57:Active; 28:False → 58:Active |
| `mq044_main.questphase / h14 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq044_com_veh"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 53:Out → 52:In; 52:Out → 60:In |
| `mq044_main.questphase / h14 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq044_com_workers"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 64:Out → 42:In; 65:Out → 64:In |
| `mq044_main.questphase / h14 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq044_com_scavs"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 66:Out → 33:In; 67:Out → 66:In |
| `mq044_main.questphase / h231 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_06_succeed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 25:Out → 2:In; 2:True → 12:In; 2:False → 32:In; 2:False → 12:In |
| `mq044_main.questphase / h231 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq044_tr_area"}}` | 2:True → 12:In; 2:False → 12:In; 12:Out → 17:Succeeded |
| `mq044_main.questphase / h231 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq044_com_veh","names":["vehicle"]},"childIsPlayer":true}}}` | 14:Out → 16:In; 16:Out → 36:In |
| `mq044_main.questphase / h231 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq044_tr_area"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq044_com_veh","names":["vehicle"]},"childIsPlayer":true}}]}}` | 15:Out → 19:In; 19:Out → 20:Succeeded |
| `mq044_main.questphase / h231 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_06_succeed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 20:Out → 28:In; 28:True → 26:Active; 28:False → 27:Active |
| `mq044_main.questphase / h231 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq044_com_scavs"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 2:False → 32:In; 32:Out → 31:In |
| `mq044_main.questphase / h420 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":1}}}` | 14:Out → 15:In; 15:Out → 16:In |
| `mq044_main.questphase / h420 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#santo_domingo_tr","isPlayerActivator":false}}` | 16:Out → 13:In; 15:Out → 16:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq044_main.questphase / h14 / 52; mq044_main.questphase / h14 / 64; mq044_main.questphase / h14 / 66 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `community_lifecycle` | mq044_main.questphase / h14 / 26; mq044_main.questphase / h14 / 41; mq044_main.questphase / h14 / 48; mq044_main.questphase / h14 / 53; +2 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq044_main.questphase / h14 / 28; mq044_main.questphase / h231 / 2; mq044_main.questphase / h231 / 28; mq044_quest_bugfixes.questphase / h0 / 17; +3 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | mq044_main.questphase / h14 / 37; mq044_main.questphase / h14 / 38; mq044_main.questphase / h420 / 4; mq044_main.questphase / h420 / 7 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | mq044_main.questphase / h420 / 15 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `mount_state` | mq044_main.questphase / h231 / 16; mq044_main.questphase / h231 / 19 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `persistent_decision` | mq044_main.questphase / h14 / 55; mq044_main.questphase / h231 / 22; mq044_quest_bugfixes.questphase / h130 / 2; mq044_quest_bugfixes.questphase / h130 / 7; +4 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `target_resolution` | mq044_main.questphase / h231 / 32 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mq044_main.questphase / h14 / 60; mq044_main.questphase / h231 / 33; mq044_main.questphase / h231 / 36 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `world_variant` | mq044_main.questphase / h14 / 39; mq044_main.questphase / h14 / 40; mq044_main.questphase / h420 / 5 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` | repair; journal anchor | `base-mq044` |
| `base\quest\minor_quests\mq044\phases\mq044_main.questphase` | content candidate; journal anchor | `base-mq044` |

Evidence shards for this dossier (including parent context): [base-mq044](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq044.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
