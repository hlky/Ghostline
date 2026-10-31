# From Her to Eternity

Journal: `ep1/quests/main_quest/q306_postcontent` · `MainQuest` · hash `922330340`.

Journal premise: Wonder how Songbird's doin'. Maybe we ougha raised a toast to her too? Never really understood why people love to gawk at the moon with those vacant, dreamy expressions. But now... might have to give it a try myself. Meanwhile, you keep your nose to the ground so you don't step in any shit.

**Coverage: journal-linked.** 15 exact journal-linked nodes in 2 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Decrypt Songbird's shard. (Optional) | `ep1/quests/main_quest/q306_postcontent/00_common/00_decrypt_shard` |
| Read the message from the unknown sender. (Primary) | `ep1/quests/main_quest/q306_postcontent/00_common/000_read_message` |
| Search the area around the provided coordinates. (Primary) | `ep1/quests/main_quest/q306_postcontent/00_common/00_find_cache` |
| Collect the contents of the container. (Primary) | `ep1/quests/main_quest/q306_postcontent/00_common/00_loot_cache` |
| Play Songbird's message on your computer. (Primary) | `ep1/quests/main_quest/q306_postcontent/00_common/01_listen_to_recording` |
| Distribute So Mi's mementos around your apartment. (Primary) | `ep1/quests/main_quest/q306_postcontent/00_common/02_place_mementos` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `q115_00_hanako.questphase / h1024 / 167` (Journal) | `ep1/quests/main_quest/q306_postcontent` | 184:Out → 167:Failed; 167:Out → 185:In |
| `q306_06_postcontent_cache.questphase / h0 / 9` (Journal) | `ep1/quests/main_quest/q306_postcontent/00_common/00_find_cache` | 39:Out → 9:Active |
| `q306_06_postcontent_cache.questphase / h0 / 14` (Journal) | `ep1/quests/main_quest/q306_postcontent/00_common/00_find_cache` | 68:True → 14:Succeeded; 14:Out → 98:In |
| `q306_06_postcontent_cache.questphase / h0 / 38` (Journal) | `ep1/quests/main_quest/q306_postcontent/00_common/000_read_message` | 2:Out → 38:Active; 38:Out → 101:In |
| `q306_06_postcontent_cache.questphase / h0 / 39` (Journal) | `ep1/quests/main_quest/q306_postcontent/00_common/000_read_message` | 39:Out → 9:Active; 20:Out → 39:Succeeded |
| `q306_06_postcontent_cache.questphase / h0 / 48` (Journal) | `ep1/quests/main_quest/q306_postcontent/00_common/000_read_message` | 66:True → 48:Succeeded; 48:Out → 68:In |
| `q306_06_postcontent_cache.questphase / h0 / 52` (Journal) | `ep1/quests/main_quest/q306_postcontent` | 52:Out → 32:In; 65:Out → 52:Succeeded |
| `q306_06_postcontent_cache.questphase / h0 / 62` (Journal) | `ep1/quests/main_quest/q306_postcontent/00_common/00_find_cache` | 85:Out1 → 62:Succeeded; 62:Out → 84:Active |
| `q306_06_postcontent_cache.questphase / h0 / 65` (Journal) | `ep1/quests/main_quest/q306_postcontent/00_common/00_loot_cache` | 30:Out1 → 65:Succeeded; 65:Out → 52:Succeeded |
| `q306_06_postcontent_cache.questphase / h0 / 66` (Condition) | `ep1/quests/main_quest/q306_postcontent/00_common/000_read_message` | 66:True → 48:Succeeded; 55:Out → 66:In; 66:False → 68:In |
| `q306_06_postcontent_cache.questphase / h0 / 68` (Condition) | `ep1/quests/main_quest/q306_postcontent/00_common/00_find_cache` | 68:True → 14:Succeeded; 48:Out → 68:In; 66:False → 68:In; 68:False → 98:In |
| `q306_06_postcontent_cache.questphase / h0 / 70` (Journal) | `ep1/quests/main_quest/q306_postcontent/00_common/00_loot_cache` | 98:True → 70:Active |
| `q306_06_postcontent_cache.questphase / h0 / 84` (Journal) | `ep1/quests/main_quest/q306_postcontent/00_common/00_loot_cache` | 62:Out → 84:Active |
| `q306_06_postcontent_cache.questphase / h0 / 98` (Condition) | `ep1/quests/main_quest/q306_postcontent/00_common/00_find_cache` | 14:Out → 98:In; 68:False → 98:In; 98:True → 70:Active |
| `q306_06_postcontent_cache.questphase / h0 / 100` (Journal) | `ep1/quests/main_quest/q306_postcontent/description` | 100:Out → 20:In; 101:Out → 100:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `q306_06_postcontent_cache.questphase / h0 / 49` | `ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene`; `#q306_sm_songbird_recording` | 78:Out → 49:Start 0; 49:End 0 → 57:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\main_quests\part1\q115\q115_afterlife.questphase` / h0 / 69 | `q115_00_hanako.questphase` | 62: Phase; 89: Input; 72: Input; 62:Out1 → 69:In1; 69:Out1 → 70:In1; 89:Out → 69:In2; 72:Out → 69:In3 |
| `ep1\quest\main_quests\q306\phases\external\q306_persistent.questphase` / h0 / 17 | `q306_06_postcontent_cache.questphase` | 19: Condition: q306_somi_betrayed; 17:Out1 → 16:Mementos_In; 19:False → 17:In1 |
| `ep1\quest\main_quests\q306\phases\external\q306_persistent.questphase` / h943 / 3 | `q306_songbird_recording.scene` | 10: PauseCondition: #q306_tr_post_content_alley; 10:Out → 3:Start 0; 3:End 0 → 5:In |
| `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 49 | `q306_songbird_recording.scene` | 78: GameManager; 78:Out → 49:Start 0; 49:End 0 → 57:In |
| `base\quest\main_quests\part1\act_1.questphase` / h329 / 4 | `q115_afterlife.questphase` | 0: Input; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 0:Out → 4:In; 4:Out1 → 1:In; 9:Out1 → 4:In; 9:OutRestaurant → 4:InRestaurant; 9:OutElevator → 4:InElevator; 9:OutRipperdoc → 4:InRipperdoc; 4:q114_out → 5:In; 9:OutPills → 4:InPills; 4:q113_out → 6:In; 9:OutRipperRoof → 4:InRipperdocRoof; 4:death_out → 7:In; 9:OutQ114 → 4:InQ114; 4:mikoshi_out → 8:In; 9:OutQ113 → 4:InQ113; 9:OutSolo → 4:InSolo; 9:OutAfterlife → 4:InAfterlife; 9:OutAfterRogue → 4:InAfterSex; 9:OutBeforeAlt → 4:InBeforeAlt; 9:OutAfterAlt → 4:InAfterlifePlan; 9:OutAV → 4:InAfterlifeAV; 9:OutJungle → 4:InJungle; 9:OutAtrium → 4:InAtrium; 9:OutNetrunner → 4:InNetrunner |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 5 | `q115_afterlife.questphase` | 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91:Out1 → 5:In; 5:Out1 → 73:In1; 91:OutRestaurant → 5:InRestaurant; 91:OutElevator → 5:InElevator; 91:OutRipperdoc → 5:InRipperdoc; 5:q114_out → 92:In1; 91:OutPills → 5:InPills; 5:q113_out → 115:In1; 91:OutRipperRoof → 5:InRipperdocRoof; 5:death_out → 116:In1; 91:OutQ114 → 5:InQ114; 5:mikoshi_out → 73:cyberspace_in; 91:OutQ113 → 5:InQ113; 91:OutSolo → 5:InSolo; 91:OutAfterlife → 5:InAfterlife; 91:OutAfterRogue → 5:InAfterSex; 91:OutBeforeAlt → 5:InBeforeAlt; 91:OutAfterAlt → 5:InAfterlifePlan; 91:OutAV → 5:InAfterlifeAV; 91:OutJungle → 5:InJungle; 91:OutAtrium → 5:InAtrium; 91:OutNetrunner → 5:InNetrunner |
| `ep1\quest\ep1_persistent_content.questphase` / h388 / 2 | `q306_persistent.questphase` | 22: LogicalHub; 22:Out1 → 2:In1 |
| `ep1\quest\main_quests\q306\q306.questphase` / h0 / 112 | `q306_persistent.questphase` | 116: LogicalHub; 115: LogicalHub; 116:Out1 → 112:In1; 115:Out1 → 112:DebugReed_In |
| `base\quest\cyberpunk2077.questphase` / h0 / 33 | `act_1.questphase` | 32: Phase: prologue.questphase; 82: Phase; 57: Phase; 57: Phase; 57: Phase; 98: Condition: ep1_active Less 1; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 102: PauseCondition: ep1_active GreaterOrEqual 1; 32:Out1 → 33:Q101; 82:CYB-656199_Out → 33:CYB-656199_In; 33:Q201 → 36:Q201; 33:Q202 → 36:Q202; 57:Q101 Out → 33:Q101; 33:Q203 → 36:Q203; 57:Q101 Vroom Out → 33:Q101 Vroom; 33:Q204 → 36:Q204; 57:Q103 Out → 33:Q103; 98:True → 33:Q103; 33:Q115 Final Boards → 91:In1; 57:Q104 Out → 33:Q104; 57:Q105 Out → 33:Q105; 57:Q108 Out → 33:Q108; 57:Q110 Out → 33:Q110; 57:Q112 Out → 33:Q112; 57:Q113 Out → 33:Q113; 57:Q114 Out → 33:Q114; 57:Q115 Out → 33:Q115; 57:Q116 Out → 33:Q116; 57:EP1_Standalone → 33:EP1_Standalone; 102:Out → 33:EP1_Standalone |
| `ep1\quest\ep1_additional_game_elements.questphase` / h0 / 2 | `ep1_persistent_content.questphase` | 0: Input; 15: Input; 0:Out → 2:In1; 15:Out → 2:growl |
| `ep1\quest\main_quests\ep1_main_quests.questphase` / h0 / 7 | `q306.questphase` | 18: Condition: q304_songbirds_path Less 1; 25: Input; 7:Point_of_no_return_out → 43:In1; 7:quest_end → 43:In2; 18:False → 7:00_start; 25:Out → 7:00_start |
| `ep1\quest\main_quests\q306\q306.quest` / h0 / 2 | `q306.questphase` | 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 3: Phase: q306_00_chickentest.questphase; 2:quest_end → 1:In; 3:Meeting → 2:00_start; 3:Song → 2:Song; 3:Mid-ride → 2:Mid-ride; 3:Cosmodrome → 2:Cosmodrome; 3:Gate Passed → 2:Gate Passed; 3:Failstate → 2:Failstate; 3:Restricted → 2:Restricted; 3:Roof → 2:Roof; 3:Myers Arrival → 2:Myers Arrival; 3:Public Revisited → 2:Public Revisited; 3:Restricted Revisited → 2:Restricted Revisited; 3:Duty Free → 2:Duty Free; 3:Viewing Gallery → 2:Viewing Gallery; 3:Station Approach → 2:Station Approach; 3:Tower Defense → 2:Tower Defense; 3:Overdrive Scene → 2:Overdrive Scene; 3:Overdrive Gameplay → 2:Overdrive Gameplay; 3:Train → 2:Train; 3:Launchpad → 2:Launchpad; 3:REED dead, SOMI on moon → 2:REED dead, SOMI on moon; 3:REED takes SOMI → 2:REED leaves, SOMI returned; 3:CreditsTest_Out → 2:CreditsTest_In; 3:Reed Epilogue Postcontent → 2:Reed Epilogue Postcontent; 3:Somi Epilogue Postcontent → 2:Somi Epilogue Postcontent |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
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
| `ep1\quest\ep1.questphase` / h0 / 9 | `ep1_main_quests.questphase` | 22: LogicalHub; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 19: Phase; 86: LogicalHub; 87: LogicalHub; 22:Out1 → 9:Base; 12:q301 → 9:q301; 12:q302 → 9:q302; 12:q303 → 9:q303; 12:q304 → 9:q304; 12:q305 → 9:q305; 12:q306 → 9:q306; 12:q307 → 9:q307; 19:Out1 → 9:Standalone; 86:Out1 → 9:CP77-64292_in; 87:Out1 → 9:CP77-65722_Out |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `q306_songbird_recording.scene` | Start 0 → End 0 | Songbird; V; 32 nodes / 32 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `q306_songbird_recording.scene / n591 / 0` | [Pick up] (`take`) | No option-level predicate stored | 0:0 → 598:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `q306_DEBUG_debugModeOn` | Producer outside selected context | q306_06_postcontent_cache.questphase / h0 / 35 |
| `q306_reed_killed` | Producer outside selected context | q306_songbird_recording.scene / scene / 631 |

