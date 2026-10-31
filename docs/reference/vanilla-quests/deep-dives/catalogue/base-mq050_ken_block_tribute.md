# I'm in Love with My Car

Journal: `quests/minor_quest/mq050_ken_block_tribute` · `MinorQuest` · hash `2765329288`.

**Coverage: journal-linked.** 10 exact journal-linked nodes in 3 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Get in the car. (Primary) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/get_inside_car` |
| Search the warehouse. (Primary) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/investigate` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq050.questphase / h0 / 23` (Journal) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/investigate` | 55:ContinueQuest → 23:Active; 23:Out → 24:Active |
| `mq050.questphase / h0 / 24` (Journal) | `quests/minor_quest/mq050_ken_block_tribute/mq050_description` | 23:Out → 24:Active; 24:Out → 81:In |
| `mq050.questphase / h0 / 26` (Journal) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/investigate` | 84:Out1 → 26:Succeeded; 26:Out → 27:Active |
| `mq050.questphase / h0 / 27` (Journal) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/get_inside_car` | 27:Out → 10:In; 27:Out → 14:In; 26:Out → 27:Active; 27:Out → 33:In; 27:Out → 32:In; 27:Out → 31:In; 27:Out → 34:In |
| `mq050.questphase / h0 / 29` (Journal) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/get_inside_car` | 40:Out → 29:Succeeded; 29:Out → 30:Succeeded |
| `mq050.questphase / h0 / 30` (Journal) | `quests/minor_quest/mq050_ken_block_tribute` | 29:Out → 30:Succeeded; 30:Out → 43:In |
| `mq050_bugfixing.questphase / h14 / 4` (Condition) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/investigate` | 2:Out → 4:In; 4:True → 18:In; 4:False → 17:In |
| `mq050_bugfixing.questphase / h14 / 17` (Condition) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/get_inside_car` | 4:False → 17:In; 17:True → 18:In |
| `mq050_bugfixing.questphase / h14 / 20` (Condition) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/get_inside_car` | 33:Out → 20:In; 20:True → 25:In; 20:True → 24:In; 20:True → 23:In; 20:True → 22:In; 20:True → 21:In; 20:True → 30:In |
| `mq050_johnny_start.scene / scene / 55` (PauseCondition) | `quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/investigate` | 55:0:0 → 58:0:0; 79:0:0 → 55:0:1; input mappings: 0:0=CutDestination, 0:1=In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq050.questphase / h0 / 55` | `base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene`; `#mq050_sm_johnny_start` | 55:ContinueQuest → 23:Active; 72:Out → 55:Start 0; 59:Out → 55:Prefetch |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\mq050\mq050.questphase` / h0 / 55 | `mq050_johnny_start.scene` | 72: PauseCondition: #mq050_tr_start; 59: PauseCondition: #mq050_tr_spawn; 55:ContinueQuest → 23:Active; 72:Out → 55:Start 0; 59:Out → 55:Prefetch |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq050_johnny_start.scene` | Start 0 → End 0, ContinueQuest | johnny; Player; 16 nodes / 18 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CP77-64925` | mq050_bugfixing.questphase / h14 / 2 | mq050_bugfixing.questphase / h14 / 3 |
| `travelling_merchant_lives` | Producer outside selected context | mq050_bugfixing.questphase / h0 / 2 |

## Exact gates, joins and cancellation

