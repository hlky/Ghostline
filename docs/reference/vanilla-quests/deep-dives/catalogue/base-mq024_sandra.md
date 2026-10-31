# Full Disclosure

Journal: `quests/minor_quest/mq024_sandra` · `MinorQuest` · hash `1278009373`.

**Coverage: journal-linked.** 27 exact journal-linked nodes in 8 resources; 10 resources in the inspected dependency context.

Resource roles in that context: 8 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Find Sandra's databank. (Primary) | `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier` |
| Sandra Dorsett who we rescued from scavengers called V and asked to find and retrieve her data carrier. (Primary) | `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra` |
| Meet with Sandra. (Primary) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` |
| Defeat Sandra. (Primary) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq024_quest_bugfixes.questphase / h98 / 5` (Condition) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 11:True → 5:In; 5:True → 12:In |
| `mq024_quest_bugfixes.questphase / h98 / 7` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 12:Out → 7:Succeeded; 7:Out → 8:Succeeded |
| `mq024_quest_bugfixes.questphase / h98 / 8` (Journal) | `quests/minor_quest/mq024_sandra` | 7:Out → 8:Succeeded; 8:Out → 9:In |
| `mq024.questphase / h0 / 14` (Journal) | `quests/minor_quest/mq024_sandra/description` | 14:Out → 3:In1; 5:False → 14:Active |
| `mq024.questphase / h0 / 15` (Journal) | `quests/minor_quest/mq024_sandra/description` | 15:Out → 4:In1; 5:True → 15:Active |
| `mq024_02_scavengers.questphase / h0 / 2` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier` | 0:Out → 2:Active; 2:Out → 3:In |
| `mq024_02_scavengers.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier` | 3:Out → 4:Succeeded; 4:Out → 5:In |
| `mq024_03_sandra_apartment.questphase / h0 / 2` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra` | 17:Out → 2:Active; 2:Out → 3:In; 2:Out → 72:Active |
| `mq024_03_sandra_apartment.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra` | 4:Out → 8:Succeeded; 8:Out → 9:Active |
| `mq024_03_sandra_apartment.questphase / h0 / 9` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` | 8:Out → 9:Active; 9:Out → 18:In |
| `mq024_03_sandra_apartment.questphase / h0 / 11` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` | 11:Out → 1:In; 30:False → 11:Succeeded; 11:Out → 62:In |
| `mq024_03_sandra_apartment.questphase / h0 / 49` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 55:False → 49:Active; 49:Out → 52:In |
| `mq024_03_sandra_apartment.questphase / h0 / 50` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 52:Out → 50:Succeeded; 50:Out → 56:In1 |
| `mq024_03_sandra_apartment.questphase / h0 / 57` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` | 57:Out → 54:In; 61:False → 57:Failed |
| `mq024_03_sandra_apartment.questphase / h0 / 72` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra/sandra` | 2:Out → 72:Active |
| `mq024_cleanup.questphase / h0 / 2` (Journal) | `quests/minor_quest/mq024_sandra` | 4:Out → 2:Succeeded; 2:Out → 7:In |
| `mq024_cleanup.questphase / h0 / 24` (Condition) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 24:False → 1:In; 10:True → 24:In; 19:Out1 → 24:In; 24:True → 26:In |
| `mq024_cleanup.questphase / h0 / 25` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 26:Out → 25:Succeeded; 25:Out → 29:In |
| `mq024_02_meet_sandra.scene / scene / 390` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra` | 390:0:0 → 396:0:1; 391:0:0 → 390:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq024_02_meet_sandra.scene / scene / 396` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 390:0:0 → 396:0:1; 396:0:0 → 395:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq024_02_meet_sandra.scene / scene / 397` (Journal) | `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra` | 397:0:0 → 2:0:0; 440:0:0 → 397:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq024_02_meet_sandra.scene / scene / 443` (MappinManager) | `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra/sandra_mp` | 265:0:0 → 443:0:1; 443:0:0 → 53:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq024_02_meet_sandra.scene / scene / 542` (Journal) | `quests/minor_quest/mq024_sandra` | 529:1:0 → 542:0:0; 539:0:0 → 542:0:4; 542:0:0 → 527:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `ep1_standalone_quest_bugfixing.questphase / h77 / 29` (Journal) | `quests/minor_quest/mq024_sandra` | 28:Out → 29:Succeeded; 29:Out → 31:Succeeded |
| `ep1_standalone_quest_bugfixing.questphase / h372 / 59` (Journal) | `quests/minor_quest/mq024_sandra/description` | 28:Out → 59:Active; 59:Out → 65:Active |
| `ep1.questphase / h3753 / 29` (Journal) | `quests/minor_quest/mq024_sandra` | 28:Out → 29:Succeeded; 29:Out → 64:Succeeded |
| `ep1.questphase / h4048 / 29` (Journal) | `quests/minor_quest/mq024_sandra/description` | 28:Out → 29:Active; 29:Out → 43:Active |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq024.questphase / h0 / 2` | `base\quest\minor_quests\mq024\phases\mq024_01_hook.questphase` | 17:Out1 → 2:In1; 2:Out1 → 5:In; 2:Out1 → 8:In |
| `mq024.questphase / h0 / 3` | `base\quest\minor_quests\mq024\phases\mq024_02_scavengers.questphase` | 14:Out → 3:In1; 3:Out1 → 4:In1 |
| `mq024.questphase / h0 / 4` | `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` | 3:Out1 → 4:In1; 4:Out1 → 10:In1; 9:Out → 4:In1; 15:Out → 4:In1; 4:Out_door → 10:In_door |
| `mq024.questphase / h0 / 10` | `base\quest\minor_quests\mq024\phases\mq024_cleanup.questphase` | 10:Out1 → 1:In; 4:Out1 → 10:In1; 4:Out_door → 10:In_door |
| `mq024_03_sandra_apartment.questphase / h0 / 5` | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene`; `#mq024_01_sm_call_sandra` | 3:Out → 5:Start 0; 5:End 0 → 4:In; 5:Holocall INT → 41:In; 5:Holocall RET → 40:In |
| `mq024_03_sandra_apartment.questphase / h0 / 10` | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene`; `#mq024_02_sm_meet_sandra` | 54:CutSource → 10:CutDestination; 18:Out → 10:Start 0; 10:End 0 → 30:In; 10:End_killed_door → 74:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 9 | `mq024.questphase` | 172: Condition: mq024_done GreaterOrEqual 1; 172:False → 9:In1 |
| `base\quest\minor_quests\mq024\mq024.questphase` / h0 / 2 | `mq024_01_hook.questphase` | 17: LogicalAnd; 17:Out1 → 2:In1; 2:Out1 → 5:In; 2:Out1 → 8:In |
| `base\quest\minor_quests\mq024\mq024.questphase` / h0 / 3 | `mq024_02_scavengers.questphase` | 14: Journal; 14:Out → 3:In1; 3:Out1 → 4:In1 |
| `base\quest\minor_quests\mq024\mq024.questphase` / h0 / 4 | `mq024_03_sandra_apartment.questphase` | 3: Phase: mq024_02_scavengers.questphase; 9: Input; 15: Journal; 3:Out1 → 4:In1; 4:Out1 → 10:In1; 9:Out → 4:In1; 15:Out → 4:In1; 4:Out_door → 10:In_door |
| `base\quest\minor_quests\mq024\mq024.questphase` / h0 / 10 | `mq024_cleanup.questphase` | 4: Phase: mq024_03_sandra_apartment.questphase; 4: Phase: mq024_03_sandra_apartment.questphase; 10:Out1 → 1:In; 4:Out1 → 10:In1; 4:Out_door → 10:In_door |
| `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` / h0 / 5 | `mq024_01_call_sandra.scene` | 3: PauseCondition; 3:Out → 5:Start 0; 5:End 0 → 4:In; 5:Holocall INT → 41:In; 5:Holocall RET → 40:In |
| `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` / h0 / 10 | `mq024_02_meet_sandra.scene` | 54: CutControl; 18: PauseCondition; 54:CutSource → 10:CutDestination; 18:Out → 10:Start 0; 10:End 0 → 30:In; 10:End_killed_door → 74:In |
| `ep1\quest\ep1_bugfixing.questphase` / h0 / 7 | `ep1_standalone_quest_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 7:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `ep1\quest\ep1.questphase` / h58 / 2 | `ep1_bugfixing.questphase` | 25: LogicalXor; 2:CP77-65722_out → 27:In; 2:CP77-64292_out → 26:In; 25:Out1 → 2:In1; 2:Out1 → 4:In2; 2:growl → 4:growl |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq024_01_call_sandra.scene` | Start 0 → End 0 | sandra; Player; 23 nodes / 26 edges |
| `mq024_02_meet_sandra.scene` | Start 0, prev_cross, prev_good_normal → End 0, End_killed_door | sandra; Player; 132 nodes / 152 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq024_01_call_sandra.scene / n6 / 0` | Yep. (``) | No option-level predicate stored | 0:0 → 8:0:0 |
| `mq024_01_call_sandra.scene / n6 / 1` | Glad you're holding up. (``) | No option-level predicate stored | 0:1 → 23:0:0 |
| `mq024_01_call_sandra.scene / n11 / 0` | You're safe now. (``) | No option-level predicate stored | 0:0 → 13:0:0 |
| `mq024_01_call_sandra.scene / n11 / 1` | I don't think I'm the right person to talk to... (``) | No option-level predicate stored | 0:1 → 14:0:0 |
| `mq024_01_call_sandra.scene / n26 / 0` | Sure thing. (``) | No option-level predicate stored | 0:0 → 28:0:0 |
| `mq024_01_call_sandra.scene / n26 / 1` | Jackie's dead. (``) | No option-level predicate stored | 0:1 → 29:0:0 |
| `mq024_02_meet_sandra.scene / n8 / 0` | [Hand over databank] Got it right here. (`give`) | No option-level predicate stored | 0:0 → 10:0:0; 0:0 → 115:1:0; 0:0 → 120:1:0; 0:0 → 121:1:0; 0:0 → 507:0:1 |
| `mq024_02_meet_sandra.scene / n8 / 1` | What are you worried about? (`Option`) | No option-level predicate stored | 0:1 → 90:0:0 |
| `mq024_02_meet_sandra.scene / n12 / 0` | Of course not. (`no`) | No option-level predicate stored | 0:0 → 14:0:1 |
| `mq024_02_meet_sandra.scene / n12 / 1` | Yes, I did. (`yes`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq024_hacked_data_carrier", "value": 1, "comparisonType": "GreaterOrEqual"}}} | 0:1 → 43:0:1 |
| `mq024_02_meet_sandra.scene / n18 / 0` | It couldn't have been me. (`still lie`) | No option-level predicate stored | 0:0 → 20:0:0 |
| `mq024_02_meet_sandra.scene / n18 / 1` | Alright, you got me. (`admit`) | No option-level predicate stored | 0:1 → 23:0:0 |
| `mq024_02_meet_sandra.scene / n25 / 0` | I wanna congratulate you. (`good job`) | No option-level predicate stored | 0:0 → 27:0:0 |
| `mq024_02_meet_sandra.scene / n25 / 1` | Blackmail you, of course. (`blackmail`) | No option-level predicate stored | 0:1 → 37:0:0 |
| `mq024_02_meet_sandra.scene / n25 / 2` | Nothing. (`dont care`) | No option-level predicate stored | 0:2 → 480:0:1 |
| `mq024_02_meet_sandra.scene / n29 / 0` | What daemons did you use? (`blueline`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "125694326540", "buildId": "95189197130", "difficulty": "MEDIUM", "comparisonType": "CO_GreaterEq"}}}} | 0:0 → 492:0:1 |
| `mq024_02_meet_sandra.scene / n29 / 1` | What they're doing... how's it even possible? (`continue`) | No option-level predicate stored | 0:1 → 487:0:1 |
| `mq024_02_meet_sandra.scene / n49 / 0` | [Knock] (`knock`) | No option-level predicate stored | 0:0 → 66:0:1; 0:0 → 110:0:0 |
| `mq024_02_meet_sandra.scene / n94 / 0` | How much for keeping my mouth shut? (`Option_01`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "128271491759", "buildId": "74910219395", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:0 → 93:0:0; 0:0 → 435:0:1 |
| `mq024_02_meet_sandra.scene / n94 / 1` | I was just kidding. (`Option_02`) | No option-level predicate stored | 0:1 → 483:0:1 |
| `mq024_02_meet_sandra.scene / n115 / 0` | You have good taste. (`compliment`) | No option-level predicate stored | 0:0 → 126:0:2 |
| `mq024_02_meet_sandra.scene / n120 / 0` | Cozy place. (`compliment`) | No option-level predicate stored | 0:0 → 126:0:1 |
| `mq024_02_meet_sandra.scene / n121 / 0` | Nice digs. (`compliment`) | No option-level predicate stored | 0:0 → 126:0:0 |
| `mq024_02_meet_sandra.scene / n200 / 0` | [Knock] Sandra? (`knock`) | No option-level predicate stored | 0:0 → 50:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CP77-48800` | mq024_quest_bugfixes.questphase / h37 / 3 | mq024_quest_bugfixes.questphase / h37 / 2 |
| `CP77-65021` | mq024_quest_bugfixes.questphase / h98 / 3 | mq024_quest_bugfixes.questphase / h98 / 2 |
| `CYB-12345` | mq024_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `codex_sandra_dorsett` | mq024_01_hook.questphase / h0 / 12; mq024_quest_bugfixes.questphase / h37 / 5 | mq024_quest_bugfixes.questphase / h37 / 4 |
| `holo_v_calls_sandra_dorsett_end_activate` | mq024_01_call_sandra.scene / scene / 117; mq024_03_sandra_apartment.questphase / h0 / 41 | No reader in selected context |
| `holo_v_calls_sandra_dorsett_end_done` | mq024_01_call_sandra.scene / scene / 112 | mq024_01_call_sandra.scene / scene / 111 |
| `holo_v_calls_sandra_dorsett_start_activate` | mq024_01_call_sandra.scene / scene / 116; mq024_03_sandra_apartment.questphase / h0 / 40 | No reader in selected context |
| `holo_v_calls_sandra_dorsett_start_done` | mq024_01_call_sandra.scene / scene / 110 | mq024_01_call_sandra.scene / scene / 109 |
| `kab_05_activated` | Producer outside selected context | mq024.questphase / h0 / 16 |
| `mq024_active` | mq024_01_hook.questphase / h0 / 9; mq024_cleanup.questphase / h0 / 3 | mq024_quest_bugfixes.questphase / h37 / 4 |
| `mq024_admit_that_looked` | mq024_02_meet_sandra.scene / scene / 43 | No reader in selected context |
| `mq024_combat_sandra` | mq024_02_meet_sandra.scene / scene / 416 | mq024_03_sandra_apartment.questphase / h0 / 30; mq024_03_sandra_apartment.questphase / h0 / 61; mq024_cleanup.questphase / h0 / 10 |
| `mq024_done` | mq024_cleanup.questphase / h0 / 4 | mq024_quest_bugfixes.questphase / h37 / 4; mq024_quest_bugfixes.questphase / h98 / 11 |
| `mq024_hacked_data_carrier` | Producer outside selected context | mq024_02_meet_sandra.scene / scene / 12; mq024_02_meet_sandra.scene / scene / 14; mq024_03_sandra_apartment.questphase / h0 / 13 |
| `mq024_hook_taken` | mq024.questphase / h0 / 8 | No reader in selected context |
| `mq024_sandra_opened_door` | mq024_02_meet_sandra.scene / scene / 469 | mq024_03_sandra_apartment.questphase / h0 / 44 |
| `q101_done` | Producer outside selected context | mq024.questphase / h0 / 13 |
| `q305_haunted_weapon_random_whisper_02` | mq024_03_sandra_apartment.questphase / h0 / 76 | No reader in selected context |
| `q305_haunted_weapon_random_whisper_02_used` | Producer outside selected context | mq024_03_sandra_apartment.questphase / h0 / 75 |
| `travelling_merchant_lives` | Producer outside selected context | mq024_quest_bugfixes.questphase / h0 / 15 |