## Exact gates, joins and cancellation

<details><summary>36 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `q115_00_hanako.questphase / h1024 / 184` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":35}}}` | 166:Out → 184:In; 184:Out → 167:Failed |
| `q115_00_hanako.questphase / h1024 / 185` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":35}}}` | 167:Out → 185:In; 185:Out → 168:Failed |
| `q306_06_postcontent_cache.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/unknown/q306_somi_cryptic_msg/q306_cryptic_msg_02_player_responses_a/q306_cryptic_msg_02_choice_01","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 55:CutSource → 3:CutDestination; 28:Out → 3:In; 3:Out → 6:In1 |
| `q306_06_postcontent_cache.questphase / h0 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/unknown/q306_somi_cryptic_msg/q306_cryptic_msg_02_player_responses_a/q306_cryptic_msg_02_choice_02","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 55:CutSource → 4:CutDestination; 28:Out → 4:In; 4:Out → 6:In2 |
| `q306_06_postcontent_cache.questphase / h0 / 6` | `questLogicalXorNodeDefinition` `{}` | 3:Out → 6:In1; 4:Out → 6:In2; 6:Out1 → 80:In |
| `q306_06_postcontent_cache.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryVisited_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/unknown/q306_somi_cryptic_msg/q306_cryptic_msg_01_coordinates","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"visited":true}}}` | 55:CutSource → 20:CutDestination; 100:Out → 20:In; 20:Out → 39:Succeeded |
| `q306_06_postcontent_cache.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#q306_songbird_epilogue_cache","eventType":"Executed"}}}` | 55:CutSource → 13:CutDestination; 86:Out1 → 13:In; 13:Out → 85:In1 |
| `q306_06_postcontent_cache.questphase / h0 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"157793759361","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 29:Out → 75:In |
| `q306_06_postcontent_cache.questphase / h0 / 30` | `questLogicalAndNodeDefinition` `{}` | 58:Out → 30:In1; 63:Out → 30:In2; 30:Out1 → 65:Succeeded |
| `q306_06_postcontent_cache.questphase / h0 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":2}}}` | 35:False → 34:In; 34:Out → 74:In |
| `q306_06_postcontent_cache.questphase / h0 / 35` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_DEBUG_debugModeOn"}}}` | 0:Out → 35:In; 35:False → 34:In; 35:True → 36:In |
| `q306_06_postcontent_cache.questphase / h0 / 55` | `questCutControlNodeDefinition` `{"permanent":true}` | 55:CutSource → 3:CutDestination; 55:CutSource → 4:CutDestination; 55:CutSource → 20:CutDestination; 55:CutSource → 13:CutDestination; 67:Out1 → 55:In; 55:Out → 66:In; 55:Out → 94:In; 55:CutSource → 83:CutDestination |
| `q306_06_postcontent_cache.questphase / h0 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"82858490129","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 58:Out → 30:In1; 64:Out1 → 58:In; 58:Out → 67:In1 |
| `q306_06_postcontent_cache.questphase / h0 / 63` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"134671136573","quantity":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"153710509724","quantity":1,"comparisonType":"GreaterOrEqual"}}]}}` | 63:Out → 30:In2; 64:Out1 → 63:In; 63:Out → 67:In2 |
| `q306_06_postcontent_cache.questphase / h0 / 66` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/main_quest/q306_postcontent/00_common/000_read_message","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 66:True → 48:Succeeded; 55:Out → 66:In; 66:False → 68:In |
| `q306_06_postcontent_cache.questphase / h0 / 67` | `questLogicalXorNodeDefinition` `{}` | 67:Out1 → 55:In; 58:Out → 67:In1; 63:Out → 67:In2 |
| `q306_06_postcontent_cache.questphase / h0 / 68` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/main_quest/q306_postcontent/00_common/00_find_cache","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 68:True → 14:Succeeded; 48:Out → 68:In; 66:False → 68:In; 68:False → 98:In |
| `q306_06_postcontent_cache.questphase / h0 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#songbird_cahce_area"}}` | 74:Out → 2:Active; 34:Out → 74:In; 36:Out → 74:In |
| `q306_06_postcontent_cache.questphase / h0 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 80:Out → 5:Active; 6:Out1 → 80:In |
| `q306_06_postcontent_cache.questphase / h0 / 83` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q306_songbird_epilogue_cache"}}}}` | 55:CutSource → 83:CutDestination; 86:Out1 → 83:In; 83:Out → 85:In2 |
| `q306_06_postcontent_cache.questphase / h0 / 85` | `questLogicalXorNodeDefinition` `{}` | 13:Out → 85:In1; 85:Out1 → 62:Succeeded; 83:Out → 85:In2 |
| `q306_06_postcontent_cache.questphase / h0 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/unknown/q306_somi_cryptic_msg/q306_cryptic_msg_02b_reponse_post/01_song","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 92:Out → 87:In; 87:Out → 90:In1 |
| `q306_06_postcontent_cache.questphase / h0 / 88` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/unknown/q306_somi_cryptic_msg/q306_cryptic_msg_02b_reponse_post/02_thanks","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 92:Out → 88:In; 88:Out → 90:In2 |
| `q306_06_postcontent_cache.questphase / h0 / 90` | `questLogicalXorNodeDefinition` `{}` | 87:Out → 90:In1; 88:Out → 90:In2; 90:Out1 → 93:In |
| `q306_06_postcontent_cache.questphase / h0 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 93:Out → 89:Active; 90:Out1 → 93:In |
| `q306_06_postcontent_cache.questphase / h0 / 94` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/unknown/q306_somi_cryptic_msg/q306_cryptic_msg_02_player_responses_a/q306_cryptic_msg_02_choice_01","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded","inverted":true}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/unknown/q306_somi_cryptic_msg/q306_cryptic_msg_02_player_responses_a/q306_cryptic_msg_02_choice_02","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded","inverted":true}}]}}` | 55:Out → 94:In; 94:True → 95:Inactive |
| `q306_06_postcontent_cache.questphase / h0 / 98` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/main_quest/q306_postcontent/00_common/00_find_cache","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Inactive"}}}` | 14:Out → 98:In; 68:False → 98:In; 98:True → 70:Active |
| `q306_06_postcontent_cache.questphase / h0 / 99` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#songbird_cahce_area"}}` | 2:Out → 99:In; 99:Out → 72:In |
| `q306_06_postcontent_cache.questphase / h0 / 101` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 38:Out → 101:In; 101:Out → 100:Active |
| `q306_songbird_recording.scene / scene / 557` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 557:0:0 → 4:0:0; 655:0:0 → 557:0:1 |
| `q306_songbird_recording.scene / scene / 568` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 4:0:0 → 568:0:1; 568:0:0 → 587:0:1; 568:0:0 → 665:0:1 |
| `q306_songbird_recording.scene / scene / 631` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_reed_killed"}}}` | 631:0:0 → 629:0:1; 631:0:1 → 634:0:1; 665:0:0 → 631:0:1 |
| `q306_songbird_recording.scene / scene / 641` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 553:0:0 → 641:0:1; 641:0:0 → 2:0:0 |
| `q306_songbird_recording.scene / scene / 647` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":700}}}` | 549:0:0 → 647:0:1; 647:0:0 → 645:0:1 |
| `q306_songbird_recording.scene / scene / 655` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 101:3:0 → 655:0:1; 655:0:0 → 538:0:1; 655:0:0 → 557:0:1 |
| `q306_songbird_recording.scene / scene / 665` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 568:0:0 → 665:0:1; 665:0:0 → 631:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `call_lifecycle` | q306_songbird_recording.scene / scene / 549; q306_songbird_recording.scene / scene / 553 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `checkpoint` | q306_06_postcontent_cache.questphase / h0 / 75; q306_06_postcontent_cache.questphase / h0 / 76; q306_songbird_recording.scene / scene / 598 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | q306_songbird_recording.scene / scene / 591 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | q306_06_postcontent_cache.questphase / h0 / 35; q306_songbird_recording.scene / scene / 631 | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | q306_06_postcontent_cache.questphase / h0 / 56; q306_06_postcontent_cache.questphase / h0 / 57; q306_06_postcontent_cache.questphase / h0 / 7; q306_06_postcontent_cache.questphase / h0 / 91; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `elapsed_time` | q306_06_postcontent_cache.questphase / h0 / 34 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | q306_06_postcontent_cache.questphase / h0 / 29; q306_06_postcontent_cache.questphase / h0 / 58; q306_06_postcontent_cache.questphase / h0 / 63 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_read` | q306_06_postcontent_cache.questphase / h0 / 20 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | q115_00_hanako.questphase / h1024 / 167; q306_06_postcontent_cache.questphase / h0 / 100; q306_06_postcontent_cache.questphase / h0 / 14; q306_06_postcontent_cache.questphase / h0 / 2; +14 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | q306_06_postcontent_cache.questphase / h0 / 30 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `race_resolution` | q306_06_postcontent_cache.questphase / h0 / 6; q306_06_postcontent_cache.questphase / h0 / 67; q306_06_postcontent_cache.questphase / h0 / 85; q306_06_postcontent_cache.questphase / h0 / 90 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | q115_00_hanako.questphase / h1024 / 184; q115_00_hanako.questphase / h1024 / 185; q306_06_postcontent_cache.questphase / h0 / 101; q306_06_postcontent_cache.questphase / h0 / 80; +7 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | q306_06_postcontent_cache.questphase / h0 / 55 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `scan_evidence` | q306_06_postcontent_cache.questphase / h0 / 83 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | q306_06_postcontent_cache.questphase / h0 / 49 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | q306_06_postcontent_cache.questphase / h0 / 74; q306_06_postcontent_cache.questphase / h0 / 99 | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `workspot_performance` | q306_songbird_recording.scene / scene / 423 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | q306_06_postcontent_cache.questphase / h0 / 72 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\main_quests\part1\q115\phases\q115_00_hanako.questphase` | content candidate; journal anchor | `base-q115` |
| `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` | content candidate; journal anchor | `ep1-q306` |
| `ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene` | content candidate; forward dependency | `ep1-q306` |

