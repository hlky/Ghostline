# Go Your Own Way

Journal: `ep1/quests/minor_quest/wst_ep1_05` · `MinorQuest` · hash `1940045604`.

Journal premise: Clever bastard’s got a head for biz. He clearly made it and then some. Wonder if he misses that old corporat cage now.

**Coverage: journal-linked.** 10 exact journal-linked nodes in 1 resources; 3 resources in the inspected dependency context.

Resource roles in that context: 3 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

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
| `ep1\openworld\street_stories\sts_ep1_04\sts_ep1_04.quest` / h0 / 10 | `wst_ep1_05.questphase` | 6: Scene: sts_ep1_04_chicken_test.scene; 6:wst_ep1_05 → 10:chickentest |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 5 | `wst_ep1_05.questphase` | 29: PauseCondition: hasan_default_on; 29:Out → 5:In1 |
| `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.quest` / h0 / 2 | `wst_ep1_05.questphase` | 0: Start; 0:Out → 2:chickentest |
| `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 41 | `sts_04_hasan_default.questphase` | 44: FactsDBManager: hasan_default_on; 44:Out → 41:In1 |
| `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 22 | `sts_04_hasan_default.questphase` | 21: FactsDBManager: hasan_default_on; 21:Out → 22:In1 |
| `ep1\quest\ep1_default_dialogs.questphase` / h0 / 9 | `sts_04_hasan_default.questphase` | 12: PauseCondition: hasan_default_on; 12:Out → 9:In1; 9:Out1 → 12:In |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h14 / 9 | `sts_04_hasan_default.scene` | 28: FactsDBManager: hasan_apartment_default_dialogue_start; 28:Out → 9:Hasan_default_1st_meeting_start; 9:Hasan_default_1st_meeting_end → 44:In |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h14 / 29 | `sts_04_hasan_default.scene` | 43: PauseCondition; 44: PauseCondition; 43:Out → 29:Hasan_default_apartment_start; 44:Out → 29:Hasan_default_apartment_start |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h245 / 28 | `sts_04_hasan_default.scene` | 29: FactsDBManager: hasan_squat_default_dialogue_start; 29:Out → 28:Hasan_squat_start; 28:End1 → 37:In |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h245 / 34 | `sts_04_hasan_default.scene` | 35: LogicalHub; 35:Out1 → 34:hasan_squat_talk_start; 34:End1 → 37:In |
| `ep1\openworld\ep1_open_world.questphase` / h0 / 14 | `ep1_world_stories.questphase` | 11: LogicalHub; 11:Out1 → 14:In1 |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest` / h0 / 7 | `ep1_world_stories.questphase` | 3: PauseCondition: {"seconds": 2}; 3:Out → 7:In1 |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest` / h0 / 112 | `ep1_world_stories.questphase` | 118: PauseCondition: sts_ep1_06_close_club; 118:Out → 112:In1 |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest` / h0 / 13 | `ep1_world_stories.questphase` | 7: PauseCondition: {"seconds": 2}; 7:Out → 13:In1 |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest` / h0 / 19 | `ep1_world_stories.questphase` | 3: FactsDBManager: ep1_12_test_def; 3:Out → 19:In1 |
| `ep1\openworld\street_stories\sts_ep1_04\sts_ep1_04.quest` / h0 / 9 | `wst_ep1_06.questphase` | 6: Scene: sts_ep1_04_chicken_test.scene; 6:wst_ep1_06 → 9:chickentest |
| `ep1\openworld\world_stories\ep1_world_stories.questphase` / h0 / 6 | `wst_ep1_06.questphase` | 30: PauseCondition: sts_ep1_04_finished; 30:Out → 6:In1 |
| `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.quest` / h0 / 1 | `wst_ep1_06.questphase` | 0: Start; 0:Out → 1:chickentest |
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

