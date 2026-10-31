# One Way or Another

Journal: `ep1/quests/minor_quest/wst_ep1_09` · `MinorQuest` · hash `1876825856`.

**Coverage: journal-linked.** 13 exact journal-linked nodes in 3 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Meet with Nele Springer. (Primary) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/find_nele` |
| Go to the meeting point. (Primary) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/meet_nele` |
| Read the message from Nele Springer. (Primary) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/read_nele_message` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `boulevard_av.questphase / h1660 / 70` (PauseCondition) | `ep1/quests/minor_quest/wst_ep1_09` | 0:Out → 70:In; 70:Out → 71:In; 70:Out → 75:In; 70:Out → 82:In |
| `boulevard_av.questphase / h1660 / 72` (PauseCondition) | `ep1/quests/minor_quest/wst_ep1_09` | 77:Out1 → 72:In; 72:Out → 73:In |
| `ep1_community.questphase / h13604 / 70` (PauseCondition) | `ep1/quests/minor_quest/wst_ep1_09` | 0:Out → 70:In; 70:Out → 71:In; 70:Out → 75:In; 70:Out → 82:In |
| `ep1_community.questphase / h13604 / 72` (PauseCondition) | `ep1/quests/minor_quest/wst_ep1_09` | 77:Out1 → 72:In; 72:Out → 73:In |
| `wst_ep1_09.questphase / h0 / 58` (Journal) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/meet_nele` | 118:Out → 58:Succeeded; 58:Out → 59:Active |
| `wst_ep1_09.questphase / h0 / 59` (Journal) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/find_nele` | 59:Out → 51:In; 58:Out → 59:Active |
| `wst_ep1_09.questphase / h0 / 61` (Journal) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/find_nele` | 81:Out → 61:Succeeded; 61:Out → 62:Succeeded |
| `wst_ep1_09.questphase / h0 / 62` (Journal) | `ep1/quests/minor_quest/wst_ep1_09` | 61:Out → 62:Succeeded; 62:Out → 102:In |
| `wst_ep1_09.questphase / h0 / 85` (Journal) | `ep1/quests/minor_quest/wst_ep1_09/description` | 132:Out → 85:Active; 85:Out → 103:In; 85:Out → 104:In |
| `wst_ep1_09.questphase / h0 / 96` (Journal) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/read_nele_message` | 1:Out → 96:Active; 96:Out → 46:Active |
| `wst_ep1_09.questphase / h0 / 131` (Journal) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/meet_nele` | 133:Out → 131:Active; 131:Out → 134:In |
| `wst_ep1_09.questphase / h0 / 132` (Journal) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/read_nele_message` | 132:Out → 85:Active; 134:Out → 132:Succeeded |
| `wst_ep1_09.questphase / h0 / 141` (MappinManager) | `ep1/quests/minor_quest/wst_ep1_09/meet_nele/find_nele/search_area` | 142:Out → 141:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\community\ep1_community.questphase` / h15727 / 2 | `boulevard_av.questphase` | 0: Input; 0:Out → 2:In1 |
| `ep1\openworld\community\ep1_world_community.questphase` / h0 / 2 | `boulevard_av.questphase` | 0: Input; 0:Out → 2:In1 |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 12 | `ep1_community.questphase` | 26: LogicalHub; 26:Out1 → 12:In1 |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 9 | `wst_ep1_09.questphase` | 33: PauseCondition: wst_ep1_09_active Equal 1; 33:Out → 9:In1 |
| `ep1\openworld\community\ep1_community.questphase` / h0 / 8 | `ep1_world_community.questphase` | 23: PauseCondition: ep1_active GreaterOrEqual 1; 23:Out → 8:In1 |
| `ep1\openworld\vendors\vehicle_metaquest\phases\vehicle_metaquest_ep1_bugfixing.questphase` / h17 / 6 | `ep1_open_world.questphase` | 4: Condition: militech_hellhound_available; 4:False → 6:CP77-63752 |
| `ep1\quest\ep1.questphase` / h58 / 5 | `ep1_open_world.questphase` | 0: Input; 9: CutControl; 0:Out → 5:In1; 9:CutSource → 5:CutDestination |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 14 | `ep1_world_stories.questphase` | 11: LogicalHub; 11:Out1 → 14:In1 |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 16 | `vehicle_metaquest_ep1_bugfixing.questphase` | 0: Input; 0:Out → 16:In1 |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 3 | `ep1_openworld_bugfixing.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\quest\ep1.questphase` / h58 / 2 | `ep1_bugfixing.questphase` | 25: LogicalXor; 2:CP77-65722_out → 27:In; 2:CP77-64292_out → 26:In; 25:Out1 → 2:In1; 2:Out1 → 4:In2; 2:growl → 4:growl |

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
| `ep1_standalone` | Producer outside selected context | wst_ep1_09.questphase / h0 / 120 |
| `travelling_merchant_lives` | Producer outside selected context | wst_ep1_09.questphase / h0 / 143 |
| `wst_ep1_09_cleanup_done` | wst_ep1_09.questphase / h0 / 144 | No reader in selected context |
| `wst_ep1_09_finished` | wst_ep1_09.questphase / h0 / 102 | No reader in selected context |
| `wst_ep1_09_start` | wst_ep1_09.questphase / h0 / 51 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>54 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `boulevard_av.questphase / h1660 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cz_gp_area_c_car_002"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 12:Out → 14:In; 14:Out → 13:In; 14:Out → 26:In |
| `boulevard_av.questphase / h1660 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":79200},"end":{"$type":"GameTime","seconds":21540}}}}` | 0:Out → 15:In; 15:Out → 12:In; 16:Out1 → 15:In |
| `boulevard_av.questphase / h1660 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":21600},"end":{"$type":"GameTime","seconds":79140}}}}` | 27:Out1 → 17:In; 17:Out → 18:In |
| `boulevard_av.questphase / h1660 / 27` | `questLogicalAndNodeDefinition` `{}` | 13:Out → 27:In1; 27:Out1 → 17:In; 26:Out → 27:In2 |
| `boulevard_av.questphase / h1660 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":79200},"end":{"$type":"GameTime","seconds":21540}}}}` | 37:Out1 → 31:In; 31:Out → 38:In |
| `boulevard_av.questphase / h1660 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":21600},"end":{"$type":"GameTime","seconds":79140}}}}` | 0:Out → 32:In; 39:Out1 → 32:In; 32:Out → 33:In |
| `boulevard_av.questphase / h1660 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cz_gp_area_c_car_004"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 33:Out → 34:In; 34:Out → 35:In; 34:Out → 36:In |
| `boulevard_av.questphase / h1660 / 37` | `questLogicalAndNodeDefinition` `{}` | 37:Out1 → 31:In; 35:Out → 37:In1; 36:Out → 37:In2 |
| `boulevard_av.questphase / h1660 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#n_cz_gp_area_c_car_001"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 56:Out → 58:In; 58:Out → 57:In; 58:Out → 66:In; 58:Out → 68:In |
| `boulevard_av.questphase / h1660 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":79200},"end":{"$type":"GameTime","seconds":21540}}}}` | 0:Out → 59:In; 59:Out → 56:In; 60:Out1 → 59:In |
| `boulevard_av.questphase / h1660 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":21600},"end":{"$type":"GameTime","seconds":79140}}}}` | 67:Out1 → 61:In; 61:Out → 62:In |
| `boulevard_av.questphase / h1660 / 67` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 57:Out → 67:In1; 67:Out1 → 61:In; 66:Out → 67:In2; 68:Out → 67:In3 |
| `boulevard_av.questphase / h1660 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/wst_ep1_09","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 0:Out → 70:In; 70:Out → 71:In; 70:Out → 75:In; 70:Out → 82:In |
| `boulevard_av.questphase / h1660 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/wst_ep1_09","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 77:Out1 → 72:In; 72:Out → 73:In |
| `boulevard_av.questphase / h1660 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#cz_gp_hidden_camp_combat_tr"}}` | 72:Out → 73:In; 73:Out → 76:In; 73:Out → 81:In; 73:Out → 83:In |
| `boulevard_av.questphase / h1660 / 77` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 71:Out → 77:In1; 77:Out1 → 72:In; 75:Out → 77:In2; 82:Out → 77:In3 |
| `ep1_community.questphase / h13604 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cz_gp_area_c_car_002"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 12:Out → 14:In; 14:Out → 13:In; 14:Out → 26:In |
| `ep1_community.questphase / h13604 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":79200},"end":{"$type":"GameTime","seconds":21540}}}}` | 0:Out → 15:In; 15:Out → 12:In; 16:Out1 → 15:In |
| `ep1_community.questphase / h13604 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":21600},"end":{"$type":"GameTime","seconds":79140}}}}` | 27:Out1 → 17:In; 17:Out → 18:In |
| `ep1_community.questphase / h13604 / 27` | `questLogicalAndNodeDefinition` `{}` | 13:Out → 27:In1; 27:Out1 → 17:In; 26:Out → 27:In2 |
| `ep1_community.questphase / h13604 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":79200},"end":{"$type":"GameTime","seconds":21540}}}}` | 37:Out1 → 31:In; 31:Out → 38:In |
| `ep1_community.questphase / h13604 / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":21600},"end":{"$type":"GameTime","seconds":79140}}}}` | 0:Out → 32:In; 39:Out1 → 32:In; 32:Out → 33:In |
| `ep1_community.questphase / h13604 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cz_gp_area_c_car_004"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 33:Out → 34:In; 34:Out → 35:In; 34:Out → 36:In |
| `ep1_community.questphase / h13604 / 37` | `questLogicalAndNodeDefinition` `{}` | 37:Out1 → 31:In; 35:Out → 37:In1; 36:Out → 37:In2 |
| `ep1_community.questphase / h13604 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#n_cz_gp_area_c_car_001"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 56:Out → 58:In; 58:Out → 57:In; 58:Out → 66:In; 58:Out → 68:In |
| `ep1_community.questphase / h13604 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":79200},"end":{"$type":"GameTime","seconds":21540}}}}` | 0:Out → 59:In; 59:Out → 56:In; 60:Out1 → 59:In |
| `ep1_community.questphase / h13604 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":21600},"end":{"$type":"GameTime","seconds":79140}}}}` | 67:Out1 → 61:In; 61:Out → 62:In |
| `ep1_community.questphase / h13604 / 67` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 57:Out → 67:In1; 67:Out1 → 61:In; 66:Out → 67:In2; 68:Out → 67:In3 |
| `ep1_community.questphase / h13604 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/wst_ep1_09","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 0:Out → 70:In; 70:Out → 71:In; 70:Out → 75:In; 70:Out → 82:In |
| `ep1_community.questphase / h13604 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/wst_ep1_09","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 77:Out1 → 72:In; 72:Out → 73:In |
| `ep1_community.questphase / h13604 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#cz_gp_hidden_camp_combat_tr"}}` | 72:Out → 73:In; 73:Out → 76:In; 73:Out → 81:In; 73:Out → 83:In |
| `ep1_community.questphase / h13604 / 77` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 71:Out → 77:In1; 77:Out1 → 72:In; 75:Out → 77:In2; 82:Out → 77:In3 |
| `wst_ep1_09.questphase / h0 / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_09_init_trigger"}}` | 55:Out → 54:In; 54:Out → 106:In |
| `wst_ep1_09.questphase / h0 / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 55:Out → 54:In; 65:Success → 55:In |
| `wst_ep1_09.questphase / h0 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_09_search_trigger"}}` | 73:Out → 57:In; 57:Out → 118:In |
| `wst_ep1_09.questphase / h0 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#wst_ep1_09_com"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 66:Out → 50:In; 63:Out → 66:In; 66:Out → 81:In |
| `wst_ep1_09.questphase / h0 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/boulevard_av_prefabHHWJYRA/boulevard_av_world_stories_prefabQ2QUVMY/wst_ep1_09_prefabSIYSNCQ/wst_ep1_09_gameplay_prefabV6YTDJQ/wst_ep1_09_devices_prefabMLOUK3Q/double_door_freight_e_prefabOGWHHPA/door_2","eventType":"Executed"}}}` | 51:Out → 68:In; 68:Out → 70:In; 68:Out → 137:In |
| `wst_ep1_09.questphase / h0 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 68:Out → 70:In; 70:Out → 77:In; 70:Out → 129:In |
| `wst_ep1_09.questphase / h0 / 81` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 81:Out → 61:Succeeded; 66:Out → 81:In |
| `wst_ep1_09.questphase / h0 / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/nele_spranger/wst_ep1_09/meet_ambush","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 46:Out → 90:In; 90:Out → 133:In |
| `wst_ep1_09.questphase / h0 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/nele_spranger/wst_ep1_09/v_answer/v_answer_message","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 85:Out → 103:In; 103:Out → 105:Active |
| `wst_ep1_09.questphase / h0 / 104` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/nele_spranger/wst_ep1_09/v_answer/v_answer_message_ambush_ver2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 85:Out → 104:In; 104:Out → 105:Active |
| `wst_ep1_09.questphase / h0 / 111` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_09_init_trigger"}}` | 111:Out → 101:In; 124:Out → 111:In |
| `wst_ep1_09.questphase / h0 / 116` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/nele_spranger/wst_ep1_09/v_answer/v_answer_message_ambush_ver2","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/contacts/nele_spranger/wst_ep1_09/v_answer/v_answer_message","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}]}}` | 116:False → 89:Inactive; 116:True → 93:In; 139:Out → 116:In |
| `wst_ep1_09.questphase / h0 / 120` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone"}}}` | 0:Out → 120:In; 120:True → 121:In; 120:False → 122:In |
| `wst_ep1_09.questphase / h0 / 121` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"EP1_Minor"}}}` | 120:True → 121:In; 121:Out → 123:In1 |
| `wst_ep1_09.questphase / h0 / 122` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"MinorQuestAndSts"}}}` | 120:False → 122:In; 122:Out → 123:In2 |
| `wst_ep1_09.questphase / h0 / 124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wst_ep1_09_init_trigger"}}` | 124:Out → 1:Active; 124:Out → 111:In; 123:Out1 → 124:In; 127:Out → 124:In |
| `wst_ep1_09.questphase / h0 / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":300}}}` | 128:Out → 80:In; 129:Out → 128:In |
| `wst_ep1_09.questphase / h0 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 90:Out → 133:In; 133:Out → 131:Active |
| `wst_ep1_09.questphase / h0 / 134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 131:Out → 134:In; 134:Out → 132:Succeeded |
| `wst_ep1_09.questphase / h0 / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_09_close_to_container_trigger"}}` | 139:Out → 116:In; 118:Out → 139:In |
| `wst_ep1_09.questphase / h0 / 142` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 93:Out → 142:In; 142:Out → 141:Active |
| `wst_ep1_09.questphase / h0 / 143` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":999}}}` | 0:Out → 143:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | boulevard_av.questphase / h1660 / 14; boulevard_av.questphase / h1660 / 34; boulevard_av.questphase / h1660 / 58; ep1_community.questphase / h13604 / 14; +3 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `call_lifecycle` | wst_ep1_09.questphase / h0 / 93; wst_ep1_09.questphase / h0 / 95 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `combat_control` | wst_ep1_09.questphase / h0 / 65 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | boulevard_av.questphase / h1660 / 71; boulevard_av.questphase / h1660 / 75; boulevard_av.questphase / h1660 / 78; boulevard_av.questphase / h1660 / 79; +20 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | wst_ep1_09.questphase / h0 / 120; wst_ep1_09.questphase / h0 / 143 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | wst_ep1_09.questphase / h0 / 108; wst_ep1_09.questphase / h0 / 135; wst_ep1_09.questphase / h0 / 136; wst_ep1_09.questphase / h0 / 77; +1 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | wst_ep1_09.questphase / h0 / 55 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_read` | wst_ep1_09.questphase / h0 / 90 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `parallel_join` | boulevard_av.questphase / h1660 / 27; boulevard_av.questphase / h1660 / 37; boulevard_av.questphase / h1660 / 67; boulevard_av.questphase / h1660 / 77; +4 locations in catalogue.json | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | wst_ep1_09.questphase / h0 / 102; wst_ep1_09.questphase / h0 / 144; wst_ep1_09.questphase / h0 / 51 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | wst_ep1_09.questphase / h0 / 128; wst_ep1_09.questphase / h0 / 133; wst_ep1_09.questphase / h0 / 134; wst_ep1_09.questphase / h0 / 142; +2 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `vehicle_control` | boulevard_av.questphase / h1660 / 13; boulevard_av.questphase / h1660 / 26; boulevard_av.questphase / h1660 / 35; boulevard_av.questphase / h1660 / 36; +10 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `world_variant` | wst_ep1_09.questphase / h0 / 101; wst_ep1_09.questphase / h0 / 106; wst_ep1_09.questphase / h0 / 137; wst_ep1_09.questphase / h0 / 138 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\community\boulevard_av\boulevard_av.questphase` | content candidate; journal anchor | `ep1-shared` |
| `ep1\openworld\community\ep1_community.questphase` | content candidate; journal anchor | `ep1-shared` |
| `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` | content candidate; journal anchor | `ep1-wst-ep1-09` |

Evidence shards for this dossier (including parent context): [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz), [ep1-wst-ep1-09](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-wst-ep1-09.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
