# Psycho Killer

Journal: `quests/minor_quest/mq043_cyberpsychos` · `MinorQuest` · hash `2681247412`.

**Coverage: journal-linked.** 29 exact journal-linked nodes in 2 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Ever heard of a fixer by the name of Regina Jones? Not exactly the same league as Dex, but she must've heard about you since she wants to turn you into a one-man army in the fight against cyberpsychosis. Understandable, seeing as most of our heroic badges seem to vanish from the scene at the mention of "cyberpsycho."\n\nDo not fuck this up – one happy fixer will make three others interested in your services.\n\nI still don't get why Regina wants them alive, but I guess the higher you go, the weirder the contracts get. That's the Afterlife for you. (Primary) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` |
| Wait for update from Regina about the Cyberpsycho Sighting. (Primary) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_a_wait_regina` |
| Meet with Regina. (Primary) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina` |
| Collect your reward. (Primary) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/03_take_reward` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `reggie_default.scene / scene / 331` (Condition) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina` | 331:0:0 → 266:0:1; 331:0:1 → 330:0:0; 397:0:1 → 331:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `reggie_default.scene / scene / 471` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina` | 394:0:0 → 471:0:3; 471:0:0 → 998:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `reggie_default.scene / scene / 998` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/03_take_reward` | 471:0:0 → 998:0:1; 998:0:0 → 960:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `open_world_cyberpsychos.questphase / h0 / 12` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 19:Out → 12:Active; 12:Out → 13:Active |
| `open_world_cyberpsychos.questphase / h0 / 13` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina/mq043_desc` | 12:Out → 13:Active |
| `open_world_cyberpsychos.questphase / h0 / 15` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina` | 67:Out → 15:Active; 15:Out → 84:In1 |
| `open_world_cyberpsychos.questphase / h0 / 26` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 27:Out → 26:Increment; 26:Out → 90:In |
| `open_world_cyberpsychos.questphase / h0 / 28` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 29:Out → 28:Increment; 28:Out → 91:In |
| `open_world_cyberpsychos.questphase / h0 / 30` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 31:Out → 30:Increment; 30:Out → 92:In |
| `open_world_cyberpsychos.questphase / h0 / 32` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 33:Out → 32:Increment; 32:Out → 93:In |
| `open_world_cyberpsychos.questphase / h0 / 34` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 35:Out → 34:Increment; 34:Out → 94:In |
| `open_world_cyberpsychos.questphase / h0 / 36` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 37:Out → 36:Increment; 36:Out → 95:In |
| `open_world_cyberpsychos.questphase / h0 / 38` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 39:Out → 38:Increment; 38:Out → 96:In |
| `open_world_cyberpsychos.questphase / h0 / 40` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 41:Out → 40:Increment; 40:Out → 97:In |
| `open_world_cyberpsychos.questphase / h0 / 42` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 43:Out → 42:Increment; 42:Out → 98:In |
| `open_world_cyberpsychos.questphase / h0 / 44` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 45:Out → 44:Increment; 44:Out → 99:In |
| `open_world_cyberpsychos.questphase / h0 / 46` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 47:Out → 46:Increment; 46:Out → 100:In |
| `open_world_cyberpsychos.questphase / h0 / 48` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 49:Out → 48:Increment; 48:Out → 101:In |
| `open_world_cyberpsychos.questphase / h0 / 50` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 51:Out → 50:Increment; 50:Out → 102:In |
| `open_world_cyberpsychos.questphase / h0 / 52` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 53:Out → 52:Increment; 52:Out → 103:In |
| `open_world_cyberpsychos.questphase / h0 / 54` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 55:Out → 54:Increment; 54:Out → 104:In |
| `open_world_cyberpsychos.questphase / h0 / 56` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 57:Out → 56:Increment; 56:Out → 105:In |
| `open_world_cyberpsychos.questphase / h0 / 58` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 59:Out → 58:Increment; 58:Out → 106:In |
| `open_world_cyberpsychos.questphase / h0 / 66` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_a_wait_regina` | 66:Out → 24:In; 68:Out → 66:Active |
| `open_world_cyberpsychos.questphase / h0 / 67` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_a_wait_regina` | 8:all_psychos_done_out → 67:Succeeded; 67:Out → 15:Active |
| `open_world_cyberpsychos.questphase / h0 / 80` (MappinManager) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina/regina` | 82:Out → 80:Active; 80:Out → 87:In |
| `open_world_cyberpsychos.questphase / h0 / 85` (PauseCondition) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina` | 85:Out → 1:In; 84:Out1 → 85:In |
| `open_world_cyberpsychos.questphase / h0 / 88` (MappinManager) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina/regina1` | 88:Out → 82:In; 87:Out → 88:Active |
| `open_world_cyberpsychos.questphase / h0 / 68` (Journal) | `quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/01_help_regina` | 9:Out → 68:Succeeded; 68:Out → 66:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `open_world_cyberpsychos.questphase / h0 / 6` | `base\open_world\fixers\reggie\scenes\reggie_default.scene`; `#reggie_sm_default` | 20:Out1 → 6:psycho_intro_in; 6:psycho_intro_out → 109:In; 6:psycho_intro_out → 19:In; 6:psycho_intro_out → 121:In; 6:regina_psycho_intro_holocall INT → 23:In; 6:regina_psycho_intro_holocall RET → 22:In |
| `open_world_cyberpsychos.questphase / h0 / 8` | `base\open_world\fixers\reggie\scenes\reggie_default.scene`; `#reggie_sm_default` | 25:Out → 8:all_psychos_one_out; 8:all_psychos_done_out → 67:Succeeded; 8:regina_psycho_intro_holocall INT → 70:In; 8:regina_psycho_intro_holocall RET → 69:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\phases\cyberpsychos\open_world_cyberpsychos.questphase` / h0 / 6 | `reggie_default.scene` | 20: LogicalXor; 20:Out1 → 6:psycho_intro_in; 6:psycho_intro_out → 109:In; 6:psycho_intro_out → 19:In; 6:psycho_intro_out → 121:In; 6:regina_psycho_intro_holocall INT → 23:In; 6:regina_psycho_intro_holocall RET → 22:In |
| `base\open_world\phases\cyberpsychos\open_world_cyberpsychos.questphase` / h0 / 8 | `reggie_default.scene` | 25: PauseCondition; 25:Out → 8:all_psychos_one_out; 8:all_psychos_done_out → 67:Succeeded; 8:regina_psycho_intro_holocall INT → 70:In; 8:regina_psycho_intro_holocall RET → 69:In |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `reggie_default.scene` | Start 0, psycho_intro_in, reggie_default_holo_in, Start 5, all_psychos_one_out, welcome → holo_to_face, psycho_intro_out, all_psychos_done_out, welcome_out, reggie_default_holo_out | regina; regina_holo; Player; 151 nodes / 161 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `reggie_default.scene / n61 / 0` | Tell me about Watson. (`watson`) | No option-level predicate stored | 0:0 → 62:0:0 |
| `reggie_default.scene / n61 / 1` | Royce – what do you know about him? (`royce`) | {"questCondition": {"$type": "questLogicalCondition", "conditions": [{"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "q001_done"}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "q003_done", "comparisonType": "Equal"}}]}} | 0:1 → 202:0:0 |
| `reggie_default.scene / n61 / 2` | How you getting along with Max? (`max_after_nid_12`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "nid_12_finished"}}} | 0:2 → 90:0:0 |
| `reggie_default.scene / n61 / 3` | Heard the news about Max. (`max_death`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "sts_wat_nid_12_result_radio_heard"}}} | 0:3 → 92:0:0 |
| `reggie_default.scene / n61 / 4` | Used to be a journalist. (`media`) | No option-level predicate stored | 0:4 → 63:0:0 |
| `reggie_default.scene / n61 / 5` | What's the situation with cyberpsychosis research? (`psychos`) | {"questCondition": {"$type": "questLogicalCondition", "conditions": [{"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "ow_psychos_done"}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "reggie_dd_holo", "value": 1, "comparisonType": "Less"}}]}} | 0:5 → 414:0:0 |
| `reggie_default.scene / n61 / 6` | Catch you later. (`Bye`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "reggie_dd_holo"}}} | 0:6 → 621:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `ep1_standalone` | Producer outside selected context | open_world_cyberpsychos.questphase / h0 / 116; open_world_cyberpsychos.questphase / h0 / 121 |
| `holo_reggie_calls_v_end_activate` | open_world_cyberpsychos.questphase / h0 / 23; open_world_cyberpsychos.questphase / h0 / 70; reggie_default.scene / scene / 779; reggie_default.scene / scene / 846; reggie_default.scene / scene / 985 | No reader in selected context |
| `holo_reggie_calls_v_end_done` | reggie_default.scene / scene / 775; reggie_default.scene / scene / 845; reggie_default.scene / scene / 983 | reggie_default.scene / scene / 774; reggie_default.scene / scene / 844; reggie_default.scene / scene / 981 |
| `holo_reggie_calls_v_start_activate` | open_world_cyberpsychos.questphase / h0 / 22; open_world_cyberpsychos.questphase / h0 / 69; reggie_default.scene / scene / 778; reggie_default.scene / scene / 839; reggie_default.scene / scene / 968 | No reader in selected context |
| `holo_reggie_calls_v_start_done` | reggie_default.scene / scene / 773; reggie_default.scene / scene / 838; reggie_default.scene / scene / 966 | reggie_default.scene / scene / 772; reggie_default.scene / scene / 837; reggie_default.scene / scene / 964 |
| `holo_setup_ended` | Producer outside selected context | reggie_default.scene / scene / 706 |
| `holo_v_calls_reggie_end_activate` | reggie_default.scene / scene / 729; reggie_default.scene / scene / 732 | No reader in selected context |
| `holo_v_calls_reggie_end_done` | reggie_default.scene / scene / 614; reggie_default.scene / scene / 767 | reggie_default.scene / scene / 613 |
| `holo_v_calls_reggie_start_activate` | reggie_default.scene / scene / 726 | No reader in selected context |
| `holo_v_calls_reggie_start_done` | reggie_default.scene / scene / 612 | reggie_default.scene / scene / 610 |
| `mq007_reggie_manual_interrupt` | Producer outside selected context | reggie_default.scene / scene / 829; reggie_default.scene / scene / 924; reggie_default.scene / scene / 929 |
| `mq043_done` | reggie_default.scene / scene / 960 | No reader in selected context |
| `nid_12_finished` | Producer outside selected context | reggie_default.scene / scene / 61 |
| `ow_psychos_done` | Producer outside selected context | open_world_cyberpsychos.questphase / h0 / 27; open_world_cyberpsychos.questphase / h0 / 29; open_world_cyberpsychos.questphase / h0 / 31; open_world_cyberpsychos.questphase / h0 / 33; open_world_cyberpsychos.questphase / h0 / 35; open_world_cyberpsychos.questphase / h0 / 37; open_world_cyberpsychos.questphase / h0 / 39; open_world_cyberpsychos.questphase / h0 / 41; open_world_cyberpsychos.questphase / h0 / 43; open_world_cyberpsychos.questphase / h0 / 45; open_world_cyberpsychos.questphase / h0 / 47; open_world_cyberpsychos.questphase / h0 / 49; open_world_cyberpsychos.questphase / h0 / 51; open_world_cyberpsychos.questphase / h0 / 53; open_world_cyberpsychos.questphase / h0 / 55; open_world_cyberpsychos.questphase / h0 / 57; open_world_cyberpsychos.questphase / h0 / 59; open_world_cyberpsychos.questphase / h0 / 9; reggie_default.scene / scene / 61 |
| `ow_psychos_intro_done` | open_world_cyberpsychos.questphase / h0 / 19 | open_world_cyberpsychos.questphase / h0 / 110 |
| `ow_psychos_intro_start` | reggie_default.scene / scene / 350 | open_world_cyberpsychos.questphase / h0 / 7 |
| `ow_psychos_killed` | Producer outside selected context | reggie_default.scene / scene / 266; reggie_default.scene / scene / 273 |
| `ow_psychos_reward_collected` | reggie_default.scene / scene / 394 | reggie_default.scene / scene / 397 |
| `q001_can_call_dex` | Producer outside selected context | open_world_cyberpsychos.questphase / h0 / 119 |
| `q001_done` | Producer outside selected context | reggie_default.scene / scene / 61 |
| `q003_done` | Producer outside selected context | reggie_default.scene / scene / 61 |
| `reggie_dd_holo` | reggie_default.scene / scene / 798 | reggie_default.scene / scene / 61; reggie_default.scene / scene / 825; reggie_default.scene / scene / 829 |
| `reggie_dd_skip_intro` | reggie_default.scene / scene / 867 | No reader in selected context |
| `reggie_visited` | reggie_default.scene / scene / 225; reggie_default.scene / scene / 226 | No reader in selected context |
| `sts_wat_nid_12_result_radio_heard` | Producer outside selected context | reggie_default.scene / scene / 61 |
| `v_vs_generic_1_done` | reggie_default.scene / scene / 442 | reggie_default.scene / scene / 426 |
| `v_vs_generic_6_done` | reggie_default.scene / scene / 439 | reggie_default.scene / scene / 421 |
| `v_vs_scene_thanks_var_1_done` | reggie_default.scene / scene / 436 | reggie_default.scene / scene / 433 |

## Exact gates, joins and cancellation

<details><summary>55 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `reggie_default.scene / scene / 157` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#reggie","names":["reggie"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"Less"}}}` | 144:0:0 → 157:0:1; 157:0:0 → 147:0:0 |
| `reggie_default.scene / scene / 227` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 225:0:0 → 227:0:1; 227:0:0 → 226:0:1 |
| `reggie_default.scene / scene / 266` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_killed","value":9,"comparisonType":"Less"}}}` | 266:0:0 → 273:0:1; 266:0:1 → 270:0:0; 331:0:0 → 266:0:1 |
| `reggie_default.scene / scene / 273` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_killed","comparisonType":"Equal"}}}` | 266:0:0 → 273:0:1; 273:0:0 → 272:0:0; 273:0:1 → 263:0:0 |
| `reggie_default.scene / scene / 331` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 331:0:0 → 266:0:1; 331:0:1 → 330:0:0; 397:0:1 → 331:0:1 |
| `reggie_default.scene / scene / 397` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_reward_collected","value":1,"comparisonType":"GreaterOrEqual"}}}` | 397:0:0 → 398:0:0; 397:0:1 → 331:0:1; 482:0:0 → 397:0:1 |
| `reggie_default.scene / scene / 421` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"v_vs_generic_6_done"}}}` | 420:0:0 → 421:0:1; 421:0:0 → 439:0:1 |
| `reggie_default.scene / scene / 426` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"v_vs_generic_1_done"}}}` | 425:0:0 → 426:0:1; 426:0:0 → 442:0:1 |
| `reggie_default.scene / scene / 433` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"v_vs_scene_thanks_var_1_done"}}}` | 433:0:0 → 436:0:1; 549:0:0 → 433:0:1 |
| `reggie_default.scene / scene / 610` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_v_calls_reggie_start_done"}}}` | 610:0:0 → 612:0:1; 726:0:0 → 610:0:1 |
| `reggie_default.scene / scene / 613` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_v_calls_reggie_end_done"}}}` | 613:0:0 → 614:0:1; 732:0:0 → 613:0:1 |
| `reggie_default.scene / scene / 655` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#reggina_jones_tr_greet"}}` | 615:0:0 → 655:0:1; 655:0:0 → 738:0:1 |
| `reggie_default.scene / scene / 706` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_ended"}}}` | 706:0:0 → 767:0:1; 729:0:0 → 706:0:1 |
| `reggie_default.scene / scene / 772` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 772:0:0 → 773:0:1; 778:0:0 → 772:0:1 |
| `reggie_default.scene / scene / 774` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 774:0:0 → 775:0:1; 779:0:0 → 774:0:1 |
| `reggie_default.scene / scene / 825` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"reggie_dd_holo"}}}` | 61:1:0 → 825:0:1; 825:0:1 → 824:0:0 |
| `reggie_default.scene / scene / 829` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"reggie_dd_holo"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq007_reggie_manual_interrupt"}}]}}` | 540:0:0 → 829:0:1; 829:0:0 → 61:0:0; 829:0:1 → 828:0:0 |
| `reggie_default.scene / scene / 837` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 837:0:0 → 838:0:1; 839:0:0 → 837:0:1 |
| `reggie_default.scene / scene / 844` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 844:0:0 → 845:0:1; 846:0:0 → 844:0:1 |
| `reggie_default.scene / scene / 888` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#reggie","names":["reggie"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0}}}}` | 888:0:0 → 892:0:0; 888:0:0 → 897:0:1; 897:0:0 → 888:0:1; 941:0:0 → 888:0:1 |
| `reggie_default.scene / scene / 897` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#reggie","names":["reggie"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"Less"}}}` | 888:0:0 → 897:0:1; 897:0:0 → 878:0:0; 897:0:0 → 888:0:1; 941:0:0 → 897:0:1 |
| `reggie_default.scene / scene / 924` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq007_reggie_manual_interrupt","value":1,"comparisonType":"GreaterOrEqual"}}}` | 1:0:0 → 924:0:1; 924:0:0 → 926:0:0 |
| `reggie_default.scene / scene / 929` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq007_reggie_manual_interrupt","comparisonType":"LessOrEqual"}}}` | 926:0:0 → 929:0:1; 929:0:0 → 935:0:0 |
| `reggie_default.scene / scene / 964` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 964:0:0 → 966:0:1; 968:0:0 → 964:0:1 |
| `reggie_default.scene / scene / 981` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 981:0:0 → 983:0:1; 985:0:0 → 981:0:1 |
| `open_world_cyberpsychos.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_intro_start"}}}` | 0:Out → 7:In |
| `open_world_cyberpsychos.questphase / h0 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":16}}}` | 113:Out → 9:In; 9:Out → 68:Succeeded |
| `open_world_cyberpsychos.questphase / h0 / 20` | `questLogicalXorNodeDefinition` `{}` | 20:Out1 → 6:psycho_intro_in; 114:Out → 20:In2; 119:Out → 20:In2 |
| `open_world_cyberpsychos.questphase / h0 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":12}}}` | 66:Out → 24:In; 24:Out → 25:In |
| `open_world_cyberpsychos.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 25:Out → 8:all_psychos_one_out; 24:Out → 25:In |
| `open_world_cyberpsychos.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":1,"comparisonType":"Equal"}}}` | 27:Out → 26:Increment; 112:Out1 → 27:In |
| `open_world_cyberpsychos.questphase / h0 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":2,"comparisonType":"Equal"}}}` | 29:Out → 28:Increment; 112:Out1 → 29:In |
| `open_world_cyberpsychos.questphase / h0 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":3,"comparisonType":"Equal"}}}` | 31:Out → 30:Increment; 112:Out1 → 31:In |
| `open_world_cyberpsychos.questphase / h0 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":4,"comparisonType":"Equal"}}}` | 33:Out → 32:Increment; 112:Out1 → 33:In |
| `open_world_cyberpsychos.questphase / h0 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":5,"comparisonType":"Equal"}}}` | 35:Out → 34:Increment; 112:Out1 → 35:In |
| `open_world_cyberpsychos.questphase / h0 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":6,"comparisonType":"Equal"}}}` | 37:Out → 36:Increment; 112:Out1 → 37:In |
| `open_world_cyberpsychos.questphase / h0 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":7,"comparisonType":"Equal"}}}` | 39:Out → 38:Increment; 112:Out1 → 39:In |
| `open_world_cyberpsychos.questphase / h0 / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":8,"comparisonType":"Equal"}}}` | 41:Out → 40:Increment; 112:Out1 → 41:In |
| `open_world_cyberpsychos.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":9,"comparisonType":"Equal"}}}` | 43:Out → 42:Increment; 112:Out1 → 43:In |
| `open_world_cyberpsychos.questphase / h0 / 45` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":10,"comparisonType":"Equal"}}}` | 45:Out → 44:Increment; 112:Out1 → 45:In |
| `open_world_cyberpsychos.questphase / h0 / 47` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":11,"comparisonType":"Equal"}}}` | 47:Out → 46:Increment; 112:Out1 → 47:In |
| `open_world_cyberpsychos.questphase / h0 / 49` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":12,"comparisonType":"Equal"}}}` | 49:Out → 48:Increment; 112:Out1 → 49:In |
| `open_world_cyberpsychos.questphase / h0 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":13,"comparisonType":"Equal"}}}` | 51:Out → 50:Increment; 112:Out1 → 51:In |
| `open_world_cyberpsychos.questphase / h0 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":14,"comparisonType":"Equal"}}}` | 53:Out → 52:Increment; 112:Out1 → 53:In |
| `open_world_cyberpsychos.questphase / h0 / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":15,"comparisonType":"Equal"}}}` | 55:Out → 54:Increment; 112:Out1 → 55:In |
| `open_world_cyberpsychos.questphase / h0 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":16,"comparisonType":"Equal"}}}` | 57:Out → 56:Increment; 112:Out1 → 57:In |
| `open_world_cyberpsychos.questphase / h0 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_done","value":17,"comparisonType":"Equal"}}}` | 59:Out → 58:Increment; 112:Out1 → 59:In |
| `open_world_cyberpsychos.questphase / h0 / 82` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#regina_dd_tr_floor"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#reggie"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}]}}` | 82:Out → 80:Active; 84:Out1 → 82:In; 88:Out → 82:In |
| `open_world_cyberpsychos.questphase / h0 / 85` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq043_cyberpsychos/mq043_cyberpsychos/02_talk_regina","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 85:Out → 1:In; 84:Out1 → 85:In |
| `open_world_cyberpsychos.questphase / h0 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#regina_dd_tr_floor"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#reggie"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"Less"}}}]}}` | 80:Out → 87:In; 87:Out → 88:Active |
| `open_world_cyberpsychos.questphase / h0 / 110` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ow_psychos_intro_done"}}}` | 111:Out → 110:In; 110:Out → 112:In1 |
| `open_world_cyberpsychos.questphase / h0 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questContentCondition","type":{"$type":"questContentToken_ConditionType","type":"EP1_SideQuest"}},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#pacifica_tr"}]}}` | 114:Out → 20:In2; 116:True → 114:In |
| `open_world_cyberpsychos.questphase / h0 / 116` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone","value":1,"comparisonType":"GreaterOrEqual"}}}` | 116:True → 114:In; 120:Out → 116:In; 116:False → 119:In |
| `open_world_cyberpsychos.questphase / h0 / 119` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_can_call_dex"}},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q001_tr_jackie_noticing_v"},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 119:Out → 20:In2; 116:False → 119:In |
| `open_world_cyberpsychos.questphase / h0 / 121` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone","value":1,"comparisonType":"GreaterOrEqual"}}}` | 6:psycho_intro_out → 121:In; 121:True → 122:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | open_world_cyberpsychos.questphase / h0 / 82; open_world_cyberpsychos.questphase / h0 / 87 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `call_lifecycle` | reggie_default.scene / scene / 1059 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `choice_gate` | reggie_default.scene / scene / 61 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | open_world_cyberpsychos.questphase / h0 / 110; open_world_cyberpsychos.questphase / h0 / 116; open_world_cyberpsychos.questphase / h0 / 119; open_world_cyberpsychos.questphase / h0 / 121; +39 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | open_world_cyberpsychos.questphase / h0 / 122 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `elapsed_time` | open_world_cyberpsychos.questphase / h0 / 24 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `persistent_decision` | open_world_cyberpsychos.questphase / h0 / 19; open_world_cyberpsychos.questphase / h0 / 22; open_world_cyberpsychos.questphase / h0 / 23; open_world_cyberpsychos.questphase / h0 / 69; +29 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | open_world_cyberpsychos.questphase / h0 / 20 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | reggie_default.scene / scene / 227 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | reggie_default.scene / scene / 864 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | open_world_cyberpsychos.questphase / h0 / 6; open_world_cyberpsychos.questphase / h0 / 8 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `workspot_performance` | reggie_default.scene / scene / 1010; reggie_default.scene / scene / 1018; reggie_default.scene / scene / 1019; reggie_default.scene / scene / 1024; +22 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\fixers\reggie\scenes\reggie_default.scene` | content candidate; journal anchor | `base-shared` |
| `base\open_world\phases\cyberpsychos\open_world_cyberpsychos.questphase` | content candidate; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
