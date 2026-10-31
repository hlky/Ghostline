# Living on the Edge

Journal: `quests/minor_quest/mq027_stunts` · `MinorQuest` · hash `53780792`.

**Coverage: journal-linked.** 2 exact journal-linked nodes in 1 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Take the recorder from the crew leader. (Primary) | `quests/minor_quest/mq027_stunts/mq027_00_hook/00_01a_take_bd` |
| Equip the recorder. (Primary) | `quests/minor_quest/mq027_stunts/mq027_00_hook/00_01b_plug_bd` |
| Get ready to ride. (Primary) | `quests/minor_quest/mq027_stunts/mq027_00_hook/00_02_ready` |
| Complete a series of stunts. (Primary) | `quests/minor_quest/mq027_stunts/mq027_00_hook/00_03_stunts` |
| Talk to the crew leader. (Primary) | `quests/minor_quest/mq027_stunts/mq027_00_hook/agree` |
| How gonked in the head do you have to ride down a wall with a motorcycle? Beats me. That jackass that just smacked the pavement from a couple stories up looks like he's lost for words too. Check if he's still breathing – maybe we'll find out what compels a person to reach for such absurd heights of gonkery. (Primary) | `quests/minor_quest/mq027_stunts/mq027_00_hook/mq027_hook` |
| Talk to the crew leader about payment. (Primary) | `quests/minor_quest/mq027_stunts/mq027_08_resolution/resolution` |
| Ride into the AV. (Primary) | `quests/minor_quest/mq027_stunts/mq027_arroyo/05_00_go_av` |
| Ride through all the markers. (Primary) | `quests/minor_quest/mq027_stunts/mq027_arroyo/05_01_drive` |
| Go back to the start. (Optional) | `quests/minor_quest/mq027_stunts/mq027_arroyo/05_04_return` |
| Ride into the AV. (Primary) | `quests/minor_quest/mq027_stunts/mq027_arroyo/05_02_repeat` |
| Talk to the crew leader. (Primary) | `quests/minor_quest/mq027_stunts/mq027_arroyo/05_03_talk` |
| Get on the bike. (Primary) | `quests/minor_quest/mq027_stunts/mq027_arroyo/05_05_mount` |
| Get on the bike. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_01/01_00_mount` |
| Ride into the AV. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_01/01_00a_go_av` |
| Get on the bike. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_02/01_00_mount` |
| Ride through all the markers. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_02/01_01_drive` |
| Ride into the AV. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_02/01_02_repeat` |
| Ride into the AV. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_02/02_00_0_prepare` |
| Talk to the crew leader. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_02/02_03_talk` |
| Go back to the start. (Optional) | `quests/minor_quest/mq027_stunts/mq027_stunt_02/02_04_return` |
| Get on the bike. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_03/01_00_mount` |
| Ride through all the markers. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_03/01_01_drive` |
| Ride into the AV. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_03/01_02_repeat` |
| Ride into the AV. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_03/02_00_0_prepare` |
| Talk to the crew leader. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_03/02_03_talk` |
| Go back to the start. (Optional) | `quests/minor_quest/mq027_stunts/mq027_stunt_03/03_04_return` |
| Get on the bike. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_04/01_00_mount` |
| Ride through all the markers. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_04/01_01_drive` |
| Ride into the AV. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_04/01_02_repeat` |
| Ride into the AV. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_04/02_00_0_prepare` |
| Talk to the crew leader. (Primary) | `quests/minor_quest/mq027_stunts/mq027_stunt_04/02_03_talk` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq027.questphase / h303 / 8` (PauseCondition) | `quests/minor_quest/mq027_stunts/mq027_arroyo/05_01_drive` | 0:Out → 8:In; 8:Out → 31:In1 |
| `mq027.questphase / h539 / 8` (PauseCondition) | `quests/minor_quest/mq027_stunts/mq027_stunt_04/01_01_drive` | 0:Out → 8:In; 8:Out → 1:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq027.questphase / h24 / 18` | `base\quest\minor_quests\mq027\scenes\mq027_01_stunt_00.scene`; `#mq027_01_sm_stunt_00` | 18:End 0 → 1:In; 9:Out → 18:Start 0; 18:vehicle_out → 23:In |
| `mq027.questphase / h86 / 11` | `base\quest\minor_quests\mq027\scenes\mq027_03_stunt_02.scene`; `#mq027_03_sm_stunt_02` | 0:Out → 11:Start 0; 11:End 0 → 3:In; 4:Out → 11:chicken_in; 11:get_on_bike_out → 19:get_on_bike_in |
| `mq027.questphase / h86 / 19` | `base\quest\minor_quests\mq027\scenes\mq027_01_stunt_00.scene`; `#mq027_01_sm_stunt_00` | 11:get_on_bike_out → 19:get_on_bike_in |
| `mq027.questphase / h117 / 11` | `base\quest\minor_quests\mq027\scenes\mq027_04_stunt_03.scene`; `#mq027_04_sm_stunt_03` | 0:Out → 11:Start 0; 11:End 0 → 1:In; 4:Out → 11:chicken_in; 11:get_on_bike_out → 14:get_on_bike_in |
| `mq027.questphase / h117 / 14` | `base\quest\minor_quests\mq027\scenes\mq027_01_stunt_00.scene`; `#mq027_01_sm_stunt_00` | 11:get_on_bike_out → 14:get_on_bike_in |
| `mq027.questphase / h167 / 8` | `base\quest\minor_quests\mq027\scenes\mq027_05_stunt_04.scene`; `#mq027_05_sm_stunt_04` | 0:Out → 8:Start 0; 8:End 0 → 1:In; 2:Out → 8:chicken_in |
| `mq027.questphase / h206 / 15` | `base\quest\minor_quests\mq027\scenes\mq027_07_owstunt02.scene`; `#mq027_07_sm_owstunt02` | 15:Continue → 10:In; 13:Out → 15:Start 0; 16:Out → 15:chicken_in; 15:get_on_bike_out → 17:get_on_bike_in |
| `mq027.questphase / h206 / 17` | `base\quest\minor_quests\mq027\scenes\mq027_01_stunt_00.scene`; `#mq027_01_sm_stunt_00` | 15:get_on_bike_out → 17:get_on_bike_in |
| `mq027.questphase / h246 / 6` | `base\quest\minor_quests\mq027\scenes\mq027_06_owstunt01.scene`; `#mq027_06_sm_owstunt01` | 5:Out → 6:chicken_in; 7:Out → 6:Start 0; 6:End 0 → 8:In; 6:get_on_bike_out → 9:get_on_bike_in |
| `mq027.questphase / h246 / 9` | `base\quest\minor_quests\mq027\scenes\mq027_01_stunt_00.scene`; `#mq027_01_sm_stunt_00` | 6:get_on_bike_out → 9:get_on_bike_in |
| `mq027.questphase / h303 / 28` | `base\quest\minor_quests\mq027\phases\mq027_msg_return.questphase` | 27:Out1 → 28:return_in; 35:Out1 → 28:waiting_in |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\mq027\mq027.quest` / h0 / 3 | `mq027.questphase` | 2: Phase: mq027_00_chickentest.questphase; 2: Phase: mq027_00_chickentest.questphase; 2: Phase: mq027_00_chickentest.questphase; 2: Phase: mq027_00_chickentest.questphase; 2: Phase: mq027_00_chickentest.questphase; 2: Phase: mq027_00_chickentest.questphase; 3:Out1 → 1:In; 2:start_out → 3:In1; 2:stunt02_out → 3:stunt02_in; 2:stunt03_out → 3:stunt03_in; 2:stunt04_out → 3:stunt04_in; 2:owstunt01_out → 3:owstunt01_in; 2:owstunt02_out → 3:owstunt02_in |
| `base\quest\minor_quests\mq027\mq027.questphase` / h303 / 28 | `mq027_msg_return.questphase` | 27: LogicalXor; 35: LogicalXor; 27:Out1 → 28:return_in; 35:Out1 → 28:waiting_in |

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
| `mq027_aborted` | Producer outside selected context | mq027.questphase / h303 / 22; mq027.questphase / h303 / 32; mq027.questphase / h303 / 40; mq027.questphase / h539 / 13 |
| `mq027_active` | mq027.questphase / h0 / 16; mq027.questphase / h0 / 4 | No reader in selected context |
| `mq027_bike_spawn` | mq027.questphase / h24 / 23 | mq027.questphase / h303 / 54 |
| `mq027_busy` | mq027.questphase / h0 / 55 | mq027.questphase / h303 / 48; mq027.questphase / h539 / 16 |
| `mq027_counter` | mq027.questphase / h0 / 40 | No reader in selected context |
| `mq027_finished` | mq027.questphase / h0 / 17 | No reader in selected context |
| `mq027_started` | mq027.questphase / h0 / 3 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>34 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq027.questphase / h0 / 57` | `questLogicalAndNodeDefinition` `{}` | 57:Out1 → 2:In; 43:Out → 57:In1; 59:Out1 → 57:In2 |
| `mq027.questphase / h24 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq027_tr_start"}}` | 0:Out → 9:In; 9:Out → 18:Start 0 |
| `mq027.questphase / h303 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef","entityReference":{"$type":"gameEntityReference","reference":"#mq027_com_bike_kiroshi","names":["mq027_bike"]},"refLocalPlayer":false},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq027_com_bike_kiroshi","names":["mq027_av"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":300.0}}}}` | 6:Out1 → 5:In; 53:Out → 5:In; 5:Out → 10:In; 5:Out → 27:In1 |
| `mq027.questphase / h303 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq027_stunts/mq027_arroyo/05_01_drive","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 0:Out → 8:In; 8:Out → 31:In1 |
| `mq027.questphase / h303 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_aborted","comparisonType":"Equal"}}}` | 23:Out → 22:In; 22:Out → 48:In |
| `mq027.questphase / h303 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 23:Out → 22:In; 57:Out → 23:In; 59:Out → 23:In; 60:Out → 23:In; 62:Out → 23:In |
| `mq027.questphase / h303 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 24:Out → 6:In1; 10:Success → 24:In |
| `mq027.questphase / h303 / 27` | `questLogicalXorNodeDefinition` `{}` | 5:Out → 27:In1; 27:Out1 → 28:return_in |
| `mq027.questphase / h303 / 31` | `questLogicalXorNodeDefinition` `{}` | 31:Out1 → 1:In; 8:Out → 31:In1 |
| `mq027.questphase / h303 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_aborted","comparisonType":"Equal"}}}` | 0:Out → 32:In; 46:CutSource → 32:CutDestination; 43:Out1 → 32:In; 32:Out → 36:In; 32:Out → 40:In |
| `mq027.questphase / h303 / 35` | `questLogicalXorNodeDefinition` `{}` | 35:Out1 → 28:waiting_in; 46:Out → 35:In1 |
| `mq027.questphase / h303 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":4}}}` | 32:Out → 36:In; 39:CutSource → 36:CutDestination; 36:Out → 44:In |
| `mq027.questphase / h303 / 39` | `questCutControlNodeDefinition` `{}` | 39:CutSource → 36:CutDestination; 40:Out → 39:In; 39:Out → 43:In1; 39:CutSource → 44:CutDestination |
| `mq027.questphase / h303 / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_aborted","value":1}}}` | 32:Out → 40:In; 40:Out → 39:In |
| `mq027.questphase / h303 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"MinorQuestAndSts"}}}` | 36:Out → 44:In; 39:CutSource → 44:CutDestination; 44:Out → 47:In |
| `mq027.questphase / h303 / 46` | `questCutControlNodeDefinition` `{}` | 46:CutSource → 32:CutDestination; 46:Out → 35:In1; 47:Out → 46:In |
| `mq027.questphase / h303 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq027_com_bike_kiroshi","names":["mq027_bike"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":80.0}}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq027_com_bike_kiroshi","names":["mq027_bike"]},"angleTolerance":90.0,"inverted":true}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_busy","comparisonType":"Equal"}}]}}` | 22:Out → 48:In; 52:Out → 48:In; 48:Out → 54:In |
| `mq027.questphase / h303 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mq027_com_bike_kiroshi","names":["mq027_bike"]}}}}` | 0:Out → 52:In; 52:Out → 48:In |
| `mq027.questphase / h303 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mq027_com_bike_kiroshi","names":["mq027_bike","mq027_av"]}}}}` | 0:Out → 53:In; 53:Out → 5:In |
| `mq027.questphase / h303 / 54` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_bike_spawn","value":1,"comparisonType":"LessOrEqual"}},"socketId":3763167259},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_bike_spawn","value":2,"comparisonType":"Equal"}},"socketId":3497005917},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_bike_spawn","value":3,"comparisonType":"Equal"}},"socketId":332946886},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_bike_spawn","value":5}},"socketId":2157933931}]}` | 48:Out → 54:In; 54:Case3763167259 → 57:In; 54:Case3497005917 → 59:In; 54:Case332946886 → 60:In; 54:Case2157933931 → 62:In |
| `mq027.questphase / h539 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef","entityReference":{"$type":"gameEntityReference","reference":"#mq027_com_bike_arroyo","names":["mq027_bike"]},"refLocalPlayer":false},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq027_com_bike_arroyo","names":["mq027_av"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":300.0}}}]}}` | 5:Out → 3:In; 6:Out1 → 5:In; 18:Out → 5:In |
| `mq027.questphase / h539 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq027_stunts/mq027_stunt_04/01_01_drive","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 0:Out → 8:In; 8:Out → 1:In |
| `mq027.questphase / h539 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_aborted","comparisonType":"Equal"}}}` | 14:Out → 13:In; 13:Out → 16:In |
| `mq027.questphase / h539 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 14:Out → 13:In; 19:Out → 14:In |
| `mq027.questphase / h539 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 3:Success → 15:In; 15:Out → 6:In1 |
| `mq027.questphase / h539 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq027_com_bike_arroyo","names":["mq027_bike"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":80.0}}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq027_com_bike_arroyo","names":["mq027_bike"]},"angleTolerance":90.0,"inverted":true}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq027_busy","comparisonType":"Equal"}}]}}` | 13:Out → 16:In; 17:Out → 16:In; 16:Out → 19:In |
| `mq027.questphase / h539 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mq027_com_bike_arroyo","names":["mq027_bike"]}}}}` | 0:Out → 17:In; 17:Out → 16:In |
| `mq027.questphase / h539 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mq027_com_bike_arroyo","names":["mq027_bike","mq027_av"]}}}}` | 0:Out → 18:In; 18:Out → 5:In |
| `mq027.questphase / h686 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1199}}}` | 4:Out1 → 2:In; 2:Out → 5:In |
| `mq027.questphase / h686 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":120}}}` | 4:Out2 → 3:In; 3:Out → 6:In |
| `mq027_msg_return.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/jessy/mq027_return/mq027_return_04_ch_steal/mq027_return_04a_accident","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 5:Out → 6:In; 6:Out → 8:Active |
| `mq027_msg_return.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/jessy/mq027_return/mq027_return_04_ch_steal/mq027_return_04b_steal","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 5:Out → 7:In; 7:Out → 9:Active |
| `mq027_msg_return.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/jessy/mq027_waiting/mq027_waiting_02_ch_busy/mq027_waiting_02a_busy","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 13:Out → 14:In; 14:Out → 16:Active |
| `mq027_msg_return.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/jessy/mq027_waiting/mq027_waiting_02_ch_busy/mq027_waiting_02b_coming","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 13:Out → 15:In; 15:Out → 16:Active |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `checkpoint` | mq027.questphase / h0 / 43 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `community_lifecycle` | mq027.questphase / h303 / 57; mq027.questphase / h303 / 59; mq027.questphase / h303 / 60; mq027.questphase / h303 / 62; +1 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq027.questphase / h303 / 22; mq027.questphase / h303 / 32; mq027.questphase / h303 / 40; mq027.questphase / h303 / 48; +3 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq027.questphase / h0 / 42; mq027.questphase / h303 / 47 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `elapsed_time` | mq027.questphase / h303 / 36 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | mq027.questphase / h0 / 47; mq027_msg_return.questphase / h0 / 10; mq027_msg_return.questphase / h0 / 12; mq027_msg_return.questphase / h0 / 13; +7 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | mq027.questphase / h0 / 57 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq027.questphase / h0 / 16; mq027.questphase / h0 / 17; mq027.questphase / h0 / 3; mq027.questphase / h0 / 4; +3 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq027.questphase / h303 / 27; mq027.questphase / h303 / 31; mq027.questphase / h303 / 35 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq027.questphase / h303 / 23; mq027.questphase / h303 / 24; mq027.questphase / h539 / 14; mq027.questphase / h539 / 15; +2 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq027.questphase / h303 / 39; mq027.questphase / h303 / 46 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `scene_interface` | mq027.questphase / h117 / 11; mq027.questphase / h117 / 14; mq027.questphase / h167 / 8; mq027.questphase / h206 / 15; +6 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq027.questphase / h24 / 9 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `weather_scope` | mq027.questphase / h206 / 10; mq027.questphase / h206 / 11 | weather operation + named source + reset policy → weather request/reset dispatched. Completion follows the caller's full restoration sequence, not an early cleanup fact. |
| `world_variant` | mq027.questphase / h686 / 5; mq027.questphase / h686 / 6 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\minor_quests\mq027\mq027.questphase` | content candidate; journal anchor | `base-mq027` |
| `base\quest\minor_quests\mq027\phases\mq027_msg_return.questphase` | content candidate; forward dependency | `base-mq027` |

Evidence shards for this dossier (including parent context): [base-mq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq027.json.gz).

Unresolved phase/scene/community resources:

- `base\quest\minor_quests\mq027\scenes\mq027_01_stunt_00.scene`
- `base\quest\minor_quests\mq027\scenes\mq027_03_stunt_02.scene`
- `base\quest\minor_quests\mq027\scenes\mq027_04_stunt_03.scene`
- `base\quest\minor_quests\mq027\scenes\mq027_05_stunt_04.scene`
- `base\quest\minor_quests\mq027\scenes\mq027_06_owstunt01.scene`
- `base\quest\minor_quests\mq027\scenes\mq027_07_owstunt02.scene`

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

52 repeated typed/socket path signatures in this selected graph context; 7 distinct direct resource identities; 10 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 3 -> 4 -> 40 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `e70b0765e99ad324f9b7` | `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 0 -> 3 -> 4 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `eb7ff9b2d44adc239222` | `base\quest\minor_quests\mq027\mq027.questphase` / h303 / 0 -> 32 -> 40 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `362cb43564e34ae74187` | `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 59 -> 57 -> 2 | questPhaseNodeDefinition -> questLogicalAndNodeDefinition -> questOutputNodeDefinition; Out1 -> In2; Out1 -> In |
| `1d51554b5336e85db40a` | `base\quest\minor_quests\mq027\mq027.questphase` / h686 / 0 -> 4 -> 2 | questInputNodeDefinition -> questLogicalHubNodeDefinition -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; Out -> In1; Out1 -> In |
| `afac8a0a934d956c841e` | `base\quest\minor_quests\mq027\mq027.questphase` / h539 / 0 -> 8 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `694dcc3f01ba46e3e166` | `base\quest\minor_quests\mq027\phases\mq027_msg_return.questphase` / h0 / 13 -> 14 -> 16 | questJournalNodeDefinition[questJournalEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalEntry_NodeType]; Out -> In; Out -> Active |
| `c6360c30becfcd41253a` | `base\quest\minor_quests\mq027\phases\mq027_msg_return.questphase` / h0 / 12 -> 13 -> 14 | questJournalNodeDefinition[questJournalEntry_NodeType] -> questJournalNodeDefinition[questJournalEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> Active; Out -> In |
| `b72c8f49e567efbe3bde` | `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 16 -> 17 -> 42 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]; Out -> In; Out -> In |
| `9e39e99ae07a5aebaed8` | `base\quest\minor_quests\mq027\phases\mq027_msg_return.questphase` / h0 / 2 -> 3 -> 4 | questJournalNodeDefinition[questJournalEntry_NodeType] -> questJournalNodeDefinition[questJournalEntry_NodeType] -> questJournalNodeDefinition[questJournalEntry_NodeType]; Out -> Active; Out -> Active |
| `3c2d3d76cbc21af939f6` | `base\quest\minor_quests\mq027\mq027.questphase` / h303 / 0 -> 32 -> 36 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]; Out -> In; Out -> In |
| `c80990c021532456289f` | `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 7 -> 8 -> 35 | questPhaseNodeDefinition -> questPhaseNodeDefinition -> questPhaseNodeDefinition[questQuestPrefabEntry]; Out1 -> In1; Out1 -> In1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 6 | `h24` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":22,"socketName":"vehicle_out","type":"NonTerminating"}] |
| `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 7 | `h86` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":3,"socketName":"Out1"},{"$type":"questInputNodeDefinition","id":4,"socketName":"chicken_in"}] |
| `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 8 | `h117` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questInputNodeDefinition","id":4,"socketName":"chicken_in"}] |
| `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 21 | `h167` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questInputNodeDefinition","id":2,"socketName":"chicken_in"}] |
| `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 34 | `h206` | [{"$type":"questInputNodeDefinition","id":13,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":14,"socketName":"Out1"},{"$type":"questInputNodeDefinition","id":16,"socketName":"chicken_in"}] |
| `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 35 | `h246` | [{"$type":"questInputNodeDefinition","id":5,"socketName":"chicken_in"},{"$type":"questInputNodeDefinition","id":7,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":8,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 49 | `h303` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq027\mq027.questphase` / h303 / 28 | `h408` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 50 | `h539` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq027\mq027.questphase` / h0 / 59 | `h686` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq027\mq027.gamedef` | content candidate | base\quest\minor_quests\mq027\mq027.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\quest\minor_quests\mq027\phases\mq027_msg_return.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq027\scenes\mq027_01_stunt_00.scene` | scene flow | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq027\scenes\mq027_03_stunt_02.scene` | scene flow | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq027\scenes\mq027_04_stunt_03.scene` | scene flow | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq027\scenes\mq027_05_stunt_04.scene` | scene flow | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq027\scenes\mq027_06_owstunt01.scene` | scene flow | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq027\scenes\mq027_07_owstunt02.scene` | scene flow | No match in inspected vanilla indexes; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `mq027_busy` | base\quest\minor_quests\mq027\phases\mq027_00_chickentest.questphase / h0 / 26; base\quest\side_quests\sq025\sq025.quest / h12 / 42; 2 total source locations in compressed evidence |
| `mq027_counter` | base\quest\minor_quests\mq027\phases\mq027_00_chickentest.questphase / h0 / 23; 1 total source locations in compressed evidence |

NodeRef uses: 43; TweakDB binding uses: 0. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
