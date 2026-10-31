# Sex On Wheels

Journal: `quests/minor_quest/mq044_jakes_vehicle` · `MinorQuest` · hash `522295962`.

**Coverage: journal-linked.** 14 exact journal-linked nodes in 2 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

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
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 60 | `mq044_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 60:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase` / h168 / 5 | `mq044_main.questphase` | 4: PauseCondition: {"days": 1}; 5:Out1 → 1:In; 4:Out → 5:In1 |
| `base\quest\minor_quests\mq044\phases\mq044.questphase` / h0 / 2 | `mq044_main.questphase` | 4: PauseCondition; 2:Out1 → 1:In; 4:Out → 2:In1 |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\open_world\bugfixing\sts\sts_glen_bugfixing.questphase` / h0 / 13 | `sts_hey_gle_06_bugfixing.questphase` | 15: DeletionMarker; 15:Out → 13:In1 |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 149 | `mq044.questphase` | 150: PauseCondition: {"days": 3}; 150:Out → 149:In1 |
| `base\quest\minor_quests\mq044\mq044.quest` / h0 / 0 | `mq044.questphase` | 3: FactsDBManager: gle_06_succeed; 3:Out → 0:In1; 0:Out1 → 1:In |
| `base\quest\cyberpunk2077.questphase` / h520 / 4 | `bugfixing.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:Out_res_act1 → 14:In; 4:to_mq025 → 6:to_mq025; 4:sq026_02_signal → 5:sq026_02_signal; 9:Out1 → 4:In1; 21:Out → 4:In1; 4:CYB-656199 → 15:In; 4:ep1_active_out → 23:In |
| `base\quest\main_quests\epilogue\q201\q201_heir.quest` / h0 / 44 | `bugfixing.questphase` | 11: Start; 11:Out → 44:In1 |
| `base\quest\main_quests\part1\q101\q101.quest` / h0 / 47 | `bugfixing.questphase` | 0: Start; 0:Out → 47:In1 |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 76 | `bugfixing.questphase` | 0: Start; 0:Out → 76:In1 |
| `base\quest\main_quests\part1\q112\q112_abduction.quest` / h0 / 23 | `bugfixing.questphase` | 0: Start; 0:Out → 23:In1 |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 140 | `bugfixing.questphase` | 0: Start; 0:Out → 140:In1 |
| `base\quest\minor_quests\mq026\mq026.quest` / h0 / 5 | `bugfixing.questphase` | 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1:Out1 → 5:In1; 1:conspiracy_out → 5:In1; 1:combat_out → 5:In1; 1:death_out → 5:In1 |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 61 | `bugfixing.questphase` | 0: Start; 0:Out → 61:In1 |
| `base\quest\side_quests\sq023\sq023.quest` / h0 / 20 | `bugfixing.questphase` | 0: Start; 0:Out → 20:In1 |
| `base\quest\side_quests\sq025\sq025.quest` / h0 / 68 | `bugfixing.questphase` | 49: Phase; 49:additional_content_out → 68:In1 |
| `base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest` / h0 / 64 | `bugfixing.questphase` | 0: Start; 0:Out → 64:In1 |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 13 | `bugfixing.questphase` | 11: LogicalHub; 11:Out1 → 13:In1 |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 42 | `sts_glen_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 42:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |

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
| `checkpoint` | mq044_main.questphase / h231 / 24; mq044_main.questphase / h231 / 25 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `community_lifecycle` | mq044_main.questphase / h14 / 26; mq044_main.questphase / h14 / 41; mq044_main.questphase / h14 / 48; mq044_main.questphase / h14 / 53; +2 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq044_main.questphase / h14 / 28; mq044_main.questphase / h231 / 2; mq044_main.questphase / h231 / 28; mq044_quest_bugfixes.questphase / h0 / 17; +3 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | mq044_main.questphase / h14 / 33; mq044_main.questphase / h231 / 31; mq044_main.questphase / h420 / 3 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | mq044_main.questphase / h14 / 37; mq044_main.questphase / h14 / 38; mq044_main.questphase / h420 / 4; mq044_main.questphase / h420 / 7 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | mq044_main.questphase / h420 / 15 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | mq044_main.questphase / h14 / 56; mq044_main.questphase / h14 / 57; mq044_main.questphase / h14 / 58; mq044_main.questphase / h14 / 59; +12 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | mq044_main.questphase / h231 / 16; mq044_main.questphase / h231 / 19 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `persistent_decision` | mq044_main.questphase / h14 / 55; mq044_main.questphase / h231 / 22; mq044_quest_bugfixes.questphase / h130 / 2; mq044_quest_bugfixes.questphase / h130 / 7; +4 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `spatial_gate` | mq044_main.questphase / h231 / 12; mq044_main.questphase / h231 / 19; mq044_main.questphase / h420 / 16 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | mq044_main.questphase / h231 / 32 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mq044_main.questphase / h14 / 60; mq044_main.questphase / h231 / 33; mq044_main.questphase / h231 / 36 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `world_variant` | mq044_main.questphase / h14 / 39; mq044_main.questphase / h14 / 40; mq044_main.questphase / h420 / 5 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` | repair; journal anchor | `base-mq044` |
| `base\quest\minor_quests\mq044\phases\mq044_main.questphase` | content candidate; journal anchor | `base-mq044` |

