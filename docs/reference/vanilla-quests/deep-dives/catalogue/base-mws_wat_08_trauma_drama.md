# Career Opportunities

Journal: `quests/minor_quest/mws_wat_08_trauma_drama` · `MinorQuest` · hash `3036379818`.

**Coverage: journal-linked.** 15 exact journal-linked nodes in 2 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Go to the Trauma Team netpage on your computer. (Primary) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/01_check_trauma_team_website` |
| Read the message from Macroware. (Primary) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/02_read_message_from_game_dev` |
| Go to the MedCenter to collect your consolation prize. (Primary) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/04_go_to_reward_location` |
| Scan your hand to confirm your identity. (Primary) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/05_scan_hand` |
| Collect your consolation prize. (Primary) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/06_take_your_reward` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mws_wat_08.questphase / h0 / 23` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/02_read_message_from_game_dev` | 66:Out → 23:Active; 23:Out → 59:Active |
| `mws_wat_08.questphase / h0 / 28` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/02_read_message_from_game_dev` | 72:Out → 28:Succeeded; 28:Out → 30:Active |
| `mws_wat_08.questphase / h0 / 30` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/01_check_trauma_team_website` | 30:Out → 10:In; 28:Out → 30:Active |
| `mws_wat_08.questphase / h0 / 31` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/01_check_trauma_team_website` | 92:Out → 31:Succeeded; 31:Out → 40:Active |
| `mws_wat_08.questphase / h0 / 32` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/02_read_message_from_game_dev` | 32:Out → 71:Active |
| `mws_wat_08.questphase / h0 / 34` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/02_read_message_from_game_dev` | 33:Out → 34:Succeeded |
| `mws_wat_08.questphase / h0 / 40` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/04_go_to_reward_location` | 40:Out → 12:In1; 31:Out → 40:Active |
| `mws_wat_08.questphase / h0 / 59` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/description` | 23:Out → 59:Active; 59:Out → 64:In |
| `mws_wat_08.questphase / h0 / 71` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/02_read_message_from_game_dev/contact` | 32:Out → 71:Active; 71:Out → 33:In |
| `mws_wat_08.scene / scene / 105` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/04_go_to_reward_location` | 83:2:0 → 105:0:3; 105:0:0 → 107:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mws_wat_08.scene / scene / 107` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/05_scan_hand` | 105:0:0 → 107:0:1; 107:0:0 → 314:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mws_wat_08.scene / scene / 112` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/05_scan_hand` | 75:0:0 → 112:0:3; 112:0:0 → 114:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mws_wat_08.scene / scene / 114` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/06_take_your_reward` | 112:0:0 → 114:0:1; 114:0:0 → 28:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mws_wat_08.scene / scene / 121` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/06_take_your_reward` | 121:0:0 → 125:0:3; 303:0:0 → 121:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mws_wat_08.scene / scene / 125` (Journal) | `quests/minor_quest/mws_wat_08_trauma_drama` | 121:0:0 → 125:0:3; 125:0:0 → 176:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mws_wat_08.questphase / h71 / 9` | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene`; `#mws_sm_wat_08` | 10:Out → 9:debug_teleport_in |
| `mws_wat_08.questphase / h89 / 7` | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene`; `#mws_sm_wat_08` | 7:out_trauma_team → 1:In; 8:Out1 → 7:in_trauma_team; 7:End1 → 9:In1 |
| `mws_wat_08.questphase / h214 / 8` | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene`; `#mws_sm_wat_08` | 4:Out → 8:in_av_toy_interaction; 8:out_av_toy_interaction → 9:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h71 / 9 | `mws_wat_08.scene` | 10: PauseCondition: mws_wat_08_collected_reward; 10:Out → 9:debug_teleport_in |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h89 / 7 | `mws_wat_08.scene` | 8: Phase; 7:out_trauma_team → 1:In; 8:Out1 → 7:in_trauma_team; 7:End1 → 9:In1 |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h214 / 8 | `mws_wat_08.scene` | 4: PauseCondition; 4:Out → 8:in_av_toy_interaction; 8:out_av_toy_interaction → 9:In |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mws_wat_08.scene` | in_trauma_team, debug_teleport_in, in_av_toy_interaction, chicken_in → out_trauma_team, out_av_toy_interaction, End1, test_toy_av_out, chicken_out | trauma_team_01; trauma_team_02; johnny; player; 85 nodes / 85 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mws_wat_08.scene / n10 / 0` | Text join unresolved (`Activate`) | No option-level predicate stored | 0:0 → 296:0:1; 0:0 → 337:0:1 |
| `mws_wat_08.scene / n28 / 0` | Text join unresolved (`Open`) | No option-level predicate stored | 0:0 → 32:666:1; 0:0 → 41:0:1; 0:0 → 51:666:1; 0:0 → 366:0:1 |
| `mws_wat_08.scene / n239 / 0` | [DEBUG ONLY] Teleport me to my apartment (`tele`) | No option-level predicate stored | 0:0 → 271:0:1 |
| `mws_wat_08.scene / n239 / 1` | [DEBUG ONLY] Don't teleport (`dont`) | No option-level predicate stored | No matching 0:ordinal output; inspect raw stamps |
| `mws_wat_08.scene / n260 / 0` | [DEBUG ONLY] Skip playing Trauma Drama game (`skip`) | No option-level predicate stored | 0:0 → 241:0:1 |
| `mws_wat_08.scene / n260 / 1` | [DEBUG ONLY] Don't skip Trauma Drama game (`dont`) | No option-level predicate stored | 0:1 → 282:0:1 |
| `mws_wat_08.scene / n260 / 2` | [DEBUG ONLY] Test Toy AV (`test_Av`) | No option-level predicate stored | 0:2 → 327:0:1 |
| `mws_wat_08.scene / n314 / 0` | [Zeskanuj dłoń] (`scan_hand`) | No option-level predicate stored | 0:0 → 74:0:1; 0:0 → 155:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `disable_tutorials` | mws_wat_08.scene / scene / 278 | No reader in selected context |
| `mws_wat_08_activate_trauma_drama_section` | mws_wat_08.questphase / h0 / 72 | mws_wat_08.questphase / h0 / 86 |
| `mws_wat_08_collected_reward` | mws_wat_08.scene / scene / 303 | mws_wat_08.questphase / h71 / 10 |
| `mws_wat_08_debug_run` | Producer outside selected context | mws_wat_08.questphase / h71 / 8 |
| `mws_wat_08_done` | mws_wat_08.questphase / h71 / 7 | No reader in selected context |
| `mws_wat_08_started` | mws_wat_08.questphase / h0 / 66 | No reader in selected context |
| `mws_wat_08_trauma_team_tried_to_apply` | Producer outside selected context | mws_wat_08.questphase / h0 / 10 |
| `mws_wat_av_toy_used_spline` | mws_wat_08.scene / scene / 217; mws_wat_08.scene / scene / 218; mws_wat_08.scene / scene / 220 | mws_wat_08.scene / scene / 228 |
| `q101_enable_side_content` | Producer outside selected context | mws_wat_08.scene / scene / 366 |
| `shooter_appeared_on_leaderboard` | mws_wat_08.scene / scene / 241 | mws_wat_08.questphase / h0 / 6 |
| `shooter_position_1` | mws_wat_08.scene / scene / 243 | mws_wat_08.questphase / h0 / 8 |

