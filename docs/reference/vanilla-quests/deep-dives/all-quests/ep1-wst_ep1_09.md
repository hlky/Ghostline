# One Way or Another

Journal: `ep1/quests/minor_quest/wst_ep1_09` · `MinorQuest` · hash `1876825856`.

Journal premise: Hm, chick’s up to somethin’. Hate to break it to ya, but nobody’s coming back to Dogtown just to see you. Still, if she wants a meet, fine – use it, get some answers. Just keep your eyes peeled... for both our sakes.

**Coverage: journal-linked.** 13 exact journal-linked nodes in 3 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

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
| `ep1\openworld\sandbox_activities\ep1_airdrop_activities.quest` / h0 / 40 | `ep1_community.questphase` | 41: FactsDBManager: ep1_active; 41:Out → 40:In1 |
| `ep1\openworld\sandbox_activities\ep1_sandbox_activities.quest` / h0 / 7 | `ep1_community.questphase` | 8: FactsDBManager: ep1_active; 8:Out → 7:In1 |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest` / h0 / 26 | `ep1_community.questphase` | 0: Start; 0:Out → 26:In1 |
| `ep1\openworld\street_stories\sts_ep1_07\sts_ep1_07.quest` / h0 / 9 | `ep1_community.questphase` | 14: FactsDBManager: ep1_side_content; 14:Out → 9:In1 |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest` / h0 / 19 | `ep1_community.questphase` | 20: FactsDBManager: ep1_active; 20:Out → 19:In1 |
| `ep1\openworld\street_stories\sts_ep1_07\sts_ep1_07.quest` / h0 / 11 | `wst_ep1_09.questphase` | 4: Scene: sts_ep1_07_chicken_test.scene; 4:ambush → 11:test def |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 9 | `wst_ep1_09.questphase` | 33: PauseCondition: wst_ep1_09_active Equal 1; 33:Out → 9:In1 |
| `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.quest` / h0 / 0 | `wst_ep1_09.questphase` | 2: FactsDBManager: wst_ep1_09_active; 2:Out → 0:In1 |
| `ep1\openworld\community\ep1_community.questphase` / h0 / 8 | `ep1_world_community.questphase` | 23: PauseCondition: ep1_active GreaterOrEqual 1; 23:Out → 8:In1 |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest` / h0 / 12 | `ep1_world_community.questphase` | 3: PauseCondition: {"seconds": 2}; 3:Out → 12:In1 |
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
| `ep1\openworld\ep1_open_world.questphase` / h0 / 14 | `ep1_world_stories.questphase` | 11: LogicalHub; 11:Out1 → 14:In1 |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest` / h0 / 7 | `ep1_world_stories.questphase` | 3: PauseCondition: {"seconds": 2}; 3:Out → 7:In1 |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest` / h0 / 112 | `ep1_world_stories.questphase` | 118: PauseCondition: sts_ep1_06_close_club; 118:Out → 112:In1 |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest` / h0 / 13 | `ep1_world_stories.questphase` | 7: PauseCondition: {"seconds": 2}; 7:Out → 13:In1 |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest` / h0 / 19 | `ep1_world_stories.questphase` | 3: FactsDBManager: ep1_12_test_def; 3:Out → 19:In1 |
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
| `ep1_standalone` | Producer outside selected context | wst_ep1_09.questphase / h0 / 120 |
| `travelling_merchant_lives` | Producer outside selected context | wst_ep1_09.questphase / h0 / 143 |
| `wst_ep1_09_cleanup_done` | wst_ep1_09.questphase / h0 / 144 | No reader in selected context |
| `wst_ep1_09_finished` | wst_ep1_09.questphase / h0 / 102 | No reader in selected context |
| `wst_ep1_09_start` | wst_ep1_09.questphase / h0 / 51 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>30 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `boulevard_av.questphase / h1660 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/wst_ep1_09","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 0:Out → 70:In; 70:Out → 71:In; 70:Out → 75:In; 70:Out → 82:In |
| `boulevard_av.questphase / h1660 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/wst_ep1_09","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 77:Out1 → 72:In; 72:Out → 73:In |
| `boulevard_av.questphase / h1660 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#cz_gp_hidden_camp_combat_tr"}}` | 72:Out → 73:In; 73:Out → 76:In; 73:Out → 81:In; 73:Out → 83:In |
| `boulevard_av.questphase / h1660 / 77` | `questLogicalAndNodeDefinition` `{"inputSocketCount":3}` | 71:Out → 77:In1; 77:Out1 → 72:In; 75:Out → 77:In2; 82:Out → 77:In3 |
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
| `actor_readiness` | wst_ep1_09.questphase / h0 / 66 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `call_lifecycle` | wst_ep1_09.questphase / h0 / 93; wst_ep1_09.questphase / h0 / 95 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `checkpoint` | wst_ep1_09.questphase / h0 / 118 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `combat_control` | wst_ep1_09.questphase / h0 / 65 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | boulevard_av.questphase / h1660 / 71; boulevard_av.questphase / h1660 / 75; boulevard_av.questphase / h1660 / 82; ep1_community.questphase / h13604 / 71; +10 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | wst_ep1_09.questphase / h0 / 120; wst_ep1_09.questphase / h0 / 143 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | wst_ep1_09.questphase / h0 / 108; wst_ep1_09.questphase / h0 / 135; wst_ep1_09.questphase / h0 / 136; wst_ep1_09.questphase / h0 / 77; +1 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | wst_ep1_09.questphase / h0 / 55 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_read` | wst_ep1_09.questphase / h0 / 90 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | wst_ep1_09.questphase / h0 / 1; wst_ep1_09.questphase / h0 / 105; wst_ep1_09.questphase / h0 / 131; wst_ep1_09.questphase / h0 / 132; +9 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | wst_ep1_09.questphase / h0 / 115; wst_ep1_09.questphase / h0 / 50 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `parallel_join` | boulevard_av.questphase / h1660 / 77; ep1_community.questphase / h13604 / 77 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | wst_ep1_09.questphase / h0 / 102; wst_ep1_09.questphase / h0 / 144; wst_ep1_09.questphase / h0 / 51 | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | wst_ep1_09.questphase / h0 / 128; wst_ep1_09.questphase / h0 / 133; wst_ep1_09.questphase / h0 / 134; wst_ep1_09.questphase / h0 / 142; +2 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `spatial_gate` | wst_ep1_09.questphase / h0 / 111; wst_ep1_09.questphase / h0 / 124; wst_ep1_09.questphase / h0 / 139; wst_ep1_09.questphase / h0 / 54; +1 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `world_variant` | wst_ep1_09.questphase / h0 / 101; wst_ep1_09.questphase / h0 / 106; wst_ep1_09.questphase / h0 / 137; wst_ep1_09.questphase / h0 / 138 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\community\boulevard_av\boulevard_av.questphase` | content candidate; journal anchor | `ep1-shared` |
| `ep1\openworld\community\ep1_community.questphase` | content candidate; journal anchor | `ep1-shared` |
| `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` | content candidate; journal anchor | `ep1-wst-ep1-09` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq306.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-01](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-01.json.gz), [ep1-sts-ep1-06-zembinsky](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-06-zembinsky.json.gz), [ep1-sts-ep1-07](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-07.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-08.json.gz), [ep1-sts-ep1-10](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-10.json.gz), [ep1-sts-ep1-12](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-12.json.gz), [ep1-wst-ep1-09](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-wst-ep1-09.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

54 repeated typed/socket path signatures in this selected graph context; 29 distinct direct resource identities; 0 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `20a77143a898bc753a26` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 71 -> 72 -> 73 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `a3e5f861a4b71433135a` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 55 -> 54 -> 106 | questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]; Out -> In; Out -> In |
| `eee71431d3a4d265f718` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 123 -> 124 -> 111 | questLogicalHubNodeDefinition -> questPauseConditionNodeDefinition[questTriggerCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out1 -> In; Out -> In |
| `7e7dbbc930b3717fd790` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 1 -> 96 -> 46 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `ebf923273db7cf158f68` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 63 -> 66 -> 50 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam] -> questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]; Out -> In; Out -> In |
| `1d48bd7cbbaeca8257d2` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 61 -> 62 -> 102 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Succeeded; Out -> In |
| `effb57f3d4d2c06d7dd2` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 54 -> 106 -> 138 | questPauseConditionNodeDefinition[questTriggerCondition] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState] -> questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]; Out -> In; Out -> In |
| `3e6f03030764fcc75954` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 85 -> 103 -> 105 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Active |
| `b54739889d4d9a0745d2` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 132 -> 85 -> 103 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> Active; Out -> In |
| `6791cbbe6b26cff8e34a` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 63 -> 66 -> 81 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; Out -> In; Out -> In |
| `f2a344c7d6fe49ec5e9b` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 127 -> 124 -> 111 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questTriggerCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `d68967c09edae88af083` | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 118 -> 58 -> 59 | questCheckpointNodeDefinition -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| No embedded handoff in resolved context | — | External calls remain in the main dossier |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
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
| `ep1\openworld\sandbox_activities\ep1_airdrop_activities.gamedef` | content candidate | ep1\openworld\sandbox_activities\ep1_airdrop_activities.quest |
| `ep1\openworld\sandbox_activities\ep1_sandbox_activities.gamedef` | content candidate | ep1\openworld\sandbox_activities\ep1_sandbox_activities.quest |
| `ep1\quest\ep1.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01_testworld.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |
| `ep1\openworld\street_stories\sts_ep1_07\sts_ep1_07_nc_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_07\sts_ep1_07.quest |
| `ep1\openworld\street_stories\sts_ep1_07\sts_ep1_07_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_07\sts_ep1_07.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_nc_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10_def.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |
| `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.gamedef` | content candidate | ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `ep1\openworld\community\boulevard_av\boulevard_av.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\boulevard_av\boulevard_av_combat.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\container_zone\container_zone.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\container_zone\container_zone_combat.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\ep1_combat_community.questphase` | phase flow | No match in inspected vanilla indexes; index evidence only |
| `ep1\openworld\community\ep1_quest_community.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\ep1_world_community.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\high_peak\high_peak.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\high_peak\high_peak_combat.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\high_peak\phases\hill_park_hill_park_spa_scrappers.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\monument_av\monument_av.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\monument_av\monument_av_combat.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\ferronia_downes.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\golden_pacific.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\heavy_hearts.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\longshore_stacks_market.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\mq306_boxing_ring.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\q301_crashsite_way_up.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\q301_stadium_entry.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\q302_basketball_court.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\q303_nighthawks.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\q305_songbird_metro_chase_crowd.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\quest_communities\stadium.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\stadium\stadium.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\stadium\stadium_combat.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\terra_cognita\terra_cognita.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\terra_cognita\terra_cognita_combat.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\openworld\community\terra_cognita\terra_cognita_combat_scrappers.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\main_quests\q301\phases\q301_way_to_crashsite_toggle_ow.questphase` | phase flow | No match in inspected vanilla indexes; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `ep1_standalone` | ep1\quest\ep1_standalone.quest / h0 / 5; 1 total source locations in compressed evidence |

NodeRef uses: 47; TweakDB binding uses: 5. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
