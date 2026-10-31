# The Show Must Go On

Journal: `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city` · `MinorQuest` · hash `753954935`.

Journal premise: Ahh, yes… Steven Santos. Our beloved little earthworm. A gonk of reason. A coward too afraid to hurt anyone wearing a suit. A man you helped... Go on, accept his thanks, shake his hand… But take a napkin – it's gonna be slimy.

**Coverage: journal-linked.** 8 exact journal-linked nodes in 3 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Read the message from Steven Santos. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city/read_message_from_steven` |
| Meet with Steven. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city/steven_meeting` |
| Talk to Steven. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city/talk_with_steven` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_ep1_08_cleanup.questphase / h13 / 9` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city/steven_meeting` | 9:Out → 2:In; 59:Out → 9:Active |
| `sts_ep1_08_cleanup.questphase / h13 / 58` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city/read_message_from_steven` | 8:Out → 58:Active; 58:Out → 96:Active |
| `sts_ep1_08_cleanup.questphase / h13 / 59` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city/read_message_from_steven` | 59:Out → 9:Active; 17:Out → 59:Succeeded |
| `sts_ep1_08_cleanup.questphase / h13 / 96` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city_description` | 96:Out → 17:In; 58:Out → 96:Active |
| `steven_default.questphase / h90 / 15` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city/talk_with_steven` | 13:Out → 15:Succeeded; 15:Out → 16:Succeeded |
| `steven_default.questphase / h90 / 16` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city` | 15:Out → 16:Succeeded; 16:Out → 33:In |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 206` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city/talk_with_steven` | 206:0:0 → 122:0:0; 209:0:0 → 206:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 209` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city/steven_default_night_city/steven_meeting` | 118:0:0 → 209:0:3; 209:0:0 → 206:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\street_stories\ep1_street_stories.questphase` / h470 / 15 | `sts_ep1_08_cleanup.questphase` | 6: Input; 20: Input; 6:Out → 15:In1; 20:Out → 15:Organitopia cleanup |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest` / h0 / 18 | `sts_ep1_08_cleanup.questphase` | 0: Phase: sts_ep1_08_phase.questphase; 0: Phase: sts_ep1_08_phase.questphase; 0:Organitopia done → 18:Organitopia cleanup; 0:Out1 → 18:In1 |
| `ep1\quest\ep1_default_dialogs.questphase` / h0 / 17 | `steven_default.questphase` | 19: PauseCondition: q304_stadium_escape_active Equal RED default; steven_santos_default_on; 19:Out → 17:In1; 17:Out1 → 19:In |
| `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\steven_default.questphase` / h90 / 3 | `sts_08_steven_default_new_biomonitor_not_destroyed.scene` | 31: Vehicle; 31:Out → 3:Start 1; 3:End 2 → 13:In |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 2 | `ep1_street_stories.questphase` | 33: PauseCondition: ep1_side_content GreaterOrEqual 1; 33:Out → 2:In1 |
| `ep1\quest\ep1_additional_game_elements.questphase` / h0 / 1 | `ep1_default_dialogs.questphase` | 0: Input; 0:Out → 1:In1 |
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
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 16 | `vehicle_metaquest_ep1_bugfixing.questphase` | 0: Input; 0:Out → 16:In1 |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 3 | `ep1_openworld_bugfixing.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\ep1.questphase` / h58 / 2 | `ep1_bugfixing.questphase` | 25: LogicalXor; 2:CP77-65722_out → 27:In; 2:CP77-64292_out → 26:In; 25:Out1 → 2:In1; 2:Out1 → 4:In2; 2:growl → 4:growl |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 12 | `ep1_bugfixing.questphase` | 11: LogicalHub; 11:Out1 → 12:In1 |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 5 | `ep1_bugfixing.questphase` | 4: LogicalHub; 4:Out1 → 5:In1 |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene` | Start 1, Start 2, Start 3 → End 2, End 3 | steven_1; player; 38 nodes / 39 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / n122 / 0` | Hey, Steve. (`Option`) | No option-level predicate stored | 0:0 → 124:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `ep1_standalone` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 87; sts_ep1_08_cleanup.questphase / h13 / 91 |
| `steven_santos_default_on` | sts_ep1_08_cleanup.questphase / h13 / 2 | No reader in selected context |
| `sts_ep1_08_agents_room_cleanup_done` | sts_ep1_08_cleanup.questphase / h958 / 3 | No reader in selected context |
| `sts_ep1_08_biomonitor_ana` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 3 |
| `sts_ep1_08_cleanup_done` | sts_ep1_08_cleanup.questphase / h0 / 87 | No reader in selected context |
| `sts_ep1_08_cleanup_executed` | sts_ep1_08_cleanup.questphase / h651 / 25 | No reader in selected context |
| `sts_ep1_08_cleanup_organitopia_done` | sts_ep1_08_cleanup.questphase / h651 / 26 | No reader in selected context |
| `sts_ep1_08_katya_killed` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 12 |
| `sts_ep1_08_save_katya_corpo_blueline` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 10 |
| `sts_ep1_08_save_katya_nomad_blueline` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 11 |

