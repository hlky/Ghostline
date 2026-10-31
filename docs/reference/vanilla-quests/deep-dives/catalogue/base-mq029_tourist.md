# The Highwayman

Journal: `quests/minor_quest/mq029_tourist` · `MinorQuest` · hash `3398058209`.

**Coverage: journal-linked.** 24 exact journal-linked nodes in 6 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 9 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Josie hid the Tyger boss's bike somewhere in the city, near the All Foods factory in Maelstrom turf. Said to look for a "ghost horse." All right then… Think of it like a scavenger hunt, though not the kind fixers in Night City usually pay you for. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist/mq029_bike` |
| The nomad Josie was lured into a trap by a Tyger Claw named James. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist/mq029_body` |
| Find out what happened to Josie. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist/mq029_garage` |
| Josie… Pretty name. Cute girl. Ugly end. This Tyger from the still… better have a word with him, V. Can't let slide what he did to this poor girl. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist/mq029_james` |
| Josie… Pretty name. Cute girl. Ugly end. This Tyger from the still… better have a word with him, V. Can't let slide what he did to this poor girl. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james` |
| Josie hid the Tyger boss's bike somewhere in the city, near the All Foods factory in Maelstrom turf. Said to look for a "ghost horse." All right then… Think of it like a scavenger hunt, though not the kind fixers in Night City usually pay you for. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike` |
| That chick, Josie, wrote something about a garage, didn't she? Somewhere near the dam. Not like it's any of my biz, but if I were you, I'd go check it out. Something tells me it'll give you a boost in the right direction. A sixth sense, shall we say. On the other hand, I am basically dead, which would mean I don't think, so don't hold me to that. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_garage` |
| There's a still of some young guy in the garage – the heartbreaker type. Emails on the computer are from a certain James –  don't have to be a genius to connect the dots. Might be worth looking for our Romeo – especially in Japantown. Got a feeling the still was snapped there. Wouldn't surprise me – kids go on dates there all the time. Shit... it always starts off so cute, doesn't it? Rarely ever ends that way. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_james` |
| Another mystery, another missing person in Night City. Used to be the cops would put out a search for people like her. Today, her fate's in your hands. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new` |
| Pick up the still. (Primary) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_pick_up_photo` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq029_tourist.questphase / h0 / 15` (Journal) | `quests/minor_quest/mq029_tourist` | 16:Out1 → 15:Succeeded; 15:Out → 17:In |
| `mq029_tourist.questphase / h0 / 19` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike` | 23:Out → 19:Active; 19:Out → 20:Active |
| `mq029_tourist.questphase / h0 / 20` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike/mq029_bike_desc` | 19:Out → 20:Active; 20:Out → 21:In |
| `mq029_tourist.questphase / h0 / 22` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike` | 21:True → 22:Succeeded |
| `mq029_tourist.questphase / h0 / 23` (PauseCondition) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james` | 13:Out1 → 23:In; 23:Out → 19:Active |
| `mq029_garage.questphase / h0 / 51` (Condition) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_garage` | 69:mq029_01a_pickup_photo_OUT → 51:In; 51:True → 56:Succeeded; 51:False → 55:Active |
| `mq029_garage.questphase / h0 / 55` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new` | 51:False → 55:Active; 55:Out → 57:Active |
| `mq029_garage.questphase / h0 / 56` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_garage` | 51:True → 56:Succeeded; 56:Out → 59:In1 |
| `mq029_garage.questphase / h0 / 57` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new/mq029_garage` | 55:Out → 57:Active; 57:Out → 59:In2 |
| `mq029_garage.questphase / h0 / 61` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_james` | 59:Out1 → 61:Active; 61:Out → 62:Active |
| `mq029_garage.questphase / h0 / 62` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_james/find_james_desc` | 62:Out → 21:In; 61:Out → 62:Active |
| `mq029_james.questphase / h0 / 31` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james` | 28:Out → 31:Succeeded; 31:Out → 38:In |
| `mq029_josie_corpse.questphase / h0 / 28` (Condition) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new` | 3:Out → 28:In; 28:True → 29:Succeeded; 28:False → 32:Active |
| `mq029_josie_corpse.questphase / h0 / 29` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new` | 28:True → 29:Succeeded; 29:Out → 34:In1 |
| `mq029_josie_corpse.questphase / h0 / 32` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_garage` | 28:False → 32:Active; 32:Out → 33:Active |
| `mq029_josie_corpse.questphase / h0 / 33` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_garage/find_garage` | 32:Out → 33:Active; 33:Out → 34:In2 |
| `mq029_josie_corpse.questphase / h0 / 35` (Condition) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_james` | 34:Out1 → 35:In; 35:True → 36:Active; 35:False → 45:In |
| `mq029_josie_corpse.questphase / h0 / 36` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james` | 35:True → 36:Active; 36:Out → 37:Active |
| `mq029_josie_corpse.questphase / h0 / 37` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james/mq029_james` | 36:Out → 37:Active; 37:Out → 45:In |
| `mq029_stolen_bike.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike` | 15:True → 8:Succeeded |
| `mq029_stolen_bike.questphase / h0 / 15` (Condition) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike` | 2:Out → 15:In; 15:True → 8:Succeeded |
| `mq029_01_james.scene / scene / 130` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_james` | 130:0:0 → 51:0:1; 151:0:0 → 130:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq029_01_james.scene / scene / 135` (Journal) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james` | 51:0:0 → 135:0:1; 135:0:0 → 75:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq029_01_james.scene / scene / 156` (MappinManager) | `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new/mappin_area` | 44:0:0 → 156:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq029_tourist.questphase / h0 / 9` | `base\quest\minor_quests\mq029\phases\mq029_setup.questphase` | 0:Out → 9:In1; 9:Out1 → 14:In1; 9:Out1 → 13:In1; 9:Out1 → 11:In1; 9:Out1 → 10:In1 |
| `mq029_tourist.questphase / h0 / 10` | `base\quest\minor_quests\mq029\phases\mq029_garage.questphase` | 9:Out1 → 10:In1; 10:Out1 → 16:In4 |
| `mq029_tourist.questphase / h0 / 11` | `base\quest\minor_quests\mq029\phases\mq029_james.questphase` | 9:Out1 → 11:In1; 11:Out1 → 16:In3 |
| `mq029_tourist.questphase / h0 / 13` | `base\quest\minor_quests\mq029\phases\mq029_josie_corpse.questphase` | 9:Out1 → 13:In1; 13:Out1 → 16:In2; 13:Out1 → 23:In |
| `mq029_tourist.questphase / h0 / 14` | `base\quest\minor_quests\mq029\phases\mq029_stolen_bike.questphase` | 9:Out1 → 14:In1; 14:Out1 → 16:In1 |
| `mq029_garage.questphase / h0 / 2` | `base\quest\minor_quests\mq029\scenes\mq029_01a_garage.scene`; `#mq029_01a_sm_garage` | 63:Out → 2:mq029_01a_destroyed_bike_IN; 2:mq029_01a_destroyed_bike_OUT → 50:In |
| `mq029_garage.questphase / h0 / 69` | `base\quest\minor_quests\mq029\scenes\mq029_01a_garage.scene`; `#mq029_01a_sm_garage` | 69:mq029_01a_pickup_photo_OUT → 51:In; 68:Out → 69:mq029_01a_pickup_photo_IN; 69:mq029_01a_pickup_photo_OUT → 70:In |
| `mq029_james.questphase / h0 / 4` | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene`; `#mq029_01_sm_james` | 49:CutSource → 4:CutDestination; 27:Out → 4:mq029_01_james_IN; 4:mq029_01_james_combat_OUT → 28:In; 4:mq029_01_james_combat_OUT → 34:In; 4:mq029_01_james_no_fight_OUT → 28:In |
| `mq029_josie_corpse.questphase / h0 / 4` | `base\quest\minor_quests\mq029\scenes\mq029_01b_josie_body.scene`; `#mq029_01b_sm_josie_body` | 17:Out → 4:mq029_01b_josie_body_IN; 4:mq029_01b_josie_body_OUT → 27:In; 4:mq029_01b_josie_body_OUT → 42:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 26 | `mq029_tourist.questphase` | 84: LogicalHub; 84:Out1 → 26:In1 |
| `base\quest\minor_quests\mq029\mq029_tourist.questphase` / h0 / 10 | `mq029_garage.questphase` | 9: Phase: mq029_setup.questphase; 9:Out1 → 10:In1; 10:Out1 → 16:In4 |
| `base\quest\minor_quests\mq029\mq029_tourist.questphase` / h0 / 11 | `mq029_james.questphase` | 9: Phase: mq029_setup.questphase; 9:Out1 → 11:In1; 11:Out1 → 16:In3 |
| `base\quest\minor_quests\mq029\mq029_tourist.questphase` / h0 / 13 | `mq029_josie_corpse.questphase` | 9: Phase: mq029_setup.questphase; 9:Out1 → 13:In1; 13:Out1 → 16:In2; 13:Out1 → 23:In |
| `base\quest\minor_quests\mq029\mq029_tourist.questphase` / h0 / 9 | `mq029_setup.questphase` | 0: Input; 0:Out → 9:In1; 9:Out1 → 14:In1; 9:Out1 → 13:In1; 9:Out1 → 11:In1; 9:Out1 → 10:In1 |
| `base\quest\minor_quests\mq029\mq029_tourist.questphase` / h0 / 14 | `mq029_stolen_bike.questphase` | 9: Phase: mq029_setup.questphase; 9:Out1 → 14:In1; 14:Out1 → 16:In1 |
| `base\quest\minor_quests\mq029\phases\mq029_james.questphase` / h0 / 4 | `mq029_01_james.scene` | 49: CutControl; 27: PauseCondition: #mq029_tr_james; 49:CutSource → 4:CutDestination; 27:Out → 4:mq029_01_james_IN; 4:mq029_01_james_combat_OUT → 28:In; 4:mq029_01_james_combat_OUT → 34:In; 4:mq029_01_james_no_fight_OUT → 28:In |
| `base\quest\minor_quests\mq029\phases\mq029_garage.questphase` / h0 / 2 | `mq029_01a_garage.scene` | 63: PauseCondition: IsOpen; 63:Out → 2:mq029_01a_destroyed_bike_IN; 2:mq029_01a_destroyed_bike_OUT → 50:In |
| `base\quest\minor_quests\mq029\phases\mq029_garage.questphase` / h0 / 69 | `mq029_01a_garage.scene` | 68: PauseCondition: IsAdvancedInteractionModeOff; 69:mq029_01a_pickup_photo_OUT → 51:In; 68:Out → 69:mq029_01a_pickup_photo_IN; 69:mq029_01a_pickup_photo_OUT → 70:In |
| `base\quest\minor_quests\mq029\phases\mq029_josie_corpse.questphase` / h0 / 4 | `mq029_01b_josie_body.scene` | 17: PauseCondition: #mq029_josie_last_note_new; 17:Out → 4:mq029_01b_josie_body_IN; 4:mq029_01b_josie_body_OUT → 27:In; 4:mq029_01b_josie_body_OUT → 42:In |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq029_01_james.scene` | mq029_01_james_IN, Start1, returnal → mq029_01_james_combat_OUT, mq029_01_james_no_fight_OUT | james; Player; 79 nodes / 95 edges |
| `mq029_01a_garage.scene` | mq029_01a_destroyed_bike_IN, mq029_01a_pickup_photo_IN → mq029_01a_destroyed_bike_OUT, mq029_01a_pickup_photo_OUT | johnny; Player; 19 nodes / 17 edges |
| `mq029_01b_josie_body.scene` | mq029_01b_josie_body_IN, mq029_01b_final_note_in → mq029_01b_josie_body_OUT, mq029_01b_final_note_out | johnny; Player; 11 nodes / 9 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq029_01_james.scene / n4 / 0` | [Show photo] You the guy in this picture? (``) | No option-level predicate stored | 0:0 → 148:0:1; 0:0 → 223:0:1 |
| `mq029_01_james.scene / n22 / 0` | Josie's dead. And it's your fault. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq029_fact_josie_body_found"}}} | 0:0 → 17:0:0 |
| `mq029_01_james.scene / n22 / 1` | Found Josie's ride. (``) | {"questCondition": {"$type": "questLogicalCondition", "conditions": [{"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq029_fact_josie_body_found", "comparisonType": "LessOrEqual"}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq029_fact_tc_bike_found", "value": 1, "comparisonType": "GreaterOrEqual"}}]}} | 0:1 → 112:0:1 |
| `mq029_01_james.scene / n22 / 2` | Got any new intel? (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq029_fact_josie_body_found", "comparisonType": "LessOrEqual"}}} | 0:2 → 25:0:0 |
| `mq029_01_james.scene / n57 / 0` | So you had a choice. (``) | No option-level predicate stored | 0:0 → 61:0:0 |
| `mq029_01_james.scene / n57 / 1` | You pathetic piece of shit. (``) | No option-level predicate stored | 0:1 → 138:0:1 |
| `mq029_01_james.scene / n63 / 0` | We'll be in touch. (``) | No option-level predicate stored | 0:0 → 69:0:0; 0:0 → 189:0:1 |
| `mq029_01_james.scene / n63 / 1` | You know where to look? (``) | No option-level predicate stored | 0:1 → 11:0:0 |
| `mq029_01a_garage.scene / n14 / 0` | Well, well... (``) | No option-level predicate stored | 0:0 → 60:0:1; 0:0 → 79:0:1 |
| `mq029_01b_josie_body.scene / n11 / 0` | [Read] (``) | No option-level predicate stored | 0:0 → 16:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `mq029_01_james_loop_on` | mq029_01_james.scene / scene / 222; mq029_01_james.scene / scene / 223; mq029_01_james.scene / scene / 227; mq029_01_james.scene / scene / 230; mq029_01_james.scene / scene / 233; mq029_01_james.scene / scene / 236; mq029_01_james.scene / scene / 239; mq029_01_james.scene / scene / 257; mq029_01_james.scene / scene / 260; mq029_01_james.scene / scene / 266 | mq029_01_james.scene / scene / 208; mq029_01_james.scene / scene / 209 |
| `mq029_fact_james_gave_directions` | mq029_01_james.scene / scene / 46 | mq029_01_james.scene / scene / 45 |
| `mq029_fact_james_hostile` | mq029_james.questphase / h0 / 34 | No reader in selected context |
| `mq029_fact_james_knows_josie_dead` | mq029_01_james.scene / scene / 31 | No reader in selected context |
| `mq029_fact_josie_body_found` | mq029_josie_corpse.questphase / h0 / 3 | mq029_01_james.scene / scene / 22; mq029_01_james.scene / scene / 51 |
| `mq029_fact_read_garage_note` | Producer outside selected context | mq029_garage.questphase / h0 / 48; mq029_james.questphase / h0 / 6 |
| `mq029_fact_tc_bike_found` | mq029_stolen_bike.questphase / h0 / 7 | mq029_01_james.scene / scene / 22; mq029_tourist.questphase / h0 / 21 |
| `mq029_josie_garage_found` | mq029_garage.questphase / h0 / 70 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>53 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq029_tourist.questphase / h0 / 16` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 10:Out1 → 16:In4; 11:Out1 → 16:In3; 13:Out1 → 16:In2; 14:Out1 → 16:In1; 16:Out1 → 15:Succeeded |
| `mq029_tourist.questphase / h0 / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq029_fact_tc_bike_found"}}}` | 20:Out → 21:In; 21:True → 22:Succeeded |
| `mq029_tourist.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 13:Out1 → 23:In; 23:Out → 19:Active |
| `mq029_garage.questphase / h0 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq029_fact_read_garage_note"}}}` | 0:Out → 48:In; 48:Out → 68:In |
| `mq029_garage.questphase / h0 / 51` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_garage","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 69:mq029_01a_pickup_photo_OUT → 51:In; 51:True → 56:Succeeded; 51:False → 55:Active |
| `mq029_garage.questphase / h0 / 59` | `questLogicalXorNodeDefinition` `{}` | 56:Out → 59:In1; 57:Out → 59:In2; 59:Out1 → 61:Active |
| `mq029_garage.questphase / h0 / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq029_door_josie_garage","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 0:Out → 63:In; 63:Out → 2:mq029_01a_destroyed_bike_IN; 63:Out → 65:In |
| `mq029_garage.questphase / h0 / 43` | `questLogicalAndNodeDefinition` `{}` | 21:Out → 43:In2; 43:Out1 → 44:In; 66:Out1 → 43:In1 |
| `mq029_garage.questphase / h0 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq029_tr_general_proximity"}}` | 63:Out → 65:In; 65:Out → 66:In1 |
| `mq029_garage.questphase / h0 / 66` | `questLogicalXorNodeDefinition` `{}` | 50:Out → 66:In2; 66:Out1 → 43:In1; 65:Out → 66:In1 |
| `mq029_garage.questphase / h0 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq029_dvc_josie_computer","deviceControllerClass":"ComputerControllerPS","deviceConditionFunction":"IsAdvancedInteractionModeOff"}}}` | 48:Out → 68:In; 68:Out → 69:mq029_01a_pickup_photo_IN |
| `mq029_james.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_com_james","names":["james"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 17:Out → 3:In; 3:Out → 6:In |
| `mq029_james.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq029_fact_read_garage_note"}}}` | 3:Out → 6:In; 6:Out → 27:In |
| `mq029_james.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq029_tr_james"}}` | 27:Out → 4:mq029_01_james_IN; 6:Out → 27:In |
| `mq029_james.questphase / h0 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq029_com_james","names":["james"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":120.0}}}}` | 37:Out → 35:In; 35:Out → 36:In |
| `mq029_james.questphase / h0 / 49` | `questCutControlNodeDefinition` `{}` | 49:CutSource → 4:CutDestination; 34:Out → 49:In; 49:Out → 56:In |
| `mq029_josie_corpse.questphase / h0 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#mq029_josie_last_note_new","eventType":"Executed"}}}` | 0:Out → 17:In; 17:Out → 4:mq029_01b_josie_body_IN; 17:Out → 40:In |
| `mq029_josie_corpse.questphase / h0 / 28` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 3:Out → 28:In; 28:True → 29:Succeeded; 28:False → 32:Active |
| `mq029_josie_corpse.questphase / h0 / 34` | `questLogicalXorNodeDefinition` `{}` | 29:Out → 34:In1; 33:Out → 34:In2; 34:Out1 → 35:In |
| `mq029_josie_corpse.questphase / h0 / 35` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_james","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 34:Out1 → 35:In; 35:True → 36:Active; 35:False → 45:In |
| `mq029_josie_corpse.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#mq029_josies_body_prevention_free_zone"}}` | 0:Out → 43:In; 43:Out → 44:In |
| `mq029_josie_corpse.questphase / h46 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_blood_stain"},"eventType":"Finished"}}}` | 0:Out → 2:In; 2:Out → 14:In1 |
| `mq029_josie_corpse.questphase / h46 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_blood_stain_001"},"eventType":"Finished"}}}` | 0:Out → 4:In; 4:Out → 14:In2 |
| `mq029_josie_corpse.questphase / h46 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_blood_stain_002"},"eventType":"Finished"}}}` | 0:Out → 5:In; 5:Out → 14:In3 |
| `mq029_josie_corpse.questphase / h46 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_blood_stain_003"},"eventType":"Finished"}}}` | 0:Out → 6:In; 6:Out → 14:In4 |
| `mq029_josie_corpse.questphase / h46 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_blood_stain_004"},"eventType":"Finished"}}}` | 0:Out → 7:In; 7:Out → 14:In5 |
| `mq029_josie_corpse.questphase / h46 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_blood_stain_005"},"eventType":"Finished"}}}` | 0:Out → 8:In; 8:Out → 14:In6 |
| `mq029_josie_corpse.questphase / h46 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_blood_stain_006"},"eventType":"Finished"}}}` | 0:Out → 9:In; 9:Out → 14:In7 |
| `mq029_josie_corpse.questphase / h46 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_blood_stain_007"},"eventType":"Finished"}}}` | 0:Out → 10:In; 10:Out → 14:In8 |
| `mq029_josie_corpse.questphase / h46 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq029_blood_stain_008"},"eventType":"Finished"}}}` | 0:Out → 11:In; 11:Out → 14:In9 |
| `mq029_josie_corpse.questphase / h46 / 14` | `questLogicalXorNodeDefinition` `{"inputSocketCount":9}` | 2:Out → 14:In1; 4:Out → 14:In2; 5:Out → 14:In3; 6:Out → 14:In4; 7:Out → 14:In5; 8:Out → 14:In6; 9:Out → 14:In7; 10:Out → 14:In8; 11:Out → 14:In9; 14:Out1 → 17:In; 14:Out1 → 18:In; 14:Out1 → 19:In; 14:Out1 → 20:In; 14:Out1 → 21:In; 14:Out1 → 22:In; 14:Out1 → 23:In; 14:Out1 → 24:In; 14:Out1 → 25:In |
| `mq029_stolen_bike.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq029_dvc_door_stolen_bike","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 0:Out → 2:In; 2:Out → 15:In; 2:Out → 17:In1; 2:Out → 18:In |
| `mq029_stolen_bike.questphase / h0 / 15` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 15:In; 15:True → 8:Succeeded |
| `mq029_stolen_bike.questphase / h63 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_01_victor","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 0:Out → 2:In; 2:True → 14:In; 2:False → 3:In |
| `mq029_stolen_bike.questphase / h63 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_01_victor","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 2:False → 3:In; 3:True → 14:In; 3:False → 4:In |
| `mq029_stolen_bike.questphase / h63 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_02_dex","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 3:False → 4:In; 4:True → 14:In; 4:False → 5:In |
| `mq029_stolen_bike.questphase / h63 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q001_intro","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 4:False → 5:In; 5:True → 14:In; 5:False → 6:In |
| `mq029_stolen_bike.questphase / h63 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q003_maelstrom","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 5:False → 6:In; 6:True → 14:In; 6:False → 8:In |
| `mq029_stolen_bike.questphase / h63 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q004_braindance","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 6:False → 8:In; 14:Out → 8:In; 8:True → 13:In; 8:False → 9:In |
| `mq029_stolen_bike.questphase / h63 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/prologue/q005_heist","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 9:False → 1:In; 8:False → 9:In; 9:True → 13:In |
| `mq029_stolen_bike.questphase / h63 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/act_01/q101_01_firestorm","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 13:Out → 1:In; 8:True → 13:In; 9:True → 13:In |
| `mq029_01_james.scene / scene / 45` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq029_fact_james_gave_directions"}}}` | 45:0:1 → 46:0:1; 69:0:0 → 45:0:1 |
| `mq029_01_james.scene / scene / 51` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq029_fact_josie_body_found","value":1,"comparisonType":"GreaterOrEqual"}}}` | 51:0:0 → 135:0:1; 51:0:1 → 53:0:0; 130:0:0 → 51:0:1 |
| `mq029_01_james.scene / scene / 112` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\minor_quests\\mq029\\scenes\\mq029_01_james.scene","Flags":"Soft"},"sectionName":"mq029_01_stolen_bike_where_josie","type":"IsOutside"}}}` | 22:0:1 → 112:0:1; 112:0:0 → 27:0:0 |
| `mq029_01_james.scene / scene / 162` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq029_tr_james"}}` | 159:0:0 → 162:0:1; 162:0:0 → 196:666:1; 174:1:0 → 162:0:0; 174:1:0 → 162:1026:0; 182:1:0 → 162:0:0; 182:1:0 → 162:1026:0 |
| `mq029_01_james.scene / scene / 164` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq029_tr_james"}}` | 164:0:0 → 159:0:1; 167:0:0 → 164:0:1; 174:1:0 → 164:0:0; 174:1:0 → 164:1026:0; 182:1:0 → 164:0:0; 182:1:0 → 164:1026:0 |
| `mq029_01_james.scene / scene / 189` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq029_tr_james"}}` | 63:0:0 → 189:0:1; 189:0:0 → 22:0:0; 269:0:0 → 189:0:1 |
| `mq029_01_james.scene / scene / 208` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq029_01_james_loop_on"}}}` | 1:0:0 → 208:0:1; 208:0:0 → 209:0:1; 208:0:0 → 214:0:0; 209:0:0 → 208:0:1 |
| `mq029_01_james.scene / scene / 209` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq029_01_james_loop_on","comparisonType":"Equal"}}}` | 208:0:0 → 209:0:1; 209:0:0 → 208:0:1; 209:0:0 → 214:1:0; 209:0:0 → 215:0:0 |
| `mq029_01_james.scene / scene / 290` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 282:0:0 → 290:0:1; 290:0:0 → 283:0:1 |
| `mq029_01a_garage.scene / scene / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq029_01a_garage_johnny"},"timeInterval":2.0,"angleTolerance":120.0,"inverted":true}}}` | 25:0:0 → 32:0:1; 32:0:0 → 31:0:1 |
| `mq029_01a_garage.scene / scene / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 79:0:0 → 80:0:1; 80:0:0 → 28:0:1 |
| `mq029_01b_josie_body.scene / scene / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq029_01b_josie_body_johnny"},"angleTolerance":90.0,"inverted":true}}}` | 6:0:0 → 24:0:1; 24:0:0 → 22:666:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq029_james.questphase / h0 / 3 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `choice_gate` | mq029_01_james.scene / scene / 22; mq029_01_james.scene / scene / 4; mq029_01_james.scene / scene / 57; mq029_01_james.scene / scene / 63; +2 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq029_01_james.scene / scene / 283; mq029_james.questphase / h0 / 54 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq029_james.questphase / h0 / 17; mq029_james.questphase / h0 / 36 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq029_01_james.scene / scene / 208; mq029_01_james.scene / scene / 209; mq029_01_james.scene / scene / 22; mq029_01_james.scene / scene / 45; +4 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq029_01_james.scene / scene / 159; mq029_01_james.scene / scene / 167; mq029_01_james.scene / scene / 172; mq029_01_james.scene / scene / 180; +4 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `device_state` | mq029_garage.questphase / h0 / 63; mq029_garage.questphase / h0 / 68; mq029_stolen_bike.questphase / h0 / 2 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `parallel_join` | mq029_garage.questphase / h0 / 43; mq029_tourist.questphase / h0 / 16 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq029_01_james.scene / scene / 222; mq029_01_james.scene / scene / 223; mq029_01_james.scene / scene / 227; mq029_01_james.scene / scene / 230; +12 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq029_garage.questphase / h0 / 59; mq029_garage.questphase / h0 / 66; mq029_josie_corpse.questphase / h0 / 34; mq029_josie_corpse.questphase / h46 / 14 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq029_01_james.scene / scene / 290; mq029_01a_garage.scene / scene / 80 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq029_james.questphase / h0 / 49 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq029_james.questphase / h0 / 28 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | mq029_josie_corpse.questphase / h46 / 10; mq029_josie_corpse.questphase / h46 / 11; mq029_josie_corpse.questphase / h46 / 2; mq029_josie_corpse.questphase / h46 / 4; +5 locations in catalogue.json | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | mq029_garage.questphase / h0 / 2; mq029_garage.questphase / h0 / 69; mq029_james.questphase / h0 / 4; mq029_josie_corpse.questphase / h0 / 4 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `vehicle_control` | mq029_stolen_bike.questphase / h0 / 13 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq029_01_james.scene / scene / 100; mq029_01_james.scene / scene / 101; mq029_01_james.scene / scene / 102; mq029_01_james.scene / scene / 201; +17 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\minor_quests\mq029\mq029_tourist.questphase` | content candidate; journal anchor | `base-mq029` |
| `base\quest\minor_quests\mq029\phases\mq029_garage.questphase` | content candidate; journal anchor | `base-mq029` |
| `base\quest\minor_quests\mq029\phases\mq029_james.questphase` | content candidate; journal anchor | `base-mq029` |
| `base\quest\minor_quests\mq029\phases\mq029_josie_corpse.questphase` | content candidate; journal anchor | `base-mq029` |
| `base\quest\minor_quests\mq029\phases\mq029_setup.questphase` | content candidate; forward dependency | `base-mq029` |
| `base\quest\minor_quests\mq029\phases\mq029_stolen_bike.questphase` | content candidate; journal anchor | `base-mq029` |
| `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` | content candidate; journal anchor | `base-mq029` |
| `base\quest\minor_quests\mq029\scenes\mq029_01a_garage.scene` | content candidate; forward dependency | `base-mq029` |
| `base\quest\minor_quests\mq029\scenes\mq029_01b_josie_body.scene` | content candidate; forward dependency | `base-mq029` |

Evidence shards for this dossier (including parent context): [base-mq029](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq029.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
