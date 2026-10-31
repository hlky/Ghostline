# Money For Nothing

Journal: `ep1/quests/minor_quest/sts_ep1_08_loot_pickup` · `MinorQuest` · hash `1379134557`.

Journal premise: Ex-SovOil agent, stashin' her goods in D-town… Big cloud, little rain, I say. But don't let my inner cynic stop ya, V. Go find that stash.

**Coverage: journal-linked.** 11 exact journal-linked nodes in 3 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Go to Katya's stash. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` |
| Find Katya's stash. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_ep1_08_bugfixing.questphase / h106 / 4` (Condition) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/description` | 3:Out → 4:In; 4:True → 5:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 5` (Condition) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` | 4:True → 5:In; 5:True → 6:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 6` (Condition) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates` | 5:True → 6:In; 6:True → 9:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 7` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` | 9:Out → 7:Active; 7:Out → 11:In |
| `sts_ep1_08_target_meeting.scene / scene / 1397` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` | 1397:0:0 → 1537:0:1; 1533:0:0 → 1397:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sts_ep1_08_target_meeting.scene / scene / 1537` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/description` | 1397:0:0 → 1537:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wst_ep1_21.questphase / h0 / 27` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` | 41:Out → 27:Succeeded; 27:Out → 28:Active |
| `wst_ep1_21.questphase / h0 / 28` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates` | 27:Out → 28:Active; 28:Out → 39:In |
| `wst_ep1_21.questphase / h0 / 29` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates` | 4:Out → 29:Succeeded; 29:Out → 31:Succeeded |
| `wst_ep1_21.questphase / h0 / 30` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup` | 30:Out → 22:In; 31:Out → 30:Succeeded |
| `wst_ep1_21.questphase / h0 / 31` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash` | 29:Out → 31:Succeeded; 31:Out → 30:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h33 / 9 | `sts_ep1_08_bugfixing.questphase` | 0: Input; 0:Out → 9:In1 |
| `ep1\openworld\street_stories\ep1_street_stories.questphase` / h558 / 7 | `sts_ep1_08_bugfixing.questphase` | 0: Input; 0:Out → 7:In1 |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase` / h0 / 67 | `sts_ep1_08_target_meeting.scene` | 153: PauseCondition: {"seconds": 2}; 153:Out → 67:Bana intro; 67:phone end 01 → 380:In |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase` / h0 / 201 | `sts_ep1_08_target_meeting.scene` | 206: Input; 474: LogicalHub; 340: LogicalHub; 206:Out → 201:Meeting; 474:Out1 → 201:Meeting; 340:Out1 → 201:katya dead comment; 201:dead → 402:In1; 201:friendly → 402:In1; 201:katya killed before order → 340:In1; 201:katya killed before order → 402:In1 |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase` / h0 / 283 | `sts_ep1_08_target_meeting.scene` | 419: Condition; 283:eliminate enemies end → 232:Inactive; 419:False → 283:eliminate enemies |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase` / h0 / 285 | `sts_ep1_08_target_meeting.scene` | 366: PauseCondition: {"seconds": 2}; 285:meeting_point → 255:In; 366:Out → 285:enemies defeated; 285:meeting_point → 453:In |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest` / h0 / 10 | `wst_ep1_21.questphase` | 11: LogicalHub; 11:Out1 → 10:debug |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 21 | `wst_ep1_21.questphase` | 40: PauseCondition: wst_ep1_21_active; 40:Out → 21:In1 |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 3 | `ep1_openworld_bugfixing.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 2 | `ep1_street_stories.questphase` | 33: PauseCondition: ep1_side_content GreaterOrEqual 1; 33:Out → 2:In1 |
| `ep1\openworld\street_stories\ep1_street_stories.questphase` / h13 / 23 | `sts_ep1_08_phase.questphase` | 17: Journal; 17:Out → 23:Start; 23:Organitopia done → 36:In; 23:Out1 → 31:In |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest` / h0 / 0 | `sts_ep1_08_phase.questphase` | 6: Scene: sts_ep1_08_chicken_test.scene; 6: Scene: sts_ep1_08_chicken_test.scene; 6: Scene: sts_ep1_08_chicken_test.scene; 6: Scene: sts_ep1_08_chicken_test.scene; 6: Scene: sts_ep1_08_chicken_test.scene; 0:Organitopia done → 18:Organitopia cleanup; 6:Start → 0:Start; 6:Botanic garden entrance → 0:Botanic garden entrance; 0:Out1 → 18:In1; 6:boss fight → 0:Boss fight; 6:Client final meeting → 0:client final meeting; 6:Meeting Katya → 0:Katya meeting |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 14 | `ep1_world_stories.questphase` | 11: LogicalHub; 11:Out1 → 14:In1 |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest` / h0 / 7 | `ep1_world_stories.questphase` | 3: PauseCondition: {"seconds": 2}; 3:Out → 7:In1 |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest` / h0 / 112 | `ep1_world_stories.questphase` | 118: PauseCondition: sts_ep1_06_close_club; 118:Out → 112:In1 |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest` / h0 / 13 | `ep1_world_stories.questphase` | 7: PauseCondition: {"seconds": 2}; 7:Out → 13:In1 |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest` / h0 / 19 | `ep1_world_stories.questphase` | 3: FactsDBManager: ep1_12_test_def; 3:Out → 19:In1 |
| `ep1\quest\ep1.questphase` / h58 / 2 | `ep1_bugfixing.questphase` | 25: LogicalXor; 2:CP77-65722_out → 27:In; 2:CP77-64292_out → 26:In; 25:Out1 → 2:In1; 2:Out1 → 4:In2; 2:growl → 4:growl |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 12 | `ep1_bugfixing.questphase` | 11: LogicalHub; 11:Out1 → 12:In1 |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 5 | `ep1_bugfixing.questphase` | 4: LogicalHub; 4:Out1 → 5:In1 |
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
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 16 | `vehicle_metaquest_ep1_bugfixing.questphase` | 0: Input; 0:Out → 16:In1 |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sts_ep1_08_target_meeting.scene` | Bana intro, fake input to keep lines alive, Start 11, Meeting, eliminate enemies, katya dead comment, enemies defeated → dead, meeting_point, friendly, phone end 01, eliminate enemies end, End 12,  enemies defeated end, katya killed before order | target; bana_voice; Ana; bana_impersonated; Player; 248 nodes / 274 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CP77-60274` | sts_ep1_08_bugfixing.questphase / h15 / 26 | No reader in selected context |
| `CP77-63629` | sts_ep1_08_bugfixing.questphase / h106 / 3 | sts_ep1_08_bugfixing.questphase / h106 / 2 |
| `sts_ep1_08_active` | Producer outside selected context | sts_ep1_08_bugfixing.questphase / h15 / 19 |
| `sts_ep1_08_boss_appears` | Producer outside selected context | sts_ep1_08_bugfixing.questphase / h15 / 13 |
| `sts_ep1_08_boss_holograms_clean_up` | Producer outside selected context | sts_ep1_08_bugfixing.questphase / h15 / 23 |
| `travelling_merchant_lives` | Producer outside selected context | sts_ep1_08_bugfixing.questphase / h0 / 23; wst_ep1_21.questphase / h0 / 43 |
| `wst_ep1_21_active` | sts_ep1_08_bugfixing.questphase / h106 / 9; sts_ep1_08_target_meeting.scene / scene / 1533 | No reader in selected context |
| `wst_ep1_21_done` | wst_ep1_21.questphase / h0 / 22 | No reader in selected context |
| `wst_ep1_21_finished` | wst_ep1_21.questphase / h0 / 35 | No reader in selected context |
| `wst_ep1_21_start` | wst_ep1_21.questphase / h0 / 21 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>18 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_ep1_08_bugfixing.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":999}}}` | 24:Out → 23:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","inverted":true}}}` | 12:Out → 9:In; 13:Out → 9:In; 9:Out → 10:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType"}}}` | 10:Out → 11:In; 11:Out → 12:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 12:Out → 9:In; 11:Out → 12:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_boss_appears","value":1,"comparisonType":"GreaterOrEqual"}}}` | 13:Out → 9:In; 19:True → 13:In; 13:Out → 23:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 19` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 19:True → 13:In; 26:Out → 19:In; 19:False → 25:In1 |
| `sts_ep1_08_bugfixing.questphase / h15 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_boss_holograms_clean_up","value":1,"comparisonType":"GreaterOrEqual"}}}` | 23:Out → 1:In; 13:Out → 23:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-63629"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/sts_ep1_08_loot_pickup/description","fileEntryIndex":2,"className":"gameJournalQuestDescription"},"state":"Active"}}}` | 3:Out → 4:In; 4:True → 5:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Inactive"}}}` | 4:True → 5:In; 5:True → 6:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Inactive"}}}` | 5:True → 6:In; 6:True → 9:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_21_search_trigger"}}` | 7:Out → 11:In; 11:True → 12:In |
| `wst_ep1_21.questphase / h0 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#wst_ep1_21_katya_loot","eventType":"Executed"}}}` | 51:Out → 4:In; 4:Out → 29:Succeeded |
| `wst_ep1_21.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#wst_ep1_21_com","names":["vehicle"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0}}}}` | 35:Out → 18:In; 18:Out → 25:In |
| `wst_ep1_21.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_21_search_trigger"}}` | 23:Out → 21:In; 24:Out → 23:In |
| `wst_ep1_21.questphase / h0 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/container_zone_prefab4PZIADQ/container_zone_world_stories_prefab4SY6XVQ/wst_ep1_21_prefabQRZL7KY/wst_ep1_21_gameplay_prefabXEJQVRA/wst_ep1_21_devices_prefabWTHKHJY/movable_dumpster_prefab66MQPEQ/movable_device_rack_prefabBQFFUUY"},"eventType":"Finished"}}}` | 24:Out → 36:In; 36:Out → 37:In |
| `wst_ep1_21.questphase / h0 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/container_zone_prefab4PZIADQ/container_zone_world_stories_prefab4SY6XVQ/wst_ep1_21_prefabQRZL7KY/wst_ep1_21_gameplay_prefabXEJQVRA/wst_ep1_21_devices_prefabWTHKHJY/movable_dumpster_prefab66MQPEQ/movable_device_rack_prefabBQFFUUY","eventType":"Executed"}}}` | 28:Out → 39:In; 39:Out → 42:In |
| `wst_ep1_21.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":999}}}` | 0:Out → 43:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `checkpoint` | sts_ep1_08_bugfixing.questphase / h15 / 10 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `conditional_route` | sts_ep1_08_bugfixing.questphase / h0 / 23; sts_ep1_08_bugfixing.questphase / h106 / 2; sts_ep1_08_bugfixing.questphase / h15 / 13; sts_ep1_08_bugfixing.questphase / h15 / 19; +2 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | wst_ep1_21.questphase / h0 / 37 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | wst_ep1_21.questphase / h0 / 48; wst_ep1_21.questphase / h0 / 50; wst_ep1_21.questphase / h0 / 51 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `journal_transition` | sts_ep1_08_bugfixing.questphase / h106 / 7; sts_ep1_08_target_meeting.scene / scene / 1397; sts_ep1_08_target_meeting.scene / scene / 1537; wst_ep1_21.questphase / h0 / 27; +4 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | sts_ep1_08_bugfixing.questphase / h106 / 3; sts_ep1_08_bugfixing.questphase / h106 / 9; sts_ep1_08_bugfixing.questphase / h15 / 26; sts_ep1_08_target_meeting.scene / scene / 1533; +3 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sts_ep1_08_bugfixing.questphase / h15 / 12 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `scan_evidence` | wst_ep1_21.questphase / h0 / 36 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `spatial_gate` | sts_ep1_08_bugfixing.questphase / h106 / 11; wst_ep1_21.questphase / h0 / 23 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `world_variant` | wst_ep1_21.questphase / h0 / 24; wst_ep1_21.questphase / h0 / 25; wst_ep1_21.questphase / h0 / 3; wst_ep1_21.questphase / h0 / 33 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_bugfixing.questphase` | repair; journal anchor | `ep1-sts-ep1-08` |
| `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_target_meeting.scene` | content candidate; journal anchor | `ep1-sts-ep1-08` |
| `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` | content candidate; journal anchor | `ep1-wst-ep1-21` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq306.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-01](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-01.json.gz), [ep1-sts-ep1-06-zembinsky](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-06-zembinsky.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-08.json.gz), [ep1-sts-ep1-10](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-10.json.gz), [ep1-sts-ep1-12](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-12.json.gz), [ep1-wst-ep1-21](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-wst-ep1-21.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

38 repeated typed/socket path signatures in this selected graph context; 21 distinct direct resource identities; 2 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `c8705a8da51824b73252` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_bugfixing.questphase` / h15 / 0 -> 26 -> 19 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `eaf5aab427d50e5598b6` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_bugfixing.questphase` / h106 / 0 -> 2 -> 3 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `cbae0fd3078e68426197` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_bugfixing.questphase` / h0 / 21 -> 24 -> 23 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `9380dda43f90ecd62efb` | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 48 -> 50 -> 51 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out -> In; Out -> In |
| `bfe95df47bd1ca67330f` | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 3 -> 33 -> 24 | questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]; Out -> In; Out -> In |
| `1d48bd7cbbaeca8257d2` | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 31 -> 30 -> 22 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Succeeded; Out -> In |
| `6b1fcb4c46676ba8a912` | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 30 -> 22 -> 35 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `f4c2b3190230913ea05b` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_bugfixing.questphase` / h106 / 2 -> 3 -> 4 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; False -> In; Out -> In |
| `3457629da944eac3b4b2` | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 0 -> 3 -> 33 | questInputNodeDefinition -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]; Out -> In; Out -> In |
| `163b243e32c0bb8c4eb7` | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 33 -> 24 -> 23 | questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `2fef53694f4256108f17` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_bugfixing.questphase` / h15 / 26 -> 19 -> 25 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questLogicalHubNodeDefinition; Out -> In; False -> In1 |
| `c4cc47f1088342201da5` | `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` / h0 / 29 -> 31 -> 30 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Succeeded |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_bugfixing.questphase` / h0 / 19 | `h15` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_bugfixing.questphase` / h0 / 25 | `h106` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_nc_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10_def.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_stand_2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__2h_up__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_bar__2h_on_keyboard__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\open_world\generic_female_average_work__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\workspots\bar\bar\generic__stand_bar_keyboard__work__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__afraid__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stretch__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__wait_nervous__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `ep1\animations\quest\sts_quests\sts_ep1_08\sts_ep1_08__target_meet__female_anims.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\openworld\street_stories\sts_ep1_08\scenes\lipsync\en\sts_ep1_08_target_meeting\ana_friedman.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\openworld\street_stories\sts_ep1_08\scenes\lipsync\en\sts_ep1_08_target_meeting\katya_karelina.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\openworld\street_stories\sts_ep1_08\scenes\lipsync\en\sts_ep1_08_target_meeting\mark_bana.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\openworld\street_stories\sts_ep1_08\scenes\lipsync\en\sts_ep1_08_target_meeting\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\workspots\quest\sts_quests\sts_ep1_08\sts_ep1_08__katya_sitting_wounded__01.workspot` | performance binding | ep1/ep1_1_nightcity.archive; index evidence only |
| `ep1\workspots\quest\sts_quests\sts_ep1_08\sts_ep1_08__stand__2h_hands_up__01.workspot` | performance binding | ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `sts_ep1_08_active` | ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase / h0 / 328; ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase / h0 / 329; 2 total source locations in compressed evidence |
| `sts_ep1_08_boss_appears` | ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_gameplay.questphase / h393 / 56; ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_enemies_chats.scene / scene / 106; 2 total source locations in compressed evidence |
| `sts_ep1_08_boss_holograms_clean_up` | ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_gameplay.questphase / h3850 / 6; 1 total source locations in compressed evidence |

NodeRef uses: 27; TweakDB binding uses: 5. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_target_meeting.scene` | 39 / 184 | scnAudioEvent: 1; scnChangeIdleAnimEvent: 8; scnDialogLineEvent: 71; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtAdvancedEvent: 3; scnLookAtEvent: 25; scnPlaySkAnimEvent: 22; scnPoseCorrectionEvent: 2; scnUnmountEvent: 1; scneventsAttachPropToNode: 1; scneventsAttachPropToPerformer: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 39; scneventsVFXDurationEvent: 3; scneventsVFXEvent: 3 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