## Exact gates, joins and cancellation

<details><summary>50 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_ep1_08_cleanup.questphase / h0 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_08/sts_ep1_08_holocall_dead","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"state":"Active"}}}` | 0:Out → 7:In; 7:True → 14:Active; 7:False → 8:In |
| `sts_ep1_08_cleanup.questphase / h0 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_08/sts_ep1_08_holocall_peaceful","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"state":"Active"}}}` | 8:True → 9:Active; 7:False → 8:In |
| `sts_ep1_08_cleanup.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_08/v_answer_biomonitor_destroyed/v_answer_biomonitor_destroyed_var_1","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 14:Out → 16:In; 16:Out → 17:In |
| `sts_ep1_08_cleanup.questphase / h0 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_08/v_answer_biomonitor_not_destroyed/v_answer_biomonitor_not_destroyed_var_1","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 9:Out → 11:In; 11:Out → 12:In |
| `sts_ep1_08_cleanup.questphase / h0 / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_08/v_answer_biomonitor_not_destroyed/v_answer_biomonitor_not_destroyed_var_1","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 27:Out → 21:In; 21:False → 25:In1 |
| `sts_ep1_08_cleanup.questphase / h0 / 22` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_08/v_answer_biomonitor_not_destroyed/v_answer_biomonitor_not_destroyed_var_2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 27:Out → 22:In; 22:False → 25:In2 |
| `sts_ep1_08_cleanup.questphase / h0 / 23` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_08/v_answer_biomonitor_destroyed/v_answer_biomonitor_destroyed_var_1","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 27:Out → 23:In; 23:False → 26:In1 |
| `sts_ep1_08_cleanup.questphase / h0 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_08/v_answer_biomonitor_destroyed/v_answer_biomonitor_destroyed_var_2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 27:Out → 24:In; 24:False → 26:In2 |
| `sts_ep1_08_cleanup.questphase / h0 / 25` | `questLogicalAndNodeDefinition` `{}` | 21:False → 25:In1; 22:False → 25:In2; 25:Out1 → 28:Inactive |
| `sts_ep1_08_cleanup.questphase / h0 / 26` | `questLogicalAndNodeDefinition` `{}` | 23:False → 26:In1; 24:False → 26:In2; 26:Out1 → 29:Inactive |
| `sts_ep1_08_cleanup.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":22}}}` | 0:Out → 27:In; 27:Out → 21:In; 27:Out → 22:In; 27:Out → 23:In; 27:Out → 24:In |
| `sts_ep1_08_cleanup.questphase / h0 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#sts_ep1_08_start_trigger"}}` | 0:Out → 31:In; 31:Out → 85:In1 |
| `sts_ep1_08_cleanup.questphase / h0 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#sts_ep1_08_main_location_init_trigger"}}` | 61:Out → 49:In; 49:Out → 84:In1 |
| `sts_ep1_08_cleanup.questphase / h0 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 30:Out → 61:In; 61:Out → 49:In |
| `sts_ep1_08_cleanup.questphase / h0 / 86` | `questLogicalAndNodeDefinition` `{}` | 84:Out1 → 86:In2; 85:Out1 → 86:In1; 86:Out1 → 87:In |
| `sts_ep1_08_cleanup.questphase / h13 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_biomonitor_ana"}}}` | 0:Out → 3:In; 3:True → 4:In; 3:False → 5:In |
| `sts_ep1_08_cleanup.questphase / h13 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":66}}}` | 3:True → 4:In; 4:Out → 6:In |
| `sts_ep1_08_cleanup.questphase / h13 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":66}}}` | 3:False → 5:In; 5:Out → 91:In |
| `sts_ep1_08_cleanup.questphase / h13 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#steve_stadium_default_spawn_trigger"}}` | 6:Out → 2:In; 4:Out → 6:In |
| `sts_ep1_08_cleanup.questphase / h13 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_save_katya_corpo_blueline"}}}` | 12:True → 10:In; 10:True → 60:In |
| `sts_ep1_08_cleanup.questphase / h13 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_save_katya_nomad_blueline"}}}` | 12:True → 11:In; 11:True → 61:In |
| `sts_ep1_08_cleanup.questphase / h13 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_katya_killed","comparisonType":"LessOrEqual"}}}` | 12:True → 10:In; 12:True → 11:In; 15:Out → 12:In |
| `sts_ep1_08_cleanup.questphase / h13 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":44}}}` | 15:Out → 12:In |
| `sts_ep1_08_cleanup.questphase / h13 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/steven_santos/sts_ep1_08/biomonitor_destroyed_meeting_invitation","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 96:Out → 17:In; 17:Out → 59:Succeeded |
| `sts_ep1_08_cleanup.questphase / h13 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/steven_santos/sts_ep1_08/v_answer_meeting_invitation/v_answer_meeting_invitation_var_1","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 39:Out → 37:In; 37:Out → 38:In |
| `sts_ep1_08_cleanup.questphase / h13 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":22}}}` | 18:Out → 33:In; 33:Out → 42:In; 33:Out → 43:In |
| `sts_ep1_08_cleanup.questphase / h13 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":22}}}` | 23:Out → 34:In; 34:Out → 46:In; 34:Out → 47:In |
| `sts_ep1_08_cleanup.questphase / h13 / 42` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/katya_karielin/sts_ep1_08/v_answer_corpo_blueline/v_answer_corpo_blueline_var_1","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 33:Out → 42:In; 42:False → 44:In1 |
| `sts_ep1_08_cleanup.questphase / h13 / 43` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/katya_karielin/sts_ep1_08/v_answer_corpo_blueline/v_answer_corpo_blueline_var_2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 33:Out → 43:In; 43:False → 44:In2 |
| `sts_ep1_08_cleanup.questphase / h13 / 44` | `questLogicalAndNodeDefinition` `{}` | 44:Out1 → 35:Inactive; 42:False → 44:In1; 43:False → 44:In2 |
| `sts_ep1_08_cleanup.questphase / h13 / 46` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/katya_karielin/sts_ep1_08/v_answer_nomad_blueline/v_answer_nomad_blueline_var_1","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 34:Out → 46:In; 46:False → 48:In1 |
| `sts_ep1_08_cleanup.questphase / h13 / 47` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/katya_karielin/sts_ep1_08/v_answer_nomad_blueline/v_answer_nomad_blueline_var_2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 34:Out → 47:In; 47:False → 48:In2 |
| `sts_ep1_08_cleanup.questphase / h13 / 48` | `questLogicalAndNodeDefinition` `{}` | 48:Out1 → 36:Inactive; 46:False → 48:In1; 47:False → 48:In2 |
| `sts_ep1_08_cleanup.questphase / h13 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"SideQuest_MainPath"}}}` | 10:True → 60:In; 60:Out → 54:In |
| `sts_ep1_08_cleanup.questphase / h13 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"SideQuest_MainPath"}}}` | 11:True → 61:In; 61:Out → 55:In |
| `sts_ep1_08_cleanup.questphase / h13 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/steven_santos/sts_ep1_08/v_answer_meeting_invitation/v_answer_meeting_invitation_var_2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 39:Out → 64:In; 64:Out → 65:In |
| `sts_ep1_08_cleanup.questphase / h13 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/janet/sts_ep1_08/katya_dead","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"state":"Active"}}}` | 68:Out → 66:In; 66:Out → 67:Active |
| `sts_ep1_08_cleanup.questphase / h13 / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/janet/sts_ep1_08/v_answer_to_janet_biomonitor_info/v_answer_to_janet_biomonitor_info_var_1","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 67:Out → 75:In; 75:Out → 77:In |
| `sts_ep1_08_cleanup.questphase / h13 / 76` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/janet/sts_ep1_08/v_answer_to_janet_biomonitor_info/v_answer_to_janet_biomonitor_info_var_2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 67:Out → 76:In; 76:Out → 78:In |
| `sts_ep1_08_cleanup.questphase / h13 / 87` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone"}}}` | 97:Out → 87:In; 87:True → 88:In; 87:False → 89:In |
| `sts_ep1_08_cleanup.questphase / h13 / 88` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"EP1_Minor"}}}` | 87:True → 88:In; 88:Out → 90:In1 |
| `sts_ep1_08_cleanup.questphase / h13 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"MinorQuestAndSts"}}}` | 87:False → 89:In; 89:Out → 90:In2 |
| `sts_ep1_08_cleanup.questphase / h13 / 91` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone"}}}` | 5:Out → 91:In; 91:True → 92:In; 91:False → 93:In |
| `sts_ep1_08_cleanup.questphase / h13 / 92` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"EP1_Minor"}}}` | 91:True → 92:In; 92:Out → 94:In1 |
| `sts_ep1_08_cleanup.questphase / h13 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"MinorQuestAndSts"}}}` | 91:False → 93:In; 93:Out → 94:In2 |
| `sts_ep1_08_cleanup.questphase / h13 / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wellsprings_content_tr"}}` | 95:Out → 56:In; 94:Out1 → 95:In |
| `sts_ep1_08_cleanup.questphase / h13 / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":23}}}` | 97:Out → 87:In; 98:Out → 97:In |
| `sts_ep1_08_cleanup.questphase / h651 / 16` | `questLogicalAndNodeDefinition` `{}` | 27:Out → 16:In1; 18:Out1 → 16:In2; 16:Out1 → 25:In |
| `steven_default.questphase / h90 / 13` | `questCutControlNodeDefinition` `{}` | 3:End 2 → 13:In; 13:CutSource → 11:CutDestination; 13:Out → 15:Succeeded |
| `steven_default.questphase / h90 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#steven_default_night_city_com","names":["steven"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0}}}}` | 16:Out → 33:In; 33:Out → 30:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `call_lifecycle` | sts_ep1_08_cleanup.questphase / h0 / 12; sts_ep1_08_cleanup.questphase / h0 / 17; sts_ep1_08_cleanup.questphase / h13 / 13; sts_ep1_08_cleanup.questphase / h13 / 14; +11 locations in catalogue.json | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `choice_gate` | sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 122 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | sts_ep1_08_cleanup.questphase / h651 / 10; sts_ep1_08_cleanup.questphase / h651 / 9; sts_ep1_08_cleanup.questphase / h958 / 2 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | sts_ep1_08_cleanup.questphase / h13 / 10; sts_ep1_08_cleanup.questphase / h13 / 11; sts_ep1_08_cleanup.questphase / h13 / 12; sts_ep1_08_cleanup.questphase / h13 / 3; +2 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_ep1_08_cleanup.questphase / h0 / 88 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_ep1_08_cleanup.questphase / h651 / 19; sts_ep1_08_cleanup.questphase / h651 / 20; sts_ep1_08_cleanup.questphase / h651 / 27; sts_ep1_08_cleanup.questphase / h651 / 28; +12 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_ep1_08_cleanup.questphase / h760 / 10; sts_ep1_08_cleanup.questphase / h760 / 11; sts_ep1_08_cleanup.questphase / h760 / 12; sts_ep1_08_cleanup.questphase / h760 / 13; +12 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | sts_ep1_08_cleanup.questphase / h0 / 27; sts_ep1_08_cleanup.questphase / h0 / 61; sts_ep1_08_cleanup.questphase / h13 / 15; sts_ep1_08_cleanup.questphase / h13 / 33; +4 locations in catalogue.json | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_read` | sts_ep1_08_cleanup.questphase / h13 / 17 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | steven_default.questphase / h90 / 15; steven_default.questphase / h90 / 16; sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 206; sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 209; +14 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | sts_ep1_08_cleanup.questphase / h0 / 25; sts_ep1_08_cleanup.questphase / h0 / 26; sts_ep1_08_cleanup.questphase / h0 / 86; sts_ep1_08_cleanup.questphase / h13 / 44; +2 locations in catalogue.json | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_ep1_08_cleanup.questphase / h0 / 87; sts_ep1_08_cleanup.questphase / h13 / 2; sts_ep1_08_cleanup.questphase / h651 / 25; sts_ep1_08_cleanup.questphase / h651 / 26; +1 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `retire_branch` | steven_default.questphase / h90 / 13 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `spatial_gate` | sts_ep1_08_cleanup.questphase / h0 / 31; sts_ep1_08_cleanup.questphase / h0 / 49; sts_ep1_08_cleanup.questphase / h13 / 6; sts_ep1_08_cleanup.questphase / h13 / 95 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | sts_ep1_08_cleanup.questphase / h651 / 24 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `world_variant` | sts_ep1_08_cleanup.questphase / h651 / 14; sts_ep1_08_cleanup.questphase / h651 / 15; sts_ep1_08_cleanup.questphase / h651 / 21; sts_ep1_08_cleanup.questphase / h651 / 22 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` | content candidate; journal anchor | `ep1-sts-ep1-08` |
| `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\steven_default.questphase` | content candidate; journal anchor | `ep1-shared` |
| `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\sts_08_steven_default_new_biomonitor_not_destroyed.scene` | content candidate; journal anchor | `ep1-shared` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mq306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq306.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-08.json.gz), [ep1-sts-ep1-13](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-13.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

71 repeated typed/socket path signatures in this selected graph context; 14 distinct direct resource identities; 4 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `215ca95d939006973a7d` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h651 / 25 -> 26 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `ea4cb15199b9b3fa8e63` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h0 / 30 -> 61 -> 49 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `f1e68c36026b90dd9a9b` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h958 / 2 -> 5 -> 4 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questEventManagerNodeDefinition -> questEventManagerNodeDefinition; Out -> In; Out -> In |
| `9380dda43f90ecd62efb` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h760 / 15 -> 10 -> 11 | questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out -> In; Out -> In |
| `178ff9eba50354aed786` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h651 / 0 -> 10 -> 9 | questInputNodeDefinition -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `bfe95df47bd1ca67330f` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h651 / 14 -> 15 -> 21 | questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]; Out -> In; Out -> In |
| `38efa89ea367b077425d` | `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\sts_08_steven_default_new_biomonitor_not_destroyed.scene` / scene / 118 -> 209 -> 206 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; 0:0 -> 0:3; 0:0 -> 0:1 |
| `9142f4e54264697a790e` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h760 / 0 -> 5 -> 7 | questInputNodeDefinition -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams] -> questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]; Out -> In; Out -> In |
| `62513b1c2fdaf0c74a1c` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h13 / 59 -> 9 -> 2 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Active; Out -> In |
| `79ff30ab7464b071eda5` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h651 / 12 -> 13 -> 11 | questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType] -> questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType] -> questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]; Out -> In; Out -> In |
| `fd953ca767fcd221cba3` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h651 / 10 -> 9 -> 2 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]; Out -> In; Out -> In |
| `240148efc76953d1c5d4` | `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h13 / 96 -> 17 -> 59 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h0 / 3 | `h13` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h0 / 84 | `h651` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h651 / 18 | `h760` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` / h0 / 85 | `h958` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq303\mq303.gamedef` | content candidate | ep1\quest\minor_quests\mq303\mq303.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq305\mq305.gamedef` | content candidate | ep1\quest\minor_quests\mq305\mq305.quest |
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
| `base\animations\facial\generic\interactive_scene\generic_facial_additives.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__sit_chair_table__2h_cup__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__sit_chair_table__2h_elbow_on_table__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__sit_chair__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\workspots\common\chair_table\generic__sit_chair_table_lean_front_can__drink__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q101\08_takemura_v_room\takemura__sit_bench__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q116\q116_05_mikoshi\q116__player__sit_chair__sit_around__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\lipsync\en\sts_08_steven_default_new_biomonitor_not_destroyed\steven_santos.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\lipsync\en\sts_08_steven_default_new_biomonitor_not_destroyed\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `ep1_standalone` | ep1\quest\ep1_standalone.quest / h0 / 5; 1 total source locations in compressed evidence |
| `steven_santos_default_on` | ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\steven_default.questphase / h90 / 14; ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_chicken_test.scene / scene / 97; ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_chicken_test.scene / scene / 100; 3 total source locations in compressed evidence |
| `sts_ep1_08_biomonitor_ana` | ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_chicken_test.scene / scene / 88; ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_client_ending.scene / scene / 649; ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_client_ending.scene / scene / 652; 3 total source locations in compressed evidence |
| `sts_ep1_08_katya_killed` | ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase / h0 / 377; 1 total source locations in compressed evidence |
| `sts_ep1_08_save_katya_corpo_blueline` | ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_target_meeting.scene / scene / 1540; 1 total source locations in compressed evidence |
| `sts_ep1_08_save_katya_nomad_blueline` | ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_target_meeting.scene / scene / 1541; 1 total source locations in compressed evidence |

NodeRef uses: 56; TweakDB binding uses: 6. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\sts_08_steven_default_new_biomonitor_not_destroyed.scene` | 6 / 75 | scnChangeIdleAnimEvent: 4; scnDialogLineEvent: 17; scnLookAtAdvancedEvent: 4; scnLookAtEvent: 12; scnPlaySkAnimEvent: 17; scneventsAttachPropToPerformer: 2; scneventsAttachPropToWorld: 1; scneventsSocket: 16; scneventsVFXEvent: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
