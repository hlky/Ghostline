# Shape of a Pony

Journal: `quests/minor_quest/mws_se5_07` · `MinorQuest` · hash `1052046523`.

**Coverage: journal-linked.** 24 exact journal-linked nodes in 1 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Go the car's last known location. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` |
| Inspect the body for clues. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` |
| Read and reply to the message from Muamar. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` |
| Find the car. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective` |
| Defeat the Wraiths and recover the key. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective1` |
| Get in the car. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective2` |
| Text Muamar about recovering the car. (Primary) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective3` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mws_se5_07.questphase / h0 / 7` (Journal) | `quests/minor_quest/mws_se5_07` | 4:Out → 7:Active; 35:Out → 7:Active; 7:Out → 154:In |
| `mws_se5_07.questphase / h0 / 27` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` | 141:True → 27:Succeeded; 27:Out → 29:Active |
| `mws_se5_07.questphase / h0 / 28` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` | 28:Out → 8:Active; 28:Out → 10:In; 154:Out → 28:Active; 28:Out → 139:In; 28:Out → 147:In1 |
| `mws_se5_07.questphase / h0 / 29` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` | 27:Out → 29:Active; 29:Out → 50:In |
| `mws_se5_07.questphase / h0 / 52` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` | 50:Out → 52:Succeeded; 52:Out → 53:Active |
| `mws_se5_07.questphase / h0 / 53` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` | 52:Out → 53:Active; 53:Out → 54:In |
| `mws_se5_07.questphase / h0 / 55` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` | 54:Out → 55:Succeeded; 55:Out → 56:Active |
| `mws_se5_07.questphase / h0 / 56` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective` | 55:Out → 56:Active; 56:Out → 65:In |
| `mws_se5_07.questphase / h0 / 66` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective` | 65:Out → 66:Succeeded; 66:Out → 67:Active |
| `mws_se5_07.questphase / h0 / 67` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective1` | 67:Out → 62:In; 66:Out → 67:Active; 152:Out → 67:Active; 67:Out → 101:In |
| `mws_se5_07.questphase / h0 / 68` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective1` | 101:Out → 68:Succeeded; 68:Out → 104:Active |
| `mws_se5_07.questphase / h0 / 70` (Journal) | `quests/minor_quest/mws_se5_07` | 108:Out → 70:Succeeded; 70:Out → 155:In |
| `mws_se5_07.questphase / h0 / 104` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective2` | 68:Out → 104:Active; 104:Out → 103:In |
| `mws_se5_07.questphase / h0 / 105` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective2` | 105:Out → 58:In; 103:Out → 105:Succeeded |
| `mws_se5_07.questphase / h0 / 142` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` | 140:Out → 142:Inactive; 142:Out → 143:Inactive |
| `mws_se5_07.questphase / h0 / 143` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` | 142:Out → 143:Inactive; 143:Out → 144:Active |
| `mws_se5_07.questphase / h0 / 144` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` | 144:Out → 54:In; 143:Out → 144:Active |
| `mws_se5_07.questphase / h0 / 149` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07a/objective` | 148:Out → 149:Inactive; 149:Out → 150:Inactive |
| `mws_se5_07.questphase / h0 / 150` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse` | 149:Out → 150:Inactive; 150:Out → 151:Inactive |
| `mws_se5_07.questphase / h0 / 151` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1` | 150:Out → 151:Inactive; 151:Out → 152:Inactive |
| `mws_se5_07.questphase / h0 / 152` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective` | 152:Out → 67:Active; 151:Out → 152:Inactive |
| `mws_se5_07.questphase / h0 / 174` (Journal) | `quests/minor_quest/mws_se5_07/description` | 8:Out → 174:Active; 174:Out → 24:Active |
| `mws_se5_07.questphase / h0 / 178` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective3` | 176:Out → 178:Active; 178:Out → 177:In |
| `mws_se5_07.questphase / h0 / 179` (Journal) | `quests/minor_quest/mws_se5_07/mws_se5_07c/objective3` | 179:Out → 106:Active; 177:Out → 179:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mws_se5_07.questphase / h0 / 14` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene`; `#mws_sm_se5_07` | 13:Out → 14:Start 0 |
| `mws_se5_07.questphase / h0 / 16` | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene`; `#mws_sm_se5_07_camp` | 15:Out → 16:Start 0 |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 14 | `mws_se5_07.scene` | 13: PauseCondition: #mws_se5_07_insvestigation; 13:Out → 14:Start 0 |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 16 | `mws_se5_07_camp.scene` | 15: PauseCondition: #mws_se5_07_tr_encounter; 15:Out → 16:Start 0 |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mws_se5_07.scene` | Start 0 → End 0 | Johnny; player; 10 nodes / 9 edges |
| `mws_se5_07_camp.scene` | Start 0 → End 0 | johnny; porsche_cabrio; player; 10 nodes / 9 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `mws_se5_07_done` | mws_se5_07.questphase / h0 / 155 | No reader in selected context |
| `mws_se5_07_objective_cut1` | mws_se5_07.questphase / h0 / 140 | mws_se5_07.questphase / h0 / 141 |
| `mws_se5_07_started` | mws_se5_07.questphase / h0 / 154 | No reader in selected context |
| `porsche_911_930_turbo_cabriolet_owned` | Producer outside selected context | mws_se5_07.questphase / h0 / 3 |
| `q101_enable_side_content` | Producer outside selected context | mws_se5_07.questphase / h0 / 200 |
| `wms_se5_07_debug` | Producer outside selected context | mws_se5_07.questphase / h0 / 33 |

