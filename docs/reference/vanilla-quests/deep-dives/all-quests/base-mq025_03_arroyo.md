# Beat on the Brat: Arroyo

Journal: `quests/minor_quest/mq025_03_arroyo` · `MinorQuest` · hash `2421816651`.

**Coverage: journal-linked.** 19 exact journal-linked nodes in 1 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Heard somewhere the champ of Arroyo is a grade-A prick. Good news – should make beatin' his ass all the more fun. (Primary) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_arroyo_fight` |
| Defeat Buck. (Primary) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_fight` |
| Heard somewhere the champ of Arroyo is a grade-A prick. Good news – should make beatin' his ass all the more fun. (Primary) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_talk` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq025_03_arroyo.questphase / h0 / 3` (Journal) | `quests/minor_quest/mq025_03_arroyo` | 34:False → 3:Active; 3:Out → 4:Active |
| `mq025_03_arroyo.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_arroyo_fight` | 3:Out → 4:Active; 4:Out → 53:Active |
| `mq025_03_arroyo.questphase / h0 / 13` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_talk` | 12:Out → 13:Active; 102:False → 13:Active; 13:Out → 100:Active |
| `mq025_03_arroyo.questphase / h0 / 14` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_talk` | 17:Out1 → 14:Succeeded; 27:mq025_03_fight → 14:Succeeded; 14:Out → 15:Active |
| `mq025_03_arroyo.questphase / h0 / 15` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_fight` | 15:Out → 11:In1; 14:Out → 15:Active |
| `mq025_03_arroyo.questphase / h0 / 16` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_talk` | 11:Out1 → 16:Active; 16:Out → 28:mq025_03_after_in |
| `mq025_03_arroyo.questphase / h0 / 18` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_talk` | 28:mq025_03_after_out → 18:Succeeded; 18:Out → 89:In |
| `mq025_03_arroyo.questphase / h0 / 19` (Journal) | `quests/minor_quest/mq025_03_arroyo` | 88:Out → 19:Succeeded; 19:Out → 48:In; 19:Out → 72:In |
| `mq025_03_arroyo.questphase / h0 / 40` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_talk` | 28:mq025_03_after_out_fight → 40:Succeeded; 40:Out → 90:In |
| `mq025_03_arroyo.questphase / h0 / 41` (Journal) | `quests/minor_quest/mq025_03_arroyo` | 64:Out → 41:Succeeded; 41:Out → 80:In |
| `mq025_03_arroyo.questphase / h0 / 53` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_arroyo_fight/description` | 4:Out → 53:Active |
| `mq025_03_arroyo.questphase / h0 / 67` (Journal) | `quests/minor_quest/mq025_03_arroyo` | 34:True → 67:Active; 67:Out → 68:Active |
| `mq025_03_arroyo.questphase / h0 / 68` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_arroyo_fight` | 67:Out → 68:Active; 68:Out → 69:Active |
| `mq025_03_arroyo.questphase / h0 / 69` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_arroyo_fight/description` | 68:Out → 69:Active |
| `mq025_03_arroyo.questphase / h0 / 100` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_talk/description_arroyo` | 13:Out → 100:Active; 100:Out → 27:mq025_03_start_in |
| `mq025_03_arroyo.questphase / h0 / 101` (Condition) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_arroyo_fight` | 92:Out → 101:In; 101:True → 103:Succeeded; 101:False → 102:In |
| `mq025_03_arroyo.questphase / h0 / 103` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_arroyo_fight` | 101:True → 103:Succeeded; 103:Out → 102:In |
| `mq025_03_arroyo.questphase / h56 / 18` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_fight` | 18:Out → 9:In; 10:Out → 18:Succeeded |
| `mq025_03_arroyo.questphase / h56 / 19` (Journal) | `quests/minor_quest/mq025_03_arroyo/arroyo/03_fight` | 8:Out → 19:Failed; 19:Out → 9:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq025_03_arroyo.questphase / h0 / 27` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene`; `#mq025_03_sm_arroyo` | 27:mq025_03_fight → 14:Succeeded; 27:fight prep → 22:In1; 100:Out → 27:mq025_03_start_in |
| `mq025_03_arroyo.questphase / h0 / 28` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene`; `#mq025_03_sm_arroyo` | 16:Out → 28:mq025_03_after_in; 28:mq025_03_fight → 17:In1; 28:mq025_03_after_out → 18:Succeeded; 28:fight prep → 22:In1; 28:mq025_03_after_out_fight → 40:Succeeded |
| `mq025_03_arroyo.questphase / h0 / 46` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene`; `#mq025_03_sm_arroyo` | 48:Out → 46:mq025_03_post_in; 46:mq025_03_after_out_fight → 71:In1 |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.questphase` / h0 / 5 | `mq025_03_arroyo.questphase` | 12: PauseCondition: q101_enable_side_content; 12:Out → 5:In1; 5:Out1 → 10:In2 |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 27 | `mq025_03_arroyo.scene` | 100: Journal; 27:mq025_03_fight → 14:Succeeded; 27:fight prep → 22:In1; 100:Out → 27:mq025_03_start_in |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 28 | `mq025_03_arroyo.scene` | 16: Journal; 16:Out → 28:mq025_03_after_in; 28:mq025_03_fight → 17:In1; 28:mq025_03_after_out → 18:Succeeded; 28:fight prep → 22:In1; 28:mq025_03_after_out_fight → 40:Succeeded |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 46 | `mq025_03_arroyo.scene` | 48: PauseCondition: {"seconds": 5}; 48:Out → 46:mq025_03_post_in; 46:mq025_03_after_out_fight → 71:In1 |
| `base\quest\main_quests\prologue\q001\q001.quest` / h0 / 100 | `mq025_psycho_brawl.questphase` | 101: PauseCondition: q001_left_v_apartment GreaterOrEqual 1; 101:Out → 100:In1 |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 28 | `mq025_psycho_brawl.questphase` | 170: Condition: mq025_done GreaterOrEqual 1; 177: Input; 206: Input; 170:False → 28:In1; 177:Out → 28:EP1_Standalone; 206:Out → 28:retro_finale_message |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.quest` / h0 / 2 | `mq025_psycho_brawl.questphase` | 3: Scene: mq025_00_setup.scene; 6: TimeManager; 2:Out1 → 1:In; 3:End 0 → 2:In1; 6:Out → 2:finale |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq025_03_arroyo.scene` | mq025_03_bottles_in, mq025_03_start_in, mq025_03_after_in, mq025_03_post_in, mq025_03_loot_in → mq025_03_bottles_out, fight prep, mq025_03_fight, Cleanup, mq025_03_after_out, mq025_03_after_out_fight, mq025_03_post_out, mq025_03_loot_out | Buck; crowd_01; crowd_02; crowd_03; 6th; mq025_arroyo_vehicle; V; 105 nodes / 117 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq025_03_arroyo.scene / n8 / 0` | Got a fight here. (`Fight`) | No option-level predicate stored | 0:0 → 97:0:0 |
| `mq025_03_arroyo.scene / n10 / 0` | I accept your offer. (`Bet`) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "171680378119"}}}} | 0:0 → 13:0:0 |
| `mq025_03_arroyo.scene / n10 / 1` | Toss in your sniper rifle. (`Boo`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq025_boo_bet"}}, "bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "174892807554"}}}} | 0:1 → 14:0:0 |
| `mq025_03_arroyo.scene / n10 / 2` | Maybe later. (`No`) | No option-level predicate stored | 0:2 → 11:0:0 |
| `mq025_03_arroyo.scene / n10 / 3` | Nice rifle. (`Weapon`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "125442197402", "buildId": "75476658533", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:3 → 40:0:0 |
| `mq025_03_arroyo.scene / n37 / 0` | [Start fight] Let's do this. (`Ready`) | No option-level predicate stored | 0:0 → 638:0:1 |
| `mq025_03_arroyo.scene / n137 / 0` | That's right, I am. (`yes i do`) | No option-level predicate stored | 0:0 → 141:0:0 |
| `mq025_03_arroyo.scene / n137 / 1` | Relax. Just a sport. (`nope`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "125442197402", "buildId": "74910219395", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:1 → 139:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `glossary_6thstreet` | mq025_03_arroyo.questphase / h0 / 104 | No reader in selected context |
| `mq025_03_arroyo_active` | mq025_03_arroyo.questphase / h0 / 5; mq025_03_arroyo.questphase / h0 / 50 | No reader in selected context |
| `mq025_03_chosen` | Producer outside selected context | mq025_03_arroyo.questphase / h0 / 34 |
| `mq025_03_fight_active` | mq025_03_arroyo.questphase / h56 / 33; mq025_03_arroyo.questphase / h56 / 34 | mq025_03_arroyo.questphase / h1338 / 10; mq025_03_arroyo.questphase / h1382 / 9 |
| `mq025_03_fight_started` | mq025_03_arroyo.questphase / h56 / 17 | mq025_03_arroyo.scene / scene / 505; mq025_03_arroyo.scene / scene / 517 |
| `mq025_03_first_time` | mq025_03_arroyo.scene / scene / 477 | mq025_03_arroyo.scene / scene / 480 |
| `mq025_03_player_wins` | mq025_03_arroyo.questphase / h56 / 10 | mq025_03_arroyo.scene / scene / 25 |
| `mq025_boo_bet` | mq025_03_arroyo.scene / scene / 106; mq025_03_arroyo.scene / scene / 110; mq025_03_arroyo.scene / scene / 113 | mq025_03_arroyo.scene / scene / 10; mq025_03_arroyo.scene / scene / 109; mq025_03_arroyo.scene / scene / 120 |
| `mq025_buck_dead` | mq025_03_arroyo.questphase / h0 / 63 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>68 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq025_03_arroyo.questphase / h0 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq025_tr_03_start"}}` | 75:Out → 7:In; 7:Out → 86:In; 7:Out → 92:Inactive |
| `mq025_03_arroyo.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq025_tr_03_leave"}}` | 43:Out → 20:In; 20:Out → 31:In |
| `mq025_03_arroyo.questphase / h0 / 34` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq025_03_chosen"}}}` | 34:False → 3:Active; 34:True → 67:Active |
| `mq025_03_arroyo.questphase / h0 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq025_tr_03_leave"}}` | 39:Out → 24:In; 99:Out → 39:In; 39:Out → 82:In1 |
| `mq025_03_arroyo.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 43:Out → 2:In; 43:Out → 20:In; 56:Out → 43:In; 57:Out → 43:In; 43:Out → 44:In2 |
| `mq025_03_arroyo.questphase / h0 / 44` | `questLogicalAndNodeDefinition` `{}` | 43:Out → 44:In2; 50:Out → 44:In1; 44:Out1 → 45:In |
| `mq025_03_arroyo.questphase / h0 / 48` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 19:Out → 48:In; 48:Out → 46:mq025_03_post_in |
| `mq025_03_arroyo.questphase / h0 / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["buck"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 62:Out → 55:In; 55:Out → 70:In |
| `mq025_03_arroyo.questphase / h0 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 59:Out → 58:Active; 63:Out → 59:In |
| `mq025_03_arroyo.questphase / h0 / 72` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 19:Out → 72:In; 72:Out → 57:Active |
| `mq025_03_arroyo.questphase / h0 / 73` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 29:Out1 → 73:In; 73:Out → 56:Active |
| `mq025_03_arroyo.questphase / h0 / 80` | `questCutControlNodeDefinition` `{"permanent":true}` | 41:Out → 80:In; 80:Out → 83:In; 80:CutSource → 82:CutDestination |
| `mq025_03_arroyo.questphase / h0 / 87` | `questCutControlNodeDefinition` `{"permanent":true}` | 51:Out → 87:In; 87:CutSource → 82:CutDestination; 87:Out → 93:In |
| `mq025_03_arroyo.questphase / h0 / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 83:Out → 96:In; 96:Out → 94:In |
| `mq025_03_arroyo.questphase / h0 / 101` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq025_03_arroyo/arroyo/03_arroyo_fight","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 92:Out → 101:In; 101:True → 103:Succeeded; 101:False → 102:In |
| `mq025_03_arroyo.questphase / h0 / 102` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq025_psycho_brawl/find_fights/fin_arroyo","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 102:True → 12:Succeeded; 102:False → 13:Active; 101:False → 102:In; 103:Out → 102:In |
| `mq025_03_arroyo.questphase / h56 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHealth_ConditionType","percent":15.0,"comparisonType":"LessOrEqual"}}}` | 3:Out → 8:In; 9:CutSource → 8:CutDestination; 8:Out → 19:Failed |
| `mq025_03_arroyo.questphase / h56 / 9` | `questCutControlNodeDefinition` `{}` | 9:CutSource → 6:CutDestination; 9:CutSource → 8:CutDestination; 19:Out → 9:In; 18:Out → 9:In; 9:Out → 24:In; 9:CutSource → 35:CutDestination |
| `mq025_03_arroyo.questphase / h56 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["buck"]},"statusEffectID":"BaseStatusEffect.DefeatedWithRecover"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["buck"]},"statusEffectID":"BaseStatusEffect.Defeated"}}]}}` | 3:Out → 35:In; 9:CutSource → 35:CutDestination; 35:Out → 50:In |
| `mq025_03_arroyo.questphase / h56 / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 54:Out → 53:In; 53:Out → 59:In |
| `mq025_03_arroyo.questphase / h56 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 11:Out → 62:In; 62:Out → 13:In |
| `mq025_03_arroyo.questphase / h433 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 0:Out → 3:In; 3:Out → 10:In |
| `mq025_03_arroyo.questphase / h540 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["buck"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 2:Out → 4:In; 4:Out → 42:In |
| `mq025_03_arroyo.questphase / h540 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["6th_street"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 3:Out → 5:In; 5:Out → 6:In2 |
| `mq025_03_arroyo.questphase / h540 / 6` | `questLogicalAndNodeDefinition` `{"inputSocketCount":5}` | 5:Out → 6:In2; 42:Out → 6:In1; 15:Out → 6:In3; 17:Out → 6:In4; 19:Out → 6:In5; 6:Out1 → 11:In1 |
| `mq025_03_arroyo.questphase / h540 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq025_tr_03_leave"}}` | 0:Out → 10:In; 10:Out → 11:In2 |
| `mq025_03_arroyo.questphase / h540 / 11` | `questLogicalXorNodeDefinition` `{}` | 11:Out1 → 1:In; 6:Out1 → 11:In1; 10:Out → 11:In2 |
| `mq025_03_arroyo.questphase / h540 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["crowd_01"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 15:Out → 6:In3; 12:Out → 15:In |
| `mq025_03_arroyo.questphase / h540 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["crowd_02"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 17:Out → 6:In4; 13:Out → 17:In |
| `mq025_03_arroyo.questphase / h540 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["crowd_03"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 19:Out → 6:In5; 14:Out → 19:In |
| `mq025_03_arroyo.questphase / h1048 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["buck"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 2:Out → 4:In; 4:Out → 6:In1 |
| `mq025_03_arroyo.questphase / h1048 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["6th_street"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 3:Out → 5:In; 5:Out → 6:In2 |
| `mq025_03_arroyo.questphase / h1048 / 6` | `questLogicalAndNodeDefinition` `{"inputSocketCount":5}` | 4:Out → 6:In1; 5:Out → 6:In2; 15:Out → 6:In3; 17:Out → 6:In4; 19:Out → 6:In5; 6:Out1 → 11:In1 |
| `mq025_03_arroyo.questphase / h1048 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq025_tr_03_leave"}}` | 0:Out → 10:In; 10:Out → 11:In2 |
| `mq025_03_arroyo.questphase / h1048 / 11` | `questLogicalXorNodeDefinition` `{}` | 11:Out1 → 1:In; 6:Out1 → 11:In1; 10:Out → 11:In2 |
| `mq025_03_arroyo.questphase / h1048 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["crowd_01"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 15:Out → 6:In3; 12:Out → 15:In |
| `mq025_03_arroyo.questphase / h1048 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["crowd_02"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 17:Out → 6:In4; 13:Out → 17:In |
| `mq025_03_arroyo.questphase / h1048 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["crowd_03"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 19:Out → 6:In5; 14:Out → 19:In |
| `mq025_03_arroyo.questphase / h1325 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 2:Out1 → 4:In; 4:Out → 3:In1 |
| `mq025_03_arroyo.questphase / h1325 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 5:Out → 2:In1; 3:Out1 → 5:In |
| `mq025_03_arroyo.questphase / h1325 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq025_tr_03_t2"}}` | 7:Out → 6:In; 6:Out → 8:In |
| `mq025_03_arroyo.questphase / h1325 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 0:Out → 7:In; 7:Out → 6:In; 11:Out → 7:In |
| `mq025_03_arroyo.questphase / h1325 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq025_tr_03_t2"}}` | 10:Out → 9:In; 9:Out → 11:In |
| `mq025_03_arroyo.questphase / h1325 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 8:Out → 10:In; 10:Out → 9:In |
| `mq025_03_arroyo.questphase / h1338 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 7:Out → 5:In; 5:Out → 10:In |
| `mq025_03_arroyo.questphase / h1338 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq025_tr_03_t2"}}` | 0:Out → 8:In; 8:Out → 7:In |
| `mq025_03_arroyo.questphase / h1338 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"XOR","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq025_tr_03_t2"},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq025_03_fight_active"}}]}}` | 10:Out → 1:In; 5:Out → 10:In |
| `mq025_03_arroyo.questphase / h1382 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 6:Out → 5:In; 5:Out → 9:In |
| `mq025_03_arroyo.questphase / h1382 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#mq025_tr_03_t2"},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq025_03_fight_active","comparisonType":"Equal"}}]}}` | 9:Out → 1:In; 5:Out → 9:In |
| `mq025_03_arroyo.scene / scene / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 11:0:0 → 12:0:1; 12:0:0 → 10:0:0 |
| `mq025_03_arroyo.scene / scene / 25` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq025_03_player_wins"}}}` | 24:0:0 → 25:0:1; 25:0:0 → 133:0:0; 25:0:1 → 28:0:0; 25:0:1 → 588:0:1 |
| `mq025_03_arroyo.scene / scene / 109` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq025_boo_bet","value":2,"comparisonType":"GreaterOrEqual"}}}` | 28:0:0 → 109:0:1; 109:0:0 → 113:0:1; 109:0:1 → 10:0:0 |
| `mq025_03_arroyo.scene / scene / 120` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq025_boo_bet","value":2,"comparisonType":"GreaterOrEqual"}}}` | 120:0:0 → 541:0:1; 120:0:0 → 598:0:1; 120:0:1 → 536:0:1; 120:0:1 → 601:0:1; 133:0:0 → 120:0:1 |
| `mq025_03_arroyo.scene / scene / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 149:0:0 → 8:0:0; 302:0:0 → 149:0:1 |
| `mq025_03_arroyo.scene / scene / 480` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq025_03_first_time","value":1,"comparisonType":"Equal"}}}` | 477:0:0 → 480:0:1; 480:0:0 → 466:0:0 |
| `mq025_03_arroyo.scene / scene / 488` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["buck"]},"timeInterval":0.10000000149011612,"onScreenTest":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["crowd_01"]},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["crowd_03"]},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}}]}}` | 488:0:0 → 497:0:1; 514:0:0 → 488:0:1 |
| `mq025_03_arroyo.scene / scene / 505` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq025_03_fight_started"}}}` | 21:0:0 → 505:0:1; 505:0:0 → 15:0:0; 505:0:1 → 500:0:0 |
| `mq025_03_arroyo.scene / scene / 514` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq025_tr_03_fight_start"}}` | 500:3:0 → 514:0:1; 514:0:0 → 488:0:1 |
| `mq025_03_arroyo.scene / scene / 517` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq025_03_fight_started"}}}` | 38:0:0 → 517:0:1; 517:0:0 → 554:0:1; 517:0:1 → 492:0:0 |
| `mq025_03_arroyo.scene / scene / 572` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":600}}}` | 541:0:0 → 572:0:1; 572:0:0 → 553:0:1; 572:0:0 → 648:0:0 |
| `mq025_03_arroyo.scene / scene / 573` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":600}}}` | 536:0:0 → 573:0:1; 573:0:0 → 562:0:1; 573:0:0 → 648:0:0 |
| `mq025_03_arroyo.scene / scene / 598` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 120:0:0 → 598:0:1; 598:0:0 → 27:0:0 |
| `mq025_03_arroyo.scene / scene / 601` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 120:0:1 → 601:0:1; 601:0:0 → 124:0:0 |
| `mq025_03_arroyo.scene / scene / 629` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":700}}}` | 97:1:0 → 629:0:1; 629:0:0 → 6:1:0 |
| `mq025_03_arroyo.scene / scene / 638` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq025_tr_03_fight_start"}}` | 37:0:0 → 638:0:1; 638:0:0 → 612:0:1 |
| `mq025_03_arroyo.scene / scene / 642` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq025_tr_03_fight_start","activatorRef":{"$type":"gameEntityReference","reference":"#mq025_com_buck","names":["buck"]},"isPlayerActivator":false}}` | 15:0:0 → 642:0:1; 642:0:0 → 37:0:0 |
| `mq025_03_arroyo.scene / scene / 652` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq025_tr_03_fight_start"}}` | 490:0:0 → 652:0:1; 652:0:0 → 615:0:1 |
| `mq025_03_arroyo.scene / scene / 657` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 620:0:0 → 657:0:1; 657:0:0 → 15:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq025_03_arroyo.questphase / h0 / 55 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq025_03_arroyo.scene / scene / 29; mq025_03_arroyo.scene / scene / 471; mq025_03_arroyo.scene / scene / 620 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | mq025_03_arroyo.questphase / h0 / 98 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq025_03_arroyo.scene / scene / 10; mq025_03_arroyo.scene / scene / 137; mq025_03_arroyo.scene / scene / 37; mq025_03_arroyo.scene / scene / 8 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq025_03_arroyo.questphase / h1048 / 16; mq025_03_arroyo.questphase / h1048 / 18; mq025_03_arroyo.questphase / h1048 / 20; mq025_03_arroyo.questphase / h1048 / 7; +7 locations in catalogue.json | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq025_03_arroyo.questphase / h0 / 23; mq025_03_arroyo.questphase / h0 / 30; mq025_03_arroyo.questphase / h433 / 10; mq025_03_arroyo.questphase / h433 / 8; +5 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq025_03_arroyo.questphase / h0 / 34; mq025_03_arroyo.questphase / h1338 / 10; mq025_03_arroyo.questphase / h1382 / 9; mq025_03_arroyo.scene / scene / 10; +6 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq025_03_arroyo.questphase / h0 / 45; mq025_03_arroyo.questphase / h0 / 93; mq025_03_arroyo.questphase / h0 / 94; mq025_03_arroyo.questphase / h1325 / 11; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `journal_transition` | mq025_03_arroyo.questphase / h0 / 100; mq025_03_arroyo.questphase / h0 / 103; mq025_03_arroyo.questphase / h0 / 12; mq025_03_arroyo.questphase / h0 / 13; +22 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `loot_binding` | mq025_03_arroyo.questphase / h540 / 42 | spawned target + item record + operation → loot injection dispatched. Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately. |
| `parallel_join` | mq025_03_arroyo.questphase / h0 / 44; mq025_03_arroyo.questphase / h1048 / 6; mq025_03_arroyo.questphase / h540 / 6 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq025_03_arroyo.questphase / h0 / 104; mq025_03_arroyo.questphase / h0 / 5; mq025_03_arroyo.questphase / h0 / 50; mq025_03_arroyo.questphase / h0 / 63; +8 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq025_03_arroyo.questphase / h1048 / 11; mq025_03_arroyo.questphase / h540 / 11 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq025_03_arroyo.questphase / h0 / 43; mq025_03_arroyo.questphase / h0 / 48; mq025_03_arroyo.questphase / h0 / 59; mq025_03_arroyo.questphase / h0 / 72; +19 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq025_03_arroyo.questphase / h0 / 80; mq025_03_arroyo.questphase / h0 / 87; mq025_03_arroyo.questphase / h56 / 9 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq025_03_arroyo.questphase / h0 / 64; mq025_03_arroyo.scene / scene / 298 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq025_03_arroyo.questphase / h0 / 27; mq025_03_arroyo.questphase / h0 / 28; mq025_03_arroyo.questphase / h0 / 46 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq025_03_arroyo.questphase / h0 / 20; mq025_03_arroyo.questphase / h0 / 39; mq025_03_arroyo.questphase / h0 / 7; mq025_03_arroyo.questphase / h1048 / 10; +10 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | mq025_03_arroyo.questphase / h1048 / 15; mq025_03_arroyo.questphase / h1048 / 17; mq025_03_arroyo.questphase / h1048 / 19; mq025_03_arroyo.questphase / h1048 / 4; +6 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mq025_03_arroyo.questphase / h0 / 86; mq025_03_arroyo.questphase / h0 / 89; mq025_03_arroyo.questphase / h0 / 90 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq025_03_arroyo.questphase / h0 / 97; mq025_03_arroyo.scene / scene / 187; mq025_03_arroyo.scene / scene / 204; mq025_03_arroyo.scene / scene / 271; +11 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mq025_03_arroyo.questphase / h56 / 15; mq025_03_arroyo.scene / scene / 612; mq025_03_arroyo.scene / scene / 615 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` | content candidate; journal anchor | `base-mq025` |
| `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` | content candidate; forward dependency | `base-mq025` |

Evidence shards for this dossier (including parent context): [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

172 repeated typed/socket path signatures in this selected graph context; 17 distinct direct resource identities; 7 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `8cd3b647ae3f592ad947` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` / scene / 101 -> 102 -> 104 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `7e7dbbc930b3717fd790` | `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 12 -> 13 -> 100 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `6b3e5fe15b7a64a01e21` | `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h56 / 17 -> 33 -> 63 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questDeletionMarkerNodeDefinition; Out -> In; Out -> In |
| `1cf9adcdd8714d9f07e3` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` / scene / 471 -> 473 -> 475 | questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `bd44fd6ebe28bd80c073` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` / scene / 466 -> 471 -> 473 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 3:0 -> 0:1; 0:0 -> 0:0 |
| `c11cf4b8fc2f0bbc6f96` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` / scene / 459 -> 454 -> 456 | scnCutControlNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId]; 1:0 -> 1:0; 0:0 -> 0:0 |
| `d18fd8da12f6125e7cd7` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` / scene / 9 -> 454 -> 456 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnHubNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `58c8902cfee139a52219` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` / scene / 505 -> 500 -> 501 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]; 0:1 -> 0:0; 4:0 -> 0:1 |
| `2c539f3df79a1ae20133` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` / scene / 24 -> 25 -> 28 | scnStartNode[scnNodeId] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:1 -> 0:0 |
| `d1644ddcb9c01c24628b` | `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` / scene / 477 -> 480 -> 466 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `4e7757b259f5b870990d` | `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h540 / 0 -> 10 -> 11 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questTriggerCondition] -> questLogicalXorNodeDefinition; Out -> In; Out -> In2 |
| `e5b8d4056ed43c4cbe71` | `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 34 -> 67 -> 68 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; True -> Active; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 11 | `h56` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 22 | `h433` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 29 | `h540` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 71 | `h1048` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h0 / 82 | `h1325` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h1325 / 2 | `h1338` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq025\phases\mq025_03_arroyo.questphase` / h1325 / 3 | `h1382` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.gamedef` | content candidate | base\quest\minor_quests\mq025\mq025_psycho_brawl.quest |
| `base\quest\main_quests\prologue\q001\q001.gamedef` | content candidate | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q001\test\q001_miss0_mark_world.gamedef` | test/debug | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_kabuki.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_kabuki.quest |
| `base\quest\demos\handson_2020\handson_2020_little_china.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_little_china.quest |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_speed_test.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_speed_test.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_hip__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_wall_lean270__rh_on_hip__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__stand__2h_phone__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\minor_quests\mq025\scenes\lipsync\en\mq025_03_arroyo\gang_6th_m_05_afam_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq025\scenes\lipsync\en\mq025_03_arroyo\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\archetype\corpo\corpo__stand_ground__look_at_products__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__look_at_products__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__nervous__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_cellphone__record__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `glossary_6thstreet` | base\quest\main_quests\part1\q103\phases\q103_05_roadhouse.questphase / h0 / 88; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h5744 / 118; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arroyo.questphase / h4344 / 66; base\open_world\street_stories\westbrook\charter_hill\sts_wbr_charter_hill.questphase / h2885 / 173; 7 total source locations in compressed evidence |
| `mq025_03_chosen` | base\quest\minor_quests\mq025\scenes\mq025_00_setup.scene / scene / 126; 1 total source locations in compressed evidence |
| `mq025_03_player_wins` | ep1\quest\test\ep1_chicken_test.scene / scene / 337; ep1\quest\test\ep1_chicken_test.scene / scene / 341; ep1\quest\test\ep1_chicken_test.scene / scene / 345; ep1\quest\test\ep1_chicken_test.scene / scene / 351; 4 total source locations in compressed evidence |
| `mq025_buck_dead` | ep1\quest\test\ep1_chicken_test.scene / scene / 339; ep1\quest\test\ep1_chicken_test.scene / scene / 343; ep1\quest\test\ep1_chicken_test.scene / scene / 347; ep1\quest\test\ep1_chicken_test.scene / scene / 349; 4 total source locations in compressed evidence |

NodeRef uses: 210; TweakDB binding uses: 46. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene` | 25 / 180 | scnChangeIdleAnimEvent: 16; scnDialogLineEvent: 46; scnGameplayTransitionEvent: 2; scnIKEvent: 4; scnLookAtEvent: 30; scnPlaySkAnimEvent: 60; scnUnmountEvent: 2; scneventsEquipItemToPerformer: 2; scneventsSetAnimFeatureEvent: 2; scneventsSocket: 16 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
