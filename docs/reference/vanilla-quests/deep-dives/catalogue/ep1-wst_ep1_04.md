# Addicted To Chaos

Journal: `ep1/quests/minor_quest/wst_ep1_04` · `MinorQuest` · hash `2722260217`.

**Coverage: journal-linked.** 11 exact journal-linked nodes in 2 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Enter code 1975 to open the garage. (Primary) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/enter_the_code` |
| Go to Rinder’s stash. (Primary) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/go_to_rinders_garage` |
| Take Rinder’s things. (Primary) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/loot_the_box` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `wst_ep1_04.questphase / h0 / 6` (Journal) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/go_to_rinders_garage` | 20:Out → 6:Active; 6:Out → 13:In |
| `wst_ep1_04.questphase / h0 / 8` (Journal) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/go_to_rinders_garage` | 35:Out → 8:Succeeded; 8:Out → 29:Active |
| `wst_ep1_04.questphase / h0 / 9` (Journal) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/loot_the_box` | 32:Out → 9:Active; 9:Out → 46:In |
| `wst_ep1_04.questphase / h0 / 10` (Journal) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/loot_the_box` | 3:Out → 10:Succeeded; 10:Out → 14:Succeeded |
| `wst_ep1_04.questphase / h0 / 14` (Journal) | `ep1/quests/minor_quest/wst_ep1_04` | 10:Out → 14:Succeeded; 14:Out → 28:In |
| `wst_ep1_04.questphase / h0 / 21` (Journal) | `ep1/quests/minor_quest/wst_ep1_04/description` | 20:Out → 21:Active |
| `wst_ep1_04.questphase / h0 / 29` (Journal) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/enter_the_code` | 8:Out → 29:Active; 29:Out → 38:In |
| `wst_ep1_04.questphase / h0 / 31` (Journal) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/enter_the_code` | 31:Out → 1:In; 37:Out → 31:Succeeded |
| `wst_ep1_04_bugfixing.questphase / h31 / 4` (Condition) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/enter_the_code` | 9:False → 4:In; 4:False → 5:In |
| `wst_ep1_04_bugfixing.questphase / h31 / 5` (Condition) | `ep1/quests/minor_quest/wst_ep1_04` | 4:False → 5:In; 5:True → 6:Active |
| `wst_ep1_04_bugfixing.questphase / h31 / 6` (Journal) | `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/enter_the_code` | 6:Out → 1:In; 5:True → 6:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 4 | `wst_ep1_04.questphase` | 46: PauseCondition: sts_ep1_03_dogtag_obtained; 46:Out → 4:In1 |
| `ep1\openworld\world_stories\ep1_world_stories_bugfixing.questphase` / h0 / 3 | `wst_ep1_04_bugfixing.questphase` | 8: DeletionMarker; 8:Out → 3:In1 |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 14 | `ep1_world_stories.questphase` | 11: LogicalHub; 11:Out1 → 14:In1 |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 18 | `ep1_world_stories_bugfixing.questphase` | 0: Input; 0:Out → 18:In1 |
| `ep1\openworld\vendors\vehicle_metaquest\phases\vehicle_metaquest_ep1_bugfixing.questphase` / h17 / 6 | `ep1_open_world.questphase` | 4: Condition: militech_hellhound_available; 4:False → 6:CP77-63752 |
| `ep1\quest\ep1.questphase` / h58 / 5 | `ep1_open_world.questphase` | 0: Input; 9: CutControl; 0:Out → 5:In1; 9:CutSource → 5:CutDestination |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 3 | `ep1_openworld_bugfixing.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 16 | `vehicle_metaquest_ep1_bugfixing.questphase` | 0: Input; 0:Out → 16:In1 |
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
| `CP77-58786` | wst_ep1_04_bugfixing.questphase / h31 / 3 | wst_ep1_04_bugfixing.questphase / h31 / 2 |
| `travelling_merchant` | Producer outside selected context | wst_ep1_04_bugfixing.questphase / h0 / 14 |
| `travelling_merchant_lives` | Producer outside selected context | wst_ep1_04.questphase / h0 / 34 |
| `wst_ep1_04_active` | wst_ep1_04.questphase / h0 / 20 | wst_ep1_04_bugfixing.questphase / h31 / 8 |
| `wst_ep1_04_finished` | wst_ep1_04.questphase / h0 / 3 | wst_ep1_04_bugfixing.questphase / h31 / 9 |
| `wst_ep1_04_gun_taken` | wst_ep1_04.questphase / h0 / 22 | No reader in selected context |
| `wst_ep1_04_start` | wst_ep1_04.questphase / h0 / 1 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>17 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `wst_ep1_04.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_04_tr_doors"}}` | 6:Out → 13:In; 13:Out → 19:In |
| `wst_ep1_04.questphase / h0 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"169147537243"}}}` | 24:Out → 22:In; 45:Out → 24:In |
| `wst_ep1_04.questphase / h0 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_04_tr_doors"},{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","hours":2}}]}}` | 14:Out → 28:In; 28:Out → 27:In |
| `wst_ep1_04.questphase / h0 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":999}}}` | 0:Out → 34:In |
| `wst_ep1_04.questphase / h0 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 11:Out → 36:In; 36:Out → 35:In |
| `wst_ep1_04.questphase / h0 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/high_peak_prefabAMBSEZY/high_peak_world_stories_prefabLBAXJZY/wst_ep1_04_prefabA4BGGJY/wst_ep1_04_gameplay_prefabNJMFDFQ/wst_ep1_04_devices_prefabMPVHGCQ/d_scav_b_t_1_eng_001_prefabFOAHXCY/door1","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 37:Out → 31:Succeeded; 41:Out → 37:In |
| `wst_ep1_04.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/high_peak_prefabAMBSEZY/high_peak_world_stories_prefabLBAXJZY/wst_ep1_04_prefabA4BGGJY/wst_ep1_04_gameplay_prefabNJMFDFQ/wst_ep1_04_devices_prefabMPVHGCQ/d_scav_b_t_1_eng_001_prefabFOAHXCY/{terminal_}1_prefabUSP7VVI"}}` | 38:Out → 43:In; 43:Out → 39:In |
| `wst_ep1_04.questphase / h0 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#wst_ep1_04_main_loot","eventType":"Executed"}}}` | 45:Out → 3:In; 45:Out → 24:In; 46:Out → 45:In |
| `wst_ep1_04.questphase / h0 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#wst_ep1_04_main_loot"}}` | 46:Out → 47:In; 47:Out → 48:In; 47:Out → 50:In |
| `wst_ep1_04.questphase / h0 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType","tickCount":10}}}` | 47:Out → 48:In; 48:Out → 49:In |
| `wst_ep1_04.questphase / h0 / 50` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/high_peak_prefabAMBSEZY/high_peak_world_stories_prefabLBAXJZY/wst_ep1_04_prefabA4BGGJY/wst_ep1_04_gameplay_prefabNJMFDFQ/wst_ep1_04_devices_prefabMPVHGCQ/d_scav_b_t_1_eng_001_prefabFOAHXCY/door1","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsUnpowered"}}}` | 47:Out → 50:In; 50:True → 51:In |
| `wst_ep1_04_bugfixing.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant","value":9999}}}` |  |
| `wst_ep1_04_bugfixing.questphase / h31 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-58786"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `wst_ep1_04_bugfixing.questphase / h31 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/enter_the_code","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 9:False → 4:In; 4:False → 5:In |
| `wst_ep1_04_bugfixing.questphase / h31 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/wst_ep1_04","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 4:False → 5:In; 5:True → 6:Active |
| `wst_ep1_04_bugfixing.questphase / h31 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_04_active"}}}` | 3:Out → 8:In; 8:True → 9:In |
| `wst_ep1_04_bugfixing.questphase / h31 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_04_finished"}}}` | 9:False → 4:In; 8:True → 9:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `conditional_route` | wst_ep1_04.questphase / h0 / 34; wst_ep1_04_bugfixing.questphase / h0 / 14; wst_ep1_04_bugfixing.questphase / h31 / 2; wst_ep1_04_bugfixing.questphase / h31 / 8; +1 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | wst_ep1_04.questphase / h0 / 11; wst_ep1_04.questphase / h0 / 25; wst_ep1_04.questphase / h0 / 27; wst_ep1_04.questphase / h0 / 35; +6 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | wst_ep1_04.questphase / h0 / 37; wst_ep1_04.questphase / h0 / 50 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `item_state` | wst_ep1_04.questphase / h0 / 24 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `persistent_decision` | wst_ep1_04.questphase / h0 / 1; wst_ep1_04.questphase / h0 / 20; wst_ep1_04.questphase / h0 / 22; wst_ep1_04.questphase / h0 / 3; +1 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | wst_ep1_04.questphase / h0 / 28; wst_ep1_04.questphase / h0 / 36 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `vehicle_control` | wst_ep1_04.questphase / h0 / 19 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` | content candidate; journal anchor | `ep1-wst-ep1-04` |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` | repair; journal anchor | `ep1-wst-ep1-04` |

Evidence shards for this dossier (including parent context): [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz), [ep1-wst-ep1-04](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-wst-ep1-04.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
