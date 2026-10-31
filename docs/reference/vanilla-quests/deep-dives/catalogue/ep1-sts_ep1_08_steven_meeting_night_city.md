# The Show Must Go On

Journal: `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city` · `MinorQuest` · hash `753954935`.

**Coverage: journal-linked.** 8 exact journal-linked nodes in 3 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

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
| `steven_default.questphase / h90 / 3` | `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\sts_08_steven_default_new_biomonitor_not_destroyed.scene`; `#sts_08_sm_steven_default_new_biomonitor_not_destroyed` | 31:Out → 3:Start 1; 3:End 2 → 13:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\street_stories\ep1_street_stories.questphase` / h470 / 15 | `sts_ep1_08_cleanup.questphase` | 6: Input; 20: Input; 6:Out → 15:In1; 20:Out → 15:Organitopia cleanup |
| `ep1\quest\ep1_default_dialogs.questphase` / h0 / 17 | `steven_default.questphase` | 19: PauseCondition: q304_stadium_escape_active Equal RED default; steven_santos_default_on; 19:Out → 17:In1; 17:Out1 → 19:In |
| `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\steven_default.questphase` / h90 / 3 | `sts_08_steven_default_new_biomonitor_not_destroyed.scene` | 31: Vehicle; 31:Out → 3:Start 1; 3:End 2 → 13:In |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 2 | `ep1_street_stories.questphase` | 33: PauseCondition: ep1_side_content GreaterOrEqual 1; 33:Out → 2:In1 |
| `ep1\quest\ep1_additional_game_elements.questphase` / h0 / 1 | `ep1_default_dialogs.questphase` | 0: Input; 0:Out → 1:In1 |
| `ep1\openworld\vendors\vehicle_metaquest\phases\vehicle_metaquest_ep1_bugfixing.questphase` / h17 / 6 | `ep1_open_world.questphase` | 4: Condition: militech_hellhound_available; 4:False → 6:CP77-63752 |
| `ep1\quest\ep1.questphase` / h58 / 5 | `ep1_open_world.questphase` | 0: Input; 9: CutControl; 0:Out → 5:In1; 9:CutSource → 5:CutDestination |
| `ep1\quest\ep1.questphase` / h58 / 4 | `ep1_additional_game_elements.questphase` | 2: Phase: ep1_bugfixing.questphase; 2: Phase: ep1_bugfixing.questphase; 9: CutControl; 7: PauseCondition: ep1_active GreaterOrEqual 1; 2:Out1 → 4:In2; 2:growl → 4:growl; 9:CutSource → 4:CutDestination; 7:Out → 4:In1 |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 16 | `vehicle_metaquest_ep1_bugfixing.questphase` | 0: Input; 0:Out → 16:In1 |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 3 | `ep1_openworld_bugfixing.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\ep1.questphase` / h58 / 2 | `ep1_bugfixing.questphase` | 25: LogicalXor; 2:CP77-65722_out → 27:In; 2:CP77-64292_out → 26:In; 25:Out1 → 2:In1; 2:Out1 → 4:In2; 2:growl → 4:growl |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene` | Start 1, Start 2, Start 3 → End 2, End 3 | steven_1; player; 38 nodes / 39 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / n122 / 0` | Hey, Steve. (`Option`) | No option-level predicate stored | 0:0 → 124:0:0 |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / n126 / 0` | Take care. (`bye`) | No option-level predicate stored | 0:0 → 128:0:0 |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / n126 / 1` | What about Ana? (`ana`) | No option-level predicate stored | 0:1 → 131:0:1 |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / n126 / 2` | What's your plan now? (`future`) | No option-level predicate stored | 0:2 → 133:0:1 |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / n195 / 0` | Text join unresolved (`Option_01`) | No option-level predicate stored | 0:0 → 197:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `ep1_standalone` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 87; sts_ep1_08_cleanup.questphase / h13 / 91 |
| `steven_night_city_default_dialogue_start` | sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 187 | No reader in selected context |
| `steven_santos_default_on` | steven_default.questphase / h90 / 14; sts_ep1_08_cleanup.questphase / h13 / 2 | No reader in selected context |
| `sts_ep1_08_agents_room_cleanup_done` | sts_ep1_08_cleanup.questphase / h958 / 3 | No reader in selected context |
| `sts_ep1_08_biomonitor_ana` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 3 |
| `sts_ep1_08_cleanup_done` | sts_ep1_08_cleanup.questphase / h0 / 87 | No reader in selected context |
| `sts_ep1_08_cleanup_executed` | sts_ep1_08_cleanup.questphase / h651 / 25 | No reader in selected context |
| `sts_ep1_08_cleanup_organitopia_done` | sts_ep1_08_cleanup.questphase / h651 / 26 | No reader in selected context |
| `sts_ep1_08_katya_killed` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 12 |
| `sts_ep1_08_save_katya_corpo_blueline` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 10 |
| `sts_ep1_08_save_katya_nomad_blueline` | Producer outside selected context | sts_ep1_08_cleanup.questphase / h13 / 11 |

## Exact gates, joins and cancellation