| Fact | Writers in context | Readers and other fact bindings in context |
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
| `controller_event` | wst_ep1_05.questphase / h0 / 74 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | wst_ep1_05.questphase / h0 / 31 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_04_hasan_default.questphase / h14 / 45; wst_ep1_05.questphase / h0 / 80 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | wst_ep1_05.questphase / h0 / 47 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | wst_ep1_05.questphase / h0 / 52 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_read` | wst_ep1_05.questphase / h0 / 72 | full journal entry path + visited state → entry visited. Verify the actual UI read event in game; keep inventory pickup distinct. |
| `journal_transition` | wst_ep1_05.questphase / h0 / 20; wst_ep1_05.questphase / h0 / 22; wst_ep1_05.questphase / h0 / 23; wst_ep1_05.questphase / h0 / 24; +12 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | wst_ep1_05.questphase / h0 / 68 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_04_hasan_default.questphase / h14 / 28; sts_04_hasan_default.questphase / h245 / 29; sts_04_hasan_default.scene / scene / 155; sts_04_hasan_default.scene / scene / 195; +11 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sts_04_hasan_default.questphase / h14 / 46; sts_04_hasan_default.questphase / h14 / 49; sts_04_hasan_default.questphase / h14 / 50; sts_04_hasan_default.questphase / h14 / 59; +8 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_04_hasan_default.questphase / h14 / 54; sts_04_hasan_default.questphase / h245 / 45 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `scene_interface` | sts_04_hasan_default.questphase / h14 / 29; sts_04_hasan_default.questphase / h14 / 9; sts_04_hasan_default.questphase / h245 / 28; sts_04_hasan_default.questphase / h245 / 34 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_04_hasan_default.questphase / h14 / 42; sts_04_hasan_default.questphase / h14 / 47; sts_04_hasan_default.questphase / h14 / 48; sts_04_hasan_default.questphase / h14 / 56; +5 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `workspot_performance` | sts_04_hasan_default.scene / scene / 315; sts_04_hasan_default.scene / scene / 317; sts_04_hasan_default.scene / scene / 318; sts_04_hasan_default.scene / scene / 494; +23 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | wst_ep1_05.questphase / h0 / 49; wst_ep1_05.questphase / h0 / 50; wst_ep1_05.questphase / h0 / 54 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` | content candidate; journal anchor | `ep1-wst-ep1-05` |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` | content candidate; forward dependency | `ep1-shared` |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` | content candidate; forward dependency | `ep1-shared` |