## Exact gates, joins and cancellation

<details><summary>40 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mws_wat_08.questphase / h0 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"shooter_appeared_on_leaderboard"}}}` | 0:Out → 6:In; 6:Out → 68:In; 6:Out → 83:Active |
| `mws_wat_08.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"shooter_position_1"}}}` | 56:Out → 8:In; 8:Out → 9:Active |
| `mws_wat_08.questphase / h0 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_08_trauma_team_tried_to_apply","value":1,"comparisonType":"GreaterOrEqual"}}}` | 30:Out → 10:In; 10:Out → 93:In |
| `mws_wat_08.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/arcade_game_manufacturer_trauma_drama/trauma_drama/congratulations_for_reaching_place_01","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 64:Out → 27:In; 27:Out → 72:In |
| `mws_wat_08.questphase / h0 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/arcade_game_manufacturer_trauma_drama/trauma_drama/consolation_prize_is_being_prepared","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 71:Out → 33:In; 33:Out → 34:Succeeded |
| `mws_wat_08.questphase / h0 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 7:Out → 57:In; 57:Out → 56:Active |
| `mws_wat_08.questphase / h0 / 86` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_08_activate_trauma_drama_section"}}}` | 83:Out → 86:In; 86:Out → 89:Inactive |
| `mws_wat_08.questphase / h0 / 92` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 92:Out → 31:Succeeded; 93:Out → 92:In; 92:Out → 95:Inactive; 92:Out → 119:In1 |
| `mws_wat_08.questphase / h0 / 107` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"internet_sites/home/00_home","fileEntryIndex":1,"className":"gameJournalInternetPage"},"state":"Active"}}}` | 107:True → 102:Inactive; 119:Out1 → 107:In |
| `mws_wat_08.questphase / h0 / 109` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"internet_sites/home/00_home3","fileEntryIndex":1,"className":"gameJournalInternetPage"},"state":"Active"}}}` | 109:True → 104:Inactive; 119:Out1 → 109:In |
| `mws_wat_08.questphase / h0 / 110` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"internet_sites/home/00_home2","fileEntryIndex":1,"className":"gameJournalInternetPage"},"state":"Active"}}}` | 110:True → 105:Inactive; 119:Out1 → 110:In |
| `mws_wat_08.questphase / h0 / 111` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"internet_sites/home/00_home1","fileEntryIndex":1,"className":"gameJournalInternetPage"},"state":"Active"}}}` | 111:True → 106:Inactive; 119:Out1 → 111:In |
| `mws_wat_08.questphase / h0 / 112` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"internet_sites/home/00_mq018_home_bartmoss","fileEntryIndex":1,"className":"gameJournalInternetPage"},"state":"Active"}}}` | 112:True → 103:Inactive; 119:Out1 → 112:In |
| `mws_wat_08.questphase / h0 / 144` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType","tickCount":15}}}` | 97:Out → 144:In; 144:Out → 138:Inactive |
| `mws_wat_08.questphase / h0 / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType","tickCount":15}}}` | 124:Out → 146:In; 146:Out → 139:Inactive |
| `mws_wat_08.questphase / h0 / 147` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType","tickCount":15}}}` | 126:Out → 147:In; 147:Out → 140:Inactive |
| `mws_wat_08.questphase / h0 / 148` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType","tickCount":15}}}` | 128:Out → 148:In; 148:Out → 141:Inactive |
| `mws_wat_08.questphase / h0 / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTickDelay_ConditionType","tickCount":15}}}` | 130:Out → 149:In; 149:Out → 142:Inactive |
| `mws_wat_08.questphase / h71 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_wat_08_tr_starter"}}` | 0:Out → 4:In; 4:Out → 5:In1 |
| `mws_wat_08.questphase / h71 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_08_debug_run"}}}` | 8:True → 10:In |
| `mws_wat_08.questphase / h71 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_08_collected_reward"}}}` | 8:True → 10:In; 10:Out → 9:debug_teleport_in |
| `mws_wat_08.questphase / h214 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleRef":{"$type":"gameEntityReference","reference":"#mws_com_trauma_team_av_model","names":["trauma_toy_spawn"]}}}}` | 2:Out → 4:In; 4:Out → 8:in_av_toy_interaction |
| `mws_wat_08.questphase / h214 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_trauma_drama_tr_interior_v_room"}}` | 5:Out → 2:In; 11:Out1 → 5:In; 20:Out1 → 5:In |
| `mws_wat_08.questphase / h214 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_trauma_drama_tr_interior_v_room"}}` | 0:Out → 22:In; 22:Out → 12:In |
| `mws_wat_08.questphase / h214 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 20:Out1 → 26:In; 26:Out → 27:In |
| `mws_wat_08.questphase / h328 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#trauma_team_av_model_generic_device_interaction","eventType":"Entered"}}}` | 0:Out → 2:In; 7:Out → 2:In; 2:Out → 3:In |
| `mws_wat_08.questphase / h328 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 3:Out → 4:In; 4:Out → 5:In |
| `mws_wat_08.questphase / h328 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#trauma_team_av_model_generic_device_interaction","eventType":"Exited"}}}` | 4:Out → 5:In; 5:Out → 6:In |
| `mws_wat_08.questphase / h328 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":200}}}` | 7:Out → 2:In; 6:Out → 7:In |
| `mws_wat_08.questphase / h328 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#trauma_team_av_model_generic_device_interaction","eventType":"Executed"}}}` | 0:Out → 8:In; 8:Out → 1:In |
| `mws_wat_08.scene / scene / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mws_trauma_drama_tr_interior_v_room"}}` | 6:0:0 → 22:0:1; 22:0:0 → 220:0:1 |
| `mws_wat_08.scene / scene / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mws_wat_08_com_trauma_team","names":["trauma_team_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 86:0:0 → 93:0:1; 93:0:0 → 83:0:0; 93:0:0 → 170:0:1 |
| `mws_wat_08.scene / scene / 176` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mws_wat_08_tr_starter"}}` | 125:0:0 → 176:0:1; 176:0:0 → 128:0:0 |
| `mws_wat_08.scene / scene / 196` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mws_wat_08_johnny"},"angleTolerance":60.0,"inverted":true}}}` | 179:0:0 → 196:0:1; 196:0:0 → 194:0:1 |
| `mws_wat_08.scene / scene / 228` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_av_toy_used_spline","comparisonType":"Equal"}}}` | 228:0:0 → 205:0:1; 228:0:1 → 212:0:1; 296:0:0 → 228:0:1 |
| `mws_wat_08.scene / scene / 290` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 290:0:0 → 18:0:0; 309:0:0 → 290:0:1 |
| `mws_wat_08.scene / scene / 319` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_wat_08_com_trauma_team","names":["trauma_team_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_wat_08_com_trauma_team","names":["trauma_team_02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}]}}` | 1:0:0 → 319:0:1; 319:0:0 → 321:0:1 |
| `mws_wat_08.scene / scene / 343` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"104253195087","comparisonType":"Greater"}}}` | 343:0:0 → 33:0:1; 355:0:0 → 343:0:1 |
| `mws_wat_08.scene / scene / 345` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"173521606896","comparisonType":"Greater"}}}` | 345:0:0 → 54:0:1; 359:0:0 → 345:0:1 |
| `mws_wat_08.scene / scene / 366` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content"}}}` | 28:0:0 → 366:0:1; 366:0:0 → 179:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mws_wat_08.scene / scene / 319 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `call_lifecycle` | mws_wat_08.questphase / h0 / 68 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `choice_gate` | mws_wat_08.scene / scene / 10; mws_wat_08.scene / scene / 239; mws_wat_08.scene / scene / 260; mws_wat_08.scene / scene / 28; +1 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | mws_wat_08.questphase / h114 / 2; mws_wat_08.questphase / h137 / 2; mws_wat_08.questphase / h214 / 2; mws_wat_08.questphase / h214 / 9 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mws_wat_08.questphase / h0 / 10; mws_wat_08.questphase / h0 / 6; mws_wat_08.questphase / h0 / 8; mws_wat_08.questphase / h0 / 86; +4 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `item_state` | mws_wat_08.scene / scene / 343; mws_wat_08.scene / scene / 345 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_read` | mws_wat_08.questphase / h0 / 27; mws_wat_08.questphase / h0 / 33 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `persistent_decision` | mws_wat_08.questphase / h0 / 66; mws_wat_08.questphase / h0 / 72; mws_wat_08.questphase / h71 / 7; mws_wat_08.scene / scene / 217; +6 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | mws_wat_08.questphase / h0 / 57; mws_wat_08.questphase / h0 / 92; mws_wat_08.questphase / h214 / 26; mws_wat_08.questphase / h328 / 4; +2 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | mws_wat_08.questphase / h0 / 64 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mws_wat_08.questphase / h214 / 8; mws_wat_08.questphase / h71 / 9; mws_wat_08.questphase / h89 / 7 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `vehicle_control` | mws_wat_08.questphase / h114 / 3; mws_wat_08.questphase / h137 / 3; mws_wat_08.scene / scene / 205; mws_wat_08.scene / scene / 212 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mws_wat_08.scene / scene / 165; mws_wat_08.scene / scene / 181; mws_wat_08.scene / scene / 183; mws_wat_08.scene / scene / 190; +5 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mws_wat_08.questphase / h214 / 12 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` | content candidate; journal anchor | `base-mws-wat-08` |
| `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` | content candidate; journal anchor | `base-mws-wat-08` |

Evidence shards for this dossier (including parent context): [base-mws-wat-08](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mws-wat-08.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
