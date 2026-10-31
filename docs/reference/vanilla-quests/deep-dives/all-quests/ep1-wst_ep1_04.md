# Addicted To Chaos

Journal: `ep1/quests/minor_quest/wst_ep1_04` · `MinorQuest` · hash `2722260217`.

Journal premise: Go on, V. Time to see if your deal with a homicidal psychopath was worth it.

**Coverage: journal-linked.** 11 exact journal-linked nodes in 2 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

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
| `ep1\openworld\street_stories\sts_ep1_03\sts_ep1_03.quest` / h0 / 8 | `wst_ep1_04.questphase` | 6: Scene: sts_ep1_03_chicken_test.scene; 6:wst_ep1_04 → 8:chickentest |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 4 | `wst_ep1_04.questphase` | 46: PauseCondition: sts_ep1_03_dogtag_obtained; 46:Out → 4:In1 |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.quest` / h0 / 2 | `wst_ep1_04.questphase` | 0: Start; 0:Out → 2:chickentest |
| `ep1\openworld\world_stories\ep1_world_stories_bugfixing.questphase` / h0 / 3 | `wst_ep1_04_bugfixing.questphase` | 8: DeletionMarker; 8:Out → 3:In1 |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 14 | `ep1_world_stories.questphase` | 11: LogicalHub; 11:Out1 → 14:In1 |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest` / h0 / 7 | `ep1_world_stories.questphase` | 3: PauseCondition: {"seconds": 2}; 3:Out → 7:In1 |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest` / h0 / 112 | `ep1_world_stories.questphase` | 118: PauseCondition: sts_ep1_06_close_club; 118:Out → 112:In1 |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest` / h0 / 13 | `ep1_world_stories.questphase` | 7: PauseCondition: {"seconds": 2}; 7:Out → 13:In1 |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest` / h0 / 19 | `ep1_world_stories.questphase` | 3: FactsDBManager: ep1_12_test_def; 3:Out → 19:In1 |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 18 | `ep1_world_stories_bugfixing.questphase` | 0: Input; 0:Out → 18:In1 |
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
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 3 | `ep1_openworld_bugfixing.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 16 | `vehicle_metaquest_ep1_bugfixing.questphase` | 0: Input; 0:Out → 16:In1 |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |
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
| `controller_event` | wst_ep1_04.questphase / h0 / 32 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | wst_ep1_04.questphase / h0 / 11; wst_ep1_04.questphase / h0 / 25; wst_ep1_04.questphase / h0 / 27; wst_ep1_04.questphase / h0 / 35; +6 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | wst_ep1_04.questphase / h0 / 37; wst_ep1_04.questphase / h0 / 50 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `item_state` | wst_ep1_04.questphase / h0 / 24 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | wst_ep1_04.questphase / h0 / 10; wst_ep1_04.questphase / h0 / 14; wst_ep1_04.questphase / h0 / 21; wst_ep1_04.questphase / h0 / 29; +5 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | wst_ep1_04.questphase / h0 / 49 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `persistent_decision` | wst_ep1_04.questphase / h0 / 1; wst_ep1_04.questphase / h0 / 20; wst_ep1_04.questphase / h0 / 22; wst_ep1_04.questphase / h0 / 3; +1 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | wst_ep1_04.questphase / h0 / 28; wst_ep1_04.questphase / h0 / 36 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `spatial_gate` | wst_ep1_04.questphase / h0 / 13; wst_ep1_04.questphase / h0 / 28 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | wst_ep1_04.questphase / h0 / 19 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` | content candidate; journal anchor | `ep1-wst-ep1-04` |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` | repair; journal anchor | `ep1-wst-ep1-04` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq306.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-01](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-01.json.gz), [ep1-sts-ep1-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-03.json.gz), [ep1-sts-ep1-06-zembinsky](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-06-zembinsky.json.gz), [ep1-sts-ep1-10](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-10.json.gz), [ep1-sts-ep1-12](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-12.json.gz), [ep1-wst-ep1-04](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-wst-ep1-04.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

28 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 1 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `eaf5aab427d50e5598b6` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` / h31 / 0 -> 2 -> 3 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `9380dda43f90ecd62efb` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 39 -> 40 -> 53 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out -> In; Out -> In |
| `5c76d3bf7160f29b884f` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` / h31 / 2 -> 3 -> 8 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; False -> In; Out -> In |
| `0781ef00ea04c05ee418` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 8 -> 29 -> 38 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questDeletionMarkerNodeDefinition; Out -> Active; Out -> In |
| `8dd5c44ffdb3cb8886ef` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` / h31 / 3 -> 8 -> 9 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; True -> In |
| `9890c704bd8503fd1750` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 11 -> 36 -> 35 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out -> In; Out -> In |
| `7a88801c0d5664236a9c` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 9 -> 46 -> 45 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]; Out -> In; Out -> In |
| `bf9c73a58053b668d2fb` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 0 -> 20 -> 6 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Active |
| `2face0cc90a9b0fee909` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 35 -> 8 -> 29 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `6cbd4aaf3157582f705c` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 29 -> 38 -> 43 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questNodeLoadingCondition]; Out -> In; Out -> In |
| `19a35d27ae1aaa1f92ef` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 3 -> 10 -> 14 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Succeeded |
| `b5032542f6cc4ccd2d26` | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 20 -> 6 -> 13 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> Active; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` / h0 / 16 | `h31` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `ep1\openworld\street_stories\sts_ep1_03\sts_ep1_03_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_03\sts_ep1_03.quest |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10_def.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.gamedef` | content candidate | ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.quest |

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

NodeRef uses: 20; TweakDB binding uses: 2. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