<details><summary>61 stored control nodes in the selected context</summary>

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
| `steven_default.questphase / h90 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#steven_default_night_city_com","names":["steven"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0}}}}` | 0:Out → 11:In; 13:CutSource → 11:CutDestination; 11:Out → 25:In |
| `steven_default.questphase / h90 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#steven_default_night_city_com","names":["steven"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0}}}}` | 12:Out → 7:In; 30:Out → 12:In |
| `steven_default.questphase / h90 / 13` | `questCutControlNodeDefinition` `{}` | 3:End 2 → 13:In; 13:CutSource → 11:CutDestination; 13:Out → 15:Succeeded |
| `steven_default.questphase / h90 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#steven_default_night_city_com","names":["steven"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":20.0},"comparisonType":"Less"}}}` | 0:Out → 17:In; 17:Out → 20:In; 17:Out → 21:In |
| `steven_default.questphase / h90 / 20` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/steven_santos/sts_ep1_08/v_answer_meeting_invitation/v_answer_meeting_invitation_var_1","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 17:Out → 20:In; 20:False → 22:In1 |
| `steven_default.questphase / h90 / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/steven_santos/sts_ep1_08/v_answer_meeting_invitation/v_answer_meeting_invitation_var_2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 17:Out → 21:In; 21:False → 22:In2 |
| `steven_default.questphase / h90 / 22` | `questLogicalAndNodeDefinition` `{}` | 22:Out1 → 19:Inactive; 20:False → 22:In1; 21:False → 22:In2 |
| `steven_default.questphase / h90 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#steven_default_night_city_com","names":["steven"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0}}}}` | 16:Out → 33:In; 33:Out → 30:In |
| `steven_default.questphase / h90 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#steven_default_night_city_com","names":["steven"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0},"comparisonType":"Less"}}}` | 0:Out → 34:In; 34:Out → 32:In |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#steve_night_city_default_scene_start"}}` | 114:0:0 → 187:0:1; 120:0:0 → 114:0:1 |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 131` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"ep1\\quest\\tertiary_characters\\default_dialogs\\steven_santos_default\\sts_08_steven_default_new_biomonitor_not_destroyed.scene","Flags":"Soft"},"sectionName":"sts_08_steven_night_city_ana","type":"IsOutside"}}}` | 126:0:1 → 131:0:1; 131:0:0 → 130:0:0 |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"ep1\\quest\\tertiary_characters\\default_dialogs\\steven_santos_default\\sts_08_steven_default_new_biomonitor_not_destroyed.scene","Flags":"Soft"},"sectionName":"sts_08_future","type":"IsOutside"}}}` | 126:0:2 → 133:0:1; 133:0:0 → 132:0:0 |
| `sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 198` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 128:0:0 → 198:0:1; 197:0:0 → 198:0:1; 198:0:0 → 195:0:0; 227:0:0 → 198:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `call_lifecycle` | steven_default.questphase / h90 / 23; sts_ep1_08_cleanup.questphase / h0 / 12; sts_ep1_08_cleanup.questphase / h0 / 17; sts_ep1_08_cleanup.questphase / h13 / 13; +12 locations in catalogue.json | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `choice_gate` | sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 122; sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 126; sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 195 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | steven_default.questphase / h90 / 7; sts_ep1_08_cleanup.questphase / h651 / 10; sts_ep1_08_cleanup.questphase / h651 / 9; sts_ep1_08_cleanup.questphase / h958 / 2 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | sts_ep1_08_cleanup.questphase / h13 / 10; sts_ep1_08_cleanup.questphase / h13 / 11; sts_ep1_08_cleanup.questphase / h13 / 12; sts_ep1_08_cleanup.questphase / h13 / 3; +2 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_ep1_08_cleanup.questphase / h0 / 88 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `device_action` | sts_ep1_08_cleanup.questphase / h760 / 10; sts_ep1_08_cleanup.questphase / h760 / 11; sts_ep1_08_cleanup.questphase / h760 / 12; sts_ep1_08_cleanup.questphase / h760 / 13; +12 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | sts_ep1_08_cleanup.questphase / h0 / 27; sts_ep1_08_cleanup.questphase / h0 / 61; sts_ep1_08_cleanup.questphase / h13 / 15; sts_ep1_08_cleanup.questphase / h13 / 33; +4 locations in catalogue.json | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_read` | sts_ep1_08_cleanup.questphase / h13 / 17 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `parallel_join` | steven_default.questphase / h90 / 22; sts_ep1_08_cleanup.questphase / h0 / 25; sts_ep1_08_cleanup.questphase / h0 / 26; sts_ep1_08_cleanup.questphase / h0 / 86; +3 locations in catalogue.json | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | steven_default.questphase / h90 / 14; sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 187; sts_ep1_08_cleanup.questphase / h0 / 87; sts_ep1_08_cleanup.questphase / h13 / 2; +3 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 198 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | steven_default.questphase / h90 / 13 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 191 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | steven_default.questphase / h90 / 3 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `vehicle_control` | steven_default.questphase / h90 / 25; steven_default.questphase / h90 / 30; steven_default.questphase / h90 / 31; sts_ep1_08_cleanup.questphase / h651 / 24 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 159; sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 165; sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 167; sts_08_steven_default_new_biomonitor_not_destroyed.scene / scene / 169; +9 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_ep1_08_cleanup.questphase / h651 / 14; sts_ep1_08_cleanup.questphase / h651 / 15; sts_ep1_08_cleanup.questphase / h651 / 21; sts_ep1_08_cleanup.questphase / h651 / 22 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_cleanup.questphase` | content candidate; journal anchor | `ep1-sts-ep1-08` |
| `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\steven_default.questphase` | content candidate; journal anchor | `ep1-shared` |
| `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\sts_08_steven_default_new_biomonitor_not_destroyed.scene` | content candidate; journal anchor | `ep1-shared` |

Evidence shards for this dossier (including parent context): [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-sts-ep1-08.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