## Exact gates, joins and cancellation

<details><summary>61 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq024_quest_bugfixes.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 17:Out1 → 15:In |
| `mq024_quest_bugfixes.questphase / h37 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-48800"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq024_quest_bugfixes.questphase / h37 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_active"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_done"}}]},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"codex_sandra_dorsett","value":1,"comparisonType":"Less"}}]}}` | 3:Out → 4:In; 4:True → 5:In |
| `mq024_quest_bugfixes.questphase / h98 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-65021"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `mq024_quest_bugfixes.questphase / h98 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 3:Out → 4:In; 4:Out → 11:In |
| `mq024_quest_bugfixes.questphase / h98 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 11:True → 5:In; 5:True → 12:In |
| `mq024_quest_bugfixes.questphase / h98 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"GreaterOrEqual"}}}` | 8:Out → 9:In; 9:Out → 10:In |
| `mq024_quest_bugfixes.questphase / h98 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_done"}}}` | 4:Out → 11:In; 11:True → 5:In |
| `mq024_quest_bugfixes.questphase / h98 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 5:True → 12:In; 12:Out → 7:Succeeded |
| `mq024.questphase / h0 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"134302024498","quantity":1}}}` | 2:Out1 → 5:In; 5:True → 15:Active; 5:False → 14:Active |
| `mq024.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 13:In; 13:Out → 17:In1 |
| `mq024.questphase / h0 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"kab_05_activated","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 16:In; 16:Out → 17:In2 |
| `mq024.questphase / h0 / 17` | `questLogicalAndNodeDefinition` `{}` | 17:Out1 → 2:In1; 13:Out → 17:In1; 16:Out → 17:In2 |
| `mq024_02_scavengers.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"134302024498","quantity":1}}}` | 2:Out → 3:In; 3:Out → 4:Succeeded |
| `mq024_03_sandra_apartment.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhone_ConditionType","caller":{"$type":"gameJournalPath","realPath":"contacts/player","fileEntryIndex":1,"className":"gameJournalContact"},"addressee":{"$type":"gameJournalPath","realPath":"contacts/sandra_dorsett","fileEntryIndex":1,"className":"gameJournalContact"}}}}` | 2:Out → 3:In; 3:Out → 5:Start 0 |
| `mq024_03_sandra_apartment.questphase / h0 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_hacked_data_carrier","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 13:In; 13:Out → 73:In; 13:Out → 77:In |
| `mq024_03_sandra_apartment.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"LessOrEqual"}}}` | 9:Out → 18:In; 18:Out → 10:Start 0; 18:Out → 35:In; 18:Out → 44:In |
| `mq024_03_sandra_apartment.questphase / h0 / 30` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_combat_sandra","value":1,"comparisonType":"GreaterOrEqual"}}}` | 30:True → 1:In; 10:End 0 → 30:In; 30:False → 11:Succeeded |
| `mq024_03_sandra_apartment.questphase / h0 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":100.0},"comparisonType":"GreaterOrEqual"}}}` | 35:Out → 36:In; 36:Out → 37:In |
| `mq024_03_sandra_apartment.questphase / h0 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0},"comparisonType":"LessOrEqual"}}}` | 38:Out → 35:In; 37:Out → 38:In |
| `mq024_03_sandra_apartment.questphase / h0 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterQuickHacked_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}}}}` | 44:Out → 42:In; 42:Out → 53:In1 |
| `mq024_03_sandra_apartment.questphase / h0 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType"}}}` | 44:Out → 43:In; 43:Out → 53:In2 |
| `mq024_03_sandra_apartment.questphase / h0 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_sandra_opened_door","value":1,"comparisonType":"GreaterOrEqual"}}}` | 18:Out → 44:In; 44:Out → 42:In; 44:Out → 43:In; 44:Out → 58:In; 44:Out → 60:In |
| `mq024_03_sandra_apartment.questphase / h0 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 49:Out → 52:In; 52:Out → 50:Succeeded |
| `mq024_03_sandra_apartment.questphase / h0 / 53` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 42:Out → 53:In1; 43:Out → 53:In2; 58:Out → 53:In3; 60:Out → 53:In4; 53:Out1 → 61:In; 53:Out1 → 65:In |
| `mq024_03_sandra_apartment.questphase / h0 / 54` | `questCutControlNodeDefinition` `{}` | 54:CutSource → 10:CutDestination; 54:Out → 45:In; 57:Out → 54:In |
| `mq024_03_sandra_apartment.questphase / h0 / 55` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 55:False → 49:Active; 67:Out → 55:In; 55:True → 56:In1 |
| `mq024_03_sandra_apartment.questphase / h0 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","slotName":"mq024_sandra"},"isPlayer":false}}}` | 44:Out → 58:In; 58:Out → 53:In3 |
| `mq024_03_sandra_apartment.questphase / h0 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 44:Out → 60:In; 60:Out → 53:In4 |
| `mq024_03_sandra_apartment.questphase / h0 / 61` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_combat_sandra","value":1,"comparisonType":"GreaterOrEqual"}}}` | 53:Out1 → 61:In; 61:False → 57:Failed |
| `mq024_03_sandra_apartment.questphase / h0 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 11:Out → 62:In; 62:Out → 63:In |
| `mq024_03_sandra_apartment.questphase / h0 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 4:Out → 68:In; 68:Out → 69:In |
| `mq024_03_sandra_apartment.questphase / h0 / 69` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 69:Out → 64:In; 68:Out → 69:In |
| `mq024_03_sandra_apartment.questphase / h0 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq024_sandras_turret","deviceControllerClass":"SecurityTurretControllerPS","deviceConditionFunction":"IsON"}}}` | 70:Out → 71:In |
| `mq024_03_sandra_apartment.questphase / h0 / 75` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q305_haunted_weapon_random_whisper_02_used"}}}` | 78:Out → 75:In; 75:False → 76:In |
| `mq024_03_sandra_apartment.questphase / h0 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questUICondition","type":{"$type":"questMenuState_ConditionType","state":"Closed"}}}` | 13:Out → 77:In; 77:Out → 78:In |
| `mq024_03_sandra_apartment.questphase / h0 / 78` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":100}}}` | 78:Out → 75:In; 77:Out → 78:In |
| `mq024_cleanup.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"GreaterOrEqual"}}}` | 5:Out → 8:In; 8:Out → 10:In |
| `mq024_cleanup.questphase / h0 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_combat_sandra","value":1,"comparisonType":"GreaterOrEqual"}}}` | 8:Out → 10:In; 10:True → 24:In; 10:False → 11:In |
| `mq024_cleanup.questphase / h0 / 18` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 11:Out → 18:In; 18:Out → 12:In; 18:Out → 19:In2 |
| `mq024_cleanup.questphase / h0 / 19` | `questLogicalAndNodeDefinition` `{}` | 16:Success → 19:In1; 18:Out → 19:In2; 19:Out1 → 24:In |
| `mq024_cleanup.questphase / h0 / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"GreaterOrEqual"}}}` | 21:Out → 22:In; 22:Out → 23:In |
| `mq024_cleanup.questphase / h0 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 24:False → 1:In; 10:True → 24:In; 19:Out1 → 24:In; 24:True → 26:In |
| `mq024_cleanup.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 24:True → 26:In; 26:Out → 25:Succeeded |
| `mq024_cleanup.questphase / h0 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"GreaterOrEqual"}}}` | 25:Out → 29:In; 29:Out → 30:In |
| `mq024_01_call_sandra.scene / scene / 109` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_v_calls_sandra_dorsett_start_done"}}}` | 109:0:0 → 110:0:1; 116:0:0 → 109:0:1 |
| `mq024_01_call_sandra.scene / scene / 111` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_v_calls_sandra_dorsett_end_done"}}}` | 111:0:0 → 112:0:1; 117:0:0 → 111:0:1 |
| `mq024_02_meet_sandra.scene / scene / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq024_hacked_data_carrier","value":1,"comparisonType":"GreaterOrEqual"}}}` | 12:0:0 → 14:0:1; 14:0:0 → 16:0:0; 14:0:1 → 476:0:1 |
| `mq024_02_meet_sandra.scene / scene / 209` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 203:0:0 → 209:0:1; 209:0:0 → 208:0:1 |
| `mq024_02_meet_sandra.scene / scene / 215` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 212:0:0 → 215:0:1; 215:0:0 → 214:0:1 |
| `mq024_02_meet_sandra.scene / scene / 226` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 223:0:0 → 226:0:1; 226:0:0 → 225:0:1 |
| `mq024_02_meet_sandra.scene / scene / 238` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 235:0:0 → 238:0:1; 238:0:0 → 237:0:1 |
| `mq024_02_meet_sandra.scene / scene / 245` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 242:0:0 → 245:0:1; 245:0:0 → 244:0:1 |
| `mq024_02_meet_sandra.scene / scene / 259` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 256:0:0 → 259:0:1; 259:0:0 → 258:0:1 |
| `mq024_02_meet_sandra.scene / scene / 266` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 50:0:0 → 266:0:1; 266:0:0 → 265:0:0 |
| `mq024_02_meet_sandra.scene / scene / 395` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"}}}}` | 395:0:0 → 440:0:1; 396:0:0 → 395:0:1 |
| `mq024_02_meet_sandra.scene / scene / 514` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 508:0:0 → 514:0:1; 514:0:0 → 133:0:1 |
| `mq024_02_meet_sandra.scene / scene / 522` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterHit_ConditionType","isAttackerPlayer":true,"targetRef":{"$type":"gameEntityReference","reference":"#q001_com_scav_girl","names":["mq024_sandra"]}}}}` | 1:0:0 → 522:0:1; 522:0:0 → 539:0:0; 529:1:0 → 522:0:0 |
| `mq024_02_meet_sandra.scene / scene / 536` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq024_ss_sandra","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 1:0:0 → 536:0:1; 529:1:0 → 536:0:0; 536:0:0 → 539:0:1 |
| `ep1_standalone_quest_bugfixing.questphase / h372 / 60` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"83635443133"}}},"socketId":2857566787},{"$type":"questConditionItem","condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"67091901544"}}},"socketId":2230468587},{"$type":"questConditionItem","condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"83574632792"}}},"socketId":243664000}]}` | 65:Out → 60:In; 60:Case2857566787 → 62:Active; 60:Case2230468587 → 63:Active; 60:Case243664000 → 64:Active; 60:Otherwise → 61:In1 |
| `ep1.questphase / h4048 / 34` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"83635443133"}}},"socketId":2857566787},{"$type":"questConditionItem","condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"67091901544"}}},"socketId":2230468587},{"$type":"questConditionItem","condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"83574632792"}}},"socketId":243664000}]}` | 43:Out → 34:In; 34:Case2857566787 → 36:Active; 34:Case2230468587 → 38:Active; 34:Case243664000 → 40:Active; 34:Otherwise → 35:In1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq024_03_sandra_apartment.questphase / h0 / 68 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq024_02_meet_sandra.scene / scene / 273 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `call_lifecycle` | mq024_01_hook.questphase / h0 / 4 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `choice_gate` | mq024_01_call_sandra.scene / scene / 11; mq024_01_call_sandra.scene / scene / 26; mq024_01_call_sandra.scene / scene / 6; mq024_02_meet_sandra.scene / scene / 115; +10 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | mq024_02_meet_sandra.scene / scene / 392; mq024_02_meet_sandra.scene / scene / 394 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | mq024_02_meet_sandra.scene / scene / 476; mq024_02_meet_sandra.scene / scene / 480; mq024_02_meet_sandra.scene / scene / 483; mq024_02_meet_sandra.scene / scene / 487; +7 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq024.questphase / h0 / 13; mq024.questphase / h0 / 16; mq024_01_call_sandra.scene / scene / 109; mq024_01_call_sandra.scene / scene / 111; +13 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq024_03_sandra_apartment.questphase / h0 / 35; mq024_03_sandra_apartment.questphase / h0 / 37; mq024_cleanup.questphase / h0 / 21; mq024_cleanup.questphase / h0 / 6; +1 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `device_action` | mq024_02_meet_sandra.scene / scene / 435; mq024_02_meet_sandra.scene / scene / 440; mq024_02_meet_sandra.scene / scene / 53; mq024_02_meet_sandra.scene / scene / 55; +5 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | mq024_02_meet_sandra.scene / scene / 536; mq024_03_sandra_apartment.questphase / h0 / 70 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `item_state` | mq024.questphase / h0 / 5; mq024_02_scavengers.questphase / h0 / 3 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `parallel_join` | mq024.questphase / h0 / 17; mq024_cleanup.questphase / h0 / 19 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq024.questphase / h0 / 8; mq024_01_call_sandra.scene / scene / 110; mq024_01_call_sandra.scene / scene / 112; mq024_01_call_sandra.scene / scene / 116; +15 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq024_03_sandra_apartment.questphase / h0 / 53 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq024_02_meet_sandra.scene / scene / 209; mq024_02_meet_sandra.scene / scene / 215; mq024_02_meet_sandra.scene / scene / 226; mq024_02_meet_sandra.scene / scene / 238; +9 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq024_03_sandra_apartment.questphase / h0 / 54 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq024_02_meet_sandra.scene / scene / 255; mq024_02_meet_sandra.scene / scene / 72; mq024_02_meet_sandra.scene / scene / 75; mq024_02_meet_sandra.scene / scene / 81; +3 locations in catalogue.json | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq024_03_sandra_apartment.questphase / h0 / 10; mq024_03_sandra_apartment.questphase / h0 / 5 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `target_resolution` | mq024_02_meet_sandra.scene / scene / 395; mq024_03_sandra_apartment.questphase / h0 / 52; mq024_03_sandra_apartment.questphase / h0 / 55; mq024_03_sandra_apartment.questphase / h0 / 60; +2 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | mq024_02_meet_sandra.scene / scene / 140; mq024_02_meet_sandra.scene / scene / 141; mq024_02_meet_sandra.scene / scene / 153; mq024_02_meet_sandra.scene / scene / 155; +16 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` | repair; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\mq024.questphase` | content candidate; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\phases\mq024_01_hook.questphase` | content candidate; forward dependency | `base-mq024` |
| `base\quest\minor_quests\mq024\phases\mq024_02_scavengers.questphase` | content candidate; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` | content candidate; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\phases\mq024_cleanup.questphase` | content candidate; journal anchor | `base-mq024` |
| `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` | content candidate; forward dependency | `base-mq024` |
| `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` | content candidate; journal anchor | `base-mq024` |
| `ep1\quest\bugfixing\ep1_standalone_quest_bugfixing.questphase` | repair; journal anchor | `ep1-shared` |
| `ep1\quest\ep1.questphase` | content candidate; journal anchor | `ep1-shared` |

Evidence shards for this dossier (including parent context): [base-mq024](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq024.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