Evidence shards for this dossier (including parent context): [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mq306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq306.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q301.json.gz), [ep1-q302](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q302.json.gz), [ep1-q303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q303.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz), [ep1-sts-ep1-01](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-01.json.gz), [ep1-sts-ep1-04](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-04.json.gz), [ep1-sts-ep1-06-zembinsky](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-06-zembinsky.json.gz), [ep1-sts-ep1-08](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-08.json.gz), [ep1-sts-ep1-10](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-10.json.gz), [ep1-sts-ep1-12](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-12.json.gz), [ep1-sts-ep1-13](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-sts-ep1-13.json.gz), [ep1-wst-ep1-05](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-wst-ep1-05.json.gz), [ep1-wst-ep1-06](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-wst-ep1-06.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

170 repeated typed/socket path signatures in this selected graph context; 25 distinct direct resource identities; 2 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 42 -> 43 -> 44 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `a909c836470d2b0e7fbc` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h0 / 0 -> 46 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `19665e3783f6f51a7337` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` / scene / 11 -> 486 -> 564 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `1666d7526b9bab74f2e2` | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 24 -> 48 -> 55 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> Active; Out -> In |
| `276aca4a2dc348a877d5` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` / scene / 18 -> 176 -> 601 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `e70b0765e99ad324f9b7` | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 39 -> 42 -> 43 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `1d48bd7cbbaeca8257d2` | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 56 -> 28 -> 27 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Succeeded; Out -> In |
| `1a9b8893087e174a603f` | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 48 -> 55 -> 56 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; Out -> Succeeded |
| `a9ab7a13237f70294da0` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` / scene / 585 -> 28 -> 538 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `4d0b89400e09faa05792` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` / scene / 18 -> 176 -> 213 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `2c4762a122ece48d0e88` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` / scene / 54 -> 73 -> 50 | questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> scnRandomizerNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `7f1e8c62437f340385bf` | `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` / scene / 11 -> 486 -> 565 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h0 / 44 | `h14` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` / h0 / 55 | `h245` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest |
| `ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01_testworld.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_01\sts_ep1_01.quest |
| `ep1\openworld\street_stories\sts_ep1_04\sts_ep1_04_nc.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_04\sts_ep1_04.quest |
| `ep1\openworld\street_stories\sts_ep1_04\sts_ep1_04_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_04\sts_ep1_04.quest |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |
| `ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_06_zembinsky\sts_ep1_06_zembinsky.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_nc_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_08\sts_ep1_08.quest |
| `ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10_def.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_10\sts_ep1_10.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |
| `ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12_gamedef_test.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_12\sts_ep1_12.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_night_city.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |
| `ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13_test_world.gamedef` | content candidate | ep1\openworld\street_stories\sts_ep1_13\sts_ep1_13.quest |
| `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.gamedef` | content candidate | ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.quest |
| `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.gamedef` | content candidate | ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_additives.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_lipsync_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\homeless\open_world\homeless_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\homeless\open_world\homeless_wounded_creepy_leg.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean180__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_ground__2h_elbow_on_knees__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_hip__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\workspots\archetype\homeless\common\ground\homeless__sit__wounded_creepy_leg__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_lean_back_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__sit_ground_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__08.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stretch__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\prologue\q000\q000_nomad_07_hideout\q000__big__stand__look_at_iguana__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `ep1\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_hip__01.anims` | asset binding .anims | ep1/ep1_2_gamedata.archive; index evidence only |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\lipsync\en\sts_04_hasan_default\hasan.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\lipsync\en\sts_04_hasan_default\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase` | phase flow | ep1/ep1_2_gamedata.archive; structurally indexed |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` | scene flow | ep1/ep1_2_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `ep1_standalone` | ep1\quest\ep1_standalone.quest / h0 / 5; 1 total source locations in compressed evidence |
| `hasan_default_on` | ep1\openworld\street_stories\sts_ep1_04\phases\sts_ep1_04_cleanup.questphase / h0 / 12; ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase / h0 / 21; 2 total source locations in compressed evidence |
| `sts_ep1_04_blueprints_corpo` | ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan_final.scene / scene / 74; ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan_final.scene / scene / 115; 2 total source locations in compressed evidence |
| `sts_ep1_04_blueprints_hasan` | ep1\openworld\street_stories\sts_ep1_04\phases\sts_ep1_04_openworld.questphase / h1625 / 710; ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan_final.scene / scene / 125; ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan_final.scene / scene / 157; ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase / h0 / 19; 4 total source locations in compressed evidence |
| `sts_ep1_04_hasan_let_go` | ep1\openworld\street_stories\sts_ep1_04\phases\sts_ep1_04_openworld.questphase / h1625 / 709; ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan_final.scene / scene / 122; 2 total source locations in compressed evidence |
| `sts_ep1_04_hasan_let_go_earlier` | ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan_final.scene / scene / 154; 1 total source locations in compressed evidence |
| `sts_ep1_04_mr_hands_holo_convinced` | ep1\openworld\street_stories\sts_ep1_04\scenes\sts_ep1_04_hasan_final.scene / scene / 365; 1 total source locations in compressed evidence |
| `wst_ep1_06_active` | ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase / h0 / 17; 1 total source locations in compressed evidence |

NodeRef uses: 67; TweakDB binding uses: 30. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene` | 23 / 297 | scnChangeIdleAnimEvent: 15; scnDialogLineEvent: 54; scnLookAtEvent: 78; scnPlaySkAnimEvent: 107; scneventsEquipItemToPerformer: 4; scneventsSocket: 39 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
