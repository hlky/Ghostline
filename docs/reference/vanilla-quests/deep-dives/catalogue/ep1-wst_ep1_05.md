# Go Your Own Way

Journal: `ep1/quests/minor_quest/wst_ep1_05` · `MinorQuest` · hash `1940045604`.

**Coverage: journal-linked.** 10 exact journal-linked nodes in 1 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Meet with Hasan in the Longshore Stacks. (Primary) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/go_to_hasan_apartment` |
| Read the message from Mr. Hands. (Primary) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/read_message_from_hands` |
| Talk to Hasan. (Primary) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/speak_with_hasan` |
| Take the gun. (Primary) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/take_the_gun` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `wst_ep1_05.questphase / h0 / 20` (Journal) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/go_to_hasan_apartment` | 31:Out → 20:Active; 20:Out → 80:In |
| `wst_ep1_05.questphase / h0 / 22` (Journal) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/go_to_hasan_apartment` | 22:Out → 10:In; 80:Out → 22:Succeeded |
| `wst_ep1_05.questphase / h0 / 23` (Journal) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/speak_with_hasan` | 10:Out → 23:Active; 23:Out → 25:In |
| `wst_ep1_05.questphase / h0 / 24` (Journal) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/speak_with_hasan` | 25:Out → 24:Inactive; 24:Out → 48:Active |
| `wst_ep1_05.questphase / h0 / 28` (Journal) | `ep1/quests/minor_quest/wst_ep1_05` | 28:Out → 27:In; 56:Out → 28:Succeeded |
| `wst_ep1_05.questphase / h0 / 29` (Journal) | `ep1/quests/minor_quest/wst_ep1_05/description` | 70:Out → 29:Active |
| `wst_ep1_05.questphase / h0 / 48` (Journal) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/take_the_gun` | 24:Out → 48:Active; 48:Out → 55:In |
| `wst_ep1_05.questphase / h0 / 56` (Journal) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/take_the_gun` | 56:Out → 28:Succeeded; 55:Out → 56:Succeeded |
| `wst_ep1_05.questphase / h0 / 70` (Journal) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/read_message_from_hands` | 70:Out → 29:Active; 45:Out → 70:Active; 70:Out → 72:In |
| `wst_ep1_05.questphase / h0 / 71` (Journal) | `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/read_message_from_hands` | 71:Out → 31:In; 72:Out → 71:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `wst_ep1_05.questphase / h0 / 41` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` | 44:Out → 41:In1 |
| `sts_04_hasan_default.questphase / h14 / 9` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene`; `#sts_04_sm_hasan_default` | 28:Out → 9:Hasan_default_1st_meeting_start; 9:Hasan_default_1st_meeting_end → 44:In |
| `sts_04_hasan_default.questphase / h14 / 29` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene`; `#sts_04_sm_hasan_default` | 43:Out → 29:Hasan_default_apartment_start; 44:Out → 29:Hasan_default_apartment_start |
| `sts_04_hasan_default.questphase / h245 / 28` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene`; `#sts_04_sm_hasan_default` | 29:Out → 28:Hasan_squat_start; 28:End1 → 37:In |
| `sts_04_hasan_default.questphase / h245 / 34` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene`; `#sts_04_sm_hasan_default` | 35:Out1 → 34:hasan_squat_talk_start; 34:End1 → 37:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 5 | `wst_ep1_05.questphase` | 29: PauseCondition: hasan_default_on; 29:Out → 5:In1 |
| `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 41 | `sts_04_hasan_default.questphase` | 44: FactsDBManager: hasan_default_on; 44:Out → 41:In1 |
| `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 22 | `sts_04_hasan_default.questphase` | 21: FactsDBManager: hasan_default_on; 21:Out → 22:In1 |
| `ep1\quest\ep1_default_dialogs.questphase` / h0 / 9 | `sts_04_hasan_default.questphase` | 12: PauseCondition: hasan_default_on; 12:Out → 9:In1; 9:Out1 → 12:In |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h14 / 9 | `sts_04_hasan_default.scene` | 28: FactsDBManager: hasan_apartment_default_dialogue_start; 28:Out → 9:Hasan_default_1st_meeting_start; 9:Hasan_default_1st_meeting_end → 44:In |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h14 / 29 | `sts_04_hasan_default.scene` | 43: PauseCondition; 44: PauseCondition; 43:Out → 29:Hasan_default_apartment_start; 44:Out → 29:Hasan_default_apartment_start |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h245 / 28 | `sts_04_hasan_default.scene` | 29: FactsDBManager: hasan_squat_default_dialogue_start; 29:Out → 28:Hasan_squat_start; 28:End1 → 37:In |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h245 / 34 | `sts_04_hasan_default.scene` | 35: LogicalHub; 35:Out1 → 34:hasan_squat_talk_start; 34:End1 → 37:In |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 14 | `ep1_world_stories.questphase` | 11: LogicalHub; 11:Out1 → 14:In1 |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 6 | `wst_ep1_06.questphase` | 30: PauseCondition: sts_ep1_04_finished; 30:Out → 6:In1 |
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
| `sts_04_hasan_default.scene` | Hasan_default_1st_meeting_start, hasan_squat_talk_start, Hasan_squat_start, Hasan_default_apartment_start → End1, Hasan_squat_end, Hasan_default_1st_meeting_end | hasan; hasan_squat; v; 92 nodes / 112 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_04_hasan_default.scene / n5 / 0` | Right, what's this about? (`what do you want`) | No option-level predicate stored | 0:0 → 21:0:0 |
| `sts_04_hasan_default.scene / n5 / 1` | Landed on your feet, huh? (`looking good`) | No option-level predicate stored | 0:1 → 18:0:0 |
| `sts_04_hasan_default.scene / n26 / 0` | Hard getting back on your feet? (`Fluff 1`) | No option-level predicate stored | 0:0 → 35:0:0 |
| `sts_04_hasan_default.scene / n26 / 1` | What're you doing now? (`Fluff 2`) | No option-level predicate stored | 0:1 → 36:0:0 |
| `sts_04_hasan_default.scene / n46 / 0` | Hasan? (`Option_02`) | No option-level predicate stored | 0:0 → 341:0:1 |
| `sts_04_hasan_default.scene / n87 / 0` | You need help? (`need help`) | No option-level predicate stored | 0:0 → 92:0:0 |
| `sts_04_hasan_default.scene / n87 / 1` | Just passin' by. (`nothing`) | No option-level predicate stored | 0:1 → 151:0:0 |
| `sts_04_hasan_default.scene / n87 / 2` | You hazed me. (`you cheated`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "sts_ep1_04_hasan_let_go_earlier"}}} | 0:2 → 163:0:0 |
| `sts_04_hasan_default.scene / n87 / 3` | Why didn't you go back to Zetatech? (`didnt come back`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "sts_ep1_04_hasan_let_go_earlier", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:3 → 159:0:0 |
| `sts_04_hasan_default.scene / n87 / 4` | What happened? (`what happened`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "sts_ep1_04_hasan_let_go"}}} | 0:4 → 88:0:0 |
| `sts_04_hasan_default.scene / n130 / 0` | Thanks. (`thanks`) | No option-level predicate stored | 0:0 → 585:0:1 |
| `sts_04_hasan_default.scene / n130 / 1` | Nah, no need. (`cant take it`) | No option-level predicate stored | 0:1 → 593:0:1 |
| `sts_04_hasan_default.scene / n130 / 2` | What's this gun? (`whats this`) | No option-level predicate stored | 0:2 → 137:0:0 |
| `sts_04_hasan_default.scene / n572 / 0` | Text join unresolved (`Option`) | No option-level predicate stored | 0:0 → 621:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `ep1_standalone` | Producer outside selected context | wst_ep1_05.questphase / h0 / 75 |
| `hasan_apartment_default_dialogue_start` | sts_04_hasan_default.questphase / h14 / 28 | No reader in selected context |
| `hasan_default_1st_meeting_finished` | sts_04_hasan_default.scene / scene / 155 | sts_04_hasan_default.questphase / h14 / 27; sts_04_hasan_default.questphase / h14 / 53; wst_ep1_05.questphase / h0 / 59 |
| `hasan_default_gun_taken_answer_01` | sts_04_hasan_default.scene / scene / 585 | sts_04_hasan_default.scene / scene / 597 |
| `hasan_default_gun_taken_answer_02` | sts_04_hasan_default.scene / scene / 593 | sts_04_hasan_default.scene / scene / 597 |
| `hasan_default_on` | wst_ep1_05.questphase / h0 / 44 | sts_04_hasan_default.questphase / h0 / 46 |
| `hasan_squat_default_dialogue_start` | sts_04_hasan_default.questphase / h245 / 29; sts_04_hasan_default.scene / scene / 341 | sts_04_hasan_default.questphase / h245 / 47 |
| `sts_ep1_04_blueprints_corpo` | wst_ep1_05.questphase / h0 / 42 | wst_ep1_05.questphase / h0 / 33 |
| `sts_ep1_04_blueprints_hasan` | Producer outside selected context | sts_04_hasan_default.questphase / h0 / 52 |
| `sts_ep1_04_hasan_let_go` | Producer outside selected context | sts_04_hasan_default.scene / scene / 87 |
| `sts_ep1_04_hasan_let_go_earlier` | Producer outside selected context | sts_04_hasan_default.scene / scene / 87 |
| `sts_ep1_04_mr_hands_holo_convinced` | wst_ep1_05.questphase / h0 / 43 | sts_04_hasan_default.questphase / h0 / 53; wst_ep1_05.questphase / h0 / 34 |
| `travelling_merchant_lives` | Producer outside selected context | wst_ep1_05.questphase / h0 / 81 |
| `wst_ep1_05_active` | wst_ep1_05.questphase / h0 / 45 | No reader in selected context |
| `wst_ep1_05_finished` | wst_ep1_05.questphase / h0 / 27 | No reader in selected context |
| `wst_ep1_05_gun_reveal` | sts_04_hasan_default.scene / scene / 213 | wst_ep1_05.questphase / h0 / 25; wst_ep1_05.questphase / h0 / 57 |
| `wst_ep1_05_gun_taken` | wst_ep1_05.questphase / h0 / 53 | sts_04_hasan_default.scene / scene / 265; sts_04_hasan_default.scene / scene / 274; sts_04_hasan_default.scene / scene / 597; wst_ep1_05.questphase / h0 / 55 |
| `wst_ep1_05_start` | wst_ep1_05.questphase / h0 / 10 | No reader in selected context |
| `wst_ep1_06_active` | Producer outside selected context | sts_04_hasan_default.questphase / h245 / 33 |
| `wst_ep1_06_hasan_scene_finished` | sts_04_hasan_default.scene / scene / 195 | sts_04_hasan_default.questphase / h245 / 30; sts_04_hasan_default.questphase / h245 / 44 |

## Exact gates, joins and cancellation

<details><summary>60 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `wst_ep1_05.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_05_gun_reveal"}}}` | 23:Out → 25:In; 25:Out → 24:Inactive |
| `wst_ep1_05.questphase / h0 / 33` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_04_blueprints_corpo"}}}` | 47:Out → 33:In; 33:True → 34:In |
| `wst_ep1_05.questphase / h0 / 34` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_04_mr_hands_holo_convinced"}}}` | 33:True → 34:In; 34:True → 75:In |
| `wst_ep1_05.questphase / h0 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":3,"hours":16}}}` | 0:Out → 47:In; 47:Out → 33:In |
| `wst_ep1_05.questphase / h0 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"106070678147","quantity":1}}}` | 74:Out → 52:In; 52:Out → 53:In |
| `wst_ep1_05.questphase / h0 / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_05_gun_taken"}}}` | 48:Out → 55:In; 55:Out → 56:Succeeded |
| `wst_ep1_05.questphase / h0 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_05_gun_reveal"}}}` | 31:Out → 57:In; 57:Out → 49:In |
| `wst_ep1_05.questphase / h0 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hasan_default_1st_meeting_finished"}}}` | 27:Out → 59:In; 59:Out → 32:In |
| `wst_ep1_05.questphase / h0 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive_v_response/sts_ep1_04_sms_hasan_alive_v_response_01","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 38:Out → 61:In; 61:Out → 63:Active |
| `wst_ep1_05.questphase / h0 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive_v_response/sts_ep1_04_sms_hasan_alive_v_response_02","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 38:Out → 62:In; 62:Out → 64:Active |
| `wst_ep1_05.questphase / h0 / 66` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive_v_response/sts_ep1_04_sms_hasan_alive_v_response_01","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 69:Out → 66:In; 66:False → 68:In1 |
| `wst_ep1_05.questphase / h0 / 67` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive_v_response/sts_ep1_04_sms_hasan_alive_v_response_02","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 69:Out → 67:In; 67:False → 68:In2 |
| `wst_ep1_05.questphase / h0 / 68` | `questLogicalAndNodeDefinition` `{}` | 68:Out1 → 65:Inactive; 66:False → 68:In1; 67:False → 68:In2 |
| `wst_ep1_05.questphase / h0 / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","hours":1}}}` | 38:Out → 69:In; 69:Out → 66:In; 69:Out → 67:In |
| `wst_ep1_05.questphase / h0 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 70:Out → 72:In; 72:Out → 71:Succeeded |
| `wst_ep1_05.questphase / h0 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 3:Out → 73:In; 73:Out → 45:In |
| `wst_ep1_05.questphase / h0 / 75` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone"}}}` | 34:True → 75:In; 75:True → 76:In; 75:False → 77:In |
| `wst_ep1_05.questphase / h0 / 76` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"EP1_Minor"}}}` | 75:True → 76:In; 76:Out → 78:In1 |
| `wst_ep1_05.questphase / h0 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"MinorQuestAndSts"}}}` | 75:False → 77:In; 77:Out → 78:In2 |
| `wst_ep1_05.questphase / h0 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_05_tr_start"},{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/container_zone_prefab4PZIADQ/container_zone_world_stories_prefab4SY6XVQ/wst_ep1_05_prefabRYSKJEA/wst_ep1_05_gameplay_prefabNNJEMLI/wst_ep1_05_devices_prefabLYHGQTY/single_door_hinged_prefabJRWRQ3Y/{single_door}_prefab67PSHKA","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}]}}` | 20:Out → 80:In; 80:Out → 22:Succeeded; 80:Out → 35:Inactive |
| `wst_ep1_05.questphase / h0 / 81` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":999}}}` | 0:Out → 81:In |
| `sts_04_hasan_default.questphase / h0 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#wst_ep1_05_com","names":["hasan"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0},"comparisonType":"Less"}}}` | 45:Out → 44:In1; 44:Out1 → 45:In; 53:True → 45:In |
| `sts_04_hasan_default.questphase / h0 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hasan_default_on","value":1,"comparisonType":"Less"}}}` | 0:Out → 46:In; 46:Out → 1:In |
| `sts_04_hasan_default.questphase / h0 / 52` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_04_blueprints_hasan"}}}` | 0:Out → 52:In; 52:True → 54:In; 52:True → 56:In; 52:False → 53:In |
| `sts_04_hasan_default.questphase / h0 / 53` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_04_mr_hands_holo_convinced"}}}` | 53:True → 45:In; 53:True → 51:In; 52:False → 53:In |
| `sts_04_hasan_default.questphase / h0 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#wst_ep1_06_com","names":["hasan"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0},"comparisonType":"Less"}}}` | 52:True → 56:In; 56:Out → 55:In1; 55:Out1 → 56:In |
| `sts_04_hasan_default.questphase / h14 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#wst_ep1_05_com","names":["hasan"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0}}}}` | 0:Out → 24:In; 24:Out → 1:In |
| `sts_04_hasan_default.questphase / h14 / 27` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hasan_default_1st_meeting_finished"}}}` | 0:Out → 27:In; 27:True → 42:In; 27:False → 45:In |
| `sts_04_hasan_default.questphase / h14 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_05_tr_default_activate"}}` | 27:True → 42:In; 42:Out → 30:In |
| `sts_04_hasan_default.questphase / h14 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterWorkspot_ConditionType","puppetRef":{"$type":"gameEntityReference","reference":"#wst_ep1_05_com","names":["hasan"]},"spotRef":"#wst_ep1_05_hasan_ws_after"}}}` | 43:Out → 29:Hasan_default_apartment_start; 30:Out → 43:In |
| `sts_04_hasan_default.questphase / h14 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterWorkspot_ConditionType","puppetRef":{"$type":"gameEntityReference","reference":"#wst_ep1_05_com","names":["hasan"]},"spotRef":"#wst_ep1_05_hasan_ws_after"}}}` | 9:Hasan_default_1st_meeting_end → 44:In; 44:Out → 29:Hasan_default_apartment_start |
| `sts_04_hasan_default.questphase / h14 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/container_zone_prefab4PZIADQ/container_zone_world_stories_prefab4SY6XVQ/wst_ep1_05_prefabRYSKJEA/wst_ep1_05_gameplay_prefabNNJEMLI/wst_ep1_05_devices_prefabLYHGQTY/single_door_hinged_prefabJRWRQ3Y/{single_door}_prefab67PSHKA","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 27:False → 45:In; 45:Out → 46:In; 45:Out → 56:In |
| `sts_04_hasan_default.questphase / h14 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 46:Out → 28:In; 45:Out → 46:In |
| `sts_04_hasan_default.questphase / h14 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_05_tr_inside"}}` | 54:CutSource → 47:CutDestination; 50:Out → 47:In; 56:Out → 47:In; 47:Out → 58:In |
| `sts_04_hasan_default.questphase / h14 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_05_tr_inside"}}` | 54:CutSource → 48:CutDestination; 49:Out → 48:In; 48:Out → 57:In |
| `sts_04_hasan_default.questphase / h14 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 49:Out → 48:In; 51:Out → 49:In |
| `sts_04_hasan_default.questphase / h14 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 50:Out → 47:In; 52:Out → 50:In |
| `sts_04_hasan_default.questphase / h14 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hasan_default_1st_meeting_finished"}}}` | 56:Out → 53:In; 53:Out → 54:In |
| `sts_04_hasan_default.questphase / h14 / 54` | `questCutControlNodeDefinition` `{}` | 54:CutSource → 47:CutDestination; 54:CutSource → 48:CutDestination; 53:Out → 54:In; 54:Out → 55:In |
| `sts_04_hasan_default.questphase / h14 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_05_tr_inside"}}` | 45:Out → 56:In; 56:Out → 47:In; 56:Out → 53:In |
| `sts_04_hasan_default.questphase / h14 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 59:Out → 51:In; 58:Out → 59:In |
| `sts_04_hasan_default.questphase / h245 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#wst_ep1_06_com","names":["hasan"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":150.0}}}}` | 0:Out → 24:In; 24:Out → 1:In |
| `sts_04_hasan_default.questphase / h245 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_06_tr_start"}}` | 33:Out → 26:In; 26:Out → 30:In |
| `sts_04_hasan_default.questphase / h245 / 30` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_06_hasan_scene_finished"}}}` | 26:Out → 30:In; 30:False → 29:In; 30:True → 37:In; 30:False → 47:In |
| `sts_04_hasan_default.questphase / h245 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_06_active"}}}` | 0:Out → 33:In; 33:Out → 26:In |
| `sts_04_hasan_default.questphase / h245 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 28:End1 → 37:In; 30:True → 37:In; 34:End1 → 37:In; 37:Out → 35:In1 |
| `sts_04_hasan_default.questphase / h245 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_06_tr_ui"}}` | 45:CutSource → 38:CutDestination; 41:Out → 38:In; 47:Out → 38:In; 38:Out → 49:In |
| `sts_04_hasan_default.questphase / h245 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_06_tr_ui"}}` | 45:CutSource → 39:CutDestination; 40:Out → 39:In; 39:Out → 48:In |
| `sts_04_hasan_default.questphase / h245 / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 40:Out → 39:In; 42:Out → 40:In |
| `sts_04_hasan_default.questphase / h245 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 41:Out → 38:In; 43:Out → 41:In |
| `sts_04_hasan_default.questphase / h245 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_06_hasan_scene_finished"}}}` | 47:Out → 44:In; 44:Out → 45:In |
| `sts_04_hasan_default.questphase / h245 / 45` | `questCutControlNodeDefinition` `{}` | 45:CutSource → 38:CutDestination; 45:CutSource → 39:CutDestination; 44:Out → 45:In; 45:Out → 46:In |
| `sts_04_hasan_default.questphase / h245 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hasan_squat_default_dialogue_start"}}}` | 30:False → 47:In; 47:Out → 38:In; 47:Out → 44:In |
| `sts_04_hasan_default.questphase / h245 / 50` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 50:Out → 42:In; 49:Out → 50:In |
| `sts_04_hasan_default.scene / scene / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 11:0:0 → 54:0:1; 50:0:0 → 54:0:1; 53:1:0 → 54:0:0; 54:0:0 → 73:0:0; 55:0:0 → 54:0:1; 57:0:0 → 54:0:1 |
| `sts_04_hasan_default.scene / scene / 265` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_05_gun_taken"}}}` | 28:2:0 → 265:0:1; 133:0:0 → 265:0:1; 265:0:0 → 140:0:0 |
| `sts_04_hasan_default.scene / scene / 274` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_05_gun_taken"}}}` | 137:0:0 → 274:0:1; 274:0:0 → 585:0:1; 274:0:1 → 130:0:0 |
| `sts_04_hasan_default.scene / scene / 353` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6,"miliseconds":500}}}` | 353:0:0 → 347:0:0; 621:0:0 → 353:0:1 |
| `sts_04_hasan_default.scene / scene / 597` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wst_ep1_05_gun_taken","value":1,"comparisonType":"Equal"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hasan_default_gun_taken_answer_01","comparisonType":"Equal"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"hasan_default_gun_taken_answer_02","comparisonType":"Equal"}},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_05_tr_inside"}]}}` | 213:0:0 → 597:0:1; 597:0:0 → 140:0:0 |
| `sts_04_hasan_default.scene / scene / 605` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#wst_ep1_06_com","names":["hasan"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"LessOrEqual"}}}` | 11:0:0 → 605:0:1; 605:0:0 → 607:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `choice_gate` | sts_04_hasan_default.scene / scene / 130; sts_04_hasan_default.scene / scene / 26; sts_04_hasan_default.scene / scene / 46; sts_04_hasan_default.scene / scene / 5; +2 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | sts_04_hasan_default.questphase / h0 / 51; sts_04_hasan_default.questphase / h0 / 54; sts_04_hasan_default.questphase / h14 / 30; wst_ep1_05.questphase / h0 / 32 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | sts_04_hasan_default.questphase / h0 / 46; sts_04_hasan_default.questphase / h0 / 52; sts_04_hasan_default.questphase / h0 / 53; sts_04_hasan_default.questphase / h14 / 27; +17 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | wst_ep1_05.questphase / h0 / 31 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_04_hasan_default.questphase / h14 / 45; wst_ep1_05.questphase / h0 / 80 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | wst_ep1_05.questphase / h0 / 47 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | wst_ep1_05.questphase / h0 / 52 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_read` | wst_ep1_05.questphase / h0 / 72 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `parallel_join` | wst_ep1_05.questphase / h0 / 68 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_04_hasan_default.questphase / h14 / 28; sts_04_hasan_default.questphase / h245 / 29; sts_04_hasan_default.scene / scene / 155; sts_04_hasan_default.scene / scene / 195; +11 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sts_04_hasan_default.questphase / h14 / 46; sts_04_hasan_default.questphase / h14 / 49; sts_04_hasan_default.questphase / h14 / 50; sts_04_hasan_default.questphase / h14 / 59; +8 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_04_hasan_default.questphase / h14 / 54; sts_04_hasan_default.questphase / h245 / 45 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `scene_interface` | sts_04_hasan_default.questphase / h14 / 29; sts_04_hasan_default.questphase / h14 / 9; sts_04_hasan_default.questphase / h245 / 28; sts_04_hasan_default.questphase / h245 / 34 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `workspot_performance` | sts_04_hasan_default.scene / scene / 315; sts_04_hasan_default.scene / scene / 317; sts_04_hasan_default.scene / scene / 318; sts_04_hasan_default.scene / scene / 494; +23 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | wst_ep1_05.questphase / h0 / 49; wst_ep1_05.questphase / h0 / 50; wst_ep1_05.questphase / h0 / 54 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` | content candidate; journal anchor | `ep1-wst-ep1-05` |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` | content candidate; forward dependency | `ep1-shared` |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` | content candidate; forward dependency | `ep1-shared` |

Evidence shards for this dossier (including parent context): [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz), [ep1-wst-ep1-05](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-wst-ep1-05.json.gz), [ep1-wst-ep1-06](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-wst-ep1-06.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