## Exact gates, joins and cancellation

<details><summary>51 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mws_se5_07.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"porsche_911_930_turbo_cabriolet_owned","value":1,"comparisonType":"GreaterOrEqual"}}}` | 199:Out → 3:In; 3:Out → 9:In; 3:Out → 203:In |
| `mws_se5_07.questphase / h0 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 195:Out → 4:In; 4:Out → 7:Active |
| `mws_se5_07.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_insvestigation"}}` | 11:Out → 13:In; 13:Out → 14:Start 0 |
| `mws_se5_07.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_tr_encounter"}}` | 11:Out → 15:In; 15:Out → 12:In; 15:Out → 16:Start 0; 15:Out → 181:In |
| `mws_se5_07.questphase / h0 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_007"}}}}` | 11:Out → 19:In; 19:Out → 18:In |
| `mws_se5_07.questphase / h0 / 31` | `questCutControlNodeDefinition` `{}` | 139:Out → 31:In; 31:Out → 140:In; 31:CutSource → 50:CutDestination |
| `mws_se5_07.questphase / h0 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wms_se5_07_debug"}}}` | 44:Out → 33:In; 33:Out → 34:In |
| `mws_se5_07.questphase / h0 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 11:Out → 44:In; 44:Out → 33:In |
| `mws_se5_07.questphase / h0 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_b","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 24:Out → 48:In; 48:Out → 26:Active; 148:CutSource → 48:CutDestination |
| `mws_se5_07.questphase / h0 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_tr_corpse"}}` | 29:Out → 50:In; 31:CutSource → 50:CutDestination; 148:CutSource → 50:CutDestination; 50:Out → 52:Succeeded |
| `mws_se5_07.questphase / h0 / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"94462363387","comparisonType":"Greater"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se5/mws_se5_07/shards1/gps","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}]}}` | 53:Out → 54:In; 148:CutSource → 54:CutDestination; 144:Out → 54:In; 54:Out → 55:Succeeded; 54:Out → 175:In |
| `mws_se5_07.questphase / h0 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_combat"}}` | 56:Out → 65:In; 148:CutSource → 65:CutDestination; 65:Out → 66:Succeeded |
| `mws_se5_07.questphase / h0 / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_a","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 24:Out → 71:In; 71:Out → 26:Active; 148:CutSource → 71:CutDestination |
| `mws_se5_07.questphase / h0 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":75600},"end":{"$type":"GameTime","seconds":18000}}}}` | 80:Out → 17:In; 80:Out → 79:In; 93:Out1 → 80:In; 181:Out → 80:In; 80:Out → 82:In; 80:Out → 83:In; 80:Out → 84:In |
| `mws_se5_07.questphase / h0 / 81` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":18000},"end":{"$type":"GameTime","seconds":75600}}}}` | 17:Out → 81:In; 79:Out → 81:In; 83:Out → 81:In; 82:Out → 81:In; 84:Out → 81:In; 81:Out → 86:In; 81:Out → 87:In; 81:Out → 88:In; 81:Out → 89:In; 81:Out → 90:In |
| `mws_se5_07.questphase / h0 / 92` | `questLogicalXorNodeDefinition` `{}` | 86:Out → 92:In1; 87:Out → 92:In1; 88:Out → 92:In1; 89:Out → 92:In2; 90:Out → 92:In2; 92:Out1 → 93:In1 |
| `mws_se5_07.questphase / h0 / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":5,"comparisonType":"GreaterOrEqual"}}}}` | 12:Out → 97:In; 97:Out → 99:In; 97:Out → 156:In; 97:Out → 157:In; 97:Out → 162:In; 97:Out → 163:In; 97:Out → 164:In |
| `mws_se5_07.questphase / h0 / 101` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"124890420321","quantity":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community","names":["ganger1","ganger2","ganger3","ganger4","ganger5"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":5,"comparisonType":"GreaterOrEqual"}}}]}}` | 67:Out → 101:In; 101:Out → 68:Succeeded; 101:Out → 76:In |
| `mws_se5_07.questphase / h0 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"},"childIsPlayer":true,"enterAnimationFinished":true}}}` | 103:Out → 72:In; 104:Out → 103:In; 103:Out → 105:Succeeded; 103:Out → 116:In |
| `mws_se5_07.questphase / h0 / 110` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mws_se5_07_chase"}}` | 119:Out → 110:In; 110:Out → 123:In; 110:Out → 128:In |
| `mws_se5_07.questphase / h0 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"},"count":1,"comparisonType":"GreaterOrEqual"}}}` | 111:Out → 113:In; 113:Out → 115:In1 |
| `mws_se5_07.questphase / h0 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community","names":["chaser1","chaser2"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 112:Out → 114:In; 114:Out → 115:In2 |
| `mws_se5_07.questphase / h0 / 115` | `questLogicalAndNodeDefinition` `{}` | 113:Out → 115:In1; 114:Out → 115:In2; 115:Out1 → 117:In; 115:Out1 → 127:In |
| `mws_se5_07.questphase / h0 / 116` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"},"inverted":true}}}` | 103:Out → 116:In; 116:Out → 111:In; 116:Out → 112:In |
| `mws_se5_07.questphase / h0 / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":250.0}}},{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community","names":["chaser1","chaser2"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":2,"comparisonType":"GreaterOrEqual"}}},{"$type":"questVehicleCondition","type":{"$type":"questVehicleDestruction_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"},"destruction":90.0}}]}]}}` | 115:Out1 → 127:In; 127:Out → 129:In |
| `mws_se5_07.questphase / h0 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 110:Out → 128:In; 128:Out → 125:In |
| `mws_se5_07.questphase / h0 / 129` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_008"},"inverted":true}}}` | 127:Out → 129:In; 129:Out → 172:In |
| `mws_se5_07.questphase / h0 / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_tr_corpse"},{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/car_dealership/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_a","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded","inverted":true}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/car_dealership/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_b","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded","inverted":true}}]}]}}` | 28:Out → 139:In; 139:Out → 31:In; 148:CutSource → 139:CutDestination |
| `mws_se5_07.questphase / h0 / 141` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_se5_07_objective_cut1","comparisonType":"Equal"}}}` | 26:Out → 141:In; 141:True → 27:Succeeded |
| `mws_se5_07.questphase / h0 / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_combat"}}` | 147:Out1 → 146:In; 146:Out → 148:In |
| `mws_se5_07.questphase / h0 / 148` | `questCutControlNodeDefinition` `{}` | 148:CutSource → 48:CutDestination; 148:CutSource → 50:CutDestination; 148:CutSource → 54:CutDestination; 148:CutSource → 65:CutDestination; 148:CutSource → 71:CutDestination; 148:CutSource → 139:CutDestination; 146:Out → 148:In; 148:Out → 149:Inactive |
| `mws_se5_07.questphase / h0 / 153` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"}}}}` | 11:Out → 153:In; 153:Out → 204:In |
| `mws_se5_07.questphase / h0 / 168` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mws_se5_07_corpse"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":200.0}}}]}}` | 155:Out → 168:In; 168:Out → 165:In |
| `mws_se5_07.questphase / h0 / 171` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_wraith_veh_007"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":200.0}}}]}}` | 155:Out → 171:In; 171:Out → 169:In |
| `mws_se5_07.questphase / h0 / 177` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_job_done/job_done","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 178:Out → 177:In; 177:Out → 179:Succeeded |
| `mws_se5_07.questphase / h0 / 181` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_car_search"}}` | 15:Out → 181:In; 181:Out → 80:In |
| `mws_se5_07.questphase / h0 / 184` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleName":"Vehicle.v_sport2_porsche_911turbo_cabrio_player"}}}` | 58:Out → 184:In; 187:Out → 184:In; 184:Out → 185:In |
| `mws_se5_07.questphase / h0 / 185` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"},"timeInterval":0.0,"onScreenTest":true}}}` | 184:Out → 185:In; 185:True → 187:In; 185:False → 186:In |
| `mws_se5_07.questphase / h0 / 186` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"},"childIsPlayer":true}}}` | 186:False → 183:In; 185:False → 186:In; 186:True → 187:In |
| `mws_se5_07.questphase / h0 / 190` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 190:Out1 → 131:In; 165:Out → 190:In3; 170:Out → 190:In2; 173:Out → 190:In4; 182:Out → 190:In1 |
| `mws_se5_07.questphase / h0 / 191` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_response/porsche_911_cabrio_message3_response_a","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 107:Out → 191:In; 191:Out → 180:Active |
| `mws_se5_07.questphase / h0 / 192` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_response/porsche_911_cabrio_message3_response_b","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 107:Out → 192:In; 192:Out → 180:Active |
| `mws_se5_07.questphase / h0 / 199` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 199:Out → 3:In; 200:Out → 199:In; 199:Out → 202:In |
| `mws_se5_07.questphase / h0 / 200` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content","value":1,"comparisonType":"GreaterOrEqual"}}}` | 196:Out → 200:In; 200:Out → 199:In |
| `mws_se5_07.questphase / h0 / 202` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":4}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 202:Out → 194:Active; 199:Out → 202:In; 203:CutSource → 202:CutDestination |
| `mws_se5_07.questphase / h0 / 203` | `questCutControlNodeDefinition` `{}` | 3:Out → 203:In; 203:CutSource → 202:CutDestination |
| `mws_se5_07.scene / scene / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_tr_corpse"}}` | 16:0:0 → 50:0:1; 50:0:0 → 6:0:0; 50:0:0 → 12:0:1 |
| `mws_se5_07.scene / scene / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"94462363387"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"onscreens/emails/quests/minor_activities/badlands/se5/mws_se5_07/shards1/gps","fileEntryIndex":7,"className":"gameJournalOnscreen"},"visited":true}}]},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]},"onScreenTest":true,"inverted":true}}]}}` | 44:0:0 → 54:0:1; 54:0:0 → 32:0:1 |
| `mws_se5_07_camp.scene / scene / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_ws_porsche"},"childIsPlayer":true,"enterAnimationFinished":true}}}` | 8:0:0 → 12:0:1; 12:0:0 → 18:0:1 |
| `mws_se5_07_camp.scene / scene / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_se5_07_near_car"}}` | 24:0:0 → 8:0:0; 48:0:0 → 24:0:1 |
| `mws_se5_07_camp.scene / scene / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"124890420321","quantity":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_se5_07_wraith_community","names":["ganger1","ganger2","ganger3","ganger4","ganger5"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":5,"comparisonType":"GreaterOrEqual"}}}]}}` | 1:0:0 → 48:0:1; 48:0:0 → 14:0:1; 48:0:0 → 24:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mws_se5_07.questphase / h0 / 114; mws_se5_07.questphase / h0 / 97 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `combat_control` | mws_se5_07.questphase / h0 / 126 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mws_se5_07.questphase / h0 / 112; mws_se5_07.questphase / h0 / 12; mws_se5_07.questphase / h0 / 170; mws_se5_07.questphase / h0 / 173 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mws_se5_07.questphase / h0 / 141; mws_se5_07.questphase / h0 / 200; mws_se5_07.questphase / h0 / 3; mws_se5_07.questphase / h0 / 33 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | mws_se5_07.questphase / h0 / 17; mws_se5_07.questphase / h0 / 86 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | mws_se5_07.questphase / h0 / 168; mws_se5_07.questphase / h0 / 171; mws_se5_07.questphase / h0 / 202 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mws_se5_07.questphase / h0 / 101; mws_se5_07.questphase / h0 / 54; mws_se5_07.scene / scene / 54; mws_se5_07_camp.scene / scene / 48 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_read` | mws_se5_07.questphase / h0 / 54; mws_se5_07.scene / scene / 54 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `mount_state` | mws_se5_07.questphase / h0 / 103; mws_se5_07.questphase / h0 / 186; mws_se5_07_camp.scene / scene / 12 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | mws_se5_07.questphase / h0 / 115; mws_se5_07.questphase / h0 / 190 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mws_se5_07.questphase / h0 / 140; mws_se5_07.questphase / h0 / 154; mws_se5_07.questphase / h0 / 155 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mws_se5_07.questphase / h0 / 92 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mws_se5_07.questphase / h0 / 128; mws_se5_07.questphase / h0 / 4; mws_se5_07.questphase / h0 / 44 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mws_se5_07.questphase / h0 / 148; mws_se5_07.questphase / h0 / 203; mws_se5_07.questphase / h0 / 31 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mws_se5_07.questphase / h0 / 108 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mws_se5_07.questphase / h0 / 14; mws_se5_07.questphase / h0 / 16 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `target_resolution` | mws_se5_07.questphase / h0 / 101; mws_se5_07.questphase / h0 / 127; mws_se5_07_camp.scene / scene / 48 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mws_se5_07.questphase / h0 / 117; mws_se5_07.questphase / h0 / 119; mws_se5_07.questphase / h0 / 134; mws_se5_07.questphase / h0 / 18; +8 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mws_se5_07.questphase / h0 / 156; mws_se5_07.questphase / h0 / 157; mws_se5_07.questphase / h0 / 162; mws_se5_07.questphase / h0 / 163; +3 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mws_se5_07.questphase / h0 / 10; mws_se5_07.questphase / h0 / 165 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` | content candidate; journal anchor | `base-mws-se5-07` |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene` | content candidate; forward dependency | `base-mws-se5-07` |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene` | content candidate; forward dependency | `base-mws-se5-07` |

Evidence shards for this dossier (including parent context): [base-mws-se5-07](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mws-se5-07.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
