# The Gift

Journal: `quests/side_quest/sq_q001_tbug` · `SideQuest` · hash `2549135402`.

**Coverage: journal-linked.** 15 exact journal-linked nodes in 1 resources; 1 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Equip the Ping quickhack in your inventory and upload it to the camera. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/01_ba_use_ping_just` |
| Equip the Ping quickhack in your inventory. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` |
| Retrieve the Ping quickhack from the netrunner. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/01_pick_programms` |
| Equip the Ping quickhack in your inventory and upload it to the camera in order to locate an Access Point. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/01b_use_ping` |
| Use your personal link to connect to the Access Point and hack it. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point` |
| Upload Ping to the camera to find the Access Point. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/02_upload_ping_find_ap` |
| Upload Ping to the camera. (Primary) | `quests/side_quest/sq_q001_tbug/tbug/02b_upload_ping_just` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `q001_tbug_tutorial.questphase / h0 / 3` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_pick_programms` | 37:Out → 3:Active; 3:Out → 4:Active |
| `q001_tbug_tutorial.questphase / h0 / 4` (Journal) | `quests/side_quest/sq_q001_tbug/desc` | 3:Out → 4:Active; 4:Out → 5:In |
| `q001_tbug_tutorial.questphase / h0 / 6` (Journal) | `quests/side_quest/sq_q001_tbug` | 43:False → 6:Succeeded; 87:Out → 6:Succeeded; 6:Out → 76:In |
| `q001_tbug_tutorial.questphase / h0 / 7` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_pick_programms` | 5:Out → 7:Succeeded; 7:Out → 111:In |
| `q001_tbug_tutorial.questphase / h0 / 8` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point` | 50:False → 8:Active |
| `q001_tbug_tutorial.questphase / h0 / 11` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point` | 48:True → 11:Succeeded; 11:Out → 43:In |
| `q001_tbug_tutorial.questphase / h0 / 38` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` | 116:Out1 → 38:Active; 38:Out → 39:In; 38:Out → 54:In; 38:Out → 88:In |
| `q001_tbug_tutorial.questphase / h0 / 43` (Condition) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` | 43:False → 6:Succeeded; 11:Out → 43:In; 48:False → 43:In; 43:True → 86:In |
| `q001_tbug_tutorial.questphase / h0 / 48` (Condition) | `quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point` | 48:True → 11:Succeeded; 32:Out → 48:In; 48:False → 43:In |
| `q001_tbug_tutorial.questphase / h0 / 78` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/01_equip_ping` | 77:Out → 78:Succeeded; 78:Out → 79:In |
| `q001_tbug_tutorial.questphase / h0 / 80` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02_upload_ping_find_ap` | 79:False → 80:Active; 80:Out → 89:In |
| `q001_tbug_tutorial.questphase / h0 / 81` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02b_upload_ping_just` | 79:True → 81:Active; 81:Out → 89:In |
| `q001_tbug_tutorial.questphase / h0 / 83` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02_upload_ping_find_ap` | 83:Out → 50:In; 82:False → 83:Succeeded |
| `q001_tbug_tutorial.questphase / h0 / 84` (Journal) | `quests/side_quest/sq_q001_tbug/tbug/02b_upload_ping_just` | 84:Out → 50:In; 82:True → 84:Succeeded |
| `q001_tbug_tutorial.questphase / h0 / 112` (Journal) | `quests/side_quest/sq_q001_tbug` | 115:Out → 112:Succeeded; 112:Out → 113:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\persistent_content.questphase` / h1469 / 11 | `q001_tbug_tutorial.questphase` | 12: PauseCondition: q001_tbug_netrunner_tut GreaterOrEqual 1; 12:Out → 11:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 17 | `persistent_content.questphase` | 0: Input; 36: Input; 0:Out → 17:In1; 36:Out → 17:EP1_Standalone |
| `base\quest\cyberpunk2077.questphase` / h520 / 3 | `additional_game_elements.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 9:Out1 → 3:Input; 21:Out → 3:EP1_Standalone |

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
| `close_inventory_mode_tutorial` | q001_tbug_tutorial.questphase / h0 / 62 | q001_tbug_tutorial.questphase / h0 / 75 |
| `cyberdeck_inventory_tutorial` | q001_tbug_tutorial.questphase / h0 / 54 | q001_tbug_tutorial.questphase / h0 / 53 |
| `ping_installed` | Producer outside selected context | q001_tbug_tutorial.questphase / h0 / 77; q001_tbug_tutorial.questphase / h0 / 91 |
| `q001_sq_tbug_done` | q001_tbug_tutorial.questphase / h0 / 76 | No reader in selected context |
| `q001_tbug_netrunner_tut` | q001_tbug_tutorial.questphase / h0 / 51 | No reader in selected context |
| `q001_tut_ap_hacked_netrunner` | q001_tbug_tutorial.questphase / h0 / 49 | q001_tbug_tutorial.questphase / h0 / 50; q001_tbug_tutorial.questphase / h0 / 79; q001_tbug_tutorial.questphase / h0 / 82 |
| `q001_tut_equip_upload_part_done` | q001_tbug_tutorial.questphase / h0 / 85 | q001_tbug_tutorial.questphase / h0 / 87 |
| `q101_new_ping_tutorial_started` | q001_tbug_tutorial.questphase / h0 / 88 | No reader in selected context |
| `q101_no_cyberdeck_initially` | q001_tbug_tutorial.questphase / h0 / 115 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>35 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `q001_tbug_tutorial.questphase / h0 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"151781844931","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 4:Out → 5:In; 5:Out → 7:Succeeded |
| `q001_tbug_tutorial.questphase / h0 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q001_exercise_access_point","deviceControllerClass":"AccessPointControllerPS","deviceConditionFunction":"WasHackingMinigameSucceeded"}}}` | 9:Out → 10:In; 10:Out → 49:In |
| `q001_tbug_tutorial.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q001_tr_accesspoint_shop_tutorial"}}` | 26:Out → 15:In; 36:Out1 → 15:In; 15:Out → 16:In; 15:Out → 27:In; 15:Out → 25:In |
| `q001_tbug_tutorial.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q001_tr_accesspoint_shop_tutorial"}}` | 15:Out → 25:In; 29:CutSource → 25:CutDestination; 25:Out → 26:In |
| `q001_tbug_tutorial.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q001_exercise_access_point","deviceControllerClass":"AccessPointControllerPS","deviceConditionFunction":"IsPersonalLinkConnecting"}}}` | 15:Out → 27:In; 27:Out → 29:In |
| `q001_tbug_tutorial.questphase / h0 / 29` | `questCutControlNodeDefinition` `{}` | 29:CutSource → 25:CutDestination; 29:CutSource → 26:CutDestination; 27:Out → 29:In; 29:Out → 28:In |
| `q001_tbug_tutorial.questphase / h0 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"112307738469","value":false}}}` | 49:Out → 32:In; 32:Out → 48:In |
| `q001_tbug_tutorial.questphase / h0 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q001_exercise_device_quickhack","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"WasQuickHackJustPerformed","functionParameters":[{"$type":"questDevice_ConditionFunctionParameter","name":"quickHackName","value":{"$type":"Variant","$rawData":"DwAGAAAAlwA="}}]}}}` | 38:Out → 39:In; 39:Out → 82:In |
| `q001_tbug_tutorial.questphase / h0 / 43` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_tbug/tbug/01_equip_ping","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 43:False → 6:Succeeded; 11:Out → 43:In; 48:False → 43:In; 43:True → 86:In |
| `q001_tbug_tutorial.questphase / h0 / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq_q001_tbug/tbug/02_exercise_access_point","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 48:True → 11:Succeeded; 32:Out → 48:In; 48:False → 43:In |
| `q001_tbug_tutorial.questphase / h0 / 50` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_tut_ap_hacked_netrunner","value":1,"comparisonType":"GreaterOrEqual"}}}` | 50:False → 8:Active; 84:Out → 50:In; 83:Out → 50:In |
| `q001_tbug_tutorial.questphase / h0 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"cyberdeck_inventory_tutorial","value":1,"comparisonType":"GreaterOrEqual"}}}` | 53:Out → 21:In; 108:Out → 53:In; 53:Out → 62:In; 53:Out → 119:In |
| `q001_tbug_tutorial.questphase / h0 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q001_tr_turnoff_equip_ping_tut"}}` | 69:CutSource → 65:CutDestination; 114:Out → 65:In; 65:Out → 66:In |
| `q001_tbug_tutorial.questphase / h0 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q001_tr_turnoff_equip_ping_tut"}}` | 72:CutSource → 67:CutDestination; 74:Out → 67:In; 67:Out → 68:In |
| `q001_tbug_tutorial.questphase / h0 / 69` | `questCutControlNodeDefinition` `{}` | 69:CutSource → 65:CutDestination; 108:Out → 69:In; 69:Out → 74:In; 69:CutSource → 114:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q001_tr_turnoff_equip_ping_tut"}}` | 73:CutSource → 70:CutDestination; 75:Out → 70:In; 70:Out → 71:In |
| `q001_tbug_tutorial.questphase / h0 / 72` | `questCutControlNodeDefinition` `{}` | 62:Out → 72:In; 72:CutSource → 67:CutDestination; 72:Out → 75:In; 72:CutSource → 74:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 73` | `questCutControlNodeDefinition` `{}` | 61:Out → 73:In; 73:CutSource → 70:CutDestination; 73:CutSource → 75:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"118585379367","value":false}}}` | 74:Out → 67:In; 69:Out → 74:In; 72:CutSource → 74:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"close_inventory_mode_tutorial","value":1,"comparisonType":"GreaterOrEqual"}}}` | 75:Out → 70:In; 72:Out → 75:In; 73:CutSource → 75:CutDestination; 75:Out → 95:In |
| `q001_tbug_tutorial.questphase / h0 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ping_installed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 88:Out → 77:In; 77:Out → 78:Succeeded; 77:Out → 97:In; 77:Out → 103:In |
| `q001_tbug_tutorial.questphase / h0 / 79` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_tut_ap_hacked_netrunner","value":1,"comparisonType":"GreaterOrEqual"}}}` | 78:Out → 79:In; 79:True → 81:Active; 79:False → 80:Active |
| `q001_tbug_tutorial.questphase / h0 / 82` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_tut_ap_hacked_netrunner","value":1,"comparisonType":"GreaterOrEqual"}}}` | 39:Out → 82:In; 82:True → 84:Succeeded; 82:False → 83:Succeeded |
| `q001_tbug_tutorial.questphase / h0 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_tut_equip_upload_part_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 87:Out → 6:Succeeded; 86:Out → 87:In |
| `q001_tbug_tutorial.questphase / h0 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q001_exercise_device_quickhack","deviceControllerClass":"SurveillanceCameraControllerPS","deviceConditionFunction":"WasQuickHackJustPerformed","functionParameters":[{"$type":"questDevice_ConditionFunctionParameter","name":"quickHackName","value":{"$type":"Variant","$rawData":"DwAGAAAAlwA="}}]}}}` | 80:Out → 89:In; 81:Out → 89:In; 89:Out → 85:In |
| `q001_tbug_tutorial.questphase / h0 / 91` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ping_installed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 91:Out → 61:In; 90:Out → 91:In; 91:Out → 96:In |
| `q001_tbug_tutorial.questphase / h0 / 102` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"75582890960","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 98:Out → 102:In; 102:Out → 99:In |
| `q001_tbug_tutorial.questphase / h0 / 105` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"93763639497","value":false}},{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"HasCyberdeck","value":1.0,"comparisonType":"GreaterOrEqual"}}]}}` | 105:Out → 13:In; 106:Out → 105:In; 105:Out → 109:In |
| `q001_tbug_tutorial.questphase / h0 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"93763639497","value":false}}}` | 107:Out → 98:In; 106:Out → 107:In |
| `q001_tbug_tutorial.questphase / h0 / 108` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"118585379367"}},{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"HasCyberdeck","value":1.0,"comparisonType":"GreaterOrEqual"}}]}}` | 108:Out → 19:In; 108:Out → 20:In; 108:Out → 53:In; 108:Out → 69:In; 119:CutSource → 108:CutDestination; 109:Out → 108:In; 117:Out → 108:In; 108:Out → 117:In |
| `q001_tbug_tutorial.questphase / h0 / 111` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"HasCyberdeck","value":1.0,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 111:In; 111:True → 116:In1; 111:False → 115:In |
| `q001_tbug_tutorial.questphase / h0 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questStat_ConditionType","entityRef":{"$type":"questUniversalRef"},"statType":"HasCyberdeck","value":1.0,"comparisonType":"GreaterOrEqual"}}}` | 112:Out → 113:In; 113:Out → 116:In1 |
| `q001_tbug_tutorial.questphase / h0 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 13:Out → 114:In; 114:Out → 65:In; 69:CutSource → 114:CutDestination |
| `q001_tbug_tutorial.questphase / h0 / 117` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questUICondition","type":{"$type":"questUIElement_ConditionType","element":"118585379367","value":false}}]}}` | 117:Out → 108:In; 108:Out → 117:In; 119:CutSource → 117:CutDestination; 117:Out → 118:In; 117:Out → 120:In |
| `q001_tbug_tutorial.questphase / h0 / 119` | `questCutControlNodeDefinition` `{}` | 53:Out → 119:In; 119:CutSource → 108:CutDestination; 119:CutSource → 117:CutDestination |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `conditional_route` | q001_tbug_tutorial.questphase / h0 / 50; q001_tbug_tutorial.questphase / h0 / 53; q001_tbug_tutorial.questphase / h0 / 75; q001_tbug_tutorial.questphase / h0 / 77; +4 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | q001_tbug_tutorial.questphase / h0 / 37; q001_tbug_tutorial.questphase / h0 / 9 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | q001_tbug_tutorial.questphase / h0 / 10; q001_tbug_tutorial.questphase / h0 / 27; q001_tbug_tutorial.questphase / h0 / 39; q001_tbug_tutorial.questphase / h0 / 89 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `item_state` | q001_tbug_tutorial.questphase / h0 / 102; q001_tbug_tutorial.questphase / h0 / 5 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `persistent_decision` | q001_tbug_tutorial.questphase / h0 / 115; q001_tbug_tutorial.questphase / h0 / 49; q001_tbug_tutorial.questphase / h0 / 51; q001_tbug_tutorial.questphase / h0 / 54; +4 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | q001_tbug_tutorial.questphase / h0 / 114 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | q001_tbug_tutorial.questphase / h0 / 119; q001_tbug_tutorial.questphase / h0 / 29; q001_tbug_tutorial.questphase / h0 / 69; q001_tbug_tutorial.questphase / h0 / 72; +1 locations in catalogue.json | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\main_quests\prologue\q001\phases\q001_tbug_tutorial.questphase` | content candidate; journal anchor | `base-q001` |

Evidence shards for this dossier (including parent context): [base-q001](../../../../../reference/quests/deep-dives/catalogue/evidence/base-q001.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
