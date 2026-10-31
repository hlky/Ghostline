# Water Runs Dry

Journal: `ep1/quests/minor_quest/mq300_safehouse` · `MinorQuest` · hash `798598778`.

**Coverage: POI-linked; quest activation unresolved.** 1 exact POI-linked nodes in 1 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Look for clues to get the water running. (Primary) | `ep1/quests/minor_quest/mq300_safehouse/mq300_safehouse/01_look_for_clues_to_fix_the_water` |
| Scan the pipes. (Primary) | `ep1/quests/minor_quest/mq300_safehouse/mq300_safehouse/02_scan_the_pipes` |
| Follow the pipes. (Primary) | `ep1/quests/minor_quest/mq300_safehouse/mq300_safehouse/03_follow_the_pipes` |
| Fix the pump. (Primary) | `ep1/quests/minor_quest/mq300_safehouse/mq300_safehouse/04_fix_water` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq300.questphase / h302 / 7` (Journal) | `ep1/points_of_interest/minor_quests/mq300_safehouse` | 19:Out → 7:Active; 7:Out → 12:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq300.questphase / h68 / 3` | `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene`; `#mq300_sm_safehouse_interactions` | 2:Out → 3:Start 0; 5:CutSource → 3:CutDestination |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\quest\ep1_persistent_content.questphase` / h17 / 4 | `mq300.questphase` | 5: PauseCondition: q302_squat_sh_unlocked GreaterOrEqual 1; 5:Out → 4:In1 |
| `ep1\quest\minor_quests\mq300\mq300.quest` / h0 / 1 | `mq300.questphase` | 3: FactsDBManager: mq300_smoking_unlocked; 3:Out → 1:In1 |
| `ep1\quest\minor_quests\mq300\mq300.questphase` / h68 / 3 | `mq300_safehouse_interactions.scene` | 2: PauseCondition: #mq300_safehouse_trigger; 5: CutControl; 2:Out → 3:Start 0; 5:CutSource → 3:CutDestination |
| `ep1\quest\ep1_additional_game_elements.questphase` / h0 / 2 | `ep1_persistent_content.questphase` | 0: Input; 15: Input; 0:Out → 2:In1; 15:Out → 2:growl |
| `ep1\openworld\ep1_open_world.quest` / h0 / 26 | `ep1_additional_game_elements.questphase` | 2: PauseCondition: {"seconds": 1}; 2:Out → 26:In1 |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 10 | `ep1_additional_game_elements.questphase` | 6: FactsDBManager: ep1_side_content; 6:Out → 10:In1 |
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_sandbox_activity.quest` / h0 / 5 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 5:In1 |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest` / h0 / 16 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 16:In1 |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest` / h0 / 20 | `ep1_additional_game_elements.questphase` | 0: Start; 0:Out → 20:In1 |
| `ep1\quest\ep1.questphase` / h58 / 4 | `ep1_additional_game_elements.questphase` | 2: Phase: ep1_bugfixing.questphase; 2: Phase: ep1_bugfixing.questphase; 9: CutControl; 7: PauseCondition: ep1_active GreaterOrEqual 1; 2:Out1 → 4:In2; 2:growl → 4:growl; 9:CutSource → 4:CutDestination; 7:Out → 4:In1 |
| `ep1\quest\main_quests\q301\q301.quest` / h0 / 13 | `ep1_additional_game_elements.questphase` | 4: CharacterManager; 4:Out → 13:In1 |
| `ep1\quest\main_quests\q302\q302.quest` / h0 / 6 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 6:In1 |
| `ep1\quest\main_quests\q303\q303.quest` / h0 / 4 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 4:In1 |
| `ep1\quest\main_quests\q304\q304.quest` / h0 / 5 | `ep1_additional_game_elements.questphase` | 12: Checkpoint; 12:Out → 5:In1 |
| `ep1\quest\main_quests\q305\q305.quest` / h0 / 4 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 4:In1 |
| `ep1\quest\main_quests\q306\q306.quest` / h354 / 3 | `ep1_additional_game_elements.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 2 | `ep1_additional_game_elements.questphase` | 4: LogicalHub; 10: CutControl; 4:Out1 → 2:In1; 10:CutSource → 2:CutDestination |
| `ep1\quest\minor_quests\mq301\mq301.quest` / h0 / 6 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 6:In1 |
| `ep1\quest\minor_quests\mq303\mq303.quest` / h95 / 3 | `ep1_additional_game_elements.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 2 | `ep1_additional_game_elements.questphase` | 4: LogicalHub; 4:Out1 → 2:In1 |
| `ep1\quest\minor_quests\mq305\mq305.quest` / h0 / 5 | `ep1_additional_game_elements.questphase` | 1: Start; 1:Out → 5:In1 |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq300_safehouse_interactions.scene` | Start 0, idris_shot →  | johnny_mirror; v_male_tpp; v_female_tpp; Johnny; idris_shot_myers; idris_shot_reed; idris_shot_kurt; idris_shot_songbird; idris_shot_johnny; idris_shot_additional_npc; Player; 294 nodes / 347 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq300_safehouse_interactions.scene / n10 / 0` | [PL][idź spać] (`sleep`) | No option-level predicate stored | 0:0 → 31:0:1 |
| `mq300_safehouse_interactions.scene / n58 / 0` | [PL][przejrzyj się w lustrze] (`mirror`) | No option-level predicate stored | 0:0 → 60:0:0; 0:0 → 142:0:1; 0:0 → 180:0:1 |
| `mq300_safehouse_interactions.scene / n66 / 0` | [PL][przestań się przeglądać] (`leave`) | No option-level predicate stored | 0:0 → 68:0:0; 0:0 → 160:0:1; 0:0 → 186:1:0; 0:0 → 204:1:0 |
| `mq300_safehouse_interactions.scene / n186 / 0` | [Happy] (`smile`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mirror_interactions_facials"}}} | 0:0 → 194:0:0 |
| `mq300_safehouse_interactions.scene / n186 / 1` | [Angry] (`frown`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mirror_interactions_facials"}}} | 0:1 → 196:0:0 |
| `mq300_safehouse_interactions.scene / n186 / 2` | [Sad] (`sadness`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mirror_interactions_facials"}}} | 0:2 → 198:0:0 |
| `mq300_safehouse_interactions.scene / n186 / 3` | [Surprised] (`surprise`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mirror_interactions_facials"}}} | 0:3 → 200:0:0 |
| `mq300_safehouse_interactions.scene / n186 / 4` | [Neutral] (`neutral`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mirror_interactions_facials"}}} | 0:4 → 202:0:0 |
| `mq300_safehouse_interactions.scene / n186 / 5` | [Go back] (`back`) | No option-level predicate stored | 0:5 → 208:0:0 |
| `mq300_safehouse_interactions.scene / n204 / 0` | [Enable the hairdresser] (`hairdresser`) | No option-level predicate stored | 0:0 → 206:0:0 |
| `mq300_safehouse_interactions.scene / n204 / 1` | [Make faces] (`facial`) | No option-level predicate stored | 0:1 → 186:0:0 |
| `mq300_safehouse_interactions.scene / n331 / 0` | [Use wardrobe] (`wardrobe`) | No option-level predicate stored | 0:0 → 333:0:1 |
| `mq300_safehouse_interactions.scene / n347 / 0` | [PL][włącz prysznic] (`shower`) | No option-level predicate stored | 0:0 → 381:0:1 |
| `mq300_safehouse_interactions.scene / n373 / 0` | [PL][wyłącz prysznic] (`shower`) | No option-level predicate stored | 0:0 → 393:0:1 |
| `mq300_safehouse_interactions.scene / n419 / 0` | [Lean] (`lean`) | No option-level predicate stored | 0:0 → 421:0:0 |
| `mq300_safehouse_interactions.scene / n426 / 0` | [Smoke a cigarette] (`smoke`) | No option-level predicate stored | 0:0 → 429:0:0; 0:0 → 1330:0:0 |
| `mq300_safehouse_interactions.scene / n426 / 1` | [Lean Back] (`lean_back`) | No option-level predicate stored | 0:1 → 432:0:0; 0:1 → 1046:0:0 |
| `mq300_safehouse_interactions.scene / n454 / 0` | [Sit] (`sit`) | No option-level predicate stored | 0:0 → 1358:0:1 |
| `mq300_safehouse_interactions.scene / n458 / 0` | [stand up] (`stand`) | No option-level predicate stored | 0:0 → 460:0:0 |
| `mq300_safehouse_interactions.scene / n468 / 0` | [meditate] (`meditate`) | No option-level predicate stored | 0:0 → 501:0:1 |
| `mq300_safehouse_interactions.scene / n480 / 0` | [Stop meditating] (`stop_meditation`) | No option-level predicate stored | 0:0 → 476:0:0 |
| `mq300_safehouse_interactions.scene / n521 / 0` | [dance] (`dance`) | {"questCondition": {"$type": "questObjectCondition", "type": {"$type": "questDevice_ConditionType", "objectRef": "#mq300_radio", "deviceControllerClass": "RadioControllerPS", "deviceConditionFunction": "IsON"}}} | 0:0 → 524:0:0 |
| `mq300_safehouse_interactions.scene / n529 / 0` | [stop dancing] (`stop_dance`) | No option-level predicate stored | 0:0 → 531:0:0; 0:0 → 1300:0:1 |
| `mq300_safehouse_interactions.scene / n694 / 0` | [look at] Boiler ...? (`hydro`) | No option-level predicate stored | 0:0 → 696:0:0 |
| `mq300_safehouse_interactions.scene / n698 / 0` | [fix the boiler] Let's try ... (`fix pomp`) | No option-level predicate stored | 0:0 → 700:0:0 |
| `mq300_safehouse_interactions.scene / n698 / 1` | [PL][napraw pompę] A to ciekawe. (`pomp techie`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "buildId": "85601791440", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 736:0:0 |
| `mq300_safehouse_interactions.scene / n1252 / 0` | [Take a drag] (`drag`) | No option-level predicate stored | 0:0 → 448:0:0 |
| `mq300_safehouse_interactions.scene / n1252 / 1` | [Stop smoking] (`throw_smoke`) | No option-level predicate stored | 0:1 → 443:0:0; 0:1 → 562:1:0; 0:1 → 563:1:0 |
| `mq300_safehouse_interactions.scene / n1372 / 0` | Text join unresolved (`Option`) | No option-level predicate stored | 0:0 → 1374:0:1; 0:0 → 1375:0:1; 0:0 → 1377:0:1; 0:0 → 1379:0:1; 0:0 → 1381:0:1; 0:0 → 1509:0:1; 0:0 → 1519:0:1; 0:0 → 1522:0:1 |
| `mq300_safehouse_interactions.scene / n1488 / 0` | Text join unresolved (`Option`) | No option-level predicate stored | 0:0 → 1399:0:1; 0:0 → 1516:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `censorship_nudity` | Producer outside selected context | mq300_safehouse_interactions.scene / scene / 385 |
| `holo_setup_active` | Producer outside selected context | mq300.questphase / h68 / 31 |
| `holo_setup_ended` | Producer outside selected context | mq300.questphase / h68 / 31 |
| `holo_setup_started` | Producer outside selected context | mq300.questphase / h68 / 31 |
| `idris_in_engine_scene_record` | Producer outside selected context | mq300_safehouse_interactions.scene / scene / 1424 |
| `idris_in_engine_shot` | Producer outside selected context | mq300.questphase / h68 / 9; mq300_safehouse_interactions.scene / scene / 1358 |
| `johnny_mirror` | mq300_safehouse_interactions.scene / scene / 146; mq300_safehouse_interactions.scene / scene / 162 | mq300_safehouse_interactions.scene / scene / 160; mq300_safehouse_interactions.scene / scene / 192 |
| `mirror_interactions_facials` | Producer outside selected context | mq300_safehouse_interactions.scene / scene / 186 |
| `mq014_done` | Producer outside selected context | mq300_safehouse_interactions.scene / scene / 1024 |
| `mq055_02_active` | Producer outside selected context | mq300.questphase / h68 / 31 |
| `mq300_smoking_unlocked` | Producer outside selected context | mq300_safehouse_interactions.scene / scene / 1336; mq300_safehouse_interactions.scene / scene / 1339 |
| `mq300_squot_cleanup_active` | mq300.questphase / h68 / 10 | mq300.questphase / h68 / 11 |
| `mq300_testing` | Producer outside selected context | mq300.questphase / h0 / 10 |
| `q101_done` | Producer outside selected context | mq300_safehouse_interactions.scene / scene / 142 |
| `q302_07_oath_ow_community` | Producer outside selected context | mq300.questphase / h226 / 6 |
| `q302_done` | Producer outside selected context | mq300.questphase / h68 / 22 |
| `q302_hydro_fixed` | mq300_safehouse_interactions.scene / scene / 712 | mq300_safehouse_interactions.scene / scene / 773; mq300_safehouse_interactions.scene / scene / 804 |
| `q302_hydrophore_done` | mq300_safehouse_interactions.scene / scene / 1097 | No reader in selected context |
| `q302_pipes_done` | mq300_safehouse_interactions.scene / scene / 1100 | No reader in selected context |
| `q302_pump_done` | mq300_safehouse_interactions.scene / scene / 1103 | No reader in selected context |
| `q302_squat_bed_switched` | mq300.questphase / h226 / 12 | mq300_safehouse_interactions.scene / scene / 1150 |
| `q302_squat_fixed` | Producer outside selected context | mq300.questphase / h226 / 7 |
| `q302_squat_sh_unlocked` | Producer outside selected context | mq300.questphase / h226 / 9; mq300_safehouse_interactions.scene / scene / 1114; mq300_safehouse_interactions.scene / scene / 764 |
| `q302_squot_fix` | mq300_safehouse_interactions.scene / scene / 708 | mq300.questphase / h9 / 8; mq300_safehouse_interactions.scene / scene / 1114; mq300_safehouse_interactions.scene / scene / 1319 |
| `q302_squot_progress` | mq300_safehouse_interactions.scene / scene / 922; mq300_safehouse_interactions.scene / scene / 948; mq300_safehouse_interactions.scene / scene / 959 | mq300_safehouse_interactions.scene / scene / 1304; mq300_safehouse_interactions.scene / scene / 1307; mq300_safehouse_interactions.scene / scene / 1311; mq300_safehouse_interactions.scene / scene / 1315 |
| `q302_water_fixed_after_quest` | mq300_safehouse_interactions.scene / scene / 912 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>74 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq300.questphase / h0 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq300_testing"}}}` | 0:Out → 10:In; 10:True → 12:In1; 10:False → 15:In1 |
| `mq300.questphase / h9 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squot_fix","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 8:In; 8:Out → 3:In |
| `mq300.questphase / h68 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq300_safehouse_trigger"}}` | 6:Out → 2:In; 2:Out → 7:In; 2:Out → 3:Start 0; 2:Out → 11:In |
| `mq300.questphase / h68 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq300_safehouse_trigger"}}` | 7:Out → 4:In; 4:Out → 6:In; 4:Out → 9:In; 4:Out → 22:In |
| `mq300.questphase / h68 / 5` | `questCutControlNodeDefinition` `{}` | 5:CutSource → 3:CutDestination; 9:False → 5:In |
| `mq300.questphase / h68 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 0:Out → 6:In; 6:Out → 2:In; 4:Out → 6:In |
| `mq300.questphase / h68 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 2:Out → 7:In; 7:Out → 4:In |
| `mq300.questphase / h68 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"idris_in_engine_shot"}}}` | 4:Out → 9:In; 9:False → 5:In |
| `mq300.questphase / h68 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq300_squot_cleanup_active"}}}` | 2:Out → 11:In; 11:True → 25:In |
| `mq300.questphase / h68 / 22` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_done"}}}` | 4:Out → 22:In; 22:True → 10:In |
| `mq300.questphase / h68 / 31` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq055_02_active","comparisonType":"Equal"}},{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","comparisonType":"Equal"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","comparisonType":"Equal"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_ended","value":1,"comparisonType":"Equal"}}]}]}}` | 28:Out → 31:In; 31:True → 32:In |
| `mq300.questphase / h226 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq300_safehouse_trigger"}}` | 7:Out → 5:In; 5:Out → 8:In |
| `mq300.questphase / h226 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_07_oath_ow_community","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 6:In; 6:Out → 7:In |
| `mq300.questphase / h226 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squat_fixed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 5:In; 6:Out → 7:In |
| `mq300.questphase / h226 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squat_sh_unlocked","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 9:In; 9:Out → 10:In |
| `mq300.questphase / h226 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq300_safehouse_trigger"}}` | 9:Out → 10:In; 10:Out → 11:In |
| `mq300_safehouse_interactions.scene / scene / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 27:0:0 → 53:0:0; 41:0:0 → 27:0:1 |
| `mq300_safehouse_interactions.scene / scene / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":1}}}` | 15:0:0 → 39:0:1; 39:0:0 → 29:0:1; 41:1:0 → 39:0:0 |
| `mq300_safehouse_interactions.scene / scene / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 68:0:0 → 74:0:1; 74:0:0 → 116:0:0; 74:0:0 → 184:0:1 |
| `mq300_safehouse_interactions.scene / scene / 76` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterBodyType_CondtionType","isPlayer":true}}}` | 76:0:0 → 126:0:1; 76:0:1 → 130:0:1; 142:0:0 → 76:0:1; 144:0:0 → 76:0:1; 144:0:1 → 76:0:1; 144:0:2 → 76:0:1; 144:0:3 → 76:0:1 |
| `mq300_safehouse_interactions.scene / scene / 90` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterBodyType_CondtionType","isPlayer":true}}}` | 90:0:0 → 658:0:0; 90:0:1 → 664:0:0; 160:0:0 → 90:0:1 |
| `mq300_safehouse_interactions.scene / scene / 120` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 118:0:0 → 120:0:1; 120:0:0 → 112:0:1 |
| `mq300_safehouse_interactions.scene / scene / 124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 122:0:0 → 124:0:1; 124:0:0 → 114:0:1 |
| `mq300_safehouse_interactions.scene / scene / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq300_safehouse_interactions_v_female_tpp"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 126:0:0 → 128:0:1; 128:0:0 → 104:0:1; 128:0:0 → 616:0:0 |
| `mq300_safehouse_interactions.scene / scene / 132` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq300_safehouse_interactions_v_male_tpp"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 130:0:0 → 132:0:1; 132:0:0 → 106:0:1; 132:0:0 → 622:0:0 |
| `mq300_safehouse_interactions.scene / scene / 138` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 108:0:0 → 138:0:1; 138:0:0 → 134:0:1 |
| `mq300_safehouse_interactions.scene / scene / 140` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 110:0:0 → 140:0:1; 140:0:0 → 136:0:1 |
| `mq300_safehouse_interactions.scene / scene / 142` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_done","comparisonType":"Equal"}}}` | 58:0:0 → 142:0:1; 142:0:0 → 76:0:1; 142:0:1 → 144:0:0 |
| `mq300_safehouse_interactions.scene / scene / 158` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq300_safehouse_interactions_johnny_mirror"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 156:0:0 → 158:0:1; 158:0:0 → 154:0:1; 158:0:0 → 649:0:0 |
| `mq300_safehouse_interactions.scene / scene / 160` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"johnny_mirror","comparisonType":"Equal"}}}` | 66:0:0 → 160:0:1; 160:0:0 → 90:0:1; 160:0:1 → 162:0:1 |
| `mq300_safehouse_interactions.scene / scene / 174` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 170:0:0 → 174:0:1; 174:0:0 → 172:0:1 |
| `mq300_safehouse_interactions.scene / scene / 192` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"johnny_mirror"}}}` | 60:0:0 → 192:0:1; 192:0:1 → 204:0:0 |
| `mq300_safehouse_interactions.scene / scene / 335` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 333:0:0 → 335:0:1; 335:0:0 → 337:0:0 |
| `mq300_safehouse_interactions.scene / scene / 355` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 355:0:0 → 347:0:0; 1012:0:0 → 355:0:1 |
| `mq300_safehouse_interactions.scene / scene / 385` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_nudity"}}}` | 381:0:0 → 385:0:1; 385:0:0 → 387:0:1; 385:0:1 → 389:0:1 |
| `mq300_safehouse_interactions.scene / scene / 437` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 432:0:0 → 437:0:1; 437:0:0 → 419:0:0 |
| `mq300_safehouse_interactions.scene / scene / 462` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 460:0:0 → 462:0:1; 462:0:0 → 454:0:0 |
| `mq300_safehouse_interactions.scene / scene / 481` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 481:0:0 → 480:0:0; 518:0:0 → 481:0:1 |
| `mq300_safehouse_interactions.scene / scene / 485` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 485:0:0 → 468:0:0; 504:0:0 → 485:0:1 |
| `mq300_safehouse_interactions.scene / scene / 535` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 531:0:0 → 535:0:1; 535:0:0 → 521:0:0 |
| `mq300_safehouse_interactions.scene / scene / 587` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq300_safehouse_interactions_johnny_mirror"},"onScreenTest":true,"inverted":true}}}` | 587:0:0 → 570:0:0; 1046:0:0 → 587:0:1 |
| `mq300_safehouse_interactions.scene / scene / 602` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq300_radio","deviceControllerClass":"RadioControllerPS","deviceConditionFunction":"IsOFF"}}}` | 602:0:0 → 521:1:0; 602:0:0 → 603:0:1; 603:0:0 → 602:0:1 |
| `mq300_safehouse_interactions.scene / scene / 603` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq300_radio","deviceControllerClass":"RadioControllerPS","deviceConditionFunction":"IsON"}}}` | 602:0:0 → 603:0:1; 603:0:0 → 521:0:0; 603:0:0 → 602:0:1; 605:0:0 → 603:0:1 |
| `mq300_safehouse_interactions.scene / scene / 716` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q302_water_pump"},"eventType":"Finished"}}}` | 716:0:0 → 728:0:1; 948:0:0 → 716:0:1; 1311:0:0 → 716:0:1 |
| `mq300_safehouse_interactions.scene / scene / 726` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q302_water_pipes_part_1"},"eventType":"Finished"}},{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q302_water_pipes_part_2"},"eventType":"Finished"}}]}}` | 726:0:0 → 734:0:0; 922:0:0 → 726:0:1; 1307:0:0 → 726:0:1 |
| `mq300_safehouse_interactions.scene / scene / 764` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squat_sh_unlocked","value":1,"comparisonType":"GreaterOrEqual"}}}` | 1:0:0 → 764:0:1; 764:0:0 → 12:0:0 |
| `mq300_safehouse_interactions.scene / scene / 773` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_hydro_fixed"}}}` | 773:0:0 → 349:0:0; 773:0:1 → 776:0:0; 995:0:0 → 773:0:1 |
| `mq300_safehouse_interactions.scene / scene / 804` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_hydro_fixed"}}}` | 791:0:0 → 804:0:1; 804:0:0 → 912:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1024` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq014_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 12:0:5 → 1024:0:1; 1024:0:0 → 468:0:0 |
| `mq300_safehouse_interactions.scene / scene / 1114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squat_sh_unlocked","value":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squot_fix","value":1,"comparisonType":"GreaterOrEqual"}}]}}` | 1:0:0 → 1114:0:1; 1114:0:0 → 347:0:0 |
| `mq300_safehouse_interactions.scene / scene / 1150` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squat_bed_switched","value":1,"comparisonType":"GreaterOrEqual"}}}` | 12:0:2 → 1150:0:1; 1150:0:0 → 10:0:0 |
| `mq300_safehouse_interactions.scene / scene / 1174` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 1172:0:0 → 1174:0:1; 1174:0:0 → 1176:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1178` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":300}}}` | 1176:0:0 → 1178:0:1; 1178:0:0 → 1182:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1184` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":400}}}` | 1182:0:0 → 1184:0:1; 1184:0:0 → 1186:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1188` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 1186:0:0 → 1188:0:1; 1188:0:0 → 1194:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1196` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":600}}}` | 1194:0:0 → 1196:0:1; 1196:0:0 → 1198:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1200` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 1198:0:0 → 1200:0:1; 1200:0:0 → 1206:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1211` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/main_quest/q302_reed/07_oath/06_wait_for_reed_to_leave","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 1211:0:0 → 1224:0:1; 1220:0:0 → 1211:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1214` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/main_quest/q302_reed/07_oath/06a_leave_building","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 1214:0:0 → 1216:0:1; 1220:0:0 → 1214:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1224` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 1211:0:0 → 1224:0:1; 1224:0:0 → 1216:0:0 |
| `mq300_safehouse_interactions.scene / scene / 1294` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1294:0:0 → 1243:0:0; 1330:0:0 → 1294:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1300` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 529:0:0 → 1300:0:1; 1300:0:0 → 524:1:0 |
| `mq300_safehouse_interactions.scene / scene / 1304` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squot_progress","value":1,"comparisonType":"Less"}}}` | 1304:0:0 → 1063:0:1; 1304:0:1 → 1307:0:1; 1319:0:0 → 1304:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1307` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squot_progress","value":1,"comparisonType":"Equal"}}}` | 1304:0:1 → 1307:0:1; 1307:0:0 → 726:0:1; 1307:0:1 → 1311:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1311` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squot_progress","value":2,"comparisonType":"Equal"}}}` | 1307:0:1 → 1311:0:1; 1311:0:0 → 716:0:1; 1311:0:1 → 1315:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1315` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squot_progress","value":3,"comparisonType":"Equal"}}}` | 1311:0:1 → 1315:0:1; 1315:0:0 → 698:0:0 |
| `mq300_safehouse_interactions.scene / scene / 1319` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_squot_fix","value":1,"comparisonType":"Less"}}}` | 1:0:0 → 1319:0:1; 1319:0:0 → 1304:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1336` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq300_smoking_unlocked","value":1,"comparisonType":"GreaterOrEqual"}}}` | 1336:0:0 → 1343:0:0; 1339:0:1 → 1336:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1339` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq300_smoking_unlocked","value":1,"comparisonType":"GreaterOrEqual"}}}` | 12:0:3 → 1339:0:1; 1339:0:0 → 1343:0:0; 1339:0:1 → 1336:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1358` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"idris_in_engine_shot"}}}` | 454:0:0 → 1358:0:1; 1358:0:0 → 1364:0:1; 1358:0:1 → 456:0:0 |
| `mq300_safehouse_interactions.scene / scene / 1366` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1364:0:0 → 1366:0:1; 1366:0:0 → 1372:0:0 |
| `mq300_safehouse_interactions.scene / scene / 1394` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1388:0:0 → 1394:0:1; 1394:0:0 → 1422:0:1; 1394:0:0 → 1432:0:1; 1394:0:0 → 1442:0:1; 1394:0:0 → 1446:0:1; 1394:0:0 → 1465:0:1; 1394:0:0 → 1526:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1424` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"idris_in_engine_scene_record"}}}` | 1424:0:0 → 1423:0:1; 1424:0:1 → 1420:0:0; 1435:0:0 → 1424:0:1 |
| `mq300_safehouse_interactions.scene / scene / 1435` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1435:0:0 → 1424:0:1; 1478:0:0 → 1435:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq300_safehouse_interactions.scene / scene / 128; mq300_safehouse_interactions.scene / scene / 132; mq300_safehouse_interactions.scene / scene / 158 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | mq300.questphase / h68 / 21 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq300_safehouse_interactions.scene / scene / 10; mq300_safehouse_interactions.scene / scene / 1252; mq300_safehouse_interactions.scene / scene / 1372; mq300_safehouse_interactions.scene / scene / 1488; +17 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | mq300.questphase / h0 / 10; mq300.questphase / h226 / 6; mq300.questphase / h226 / 7; mq300.questphase / h226 / 9; +25 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq300.questphase / h68 / 32 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq300.questphase / h9 / 10; mq300.questphase / h9 / 11; mq300_safehouse_interactions.scene / scene / 1063; mq300_safehouse_interactions.scene / scene / 1072; +17 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | mq300.questphase / h302 / 12; mq300.questphase / h9 / 13; mq300.questphase / h9 / 3; mq300.questphase / h9 / 5; +2 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | mq300_safehouse_interactions.scene / scene / 521; mq300_safehouse_interactions.scene / scene / 602; mq300_safehouse_interactions.scene / scene / 603 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | mq300_safehouse_interactions.scene / scene / 39 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | mq300.questphase / h302 / 7 | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | mq300.questphase / h226 / 12; mq300.questphase / h68 / 10; mq300_safehouse_interactions.scene / scene / 1097; mq300_safehouse_interactions.scene / scene / 1100; +9 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | mq300.questphase / h68 / 6; mq300.questphase / h68 / 7; mq300_safehouse_interactions.scene / scene / 1174; mq300_safehouse_interactions.scene / scene / 1178; +24 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq300.questphase / h68 / 5 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `scan_evidence` | mq300_safehouse_interactions.scene / scene / 716; mq300_safehouse_interactions.scene / scene / 726 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | mq300.questphase / h68 / 3 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq300.questphase / h226 / 10; mq300.questphase / h226 / 5; mq300.questphase / h68 / 2; mq300.questphase / h68 / 4 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | mq300.questphase / h68 / 28 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq300_safehouse_interactions.scene / scene / 1234; mq300_safehouse_interactions.scene / scene / 1247; mq300_safehouse_interactions.scene / scene / 1266; mq300_safehouse_interactions.scene / scene / 1272; +33 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq300.questphase / h0 / 22; mq300.questphase / h226 / 11; mq300.questphase / h226 / 8; mq300_safehouse_interactions.scene / scene / 112; +7 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\quest\minor_quests\mq300\mq300.questphase` | content candidate; journal anchor | `ep1-mq300` |
| `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` | content candidate; forward dependency | `ep1-mq300` |

Evidence shards for this dossier (including parent context): [ep1-mq300](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq300.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-08.json.gz), [ep1-sts-ep1-13](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-13.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

257 repeated typed/socket path signatures in this selected graph context; 47 distinct direct resource identities; 4 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `0a00bd6805b0f812c475` | `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` / scene / 224 -> 218 -> 226 | scnRandomizerNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `eb7ff9b2d44adc239222` | `ep1\quest\minor_quests\mq300\mq300.questphase` / h226 / 0 -> 6 -> 7 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `2e0a7d7db4cf1ad4fa9a` | `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` / scene / 776 -> 783 -> 787 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]; 0:0 -> 0:0; 4:0 -> 0:1 |
| `dfd4d7249953e7dc9b66` | `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` / scene / 194 -> 188 -> 190 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId] -> scnHubNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `356028081b3ec12a534d` | `ep1\quest\minor_quests\mq300\mq300.questphase` / h0 / 0 -> 10 -> 12 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questLogicalHubNodeDefinition; Out -> In; True -> In1 |
| `2aa0f3a3b004f071652f` | `ep1\quest\minor_quests\mq300\mq300.questphase` / h226 / 5 -> 8 -> 1 | questPauseConditionNodeDefinition[questTriggerCondition] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `9142f4e54264697a790e` | `ep1\quest\minor_quests\mq300\mq300.questphase` / h9 / 0 -> 5 -> 13 | questInputNodeDefinition -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out -> In; Out -> In |
| `2c4762a122ece48d0e88` | `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` / scene / 1294 -> 1243 -> 563 | questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> scnRandomizerNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `32e7c7376e0b24455051` | `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` / scene / 773 -> 776 -> 783 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:1 -> 0:0; 0:0 -> 0:0 |
| `8530bf9138e338d3b6fa` | `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` / scene / 162 -> 670 -> 674 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]; 0:0 -> 0:0; 4:0 -> 0:1 |
| `c8b3108c074b0828457d` | `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` / scene / 128 -> 616 -> 1281 | questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `2e3e02f88d3445afaa5f` | `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` / scene / 700 -> 973 -> 712 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `ep1\quest\minor_quests\mq300\mq300.questphase` / h0 / 1 | `h9` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `ep1\quest\minor_quests\mq300\mq300.questphase` / h0 / 4 | `h68` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `ep1\quest\minor_quests\mq300\mq300.questphase` / h0 / 5 | `h226` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `ep1\quest\minor_quests\mq300\mq300.questphase` / h0 / 15 | `h302` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `ep1\quest\minor_quests\mq300\mq300.gamedef` | content candidate | ep1\quest\minor_quests\mq300\mq300.quest |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq303\mq303.gamedef` | content candidate | ep1\quest\minor_quests\mq303\mq303.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq305\mq305.gamedef` | content candidate | ep1\quest\minor_quests\mq305\mq305.quest |
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
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_sandbox_activity_test.gamedef` | content candidate | ep1\openworld\sandbox_activities\courier_spot\ep1_courier_sandbox_activity.quest |
| `ep1\quest\ep1.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_nc_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_car_lean90__rl_on_seat__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_bar_lean0__2h_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_rail_lean0__lh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\female\body\player_locomotion_johnny_guitar.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__monk__sit_ground__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__sit_chair_lean180__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__monk__sit_ground__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__sit_chair_lean180__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand_rail_lean90__rh_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\male\body\player_locomotion_sick.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01_wakeup\body\q203_01_wakeup__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01_wakeup\body\q203_01_wakeup__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q105\q105_11_judys_evelyn\player__stand_rail_lean90__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q113\q113_06_saburo_office\body\q113_06_saburo_office__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q001\q001_01_wakeup\anim\body\q001_01_wakeup__female_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q001\q001_01_wakeup\anim\body\q001_01_wakeup__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q001\q001_01_wakeup\anim\body\q001_01_wakeup__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q001\q001_01_wakeup\anim\body\q001_01_wakeup__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q005\q005_15_no_tell_motel\anim\q005_15_no_tell_motel__player_animation.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q005\q005_15_no_tell_motel\anim\q005_15_no_tell_motel__player_ma_animation.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q005\q005_15_no_tell_motel\anim\q005_15_no_tell_motel__player_ma_tpp_animation.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q005\q005_15_no_tell_motel\anim\q005_15_no_tell_motel__player_wa_tpp_animation.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\workspots\archetype\monk\common\ground\monk__sit_ground__meditate__04.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_right__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\bar\johnny__stand_bar_lean_front__idle__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_car_lean_right__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\chair\player__sit_chair__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\ground\player__stand__dance__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_01_wakeup\player__stand_wall_lean_front_shower__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_01_wakeup\player__stand_wall_lean_front_shower_blood__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q105\q105_09_braindance_evelyn\johnny__stand__lean_front_rail__smoke_cigarette__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q105\q105_11_judys_evelyn\player__stand_rail_lean_right__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\prologue\q001\q001_01_wakeup\q001_01_wakeup_player_lie_bed_90__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\prologue\q005\q005_15_no_tell_motel\q005_15_no_tell_motel__player_at_the_sink.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\animations\marketing\live_action_reed\rid\live_action__reed__anim__01.scenerid` | asset binding .scenerid | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\quest\minor_quests\mq300\scenes\lipsync\en\mq300_safehouse_interactions\alex.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\minor_quests\mq300\scenes\lipsync\en\mq300_safehouse_interactions\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\minor_quests\mq300\scenes\lipsync\en\mq300_safehouse_interactions\kurtz.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\minor_quests\mq300\scenes\lipsync\en\mq300_safehouse_interactions\myers.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\minor_quests\mq300\scenes\lipsync\en\mq300_safehouse_interactions\reed.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\minor_quests\mq300\scenes\lipsync\en\mq300_safehouse_interactions\songbird.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\minor_quests\mq300\scenes\lipsync\en\mq300_safehouse_interactions\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_ended` | base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 57; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 58; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 61; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 478; 463 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `johnny_mirror` | base\quest\minor_quests\mq000\scenes\mq000_01_apartment.scene / scene / 988; base\quest\minor_quests\mq000\scenes\mq000_01_apartment.scene / scene / 1003; base\quest\minor_quests\mq055\scenes\mq055_05_downtown.scene / scene / 2443; dlc\dlc6_apart\loc_dlc6_apart_cct_dtn\quest\scenes\dlc6_apart_cct_dtn_interactions.scene / scene / 988; 11 total source locations in compressed evidence |
| `mirror_interactions_facials` | base\open_world\scenes\mirrors\mirror_interactions_control.questphase / h9 / 51; base\open_world\scenes\mirrors\mirror_scene_test.quest / h0 / 6; 2 total source locations in compressed evidence |
| `mq014_done` | base\quest\minor_quests\mq014\mq014.questphase / h3758 / 59; base\quest\minor_quests\mq033\mq033_tarot.quest / h0 / 28; base\quest\minor_quests\mq055\test\mq055_chicken.scene / scene / 154; 3 total source locations in compressed evidence |
| `mq055_02_active` | base\quest\minor_quests\mq055\phases\mq055_apartment.questphase / h0 / 13; base\quest\minor_quests\mq055\phases\mq055_apartment.questphase / h0 / 14; 2 total source locations in compressed evidence |
| `mq300_smoking_unlocked` | ep1\quest\minor_quests\mq300\mq300.quest / h0 / 3; ep1\quest\main_quests\q302\phases\q302_07_oath.questphase / h560 / 49; 2 total source locations in compressed evidence |
| `mq300_testing` | ep1\quest\minor_quests\mq300\mq300.quest / h0 / 2; ep1\quest\main_quests\q303\q303.quest / h11933 / 3; 2 total source locations in compressed evidence |
| `q101_done` | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\test\ma_wat_lch_06_chicken_test.scene / scene / 6; base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest / h0 / 24; base\quest\minor_quests\mq010\mq010.quest / h0 / 12; base\quest\minor_quests\mq018\phases\mq018_00_chickentest.questphase / h0 / 27; 51 total source locations in compressed evidence |
| `q302_07_oath_ow_community` | ep1\quest\main_quests\q302\phases\q302_07_oath.questphase / h315 / 51; ep1\quest\main_quests\q302\phases\q302_07_oath.questphase / h560 / 22; ep1\quest\main_quests\q302\phases\q302_07_oath.questphase / h1029 / 35; 3 total source locations in compressed evidence |
| `q302_done` | ep1\quest\minor_quests\mq304\test\mq304_chickentest.questphase / h0 / 16; ep1\quest\minor_quests\mq306\mq306.questphase / h201 / 8; ep1\quest\main_quests\q302\phases\q302_08_call.questphase / h0 / 29; ep1\quest\main_quests\q306\q306.quest / h212 / 5; 10 total source locations in compressed evidence |
| `q302_squat_sh_unlocked` | ep1\quest\main_quests\q302\scenes\q302_07_oath.scene / scene / 13217; ep1\quest\main_quests\q303\q303.quest / h11933 / 4; 2 total source locations in compressed evidence |

NodeRef uses: 147; TweakDB binding uses: 97. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene` | 42 / 223 | scnAudioEvent: 10; scnChangeIdleAnimEvent: 3; scnDialogLineEvent: 5; scnGameplayTransitionEvent: 11; scnIKEvent: 22; scnLookAtEvent: 11; scnPlayRidAnimEvent: 1; scnPlaySkAnimEvent: 58; scnUnmountEvent: 11; scneventsAttachPropToNode: 3; scneventsAttachPropToPerformer: 3; scneventsCameraParamsEvent: 2; scneventsPlayRidCameraAnimEvent: 1; scneventsSetAnimFeatureEvent: 11; scneventsSocket: 55; scneventsVFXEvent: 16 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
