# Money For Nothing

Journal: `ep1/quests/minor_quest/sts_ep1_08_loot_pickup` · `MinorQuest` · hash `1379134557`.

**Coverage: journal-linked.** 11 exact journal-linked nodes in 3 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Go to Katya's stash. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` |
| Find Katya's stash. (Primary) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_ep1_08_bugfixing.questphase / h106 / 4` (Condition) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/description` | 3:Out → 4:In; 4:True → 5:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 5` (Condition) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` | 4:True → 5:In; 5:True → 6:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 6` (Condition) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates` | 5:True → 6:In; 6:True → 9:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 7` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` | 9:Out → 7:Active; 7:Out → 11:In |
| `sts_ep1_08_target_meeting.scene / scene / 1397` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` | 1397:0:0 → 1537:0:1; 1533:0:0 → 1397:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sts_ep1_08_target_meeting.scene / scene / 1537` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/description` | 1397:0:0 → 1537:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `wst_ep1_21.questphase / h0 / 27` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash` | 41:Out → 27:Succeeded; 27:Out → 28:Active |
| `wst_ep1_21.questphase / h0 / 28` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates` | 27:Out → 28:Active; 28:Out → 39:In |
| `wst_ep1_21.questphase / h0 / 29` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates` | 4:Out → 29:Succeeded; 29:Out → 31:Succeeded |
| `wst_ep1_21.questphase / h0 / 30` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup` | 30:Out → 22:In; 31:Out → 30:Succeeded |
| `wst_ep1_21.questphase / h0 / 31` (Journal) | `ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash` | 29:Out → 31:Succeeded; 31:Out → 30:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h33 / 9 | `sts_ep1_08_bugfixing.questphase` | 0: Input; 0:Out → 9:In1 |
| `ep1\openworld\street_stories\ep1_street_stories.questphase` / h558 / 7 | `sts_ep1_08_bugfixing.questphase` | 0: Input; 0:Out → 7:In1 |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase` / h0 / 67 | `sts_ep1_08_target_meeting.scene` | 153: PauseCondition: {"seconds": 2}; 153:Out → 67:Bana intro; 67:phone end 01 → 380:In |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase` / h0 / 201 | `sts_ep1_08_target_meeting.scene` | 206: Input; 474: LogicalHub; 340: LogicalHub; 206:Out → 201:Meeting; 474:Out1 → 201:Meeting; 340:Out1 → 201:katya dead comment; 201:dead → 402:In1; 201:friendly → 402:In1; 201:katya killed before order → 340:In1; 201:katya killed before order → 402:In1 |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase` / h0 / 283 | `sts_ep1_08_target_meeting.scene` | 419: Condition; 283:eliminate enemies end → 232:Inactive; 419:False → 283:eliminate enemies |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_phase.questphase` / h0 / 285 | `sts_ep1_08_target_meeting.scene` | 366: PauseCondition: {"seconds": 2}; 285:meeting_point → 255:In; 366:Out → 285:enemies defeated; 285:meeting_point → 453:In |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 21 | `wst_ep1_21.questphase` | 40: PauseCondition: wst_ep1_21_active; 40:Out → 21:In1 |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 3 | `ep1_openworld_bugfixing.questphase` | 0: Input; 0:Out → 3:In1 |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 2 | `ep1_street_stories.questphase` | 33: PauseCondition: ep1_side_content GreaterOrEqual 1; 33:Out → 2:In1 |
| `ep1\openworld\street_stories\ep1_street_stories.questphase` / h13 / 23 | `sts_ep1_08_phase.questphase` | 17: Journal; 17:Out → 23:Start; 23:Organitopia done → 36:In; 23:Out1 → 31:In |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 14 | `ep1_world_stories.questphase` | 11: LogicalHub; 11:Out1 → 14:In1 |
| `ep1\quest\ep1.questphase` / h58 / 2 | `ep1_bugfixing.questphase` | 25: LogicalXor; 2:CP77-65722_out → 27:In; 2:CP77-64292_out → 26:In; 25:Out1 → 2:In1; 2:Out1 → 4:In2; 2:growl → 4:growl |
| `ep1\openworld\vendors\vehicle_metaquest\phases\vehicle_metaquest_ep1_bugfixing.questphase` / h17 / 6 | `ep1_open_world.questphase` | 4: Condition: militech_hellhound_available; 4:False → 6:CP77-63752 |
| `ep1\quest\ep1.questphase` / h58 / 5 | `ep1_open_world.questphase` | 0: Input; 9: CutControl; 0:Out → 5:In1; 9:CutSource → 5:CutDestination |
| `ep1\openworld\bugfixing\ep1_openworld_bugfixing.questphase` / h0 / 16 | `vehicle_metaquest_ep1_bugfixing.questphase` | 0: Input; 0:Out → 16:In1 |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sts_ep1_08_target_meeting.scene` | Bana intro, fake input to keep lines alive, Start 11, Meeting, eliminate enemies, katya dead comment, enemies defeated → dead, meeting_point, friendly, phone end 01, eliminate enemies end, End 12,  enemies defeated end, katya killed before order | target; bana_voice; Ana; bana_impersonated; Player; 248 nodes / 274 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_ep1_08_target_meeting.scene / n997 / 0` | Bana? You alive? (`alive`) | No option-level predicate stored | 0:0 → 1000:0:0 |
| `sts_ep1_08_target_meeting.scene / n997 / 1` | How'd you connect to me? (`how`) | No option-level predicate stored | 0:1 → 1004:0:0 |
| `sts_ep1_08_target_meeting.scene / n1016 / 0` | How the hell'd you get here? (`what_are_you_doin`) | No option-level predicate stored | 0:0 → 1018:0:0 |
| `sts_ep1_08_target_meeting.scene / n1016 / 1` | Why use Bana's voice? (`voice`) | No option-level predicate stored | 0:1 → 1020:0:0 |
| `sts_ep1_08_target_meeting.scene / n1025 / 0` | Where's Bana? (`bana`) | No option-level predicate stored | 0:0 → 1027:0:0 |
| `sts_ep1_08_target_meeting.scene / n1025 / 1` | How'd you get the biomonitor? (`biomonitor`) | No option-level predicate stored | 0:1 → 1031:0:0 |
| `sts_ep1_08_target_meeting.scene / n1049 / 0` | How you know he's dead? (`How do you know`) | No option-level predicate stored | 0:0 → 1051:0:0 |
| `sts_ep1_08_target_meeting.scene / n1049 / 1` | You killed him? (`Did you kill him`) | No option-level predicate stored | 0:1 → 1053:0:0 |
| `sts_ep1_08_target_meeting.scene / n1062 / 0` | Better worry about me, not SovOil. (`me`) | No option-level predicate stored | 0:0 → 1064:0:0 |
| `sts_ep1_08_target_meeting.scene / n1062 / 1` | You interrogated Bana. (`interrogate`) | No option-level predicate stored | 0:1 → 1066:0:0 |
| `sts_ep1_08_target_meeting.scene / n1075 / 0` | Said I gotta kill ya. (`tell truth`) | No option-level predicate stored | 0:0 → 1081:0:0 |
| `sts_ep1_08_target_meeting.scene / n1075 / 1` | Don't think they buy it. (`try to trick `) | No option-level predicate stored | 0:1 → 1083:0:0 |
| `sts_ep1_08_target_meeting.scene / n1085 / 0` | Make it quick. (`accept`) | No option-level predicate stored | 0:0 → 1087:0:0 |
| `sts_ep1_08_target_meeting.scene / n1085 / 1` | Too bad. Got a "job" to do too. (`deny`) | No option-level predicate stored | 0:1 → 1111:0:0; 0:1 → 2115:0:1 |
| `sts_ep1_08_target_meeting.scene / n1107 / 0` | Fine. Deal. (`deal`) | No option-level predicate stored | 0:0 → 2321:0:0 |
| `sts_ep1_08_target_meeting.scene / n1107 / 1` | Unfortunately, I do care. (`kill`) | No option-level predicate stored | 0:1 → 1185:0:0 |
| `sts_ep1_08_target_meeting.scene / n2224 / 0` | [Take biomonitor] We have a deal. (`Take biomonitor - deal`) | No option-level predicate stored | 0:0 → 2244:0:0; 0:0 → 2273:0:1 |
| `sts_ep1_08_target_meeting.scene / n2302 / 0` | Text join unresolved (`Option`) | No option-level predicate stored | 0:0 → 1183:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CP77-60274` | sts_ep1_08_bugfixing.questphase / h15 / 26 | No reader in selected context |
| `CP77-63629` | sts_ep1_08_bugfixing.questphase / h106 / 3 | sts_ep1_08_bugfixing.questphase / h106 / 2 |
| `audio_mark_bana_calls_v_end_activate` | sts_ep1_08_target_meeting.scene / scene / 1580; sts_ep1_08_target_meeting.scene / scene / 1774; sts_ep1_08_target_meeting.scene / scene / 2413 | No reader in selected context |
| `audio_mark_bana_calls_v_start_activate` | sts_ep1_08_target_meeting.scene / scene / 1554; sts_ep1_08_target_meeting.scene / scene / 1788; sts_ep1_08_target_meeting.scene / scene / 2394; sts_ep1_08_target_meeting.scene / scene / 2428 | No reader in selected context |
| `audio_mark_bana_reveal` | sts_ep1_08_target_meeting.scene / scene / 1556; sts_ep1_08_target_meeting.scene / scene / 1582; sts_ep1_08_target_meeting.scene / scene / 1776; sts_ep1_08_target_meeting.scene / scene / 1790; sts_ep1_08_target_meeting.scene / scene / 2396; sts_ep1_08_target_meeting.scene / scene / 2415; sts_ep1_08_target_meeting.scene / scene / 2430 | sts_ep1_08_target_meeting.scene / scene / 2387 |
| `codex_katya_karielin` | sts_ep1_08_target_meeting.scene / scene / 1453 | No reader in selected context |
| `codex_sov_oil` | sts_ep1_08_target_meeting.scene / scene / 1843 | No reader in selected context |
| `holo_janet_calls_v_end_activate` | sts_ep1_08_target_meeting.scene / scene / 1606; sts_ep1_08_target_meeting.scene / scene / 1677 | No reader in selected context |
| `holo_janet_calls_v_end_done` | sts_ep1_08_target_meeting.scene / scene / 1602; sts_ep1_08_target_meeting.scene / scene / 1673 | sts_ep1_08_target_meeting.scene / scene / 1600; sts_ep1_08_target_meeting.scene / scene / 1671 |
| `holo_janet_calls_v_start_activate` | sts_ep1_08_target_meeting.scene / scene / 1594 | No reader in selected context |
| `holo_janet_calls_v_start_done` | Producer outside selected context | sts_ep1_08_target_meeting.scene / scene / 1598 |
| `holo_janet_reveal` | sts_ep1_08_target_meeting.scene / scene / 1596; sts_ep1_08_target_meeting.scene / scene / 1608; sts_ep1_08_target_meeting.scene / scene / 1679 | No reader in selected context |
| `holo_jant_calls_v_start_done` | sts_ep1_08_target_meeting.scene / scene / 1590 | No reader in selected context |
| `holo_mark_bana_calls_v_end_done` | sts_ep1_08_target_meeting.scene / scene / 1576; sts_ep1_08_target_meeting.scene / scene / 1770; sts_ep1_08_target_meeting.scene / scene / 2411 | sts_ep1_08_target_meeting.scene / scene / 1574; sts_ep1_08_target_meeting.scene / scene / 1768; sts_ep1_08_target_meeting.scene / scene / 2409 |
| `holo_mark_bana_calls_v_start_done` | sts_ep1_08_target_meeting.scene / scene / 1550; sts_ep1_08_target_meeting.scene / scene / 1784; sts_ep1_08_target_meeting.scene / scene / 2390; sts_ep1_08_target_meeting.scene / scene / 2426 | sts_ep1_08_target_meeting.scene / scene / 1560; sts_ep1_08_target_meeting.scene / scene / 1792; sts_ep1_08_target_meeting.scene / scene / 2398; sts_ep1_08_target_meeting.scene / scene / 2432 |
| `sts_ep1_08_active` | Producer outside selected context | sts_ep1_08_bugfixing.questphase / h15 / 19 |
| `sts_ep1_08_ana_gave_kill_order` | sts_ep1_08_target_meeting.scene / scene / 1421 | sts_ep1_08_target_meeting.scene / scene / 1418 |
| `sts_ep1_08_biomonitor_moved_to_loot_box` | sts_ep1_08_target_meeting.scene / scene / 2353; sts_ep1_08_target_meeting.scene / scene / 2355 | sts_ep1_08_target_meeting.scene / scene / 2344 |
| `sts_ep1_08_boss_appears` | Producer outside selected context | sts_ep1_08_bugfixing.questphase / h15 / 13 |
| `sts_ep1_08_boss_holograms_clean_up` | Producer outside selected context | sts_ep1_08_bugfixing.questphase / h15 / 23 |
| `sts_ep1_08_info_about_biomonitor_in_loot_box` | sts_ep1_08_target_meeting.scene / scene / 2335 | sts_ep1_08_target_meeting.scene / scene / 2344 |
| `sts_ep1_08_save_katya_corpo_blueline` | sts_ep1_08_target_meeting.scene / scene / 1540 | No reader in selected context |
| `sts_ep1_08_save_katya_nomad_blueline` | sts_ep1_08_target_meeting.scene / scene / 1541 | No reader in selected context |
| `sts_ep1_08_show_bana_avatar` | sts_ep1_08_target_meeting.scene / scene / 2440; sts_ep1_08_target_meeting.scene / scene / 2443 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | sts_ep1_08_bugfixing.questphase / h0 / 23; wst_ep1_21.questphase / h0 / 43 |
| `wst_ep1_21_active` | sts_ep1_08_bugfixing.questphase / h106 / 9; sts_ep1_08_target_meeting.scene / scene / 1533 | No reader in selected context |
| `wst_ep1_21_done` | wst_ep1_21.questphase / h0 / 22 | No reader in selected context |
| `wst_ep1_21_finished` | wst_ep1_21.questphase / h0 / 35 | No reader in selected context |
| `wst_ep1_21_start` | wst_ep1_21.questphase / h0 / 21 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>53 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_ep1_08_bugfixing.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":999}}}` | 24:Out → 23:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","inverted":true}}}` | 12:Out → 9:In; 13:Out → 9:In; 9:Out → 10:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType"}}}` | 10:Out → 11:In; 11:Out → 12:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 12:Out → 9:In; 11:Out → 12:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_boss_appears","value":1,"comparisonType":"GreaterOrEqual"}}}` | 13:Out → 9:In; 19:True → 13:In; 13:Out → 23:In |
| `sts_ep1_08_bugfixing.questphase / h15 / 19` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 19:True → 13:In; 26:Out → 19:In; 19:False → 25:In1 |
| `sts_ep1_08_bugfixing.questphase / h15 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_boss_holograms_clean_up","value":1,"comparisonType":"GreaterOrEqual"}}}` | 23:Out → 1:In; 13:Out → 23:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-63629"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/sts_ep1_08_loot_pickup/description","fileEntryIndex":2,"className":"gameJournalQuestDescription"},"state":"Active"}}}` | 3:Out → 4:In; 4:True → 5:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/find_stash","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Inactive"}}}` | 4:True → 5:In; 5:True → 6:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/sts_ep1_08_loot_pickup/hidden_stash/go_to_coordinates","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Inactive"}}}` | 5:True → 6:In; 6:True → 9:In |
| `sts_ep1_08_bugfixing.questphase / h106 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_21_search_trigger"}}` | 7:Out → 11:In; 11:True → 12:In |
| `sts_ep1_08_target_meeting.scene / scene / 130` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sts_ep1_08_target_meeting_trigger"}}` | 130:0:0 → 360:0:3; 130:0:0 → 811:0:1; 1299:0:0 → 130:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 206` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 204:0:0 → 206:0:1; 206:0:0 → 197:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 547` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 545:0:0 → 547:0:1; 547:0:0 → 543:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 560` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sts_ep1_08_directors_office_trigger"}}` | 560:0:0 → 680:0:1; 560:0:0 → 1204:0:0; 560:0:0 → 1762:0:1; 560:0:0 → 2147:0:1; 595:0:0 → 560:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 572` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 348:0:0 → 572:0:1; 572:0:0 → 2428:0:1; 572:0:0 → 2453:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 680` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_ep1_08_target_spawnset","names":["target"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 560:0:0 → 680:0:1; 680:0:0 → 2448:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 685` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/sts_ep1_08/target_meeting/kill_katya","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 685:0:0 → 682:0:3; 685:0:1 → 691:0:1; 723:0:0 → 685:0:1; 1934:0:0 → 685:0:1; 2157:0:0 → 685:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 691` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/sts_ep1_08/target_meeting/05c_talk_with_target","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 682:0:0 → 691:0:1; 685:0:1 → 691:0:1; 691:0:0 → 689:0:4; 691:0:1 → 1313:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 723` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/sts_ep1_08/target_meeting/07_pick_up_the_target","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 723:0:0 → 685:0:1; 723:0:1 → 720:0:1; 2157:0:1 → 723:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 811` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sts_ep1_08_target_meeting_door_close_trigger"}}` | 130:0:0 → 811:0:1; 811:0:0 → 809:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1199` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","minutes":1}}}` | 595:0:0 → 1199:0:1; 1199:0:0 → 1198:0:0; 1204:1:0 → 1199:0:0 |
| `sts_ep1_08_target_meeting.scene / scene / 1313` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/sts_ep1_08/target_meeting/talk_with_katya","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 689:0:0 → 1313:0:1; 691:0:1 → 1313:0:1; 1313:0:0 → 1311:0:4; 1313:0:1 → 1488:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1418` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_ana_gave_kill_order","value":1,"comparisonType":"Equal"}}}` | 1418:0:0 → 24:0:0; 1418:0:1 → 1416:0:0; 2338:0:0 → 1418:0:1; 2344:0:1 → 1418:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1436` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/sts_ep1_08/target_meeting/05a_confront","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 826:0:0 → 1436:0:1; 1436:0:0 → 1434:0:2; 1436:0:1 → 1445:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1445` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/sts_ep1_08/target_meeting/05aa_secret_room","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 1434:0:0 → 1445:0:1; 1436:0:1 → 1445:0:1; 1445:0:0 → 1438:0:2; 1445:0:1 → 2157:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1459` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_ep1_08_door_to_the_target_interior"},"eventType":"Finished"}}}` | 1456:0:0 → 1459:0:1; 1459:0:0 → 1462:0:0 |
| `sts_ep1_08_target_meeting.scene / scene / 1460` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_ep1_08_directors_office_trigger"},"timeInterval":2.0,"angleTolerance":20.0}},{"$type":"questTriggerCondition","triggerAreaRef":"#sts_ep1_07_swimming_pool"}]}}` | 1456:0:0 → 1460:0:1; 1460:0:0 → 1462:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1461` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#sts_ep1_08_door_to_the_target_interior"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"Less"}}}` | 1456:0:0 → 1461:0:1; 1461:0:0 → 1462:0:2 |
| `sts_ep1_08_target_meeting.scene / scene / 1488` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/sts_ep1_08/target_meeting/talk_with_katya1","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 1311:0:0 → 1488:0:1; 1313:0:1 → 1488:0:1; 1488:0:0 → 1486:0:4; 1488:0:1 → 2344:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1560` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_mark_bana_calls_v_start_done"}}}` | 1554:0:0 → 1560:0:1; 1560:0:0 → 1550:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1574` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_mark_bana_calls_v_end_done"}}}` | 1574:0:0 → 1576:0:1; 1580:0:0 → 1574:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1598` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_janet_calls_v_start_done"}}}` | 1594:0:0 → 1598:0:1; 1598:0:0 → 1590:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1600` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_janet_calls_v_end_done"}}}` | 1600:0:0 → 1602:0:1; 1606:0:0 → 1600:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1671` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_janet_calls_v_end_done"}}}` | 1671:0:0 → 1673:0:1; 1677:0:0 → 1671:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1768` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_mark_bana_calls_v_end_done"}}}` | 1768:0:0 → 1770:0:1; 1774:0:0 → 1768:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 1792` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_mark_bana_calls_v_start_done"}}}` | 1788:0:0 → 1792:0:1; 1792:0:0 → 1784:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 2147` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#sts_ep1_08_target_spawnset","names":["target"]}}}}` | 560:0:0 → 2147:0:1; 2147:0:0 → 2151:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 2157` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/street_stories/sts_ep1_08/target_meeting/07_pick_up_the_target","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 1438:0:0 → 2157:0:1; 1445:0:1 → 2157:0:1; 2157:0:0 → 685:0:1; 2157:0:1 → 723:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 2234` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 1115:0:0 → 2234:0:1; 2234:0:0 → 2238:0:0 |
| `sts_ep1_08_target_meeting.scene / scene / 2344` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_biomonitor_moved_to_loot_box","comparisonType":"Equal"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_ep1_08_info_about_biomonitor_in_loot_box"}}]}}` | 1486:0:0 → 2344:0:1; 1488:0:1 → 2344:0:1; 2344:0:0 → 2340:0:1; 2344:0:1 → 1418:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 2367` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sts_ep1_08_directors_office_trigger"}}` | 2363:0:0 → 2367:0:1; 2367:0:0 → 2362:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 2387` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"audio_mark_bana_reveal"}}}` | 923:0:0 → 2387:0:1; 2387:0:0 → 926:0:0; 2387:0:1 → 2394:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 2398` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_mark_bana_calls_v_start_done"}}}` | 2394:0:0 → 2398:0:1; 2398:0:0 → 2390:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 2409` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_mark_bana_calls_v_end_done"}}}` | 2409:0:0 → 2411:0:1; 2413:0:0 → 2409:0:1 |
| `sts_ep1_08_target_meeting.scene / scene / 2432` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_mark_bana_calls_v_start_done"}}}` | 2428:0:0 → 2432:0:1; 2432:0:0 → 2426:0:1 |
| `wst_ep1_21.questphase / h0 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#wst_ep1_21_katya_loot","eventType":"Executed"}}}` | 51:Out → 4:In; 4:Out → 29:Succeeded |
| `wst_ep1_21.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#wst_ep1_21_com","names":["vehicle"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0}}}}` | 35:Out → 18:In; 18:Out → 25:In |
| `wst_ep1_21.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wst_ep1_21_search_trigger"}}` | 23:Out → 21:In; 24:Out → 23:In |
| `wst_ep1_21.questphase / h0 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/container_zone_prefab4PZIADQ/container_zone_world_stories_prefab4SY6XVQ/wst_ep1_21_prefabQRZL7KY/wst_ep1_21_gameplay_prefabXEJQVRA/wst_ep1_21_devices_prefabWTHKHJY/movable_dumpster_prefab66MQPEQ/movable_device_rack_prefabBQFFUUY"},"eventType":"Finished"}}}` | 24:Out → 36:In; 36:Out → 37:In |
| `wst_ep1_21.questphase / h0 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"$/03_night_city/c_pacifica/combat_zone_prefabUEX7DCY/container_zone_prefab4PZIADQ/container_zone_world_stories_prefab4SY6XVQ/wst_ep1_21_prefabQRZL7KY/wst_ep1_21_gameplay_prefabXEJQVRA/wst_ep1_21_devices_prefabWTHKHJY/movable_dumpster_prefab66MQPEQ/movable_device_rack_prefabBQFFUUY","eventType":"Executed"}}}` | 28:Out → 39:In; 39:Out → 42:In |
| `wst_ep1_21.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":999}}}` | 0:Out → 43:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_route` | sts_ep1_08_target_meeting.scene / scene / 2081 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `call_lifecycle` | sts_ep1_08_target_meeting.scene / scene / 1644; sts_ep1_08_target_meeting.scene / scene / 1647; sts_ep1_08_target_meeting.scene / scene / 1650; sts_ep1_08_target_meeting.scene / scene / 1759; +4 locations in catalogue.json | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `choice_gate` | sts_ep1_08_target_meeting.scene / scene / 1016; sts_ep1_08_target_meeting.scene / scene / 1025; sts_ep1_08_target_meeting.scene / scene / 1049; sts_ep1_08_target_meeting.scene / scene / 1062; +6 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | sts_ep1_08_bugfixing.questphase / h0 / 23; sts_ep1_08_bugfixing.questphase / h106 / 2; sts_ep1_08_bugfixing.questphase / h15 / 13; sts_ep1_08_bugfixing.questphase / h15 / 19; +15 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `device_action` | sts_ep1_08_target_meeting.scene / scene / 197; sts_ep1_08_target_meeting.scene / scene / 204; sts_ep1_08_target_meeting.scene / scene / 2362; sts_ep1_08_target_meeting.scene / scene / 2363; +11 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `persistent_decision` | sts_ep1_08_bugfixing.questphase / h106 / 3; sts_ep1_08_bugfixing.questphase / h106 / 9; sts_ep1_08_bugfixing.questphase / h15 / 26; sts_ep1_08_target_meeting.scene / scene / 1421; +43 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sts_ep1_08_bugfixing.questphase / h15 / 12; sts_ep1_08_target_meeting.scene / scene / 1199; sts_ep1_08_target_meeting.scene / scene / 206; sts_ep1_08_target_meeting.scene / scene / 2234; +2 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `scan_evidence` | sts_ep1_08_target_meeting.scene / scene / 1459; wst_ep1_21.questphase / h0 / 36 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `target_resolution` | sts_ep1_08_target_meeting.scene / scene / 680 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | sts_ep1_08_target_meeting.scene / scene / 1374; sts_ep1_08_target_meeting.scene / scene / 1869; sts_ep1_08_target_meeting.scene / scene / 2036; sts_ep1_08_target_meeting.scene / scene / 2060; +8 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_ep1_08_target_meeting.scene / scene / 2453; sts_ep1_08_target_meeting.scene / scene / 2456; sts_ep1_08_target_meeting.scene / scene / 788; sts_ep1_08_target_meeting.scene / scene / 988; +4 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\street_stories\sts_ep1_08\phases\sts_ep1_08_bugfixing.questphase` | repair; journal anchor | `ep1-sts-ep1-08` |
| `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_target_meeting.scene` | content candidate; journal anchor | `ep1-sts-ep1-08` |
| `ep1\openworld\world_stories\wst_ep1_21\wst_ep1_21.questphase` | content candidate; journal anchor | `ep1-wst-ep1-21` |

Evidence shards for this dossier (including parent context): [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-sts-ep1-08.json.gz), [ep1-wst-ep1-21](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-wst-ep1-21.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