<details><summary>29 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq050.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq050_tr_spawn"}}` | 0:Out → 3:In; 3:Out → 11:In |
| `mq050.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleName":"Vehicle.v_sport2_quadra_type66_nomad_tribute","vehicleGlobalName":"#mq050_vehicle"}}}` | 11:Out → 8:In; 8:Out → 36:In; 8:Out → 59:In; 8:Out → 67:In |
| `mq050.questphase / h0 / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq050_vehicle"},"childIsPlayer":true}}}` | 40:Out → 15:In; 40:Out → 28:In; 40:Out → 29:Succeeded; 41:Out → 40:In; 42:True → 40:In; 40:Out → 89:In; 40:Out → 88:In |
| `mq050.questphase / h0 / 42` | `questConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleName":"Vehicle.v_sport2_quadra_type66_nomad_tribute","vehicleGlobalName":"#mq050_vehicle"}}}` | 14:Out → 42:In; 42:True → 40:In; 42:False → 41:In |
| `mq050.questphase / h0 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq050_tr_spawn"}}` | 8:Out → 59:In; 59:Out → 55:Prefetch |
| `mq050.questphase / h0 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType","tickCount":100}}}` | 65:Out → 66:In |
| `mq050.questphase / h0 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq050_main_loot"},"timeInterval":0.10000000149011612,"onScreenTest":true}}}` | 8:Out → 67:In; 67:Out → 51:In |
| `mq050.questphase / h0 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#mq050_tr_start"},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq050_vehicle"},"onScreenTest":true}}]}}` | 12:Out → 72:In; 72:Out → 55:Start 0 |
| `mq050.questphase / h0 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 74:Out → 12:In; 70:Out → 74:In |
| `mq050.questphase / h0 / 76` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq050_tr_reactivate_physics"}}` | 75:Out → 76:In; 76:Out → 77:In |
| `mq050.questphase / h0 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 77:Out → 70:In; 76:Out → 77:In |
| `mq050.questphase / h0 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"99716362400","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 81:Out → 80:In; 80:Out → 84:In1 |
| `mq050.questphase / h0 / 84` | `questLogicalXorNodeDefinition` `{}` | 84:Out1 → 26:Succeeded; 80:Out → 84:In1; 87:Out → 84:In2 |
| `mq050.questphase / h0 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mq050_vehicle"},"childIsPlayer":true}}}` | 81:Out → 87:In; 87:Out → 84:In2 |
| `mq050_bugfixing.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 2:In |
| `mq050_bugfixing.questphase / h14 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-64925"}}}` | 0:Out → 3:In; 3:False → 2:In |
| `mq050_bugfixing.questphase / h14 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/investigate","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 4:In; 4:True → 18:In; 4:False → 17:In |
| `mq050_bugfixing.questphase / h14 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 12:Out → 7:In; 11:Out → 12:In |
| `mq050_bugfixing.questphase / h14 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq050_tr_reactivate_physics"}}` | 13:Out → 14:In; 14:Out → 15:In |
| `mq050_bugfixing.questphase / h14 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 15:Out → 11:In; 14:Out → 15:In |
| `mq050_bugfixing.questphase / h14 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/get_inside_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 4:False → 17:In; 17:True → 18:In |
| `mq050_bugfixing.questphase / h14 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleName":"Vehicle.v_sport2_quadra_type66_nomad_tribute","vehicleGlobalName":"#mq050_vehicle"}}}` | 5:Out → 19:In; 19:Out → 10:In |
| `mq050_bugfixing.questphase / h14 / 20` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/get_inside_car","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 33:Out → 20:In; 20:True → 25:In; 20:True → 24:In; 20:True → 23:In; 20:True → 22:In; 20:True → 21:In; 20:True → 30:In |
| `mq050_johnny_start.scene / scene / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 15:0:0 → 79:0:0; 65:0:0 → 15:0:1 |
| `mq050_johnny_start.scene / scene / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq050_johnny_start_johnny"},"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 17:0:0 → 19:0:1; 58:0:0 → 17:0:1; 69:0:0 → 17:0:1 |
| `mq050_johnny_start.scene / scene / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq050_johnny_start_johnny"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 4:0:1 → 42:0:1; 42:0:0 → 21:666:1 |
| `mq050_johnny_start.scene / scene / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq050_johnny_start_johnny"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"Less"}},{"$type":"questTriggerCondition","triggerAreaRef":"#mq050_tr_start"}]}}` | 52:0:0 → 69:0:0; 58:1:0 → 52:0:0; 79:0:0 → 52:0:1 |
| `mq050_johnny_start.scene / scene / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq050_ken_block_tribute/mq050_warehouse/investigate","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 55:0:0 → 58:0:0; 79:0:0 → 55:0:1 |
| `mq050_johnny_start.scene / scene / 74` | `questConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq050_johnny_start_johnny"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0}}}}` | 21:666:0 → 74:0:1; 74:0:0 → 65:0:0; 74:0:1 → 79:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq050_johnny_start.scene / scene / 42 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `conditional_route` | mq050_bugfixing.questphase / h0 / 2; mq050_bugfixing.questphase / h14 / 3 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `item_state` | mq050.questphase / h0 / 80 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `mount_state` | mq050.questphase / h0 / 40; mq050.questphase / h0 / 87 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `persistent_decision` | mq050_bugfixing.questphase / h14 / 2 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq050.questphase / h0 / 84 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq050.questphase / h0 / 74; mq050.questphase / h0 / 77; mq050_bugfixing.questphase / h14 / 12; mq050_bugfixing.questphase / h14 / 15; +1 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `scene_interface` | mq050.questphase / h0 / 55 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `vehicle_control` | mq050.questphase / h0 / 10; mq050.questphase / h0 / 11; mq050.questphase / h0 / 12; mq050.questphase / h0 / 14; +33 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq050_johnny_start.scene / scene / 19; mq050_johnny_start.scene / scene / 4 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\minor_quests\mq050\mq050.questphase` | content candidate; journal anchor | `base-mq050` |
| `base\quest\minor_quests\mq050\mq050_bugfixing.questphase` | repair; journal anchor | `base-mq050` |
| `base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene` | content candidate; journal anchor | `base-mq050` |

Evidence shards for this dossier (including parent context): [base-mq050](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq050.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