Evidence shards for this dossier (including parent context): [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq044](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq044.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sts-hey-gle-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-gle-06.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

61 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 6 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `fee3756653cd083fb28e` | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h420 / 14 -> 15 -> 16 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `c8705a8da51824b73252` | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 0 -> 2 -> 5 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `eaf5aab427d50e5598b6` | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h130 / 0 -> 3 -> 2 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `4e9253a72e6b0134b8dd` | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h231 / 12 -> 17 -> 14 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `cbae0fd3078e68426197` | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h0 / 14 -> 18 -> 17 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `7e7dbbc930b3717fd790` | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 10 -> 8 -> 11 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `90cf58434e79ce42af1e` | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h420 / 0 -> 14 -> 15 | questInputNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]; Out -> In; Out -> In |
| `2cb6a780f07f49d4270b` | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h14 / 37 -> 38 -> 1 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `d5204524c8aea0449912` | `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h231 / 20 -> 28 -> 26 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; True -> Active |
| `80c436c3f41257230312` | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 7 -> 6 -> 10 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; False -> Active |
| `23ae0d4630e5c2a0331c` | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 8 -> 11 -> 1 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questOutputNodeDefinition; Out -> Active; Out -> In |
| `e5b8d4056ed43c4cbe71` | `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h37 / 6 -> 9 -> 8 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; True -> Active; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h0 / 15 | `h37` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq044\mq044_quest_bugfixes.questphase` / h0 / 16 | `h130` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h0 / 2 | `h14` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h0 / 3 | `h231` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq044\phases\mq044_main.questphase` / h0 / 4 | `h420` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
| `base\quest\minor_quests\mq044\mq044.gamedef` | content candidate | base\quest\minor_quests\mq044\mq044.quest |
| `base\quest\main_quests\part1\q101\q101.gamedef` | content candidate | base\quest\main_quests\part1\q101\q101.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_kabuki.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_kabuki.quest |
| `base\quest\demos\handson_2020\handson_2020_little_china.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_little_china.quest |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_speed_test.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_speed_test.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `base\quest\side_quests\sq021\sq021.gamedef` | content candidate | base\quest\side_quests\sq021\sq021.quest |
| `base\quest\side_quests\sq023\sq023.gamedef` | content candidate | base\quest\side_quests\sq023\sq023.quest |
| `base\quest\side_quests\sq025\sq025.gamedef` | content candidate | base\quest\side_quests\sq025\sq025.quest |
| `base\quest\side_quests\sq027\sq027_queen_of_the_highway.gamedef` | content candidate | base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| No attributed direct resource binding | Attribution unresolved | — |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `gle_06_succeed` | base\quest\minor_quests\mq044\mq044.quest / h0 / 3; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h6624 / 37; base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase / h136 / 3; base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase / h882 / 37; 4 total source locations in compressed evidence |
| `mq_044_started_in_main` | base\quest\minor_quests\mq044\phases\mq044.questphase / h0 / 3; 1 total source locations in compressed evidence |

NodeRef uses: 38; TweakDB binding uses: 0. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