Evidence shards for this dossier (including parent context): [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-08.json.gz), [ep1-sts-ep1-13](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-13.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

61 repeated typed/socket path signatures in this selected graph context; 5 distinct direct resource identities; 0 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `284bdb86131aa380ab85` | `ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene` / scene / 557 -> 4 -> 568 | questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `2a18d536739310eb7e61` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 85 -> 62 -> 84 | questLogicalXorNodeDefinition -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out1 -> Succeeded; Out -> Active |
| `b54739889d4d9a0745d2` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 2 -> 28 -> 3 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> Active; Out -> In |
| `abbf46d00a7c0ae464b9` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 66 -> 68 -> 98 | questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; False -> In; False -> In |
| `e2c6f0e72acf88934391` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 2 -> 38 -> 101 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; Out -> Active; Out -> In |
| `2be296de9cd6ded33fbd` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 48 -> 68 -> 98 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]; Out -> In; False -> In |
| `240148efc76953d1c5d4` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 100 -> 20 -> 39 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `8aa96c885edb6b1bc3c2` | `ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene` / scene / 655 -> 557 -> 4 | questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `96d50f7c3b7520546f50` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 48 -> 68 -> 14 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; True -> Succeeded |
| `a732a0cf44ff0251be89` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 13 -> 85 -> 62 | questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition] -> questLogicalXorNodeDefinition -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In1; Out1 -> Succeeded |
| `dea8e50289b8821c58be` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 65 -> 52 -> 32 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questOutputNodeDefinition; Out -> Succeeded; Out -> In |
| `2168db21f40f2c87ea45` | `ep1\quest\main_quests\q306\phases\subphases\q306_06_postcontent_cache.questphase` / h0 / 38 -> 101 -> 100 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| No embedded handoff in resolved context | — | External calls remain in the main dossier |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq303\mq303.gamedef` | content candidate | ep1\quest\minor_quests\mq303\mq303.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq305\mq305.gamedef` | content candidate | ep1\quest\minor_quests\mq305\mq305.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
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
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest; ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest; ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_nc_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `ep1\animations\quest\main_quests\q303\q303_04_mr_hands\body\q303_04_mr_hands__player_male.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\gameplay\gui\quests\q306\q306_songbird_shard_message.inkwidget` | UI | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_songbird_recording\songbird.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\lipsync\en\q306_songbird_recording\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `q306_DEBUG_debugModeOn` | ep1\quest\main_quests\q306\q306.quest / h99 / 9; ep1\quest\test\q306_spaceport_performance.quest / h11 / 9; 2 total source locations in compressed evidence |
| `q306_reed_killed` | ep1\quest\main_quests\q306\scenes\q306_10_finale.scene / scene / 803; ep1\quest\main_quests\q306\test\q306_00_chickentest.scene / scene / 825; 2 total source locations in compressed evidence |

NodeRef uses: 14; TweakDB binding uses: 23. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `ep1\quest\main_quests\q306\scenes\q306_songbird_recording.scene` | 2 / 15 | scnAudioEvent: 1; scnDialogLineEvent: 3; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnPlaySkAnimEvent: 1; scnUnmountEvent: 1; scneventsEquipItemToPerformer: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 3; scneventsVFXEvent: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
