# Paid in Full

Journal: `quests/minor_quest/mq045_victor_debt` · `MinorQuest` · hash `3692983722`.

**Coverage: journal-linked.** 4 exact journal-linked nodes in 1 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 1 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Pay off your debt to Viktor – 21000 €$ (Primary) | `quests/minor_quest/mq045_victor_debt/mq045_debt/mq045_pay_off_victor` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq033_quest_bugfixes.questphase / h180 / 8` (Journal) | `quests/minor_quest/mq045_victor_debt/mq045_debt/mq045_pay_off_victor` | 13:Out → 8:Active; 8:Out → 9:Active |
| `mq033_quest_bugfixes.questphase / h180 / 9` (Journal) | `quests/minor_quest/mq045_victor_debt/mq045_desc` | 8:Out → 9:Active; 9:Out → 12:In |
| `mq033_quest_bugfixes.questphase / h180 / 10` (Journal) | `quests/minor_quest/mq045_victor_debt/mq045_debt/mq045_pay_off_victor` | 12:Out → 10:Succeeded; 10:Out → 11:Succeeded |
| `mq033_quest_bugfixes.questphase / h180 / 11` (Journal) | `quests/minor_quest/mq045_victor_debt` | 11:Out → 1:In; 10:Out → 11:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq033_quest_bugfixes.questphase / h30 / 20` | `base\quest\minor_quests\mq033\scenes\mq033_1_first_grafitti.scene`; `#mq033_1_sm_first_grafitti` | 20:q115_q201_tarots_out → 1:In; 21:Out → 20:q115_q201_tarots_in |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq033\mq033_quest_bugfixes.questphase` / h30 / 20 | `mq033_1_first_grafitti.scene` | 21: PauseCondition: q115_point_of_no_return; 20:q115_q201_tarots_out → 1:In; 21:Out → 20:q115_q201_tarots_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h0 / 30 | `mq033_1_first_grafitti.scene` | 78: GameManager; 78:Out → 30:mq033_1_v_comments_grafitti_in; 30:mq033_1_v_comments_grafitti_out → 77:In |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h0 / 46 | `mq033_1_first_grafitti.scene` | 226: Condition: ep1_standalone Equal RED default; 226: Condition: ep1_standalone Equal RED default; 226: Condition: ep1_standalone Equal RED default; 226:True → 46:mq033_1_ch_clues_in; 226:False → 46:mq033_1_ch_clues_in; 226:False → 46:ep1 |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 5 | `mq033_1_first_grafitti.scene` | 177: PauseCondition: #mq033_fool_tr; 177:Out → 5:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 14 | `mq033_1_first_grafitti.scene` | 178: PauseCondition: #mq033_chariot_tr; 178:Out → 14:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 20 | `mq033_1_first_grafitti.scene` | 179: PauseCondition: #mq033_death_tr; 179:Out → 20:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 26 | `mq033_1_first_grafitti.scene` | 180: PauseCondition: #mq033_emperor_tr; 180:Out → 26:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 32 | `mq033_1_first_grafitti.scene` | 181: PauseCondition: #mq033_empress_tr; 181:Out → 32:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 38 | `mq033_1_first_grafitti.scene` | 182: PauseCondition: #mq033_fortune_tr; 182:Out → 38:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 44 | `mq033_1_first_grafitti.scene` | 184: PauseCondition: #mq033_hangedman_tr; 184:Out → 44:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 50 | `mq033_1_first_grafitti.scene` | 185: PauseCondition: #mq033_hermit_tr; 185:Out → 50:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 56 | `mq033_1_first_grafitti.scene` | 186: PauseCondition: #mq033_hierophant_tr; 186:Out → 56:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 62 | `mq033_1_first_grafitti.scene` | 187: PauseCondition: #mq033_justice_tr; 187:Out → 62:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 68 | `mq033_1_first_grafitti.scene` | 188: PauseCondition: #mq033_lovers_tr; 188:Out → 68:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 74 | `mq033_1_first_grafitti.scene` | 189: PauseCondition: #mq033_magician_tr; 189:Out → 74:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 80 | `mq033_1_first_grafitti.scene` | 190: PauseCondition: #mq033_moon_tr; 190:Out → 80:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 86 | `mq033_1_first_grafitti.scene` | 191: PauseCondition: #mq033_priestess_tr; 191:Out → 86:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 92 | `mq033_1_first_grafitti.scene` | 192: PauseCondition: #mq033_star_tr; 192:Out → 92:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 98 | `mq033_1_first_grafitti.scene` | 193: PauseCondition: #mq033_strength_tr; 193:Out → 98:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 104 | `mq033_1_first_grafitti.scene` | 194: PauseCondition: #mq033_sun_tr; 194:Out → 104:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 110 | `mq033_1_first_grafitti.scene` | 195: PauseCondition: #mq033_temperance_tr; 195:Out → 110:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 116 | `mq033_1_first_grafitti.scene` | 196: PauseCondition: #mq033_tower_tr; 196:Out → 116:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 122 | `mq033_1_first_grafitti.scene` | 197: PauseCondition: #mq033_world_tr; 197:Out → 122:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h197 / 131 | `mq033_1_first_grafitti.scene` | 183: PauseCondition: #mq033_fortune_lower_tr; 183:Out → 131:mq033_1_johnny_grafitti_in |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h1676 / 4 | `mq033_1_first_grafitti.scene` | 0: Input; 28: Scene: mq033_ep1_grafitti.scene; 0:Out → 4:mq033_1_misty_about_grafitti_in; 28:to_mq033_first_scene → 4:from_mq033_ep1_tarot; 4:mq033_1_misty_about_grafitti_out → 25:In; 4:mq033_1_misty_to_all_tarots → 6:In; 4:mq033_ep1_tarot → 28:in misty |
| `base\quest\minor_quests\mq033\mq033_tarot.questphase` / h1877 / 4 | `mq033_1_first_grafitti.scene` | 0: Input; 0:Out → 4:mq033_1_victor_about_grafitti_in; 4:mq033_1_victor_about_grafitti_out → 5:In; 4:Holocall INT → 9:In; 4:Holocall RET → 8:In |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 79 | `mq033_tarot.questphase` | 109: PauseCondition: q101_done; 109:Out → 79:mq033_start |
| `ep1\quest\minor_quests\ep1_minor_quests.questphase` / h0 / 22 | `mq033_tarot.questphase` | 0: Input; 0:Out → 22:ep1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `ep1\quest\ep1.questphase` / h58 / 3 | `ep1_minor_quests.questphase` | 7: PauseCondition: ep1_active GreaterOrEqual 1; 9: CutControl; 7:Out → 3:In1; 9:CutSource → 3:CutDestination |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq033_1_first_grafitti.scene` | mq033_1_misty_about_grafitti_in, mq033_1_v_comments_grafitti_in, mq033_1_victor_about_grafitti_in, mq033_1_johnny_grafitti_in, mq033_1_ch_clues_in, ep1, from_mq033_ep1_tarot, q115_q201_tarots_in → mq033_1_misty_about_grafitti_out, mq033_1_v_comments_grafitti_out, mq033_1_victor_about_grafitti_out, mq033_1_johnny_grafitti_out, mq033_1_misty_to_all_tarots, mq033_ep1_tarot, End 8, q115_q201_tarots_out | Misty; Victor; Johnny; Victor_holocall; Player; 440 nodes / 587 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq033_1_first_grafitti.scene / n4 / 0` | Saw a weird image in town. (`grafitti`) | No option-level predicate stored | 0:0 → 7:0:0 |
| `mq033_1_first_grafitti.scene / n18 / 0` | So – saw a weird mural on the wall. (`grafitti`) | No option-level predicate stored | 0:0 → 1109:666:1; 0:0 → 1918:0:1; 0:0 → 1927:0:1; 0:0 → 2014:0:1 |
| `mq033_1_first_grafitti.scene / n23 / 0` | Higher power could be a little clearer. (`Option`) | No option-level predicate stored | 0:0 → 28:0:0 |
| `mq033_1_first_grafitti.scene / n23 / 1` | Major arcanum? What's that? (`Option_01`) | No option-level predicate stored | 0:1 → 25:0:0 |
| `mq033_1_first_grafitti.scene / n31 / 0` | Nope. Not buyin' it. (`Option_02`) | No option-level predicate stored | 0:0 → 33:0:0 |
| `mq033_1_first_grafitti.scene / n31 / 1` | What do I do with what I find? (`Option_03`) | No option-level predicate stored | 0:1 → 34:0:0 |
| `mq033_1_first_grafitti.scene / n48 / 0` | Huh, interesting. (`inspect`) | No option-level predicate stored | 0:0 → 1696:0:1 |
| `mq033_1_first_grafitti.scene / n53 / 0` | Well, well, well... (`inspect`) | No option-level predicate stored | 0:0 → 1704:0:1 |
| `mq033_1_first_grafitti.scene / n58 / 0` | Who woulda thought... (`inspect`) | No option-level predicate stored | 0:0 → 1769:0:1 |
| `mq033_1_first_grafitti.scene / n63 / 0` | What do we have here? (`inspect`) | No option-level predicate stored | 0:0 → 1764:0:1 |
| `mq033_1_first_grafitti.scene / n68 / 0` | Whoa... (`inspect`) | No option-level predicate stored | 0:0 → 1774:0:1 |
| `mq033_1_first_grafitti.scene / n73 / 0` | Huh, interesting. (`inspect`) | No option-level predicate stored | 0:0 → 1724:0:1 |
| `mq033_1_first_grafitti.scene / n78 / 0` | Well, well, well... (`inspect`) | No option-level predicate stored | 0:0 → 1699:0:1 |
| `mq033_1_first_grafitti.scene / n83 / 0` | Who woulda thought... (`inspect`) | No option-level predicate stored | 0:0 → 1709:0:1 |
| `mq033_1_first_grafitti.scene / n88 / 0` | What do we have here? (`inspect`) | No option-level predicate stored | 0:0 → 1754:0:1 |
| `mq033_1_first_grafitti.scene / n93 / 0` | Whoa... (`inspect`) | No option-level predicate stored | 0:0 → 1739:0:1 |
| `mq033_1_first_grafitti.scene / n98 / 0` | Huh, interesting. (`inspect`) | No option-level predicate stored | 0:0 → 1744:0:1 |
| `mq033_1_first_grafitti.scene / n103 / 0` | Well, well, well... (`inspect`) | No option-level predicate stored | 0:0 → 1749:0:1 |
| `mq033_1_first_grafitti.scene / n108 / 0` | Who woulda thought... (`inspect`) | No option-level predicate stored | 0:0 → 1789:0:1 |
| `mq033_1_first_grafitti.scene / n113 / 0` | What do we have here? (`inspect`) | No option-level predicate stored | 0:0 → 1794:0:1 |
| `mq033_1_first_grafitti.scene / n118 / 0` | Whoa... (`inspect`) | No option-level predicate stored | 0:0 → 1719:0:1 |
| `mq033_1_first_grafitti.scene / n123 / 0` | Huh, interesting. (`inspect`) | No option-level predicate stored | 0:0 → 1714:0:1 |
| `mq033_1_first_grafitti.scene / n128 / 0` | Well, well, well... (`inspect`) | No option-level predicate stored | 0:0 → 1729:0:1 |
| `mq033_1_first_grafitti.scene / n133 / 0` | Who woulda thought... (`inspect`) | No option-level predicate stored | 0:0 → 1734:0:1 |
| `mq033_1_first_grafitti.scene / n138 / 0` | What do we have here? (`inspect`) | No option-level predicate stored | 0:0 → 1784:0:1 |
| `mq033_1_first_grafitti.scene / n143 / 0` | Whoa... (`inspect`) | No option-level predicate stored | 0:0 → 1779:0:1 |
| `mq033_1_first_grafitti.scene / n438 / 0` | Huh, interesting. (`inspect`) | No option-level predicate stored | 0:0 → 1839:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CP77-58095` | mq033_quest_bugfixes.questphase / h344 / 2 | mq033_quest_bugfixes.questphase / h344 / 3 |
| `CP77-58095_applied` | mq033_quest_bugfixes.questphase / h344 / 4 | No reader in selected context |
| `CYB-12345` | mq033_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-571237` | mq033_quest_bugfixes.questphase / h180 / 2 | No reader in selected context |
| `CYB-591799` | mq033_quest_bugfixes.questphase / h30 / 2 | No reader in selected context |
| `CYB-591947` | mq033_quest_bugfixes.questphase / h88 / 2 | mq033_quest_bugfixes.questphase / h88 / 11 |
| `CYB-644298_MQ033` | mq033_quest_bugfixes.questphase / h249 / 4 | mq033_quest_bugfixes.questphase / h249 / 9 |
| `ep1_mq033_asked_misty` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1979 |
| `ep1_standalone` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1957 |
| `ep1_tarrot_scene_from_card_scene` | mq033_1_first_grafitti.scene / scene / 1971 | No reader in selected context |
| `holo_interrupt_call` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 2021; mq033_1_first_grafitti.scene / scene / 2042 |
| `holo_setup_started` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 2042 |
| `holo_v_calls_victor_end_activate` | mq033_1_first_grafitti.scene / scene / 1027 | No reader in selected context |
| `holo_v_calls_victor_end_done` | mq033_1_first_grafitti.scene / scene / 1017 | mq033_1_first_grafitti.scene / scene / 1015 |
| `king_of_the_cups_scanned` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1979 |
| `king_of_the_pentacles_scanned` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1979 |
| `king_of_the_swords_scanned` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1979 |
| `king_of_the_wands_scanned` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1979 |
| `misty_default_on` | mq033_quest_bugfixes.questphase / h344 / 10; mq033_quest_bugfixes.questphase / h88 / 13 | mq033_quest_bugfixes.questphase / h344 / 16 |
| `mq033_done` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1984; mq033_quest_bugfixes.questphase / h249 / 15; mq033_quest_bugfixes.questphase / h88 / 9 |
| `mq033_grafitti_counter` | mq033_1_first_grafitti.scene / scene / 149 | mq033_1_first_grafitti.scene / scene / 513; mq033_quest_bugfixes.questphase / h88 / 17 |
| `mq033_misty_dialogue_on` | mq033_quest_bugfixes.questphase / h344 / 11; mq033_quest_bugfixes.questphase / h88 / 14 | mq033_quest_bugfixes.questphase / h344 / 14 |
| `mq033_misty_tarot_talk_needed` | mq033_quest_bugfixes.questphase / h88 / 15 | mq033_quest_bugfixes.questphase / h344 / 8 |
| `mq033_victor_dlg_started` | mq033_1_first_grafitti.scene / scene / 1003; mq033_1_first_grafitti.scene / scene / 1004 | No reader in selected context |
| `q001_just_after_rd_scene` | Producer outside selected context | mq033_quest_bugfixes.questphase / h180 / 13 |
| `q115_point_of_no_return` | Producer outside selected context | mq033_quest_bugfixes.questphase / h249 / 11; mq033_quest_bugfixes.questphase / h30 / 21 |
| `q116_smasher_defeated` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 773 |
| `q201_cube_solved` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 521 |
| `q301_failed` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1979 |
| `sq018_03_done` | Producer outside selected context | mq033_quest_bugfixes.questphase / h88 / 8 |
| `sq018_done` | Producer outside selected context | mq033_quest_bugfixes.questphase / h344 / 12 |
| `travelling_merchant_lives` | Producer outside selected context | mq033_quest_bugfixes.questphase / h0 / 25 |
| `victor_dd_is_call` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1038; mq033_1_first_grafitti.scene / scene / 18; mq033_1_first_grafitti.scene / scene / 2014; mq033_1_first_grafitti.scene / scene / 2037 |
| `victor_debt_paid_full` | Producer outside selected context | mq033_quest_bugfixes.questphase / h180 / 12 |
| `victor_default_pose_active` | Producer outside selected context | mq033_1_first_grafitti.scene / scene / 1922; mq033_1_first_grafitti.scene / scene / 1936 |
| `vv_default_initial_dialogue_played` | mq033_1_first_grafitti.scene / scene / 1918 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>126 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq033_quest_bugfixes.questphase / h0 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 26:Out → 25:In |
| `mq033_quest_bugfixes.questphase / h30 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_point_of_no_return"}}}` | 2:Out → 21:In; 21:Out → 20:q115_q201_tarots_in |
| `mq033_quest_bugfixes.questphase / h88 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq018_03_done"}}}` | 0:Out → 8:In; 8:Out → 11:In |
| `mq033_quest_bugfixes.questphase / h88 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq033_done"}}}` | 9:True → 1:In; 17:True → 9:In; 9:False → 12:In |
| `mq033_quest_bugfixes.questphase / h88 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-591947"}}}` | 11:False → 2:In; 8:Out → 11:In; 11:True → 19:In1 |
| `mq033_quest_bugfixes.questphase / h88 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq033_grafitti_counter"}}}` | 2:Out → 17:In; 17:True → 9:In; 17:False → 20:In1 |
| `mq033_quest_bugfixes.questphase / h180 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"victor_debt_paid_full"}}}` | 9:Out → 12:In; 12:Out → 10:Succeeded |
| `mq033_quest_bugfixes.questphase / h180 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q001_just_after_rd_scene"}}}` | 2:Out → 13:In; 13:Out → 8:Active |
| `mq033_quest_bugfixes.questphase / h249 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq000_tr_vs_apartment"}}` | 10:CutSource → 2:CutDestination; 15:Out → 2:In; 2:Out → 10:In; 2:Out → 13:In |
| `mq033_quest_bugfixes.questphase / h249 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-644298_MQ033"}}}` | 0:Out → 9:In; 9:False → 15:In |
| `mq033_quest_bugfixes.questphase / h249 / 10` | `questCutControlNodeDefinition` `{}` | 10:CutSource → 2:CutDestination; 2:Out → 10:In; 11:Out → 10:In; 10:Out → 12:In |
| `mq033_quest_bugfixes.questphase / h249 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_point_of_no_return"}}}` | 11:Out → 10:In; 13:CutSource → 11:CutDestination; 15:Out → 11:In |
| `mq033_quest_bugfixes.questphase / h249 / 13` | `questCutControlNodeDefinition` `{}` | 2:Out → 13:In; 13:Out → 3:In; 13:CutSource → 11:CutDestination |
| `mq033_quest_bugfixes.questphase / h249 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq033_done"}}}` | 15:Out → 2:In; 9:False → 15:In; 15:Out → 11:In |
| `mq033_quest_bugfixes.questphase / h344 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-58095"}}}` | 0:Out → 3:In; 3:False → 2:In |
| `mq033_quest_bugfixes.questphase / h344 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"ep1/quests/minor_quest/mq033_ep1/mq033_ep1_tarot/talk_to_misty","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 6:In; 6:True → 12:In |
| `mq033_quest_bugfixes.questphase / h344 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq033_misty_tarot_talk_needed"}}}` | 12:True → 8:In; 8:True → 14:In |
| `mq033_quest_bugfixes.questphase / h344 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq018_done"}}}` | 6:True → 12:In; 12:True → 8:In |
| `mq033_quest_bugfixes.questphase / h344 / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq033_misty_dialogue_on"}}}` | 8:True → 14:In; 14:True → 16:In |
| `mq033_quest_bugfixes.questphase / h344 / 16` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"misty_default_on","comparisonType":"Equal"}}}` | 14:True → 16:In; 16:True → 17:In |
| `mq033_quest_bugfixes.questphase / h344 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq033_tarot/mq033_tarot/03_talk_to_misty","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active","inverted":true}}}` | 17:True → 9:In; 16:True → 17:In |
| `mq033_1_first_grafitti.scene / scene / 228` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_fool"},"eventType":"Finished"}}}` | 228:0:0 → 230:0:0; 623:0:0 → 228:0:1; 1952:0:0 → 228:0:0 |
| `mq033_1_first_grafitti.scene / scene / 237` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_death"},"eventType":"Finished"}}}` | 237:0:0 → 236:0:0; 627:0:0 → 237:0:1 |
| `mq033_1_first_grafitti.scene / scene / 247` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_justice"},"eventType":"Finished"}}}` | 247:0:0 → 243:0:0; 634:0:0 → 247:0:1 |
| `mq033_1_first_grafitti.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_strength"},"eventType":"Finished"}}}` | 251:0:0 → 250:0:0; 641:0:0 → 251:0:1 |
| `mq033_1_first_grafitti.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_temperance"},"eventType":"Finished"}}}` | 258:0:0 → 257:0:0; 649:0:0 → 258:0:1 |
| `mq033_1_first_grafitti.scene / scene / 265` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_chariot"},"eventType":"Finished"}}}` | 265:0:0 → 264:0:0; 657:0:0 → 265:0:1 |
| `mq033_1_first_grafitti.scene / scene / 272` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_emperor"},"eventType":"Finished"}}}` | 272:0:0 → 271:0:0; 667:0:0 → 272:0:1 |
| `mq033_1_first_grafitti.scene / scene / 279` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_empress"},"eventType":"Finished"}}}` | 279:0:0 → 278:0:0; 671:0:0 → 279:0:1 |
| `mq033_1_first_grafitti.scene / scene / 286` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_hanged_man"},"eventType":"Finished"}}}` | 286:0:0 → 285:0:0; 721:0:0 → 286:0:1 |
| `mq033_1_first_grafitti.scene / scene / 293` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_hermit"},"eventType":"Finished"}}}` | 293:0:0 → 292:0:0; 725:0:0 → 293:0:1 |
| `mq033_1_first_grafitti.scene / scene / 299` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_hierophant"},"eventType":"Finished"}}}` | 299:0:0 → 298:0:0; 729:0:0 → 299:0:1 |
| `mq033_1_first_grafitti.scene / scene / 305` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_high_priestess"},"eventType":"Finished"}}}` | 305:0:0 → 304:0:0; 733:0:0 → 305:0:1 |
| `mq033_1_first_grafitti.scene / scene / 311` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_lovers"},"eventType":"Finished"}}}` | 311:0:0 → 310:0:0; 737:0:0 → 311:0:1 |
| `mq033_1_first_grafitti.scene / scene / 323` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_moon"},"eventType":"Finished"}}}` | 323:0:0 → 322:0:0; 745:0:0 → 323:0:1 |
| `mq033_1_first_grafitti.scene / scene / 329` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_star"},"eventType":"Finished"}}}` | 329:0:0 → 328:0:0; 749:0:0 → 329:0:1 |
| `mq033_1_first_grafitti.scene / scene / 335` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_sun"},"eventType":"Finished"}}}` | 335:0:0 → 334:0:0; 753:0:0 → 335:0:1 |
| `mq033_1_first_grafitti.scene / scene / 344` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_wheel_of_fortune"},"eventType":"Finished"}}}` | 344:0:0 → 343:0:0; 761:0:0 → 344:0:1 |
| `mq033_1_first_grafitti.scene / scene / 441` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_judgement"},"eventType":"Finished"}}}` | 441:0:0 → 440:0:0; 769:0:0 → 441:0:1 |
| `mq033_1_first_grafitti.scene / scene / 483` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_misty_respawn_tr"},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#misty","names":["misty"]},"onScreenTest":true,"inverted":true}}]}}` | 483:0:0 → 463:0:1; 1974:0:0 → 483:0:1; 1979:0:1 → 483:0:1 |
| `mq033_1_first_grafitti.scene / scene / 513` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq033_grafitti_counter","value":20,"comparisonType":"GreaterOrEqual"}}}` | 39:0:0 → 513:0:1; 513:0:0 → 517:0:0; 513:0:0 → 1984:0:1; 513:0:1 → 486:0:3 |
| `mq033_1_first_grafitti.scene / scene / 521` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q201_cube_solved"}}}` | 521:0:0 → 523:0:1; 1116:0:0 → 521:0:1 |
| `mq033_1_first_grafitti.scene / scene / 597` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterLifePath_ConditionType","lifePathID":"83574632792"}}}` | 531:0:0 → 597:0:1; 597:0:0 → 600:0:1; 597:0:1 → 598:0:1 |
| `mq033_1_first_grafitti.scene / scene / 598` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterLifePath_ConditionType","lifePathID":"67091901544"}}}` | 597:0:1 → 598:0:1; 598:0:0 → 599:0:1; 598:0:1 → 378:0:1 |
| `mq033_1_first_grafitti.scene / scene / 773` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q116_smasher_defeated"}}}` | 773:0:0 → 769:0:1; 1116:0:0 → 773:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1015` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_v_calls_victor_end_done"}}}` | 1015:0:0 → 1017:0:1; 1085:0:0 → 1015:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1038` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"victor_dd_is_call"}}}` | 1004:0:0 → 1038:0:1; 1038:0:0 → 1027:0:1; 1038:0:1 → 17:0:0 |
| `mq033_1_first_grafitti.scene / scene / 1124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_fool_exit_tr"}}` | 623:0:0 → 1124:0:1; 1124:0:0 → 1148:0:1; 1136:1:0 → 1124:0:0; 1160:0:0 → 1124:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_fool_exit_tr"}}` | 1128:0:0 → 1152:0:2; 1136:1:0 → 1128:0:0; 1156:0:0 → 1128:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1166` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_death_exit_tr"}}` | 627:0:0 → 1166:0:1; 1166:0:0 → 1174:0:1; 1170:1:0 → 1166:0:0; 1180:0:0 → 1166:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1168` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_death_exit_tr"}}` | 1168:0:0 → 1176:0:2; 1170:1:0 → 1168:0:0; 1178:0:0 → 1168:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1193` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_justice_exit_tr"}}` | 634:0:0 → 1193:0:1; 1193:0:0 → 1201:0:1; 1197:1:0 → 1193:0:0; 1207:0:0 → 1193:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1195` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_justice_exit_tr"}}` | 1195:0:0 → 1203:0:2; 1197:1:0 → 1195:0:0; 1205:0:0 → 1195:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1222` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_strength_exit_tr"}}` | 641:0:0 → 1222:0:1; 1222:0:0 → 1228:0:1; 1226:1:0 → 1222:0:0; 1234:0:0 → 1222:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1224` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_strength_exit_tr"}}` | 1224:0:0 → 1230:0:2; 1226:1:0 → 1224:0:0; 1232:0:0 → 1224:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1246` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_temperance_exit_tr"}}` | 649:0:0 → 1246:0:1; 1246:0:0 → 1252:0:1; 1250:1:0 → 1246:0:0; 1258:0:0 → 1246:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1248` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_temperance_exit_tr"}}` | 1248:0:0 → 1254:0:2; 1250:1:0 → 1248:0:0; 1256:0:0 → 1248:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1270` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_chariot_exit_tr"}}` | 657:0:0 → 1270:0:1; 1270:0:0 → 1276:0:1; 1274:1:0 → 1270:0:0; 1282:0:0 → 1270:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1272` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_chariot_exit_tr"}}` | 1272:0:0 → 1278:0:2; 1274:1:0 → 1272:0:0; 1280:0:0 → 1272:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1294` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_emperor_exit_tr"}}` | 667:0:0 → 1294:0:1; 1294:0:0 → 1300:0:1; 1298:1:0 → 1294:0:0; 1306:0:0 → 1294:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1296` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_emperor_exit_tr"}}` | 1296:0:0 → 1302:0:2; 1298:1:0 → 1296:0:0; 1304:0:0 → 1296:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1318` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_empress_exit_tr"}}` | 671:0:0 → 1318:0:1; 1318:0:0 → 1324:0:1; 1322:1:0 → 1318:0:0; 1330:0:0 → 1318:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1320` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_empress_exit_tr"}}` | 1320:0:0 → 1326:0:2; 1322:1:0 → 1320:0:0; 1328:0:0 → 1320:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1342` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_hangedman_exit_tr"}}` | 721:0:0 → 1342:0:1; 1342:0:0 → 1348:0:1; 1346:1:0 → 1342:0:0; 1354:0:0 → 1342:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1344` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_hangedman_exit_tr"}}` | 1344:0:0 → 1350:0:2; 1346:1:0 → 1344:0:0; 1366:0:0 → 1344:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1372` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_hermit_exit_tr"}}` | 725:0:0 → 1372:0:1; 1372:0:0 → 1378:0:1; 1376:1:0 → 1372:0:0; 1382:0:0 → 1372:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1374` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_hermit_exit_tr"}}` | 1374:0:0 → 1380:0:2; 1376:1:0 → 1374:0:0; 1384:0:0 → 1374:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1396` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_hierophant_exit_tr"}}` | 729:0:0 → 1396:0:1; 1396:0:0 → 1402:0:1; 1400:1:0 → 1396:0:0; 1406:0:0 → 1396:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1398` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_hierophant_exit_tr"}}` | 1398:0:0 → 1404:0:2; 1400:1:0 → 1398:0:0; 1408:0:0 → 1398:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1420` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_priestess_exit_tr"}}` | 733:0:0 → 1420:0:1; 1420:0:0 → 1426:0:1; 1424:1:0 → 1420:0:0; 1430:0:0 → 1420:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1422` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_priestess_exit_tr"}}` | 1422:0:0 → 1428:0:2; 1424:1:0 → 1422:0:0; 1432:0:0 → 1422:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1444` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_lovers_exit_tr"}}` | 737:0:0 → 1444:0:1; 1444:0:0 → 1450:0:1; 1448:1:0 → 1444:0:0; 1454:0:0 → 1444:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1446` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_lovers_exit_tr"}}` | 1446:0:0 → 1452:0:2; 1448:1:0 → 1446:0:0; 1456:0:0 → 1446:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1468` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_magician_exit_tr"}}` | 741:0:0 → 1468:0:1; 1468:0:0 → 1474:0:1; 1472:1:0 → 1468:0:0; 1478:0:0 → 1468:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1470` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_magician_exit_tr"}}` | 1470:0:0 → 1476:0:2; 1472:1:0 → 1470:0:0; 1480:0:0 → 1470:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1492` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_moon_exit_tr"}}` | 745:0:0 → 1492:0:1; 1492:0:0 → 1498:0:1; 1496:1:0 → 1492:0:0; 1502:0:0 → 1492:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1494` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_moon_exit_tr"}}` | 1494:0:0 → 1500:0:2; 1496:1:0 → 1494:0:0; 1504:0:0 → 1494:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1516` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_star_exit_tr"}}` | 749:0:0 → 1516:0:1; 1516:0:0 → 1522:0:1; 1520:1:0 → 1516:0:0; 1526:0:0 → 1516:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1518` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_star_exit_tr"}}` | 1518:0:0 → 1524:0:2; 1520:1:0 → 1518:0:0; 1528:0:0 → 1518:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1540` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_sun_exit_tr"}}` | 753:0:0 → 1540:0:1; 1540:0:0 → 1546:0:1; 1544:1:0 → 1540:0:0; 1550:0:0 → 1540:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1542` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_sun_exit_tr"}}` | 1542:0:0 → 1548:0:2; 1544:1:0 → 1542:0:0; 1552:0:0 → 1542:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1564` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_tower_exit_tr"}}` | 757:0:0 → 1564:0:1; 1564:0:0 → 1570:0:1; 1568:1:0 → 1564:0:0; 1574:0:0 → 1564:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1566` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_tower_exit_tr"}}` | 1566:0:0 → 1572:0:2; 1568:1:0 → 1566:0:0; 1576:0:0 → 1566:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1588` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_fortune_lower_exit_tr"}}` | 761:0:0 → 1588:0:1; 1588:0:0 → 1594:0:1; 1592:1:0 → 1588:0:0; 1598:0:0 → 1588:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1590` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_fortune_lower_exit_tr"}}` | 1590:0:0 → 1596:0:2; 1592:1:0 → 1590:0:0; 1600:0:0 → 1590:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1612` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq033_world_exit_tr"}}` | 765:0:0 → 1612:0:1; 1612:0:0 → 1618:0:1; 1616:1:0 → 1612:0:0; 1622:0:0 → 1612:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1614` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_world_exit_tr"}}` | 1614:0:0 → 1620:0:2; 1616:1:0 → 1614:0:0; 1624:0:0 → 1614:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1697` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1696:0:0 → 1697:0:1; 1697:0:0 → 230:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1701` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1699:0:0 → 1701:0:1; 1701:0:0 → 271:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1706` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1704:0:0 → 1706:0:1; 1706:0:0 → 236:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1711` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1709:0:0 → 1711:0:1; 1711:0:0 → 278:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1716` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1714:0:0 → 1716:0:1; 1716:0:0 → 328:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1721` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1719:0:0 → 1721:0:1; 1721:0:0 → 322:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1726` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1724:0:0 → 1726:0:1; 1726:0:0 → 264:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1731` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1729:0:0 → 1731:0:1; 1731:0:0 → 334:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1736` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1734:0:0 → 1736:0:1; 1736:0:0 → 340:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1741` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1739:0:0 → 1741:0:1; 1741:0:0 → 292:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1746` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1744:0:0 → 1746:0:1; 1746:0:0 → 298:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1751` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1749:0:0 → 1751:0:1; 1751:0:0 → 304:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1756` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1754:0:0 → 1756:0:1; 1756:0:0 → 285:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1766` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1764:0:0 → 1766:0:1; 1766:0:0 → 250:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1771` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1769:0:0 → 1771:0:1; 1771:0:0 → 243:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1776` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1774:0:0 → 1776:0:1; 1776:0:0 → 257:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1781` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1779:0:0 → 1781:0:1; 1781:0:0 → 346:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1786` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1784:0:0 → 1786:0:1; 1786:0:0 → 343:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1791` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1789:0:0 → 1791:0:1; 1791:0:0 → 310:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1796` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1794:0:0 → 1796:0:1; 1796:0:0 → 316:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1841` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1839:0:0 → 1841:0:1; 1841:0:0 → 440:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1848` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_tower"},"eventType":"Finished"}}}` | 1848:0:0 → 340:0:0; 1850:0:0 → 1848:0:1; 1852:0:0 → 1848:0:0 |
| `mq033_1_first_grafitti.scene / scene / 1850` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq033_tower_scanning_tr"}}` | 340:0:0 → 1850:0:0; 341:666:0 → 1850:0:1; 1850:0:0 → 133:0:0; 1850:0:0 → 1848:0:1; 1850:0:0 → 1852:0:1; 1850:0:0 → 1912:0:1; 1852:0:0 → 1850:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1852` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_tower_scanning_tr"}}` | 340:0:0 → 1852:0:0; 1850:0:0 → 1852:0:1; 1852:0:0 → 133:1:0; 1852:0:0 → 1848:0:0; 1852:0:0 → 1850:0:1; 1852:0:0 → 1915:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1865` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_magician"},"eventType":"Finished"}}}` | 1865:0:0 → 316:0:0; 1867:0:0 → 1865:0:1; 1869:0:0 → 1865:0:0 |
| `mq033_1_first_grafitti.scene / scene / 1867` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq033_magician_scanning_tr"}}` | 316:0:0 → 1867:0:0; 317:666:0 → 1867:0:1; 1867:0:0 → 113:0:0; 1867:0:0 → 1865:0:1; 1867:0:0 → 1869:0:1; 1867:0:0 → 1882:0:1; 1869:0:0 → 1867:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1869` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_magician_scanning_tr"}}` | 316:0:0 → 1869:0:0; 1867:0:0 → 1869:0:1; 1869:0:0 → 113:1:0; 1869:0:0 → 1865:0:0; 1869:0:0 → 1867:0:1; 1869:0:0 → 1885:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1889` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq033_the_world"},"eventType":"Finished"}}}` | 1889:0:0 → 346:0:0; 1891:0:0 → 1889:0:1; 1893:0:0 → 1889:0:0 |
| `mq033_1_first_grafitti.scene / scene / 1891` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#mq033_world_scanning_tr"},{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_world_scanning_02_tr"}]}}` | 346:0:0 → 1891:0:0; 347:666:0 → 1891:0:1; 1891:0:0 → 143:0:0; 1891:0:0 → 1889:0:1; 1891:0:0 → 1893:0:1; 1891:0:0 → 1906:0:1; 1893:0:0 → 1891:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1893` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq033_world_scanning_tr"},{"$type":"questTriggerCondition","triggerAreaRef":"#mq033_world_scanning_02_tr"}]}}` | 346:0:0 → 1893:0:0; 1891:0:0 → 1893:0:1; 1893:0:0 → 143:1:0; 1893:0:0 → 1889:0:0; 1893:0:0 → 1891:0:1; 1893:0:0 → 1908:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1922` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"victor_default_pose_active"}}}` | 1922:0:0 → 1923:0:1; 1922:0:0 → 1940:0:1; 1927:0:0 → 1922:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1936` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"victor_default_pose_active","comparisonType":"Equal"}}}` | 1927:0:0 → 1936:0:1; 1936:0:0 → 1934:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1957` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_standalone","comparisonType":"Equal"}}}` | 49:0:0 → 1957:0:1; 1957:0:0 → 623:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1979` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"ep1_mq033_asked_misty","comparisonType":"Equal"}},{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"king_of_the_cups_scanned"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"king_of_the_pentacles_scanned"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"king_of_the_swords_scanned"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"king_of_the_wands_scanned"}}]},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q301_failed","comparisonType":"Equal"}}]}}` | 486:0:0 → 1979:0:1; 1979:0:0 → 1971:0:1; 1979:0:1 → 483:0:1 |
| `mq033_1_first_grafitti.scene / scene / 1984` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq033_done"}}}` | 513:0:0 → 1984:0:1; 1984:0:0 → 1986:0:0 |
| `mq033_1_first_grafitti.scene / scene / 2014` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"victor_dd_is_call"}}}` | 18:0:0 → 2014:0:1; 2014:0:0 → 1995:0:1 |
| `mq033_1_first_grafitti.scene / scene / 2021` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_interrupt_call"}}}` | 2021:0:0 → 18:1:0; 2021:0:0 → 2042:0:1; 2037:0:0 → 2021:0:1 |
| `mq033_1_first_grafitti.scene / scene / 2037` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"victor_dd_is_call"}}}` | 16:0:0 → 2037:0:1; 2037:0:0 → 2021:0:1; 2042:0:0 → 2037:0:1 |
| `mq033_1_first_grafitti.scene / scene / 2042` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_interrupt_call","comparisonType":"Equal"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"GreaterOrEqual"}},{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}]}}` | 2021:0:0 → 2042:0:1; 2042:0:0 → 18:0:0; 2042:0:0 → 2037:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `choice_gate` | mq033_1_first_grafitti.scene / scene / 103; mq033_1_first_grafitti.scene / scene / 108; mq033_1_first_grafitti.scene / scene / 113; mq033_1_first_grafitti.scene / scene / 118; +21 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | mq033_1_first_grafitti.scene / scene / 1015; mq033_1_first_grafitti.scene / scene / 1038; mq033_1_first_grafitti.scene / scene / 18; mq033_1_first_grafitti.scene / scene / 1922; +27 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `persistent_decision` | mq033_1_first_grafitti.scene / scene / 1003; mq033_1_first_grafitti.scene / scene / 1004; mq033_1_first_grafitti.scene / scene / 1017; mq033_1_first_grafitti.scene / scene / 1027; +15 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | mq033_1_first_grafitti.scene / scene / 1697; mq033_1_first_grafitti.scene / scene / 1701; mq033_1_first_grafitti.scene / scene / 1706; mq033_1_first_grafitti.scene / scene / 1711; +18 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq033_quest_bugfixes.questphase / h249 / 10; mq033_quest_bugfixes.questphase / h249 / 13 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `scan_evidence` | mq033_1_first_grafitti.scene / scene / 1848; mq033_1_first_grafitti.scene / scene / 1865; mq033_1_first_grafitti.scene / scene / 1889; mq033_1_first_grafitti.scene / scene / 228; +17 locations in catalogue.json | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | mq033_quest_bugfixes.questphase / h30 / 20 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `workspot_performance` | mq033_1_first_grafitti.scene / scene / 468; mq033_1_first_grafitti.scene / scene / 500; mq033_1_first_grafitti.scene / scene / 511 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq033\mq033_quest_bugfixes.questphase` | repair; journal anchor | `base-mq033` |
| `base\quest\minor_quests\mq033\scenes\mq033_1_first_grafitti.scene` | content candidate; forward dependency | `base-mq033` |

Evidence shards for this dossier (including parent context): [base-mq033](../../../../../reference/quests/deep-dives/catalogue/evidence/base-mq033.json.gz), [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
