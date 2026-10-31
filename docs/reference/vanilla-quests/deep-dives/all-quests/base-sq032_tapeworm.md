# Tapeworm

Journal: `quests/side_quest/sq032_tapeworm` · `MainQuest` · hash `189903109`.

**Coverage: journal-linked.** 33 exact journal-linked nodes in 9 resources; 11 resources in the inspected dependency context.

Resource roles in that context: 11 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Take the Omega Blockers. (Primary) | `quests/side_quest/sq032_tapeworm/00_johnny/00_take_pill` |
| Looks like "know thyself" has become a two-for-one deal. If it's true we're becoming one person, I suggest we keep an open dialogue. And by the way, I'd be happy to explain why the only shot you got to survive is to reach Mikoshi and stay in one piece along the way. You'd be doing me a huge favor. After all, if you're not good at following my instructions, I have to inherit whatever's left of you. (Primary) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` |
| Sit and rest. (Primary) | `quests/side_quest/sq032_tapeworm/00_johnny/01_sit_down` |
| Follow Johnny. (Primary) | `quests/side_quest/sq032_tapeworm/00_johnny/02_follow_johnny` |
| Enter through the window. (Primary) | `quests/side_quest/sq032_tapeworm/00_johnny/03_break_window` |
| Open the cache. (Primary) | `quests/side_quest/sq032_tapeworm/00_johnny/04_open_cache` |
| Take the dogtags. (Primary) | `quests/side_quest/sq032_tapeworm/00_johnny/05_take_dogtags` |
| Leave the hotel through the window. (Primary) | `quests/side_quest/sq032_tapeworm/00_johnny/06_leave_motel_room` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sq032_episode_3.questphase / h0 / 61` (Journal) | `quests/side_quest/sq032_tapeworm` | 45:Out → 61:Inactive; 61:Out → 56:In |
| `sq032_episode_4.questphase / h0 / 33` (Journal) | `quests/side_quest/sq032_tapeworm` | 20:Out → 33:Inactive; 33:Out → 32:In |
| `sq032_episode_5.questphase / h0 / 38` (Journal) | `quests/side_quest/sq032_tapeworm` | 5:Out → 38:Inactive; 38:Out → 16:In |
| `sq032_03_third_episode.scene / scene / 100` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 188:0:0 → 100:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_03_third_episode.scene / scene / 105` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 105:0:0 → 982:0:1; 327:0:0 → 105:0:2; 395:2:0 → 105:0:2; 3800:0:0 → 105:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_03_third_episode.scene / scene / 3784` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny/description` | 188:0:0 → 3784:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_04_fourth_episode.scene / scene / 1308` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_take_pill` | 1308:0:0 → 1847:0:1; 1329:0:0 → 1308:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_04_fourth_episode.scene / scene / 1381` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 512:0:0 → 1381:0:2; 669:0:0 → 1381:0:2; 1381:0:0 → 1396:0:1; 1381:0:0 → 1710:0:0; 1417:0:0 → 1381:0:2; 1867:0:0 → 1381:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_04_fourth_episode.scene / scene / 1859` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_take_pill` | 1411:0:0 → 1859:0:3; 1859:0:0 → 1417:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_04_fourth_episode.scene / scene / 1863` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_take_pill` | 334:3:0 → 1863:0:3; 1863:0:0 → 512:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_04_fourth_episode.scene / scene / 1867` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_take_pill` | 1404:0:0 → 1867:0:4; 1867:0:0 → 1381:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_04_fourth_episode.scene / scene / 1875` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_take_pill` | 1786:0:0 → 1875:0:1; 1875:0:0 → 1887:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_04_fourth_episode.scene / scene / 1887` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 1875:0:0 → 1887:0:1; 1887:0:0 → 1317:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_04_fourth_episode.scene / scene / 1943` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny/description` | 1786:0:0 → 1943:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_05_fifth_episode.scene / scene / 42` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 50:0:0 → 42:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_05_fifth_episode.scene / scene / 44` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 44:0:0 → 384:0:1; 44:0:0 → 723:0:1; 130:0:0 → 44:0:2; 181:0:0 → 44:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_05_fifth_episode.scene / scene / 47` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/01_sit_down` | 27:0:0 → 47:0:1; 47:0:0 → 712:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_05_fifth_episode.scene / scene / 50` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/01_sit_down` | 50:0:0 → 42:0:1; 307:0:0 → 50:0:3; 597:0:0 → 50:0:3; 634:0:0 → 50:0:3; 651:0:0 → 50:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_05_fifth_episode.scene / scene / 1119` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny/description` | 27:0:0 → 1119:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_06_sixth_episode.scene / scene / 64` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 135:0:0 → 64:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_06_sixth_episode.scene / scene / 285` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 286:0:0 → 285:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_06_sixth_episode.scene / scene / 291` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 292:0:0 → 291:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_06_sixth_episode.scene / scene / 467` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny/description` | 380:0:0 → 467:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_07_finale.scene / scene / 458` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/03_break_window` | 460:0:0 → 458:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_07_finale.scene / scene / 459` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/04_open_cache` | 464:0:0 → 459:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_07_finale.scene / scene / 460` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 379:0:0 → 460:0:2; 460:0:0 → 458:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_07_finale.scene / scene / 463` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 463:0:0 → 696:0:1; 470:0:0 → 463:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_07_finale.scene / scene / 464` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/03_break_window` | 168:0:0 → 464:0:3; 464:0:0 → 459:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_07_finale.scene / scene / 470` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/04_open_cache` | 171:0:0 → 470:0:3; 470:0:0 → 463:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_07_finale.scene / scene / 473` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny` | 244:0:0 → 473:0:3; 473:0:0 → 477:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_07_finale.scene / scene / 477` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/06_leave_motel_room` | 473:0:0 → 477:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032_07_finale.scene / scene / 479` (Journal) | `quests/side_quest/sq032_tapeworm/00_johnny/06_leave_motel_room` | 435:0:0 → 479:0:3; 479:0:0 → 445:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq032.questphase / h0 / 99` (Journal) | `quests/side_quest/sq032_tapeworm` | 76:Out → 99:Succeeded; 99:Out → 92:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sq032_episode_3.questphase / h0 / 66` | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene`; `#sq032_03_sm_third_episode` | 66:out → 48:In; 74:True → 66:in_q104; 66:out_clean_up → 70:In1; 88:Case2488326877 → 66:Prefetch |
| `sq032_episode_3.questphase / h0 / 80` | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene`; `#sq032_03_sm_third_episode` | 80:out → 50:In; 80:out_clean_up → 70:In1; 75:True → 80:in_q105; 88:Case2173311359 → 80:Prefetch |
| `sq032_episode_4.questphase / h0 / 41` | `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene`; `#sq032_04_sm_fourth_episode` | 41:out → 23:In; 54:True → 41:in_q110; 41:out_clean_up → 45:In1; 78:Case285067426 → 41:Prefetch |
| `sq032_episode_4.questphase / h0 / 42` | `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene`; `#sq032_04_sm_fourth_episode` | 42:out → 24:In; 51:True → 42:in_q104; 42:out_clean_up → 45:In1; 78:Case2488326877 → 42:Prefetch |
| `sq032_episode_4.questphase / h0 / 43` | `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene`; `#sq032_04_sm_fourth_episode` | 43:out → 25:In; 52:True → 43:in_q112; 43:out_clean_up → 45:In1; 78:Case1379322888 → 43:Prefetch |
| `sq032_episode_4.questphase / h0 / 48` | `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene`; `#sq032_04_sm_fourth_episode` | 48:out → 26:In; 53:True → 48:in_q105; 48:out_clean_up → 45:In1; 78:Case2173311359 → 48:Prefetch |
| `sq032_episode_5.questphase / h0 / 43` | `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene`; `#sq032_05_sm_fifth_episode` | 43:out → 29:In; 54:True → 43:in_q105; 43:out_clean_up → 48:In1; 58:Case2173311359 → 43:Prefetch |
| `sq032_episode_5.questphase / h0 / 44` | `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene`; `#sq032_05_sm_fifth_episode` | 44:out → 23:In; 55:True → 44:in_q110; 44:out_clean_up → 48:In1; 58:Case285067426 → 44:Prefetch |
| `sq032_episode_5.questphase / h0 / 45` | `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene`; `#sq032_05_sm_fifth_episode` | 45:out → 24:In; 52:True → 45:in_q104; 45:out_clean_up → 48:In1; 58:Case2488326877 → 45:Prefetch |
| `sq032_episode_5.questphase / h0 / 46` | `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene`; `#sq032_05_sm_fifth_episode` | 46:out → 25:In; 53:True → 46:in_q112; 46:out_clean_up → 48:In1; 58:Case1379322888 → 46:Prefetch |
| `sq032_episode_6.questphase / h0 / 84` | `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene`; `#sq032_06_sm_sixth_episode` | 84:out → 5:In; 69:True → 84:in_q110; 90:Case285067426 → 84:Prefetch |
| `sq032_episode_6.questphase / h0 / 87` | `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene`; `#sq032_06_sm_sixth_episode` | 87:out → 5:In; 66:True → 87:in_q104; 90:Case2488326877 → 87:Prefetch |
| `sq032_episode_6.questphase / h0 / 88` | `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene`; `#sq032_06_sm_sixth_episode` | 88:out → 5:In; 67:True → 88:in_q112; 90:Case1379322888 → 88:Prefetch |
| `sq032_episode_6.questphase / h47 / 13` | `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene`; `#sq032_06_sm_sixth_episode` | 0:Out → 13:in_q110; 13:out → 1:In |
| `sq032_episode_6.questphase / h75 / 9` | `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene`; `#sq032_06_sm_sixth_episode` | 0:Out → 9:in_q104; 9:out → 1:In |
| `sq032_episode_6.questphase / h96 / 9` | `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene`; `#sq032_06_sm_sixth_episode` | 0:Out → 9:in_q112; 9:out → 1:In |
| `sq032_finale.questphase / h0 / 10` | `base\quest\side_quests\sq032\scenes\sq032_07_finale.scene`; `#sq032_07_sm_finale` | 2:Out → 10:in; 10:out → 23:In |
| `sq032.questphase / h0 / 50` | `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` | 50:Out1 → 83:In; 50:Out1 → 51:In1; 95:Out1 → 50:In1 |
| `sq032.questphase / h0 / 51` | `base\quest\side_quests\sq032\phases\sq032_episode_4.questphase` | 50:Out1 → 51:In1; 51:Out1 → 83:In; 51:Out1 → 52:In1; 78:Out → 51:In1 |
| `sq032.questphase / h0 / 52` | `base\quest\side_quests\sq032\phases\sq032_episode_5.questphase` | 51:Out1 → 52:In1; 52:Out1 → 53:In1; 52:Out1 → 83:In; 79:Out → 52:In1 |
| `sq032.questphase / h0 / 53` | `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` | 52:Out1 → 53:In1; 80:Out → 53:In1; 53:Out1 → 96:In1 |
| `sq032.questphase / h0 / 96` | `base\quest\side_quests\sq032\phases\sq032_finale.questphase` | 53:Out1 → 96:In1; 96:Out1 → 103:In1; 96:Out1 → 107:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\side_quests\sq032\sq032.questphase` / h0 / 50 | `sq032_episode_3.questphase` | 95: Phase; 50:Out1 → 83:In; 50:Out1 → 51:In1; 95:Out1 → 50:In1 |
| `base\quest\side_quests\sq032\sq032.questphase` / h0 / 51 | `sq032_episode_4.questphase` | 50: Phase: sq032_episode_3.questphase; 78: Input; 50:Out1 → 51:In1; 51:Out1 → 83:In; 51:Out1 → 52:In1; 78:Out → 51:In1 |
| `base\quest\side_quests\sq032\sq032.questphase` / h0 / 52 | `sq032_episode_5.questphase` | 51: Phase: sq032_episode_4.questphase; 79: Input; 51:Out1 → 52:In1; 52:Out1 → 53:In1; 52:Out1 → 83:In; 79:Out → 52:In1 |
| `base\quest\side_quests\sq032\sq032.questphase` / h0 / 53 | `sq032_episode_6.questphase` | 52: Phase: sq032_episode_5.questphase; 80: Input; 52:Out1 → 53:In1; 80:Out → 53:In1; 53:Out1 → 96:In1 |
| `base\quest\side_quests\sq032\sq032.questphase` / h0 / 96 | `sq032_finale.questphase` | 53: Phase: sq032_episode_6.questphase; 53:Out1 → 96:In1; 96:Out1 → 103:In1; 96:Out1 → 107:In |
| `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` / h0 / 66 | `sq032_03_third_episode.scene` | 74: Condition: #sq032_tr_roadhouse; 88: Switch: sq032_q104_prefetch; sq032_q105_prefetch; 66:out → 48:In; 74:True → 66:in_q104; 66:out_clean_up → 70:In1; 88:Case2488326877 → 66:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` / h0 / 80 | `sq032_03_third_episode.scene` | 75: Condition: #sq032_tr_dollhouse; 88: Switch: sq032_q104_prefetch; sq032_q105_prefetch; 80:out → 50:In; 80:out_clean_up → 70:In1; 75:True → 80:in_q105; 88:Case2173311359 → 80:Prefetch |
| `base\quest\main_quests\prologue\q003\phases\q003_stout.questphase` / h575 / 3 | `sq032_04_fourth_episode.scene` | 5: PauseCondition: q003_johnny_comment_cat; 5:Out → 3:q003_cat_reaction_in; 3:q003_cat_reaction_out → 7:In |
| `base\quest\side_quests\sq032\phases\sq032_episode_4.questphase` / h0 / 41 | `sq032_04_fourth_episode.scene` | 54: Condition: #sq032_tr_chapel; 78: Switch: sq032_q104_prefetch; sq032_q105_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 41:out → 23:In; 54:True → 41:in_q110; 41:out_clean_up → 45:In1; 78:Case285067426 → 41:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_4.questphase` / h0 / 42 | `sq032_04_fourth_episode.scene` | 51: Condition: #sq032_tr_roadhouse; 78: Switch: sq032_q104_prefetch; sq032_q105_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 42:out → 24:In; 51:True → 42:in_q104; 42:out_clean_up → 45:In1; 78:Case2488326877 → 42:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_4.questphase` / h0 / 43 | `sq032_04_fourth_episode.scene` | 52: Condition: #sq032_tr_motel; 78: Switch: sq032_q104_prefetch; sq032_q105_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 43:out → 25:In; 52:True → 43:in_q112; 43:out_clean_up → 45:In1; 78:Case1379322888 → 43:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_4.questphase` / h0 / 48 | `sq032_04_fourth_episode.scene` | 53: Condition: #sq032_tr_dollhouse; 78: Switch: sq032_q104_prefetch; sq032_q105_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 48:out → 26:In; 53:True → 48:in_q105; 48:out_clean_up → 45:In1; 78:Case2173311359 → 48:Prefetch |
| `base\quest\bugfixing\sidequests\sq032\sq032_cinematic_bugfixes.questphase` / h115 / 5 | `sq032_05_fifth_episode.scene` | 29: EquipItem; 5:cigarette_prop_removal_out → 1:In; 29:Out → 5:cigarette_prop_removal |
| `base\quest\side_quests\sq032\phases\sq032_episode_5.questphase` / h0 / 43 | `sq032_05_fifth_episode.scene` | 54: Condition: #sq032_tr_dollhouse; 58: Switch: sq032_q104_prefetch; sq032_q105_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 43:out → 29:In; 54:True → 43:in_q105; 43:out_clean_up → 48:In1; 58:Case2173311359 → 43:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_5.questphase` / h0 / 44 | `sq032_05_fifth_episode.scene` | 55: Condition: #sq032_tr_chapel; 58: Switch: sq032_q104_prefetch; sq032_q105_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 44:out → 23:In; 55:True → 44:in_q110; 44:out_clean_up → 48:In1; 58:Case285067426 → 44:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_5.questphase` / h0 / 45 | `sq032_05_fifth_episode.scene` | 52: Condition: #sq032_tr_roadhouse; 58: Switch: sq032_q104_prefetch; sq032_q105_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 45:out → 24:In; 52:True → 45:in_q104; 45:out_clean_up → 48:In1; 58:Case2488326877 → 45:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_5.questphase` / h0 / 46 | `sq032_05_fifth_episode.scene` | 53: Condition: #sq032_tr_motel; 58: Switch: sq032_q104_prefetch; sq032_q105_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 46:out → 25:In; 53:True → 46:in_q112; 46:out_clean_up → 48:In1; 58:Case1379322888 → 46:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` / h0 / 84 | `sq032_06_sixth_episode.scene` | 69: Condition: #sq032_tr_chapel; 90: Switch: sq032_q104_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 84:out → 5:In; 69:True → 84:in_q110; 90:Case285067426 → 84:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` / h0 / 87 | `sq032_06_sixth_episode.scene` | 66: Condition: #sq032_tr_roadhouse; 90: Switch: sq032_q104_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 87:out → 5:In; 66:True → 87:in_q104; 90:Case2488326877 → 87:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` / h0 / 88 | `sq032_06_sixth_episode.scene` | 67: Condition: #sq032_tr_motel; 90: Switch: sq032_q104_prefetch; sq032_q110_prefetch; sq032_q112_prefetch; 88:out → 5:In; 67:True → 88:in_q112; 90:Case1379322888 → 88:Prefetch |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` / h47 / 13 | `sq032_06_sixth_episode.scene` | 0: Input; 0:Out → 13:in_q110; 13:out → 1:In |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` / h75 / 9 | `sq032_06_sixth_episode.scene` | 0: Input; 0:Out → 9:in_q104; 9:out → 1:In |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` / h96 / 9 | `sq032_06_sixth_episode.scene` | 0: Input; 0:Out → 9:in_q112; 9:out → 1:In |
| `base\quest\side_quests\sq032\phases\sq032_finale.questphase` / h0 / 10 | `sq032_07_finale.scene` | 2: TeleportPuppet; 2:Out → 10:in; 10:out → 23:In |
| `base\quest\main_quests\part1\q105\q105_main.quest` / h0 / 60 | `sq032.questphase` | 58: LogicalHub; 58:Out1 → 60:In1 |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 75 | `sq032.questphase` | 71: FactsDBManager: q110_active; 71:Out → 75:InEp06 |
| `base\quest\side_quests\sidequests.questphase` / h0 / 94 | `sq032.questphase` | 31: PauseCondition: q101_enable_side_content; 195: LogicalHub; 194: FactsDBManager: sq032_q104_used; 31:Out → 94:In1; 94:Out1 → 38:In1; 195:Out1 → 94:InEp05; 194:Out → 94:InEp06 |
| `base\quest\side_quests\sq032\sq032.quest` / h0 / 2 | `sq032.questphase` | 4: Scene: sq032_chicken_test.scene; 4: Scene: sq032_chicken_test.scene; 4: Scene: sq032_chicken_test.scene; 4: Scene: sq032_chicken_test.scene; 4:out → 2:In1; 4:out_05 → 2:InEp05; 4:out_04 → 2:InEp04; 4:out_06 → 2:InEp06 |
| `base\quest\main_quests\prologue\q003\q003.quest` / h0 / 28 | `q003_stout.questphase` |  |
| `base\quest\minor_quests\mq000\mq000.quest` / h0 / 14 | `q003_stout.questphase` |  |
| `base\quest\persistent_content.questphase` / h2254 / 2 | `q003_stout.questphase` | 8: PauseCondition: q003_done; 8:Out → 2:In1 |
| `base\quest\bugfixing\cinematic_bugfixing.questphase` / h138 / 19 | `sq032_cinematic_bugfixes.questphase` | 2: Input; 2:Out → 19:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 5 | `sidequests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:sq026_02_signal → 5:sq026_02_signal; 7:Out1 → 5:In1; 8:Out → 5:In1; 21:Out → 5:EP1_Standalone |
| `base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.quest` / h0 / 10 | `persistent_content.questphase` | 0: Start; 0:Out → 10:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 17 | `persistent_content.questphase` | 0: Input; 36: Input; 0:Out → 17:In1; 36:Out → 17:EP1_Standalone |
| `base\quest\main_quests\part1\q108\q108_johnny.quest` / h0 / 24 | `persistent_content.questphase` | 0: Start; 0:Out → 24:In1 |
| `base\quest\minor_quests\mq025\batty\batty_quest.quest` / h0 / 3 | `persistent_content.questphase` | 0: Start; 0:Out → 3:In1 |
| `base\quest\bugfixing.questphase` / h0 / 10 | `cinematic_bugfixing.questphase` | 16: DeletionMarker; 10:sq026_02_signal → 21:In; 16:Out → 10:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest` / h0 / 10 | `additional_game_elements.questphase` | 1: Start; 1:Out → 10:Input |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest` / h0 / 4 | `additional_game_elements.questphase` | 5: FactsDBManager: sts_bls_ina_tier_1; 5:Out → 4:Input |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest` / h0 / 6 | `additional_game_elements.questphase` | 4: FactsDBManager: sts_bls_ina_tier_1; 4:Out → 6:Input |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest` / h0 / 5 | `additional_game_elements.questphase` | 4: FactsDBManager: sts_cct_dtn_tier_1; 4:Out → 5:Input |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_cct_dtn_tier_1; 3:Out → 2:Input |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest` / h0 / 6 | `additional_game_elements.questphase` | 4: Scene: ma_hey_spr_04_00_chickentest.scene; 4:End 0 → 6:Input |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest` / h0 / 4 | `additional_game_elements.questphase` | 5: FactsDBManager: sts_hey_spr_tier_1; 5:Out → 4:Input |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest` / h0 / 4 | `additional_game_elements.questphase` | 3: Scene: ma_pac_cvi_08_00_chickentest.scene; 3:End 0 → 4:Input |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_pac_cvi_tier_1; 3:Out → 2:Input |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest` / h0 / 3 | `additional_game_elements.questphase` | 2: Scene: mq_std_rcr_11_00_chickentest.scene; 2:End 0 → 3:Input |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest` / h0 / 6 | `additional_game_elements.questphase` | 1: Start; 1:Out → 6:Input |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest` / h0 / 7 | `additional_game_elements.questphase` | 3: FactsDBManager: sts_wat_kab_tier_1; 3:Out → 7:Input |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest` / h0 / 2 | `additional_game_elements.questphase` | 3: Scene: ma_wat_lch_06_chicken_test.scene; 3:End 0 → 2:Input |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest` / h0 / 8 | `additional_game_elements.questphase` | 9: FactsDBManager: ow_psychos_intro_done; 9:Out → 8:Input |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest` / h0 / 6 | `additional_game_elements.questphase` | 8: LogicalHub; 8:Out1 → 6:Input |
| `base\quest\cyberpunk2077.questphase` / h520 / 3 | `additional_game_elements.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 9:Out1 → 3:Input; 21:Out → 3:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 20 | `additional_game_elements.questphase` | 25: LogicalHub; 25:Out1 → 20:Input |
| `base\quest\main_quests\epilogue\q201\q201_heir.quest` / h0 / 29 | `additional_game_elements.questphase` | 11: Start; 11:Out → 29:Input |
| `base\quest\main_quests\epilogue\q202\q202.quest` / h0 / 22 | `additional_game_elements.questphase` | 0: Start; 0:Out → 22:Input |
| `base\quest\main_quests\epilogue\q203\q203_legend.quest` / h0 / 30 | `additional_game_elements.questphase` | 27: FactsDBManager: q204_var_test_def; 27:Out → 30:Input |
| `base\quest\main_quests\epilogue\q204\q204_reborn.quest` / h0 / 6 | `additional_game_elements.questphase` | 0: Start; 0:Out → 6:Input |
| `base\quest\main_quests\part1\q101\q101.quest` / h0 / 30 | `additional_game_elements.questphase` | 0: Start; 0:Out → 30:Input |
| `base\quest\main_quests\part1\q103\q103.quest` / h0 / 45 | `additional_game_elements.questphase` | 0: Start; 0:Out → 45:Input |
| `base\quest\main_quests\part1\q105\q105_main.quest` / h0 / 40 | `additional_game_elements.questphase` | 58: LogicalHub; 58:Out1 → 40:Input |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 17 | `additional_game_elements.questphase` | 0: Start; 0:Out → 17:Input |
| `base\quest\main_quests\part1\q112\q112_abduction.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\main_quests\part1\q113\q113.quest` / h0 / 40 | `additional_game_elements.questphase` | 36: FactsDBManager: q113_active; 36:Out → 40:Input |
| `base\quest\main_quests\part1\q114\q114_nomads.quest` / h0 / 16 | `additional_game_elements.questphase` | 0: Start; 0:Out → 16:Input |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 57 | `additional_game_elements.questphase` | 0: Start; 0:Out → 57:Input |
| `base\quest\main_quests\prologue\q000\q000.quest` / h0 / 10 | `additional_game_elements.questphase` | 2: Start; 2:Out → 10:Input |
| `base\quest\main_quests\prologue\q001\q001.quest` / h0 / 30 | `additional_game_elements.questphase` | 120: LogicalHub; 120:Out1 → 30:Input |
| `base\quest\main_quests\prologue\q003\q003.quest` / h0 / 26 | `additional_game_elements.questphase` | 0: Start; 0:Out → 26:Input |
| `base\quest\main_quests\prologue\q004\q004.quest` / h0 / 1087 | `additional_game_elements.questphase` | 24: Start; 24:Out → 1087:Input |
| `base\quest\main_quests\prologue\q005\q005_heist.quest` / h0 / 14 | `additional_game_elements.questphase` | 17: FactsDBManager: jackie_default_on write/default comparison 0; 17:Out → 14:Input |
| `base\quest\minor_quests\mq000\mq000.quest` / h0 / 12 | `additional_game_elements.questphase` | 3: Scene: mq000_00_chickentest.scene; 3:out → 12:Input |
| `base\quest\minor_quests\mq001\mq001.quest` / h0 / 10 | `additional_game_elements.questphase` | 21: Start; 21:Out → 10:Input |
| `base\quest\minor_quests\mq003\mq003_orbitals.quest` / h0 / 7 | `additional_game_elements.questphase` | 2: Start; 2:Out → 7:Input |
| `base\quest\minor_quests\mq006\mq006.quest` / h0 / 7 | `additional_game_elements.questphase` | 6: Scene: mq006_chicken_test.scene; 6:End 0 → 7:Input |
| `base\quest\minor_quests\mq007\mq007.quest` / h0 / 10 | `additional_game_elements.questphase` | 0: Start; 0:Out → 10:Input |
| `base\quest\minor_quests\mq008\mq008.quest` / h0 / 14 | `additional_game_elements.questphase` | 0: Start; 0:Out → 14:Input |
| `base\quest\minor_quests\mq011\mq011.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq012\mq012.quest` / h0 / 9 | `additional_game_elements.questphase` | 1: Start; 1:Out → 9:Input |
| `base\quest\minor_quests\mq013\mq013.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Start; 1:Out → 4:Input |
| `base\quest\minor_quests\mq014\mq014.quest` / h0 / 5 | `additional_game_elements.questphase` | 0: Start; 0:Out → 5:Input |
| `base\quest\minor_quests\mq015\mq015_wizardbook.quest` / h0 / 7 | `additional_game_elements.questphase` | 0: Start; 0:Out → 7:Input |
| `base\quest\minor_quests\mq016\mq016_bartmoss.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\minor_quests\mq017\mq017_streetkid.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq018\mq018.quest` / h0 / 5 | `additional_game_elements.questphase` | 1: Phase: mq018_00_chickentest.questphase; 1:additional_content_out → 5:Input |
| `base\quest\minor_quests\mq019\mq019_paparazzi.quest` / h0 / 7 | `additional_game_elements.questphase` | 0: Start; 0:Out → 7:Input |
| `base\quest\minor_quests\mq021\mq021.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq022\mq022.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq023\mq023_bootleg.quest` / h0 / 11 | `additional_game_elements.questphase` | 1: Start; 1:Out → 11:Input |
| `base\quest\minor_quests\mq024\mq024.quest` / h0 / 15 | `additional_game_elements.questphase` | 0: Start; 0:Out → 15:Input |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.quest` / h0 / 4 | `additional_game_elements.questphase` | 10: FactsDBManager: disable_tutorials; 10:Out → 4:Input |
| `base\quest\minor_quests\mq026\mq026.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Phase: mq026_00_chickentest.questphase; 1:additional_content_out → 4:Input |
| `base\quest\minor_quests\mq028\mq028.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Phase: mq028_00_chickentest.questphase; 1:additional_content_out → 4:Input |
| `base\quest\minor_quests\mq030\mq030.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\minor_quests\mq032\mq032_sacrum.quest` / h0 / 12 | `additional_game_elements.questphase` | 0: Start; 0:Out → 12:Input |
| `base\quest\minor_quests\mq033\mq033_tarot.quest` / h0 / 2 | `additional_game_elements.questphase` | 0: Start; 0:Out → 2:Input |
| `base\quest\minor_quests\mq035\mq035_ozob.quest` / h0 / 5 | `additional_game_elements.questphase` | 4: Scene: mq035_chicken_test.scene; 4:start → 5:Input |
| `base\quest\minor_quests\mq037\mq037_brendan.quest` / h0 / 4 | `additional_game_elements.questphase` | 0: Start; 0:Out → 4:Input |
| `base\quest\minor_quests\mq038\mq038.quest` / h0 / 5 | `additional_game_elements.questphase` | 2: Start; 2:Out → 5:Input |
| `base\quest\minor_quests\mq040\mq040_biosculpt.quest` / h0 / 10 | `additional_game_elements.questphase` | 22: Condition: mq040_add_ele_on Equal 1; 22:True → 10:Input |
| `base\quest\minor_quests\mq041\mq041_corpo.quest` / h0 / 8 | `additional_game_elements.questphase` | 1: Start; 1:Out → 8:Input |
| `base\quest\minor_quests\mq048\mq048.quest` / h0 / 12 | `additional_game_elements.questphase` | 1: Start; 1:Out → 12:Input |
| `base\quest\minor_quests\mq055\mq055.quest` / h0 / 4 | `additional_game_elements.questphase` | 3: Scene: mq055_chicken.scene; 3:End 0 → 4:EP1_Standalone |
| `base\quest\side_quests\sq004\sq004_riders_quest.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq006\sq006.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq011\sq011.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq012\sq012_the_law.quest` / h0 / 6 | `additional_game_elements.questphase` | 2: Start; 2:Out → 6:Input |
| `base\quest\side_quests\sq017\sq017.quest` / h0 / 5 | `additional_game_elements.questphase` | 0: Start; 0:Out → 5:Input |
| `base\quest\side_quests\sq018\sq018.quest` / h0 / 24 | `additional_game_elements.questphase` | 16: Start; 16:Out → 24:Input |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 17 | `additional_game_elements.questphase` | 0: Start; 0:Out → 17:Input |
| `base\quest\side_quests\sq023\sq023.quest` / h0 / 15 | `additional_game_elements.questphase` | 0: Start; 0:Out → 15:Input |
| `base\quest\side_quests\sq024\sq024.quest` / h0 / 29 | `additional_game_elements.questphase` | 0: Start; 0:Out → 29:Input |
| `base\quest\side_quests\sq025\sq025.quest` / h0 / 66 | `additional_game_elements.questphase` | 49: Phase; 49:additional_content_out → 66:Input |
| `base\quest\side_quests\sq026\sq026.quest` / h0 / 9 | `additional_game_elements.questphase` | 0: Start; 0:Out → 9:Input |
| `base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest` / h0 / 8 | `additional_game_elements.questphase` | 0: Start; 0:Out → 8:Input |
| `base\quest\side_quests\sq028\sq028.quest` / h0 / 4 | `additional_game_elements.questphase` | 0: Start; 0:Out → 4:Input |
| `base\quest\side_quests\sq029\sq029.quest` / h0 / 20 | `additional_game_elements.questphase` | 1: Start; 1:Out → 20:Input |
| `base\quest\side_quests\sq030\sq030.quest` / h0 / 11 | `additional_game_elements.questphase` | 4: SceneManager; 4:Out → 11:Input |
| `base\quest\side_quests\sq031\sq031.quest` / h0 / 6 | `additional_game_elements.questphase` | 0: Start; 0:Out → 6:Input |
| `base\quest\side_quests\sq032\sq032.quest` / h0 / 12 | `additional_game_elements.questphase` | 0: Start; 0:Out → 12:Input |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 11 | `additional_game_elements.questphase` | 6: FactsDBManager: ep1_side_content; 6:Out → 11:Input |
| `ep1\quest\main_quests\q304\q304.quest` / h0 / 20 | `additional_game_elements.questphase` | 12: Checkpoint; 12:Out → 20:EP1_Standalone |
| `ep1\quest\main_quests\q305\q305.quest` / h0 / 5 | `additional_game_elements.questphase` | 1: Start; 1:Out → 5:Input |
| `ep1\quest\main_quests\q306\q306.quest` / h0 / 8 | `additional_game_elements.questphase` | 9: PauseCondition: q306_DEBUG_useBaseGameAdditionalGameElements; 9:Out → 8:Input |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 3 | `additional_game_elements.questphase` | 4: LogicalHub; 10: CutControl; 4:Out1 → 3:Input; 10:CutSource → 3:CutDestination |
| `ep1\quest\minor_quests\mq301\mq301.quest` / h0 / 7 | `additional_game_elements.questphase` | 1: Start; 1:Out → 7:Input |
| `ep1\quest\minor_quests\mq303\mq303.quest` / h95 / 2 | `additional_game_elements.questphase` | 0: Input; 0:Out → 2:Input |
| `ep1\quest\minor_quests\mq304\mq304.quest` / h130 / 3 | `additional_game_elements.questphase` | 4: LogicalHub; 4:Out1 → 3:Input |
| `ep1\quest\minor_quests\mq305\mq305.quest` / h0 / 4 | `additional_game_elements.questphase` | 1: Start; 1:Out → 4:Input |
| `base\quest\cyberpunk2077.questphase` / h520 / 4 | `bugfixing.questphase` | 9: LogicalHub; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:Out_res_act1 → 14:In; 4:to_mq025 → 6:to_mq025; 4:sq026_02_signal → 5:sq026_02_signal; 9:Out1 → 4:In1; 21:Out → 4:In1; 4:CYB-656199 → 15:In; 4:ep1_active_out → 23:In |
| `base\quest\main_quests\epilogue\q201\q201_heir.quest` / h0 / 44 | `bugfixing.questphase` | 11: Start; 11:Out → 44:In1 |
| `base\quest\main_quests\part1\q101\q101.quest` / h0 / 47 | `bugfixing.questphase` | 0: Start; 0:Out → 47:In1 |
| `base\quest\main_quests\part1\q110\q110.quest` / h0 / 76 | `bugfixing.questphase` | 0: Start; 0:Out → 76:In1 |
| `base\quest\main_quests\part1\q112\q112_abduction.quest` / h0 / 23 | `bugfixing.questphase` | 0: Start; 0:Out → 23:In1 |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 140 | `bugfixing.questphase` | 0: Start; 0:Out → 140:In1 |
| `base\quest\minor_quests\mq026\mq026.quest` / h0 / 5 | `bugfixing.questphase` | 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1: Phase: mq026_00_chickentest.questphase; 1:Out1 → 5:In1; 1:conspiracy_out → 5:In1; 1:combat_out → 5:In1; 1:death_out → 5:In1 |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 61 | `bugfixing.questphase` | 0: Start; 0:Out → 61:In1 |
| `base\quest\side_quests\sq023\sq023.quest` / h0 / 20 | `bugfixing.questphase` | 0: Start; 0:Out → 20:In1 |
| `base\quest\side_quests\sq025\sq025.quest` / h0 / 68 | `bugfixing.questphase` | 49: Phase; 49:additional_content_out → 68:In1 |
| `base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest` / h0 / 64 | `bugfixing.questphase` | 0: Start; 0:Out → 64:In1 |
| `ep1\quest\main_quests\q307\q307.quest` / h128 / 13 | `bugfixing.questphase` | 11: LogicalHub; 11:Out1 → 13:In1 |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sq032_03_third_episode.scene` | Start 1, in_q105, in_q104, preview_02 → out_clean_up, out | Johnny; Player; 172 nodes / 198 edges |
| `sq032_04_fourth_episode.scene` | in_q105, in_q110, in_q104, in_q112, q104_end, q003_cat_reaction_in, q112_end, Start1 → out, q003_cat_reaction_out, out_clean_up | Johnny; johnny_spawnset_cat; Player; 248 nodes / 322 edges |
| `sq032_05_fifth_episode.scene` | in_q105, in_q110, in_q104, in_q112, Start 1, cigarette_prop_removal → out, out_clean_up, cigarette_prop_removal_out | Johnny; women; man; Player; 191 nodes / 226 edges |
| `sq032_06_sixth_episode.scene` | in_q110, in_q104, in_q112 → out | Johnny; Player; 70 nodes / 89 edges |
| `sq032_07_finale.scene` | in, Start 1, Start 2, Start 0 → out, out_clean_up | Johnny; Player; 222 nodes / 266 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sq032_03_third_episode.scene / n107 / 0` | You don't care if I live. (`change`) | No option-level predicate stored | 0:0 → 137:0:0 |
| `sq032_03_third_episode.scene / n107 / 1` | Leave me alone. (`leave me be`) | No option-level predicate stored | 0:1 → 170:0:0 |
| `sq032_03_third_episode.scene / n116 / 0` | What do Soulkiller and Mikoshi have to do with me? (`mikoshi`) | No option-level predicate stored | 0:0 → 118:0:0 |
| `sq032_03_third_episode.scene / n116 / 1` | Ravings of a lunatic. (`no sense`) | No option-level predicate stored | 0:1 → 240:0:0 |
| `sq032_03_third_episode.scene / n139 / 0` | Gonna make a terrorist of me? (`terrorist`) | No option-level predicate stored | 0:0 → 141:0:0; 0:0 → 3833:0:1 |
| `sq032_03_third_episode.scene / n139 / 1` | Funny guy. (`funny_guy`) | No option-level predicate stored | 0:1 → 143:0:0; 0:1 → 176:0:0 |
| `sq032_03_third_episode.scene / n139 / 2` | For some ideal? Or to square a grudge? (`vendetta`) | No option-level predicate stored | 0:2 → 218:0:0 |
| `sq032_03_third_episode.scene / n145 / 0` | Mikoshi – what's that, exactly? (`what is mikoshi`) | No option-level predicate stored | 0:0 → 150:0:0 |
| `sq032_03_third_episode.scene / n145 / 1` | But I don't trust you. (`dont trust you`) | No option-level predicate stored | 0:1 → 152:0:0 |
| `sq032_03_third_episode.scene / n145 / 2` | You're just a hallucination. (`you only a ghost`) | No option-level predicate stored | 0:2 → 896:0:1 |
| `sq032_03_third_episode.scene / n154 / 0` | Mikoshi – what's that, exactly? (`what is mikoshi`) | No option-level predicate stored | 0:0 → 150:0:0 |
| `sq032_03_third_episode.scene / n154 / 1` | Not particularly. (`not really`) | No option-level predicate stored | 0:1 → 157:0:0 |
| `sq032_03_third_episode.scene / n159 / 0` | Me and Mikoshi – how're we linked at all? (`me and mikoshi`) | No option-level predicate stored | 0:0 → 382:0:0 |
| `sq032_03_third_episode.scene / n159 / 1` | Cut to the chase. (`why`) | No option-level predicate stored | 0:1 → 161:0:0 |
| `sq032_03_third_episode.scene / n178 / 0` | Arasaka – how you plan to destroy it this time? (`destroy arasaka`) | No option-level predicate stored | 0:0 → 249:0:0 |
| `sq032_03_third_episode.scene / n178 / 1` | [Stand] OK, talked enough. (`end talk`) | No option-level predicate stored | 0:1 → 327:0:0 |
| `sq032_03_third_episode.scene / n203 / 0` | Asked you – what the hell do you want? (`change`) | No option-level predicate stored | 0:0 → 198:0:0 |
| `sq032_03_third_episode.scene / n203 / 1` | Fucked in the head worse than me. (`full_life`) | No option-level predicate stored | 0:1 → 201:0:0 |
| `sq032_03_third_episode.scene / n265 / 0` | Following. (`yes`) | No option-level predicate stored | 0:0 → 567:0:0 |
| `sq032_03_third_episode.scene / n265 / 1` | Yep, saw what happened to you. (`yes_memory`) | No option-level predicate stored | 0:1 → 271:0:0 |
| `sq032_03_third_episode.scene / n265 / 2` | Don't care. (`bonkers`) | No option-level predicate stored | 0:2 → 280:0:0 |
| `sq032_03_third_episode.scene / n297 / 0` | [Sit] Dunno. (`Option_15`) | No option-level predicate stored | 0:0 → 300:0:0 |
| `sq032_03_third_episode.scene / n298 / 0` | [Sit] (`Option_16`) | No option-level predicate stored | 0:0 → 304:0:0 |
| `sq032_03_third_episode.scene / n393 / 0` | [Stand] (`get_up`) | No option-level predicate stored | 0:0 → 395:0:0 |
| `sq032_03_third_episode.scene / n591 / 0` | What do you want from me? (`Option`) | No option-level predicate stored | 0:0 → 589:0:0 |
| `sq032_04_fourth_episode.scene / n36 / 0` | Arasaka killed you, too, 'member. (`arasaka killed u`) | No option-level predicate stored | 0:0 → 113:0:1 |
| `sq032_04_fourth_episode.scene / n36 / 1` | Piss off. (`piss off`) | No option-level predicate stored | 0:1 → 412:0:0 |
| `sq032_04_fourth_episode.scene / n36 / 2` | What the fuck you want – just tell me. (`what you want`) | No option-level predicate stored | 0:2 → 43:0:0 |
| `sq032_04_fourth_episode.scene / n44 / 0` | [Sit] Seem to know a lot about my past. (`howdo you know`) | No option-level predicate stored | 0:0 → 45:0:0; 0:0 → 708:0:1; 0:0 → 986:0:1 |
| `sq032_04_fourth_episode.scene / n44 / 1` | You're the worst kind of asshole. (`youre_the_worst`) | No option-level predicate stored | 0:1 → 57:0:0 |
| `sq032_04_fourth_episode.scene / n47 / 0` | That pisses me off. (`memorymix`) | No option-level predicate stored | 0:0 → 56:0:0 |
| `sq032_04_fourth_episode.scene / n47 / 1` | Scared I'll lose myself, stop being me. (`loose_myself`) | No option-level predicate stored | 0:1 → 58:0:0 |
| `sq032_04_fourth_episode.scene / n47 / 2` | Why can't you just leave me alone? (`why_me`) | No option-level predicate stored | 0:2 → 439:0:0 |
| `sq032_04_fourth_episode.scene / n63 / 0` | What do you want from me, really? (`arasakabis`) | No option-level predicate stored | 0:0 → 67:0:0 |
| `sq032_04_fourth_episode.scene / n63 / 1` | The moment when I turn into you – will I notice it? (`both_ways`) | No option-level predicate stored | 0:1 → 211:0:0 |
| `sq032_04_fourth_episode.scene / n63 / 2` | How's life in my body? (`say_more`) | No option-level predicate stored | 0:2 → 71:0:0 |
| `sq032_04_fourth_episode.scene / n65 / 0` | You afraid of death? (`death_Scared`) | No option-level predicate stored | 0:0 → 255:0:0 |
| `sq032_04_fourth_episode.scene / n65 / 1` | What's it like, bein' in someone else's head? (`mysituation`) | No option-level predicate stored | 0:1 → 69:0:0 |
| `sq032_04_fourth_episode.scene / n65 / 2` | [End convo] Don't need your sympathy. (`noneed`) | No option-level predicate stored | 0:2 → 405:0:0 |
| `sq032_04_fourth_episode.scene / n77 / 0` | Incapable of sitting still, letting anything go, aren't you. (`thisisjohnny`) | No option-level predicate stored | 0:0 → 80:0:0 |
| `sq032_04_fourth_episode.scene / n77 / 1` | An enemy – you need to have one at all times. (`need_enemy`) | No option-level predicate stored | 0:1 → 178:0:0 |
| `sq032_04_fourth_episode.scene / n77 / 2` | You got no idea what you want. (`what_you_want`) | No option-level predicate stored | 0:2 → 320:0:0 |
| `sq032_04_fourth_episode.scene / n77 / 3` | Got a clear goal. Like I do. (`common_goal`) | No option-level predicate stored | 0:3 → 324:0:0 |
| `sq032_04_fourth_episode.scene / n186 / 0` | Why're we talkin' about this? (`why even talk`) | No option-level predicate stored | 0:0 → 503:0:0 |
| `sq032_04_fourth_episode.scene / n186 / 1` | Fuckin' leprous Arasaka again? (`q110`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "sq032_04_q110", "value": 1, "comparisonType": "Equal"}}} | 0:1 → 518:0:0 |
| `sq032_04_fourth_episode.scene / n186 / 2` | Paranoid – that's what you are. (`q112`) | {"questCondition": {"$type": "questLogicalCondition", "operation": "OR", "conditions": [{"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "sq032_04_q112", "value": 1, "comparisonType": "Equal"}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "sq032_04_q104", "value": 1, "comparisonType": "Equal"}}]}} | 0:2 → 1113:0:0 |
| `sq032_04_fourth_episode.scene / n186 / 3` | It's a fucking video feed. Chill. (`q104`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "sq032_04_q104", "value": 33, "comparisonType": "Equal"}}} | 0:3 → 1108:0:0 |
| `sq032_04_fourth_episode.scene / n186 / 4` | Whup – another speech about demolishing Arasaka incoming. (`talk arasaka`) | No option-level predicate stored | 0:4 → 16:0:0 |
| `sq032_04_fourth_episode.scene / n186 / 5` | Not up for this discussion. (`dont wanna talk`) | No option-level predicate stored | 0:5 → 412:0:1 |
| `sq032_04_fourth_episode.scene / n331 / 0` | Yeah. (`yes`) | No option-level predicate stored | 0:0 → 550:0:1; 0:0 → 1686:0:1 |
| `sq032_04_fourth_episode.scene / n331 / 1` | [End convo] Hmm... No. (`no`) | No option-level predicate stored | 0:1 → 509:0:0 |
| `sq032_04_fourth_episode.scene / n343 / 0` | Damn straight. (`agree`) | No option-level predicate stored | 0:0 → 345:0:0 |
| `sq032_04_fourth_episode.scene / n343 / 1` | Don't exaggerate. (`exaggerated`) | No option-level predicate stored | 0:1 → 347:0:0 |
| `sq032_04_fourth_episode.scene / n464 / 0` | Let's blow, get outta here… (`terrified1`) | No option-level predicate stored | 0:0 → 443:0:0 |
| `sq032_04_fourth_episode.scene / n469 / 0` | Johnny... (`terrified2`) | No option-level predicate stored | 0:0 → 444:0:0 |
| `sq032_04_fourth_episode.scene / n541 / 0` | [Stand] (`get_up`) | No option-level predicate stored | 0:0 → 544:0:0; 0:0 → 1761:0:0 |
| `sq032_04_fourth_episode.scene / n675 / 0` | [End convo] Not in the mood for your cheap psychoanalysis. (`notyourbuisness`) | No option-level predicate stored | No matching 0:ordinal output; inspect raw stamps |
| `sq032_04_fourth_episode.scene / n803 / 0` | Least I'm still allive. (`snap`) | No option-level predicate stored | 0:0 → 805:0:0 |
| `sq032_04_fourth_episode.scene / n875 / 0` | You've become no one – makes you anxious as fuck. (`Option`) | No option-level predicate stored | 0:0 → 872:0:0 |
| `sq032_04_fourth_episode.scene / n875 / 1` | [End convo] Had enough of this spat. (`I_go`) | No option-level predicate stored | 0:1 → 881:0:0 |
| `sq032_04_fourth_episode.scene / n1026 / 0` | [Stand] (`get_up`) | No option-level predicate stored | 0:0 → 1027:0:0; 0:0 → 1761:0:0 |
| `sq032_04_fourth_episode.scene / n1042 / 0` | [Stand] (`get_up`) | No option-level predicate stored | 0:0 → 1043:0:0; 0:0 → 1761:0:0 |
| `sq032_04_fourth_episode.scene / n1056 / 0` | [Stand] (`get_up`) | No option-level predicate stored | 0:0 → 1057:0:0; 0:0 → 1761:0:0 |
| `sq032_04_fourth_episode.scene / n1170 / 0` | Though not ideal, I'm a nemesis to you, too. (`Option`) | No option-level predicate stored | 0:0 → 1175:0:0 |
| `sq032_04_fourth_episode.scene / n1170 / 1` | [End convo] OK, end of topic. (`I_go`) | No option-level predicate stored | 0:1 → 881:0:1 |
| `sq032_04_fourth_episode.scene / n1178 / 0` | Got no idea who you are, what you're supposed to do. (`Option`) | No option-level predicate stored | 0:0 → 1182:0:0 |
| `sq032_04_fourth_episode.scene / n1178 / 1` | [End convo] OK, done enough tongue flapping. (`I_go`) | No option-level predicate stored | 0:1 → 881:0:0 |
| `sq032_04_fourth_episode.scene / n1180 / 0` | Man, do you go around in circles… (`Option`) | No option-level predicate stored | 0:0 → 1185:0:0 |
| `sq032_04_fourth_episode.scene / n1180 / 1` | [End convo] Heard enough. I'm tired. (`I_go`) | No option-level predicate stored | 0:1 → 881:0:1 |
| `sq032_04_fourth_episode.scene / n1301 / 0` | [End convo] Toodles… (`take`) | No option-level predicate stored | 0:0 → 1329:0:0 |
| `sq032_05_fifth_episode.scene / n62 / 0` | [Stand] Third trimester cramping. (`Option`) | No option-level predicate stored | 0:0 → 54:0:0 |
| `sq032_05_fifth_episode.scene / n62 / 1` | [Stand] Of course it's the chip. (`Option_01`) | No option-level predicate stored | 0:1 → 55:0:0 |
| `sq032_05_fifth_episode.scene / n62 / 2` | [Stand] It's you, you bastard! (`Option_02`) | No option-level predicate stored | 0:2 → 56:0:0 |
| `sq032_05_fifth_episode.scene / n72 / 0` | [Don't smoke] Not good, you're a prick. (`thats_bad`) | No option-level predicate stored | 0:0 → 74:0:0 |
| `sq032_05_fifth_episode.scene / n72 / 1` | [Smoke] Prolly not wrong. (`you_not_wrong`) | No option-level predicate stored | 0:1 → 75:0:0 |
| `sq032_05_fifth_episode.scene / n78 / 0` | But I don't even like you. (`dontlike`) | No option-level predicate stored | 0:0 → 90:0:0 |
| `sq032_05_fifth_episode.scene / n78 / 1` | Problem is you think the ends justify the means. (`masskiller`) | No option-level predicate stored | 0:1 → 89:0:0 |
| `sq032_05_fifth_episode.scene / n78 / 2` | Don't even know where I'm going. (`whowillbe`) | No option-level predicate stored | 0:2 → 91:0:0 |
| `sq032_05_fifth_episode.scene / n111 / 0` | The problem's the madman in my head. (`Option_07`) | No option-level predicate stored | 0:0 → 113:0:0 |
| `sq032_05_fifth_episode.scene / n111 / 1` | We deserve each other. (`Option_08`) | No option-level predicate stored | 0:1 → 114:0:0 |
| `sq032_05_fifth_episode.scene / n111 / 2` | You're unpredictable – that's my point. (`Option_09`) | No option-level predicate stored | 0:2 → 118:0:0 |
| `sq032_05_fifth_episode.scene / n120 / 0` | Guess I understand why you hate Mikoshi. (`Option_10`) | No option-level predicate stored | 0:0 → 129:0:0 |
| `sq032_05_fifth_episode.scene / n120 / 1` | Got what you deserved. (`Option_13`) | No option-level predicate stored | 0:1 → 131:0:0 |
| `sq032_05_fifth_episode.scene / n120 / 2` | Why'd Arasaka build that place? (`Option_29`) | No option-level predicate stored | 0:2 → 803:0:1 |
| `sq032_05_fifth_episode.scene / n120 / 3` | [Stand] Let's get goin'. (`Option_14`) | No option-level predicate stored | 0:3 → 266:0:0 |
| `sq032_05_fifth_episode.scene / n124 / 0` | It's all so fucked up… (`Option_11`) | No option-level predicate stored | 0:0 → 91:0:0 |
| `sq032_05_fifth_episode.scene / n124 / 1` | [Stand] Don't wanna hear it. (`Option_12`) | No option-level predicate stored | 0:1 → 269:0:0 |
| `sq032_05_fifth_episode.scene / n135 / 0` | Eternity – it lasts forever. (`Option_15`) | No option-level predicate stored | 0:0 → 137:0:0 |
| `sq032_05_fifth_episode.scene / n135 / 1` | You're denied the right to die. (`Option_16`) | No option-level predicate stored | 0:1 → 138:0:0 |
| `sq032_05_fifth_episode.scene / n135 / 2` | They can change you into somebody else. (`Option_17`) | No option-level predicate stored | 0:2 → 139:0:0 |
| `sq032_05_fifth_episode.scene / n135 / 3` | They experiment on the human psyche. (`Option_18`) | No option-level predicate stored | 0:3 → 140:0:0 |
| `sq032_05_fifth_episode.scene / n135 / 4` | I dunno. (`Option_19`) | No option-level predicate stored | 0:4 → 141:0:0 |
| `sq032_05_fifth_episode.scene / n156 / 0` | Doin' the same to me, you know. Erasing my identity. (`Option_20`) | No option-level predicate stored | 0:0 → 158:0:0 |
| `sq032_05_fifth_episode.scene / n156 / 1` | [Stand] Enough. Let's go. (`Option_21`) | No option-level predicate stored | 0:1 → 130:0:0 |
| `sq032_05_fifth_episode.scene / n177 / 0` | Got no idea what's happening to me. (`Option_22`) | No option-level predicate stored | 0:0 → 180:0:0 |
| `sq032_05_fifth_episode.scene / n177 / 1` | [Stand] Can't stand you. I'm outta here. (`Option_23`) | No option-level predicate stored | 0:1 → 1062:0:0 |
| `sq032_05_fifth_episode.scene / n177 / 2` | Really don't understand what people saw in you. (`Option_34`) | No option-level predicate stored | 0:2 → 822:0:1 |
| `sq032_05_fifth_episode.scene / n185 / 0` | Dunno where I'm going. (`Option_24`) | No option-level predicate stored | 0:0 → 91:0:0 |
| `sq032_05_fifth_episode.scene / n185 / 1` | [Stand] Need to get our shit together. (`Option_25`) | No option-level predicate stored | 0:1 → 257:0:0 |
| `sq032_05_fifth_episode.scene / n212 / 0` | Maybe. (`maybe`) | No option-level predicate stored | 0:0 → 214:0:0 |
| `sq032_05_fifth_episode.scene / n212 / 1` | Bullshit. (`bullshit`) | No option-level predicate stored | 0:1 → 215:0:0 |
| `sq032_05_fifth_episode.scene / n212 / 2` | [Stand] Let's go. (`lets_go`) | No option-level predicate stored | 0:2 → 1065:0:0 |
| `sq032_05_fifth_episode.scene / n442 / 0` | When you died – what was it like? (`how_it_was_to_die`) | No option-level predicate stored | 0:0 → 218:0:0 |
| `sq032_05_fifth_episode.scene / n442 / 1` | [Stand] Let's delta. (`lets_go`) | No option-level predicate stored | 0:1 → 1065:0:0 |
| `sq032_06_sixth_episode.scene / n44 / 0` | I'm dyin'... (`fine`) | No option-level predicate stored | 0:0 → 53:0:0 |
| `sq032_06_sixth_episode.scene / n80 / 0` | Back again? Got more to spew about the Arasakas? (`options`) | No option-level predicate stored | 0:0 → 34:0:0; 0:0 → 96:0:0 |
| `sq032_06_sixth_episode.scene / n207 / 0` | My first ever extraction – feels good. (`options`) | No option-level predicate stored | 0:0 → 209:0:0; 0:0 → 217:0:0 |
| `sq032_06_sixth_episode.scene / n228 / 0` | What now? (`options`) | No option-level predicate stored | 0:0 → 225:0:0; 0:0 → 232:0:0 |
| `sq032_07_finale.scene / n21 / 0` | [Stand] Almost got flatlined. (`Option`) | No option-level predicate stored | 0:0 → 23:0:0 |
| `sq032_07_finale.scene / n25 / 0` | Where are we? (`where_are_we`) | No option-level predicate stored | 0:0 → 30:0:0 |
| `sq032_07_finale.scene / n25 / 1` | The ocean is beautiful. (`ocean`) | No option-level predicate stored | 0:1 → 27:0:0 |
| `sq032_07_finale.scene / n32 / 0` | [Step away] Why bring me here? (`why_here`) | No option-level predicate stored | 0:0 → 34:0:0 |
| `sq032_07_finale.scene / n32 / 1` | [Step away] Saw Misty's meds in your hand. (`meds`) | No option-level predicate stored | 0:1 → 36:0:0 |
| `sq032_07_finale.scene / n42 / 0` | Got a better idea? (`better idea`) | No option-level predicate stored | 0:0 → 46:0:0 |
| `sq032_07_finale.scene / n42 / 1` | We share the same goals. (`same goal`) | No option-level predicate stored | 0:1 → 47:0:0 |
| `sq032_07_finale.scene / n42 / 2` | Don't start. (`dont start`) | No option-level predicate stored | 0:2 → 43:0:0 |
| `sq032_07_finale.scene / n42 / 3` | I'll do what I need to do to survive. (`corpo`) | No option-level predicate stored | 0:3 → 44:0:0 |
| `sq032_07_finale.scene / n49 / 0` | That your last wish – revenge? (`last wish`) | No option-level predicate stored | 0:0 → 50:0:0; 0:0 → 740:0:0 |
| `sq032_07_finale.scene / n49 / 1` | Not about to risk my life for this. (`how you imagine`) | No option-level predicate stored | 0:1 → 51:0:0; 0:1 → 740:0:1 |
| `sq032_07_finale.scene / n49 / 2` | Understood. (`understand`) | No option-level predicate stored | 0:2 → 52:0:0; 0:2 → 740:0:2 |
| `sq032_07_finale.scene / n49 / 3` | Suddenly remember Smasher, huh? (`smasher`) | No option-level predicate stored | 0:3 → 496:0:0 |
| `sq032_07_finale.scene / n54 / 0` | Not sure Rogue's so sentimental. (`sentimental`) | No option-level predicate stored | 0:0 → 55:0:0 |
| `sq032_07_finale.scene / n54 / 1` | Not how Rogue operates anymore. (`fixer street`) | No option-level predicate stored | 0:1 → 56:0:0 |
| `sq032_07_finale.scene / n54 / 2` | So I tell Rogue everything? (`you want to tell`) | No option-level predicate stored | 0:2 → 57:0:0 |
| `sq032_07_finale.scene / n54 / 3` | Not true. (`disagree`) | No option-level predicate stored | 0:3 → 236:0:0 |
| `sq032_07_finale.scene / n59 / 0` | Tell me what you're planning. (`exactly`) | No option-level predicate stored | 0:0 → 60:0:0 |
| `sq032_07_finale.scene / n59 / 1` | No deal. (`nope like nope`) | No option-level predicate stored | 0:1 → 61:0:0 |
| `sq032_07_finale.scene / n59 / 2` | Don't know if I trust you. (`trust`) | No option-level predicate stored | 0:2 → 63:0:0 |
| `sq032_07_finale.scene / n59 / 3` | I can see what you're up to. (`other reason`) | No option-level predicate stored | 0:3 → 67:0:0 |
| `sq032_07_finale.scene / n59 / 4` | So, Hellman was right. (`hellman`) | No option-level predicate stored | 0:4 → 62:0:0 |
| `sq032_07_finale.scene / n64 / 0` | OK, I'll give you control. (`yes`) | No option-level predicate stored | 0:0 → 66:0:0 |
| `sq032_07_finale.scene / n64 / 1` | Not gonna happen. (`nope`) | No option-level predicate stored | 0:1 → 68:0:0 |
| `sq032_07_finale.scene / n64 / 2` | Need to think about it. (`will think`) | No option-level predicate stored | 0:2 → 69:0:0 |
| `sq032_07_finale.scene / n65 / 0` | Might be you're right, might be a good idea. (`coward`) | No option-level predicate stored | 0:0 → 66:0:0 |
| `sq032_07_finale.scene / n65 / 1` | End of discussion. (`manipulative`) | No option-level predicate stored | 0:1 → 68:0:0 |
| `sq032_07_finale.scene / n65 / 2` | Need to think about it. (`will think about it`) | No option-level predicate stored | 0:2 → 69:0:0 |
| `sq032_07_finale.scene / n124 / 0` | Seriously consider taking the meds from Misty? (`want`) | No option-level predicate stored | 0:0 → 137:0:0 |
| `sq032_07_finale.scene / n124 / 1` | Did you really want to take the meds from Misty? (`caught_you`) | No option-level predicate stored | 0:1 → 136:0:0 |
| `sq032_07_finale.scene / n124 / 2` | Thanks for helping. (`thanks`) | No option-level predicate stored | 0:2 → 126:0:0 |
| `sq032_07_finale.scene / n134 / 0` | Did you want to take the pill? (`want`) | No option-level predicate stored | 0:0 → 137:0:0 |
| `sq032_07_finale.scene / n134 / 1` | Caught you red-handed. (`caught_you`) | No option-level predicate stored | 0:1 → 136:0:0 |
| `sq032_07_finale.scene / n140 / 0` | Stopped you in the nick of time. (`stopped_you`) | No option-level predicate stored | 0:0 → 143:0:0 |
| `sq032_07_finale.scene / n140 / 1` | Think doubts crept in. (`doubt`) | No option-level predicate stored | 0:1 → 145:0:0 |
| `sq032_07_finale.scene / n140 / 2` | I believe you. (`believe`) | No option-level predicate stored | 0:2 → 147:0:0 |
| `sq032_07_finale.scene / n149 / 0` | Why you givin' them to me? (`why`) | No option-level predicate stored | 0:0 → 180:0:0 |
| `sq032_07_finale.scene / n149 / 1` | They from the Mexican conflict? (`mexican_conflict`) | No option-level predicate stored | 0:1 → 1084:0:1 |
| `sq032_07_finale.scene / n157 / 0` | Think I'm gonna die soon. (`die_soon`) | No option-level predicate stored | 0:0 → 38:0:0 |
| `sq032_07_finale.scene / n157 / 1` | I'll, uh, get you back someday. (`back`) | No option-level predicate stored | 0:1 → 129:0:0 |
| `sq032_07_finale.scene / n161 / 0` | Think I'm gonna die soon. (`die_soon`) | No option-level predicate stored | 0:0 → 38:0:0 |
| `sq032_07_finale.scene / n161 / 1` | Thinking of sex, aren't you? (`sex`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "censorship_homosexuality", "comparisonType": "Equal"}}} | 0:1 → 164:0:0 |
| `sq032_07_finale.scene / n171 / 0` | [Open compartment] (`open`) | No option-level predicate stored | 0:0 → 173:0:0; 0:0 → 470:0:3; 0:0 → 1028:0:1 |
| `sq032_07_finale.scene / n182 / 0` | Yes. (`yes`) | No option-level predicate stored | 0:0 → 184:0:0 |
| `sq032_07_finale.scene / n182 / 1` | No. (`no`) | No option-level predicate stored | 0:1 → 185:0:0 |
| `sq032_07_finale.scene / n182 / 2` | Dunno. (`dont_know`) | No option-level predicate stored | 0:2 → 186:0:0 |
| `sq032_07_finale.scene / n182 / 3` | Dumb question. (`dumb_question`) | No option-level predicate stored | 0:3 → 187:0:0 |
| `sq032_07_finale.scene / n197 / 0` | I'd do the same for you. (`yes`) | No option-level predicate stored | 0:0 → 200:0:0 |
| `sq032_07_finale.scene / n197 / 1` | Body's always been mine. (`no`) | No option-level predicate stored | 0:1 → 202:0:0 |
| `sq032_07_finale.scene / n385 / 0` | [Enter through window] (`crawl_thru_window`) | No option-level predicate stored | 0:0 → 168:0:0; 0:0 → 971:0:0 |
| `sq032_07_finale.scene / n640 / 0` | Musta been nice… to have control of your faculties again? (`how_was_it`) | No option-level predicate stored | 0:0 → 300:0:0 |
| `sq032_07_finale.scene / n659 / 0` | Ugh, stop fakin' it. (`fuck_off`) | No option-level predicate stored | 0:0 → 661:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-635910` | Producer outside selected context | sq032_05_fifth_episode.scene / scene / 1104 |
| `censorship_homosexuality` | Producer outside selected context | sq032_07_finale.scene / scene / 161 |
| `glossary_mikoshi` | sq032_03_third_episode.scene / scene / 607 | No reader in selected context |
| `johnny_default_on` | sq032_finale.questphase / h0 / 24 | No reader in selected context |
| `mq032_johnny_military_talk` | sq032_07_finale.scene / scene / 1102 | No reader in selected context |
| `player_killed_npc` | Producer outside selected context | sq032_05_fifth_episode.scene / scene / 166 |
| `q032_03_said_thanks` | sq032_03_third_episode.scene / scene / 252 | No reader in selected context |
| `q104_done` | Producer outside selected context | sq032_03_third_episode.scene / scene / 309 |
| `q105_done` | Producer outside selected context | sq032_03_third_episode.scene / scene / 307 |
| `q112_hanako_meeting_set_up` | Producer outside selected context | sq032.questphase / h0 / 105 |
| `q302_done` | Producer outside selected context | sq032_07_finale.scene / scene / 1084 |
| `sq032_03_mikoshi_known` | sq032_03_third_episode.scene / scene / 134 | No reader in selected context |
| `sq032_04_q104` | sq032_04_fourth_episode.scene / scene / 977 | sq032_04_fourth_episode.scene / scene / 1014; sq032_04_fourth_episode.scene / scene / 186; sq032_04_fourth_episode.scene / scene / 990 |
| `sq032_04_q105` | sq032_04_fourth_episode.scene / scene / 983 | sq032_04_fourth_episode.scene / scene / 1010; sq032_04_fourth_episode.scene / scene / 986 |
| `sq032_04_q110` | sq032_04_fourth_episode.scene / scene / 515 | sq032_04_fourth_episode.scene / scene / 1012; sq032_04_fourth_episode.scene / scene / 186; sq032_04_fourth_episode.scene / scene / 988 |
| `sq032_04_q112` | sq032_04_fourth_episode.scene / scene / 980 | sq032_04_fourth_episode.scene / scene / 1013; sq032_04_fourth_episode.scene / scene / 186; sq032_04_fourth_episode.scene / scene / 989 |
| `sq032_05_q104` | sq032_05_fifth_episode.scene / scene / 572 | sq032_05_fifth_episode.scene / scene / 513 |
| `sq032_05_q105` | sq032_05_fifth_episode.scene / scene / 575 | sq032_05_fifth_episode.scene / scene / 510 |
| `sq032_05_q110` | sq032_05_fifth_episode.scene / scene / 557 | sq032_05_fifth_episode.scene / scene / 512 |
| `sq032_05_q112` | sq032_05_fifth_episode.scene / scene / 540 | sq032_05_fifth_episode.scene / scene / 511 |
| `sq032_07_deserter` | sq032_07_finale.scene / scene / 1123 | No reader in selected context |
| `sq032_bystanders_active` | Producer outside selected context | sq032_03_third_episode.scene / scene / 356 |
| `sq032_dbg_mode` | Producer outside selected context | sq032.questphase / h0 / 83 |
| `sq032_dbg_start` | Producer outside selected context | sq032.questphase / h106 / 3 |
| `sq032_done` | sq032.questphase / h0 / 76 | No reader in selected context |
| `sq032_episode_3_done` | sq032_episode_3.questphase / h0 / 45 | No reader in selected context |
| `sq032_episode_3_failed` | sq032_episode_3.questphase / h0 / 91 | No reader in selected context |
| `sq032_episode_4_done` | sq032_episode_4.questphase / h0 / 20 | No reader in selected context |
| `sq032_episode_4_failed` | sq032_episode_4.questphase / h0 / 79 | No reader in selected context |
| `sq032_episode_5_done` | sq032_episode_5.questphase / h0 / 5 | No reader in selected context |
| `sq032_episode_5_failed` | sq032_episode_5.questphase / h0 / 61 | No reader in selected context |
| `sq032_episode_6_done` | sq032_episode_6.questphase / h0 / 5 | No reader in selected context |
| `sq032_finale_done` | sq032_finale.questphase / h0 / 23 | No reader in selected context |
| `sq032_johnnys_motivation` | sq032_04_fourth_episode.scene / scene / 550 | No reader in selected context |
| `sq032_q104_prefetch` | sq032_episode_3.questphase / h0 / 89; sq032_episode_4.questphase / h0 / 74; sq032_episode_5.questphase / h0 / 74 | sq032_episode_3.questphase / h0 / 79; sq032_episode_3.questphase / h0 / 88; sq032_episode_4.questphase / h0 / 66; sq032_episode_4.questphase / h0 / 78; sq032_episode_5.questphase / h0 / 57; sq032_episode_5.questphase / h0 / 58; sq032_episode_6.questphase / h0 / 89; sq032_episode_6.questphase / h0 / 90 |
| `sq032_q104_ready` | sq032.questphase / h145 / 6; sq032_episode_3.questphase / h0 / 48; sq032_episode_4.questphase / h0 / 24; sq032_episode_5.questphase / h0 / 24 | sq032_episode_3.questphase / h0 / 47; sq032_episode_4.questphase / h0 / 22; sq032_episode_5.questphase / h0 / 22; sq032_episode_6.questphase / h0 / 33 |
| `sq032_q104_used` | sq032_episode_3.questphase / h0 / 83; sq032_episode_4.questphase / h0 / 70; sq032_episode_5.questphase / h0 / 70 | No reader in selected context |
| `sq032_q105_prefetch` | sq032_episode_3.questphase / h0 / 90; sq032_episode_4.questphase / h0 / 72; sq032_episode_5.questphase / h0 / 72 | sq032_episode_3.questphase / h0 / 79; sq032_episode_3.questphase / h0 / 88; sq032_episode_4.questphase / h0 / 66; sq032_episode_4.questphase / h0 / 78; sq032_episode_5.questphase / h0 / 57; sq032_episode_5.questphase / h0 / 58 |
| `sq032_q105_ready` | sq032.questphase / h145 / 8; sq032_episode_3.questphase / h0 / 50; sq032_episode_4.questphase / h0 / 26; sq032_episode_5.questphase / h0 / 29 | sq032_episode_3.questphase / h0 / 47; sq032_episode_4.questphase / h0 / 22; sq032_episode_5.questphase / h0 / 22 |
| `sq032_q105_used` | sq032_episode_3.questphase / h0 / 82; sq032_episode_4.questphase / h0 / 68; sq032_episode_5.questphase / h0 / 68 | No reader in selected context |
| `sq032_q110_prefetch` | sq032_episode_4.questphase / h0 / 73; sq032_episode_5.questphase / h0 / 73 | sq032_episode_4.questphase / h0 / 66; sq032_episode_4.questphase / h0 / 78; sq032_episode_5.questphase / h0 / 57; sq032_episode_5.questphase / h0 / 58; sq032_episode_6.questphase / h0 / 89; sq032_episode_6.questphase / h0 / 90 |
| `sq032_q110_ready` | sq032.questphase / h145 / 5; sq032_episode_4.questphase / h0 / 23; sq032_episode_5.questphase / h0 / 23 | sq032_episode_4.questphase / h0 / 22; sq032_episode_5.questphase / h0 / 22; sq032_episode_6.questphase / h0 / 33 |
| `sq032_q110_used` | sq032_episode_4.questphase / h0 / 69; sq032_episode_5.questphase / h0 / 69 | No reader in selected context |
| `sq032_q112_prefetch` | sq032_episode_4.questphase / h0 / 75; sq032_episode_5.questphase / h0 / 75 | sq032_episode_4.questphase / h0 / 66; sq032_episode_4.questphase / h0 / 78; sq032_episode_5.questphase / h0 / 57; sq032_episode_5.questphase / h0 / 58; sq032_episode_6.questphase / h0 / 89; sq032_episode_6.questphase / h0 / 90 |
| `sq032_q112_ready` | sq032.questphase / h145 / 7; sq032_episode_4.questphase / h0 / 25; sq032_episode_5.questphase / h0 / 25 | sq032_03_third_episode.scene / scene / 129; sq032_episode_4.questphase / h0 / 22; sq032_episode_5.questphase / h0 / 22; sq032_episode_6.questphase / h0 / 33 |
| `sq032_q112_used` | sq032_episode_4.questphase / h0 / 71; sq032_episode_5.questphase / h0 / 71 | No reader in selected context |
| `sq032_tapeworm_stage` | sq032.questphase / h106 / 2 | sq032_episode_3.questphase / h0 / 77; sq032_episode_4.questphase / h0 / 60; sq032_episode_5.questphase / h0 / 62; sq032_episode_6.questphase / h0 / 92 |
| `sq032_v_wants_the_body` | sq032_07_finale.scene / scene / 228; sq032_07_finale.scene / scene / 229 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>118 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sq032_episode_3.questphase / h0 / 47` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q105_ready"}},"socketId":2173311359},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_ready"}},"socketId":2488326877}]}` | 64:Out → 47:In; 47:Case2173311359 → 81:In; 47:Case2488326877 → 74:In |
| `sq032_episode_3.questphase / h0 / 55` | `questLogicalXorNodeDefinition` `{}` | 55:Out1 → 45:In; 82:Out → 55:In1; 83:Out → 55:In2 |
| `sq032_episode_3.questphase / h0 / 69` | `questLogicalAndNodeDefinition` `{}` | 58:Out → 69:In1; 91:Out → 69:In2; 69:Out1 → 100:In |
| `sq032_episode_3.questphase / h0 / 74` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_roadhouse"}}` | 47:Case2488326877 → 74:In; 74:False → 48:In; 74:True → 66:in_q104; 74:False → 70:In1 |
| `sq032_episode_3.questphase / h0 / 75` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_dollhouse"}}` | 75:False → 50:In; 75:False → 70:In1; 81:Out → 75:In; 75:True → 80:in_q105 |
| `sq032_episode_3.questphase / h0 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_tapeworm_stage","value":3,"comparisonType":"GreaterOrEqual"}}}` | 77:Out → 64:In; 78:Out → 77:In |
| `sq032_episode_3.questphase / h0 / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q105_prefetch"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_prefetch"}}]}}` | 78:Out → 79:In; 79:Out → 88:In |
| `sq032_episode_3.questphase / h0 / 88` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q105_prefetch"}},"socketId":2173311359},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_prefetch"}},"socketId":2488326877}]}` | 88:Case2488326877 → 66:Prefetch; 79:Out → 88:In; 88:Case2173311359 → 80:Prefetch |
| `sq032_episode_3.questphase / h0 / 92` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 58:Out → 92:In; 92:Out → 62:In |
| `sq032_episode_3.questphase / h0 / 102` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8,"miliseconds":500}}}` | 102:Out → 97:In; 101:Out → 102:In |
| `sq032_episode_4.questphase / h0 / 22` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q105_ready"}},"socketId":2173311359},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q110_ready"}},"socketId":285067426},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_ready"}},"socketId":2488326877},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_ready"}},"socketId":1379322888}]}` | 39:Out → 22:In; 22:Case2173311359 → 49:In; 22:Case285067426 → 54:In; 22:Case2488326877 → 51:In; 22:Case1379322888 → 52:In |
| `sq032_episode_4.questphase / h0 / 31` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 31:Out1 → 20:In; 72:Out → 31:In1; 73:Out → 31:In2; 74:Out → 31:In3; 75:Out → 31:In4 |
| `sq032_episode_4.questphase / h0 / 44` | `questLogicalAndNodeDefinition` `{}` | 34:Out → 44:In1; 79:Out → 44:In2; 44:Out1 → 86:In |
| `sq032_episode_4.questphase / h0 / 51` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_roadhouse"}}` | 22:Case2488326877 → 51:In; 51:False → 24:In; 51:True → 42:in_q104; 51:False → 65:In1 |
| `sq032_episode_4.questphase / h0 / 52` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_motel"}}` | 22:Case1379322888 → 52:In; 52:False → 25:In; 52:True → 43:in_q112; 52:False → 65:In1 |
| `sq032_episode_4.questphase / h0 / 53` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_dollhouse"}}` | 53:False → 26:In; 53:True → 48:in_q105; 49:Out → 53:In; 53:False → 65:In1 |
| `sq032_episode_4.questphase / h0 / 54` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_chapel"}}` | 22:Case285067426 → 54:In; 54:False → 23:In; 54:True → 41:in_q110; 54:False → 65:In1 |
| `sq032_episode_4.questphase / h0 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_tapeworm_stage","value":4,"comparisonType":"GreaterOrEqual"}}}` | 60:Out → 39:In; 61:Out → 60:In |
| `sq032_episode_4.questphase / h0 / 66` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q105_prefetch"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q110_prefetch"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_prefetch"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_prefetch"}}]}}` | 61:Out → 66:In; 66:Out → 78:In |
| `sq032_episode_4.questphase / h0 / 78` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q105_prefetch"}},"socketId":2173311359},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q110_prefetch"}},"socketId":285067426},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_prefetch"}},"socketId":2488326877},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_prefetch"}},"socketId":1379322888}]}` | 78:Case285067426 → 41:Prefetch; 78:Case2488326877 → 42:Prefetch; 78:Case1379322888 → 43:Prefetch; 78:Case2173311359 → 48:Prefetch; 66:Out → 78:In |
| `sq032_episode_4.questphase / h0 / 82` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 34:Out → 82:In; 82:Out → 38:In |
| `sq032_episode_4.questphase / h0 / 88` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8,"miliseconds":500}}}` | 88:Out → 84:In; 87:Out → 88:In |
| `sq032_episode_5.questphase / h0 / 22` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q105_ready"}},"socketId":2173311359},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q110_ready"}},"socketId":285067426},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_ready"}},"socketId":2488326877},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_ready"}},"socketId":1379322888}]}` | 41:Out → 22:In; 22:Case2173311359 → 54:In; 22:Case285067426 → 55:In; 22:Case2488326877 → 52:In; 22:Case1379322888 → 53:In |
| `sq032_episode_5.questphase / h0 / 42` | `questLogicalXorNodeDefinition` `{"inputSocketCount":4}` | 42:Out1 → 5:In; 72:Out → 42:In1; 73:Out → 42:In2; 74:Out → 42:In3; 75:Out → 42:In4 |
| `sq032_episode_5.questphase / h0 / 47` | `questLogicalAndNodeDefinition` `{}` | 35:Out → 47:In1; 61:Out → 47:In2; 47:Out1 → 80:In |
| `sq032_episode_5.questphase / h0 / 52` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_roadhouse"}}` | 22:Case2488326877 → 52:In; 52:False → 24:In; 52:True → 45:in_q104; 52:False → 60:In1 |
| `sq032_episode_5.questphase / h0 / 53` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_motel"}}` | 22:Case1379322888 → 53:In; 53:False → 25:In; 53:True → 46:in_q112; 53:False → 60:In1 |
| `sq032_episode_5.questphase / h0 / 54` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_dollhouse"}}` | 22:Case2173311359 → 54:In; 54:False → 29:In; 54:True → 43:in_q105; 54:False → 60:In1 |
| `sq032_episode_5.questphase / h0 / 55` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_chapel"}}` | 22:Case285067426 → 55:In; 55:False → 23:In; 55:True → 44:in_q110; 55:False → 60:In1 |
| `sq032_episode_5.questphase / h0 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q105_prefetch"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q110_prefetch"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_prefetch"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_prefetch"}}]}}` | 63:Out → 57:In; 57:Out → 58:In |
| `sq032_episode_5.questphase / h0 / 58` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q105_prefetch"}},"socketId":2173311359},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q110_prefetch"}},"socketId":285067426},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_prefetch"}},"socketId":2488326877},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_prefetch"}},"socketId":1379322888}]}` | 58:Case2173311359 → 43:Prefetch; 58:Case285067426 → 44:Prefetch; 58:Case2488326877 → 45:Prefetch; 58:Case1379322888 → 46:Prefetch; 57:Out → 58:In |
| `sq032_episode_5.questphase / h0 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_tapeworm_stage","value":5,"comparisonType":"GreaterOrEqual"}}}` | 62:Out → 41:In; 63:Out → 62:In |
| `sq032_episode_5.questphase / h0 / 76` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8}}}` | 35:Out → 76:In; 76:Out → 40:In |
| `sq032_episode_5.questphase / h0 / 82` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":8,"miliseconds":500}}}` | 82:Out → 78:In; 81:Out → 82:In |
| `sq032_episode_6.questphase / h0 / 33` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q110_ready"}},"socketId":2173311359},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_ready"}},"socketId":285067426},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_ready"}},"socketId":2488326877}]}` | 65:Out → 33:In; 33:Case2173311359 → 69:In; 33:Case285067426 → 66:In; 33:Case2488326877 → 67:In |
| `sq032_episode_6.questphase / h0 / 66` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_roadhouse"}}` | 33:Case285067426 → 66:In; 66:True → 87:in_q104; 66:False → 75:In |
| `sq032_episode_6.questphase / h0 / 67` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_motel"}}` | 33:Case2488326877 → 67:In; 67:True → 88:in_q112; 67:False → 75:In |
| `sq032_episode_6.questphase / h0 / 69` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_chapel"}}` | 33:Case2173311359 → 69:In; 69:True → 84:in_q110; 69:False → 75:In |
| `sq032_episode_6.questphase / h0 / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","anyParent":true,"childIsPlayer":true,"condition":"OnUnmount"}},{"$type":"questSceneCondition","type":{"$type":"questSceneTier_ConditionType","tier":"Tier1_FullGameplay"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","inverted":true}}]}}` | 66:False → 75:In; 67:False → 75:In; 69:False → 75:In; 75:Out → 76:In |
| `sq032_episode_6.questphase / h0 / 82` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 82:Out → 73:In; 76:Out → 82:In |
| `sq032_episode_6.questphase / h0 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q110_prefetch"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_prefetch"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_prefetch"}}]}}` | 93:Out → 89:In; 89:Out → 90:In |
| `sq032_episode_6.questphase / h0 / 90` | `questSwitchNodeDefinition` `{"conditions":[{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q110_prefetch"}},"socketId":285067426},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q104_prefetch"}},"socketId":2488326877},{"$type":"questConditionItem","condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_prefetch"}},"socketId":1379322888}]}` | 90:Case285067426 → 84:Prefetch; 90:Case2488326877 → 87:Prefetch; 90:Case1379322888 → 88:Prefetch; 89:Out → 90:In |
| `sq032_episode_6.questphase / h0 / 92` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_tapeworm_stage","value":6,"comparisonType":"GreaterOrEqual"}}}` | 92:Out → 65:In; 93:Out → 92:In |
| `sq032_03_third_episode.scene / scene / 129` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_q112_ready"}}}` | 129:0:0 → 116:0:0; 129:0:1 → 134:0:1; 143:2:0 → 129:0:1 |
| `sq032_03_third_episode.scene / scene / 307` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 170:0:0 → 307:0:1; 307:0:0 → 311:0:0; 307:0:1 → 309:0:1 |
| `sq032_03_third_episode.scene / scene / 309` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q104_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 307:0:1 → 309:0:1; 309:0:0 → 314:0:0; 309:0:1 → 313:0:0 |
| `sq032_03_third_episode.scene / scene / 356` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_bystanders_active","value":1,"comparisonType":"Equal"}}}` | 188:0:0 → 356:0:1; 356:0:0 → 331:0:0; 356:0:0 → 332:0:0; 356:0:0 → 333:0:0; 356:0:0 → 334:0:0; 356:0:0 → 335:0:0 |
| `sq032_03_third_episode.scene / scene / 399` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq032_03_third_episode_Johnny"},"timeInterval":0.10000000149011612,"angleTolerance":60.0,"inverted":true}}}` | 327:3:0 → 399:0:1; 395:3:0 → 399:0:1; 399:0:0 → 973:0:1; 3800:0:0 → 399:0:1 |
| `sq032_03_third_episode.scene / scene / 649` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_06_tr_sixth_episode"}}` | 649:0:0 → 82:0:0; 649:0:0 → 629:1:0; 649:0:0 → 631:1:0; 773:0:0 → 649:0:1 |
| `sq032_03_third_episode.scene / scene / 664` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_03_third_roadhouse"}}` | 76:0:0 → 664:0:1; 664:0:0 → 662:1:0; 664:0:0 → 980:0:1; 664:0:0 → 3819:0:1 |
| `sq032_03_third_episode.scene / scene / 863` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 856:0:0 → 863:0:1; 863:0:0 → 3811:0:1 |
| `sq032_03_third_episode.scene / scene / 896` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq032\\scenes\\sq032_03_third_episode.scene","Flags":"Soft"},"sectionName":"sq032_03_only_a_ghost","type":"IsOutside"}}}` | 145:0:2 → 896:0:1; 896:0:0 → 147:0:0 |
| `sq032_03_third_episode.scene / scene / 3733` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 107:1:0 → 3733:0:1; 3733:0:0 → 990:0:1 |
| `sq032_03_third_episode.scene / scene / 3772` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":20}}}` | 990:0:0 → 3772:0:1; 3772:0:0 → 3770:0:1 |
| `sq032_03_third_episode.scene / scene / 3778` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 3770:0:0 → 3778:0:1; 3778:0:0 → 831:0:1 |
| `sq032_03_third_episode.scene / scene / 3790` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_dollhouse"}}` | 679:666:0 → 3790:0:1; 3790:0:0 → 3791:0:1; 3790:0:1 → 3798:0:0 |
| `sq032_03_third_episode.scene / scene / 3791` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_03_dollhouse"}}` | 3790:0:0 → 3791:0:1; 3791:0:0 → 3822:0:1 |
| `sq032_04_fourth_episode.scene / scene / 113` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"83635443133"}}}}` | 36:0:0 → 113:0:1; 113:0:0 → 41:0:0; 113:0:1 → 115:0:1 |
| `sq032_04_fourth_episode.scene / scene / 115` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"67091901544"}}}}` | 113:0:1 → 115:0:1; 115:0:0 → 112:0:0; 115:0:1 → 118:0:0 |
| `sq032_04_fourth_episode.scene / scene / 123` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"83635443133"}}}}` | 43:0:0 → 123:0:1; 123:0:0 → 128:0:0; 123:0:1 → 124:0:1 |
| `sq032_04_fourth_episode.scene / scene / 124` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questLifePath_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"LifePath_ScriptConditionType","lifePathId":"67091901544"}}}}` | 123:0:1 → 124:0:1; 124:0:0 → 130:0:0; 124:0:1 → 131:0:0 |
| `sq032_04_fourth_episode.scene / scene / 970` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_04_dollhouse"}}` | 1:0:0 → 970:0:1; 970:0:0 → 983:0:1; 970:0:0 → 1196:0:0 |
| `sq032_04_fourth_episode.scene / scene / 986` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_04_q105","value":1,"comparisonType":"Equal"}}}` | 44:0:0 → 986:0:1; 986:0:0 → 997:0:0; 986:0:1 → 988:0:1 |
| `sq032_04_fourth_episode.scene / scene / 988` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_04_q110","value":1,"comparisonType":"Equal"}}}` | 986:0:1 → 988:0:1; 988:0:0 → 975:0:0; 988:0:1 → 989:0:1 |
| `sq032_04_fourth_episode.scene / scene / 989` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_04_q112","value":1,"comparisonType":"Equal"}}}` | 988:0:1 → 989:0:1; 989:0:0 → 1001:0:0; 989:0:1 → 990:0:1 |
| `sq032_04_fourth_episode.scene / scene / 990` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_04_q104","value":1,"comparisonType":"Equal"}}}` | 989:0:1 → 990:0:1; 990:0:0 → 1005:0:0 |
| `sq032_04_fourth_episode.scene / scene / 1010` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_04_q105","value":1,"comparisonType":"Equal"}}}` | 461:2:0 → 1010:0:1; 1010:0:0 → 1272:0:0; 1010:0:1 → 1012:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1012` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_04_q110","value":1,"comparisonType":"Equal"}}}` | 1010:0:1 → 1012:0:1; 1012:0:0 → 1252:0:0; 1012:0:1 → 1013:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1013` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_04_q112","value":1,"comparisonType":"Equal"}}}` | 1012:0:1 → 1013:0:1; 1013:0:0 → 1038:0:0; 1013:0:1 → 1014:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1014` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_04_q104","value":1,"comparisonType":"Equal"}}}` | 1013:0:1 → 1014:0:1; 1014:0:0 → 1263:0:0; 1076:0:0 → 1014:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1088` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_04_tr_motel"}}` | 13:0:0 → 1088:0:1; 1088:0:0 → 980:0:1; 1088:0:0 → 1196:0:0 |
| `sq032_04_fourth_episode.scene / scene / 1337` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq032_04_fourth_episode_Johnny"},"timeInterval":0.4000000059604645,"onScreenTest":true,"angleTolerance":90.0,"inverted":true}}}` | 1337:0:0 → 1628:0:1; 1710:0:0 → 1337:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1445` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 1445:0:0 → 1437:0:0; 1951:0:0 → 1445:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1703` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq032_04_fourth_episode_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":90.0,"inverted":true}}}` | 1703:0:0 → 1704:0:1; 1761:0:0 → 1703:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1725` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 1639:0:0 → 1725:0:1; 1725:0:0 → 1882:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1737` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq032_04_fourth_episode_Johnny"},"angleTolerance":40.0,"inverted":true}}}` | 1737:0:0 → 1739:0:0; 1743:0:0 → 1737:0:1; 1745:1:0 → 1737:0:0; 1745:1:0 → 1737:1026:0; 1753:0:0 → 1737:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1741` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq032_04_fourth_episode_Johnny"},"angleTolerance":40.0}}}` | 1739:0:0 → 1741:0:1; 1741:0:0 → 1743:0:0; 1745:1:0 → 1741:0:0; 1745:1:0 → 1741:1026:0 |
| `sq032_04_fourth_episode.scene / scene / 1916` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 1882:0:0 → 1916:0:1; 1916:0:0 → 1913:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1926` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":50}}}` | 1839:0:0 → 1926:0:1; 1926:0:0 → 1924:0:1 |
| `sq032_04_fourth_episode.scene / scene / 1946` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q104_tr_squad_arrival"}}` | 10:0:0 → 1946:0:1; 1946:0:0 → 977:0:1; 1946:0:0 → 1196:0:0 |
| `sq032_05_fifth_episode.scene / scene / 166` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"player_killed_npc"}}}` | 89:0:0 → 166:0:1; 166:0:0 → 168:0:0; 166:0:1 → 169:0:0 |
| `sq032_05_fifth_episode.scene / scene / 384` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq032_05_fifth_episode_Johnny"},"onScreenTest":true,"angleTolerance":90.0,"inverted":true}}}` | 44:0:0 → 384:0:1; 384:0:0 → 885:0:1 |
| `sq032_05_fifth_episode.scene / scene / 510` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_05_q105","value":1,"comparisonType":"Equal"}}}` | 510:0:0 → 986:0:0; 510:0:1 → 512:0:1; 698:2:0 → 510:0:1 |
| `sq032_05_fifth_episode.scene / scene / 511` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_05_q112","value":1,"comparisonType":"Equal"}}}` | 511:0:0 → 991:0:0; 513:0:1 → 511:0:1 |
| `sq032_05_fifth_episode.scene / scene / 512` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_05_q110","value":1,"comparisonType":"Equal"}}}` | 510:0:1 → 512:0:1; 512:0:0 → 981:0:0; 512:0:1 → 513:0:1 |
| `sq032_05_fifth_episode.scene / scene / 513` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_05_q104","value":1,"comparisonType":"Equal"}}}` | 512:0:1 → 513:0:1; 513:0:0 → 991:0:0; 513:0:1 → 511:0:1 |
| `sq032_05_fifth_episode.scene / scene / 606` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_05_tr_fifth_episode_motel"}}` | 540:0:0 → 606:0:1; 606:0:0 → 1185:0:1 |
| `sq032_05_fifth_episode.scene / scene / 610` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_05_tr_fifth_episode_dollhouse"}}` | 575:0:0 → 610:0:1; 610:0:0 → 1162:0:1 |
| `sq032_05_fifth_episode.scene / scene / 738` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 730:0:0 → 738:0:1; 738:0:0 → 734:0:0 |
| `sq032_05_fifth_episode.scene / scene / 803` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq032\\scenes\\sq032_05_fifth_episode.scene","Flags":"Soft"},"sectionName":"sq032_05_mikoshi_why","type":"IsOutside"}}}` | 120:0:2 → 803:0:1; 803:0:0 → 203:0:0 |
| `sq032_05_fifth_episode.scene / scene / 822` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq032\\scenes\\sq032_05_fifth_episode.scene","Flags":"Soft"},"sectionName":"sq032_05_whats_the_charm","type":"IsOutside"}}}` | 177:0:2 → 822:0:1; 822:0:0 → 304:0:0 |
| `sq032_05_fifth_episode.scene / scene / 1020` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 1020:0:0 → 1074:0:1; 1023:0:0 → 1020:0:1 |
| `sq032_05_fifth_episode.scene / scene / 1077` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":10}}}` | 1074:0:0 → 1077:0:1; 1077:0:0 → 1079:0:1 |
| `sq032_05_fifth_episode.scene / scene / 1085` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":20}}}` | 1079:0:0 → 1085:0:1; 1085:0:0 → 1081:0:1 |
| `sq032_05_fifth_episode.scene / scene / 1096` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_05_tr_fifth_episode"}}` | 1096:0:0 → 1178:0:1; 1104:0:0 → 1096:0:1 |
| `sq032_05_fifth_episode.scene / scene / 1104` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-635910","comparisonType":"Equal"}}}` | 225:666:0 → 1104:0:1; 1104:0:0 → 1096:0:1; 1104:0:1 → 1108:0:0 |
| `sq032_06_sixth_episode.scene / scene / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Exited","triggerAreaRef":"#sq032_06_tr_sixth_episode"}}` | 5:0:0 → 96:0:1; 80:0:0 → 96:0:0; 96:0:0 → 80:1:0; 96:0:0 → 315:0:1; 96:0:0 → 457:0:0 |
| `sq032_06_sixth_episode.scene / scene / 209` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Exited","triggerAreaRef":"#sq032_06_tr_sixth_episode_roadhouse"}}` | 4:0:0 → 209:0:1; 207:0:0 → 209:0:0; 209:0:0 → 207:1:0; 209:0:0 → 313:0:1; 209:0:0 → 446:0:1 |
| `sq032_06_sixth_episode.scene / scene / 225` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 135:0:0 → 225:0:1; 225:0:0 → 6:0:0; 225:0:0 → 228:1:0; 225:0:0 → 311:0:1; 228:0:0 → 225:0:0 |
| `sq032_06_sixth_episode.scene / scene / 380` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 1:0:0 → 380:0:1; 4:0:0 → 380:0:1; 5:0:0 → 380:0:1; 380:0:0 → 403:0:1; 380:0:0 → 467:0:1 |
| `sq032_06_sixth_episode.scene / scene / 386` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 386:0:0 → 413:0:1; 386:0:0 → 484:0:1; 409:0:0 → 386:0:1 |
| `sq032_07_finale.scene / scene / 257` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterGender_CondtionType","isPlayer":true}}}` | 60:0:0 → 257:0:1; 257:0:0 → 264:0:0; 257:0:1 → 263:0:0 |
| `sq032_07_finale.scene / scene / 318` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_07_second_fall"}}` | 318:0:0 → 323:0:0; 318:0:0 → 665:0:0; 353:0:0 → 318:0:1 |
| `sq032_07_finale.scene / scene / 336` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_07_first_fall"}}` | 34:3:0 → 336:0:1; 336:0:0 → 300:1:0; 336:0:0 → 315:0:0; 336:0:0 → 640:1:0 |
| `sq032_07_finale.scene / scene / 340` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_07_first_fall"}}` | 36:3:0 → 340:0:1; 340:0:0 → 312:0:0 |
| `sq032_07_finale.scene / scene / 700` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq032_07_finale_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}}}` | 445:0:0 → 700:0:1; 700:0:0 → 952:0:1 |
| `sq032_07_finale.scene / scene / 746` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 1:0:0 → 746:0:1; 746:0:0 → 4:0:1 |
| `sq032_07_finale.scene / scene / 770` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq032_tr_07_exit"}}` | 244:0:0 → 770:0:1; 770:0:0 → 435:0:0 |
| `sq032_07_finale.scene / scene / 788` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 788:0:0 → 795:0:0; 791:0:0 → 788:0:1 |
| `sq032_07_finale.scene / scene / 1000` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 1000:0:0 → 1047:0:1; 1045:0:0 → 1000:0:1 |
| `sq032_07_finale.scene / scene / 1028` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 171:0:0 → 1028:0:1; 1028:0:0 → 1030:0:1 |
| `sq032_07_finale.scene / scene / 1038` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 23:0:0 → 1038:0:1; 1038:0:0 → 1045:0:1 |
| `sq032_07_finale.scene / scene / 1084` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q302_done"}}}` | 149:0:1 → 1084:0:1; 1084:0:0 → 1119:0:0; 1084:0:1 → 177:0:0 |
| `sq032.questphase / h0 / 83` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_dbg_mode"}}}` | 50:Out1 → 83:In; 51:Out1 → 83:In; 52:Out1 → 83:In; 83:True → 82:In |
| `sq032.questphase / h0 / 105` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q112_hanako_meeting_set_up"}}}` | 105:False → 90:Active; 92:Out → 105:In; 105:True → 106:Active |
| `sq032.questphase / h0 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 96:Out1 → 107:In; 107:Out → 104:In |
| `sq032.questphase / h0 / 108` | `questLogicalAndNodeDefinition` `{}` | 108:Out1 → 81:In; 89:Out → 108:In1; 109:Out1 → 108:In2 |
| `sq032.questphase / h106 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_dbg_start"}}}` | 0:Out → 3:In; 3:True → 1:In; 3:False → 2:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `checkpoint` | sq032.questphase / h0 / 92; sq032_episode_3.questphase / h0 / 58; sq032_episode_4.questphase / h0 / 34; sq032_episode_5.questphase / h0 / 35 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sq032_03_third_episode.scene / scene / 107; sq032_03_third_episode.scene / scene / 116; sq032_03_third_episode.scene / scene / 139; sq032_03_third_episode.scene / scene / 145; +68 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | sq032.questphase / h0 / 105; sq032.questphase / h0 / 83; sq032.questphase / h106 / 3; sq032_03_third_episode.scene / scene / 129; +36 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sq032.questphase / h145 / 9; sq032_episode_3.questphase / h0 / 63; sq032_episode_3.questphase / h0 / 64; sq032_episode_3.questphase / h0 / 98; +8 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sq032.questphase / h145 / 10; sq032_03_third_episode.scene / scene / 3819; sq032_03_third_episode.scene / scene / 3822; sq032_03_third_episode.scene / scene / 3828; +10 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `journal_transition` | sq032.questphase / h0 / 106; sq032.questphase / h0 / 89; sq032.questphase / h0 / 90; sq032.questphase / h0 / 99; +32 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | sq032_episode_6.questphase / h0 / 75 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | sq032.questphase / h0 / 108; sq032_episode_3.questphase / h0 / 69; sq032_episode_4.questphase / h0 / 44; sq032_episode_5.questphase / h0 / 47 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sq032.questphase / h0 / 76; sq032.questphase / h106 / 2; sq032.questphase / h145 / 5; sq032.questphase / h145 / 6; +57 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sq032_episode_3.questphase / h0 / 55; sq032_episode_4.questphase / h0 / 31; sq032_episode_5.questphase / h0 / 42 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sq032.questphase / h0 / 107; sq032_03_third_episode.scene / scene / 3733; sq032_03_third_episode.scene / scene / 3772; sq032_03_third_episode.scene / scene / 3778; +24 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `scene_interface` | sq032_episode_3.questphase / h0 / 66; sq032_episode_3.questphase / h0 / 80; sq032_episode_4.questphase / h0 / 41; sq032_episode_4.questphase / h0 / 42; +13 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sq032_03_third_episode.scene / scene / 3790; sq032_03_third_episode.scene / scene / 3791; sq032_03_third_episode.scene / scene / 649; sq032_03_third_episode.scene / scene / 664; +25 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `weather_scope` | sq032_07_finale.scene / scene / 783; sq032_07_finale.scene / scene / 785 | weather operation + named source + reset policy → weather request/reset dispatched. Completion follows the caller's full restoration sequence, not an early cleanup fact. |
| `workspot_performance` | sq032_03_third_episode.scene / scene / 420; sq032_03_third_episode.scene / scene / 422; sq032_03_third_episode.scene / scene / 424; sq032_03_third_episode.scene / scene / 425; +216 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sq032_03_third_episode.scene / scene / 1055; sq032_03_third_episode.scene / scene / 1057; sq032_07_finale.scene / scene / 1069; sq032_07_finale.scene / scene / 1071; +1 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` | content candidate; journal anchor | `base-sq032` |
| `base\quest\side_quests\sq032\phases\sq032_episode_4.questphase` | content candidate; journal anchor | `base-sq032` |
| `base\quest\side_quests\sq032\phases\sq032_episode_5.questphase` | content candidate; journal anchor | `base-sq032` |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` | content candidate; forward dependency | `base-sq032` |
| `base\quest\side_quests\sq032\phases\sq032_finale.questphase` | content candidate; forward dependency | `base-sq032` |
| `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` | content candidate; journal anchor | `base-sq032` |
| `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene` | content candidate; journal anchor | `base-sq032` |
| `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene` | content candidate; journal anchor | `base-sq032` |
| `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene` | content candidate; journal anchor | `base-sq032` |
| `base\quest\side_quests\sq032\scenes\sq032_07_finale.scene` | content candidate; journal anchor | `base-sq032` |
| `base\quest\side_quests\sq032\sq032.questphase` | content candidate; journal anchor | `base-sq032` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q108](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q108.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

647 repeated typed/socket path signatures in this selected graph context; 151 distinct direct resource identities; 5 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` / h0 / 48 -> 89 -> 83 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `215ca95d939006973a7d` | `base\quest\side_quests\sq032\phases\sq032_finale.questphase` / h0 / 23 -> 24 -> 1 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `8cd3b647ae3f592ad947` | `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene` / scene / 1197 -> 1199 -> 1201 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `eaf5aab427d50e5598b6` | `base\quest\side_quests\sq032\sq032.questphase` / h106 / 0 -> 3 -> 2 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `9c634ff27b9a7aa77918` | `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` / h0 / 0 -> 78 -> 77 | questInputNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `19665e3783f6f51a7337` | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 76 -> 662 -> 784 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `d1586abf7da1797dd601` | `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` / h0 / 89 -> 83 -> 55 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questLogicalXorNodeDefinition; Out -> In; Out -> In2 |
| `b8e20c88e3e3780549b4` | `base\quest\side_quests\sq032\sq032.questphase` / h106 / 3 -> 2 -> 1 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questOutputNodeDefinition; False -> In; Out -> In |
| `95d4997362b664c5c23b` | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 198 -> 139 -> 141 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |
| `276aca4a2dc348a877d5` | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 113 -> 193 -> 428 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 3:0 -> 0:1 |
| `e70b0765e99ad324f9b7` | `base\quest\side_quests\sq032\sq032.questphase` / h145 / 0 -> 8 -> 5 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `016828d499c85128303c` | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 170 -> 307 -> 311 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` / h0 / 48 | `h47` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` / h0 / 49 | `h75` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` / h0 / 50 | `h96` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\side_quests\sq032\sq032.questphase` / h0 / 95 | `h106` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\side_quests\sq032\sq032.questphase` / h0 / 103 | `h145` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_def.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.gamedef` | content candidate | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest |
| `base\quest\minor_quests\mq000\mq000.gamedef` | content candidate | base\quest\minor_quests\mq000\mq000.quest |
| `base\quest\minor_quests\mq000\mq000_thank_you.gamedef` | content candidate | base\quest\minor_quests\mq000\mq000.quest |
| `base\quest\minor_quests\mq001\mq001.gamedef` | content candidate | base\quest\minor_quests\mq001\mq001.quest |
| `base\quest\minor_quests\mq003\mq003_orbitals.gamedef` | content candidate | base\quest\minor_quests\mq003\mq003_orbitals.quest |
| `base\quest\minor_quests\mq006\mq006.gamedef` | content candidate | base\quest\minor_quests\mq006\mq006.quest |
| `base\quest\minor_quests\mq007\mq007.gamedef` | content candidate | base\quest\minor_quests\mq007\mq007.quest |
| `base\quest\minor_quests\mq008\mq008.gamedef` | content candidate | base\quest\minor_quests\mq008\mq008.quest |
| `base\quest\minor_quests\mq011\mq011.gamedef` | content candidate | base\quest\minor_quests\mq011\mq011.quest |
| `base\quest\minor_quests\mq012\mq012.gamedef` | content candidate | base\quest\minor_quests\mq012\mq012.quest |
| `base\quest\minor_quests\mq013\mq013.gamedef` | content candidate | base\quest\minor_quests\mq013\mq013.quest |
| `base\quest\minor_quests\mq014\mq014.gamedef` | content candidate | base\quest\minor_quests\mq014\mq014.quest |
| `base\quest\minor_quests\mq015\mq015_wizardbook.gamedef` | content candidate | base\quest\minor_quests\mq015\mq015_wizardbook.quest |
| `base\quest\minor_quests\mq016\mq016_bartmoss.gamedef` | content candidate | base\quest\minor_quests\mq016\mq016_bartmoss.quest |
| `base\quest\minor_quests\mq017\mq017_streetkid.gamedef` | content candidate | base\quest\minor_quests\mq017\mq017_streetkid.quest |
| `base\quest\minor_quests\mq018\mq018.gamedef` | content candidate | base\quest\minor_quests\mq018\mq018.quest |
| `base\quest\minor_quests\mq019\mq019_paparazzi.gamedef` | content candidate | base\quest\minor_quests\mq019\mq019_paparazzi.quest |
| `base\quest\minor_quests\mq021\mq021.gamedef` | content candidate | base\quest\minor_quests\mq021\mq021.quest |
| `base\quest\minor_quests\mq022\mq022.gamedef` | content candidate | base\quest\minor_quests\mq022\mq022.quest |
| `base\quest\minor_quests\mq023\mq023_bootleg.gamedef` | content candidate | base\quest\minor_quests\mq023\mq023_bootleg.quest |
| `base\quest\minor_quests\mq024\mq024.gamedef` | content candidate | base\quest\minor_quests\mq024\mq024.quest |
| `base\quest\minor_quests\mq025\batty\batty_definition.gamedef` | content candidate | base\quest\minor_quests\mq025\batty\batty_quest.quest |
| `base\quest\minor_quests\mq025\mq025_psycho_brawl.gamedef` | content candidate | base\quest\minor_quests\mq025\mq025_psycho_brawl.quest |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | base\quest\minor_quests\mq026\mq026.quest |
| `base\quest\minor_quests\mq028\mq028.gamedef` | content candidate | base\quest\minor_quests\mq028\mq028.quest |
| `base\quest\minor_quests\mq030\mq030.gamedef` | content candidate | base\quest\minor_quests\mq030\mq030.quest |
| `base\quest\minor_quests\mq032\mq032_sacrum.gamedef` | content candidate | base\quest\minor_quests\mq032\mq032_sacrum.quest |
| `base\quest\minor_quests\mq033\mq033_tarot.gamedef` | content candidate | base\quest\minor_quests\mq033\mq033_tarot.quest |
| `base\quest\minor_quests\mq035\mq035_ozob.gamedef` | content candidate | base\quest\minor_quests\mq035\mq035_ozob.quest |
| `base\quest\minor_quests\mq037\mq037_brendan.gamedef` | content candidate | base\quest\minor_quests\mq037\mq037_brendan.quest |
| `base\quest\minor_quests\mq038\mq038.gamedef` | content candidate | base\quest\minor_quests\mq038\mq038.quest |
| `base\quest\minor_quests\mq040\mq040_biosculpt.gamedef` | content candidate | base\quest\minor_quests\mq040\mq040_biosculpt.quest |
| `base\quest\minor_quests\mq041\mq041_corpo.gamedef` | content candidate | base\quest\minor_quests\mq041\mq041_corpo.quest |
| `base\quest\minor_quests\mq048\mq048.gamedef` | content candidate | base\quest\minor_quests\mq048\mq048.quest |
| `base\quest\minor_quests\mq055\mq055.gamedef` | content candidate | base\quest\minor_quests\mq055\mq055.quest |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.gamedef` | content candidate | base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest |
| `base\quest\main_quests\prologue\q000\q000.gamedef` | content candidate | base\quest\main_quests\prologue\q000\q000.quest |
| `base\quest\main_quests\prologue\q001\q001.gamedef` | content candidate | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q001\test\q001_miss0_mark_world.gamedef` | test/debug | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q003\q003.gamedef` | content candidate | base\quest\main_quests\prologue\q003\q003.quest |
| `base\quest\main_quests\prologue\q005\q005_heist.gamedef` | content candidate | base\quest\main_quests\prologue\q005\q005_heist.quest |
| `base\quest\main_quests\part1\q101\q101.gamedef` | content candidate | base\quest\main_quests\part1\q101\q101.quest |
| `base\quest\main_quests\part1\q103\q103.gamedef` | content candidate | base\quest\main_quests\part1\q103\q103.quest |
| `base\quest\main_quests\part1\q105\q105_main.gamedef` | content candidate | base\quest\main_quests\part1\q105\q105_main.quest |
| `base\quest\main_quests\part1\q108\q108_johnny.gamedef` | content candidate | base\quest\main_quests\part1\q108\q108_johnny.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q113\q113.gamedef` | content candidate | base\quest\main_quests\part1\q113\q113.quest |
| `base\quest\main_quests\part1\q114\q114_nomads.gamedef` | content candidate | base\quest\main_quests\part1\q114\q114_nomads.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\main_quests\epilogue\q202\q202.gamedef` | content candidate | base\quest\main_quests\epilogue\q202\q202.quest |
| `base\quest\main_quests\epilogue\q203\q203_legend.gamedef` | content candidate | base\quest\main_quests\epilogue\q203\q203_legend.quest |
| `base\quest\main_quests\epilogue\q204\q204_reborn.gamedef` | content candidate | base\quest\main_quests\epilogue\q204\q204_reborn.quest |
| `base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.gamedef` | content candidate | base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `base\quest\side_quests\sq004\sq004_riders_on_the_storm.gamedef` | content candidate | base\quest\side_quests\sq004\sq004_riders_quest.quest |
| `base\quest\side_quests\sq006\sq006.gamedef` | content candidate | base\quest\side_quests\sq006\sq006.quest |
| `base\quest\side_quests\sq011\sq011.gamedef` | content candidate | base\quest\side_quests\sq011\sq011.quest |
| `base\quest\side_quests\sq012\sq012_the_law.gamedef` | content candidate | base\quest\side_quests\sq012\sq012_the_law.quest |
| `base\quest\side_quests\sq017\sq017.gamedef` | content candidate | base\quest\side_quests\sq017\sq017.quest |
| `base\quest\side_quests\sq018\sq018.gamedef` | content candidate | base\quest\side_quests\sq018\sq018.quest |
| `base\quest\side_quests\sq021\sq021.gamedef` | content candidate | base\quest\side_quests\sq021\sq021.quest |
| `base\quest\side_quests\sq023\sq023.gamedef` | content candidate | base\quest\side_quests\sq023\sq023.quest |
| `base\quest\side_quests\sq024\sq024.gamedef` | content candidate | base\quest\side_quests\sq024\sq024.quest |
| `base\quest\side_quests\sq025\sq025.gamedef` | content candidate | base\quest\side_quests\sq025\sq025.quest |
| `base\quest\side_quests\sq026\sq026.gamedef` | content candidate | base\quest\side_quests\sq026\sq026.quest |
| `base\quest\side_quests\sq027\sq027_queen_of_the_highway.gamedef` | content candidate | base\quest\side_quests\sq027\sq0027_queen_of_the_highway.quest |
| `base\quest\side_quests\sq028\sq028.gamedef` | content candidate | base\quest\side_quests\sq028\sq028.quest |
| `base\quest\side_quests\sq029\sq029.gamedef` | content candidate | base\quest\side_quests\sq029\sq029.quest |
| `base\quest\side_quests\sq030\sq030.gamedef` | content candidate | base\quest\side_quests\sq030\sq030.quest |
| `base\quest\side_quests\sq031\sq031.gamedef` | content candidate | base\quest\side_quests\sq031\sq031.quest |
| `base\quest\side_quests\sq032\sq032.gamedef` | content candidate | base\quest\side_quests\sq032\sq032.quest |
| `ep1\quest\minor_quests\mq301\mq301.gamedef` | content candidate | ep1\quest\minor_quests\mq301\mq301.quest |
| `ep1\quest\minor_quests\mq303\mq303.gamedef` | content candidate | ep1\quest\minor_quests\mq303\mq303.quest |
| `ep1\quest\minor_quests\mq304\mq304.gamedef` | content candidate | ep1\quest\minor_quests\mq304\mq304.quest |
| `ep1\quest\minor_quests\mq305\mq305.gamedef` | content candidate | ep1\quest\minor_quests\mq305\mq305.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.gamedef` | content candidate | ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest |
| `ep1\quest\main_quests\q304\q304.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\q304_car_retrieval_test.gamedef` | content candidate | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_escape.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_lab.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_songbird_finale.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q304\test\q304_from_stadium.gamedef` | test/debug | ep1\quest\main_quests\q304\q304.quest |
| `ep1\quest\main_quests\q305\q305.gamedef` | content candidate | ep1\quest\main_quests\q305\q305.quest |
| `ep1\quest\main_quests\q306\q306.gamedef` | content candidate | ep1\quest\main_quests\q306\q306.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| `base\animations\facial\female_average\interactive_scene\generic_average_female_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtgirl\interactive_scene\dirtgirl__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean0__2h_elbow_on_knees__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean180__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean180__2h_on_lap__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean180__2h_on_lap__03.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_couch_lean180__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_bar_lean180__2h_elbow_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_bar_lean90__rh_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world_master\generic_male_average__stand_wall_lean180__2h_on_sides__ow__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair__2h_on_lap_lh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair__2h_up_lh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__2h_elbow_on_knees__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__2h_elbow_on_knees__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__2h_on_backrest__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__lh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__lh_cigarette__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__rh_glasses__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__rh_on_backrest__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__rh_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean180__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean180__arms_legs_crossed__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__2h_glasses__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__2h_on_sides__aggressive__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__2h_on_sides__aggressive__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__lh_pocket__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_bar_lean0__2h_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_rail_lean180__2h_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_rail_lean180__lh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_wall_lean180__lh_pocket__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_wall_lean180__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_wall_lean180__rh_glasses_lh_pocket__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_wall_lean90__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_wall_lean90__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\female\body\player_locomotion_johnny_guitar.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__fpp_contextual_sickness__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__fpp_contextual_sickness__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\male\body\player_locomotion_sick.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q101\07c_johnny_triggers\q101_07c_johnny_triggers__player_ma_animset.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q101\07c_johnny_triggers\q101_07c_johnny_triggers__player_wa_animset.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q105\q105_05_fingers_enter\q105_05_fingers_enter__player.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q105\q105_08a_braindance_investigation\q105_08a_braindance_investigation__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q110\q110_04_netrunners_den\q110_04_netrunners_den__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq031\sq031_01a_smack_afterlife\sq031_01a_smack_afterlife__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq031\sq031_01c_smack_striptease\synced\synced__sq031_01c_smack_striptease__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq031\sq031_01c_smack_striptease\synced\synced__sq031_01c_smack_striptease__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq031\sq031_01c_smack_striptease\synced\synced__sq031_01c_smack_striptease__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq031\sq031_05_grave\sq031_05_grave__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_03_third_episode\sq032_03_third_episode__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_03_third_episode\sq032_03_third_episode__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_03_third_episode\sq032_03_third_episode__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_03_third_episode\synced\synced__sq032_03_third_episode__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_03_third_episode\synced\synced__sq032_03_third_episode__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_04_fourth_episode\sq032_04_fourth_episode__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_04_fourth_episode\sq032_04_fourth_episode__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_04_fourth_episode\sq032_04_fourth_episode__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_05_fifth_episode\sq032_05_fifth_episode__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_05_fifth_episode\sq032_05_fifth_episode__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_05_fifth_episode\synced\synced__sq032_05_fifth_episode__female_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_05_fifth_episode\synced\synced__sq032_05_fifth_episode__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_05_fifth_episode\synced\synced__sq032_05_fifth_episode__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_05_fifth_episode\synced\synced__sq032_05_fifth_episode__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_05_fifth_episode\synced\synced__sq032_05_fifth_episode__shoping_cart.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_06_sixth_episode\synced\synced__sq032_06_sixth_episode__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_06_sixth_episode\synced\synced__sq032_06_sixth_episode__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_06_sixth_episode\synced\synced__sq032_06_sixth_episode__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_07_finale\sq032_07_finale__dogtag.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_07_finale\sq032_07_finale__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_07_finale\sq032_07_finale__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_07_finale\sq032_07_finale__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\fx\quest\sq032\sq032_vomit.effect` | asset binding .effect | content/basegame_4_gamedata.archive; index evidence only |
| `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq032\phases\sq032_episode_4.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq032\phases\sq032_episode_5.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq032\phases\sq032_finale.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_03_third_episode\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_03_third_episode\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_04_fourth_episode\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_04_fourth_episode\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_05_fifth_episode\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_05_fifth_episode\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_06_sixth_episode\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_06_sixth_episode\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_07_finale\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\lipsync\en\sq032_07_finale\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\side_quests\sq032\scenes\sq032_07_finale.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\archetype\dirt\common\ground\dirt__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bar\generic__stand_bar_lean_back__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bar\generic__stand_bar_lean_right__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\bar\johnny__stand_bar_lean_front__idle__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_back__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_front__sit_around__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_front__sit_around__04.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_front_cigarette__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_front_cigarette__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_front_glasses__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__aggressive__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__aggressive__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground_glasses__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_wall_lean_back__think__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_wall_lean_back_cigarette__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_wall_lean_right__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_wall_lean_right__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\master\master_dirt__stand_wall__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\ground\player__stand_ground_bar__scan__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q101\07c_johnny_triggers\q101_07c__player_crawling_2h_front.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q110\q110_00_e3_demo_intro\johnny__stand_wall_lean_back_glasses__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q110\q110_08\player__lie__unconscious__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_03_third_episode\sq032__johnny__sit_chair_cigarette__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_03_third_episode\sq032__johnny__sit_chair_cigarette__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_03_third_episode\sq032__johnny__stand_rail_lean_back_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_03_third_episode\sq032__player__sit_chair_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_03_third_episode\sq032__player__sit_chair_lean_front__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_04_fourth_episode\sq032__johnny__sit_chair_lean_back__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_04_fourth_episode\sq032__johnny__sit_chair_lean_front__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_04_fourth_episode\sq032__johnny__sit_chair_lean_front__sit_around__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_04_fourth_episode\sq032__johnny__stand_stand_lean_front__watch__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_04_fourth_episode\sq032__player__sit_chair_lean_front__sit_around__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_04_fourth_episode\sq032__player__stand_rail_lean_front__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_05_fifth_episode\sq032__johnny__kneel_ground__kneel_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_05_fifth_episode\sq032__johnny__sit_chair_lean_front_cigarette__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_05_fifth_episode\sq032__johnny__sit_chair_table_lean_back_cigarette__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_05_fifth_episode\sq032__johnny__sit_chair_table_lean_front_cigarette__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_05_fifth_episode\sq032__player__kneel_ground_lean_front__kneel_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_05_fifth_episode\sq032__player__sit_chair_lean_back__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_05_fifth_episode\sq032__player__sit_chair_lean_back_cigarette__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_05_fifth_episode\sq032__player__sit_chair_lean_back_lighter__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_07_finale\sq032__johnny__sit_chair_lean_front__sit_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_07_finale\sq032__johnny__stand_rail_lean_back__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_07_finale\sq032__player__kneel_rail_lean_front__kneel_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_07_finale\sq032__player__lie_ground_lean_right__lie_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_07_finale\sq032__player__sit_ground__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_07_finale\sq032__player__sit_ground_lean_back_dogtag__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\side_quests\sq032\sq032_07_finale\sq032__player__stand_rail_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-635910` | base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 81; 1 total source locations in compressed evidence |
| `censorship_homosexuality` | base\quest\side_quests\sq017\test\sq017_chicken_test.scene / scene / 55; base\quest\side_quests\sq026\definitions\sq026_chicken_test.scene / scene / 468; base\quest\side_quests\sq030\definitions\sq030_chicken_test.scene / scene / 155; 3 total source locations in compressed evidence |
| `glossary_mikoshi` | base\quest\main_quests\part1\q112\scenes\q112_11_shotgun.scene / scene / 1127; 1 total source locations in compressed evidence |
| `johnny_default_on` | base\quest\minor_quests\mq033\mq033_tarot.questphase / h197 / 226; base\quest\minor_quests\mq033\mq033_tarot.questphase / h197 / 227; base\quest\minor_quests\mq033\mq033_tarot.questphase / h197 / 228; base\quest\minor_quests\mq033\mq033_tarot.questphase / h197 / 229; 29 total source locations in compressed evidence |
| `q104_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest / h0 / 9; base\quest\minor_quests\mq001\mq001.quest / h0 / 20; base\quest\minor_quests\mq033\mq033_tarot.quest / h0 / 32; base\quest\main_quests\part1\q104\q104.questphase / h129 / 22; 15 total source locations in compressed evidence |
| `q105_done` | base\quest\minor_quests\mq055\mq055.quest / h37 / 8; base\quest\main_quests\part1\q105\phases\q105_complete.questphase / h0 / 79; base\quest\test\cp77_chicken_test.scene / scene / 789; base\quest\test\cp77_chicken_test.scene / scene / 1375; 8 total source locations in compressed evidence |
| `q112_hanako_meeting_set_up` | base\quest\main_quests\part1\q112\scenes\q112_11_shotgun.scene / scene / 919; base\quest\main_quests\part1\q115\test\q115_00_chickentest.scene / scene / 591; 2 total source locations in compressed evidence |
| `q302_done` | ep1\quest\minor_quests\mq304\test\mq304_chickentest.questphase / h0 / 16; ep1\quest\minor_quests\mq306\mq306.questphase / h201 / 8; ep1\quest\main_quests\q302\phases\q302_08_call.questphase / h0 / 29; ep1\quest\main_quests\q306\q306.quest / h212 / 5; 10 total source locations in compressed evidence |
| `sq032_dbg_mode` | base\quest\side_quests\sq032\test\sq032_chicken_test.scene / scene / 367; 1 total source locations in compressed evidence |
| `sq032_dbg_start` | base\quest\test\coyote_performance.quest / h0 / 9; base\quest\test\farm_bd_perf.quest / h0 / 12; base\quest\test\judy_bd_perf.quest / h0 / 12; base\quest\test\kabuki_performance.quest / h0 / 12; 12 total source locations in compressed evidence |
| `sq032_episode_3_done` | base\quest\minor_quests\mq055\mq055.quest / h37 / 24; ep1\quest\minor_quests\mq306\mq306.quest / h47 / 25; ep1\quest\ep1.questphase / h2539 / 27; ep1\quest\ep1.questphase / h3117 / 27; 4 total source locations in compressed evidence |
| `sq032_episode_4_done` | base\quest\minor_quests\mq055\mq055.quest / h37 / 26; ep1\quest\minor_quests\mq306\mq306.quest / h47 / 27; ep1\quest\ep1.questphase / h2539 / 29; ep1\quest\ep1.questphase / h3117 / 29; 4 total source locations in compressed evidence |
| `sq032_episode_5_done` | base\quest\side_quests\sidequests.questphase / h0 / 193; 1 total source locations in compressed evidence |
| `sq032_q104_prefetch` | base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 85; 1 total source locations in compressed evidence |
| `sq032_q104_ready` | base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 14; base\quest\side_quests\sq032\test\sq032_chicken_test.scene / scene / 352; 2 total source locations in compressed evidence |
| `sq032_q104_used` | base\quest\side_quests\sidequests.questphase / h0 / 194; 1 total source locations in compressed evidence |
| `sq032_q105_prefetch` | base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 83; 1 total source locations in compressed evidence |
| `sq032_q105_ready` | base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 4; base\quest\side_quests\sq032\test\sq032_chicken_test.scene / scene / 350; 2 total source locations in compressed evidence |
| `sq032_q105_used` | base\quest\minor_quests\mq055\mq055.quest / h37 / 25; ep1\quest\minor_quests\mq306\mq306.quest / h47 / 26; ep1\quest\ep1.questphase / h2539 / 28; ep1\quest\ep1.questphase / h3117 / 28; 4 total source locations in compressed evidence |
| `sq032_q110_prefetch` | base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 84; 1 total source locations in compressed evidence |
| `sq032_q110_ready` | base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 11; base\quest\side_quests\sq032\test\sq032_chicken_test.scene / scene / 351; 2 total source locations in compressed evidence |
| `sq032_q110_used` | base\quest\minor_quests\mq055\mq055.quest / h37 / 27; ep1\quest\minor_quests\mq306\mq306.quest / h47 / 28; ep1\quest\ep1.questphase / h2539 / 30; ep1\quest\ep1.questphase / h3117 / 30; 4 total source locations in compressed evidence |
| `sq032_q112_prefetch` | base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 86; 1 total source locations in compressed evidence |
| `sq032_q112_ready` | base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 17; base\quest\side_quests\sq032\test\sq032_chicken_test.scene / scene / 353; 2 total source locations in compressed evidence |
| `sq032_tapeworm_stage` | base\quest\minor_quests\mq055\mq055.quest / h37 / 23; base\quest\main_quests\part1\q105\q105_main.quest / h0 / 59; base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 6; base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase / h0 / 12; 17 total source locations in compressed evidence |
| `sq032_v_wants_the_body` | base\quest\main_quests\part1\q116\test\q116_00_chicken_test.scene / scene / 225; base\quest\main_quests\part1\q116\test\q116_00_chicken_test.scene / scene / 226; 2 total source locations in compressed evidence |

NodeRef uses: 282; TweakDB binding uses: 276. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` | 45 / 357 | scnAudioEvent: 12; scnChangeIdleAnimEvent: 18; scnDialogLineEvent: 83; scnGameplayTransitionEvent: 2; scnIKEvent: 4; scnLookAtAdvancedEvent: 1; scnLookAtEvent: 44; scnOverridePhantomParamsEvent: 5; scnPlaySkAnimEvent: 61; scnUnmountEvent: 2; scneventsAttachPropToPerformer: 10; scneventsAttachPropToWorld: 7; scneventsCameraParamsEvent: 9; scneventsSetAnimFeatureEvent: 2; scneventsSocket: 84; scneventsVFXEvent: 13 |
| `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene` | 70 / 431 | scnAudioEvent: 2; scnChangeIdleAnimEvent: 4; scnDialogLineEvent: 117; scnGameplayTransitionEvent: 6; scnIKEvent: 12; scnLookAtEvent: 61; scnPlaySkAnimEvent: 92; scnUnmountEvent: 6; scneventsAttachPropToPerformer: 4; scneventsAttachPropToWorld: 4; scneventsCameraParamsEvent: 13; scneventsSetAnimFeatureEvent: 6; scneventsSocket: 81; scneventsVFXEvent: 23 |
| `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene` | 53 / 422 | scnAudioEvent: 31; scnChangeIdleAnimEvent: 10; scnDialogLineEvent: 107; scnGameplayTransitionEvent: 2; scnIKEvent: 4; scnLookAtEvent: 26; scnOverridePhantomParamsEvent: 1; scnPlaySkAnimEvent: 81; scnUnmountEvent: 2; scneventsAttachPropToNode: 2; scneventsAttachPropToPerformer: 6; scneventsAttachPropToWorld: 2; scneventsCameraParamsEvent: 5; scneventsEquipItemToPerformer: 11; scneventsSetAnimFeatureEvent: 2; scneventsSocket: 84; scneventsUnequipItemFromPerformer: 10; scneventsUnequipItemFromPerformerByItem: 5; scneventsVFXEvent: 31 |
| `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene` | 15 / 104 | scnAudioEvent: 10; scnChangeIdleAnimEvent: 4; scnDialogLineEvent: 17; scnLookAtEvent: 9; scnPlaySkAnimEvent: 15; scneventsCameraParamsEvent: 10; scneventsSocket: 17; scneventsVFXEvent: 22 |
| `base\quest\side_quests\sq032\scenes\sq032_07_finale.scene` | 68 / 427 | scnAudioEvent: 4; scnChangeIdleAnimEvent: 7; scnDialogLineEvent: 147; scnGameplayTransitionEvent: 9; scnIKEvent: 18; scnLookAtEvent: 27; scnPlaySkAnimEvent: 95; scnUnmountEvent: 9; scneventsAttachPropToPerformer: 4; scneventsAttachPropToWorld: 4; scneventsCameraParamsEvent: 2; scneventsSetAnimFeatureEvent: 9; scneventsSocket: 75; scneventsVFXEvent: 17 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
